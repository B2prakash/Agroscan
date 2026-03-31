"""
Preprocessing utilities for crop disease detection.

Provides:
  - get_transforms()        training and inference transforms
  - preprocess_image()      single PIL/path → tensor for inference
  - CropDiseaseDataset      PyTorch Dataset for the merged folder layout
  - get_dataloaders()       returns train / val / test DataLoaders
  - load_class_names()      reads class list from merged directory
  - compute_class_weights() for imbalanced training loss
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional

import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms, datasets
from PIL import Image


# ── constants ─────────────────────────────────────────────────────────────────

IMAGE_SIZE  = 224          # EfficientNet-B0 default input
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD  = [0.229, 0.224, 0.225]


# ── transforms ────────────────────────────────────────────────────────────────

def get_transforms(split: str = "train") -> transforms.Compose:
    """
    Return torchvision transforms for a given split.

    train:  augmentation + normalize
    val / test / inference: resize + center-crop + normalize only
    """
    if split == "train":
        return transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.RandomCrop(IMAGE_SIZE),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomVerticalFlip(p=0.2),
            transforms.ColorJitter(
                brightness=0.3, contrast=0.3,
                saturation=0.3, hue=0.05
            ),
            transforms.RandomRotation(degrees=20),
            transforms.RandomGrayscale(p=0.02),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ])
    else:
        return transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.CenterCrop(IMAGE_SIZE),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ])


# ── inference preprocessing ───────────────────────────────────────────────────

def preprocess_image(image_input, device: str = "cpu") -> torch.Tensor:
    """
    Accept a file path (str/Path) or a PIL Image and return
    a normalised (1, 3, 224, 224) tensor ready for model inference.
    """
    if isinstance(image_input, (str, Path)):
        img = Image.open(image_input).convert("RGB")
    elif isinstance(image_input, Image.Image):
        img = image_input.convert("RGB")
    else:
        raise TypeError(f"Unsupported image type: {type(image_input)}")

    tfm    = get_transforms("val")
    tensor = tfm(img).unsqueeze(0).to(device)   # (1, 3, 224, 224)
    return tensor


def tensor_to_numpy(tensor: torch.Tensor):
    """Convert a (C, H, W) or (1, C, H, W) normalised tensor back to HWC uint8."""
    import numpy as np
    if tensor.dim() == 4:
        tensor = tensor.squeeze(0)
    mean = torch.tensor(IMAGENET_MEAN).view(3, 1, 1)
    std  = torch.tensor(IMAGENET_STD).view(3, 1, 1)
    img  = tensor.cpu() * std + mean
    img  = img.clamp(0, 1).permute(1, 2, 0).numpy()
    return (img * 255).astype("uint8")


# ── dataset & dataloaders ─────────────────────────────────────────────────────

class CropDiseaseDataset(Dataset):
    """
    Wraps torchvision.datasets.ImageFolder.
    Folder layout expected:
        root/
          train/<classname>/*.jpg
          val/<classname>/*.jpg
          test/<classname>/*.jpg
    """

    def __init__(self, root: str, split: str = "train"):
        split_dir = os.path.join(root, split)
        if not os.path.isdir(split_dir):
            raise FileNotFoundError(f"Split directory not found: {split_dir}")
        self._ds = datasets.ImageFolder(
            root=split_dir,
            transform=get_transforms(split),
        )
        self.classes    = self._ds.classes
        self.class_to_idx = self._ds.class_to_idx

    def __len__(self):
        return len(self._ds)

    def __getitem__(self, idx):
        return self._ds[idx]


def get_dataloaders(
    data_root: str,
    batch_size: int = 32,
    num_workers: int = 4,
    splits: Tuple[str, ...] = ("train", "val", "test"),
) -> Dict[str, DataLoader]:
    """
    Build and return a dict of DataLoaders for the requested splits.
    """
    loaders = {}
    for split in splits:
        dataset = CropDiseaseDataset(root=data_root, split=split)
        shuffle = (split == "train")
        loaders[split] = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=shuffle,
            num_workers=num_workers,
            pin_memory=torch.cuda.is_available(),
            drop_last=(split == "train"),
        )
    return loaders


# ── class name helpers ────────────────────────────────────────────────────────

def load_class_names(data_root: str, split: str = "train") -> List[str]:
    """
    Return sorted list of class names by reading subfolder names in split dir.
    """
    split_dir = Path(data_root) / split
    names = sorted(
        d.name for d in split_dir.iterdir()
        if d.is_dir()
    )
    return names


def save_class_names(class_names: List[str], out_path: str):
    """Save class list (one per line) to a text file."""
    with open(out_path, "w") as f:
        for name in class_names:
            f.write(name + "\n")


def read_class_names(path: str) -> List[str]:
    """Load class list from a text file produced by save_class_names."""
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


# ── class weights for imbalanced training ────────────────────────────────────

def compute_class_weights(
    data_root: str,
    split: str = "train",
    device: str = "cpu",
) -> torch.Tensor:
    """
    Compute inverse-frequency class weights for CrossEntropyLoss.

    Returns a tensor of shape (num_classes,) on `device`.
    """
    split_dir = Path(data_root) / split
    class_names = load_class_names(data_root, split)

    counts = []
    for cls in class_names:
        cls_dir = split_dir / cls
        n = sum(
            1 for f in cls_dir.iterdir()
            if f.is_file() and f.suffix.lower() in
            {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}
        )
        counts.append(max(n, 1))

    counts_t = torch.tensor(counts, dtype=torch.float)
    weights  = 1.0 / counts_t
    weights  = weights / weights.sum() * len(counts_t)   # normalise
    return weights.to(device)


if __name__ == "__main__":
    DATA = "/Users/vedprakash/Downloads/crop-disease-detector/data/merged"
    names = load_class_names(DATA, "train")
    print(f"Classes found: {len(names)}")
    print("First 5 :", names[:5])
    print("Last  5 :", names[-5:])

    tensor = preprocess_image(
        next((Path(DATA) / "train" / names[0]).iterdir())
    )
    print("Inference tensor shape:", tensor.shape)
