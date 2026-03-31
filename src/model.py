"""
EfficientNet-B0 model for crop disease classification.
Supports:
  - Building a fresh model with custom head for num_classes
  - Loading a saved checkpoint
  - Extracting the final feature map layer for Grad-CAM
"""

import torch
import torch.nn as nn
from torchvision import models
from torchvision.models import EfficientNet_B0_Weights


class CropDiseaseModel(nn.Module):
    """
    EfficientNet-B0 backbone with a custom classification head.

    Architecture:
        EfficientNet-B0 (pretrained ImageNet)
            └── features (conv + MBConv blocks)  ← Grad-CAM hooks here
            └── avgpool
            └── classifier
                    Dropout(0.3)
                    Linear(1280 → 512)
                    ReLU
                    Dropout(0.2)
                    Linear(512 → num_classes)
    """

    def __init__(self, num_classes: int, dropout: float = 0.3):
        super().__init__()
        base = models.efficientnet_b0(weights=EfficientNet_B0_Weights.IMAGENET1K_V1)

        # Keep the full feature extractor (all MBConv blocks)
        self.features   = base.features       # output: (B, 1280, H/32, W/32)
        self.avgpool     = base.avgpool        # AdaptiveAvgPool2d → (B, 1280, 1, 1)

        self.classifier  = nn.Sequential(
            nn.Dropout(p=dropout),
            nn.Linear(1280, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.2),
            nn.Linear(512, num_classes),
        )

        # Target layer for Grad-CAM: last conv block inside features
        self.gradcam_layer = self.features[-1]

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


# ── factory helpers ───────────────────────────────────────────────────────────

def build_model(num_classes: int, dropout: float = 0.3) -> CropDiseaseModel:
    """Return a freshly initialised model."""
    return CropDiseaseModel(num_classes=num_classes, dropout=dropout)


def load_model(checkpoint_path: str, num_classes: int,
               device: str = "cpu") -> CropDiseaseModel:
    """
    Load model weights from a saved checkpoint.

    Checkpoint format (saved by train.py):
        {
            "model_state": state_dict,
            "num_classes": int,
            "class_names": list[str],   # optional
        }
    """
    model = build_model(num_classes=num_classes)
    ckpt  = torch.load(checkpoint_path, map_location=device)

    state = ckpt.get("model_state", ckpt)   # handle both formats
    model.load_state_dict(state)
    model.to(device)
    model.eval()
    return model


def get_model_info(model: CropDiseaseModel) -> dict:
    """Return parameter counts and Grad-CAM layer name."""
    total  = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return {
        "total_params":     total,
        "trainable_params": trainable,
        "gradcam_layer":    str(model.gradcam_layer.__class__.__name__),
        "backbone":         "EfficientNet-B0",
    }


# ── freeze / unfreeze helpers (for transfer learning stages) ─────────────────

def freeze_backbone(model: CropDiseaseModel):
    """Freeze all feature extractor weights; only train the head."""
    for param in model.features.parameters():
        param.requires_grad = False


def unfreeze_backbone(model: CropDiseaseModel):
    """Unfreeze all weights for full fine-tuning."""
    for param in model.features.parameters():
        param.requires_grad = True


if __name__ == "__main__":
    m = build_model(num_classes=87)
    info = get_model_info(m)
    print("Model        :", info["backbone"])
    print("Total params :", f"{info['total_params']:,}")
    print("Trainable    :", f"{info['trainable_params']:,}")
    dummy = torch.randn(2, 3, 224, 224)
    out   = m(dummy)
    print("Output shape :", out.shape)   # (2, 87)
