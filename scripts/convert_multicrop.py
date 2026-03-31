"""
Multi-Crop YOLO → Classification Converter
Reads YOLO bounding-box labels, crops each detection from the image,
and saves cropped patches into per-class folders preserving train/valid/test splits.

Output layout:
  data/multicrop_classification/
      train/<classname>/  *.jpg
      valid/<classname>/  *.jpg
      test/<classname>/   *.jpg
"""

import os
import cv2

# ── paths ────────────────────────────────────────────────────────────────────
YOLO_ROOT = (
    "/Users/vedprakash/Downloads/crop-disease-detector/data"
    "/Multi-Crop Disease Dataset/Multicrop Disease Dataset"
    "/Multicrop Disease Dataset"
)
OUT_ROOT = (
    "/Users/vedprakash/Downloads/crop-disease-detector/data"
    "/multicrop_classification"
)

# class names from data.yaml (index → name)
CLASS_NAMES = [
    "banana_bract_mosaic_virus",   # 0
    "banana_cordana",              # 1
    "banana_healthy",              # 2
    "banana_insectpest",           # 3
    "banana_moko",                 # 4
    "banana_panama",               # 5
    "banana_pestalotiopsis",       # 6
    "banana_sigatoka",             # 7
    "banana_yb_sigatoka",          # 8
    "cauliflower_Blackrot",        # 9
    "cauliflower_bacterial_spot_rot",  # 10
    "cauliflower_downy_mildew",    # 11
    "cauliflower_healthy",         # 12
    "chilli_anthracnose",          # 13
    "chilli_healthy",              # 14
    "chilli_leafcurl",             # 15
    "chilli_leafspot",             # 16
    "chilli_whitefly",             # 17
    "chilli_yellowish",            # 18
    "groundnut_early_leaf_spot",   # 19
    "groundnut_early_rust",        # 20
    "groundnut_healthy",           # 21
    "groundnut_late_leaf_spot",    # 22
    "groundnut_nutrition_deficiency",  # 23
    "groundnut_rust",              # 24
    "radish_black_leaf_spot",      # 25
    "radish_downey_mildew",        # 26
    "radish_flea_beetle",          # 27
    "radish_healthy",              # 28
    "radish_mosaic",               # 29
]

SPLITS = ["train", "valid", "test"]
IMG_EXTS = {".jpg", ".jpeg", ".png"}
MIN_CROP_PX = 20   # skip crops smaller than 20×20 px (noise)


def yolo_to_pixel(cx, cy, bw, bh, img_w, img_h):
    """Convert YOLO normalised coords to pixel (x1,y1,x2,y2)."""
    x1 = int((cx - bw / 2) * img_w)
    y1 = int((cy - bh / 2) * img_h)
    x2 = int((cx + bw / 2) * img_w)
    y2 = int((cy + bh / 2) * img_h)
    # clamp to image bounds
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(img_w, x2), min(img_h, y2)
    return x1, y1, x2, y2


def process_split(split):
    img_dir   = os.path.join(YOLO_ROOT, split, "images")
    label_dir = os.path.join(YOLO_ROOT, split, "labels")

    saved      = 0
    skipped    = 0
    per_class  = {}

    img_files = [
        f for f in os.listdir(img_dir)
        if os.path.splitext(f)[1].lower() in IMG_EXTS
    ]

    for img_name in img_files:
        img_path   = os.path.join(img_dir, img_name)
        label_path = os.path.join(
            label_dir,
            os.path.splitext(img_name)[0] + ".txt"
        )

        if not os.path.exists(label_path):
            continue

        img = cv2.imread(img_path)
        if img is None:
            skipped += 1
            continue

        img_h, img_w = img.shape[:2]

        with open(label_path) as f:
            lines = f.read().strip().splitlines()

        for idx, line in enumerate(lines):
            parts = line.split()
            if len(parts) != 5:
                continue
            cls_id = int(parts[0])
            cx, cy, bw, bh = map(float, parts[1:])

            x1, y1, x2, y2 = yolo_to_pixel(cx, cy, bw, bh, img_w, img_h)

            if (x2 - x1) < MIN_CROP_PX or (y2 - y1) < MIN_CROP_PX:
                skipped += 1
                continue

            crop = img[y1:y2, x1:x2]
            cls_name = CLASS_NAMES[cls_id]

            out_dir = os.path.join(OUT_ROOT, split, cls_name)
            os.makedirs(out_dir, exist_ok=True)

            stem     = os.path.splitext(img_name)[0]
            out_name = f"{stem}_crop{idx:02d}.jpg"
            cv2.imwrite(os.path.join(out_dir, out_name), crop,
                        [cv2.IMWRITE_JPEG_QUALITY, 90])

            per_class[cls_name] = per_class.get(cls_name, 0) + 1
            saved += 1

    return saved, skipped, per_class


def main():
    print("=== Multi-Crop YOLO → Classification Converter ===\n")
    grand_total = 0
    all_per_class = {}

    for split in SPLITS:
        print(f"Processing {split} ...")
        saved, skipped, per_class = process_split(split)
        grand_total += saved
        print(f"  Saved: {saved}  |  Skipped (tiny/missing): {skipped}")
        for cls, n in sorted(per_class.items()):
            all_per_class[cls] = all_per_class.get(cls, 0) + n

    print(f"\nGrand total crops saved: {grand_total}")
    print("\n--- Per-class totals (all splits combined) ---")
    for cls, n in sorted(all_per_class.items()):
        print(f"  {cls}: {n}")

    print("\nDone. Output at:", OUT_ROOT)


if __name__ == "__main__":
    main()
