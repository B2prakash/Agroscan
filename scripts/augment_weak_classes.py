"""
Augment weak classes in data/merged/ up to TARGET images (in train split only).
Val and test are left untouched — augmentation only goes into train.
"""

import os
import random
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

MERGED_TRAIN = Path("/Users/vedprakash/Downloads/crop-disease-detector/data/merged/train")
TARGET       = 300
IMG_EXTS     = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

WEAK_CLASSES = [
    "cauliflower_healthy",
    "cauliflower_downy_mildew",
    "cauliflower_bacterial_spot_rot",
    "chilli_yellowish",
    "potato_healthy",
]

random.seed(42)

# ── augmentation ──────────────────────────────────────────────────────────────

def _h_flip(img):  return img.transpose(Image.FLIP_LEFT_RIGHT)
def _rotate(img):  return img.rotate(random.uniform(-30, 30), resample=Image.BILINEAR)
def _bright(img):  return ImageEnhance.Brightness(img).enhance(random.uniform(0.6, 1.4))
def _zoom(img):
    f = random.uniform(0.80, 0.95)
    w, h = img.size
    l, t = int(w*(1-f)/2), int(h*(1-f)/2)
    return img.crop((l, t, w-l, h-t)).resize((w, h), Image.BILINEAR)
def _blur(img):    return img.filter(ImageFilter.GaussianBlur(random.uniform(0.5, 1.5)))

AUG_FNS = [_h_flip, _rotate, _bright, _zoom, _blur]

def augment_one(img):
    for fn in random.sample(AUG_FNS, k=random.randint(2, 4)):
        img = fn(img)
    return img


def augment_class(cls_name: str):
    cls_dir = MERGED_TRAIN / cls_name
    if not cls_dir.exists():
        print(f"  [WARN] {cls_name}: folder not found in train — skipping")
        return

    originals = [p for p in cls_dir.iterdir()
                 if p.is_file() and p.suffix.lower() in IMG_EXTS]
    current   = len(originals)
    needed    = max(0, TARGET - current)

    if needed == 0:
        print(f"  {cls_name}: already {current} images — no augmentation needed")
        return

    print(f"  {cls_name}: {current} → need {needed} more")
    generated = 0
    while generated < needed:
        src = random.choice(originals)
        try:
            img = Image.open(src).convert("RGB")
        except Exception:
            continue
        aug = augment_one(img)
        out_name = f"{cls_name}_aug_{generated:04d}.jpg"
        aug.save(cls_dir / out_name, quality=90)
        generated += 1

    final = len([p for p in cls_dir.iterdir()
                 if p.is_file() and p.suffix.lower() in IMG_EXTS])
    print(f"    → added {generated} images  |  train total now: {final}")


def main():
    print("=== Augmenting weak classes in merged/train ===\n")
    for cls in WEAK_CLASSES:
        augment_class(cls)
    print("\nDone.")


if __name__ == "__main__":
    main()
