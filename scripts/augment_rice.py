"""
Rice Leaf Disease Augmentation
Goal: bring each class from ~40 images to >= 500
Techniques: horizontal flip, rotation, brightness, zoom, blur
Saves augmented images back into the same class folders.
"""

import os
import random
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

RICE_ROOT   = "/Users/vedprakash/Downloads/crop-disease-detector/data/rice_leaf_diseases"
TARGET      = 500
IMG_EXTS    = {'.jpg', '.jpeg', '.png'}
random.seed(42)
np.random.seed(42)


def horizontal_flip(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def rotate(img):
    angle = random.uniform(-30, 30)
    return img.rotate(angle, resample=Image.BILINEAR, expand=False)


def brightness(img):
    factor = random.uniform(0.6, 1.4)
    return ImageEnhance.Brightness(img).enhance(factor)


def zoom(img):
    factor = random.uniform(0.80, 0.95)   # crop then resize back
    w, h = img.size
    left   = int(w * (1 - factor) / 2)
    top    = int(h * (1 - factor) / 2)
    right  = w - left
    bottom = h - top
    return img.crop((left, top, right, bottom)).resize((w, h), Image.BILINEAR)


def blur(img):
    radius = random.uniform(0.5, 1.5)
    return img.filter(ImageFilter.GaussianBlur(radius=radius))


# Pool of augmentation functions – applied in random combinations
AUG_FNS = [horizontal_flip, rotate, brightness, zoom, blur]


def augment_one(img):
    """Apply 2-4 random augmentations to a single image."""
    fns = random.sample(AUG_FNS, k=random.randint(2, 4))
    for fn in fns:
        img = fn(img)
    return img


def collect_images(folder):
    paths = []
    for f in os.listdir(folder):
        if os.path.splitext(f)[1].lower() in IMG_EXTS:
            paths.append(os.path.join(folder, f))
    return paths


def augment_class(class_dir):
    originals = collect_images(class_dir)
    current   = len(originals)
    needed    = max(0, TARGET - current)
    print(f"  {os.path.basename(class_dir)}: {current} originals → need {needed} more")

    generated = 0
    while generated < needed:
        src_path = random.choice(originals)
        try:
            img = Image.open(src_path).convert("RGB")
        except Exception:
            continue

        aug_img  = augment_one(img)
        stem     = os.path.splitext(os.path.basename(src_path))[0]
        out_name = f"aug_{generated:04d}_{stem}.jpg"
        out_path = os.path.join(class_dir, out_name)
        aug_img.save(out_path, quality=90)
        generated += 1

    final = len(collect_images(class_dir))
    print(f"    → saved {generated} augmented images  |  total now: {final}")
    return final


def main():
    print("=== Rice Leaf Disease Augmentation ===\n")
    totals = {}
    for cls in sorted(os.listdir(RICE_ROOT)):
        cls_dir = os.path.join(RICE_ROOT, cls)
        if not os.path.isdir(cls_dir):
            continue
        final = augment_class(cls_dir)
        totals[cls] = final

    print("\n--- Final counts ---")
    for cls, n in totals.items():
        status = "OK" if n >= TARGET else f"WARN: only {n}"
        print(f"  {cls}: {n}  [{status}]")


if __name__ == "__main__":
    main()
