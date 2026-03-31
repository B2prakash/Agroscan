"""
Two-stage training script for CropDiseaseModel (EfficientNet-B0).

Stage 1: Backbone frozen  — 5 epochs,  LR=1e-3  (train head only)
Stage 2: Full fine-tune   — 15 epochs, LR=1e-4  (all layers)

Supports Apple Silicon (MPS), CUDA, and CPU backends.

Usage:
    # Run Stage 1 only, then pause:
    python train.py --data data/merged --epochs_stage1 5 --epochs_stage2 15 --stage 1

    # Resume with Stage 2 after approval:
    python train.py --data data/merged --epochs_stage1 5 --epochs_stage2 15 --stage 2

    # Run both stages without stopping (original behaviour):
    python train.py --data data/merged --epochs_stage1 5 --epochs_stage2 15

Outputs:
    models/best_model.pth       — best checkpoint (val accuracy)
    models/class_names.json     — ordered class list
    models/stage1_history.json  — Stage 1 metrics (used when resuming Stage 2)
    models/training_curves.png  — loss/accuracy plots
"""

import argparse
import json
import os
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.optim import Adam
from torch.optim.lr_scheduler import CosineAnnealingLR

from src.model import build_model, freeze_backbone, unfreeze_backbone
from src.utils import get_dataloaders, compute_class_weights, load_class_names


# ── Device selection ──────────────────────────────────────────────────────────

def get_device() -> torch.device:
    if torch.cuda.is_available():
        dev = torch.device("cuda")
    elif torch.backends.mps.is_available():
        dev = torch.device("mps")
    else:
        dev = torch.device("cpu")
    print(f"Using device: {dev}")
    return dev


# ── Early stopping ────────────────────────────────────────────────────────────

class EarlyStopping:
    def __init__(self, patience: int = 5, delta: float = 1e-4):
        self.patience  = patience
        self.delta     = delta
        self.best_val  = 0.0
        self.counter   = 0
        self.triggered = False

    def step(self, val_acc: float) -> bool:
        """Returns True if training should stop."""
        if val_acc > self.best_val + self.delta:
            self.best_val = val_acc
            self.counter  = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                self.triggered = True
        return self.triggered


# ── One epoch ────────────────────────────────────────────────────────────────

def run_epoch(
    model: nn.Module,
    loader,
    criterion: nn.Module,
    optimizer,
    device: torch.device,
    train: bool,
) -> tuple[float, float]:
    """Returns (avg_loss, accuracy)."""
    model.train(train)
    total_loss = 0.0
    correct    = 0
    total      = 0

    with torch.set_grad_enabled(train):
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)

            logits = model(images)
            loss   = criterion(logits, labels)

            if train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            total_loss += loss.item() * images.size(0)
            correct    += (logits.argmax(dim=1) == labels).sum().item()
            total      += images.size(0)

    return total_loss / total, correct / total


# ── Training stage ────────────────────────────────────────────────────────────

def train_stage(
    stage_name: str,
    model: nn.Module,
    loaders: dict,
    criterion: nn.Module,
    optimizer,
    scheduler,
    device: torch.device,
    num_epochs: int,
    early_stopping: EarlyStopping,
    models_dir: Path,
    history: dict,
) -> float:
    """
    Train for num_epochs; save best checkpoint; return best val accuracy.
    """
    best_val_acc = 0.0

    for epoch in range(1, num_epochs + 1):
        t0 = time.time()

        train_loss, train_acc = run_epoch(
            model, loaders["train"], criterion, optimizer, device, train=True
        )
        val_loss, val_acc = run_epoch(
            model, loaders["val"], criterion, optimizer, device, train=False
        )

        if scheduler is not None:
            scheduler.step()

        elapsed = time.time() - t0
        lr_now  = optimizer.param_groups[0]["lr"]

        print(
            f"[{stage_name}] Epoch {epoch:3d}/{num_epochs} | "
            f"Train loss={train_loss:.4f} acc={train_acc:.4f} | "
            f"Val   loss={val_loss:.4f} acc={val_acc:.4f} | "
            f"LR={lr_now:.2e} | {elapsed:.1f}s"
        )

        history["train_loss"].append(train_loss)
        history["train_acc"].append(train_acc)
        history["val_loss"].append(val_loss)
        history["val_acc"].append(val_acc)

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(
                {
                    "epoch":      epoch,
                    "stage":      stage_name,
                    "model_state_dict":     model.state_dict(),
                    "optimizer_state_dict": optimizer.state_dict(),
                    "val_acc":    val_acc,
                    "val_loss":   val_loss,
                },
                models_dir / "best_model.pth",
            )
            print(f"  → Saved best model (val_acc={val_acc:.4f})")

        if early_stopping.step(val_acc):
            print(f"  → Early stopping triggered after epoch {epoch}.")
            break

    return best_val_acc


# ── Plotting ──────────────────────────────────────────────────────────────────

def plot_training_curves(history: dict, out_path: Path, stage1_len: int):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    epochs = range(1, len(history["train_loss"]) + 1)

    # Loss
    ax1.plot(epochs, history["train_loss"], label="Train loss")
    ax1.plot(epochs, history["val_loss"],   label="Val loss")
    ax1.axvline(x=stage1_len + 0.5, color="gray", linestyle="--", alpha=0.5,
                label="Stage 1/2 boundary")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Loss")
    ax1.set_title("Training & Validation Loss")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Accuracy
    ax2.plot(epochs, history["train_acc"], label="Train acc")
    ax2.plot(epochs, history["val_acc"],   label="Val acc")
    ax2.axvline(x=stage1_len + 0.5, color="gray", linestyle="--", alpha=0.5,
                label="Stage 1/2 boundary")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Accuracy")
    ax2.set_title("Training & Validation Accuracy")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Training curves saved to {out_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Train CropDiseaseModel")
    parser.add_argument("--data",           default="data/merged",
                        help="Path to merged data root (train/val/test subdirs)")
    parser.add_argument("--epochs_stage1",  type=int, default=5,
                        help="Epochs with backbone frozen (Stage 1)")
    parser.add_argument("--epochs_stage2",  type=int, default=15,
                        help="Epochs with full fine-tune (Stage 2)")
    parser.add_argument("--batch_size",     type=int, default=32)
    parser.add_argument("--num_workers",    type=int, default=4)
    parser.add_argument("--lr_stage1",      type=float, default=1e-3)
    parser.add_argument("--lr_stage2",      type=float, default=1e-4)
    parser.add_argument("--patience",       type=int, default=5,
                        help="Early stopping patience (per stage)")
    parser.add_argument("--models_dir",     default="models")
    parser.add_argument("--stage",          choices=["1", "2", "both"], default="both",
                        help="'1' = Stage 1 only; '2' = Stage 2 only (resumes from "
                             "best_model.pth); 'both' = run both in sequence (default)")
    args = parser.parse_args()

    # ── Setup ─────────────────────────────────────────────────────────────────
    device     = get_device()
    models_dir = Path(args.models_dir)
    models_dir.mkdir(parents=True, exist_ok=True)

    run_stage1 = args.stage in ("1", "both")
    run_stage2 = args.stage in ("2", "both")

    # ── Data ──────────────────────────────────────────────────────────────────
    print(f"\nLoading data from: {args.data}")
    loaders = get_dataloaders(
        data_root   = args.data,
        batch_size  = args.batch_size,
        num_workers = args.num_workers,
        splits      = ("train", "val"),
    )

    # ── Class names ───────────────────────────────────────────────────────────
    class_names_path = models_dir / "class_names.json"
    if run_stage1:
        class_names = load_class_names(args.data, "train")
        with open(class_names_path, "w") as f:
            json.dump(class_names, f, indent=2)
        print(f"Classes: {len(class_names)}  (saved to {class_names_path})")
    else:
        # Stage 2 resume — load from saved file
        if not class_names_path.exists():
            raise FileNotFoundError(
                f"class_names.json not found at {class_names_path}. "
                "Run Stage 1 first."
            )
        with open(class_names_path) as f:
            class_names = json.load(f)
        print(f"Classes: {len(class_names)}  (loaded from {class_names_path})")

    num_classes = len(class_names)

    # ── Loss with class weights ───────────────────────────────────────────────
    print("\nComputing class weights...")
    weights   = compute_class_weights(args.data, split="train", device=str(device))
    criterion = nn.CrossEntropyLoss(weight=weights)

    # ── Model ─────────────────────────────────────────────────────────────────
    model = build_model(num_classes=num_classes).to(device)

    if not run_stage1:
        # Stage 2 resume — load best checkpoint from Stage 1
        ckpt_path = models_dir / "best_model.pth"
        if not ckpt_path.exists():
            raise FileNotFoundError(
                f"Checkpoint not found at {ckpt_path}. Run Stage 1 first."
            )
        ckpt = torch.load(ckpt_path, map_location=device)
        model.load_state_dict(ckpt["model_state_dict"])
        print(f"Loaded Stage 1 checkpoint (val_acc={ckpt.get('val_acc', '?'):.4f})")

    # ── History ───────────────────────────────────────────────────────────────
    history = {
        "train_loss": [], "train_acc": [],
        "val_loss":   [], "val_acc":   [],
    }
    stage1_history_path = models_dir / "stage1_history.json"

    # ════════════════════════════════════════════════════════════════════════
    # Stage 1 — frozen backbone, train head only
    # ════════════════════════════════════════════════════════════════════════
    if run_stage1:
        print(f"\n{'='*60}")
        print(f"Stage 1: Backbone frozen — {args.epochs_stage1} epochs, LR={args.lr_stage1}")
        print(f"{'='*60}")

        freeze_backbone(model)

        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(f"Trainable parameters: {trainable_params:,}")

        optimizer1  = Adam(filter(lambda p: p.requires_grad, model.parameters()),
                           lr=args.lr_stage1)
        scheduler1  = CosineAnnealingLR(optimizer1, T_max=args.epochs_stage1, eta_min=1e-5)
        early_stop1 = EarlyStopping(patience=args.patience)

        best1 = train_stage(
            stage_name     = "Stage1",
            model          = model,
            loaders        = loaders,
            criterion      = criterion,
            optimizer      = optimizer1,
            scheduler      = scheduler1,
            device         = device,
            num_epochs     = args.epochs_stage1,
            early_stopping = early_stop1,
            models_dir     = models_dir,
            history        = history,
        )
        stage1_actual_len = len(history["train_loss"])

        # Persist Stage 1 metrics so Stage 2 can load them for combined plotting
        with open(stage1_history_path, "w") as f:
            json.dump({"history": history, "stage1_len": stage1_actual_len,
                       "best_val_acc": best1}, f, indent=2)

        print(f"\n{'='*60}")
        print(f"  STAGE 1 COMPLETE")
        print(f"  Best val accuracy : {best1:.4f}")
        print(f"  Checkpoint        : {models_dir / 'best_model.pth'}")
        print(f"  History saved     : {stage1_history_path}")
        print(f"{'='*60}")

        if args.stage == "1":
            print("\nStage 1 done. Waiting for your go-ahead before Stage 2.")
            print("When ready, run:")
            print(f"  python train.py --data {args.data} "
                  f"--epochs_stage1 {args.epochs_stage1} "
                  f"--epochs_stage2 {args.epochs_stage2} --stage 2")
            return   # Stop here — user must approve Stage 2

    # ════════════════════════════════════════════════════════════════════════
    # Stage 2 — full fine-tune (all layers)
    # ════════════════════════════════════════════════════════════════════════
    if run_stage2:
        # If we only ran Stage 2, prepend Stage 1 history for combined plot
        if not run_stage1 and stage1_history_path.exists():
            with open(stage1_history_path) as f:
                s1_data = json.load(f)
            s1_hist          = s1_data["history"]
            stage1_actual_len = s1_data["stage1_len"]
            best1             = s1_data["best_val_acc"]
            for key in history:
                history[key] = s1_hist[key] + history[key]
            print(f"Loaded Stage 1 history ({stage1_actual_len} epochs) for combined plot.")
        elif not run_stage1:
            stage1_actual_len = 0
            best1             = 0.0

        print(f"\n{'='*60}")
        print(f"Stage 2: Full fine-tune — {args.epochs_stage2} epochs, LR={args.lr_stage2}")
        print(f"{'='*60}")

        unfreeze_backbone(model)

        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(f"Trainable parameters: {trainable_params:,}")

        optimizer2  = Adam(model.parameters(), lr=args.lr_stage2)
        scheduler2  = CosineAnnealingLR(optimizer2, T_max=args.epochs_stage2, eta_min=1e-6)
        early_stop2 = EarlyStopping(patience=args.patience)

        best2 = train_stage(
            stage_name     = "Stage2",
            model          = model,
            loaders        = loaders,
            criterion      = criterion,
            optimizer      = optimizer2,
            scheduler      = scheduler2,
            device         = device,
            num_epochs     = args.epochs_stage2,
            early_stopping = early_stop2,
            models_dir     = models_dir,
            history        = history,
        )
        print(f"\nStage 2 complete. Best val accuracy: {best2:.4f}")

        # ── Final summary ─────────────────────────────────────────────────────
        overall_best = max(best1, best2) if run_stage1 else best2
        print(f"\n{'='*60}")
        print(f"Training complete.")
        print(f"Overall best val accuracy: {overall_best:.4f}")
        print(f"Best model saved to: {models_dir / 'best_model.pth'}")
        print(f"{'='*60}")

        plot_training_curves(
            history      = history,
            out_path     = models_dir / "training_curves.png",
            stage1_len   = stage1_actual_len,
        )


if __name__ == "__main__":
    main()
