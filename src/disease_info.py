"""
Disease information for all 87 crop disease classes.

Bilingual (English + Hindi) information sourced from ICAR and PAU Ludhiana guidelines.
Assembled from three part files for manageability.

Usage:
    from src.disease_info import DISEASE_INFO, get_disease_info

    info = get_disease_info("tomato_early_blight", lang="en")
    # Returns dict with keys: name, cause, symptoms, cure, prevention, pesticide,
    #                          severity, is_healthy

    info = get_disease_info("tomato_early_blight", lang="hi")
    # Same keys but Hindi values.
"""

from src.disease_info_1 import DISEASE_INFO_1
from src.disease_info_2 import DISEASE_INFO_2
from src.disease_info_3 import DISEASE_INFO_3

# ── Merge all three parts ──────────────────────────────────────────────────────

DISEASE_INFO: dict = {}
DISEASE_INFO.update(DISEASE_INFO_1)
DISEASE_INFO.update(DISEASE_INFO_2)
DISEASE_INFO.update(DISEASE_INFO_3)

# ── Validation (runs at import time, raises if broken) ────────────────────────

_EXPECTED_CLASSES = 87
_REQUIRED_FIELDS = [
    "name_en", "name_hi",
    "cause_en", "cause_hi",
    "symptoms_en", "symptoms_hi",
    "cure_en", "cure_hi",
    "prevention_en", "prevention_hi",
    "pesticide_en", "pesticide_hi",
    "severity", "is_healthy",
]

def _validate():
    if len(DISEASE_INFO) != _EXPECTED_CLASSES:
        raise ValueError(
            f"Expected {_EXPECTED_CLASSES} classes, found {len(DISEASE_INFO)}."
        )
    for cls, entry in DISEASE_INFO.items():
        missing = [f for f in _REQUIRED_FIELDS if f not in entry]
        if missing:
            raise ValueError(f"Class '{cls}' is missing fields: {missing}")

_validate()


# ── Public API ────────────────────────────────────────────────────────────────

def get_disease_info(class_name: str, lang: str = "en") -> dict:
    """
    Return a language-specific dict for the given class name.

    Parameters
    ----------
    class_name : str   e.g. "tomato_early_blight"
    lang       : str   "en" (English) or "hi" (Hindi)

    Returns
    -------
    dict with keys:
        name, cause, symptoms, cure, prevention, pesticide, severity, is_healthy

    Raises
    ------
    KeyError  if class_name is not in DISEASE_INFO
    ValueError if lang is not "en" or "hi"
    """
    if lang not in ("en", "hi"):
        raise ValueError(f"lang must be 'en' or 'hi', got '{lang}'")

    if class_name not in DISEASE_INFO:
        raise KeyError(
            f"Unknown class '{class_name}'. "
            f"Available: {sorted(DISEASE_INFO.keys())}"
        )

    entry = DISEASE_INFO[class_name]
    suffix = f"_{lang}"

    return {
        "name":       entry[f"name{suffix}"],
        "cause":      entry[f"cause{suffix}"],
        "symptoms":   entry[f"symptoms{suffix}"],
        "cure":       entry[f"cure{suffix}"],
        "prevention": entry[f"prevention{suffix}"],
        "pesticide":  entry[f"pesticide{suffix}"],
        "severity":   entry["severity"],
        "is_healthy": entry["is_healthy"],
    }


# ── Convenience helpers ───────────────────────────────────────────────────────

def list_classes() -> list:
    """Return sorted list of all 87 class names."""
    return sorted(DISEASE_INFO.keys())


def get_healthy_classes() -> list:
    """Return list of class names where is_healthy=True."""
    return sorted(k for k, v in DISEASE_INFO.items() if v["is_healthy"])


def get_classes_by_severity(severity: str) -> list:
    """
    Return class names matching the given severity level.
    severity: "none" | "low" | "medium" | "high"
    """
    return sorted(k for k, v in DISEASE_INFO.items() if v["severity"] == severity)


if __name__ == "__main__":
    print(f"Total classes  : {len(DISEASE_INFO)}")
    print(f"Healthy classes: {len(get_healthy_classes())}")

    for sev in ("none", "low", "medium", "high"):
        print(f"Severity '{sev}': {len(get_classes_by_severity(sev))} classes")

    # Spot-check one class in each language
    for cls in ["tomato_early_blight", "wheat_blast", "banana_healthy"]:
        en = get_disease_info(cls, "en")
        hi = get_disease_info(cls, "hi")
        print(f"\n{cls}")
        print(f"  EN: {en['name']} | severity={en['severity']} | healthy={en['is_healthy']}")
        print(f"  HI: {hi['name']}")

    print("\ndisease_info.py OK")
