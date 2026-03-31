"""
Dataset Merger
Merges PlantVillage (color), Rice Leaf, Wheat, and Multi-Crop (classification)
into ./data/merged/  with train / val / test splits (80/10/10).

Rules applied:
  - All class names normalized to lowercase_with_underscores
  - Classes with > 1000 images capped at 1000 (random sample)
  - Classes with < 100 images augmented up to 300
  - Final split: 80% train / 10% val / 10% test
"""

import os
import re
import shutil
import random
import math
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

# ── config ────────────────────────────────────────────────────────────────────
BASE  = Path("/Users/vedprakash/Downloads/crop-disease-detector/data")
OUT   = BASE / "merged"
SEED  = 42
CAP   = 1000
WEAK_THRESHOLD = 100
WEAK_TARGET    = 300
TRAIN_RATIO    = 0.80
VAL_RATIO      = 0.10
# TEST_RATIO   = 0.10  (remainder)

IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

random.seed(SEED)


# ── name normalizer ───────────────────────────────────────────────────────────

def normalize(name: str) -> str:
    """Convert any raw folder name to lowercase_with_underscores."""
    s = name.strip()
    # strip dataset split suffixes from wheat
    s = re.sub(r'_(valid|test)$', '', s, flags=re.IGNORECASE)
    # PlantVillage triple-underscore separator → single _
    s = s.replace("___", "_")
    # parentheses, commas, periods → nothing
    s = re.sub(r'[(),.]', '', s)
    # spaces, hyphens, forward-slashes → _
    s = re.sub(r'[\s\-/]+', '_', s)
    # collapse multiple underscores
    s = re.sub(r'_+', '_', s)
    # lowercase and strip edge underscores
    s = s.lower().strip('_')
    return s


# ── augmentation helpers ──────────────────────────────────────────────────────

def _h_flip(img):   return img.transpose(Image.FLIP_LEFT_RIGHT)
def _rotate(img):   return img.rotate(random.uniform(-30, 30), resample=Image.BILINEAR)
def _bright(img):   return ImageEnhance.Brightness(img).enhance(random.uniform(0.6, 1.4))
def _zoom(img):
    f = random.uniform(0.80, 0.95)
    w, h = img.size
    l, t = int(w*(1-f)/2), int(h*(1-f)/2)
    return img.crop((l, t, w-l, h-t)).resize((w, h), Image.BILINEAR)
def _blur(img):     return img.filter(ImageFilter.GaussianBlur(random.uniform(0.5, 1.5)))

AUG_FNS = [_h_flip, _rotate, _bright, _zoom, _blur]

def augment_one(img):
    for fn in random.sample(AUG_FNS, k=random.randint(2, 4)):
        img = fn(img)
    return img


def augment_to_target(paths: list, target: int) -> list:
    """
    Returns a list of (PIL.Image, suggested_stem) tuples covering
    the original paths + enough augmented copies to reach `target`.
    Originals are returned as file paths; augmented as PIL Images.
    """
    result_paths = list(paths)          # originals stay as paths
    aug_images   = []                   # (PIL.Image, stem)
    needed = target - len(paths)
    idx = 0
    while idx < needed:
        src = random.choice(paths)
        try:
            img = Image.open(src).convert("RGB")
        except Exception:
            continue
        aug_images.append((augment_one(img), f"aug_{idx:04d}"))
        idx += 1
    return result_paths, aug_images


# ── image collection ──────────────────────────────────────────────────────────

def collect_folder(folder: Path) -> list:
    """Return list of all image paths directly inside a folder."""
    return [
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in IMG_EXTS
    ]


# ── source definitions ────────────────────────────────────────────────────────
# Each source is a dict:
#   "root"   : Path  — parent directory containing class subfolders
#   "splits" : list  — subfolder names inside root that hold class dirs
#                      (use ["."] for flat root/classname layout)

SOURCES = [
    # PlantVillage — color only, no pre-existing splits
    {
        "name":   "plantvillage",
        "root":   BASE / "plantvillage dataset" / "color",
        "splits": ["."],
    },
    # Rice — no pre-existing splits (already augmented)
    {
        "name":   "rice",
        "root":   BASE / "rice_leaf_diseases",
        "splits": ["."],
    },
    # Wheat — has train / valid / test splits
    {
        "name":   "wheat",
        "root":   BASE / "wheat_dataset",
        "splits": ["train", "valid", "test"],
    },
    # Multi-Crop classification — has train / valid / test
    {
        "name":   "multicrop",
        "root":   BASE / "multicrop_classification",
        "splits": ["train", "valid", "test"],
    },
]


def gather_all() -> dict:
    """
    Walk every source and return:
      { normalized_class_name : [path, path, ...] }
    """
    class_map = {}

    for src in SOURCES:
        root = src["root"]
        for split in src["splits"]:
            split_dir = root if split == "." else root / split
            if not split_dir.is_dir():
                print(f"  [WARN] missing dir: {split_dir}")
                continue
            for cls_dir in sorted(split_dir.iterdir()):
                if not cls_dir.is_dir():
                    continue
                norm = normalize(cls_dir.name)
                imgs = collect_folder(cls_dir)
                if not imgs:
                    continue
                class_map.setdefault(norm, []).extend(imgs)

    return class_map


# ── copy / save helpers ───────────────────────────────────────────────────────

def save_path_image(src_path: Path, dst_path: Path):
    shutil.copy2(src_path, dst_path)


def save_pil_image(img: Image.Image, dst_path: Path):
    img.save(dst_path, quality=90)


# ── main merge ────────────────────────────────────────────────────────────────

def main():
    print("=== Dataset Merger ===\n")

    # 1. Gather all images per normalized class
    print("Step 1/4  Gathering images from all sources ...")
    class_map = gather_all()
    print(f"          Found {len(class_map)} unique classes before filtering.\n")

    # 2. Cap, augment, deduplicate paths (avoid exact same path twice)
    print("Step 2/4  Applying cap (≤1000) and weak-class augmentation (→300) ...")
    final_class_map = {}   # norm_name → { "paths": [...], "aug": [(PIL, stem)] }
    aug_log   = []
    cap_log   = []

    for cls, paths in sorted(class_map.items()):
        # deduplicate by string
        paths = list(dict.fromkeys(str(p) for p in paths))
        paths = [Path(p) for p in paths]
        random.shuffle(paths)

        aug_images = []

        if len(paths) < WEAK_THRESHOLD:
            orig_n = len(paths)
            paths, aug_images = augment_to_target(paths, WEAK_TARGET)
            aug_log.append(f"  {cls}: {orig_n} → {len(paths)+len(aug_images)} (augmented)")

        if len(paths) > CAP:
            paths = paths[:CAP]
            cap_log.append(f"  {cls}: capped at {CAP}")

        final_class_map[cls] = {"paths": paths, "aug": aug_images}

    if cap_log:
        print("  Capped classes:")
        for l in cap_log: print(l)
    if aug_log:
        print("  Augmented weak classes:")
        for l in aug_log: print(l)
    print()

    # 3. Split each class 80/10/10 and write to disk
    print("Step 3/4  Splitting and writing to disk ...")
    for split in ("train", "val", "test"):
        (OUT / split).mkdir(parents=True, exist_ok=True)

    total_written = {"train": 0, "val": 0, "test": 0}
    class_totals  = {}

    for cls, data in sorted(final_class_map.items()):
        paths     = data["paths"]
        aug_imgs  = data["aug"]
        all_items = [("path", p) for p in paths] + [("pil", item) for item in aug_imgs]
        random.shuffle(all_items)

        n     = len(all_items)
        n_tr  = math.ceil(n * TRAIN_RATIO)
        n_val = math.ceil(n * VAL_RATIO)
        # remainder goes to test
        splits_items = {
            "train": all_items[:n_tr],
            "val":   all_items[n_tr : n_tr + n_val],
            "test":  all_items[n_tr + n_val :],
        }

        cls_total = 0
        for split, items in splits_items.items():
            dst_dir = OUT / split / cls
            dst_dir.mkdir(parents=True, exist_ok=True)

            for i, (kind, item) in enumerate(items):
                if kind == "path":
                    ext      = item.suffix.lower() if item.suffix else ".jpg"
                    dst_name = f"{cls}_{split}_{i:05d}{ext}"
                    save_path_image(item, dst_dir / dst_name)
                else:
                    pil_img, stem = item
                    dst_name = f"{cls}_{split}_{stem}.jpg"
                    save_pil_image(pil_img, dst_dir / dst_name)

                total_written[split] += 1
                cls_total += 1

        class_totals[cls] = cls_total

    print(f"  Done writing.\n")

    # 4. Summary
    print("Step 4/4  Computing summary ...\n")

    print("=" * 55)
    print("  MERGE SUMMARY")
    print("=" * 55)
    print(f"  Total classes      : {len(class_totals)}")
    print(f"  Train images       : {total_written['train']:>7,}")
    print(f"  Val   images       : {total_written['val']:>7,}")
    print(f"  Test  images       : {total_written['test']:>7,}")
    print(f"  TOTAL              : {sum(total_written.values()):>7,}")
    print()

    sorted_cls = sorted(class_totals.items(), key=lambda x: x[1], reverse=True)
    print("  Top 5 LARGEST classes:")
    for cls, n in sorted_cls[:5]:
        print(f"    {cls:<45} {n:>5}")
    print()
    print("  Top 5 SMALLEST classes:")
    for cls, n in sorted_cls[-5:]:
        print(f"    {cls:<45} {n:>5}")
    print("=" * 55)

    # Full class list to file for reference
    summary_path = OUT / "class_summary.txt"
    with open(summary_path, "w") as f:
        f.write(f"Total classes: {len(class_totals)}\n")
        f.write(f"Train: {total_written['train']}  Val: {total_written['val']}  Test: {total_written['test']}\n\n")
        f.write(f"{'Class':<50} {'Total':>6}  {'Train':>6}  {'Val':>5}  {'Test':>5}\n")
        f.write("-" * 80 + "\n")
        for i, (cls, _) in enumerate(sorted_cls):
            tr = len(list((OUT / "train" / cls).iterdir())) if (OUT / "train" / cls).exists() else 0
            va = len(list((OUT / "val"   / cls).iterdir())) if (OUT / "val"   / cls).exists() else 0
            te = len(list((OUT / "test"  / cls).iterdir())) if (OUT / "test"  / cls).exists() else 0
            f.write(f"{cls:<50} {tr+va+te:>6}  {tr:>6}  {va:>5}  {te:>5}\n")
    print(f"\n  Full class list saved → {summary_path}")


if __name__ == "__main__":
    main()
