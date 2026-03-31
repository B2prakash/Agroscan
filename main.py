"""
AgroScan — FastAPI backend for crop disease detection.

Endpoints
---------
GET  /health      → model status, loaded flag, class count, device
POST /predict     → image upload → class, confidence, severity,
                    bilingual disease info, base64 Grad-CAM overlay
POST /whatsapp    → Twilio WhatsApp webhook → Hindi TwiML reply

Design notes
------------
* Model, class names and GradCAM are loaded ONCE at startup via FastAPI
  lifespan and stored in app.state — zero per-request overhead.
* Grad-CAM runs a second forward+backward pass; a threading.Lock ensures
  a single GradCAM instance is never used concurrently (safe for the
  default thread-pool executor used by async endpoints).
* CORS is open (*) so any frontend / mobile app can call the API.
"""

import asyncio
import base64
import io
import json
import logging
import os
import threading
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
import torch
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from PIL import Image, UnidentifiedImageError

from src.disease_info import DISEASE_INFO
from src.gradcam import GradCAM, overlay_on_image
from src.model import build_model
from src.utils import preprocess_image


# ── Logging ───────────────────────────────────────────────────────────────────

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")
log = logging.getLogger("agroscan")


# ── Paths ─────────────────────────────────────────────────────────────────────

_MODELS_DIR       = Path("models")
_CLASS_NAMES_PATH = _MODELS_DIR / "class_names.json"


# ── Concurrency guard for GradCAM ─────────────────────────────────────────────

_predict_lock = threading.Lock()


# ── Device selection ──────────────────────────────────────────────────────────

def _get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


# ── Lifespan — model loaded once at startup ───────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── startup ───────────────────────────────────────────────────────────────
    from huggingface_hub import hf_hub_download

    model_path = "/tmp/best_model.pth"
    if not os.path.exists(model_path):
        print("Downloading model...")
        hf_hub_download(
            repo_id="B2prakash/agroscan-model",
            filename="best_model.pth",
            repo_type="model",
            local_dir="/tmp",
            token=os.environ.get("HF_TOKEN")
        )
        print("Model downloaded!")

    _CHECKPOINT_PATH = model_path

    device = _get_device()
    log.info(f"Device: {device}")

    with open(_CLASS_NAMES_PATH) as f:
        class_names = json.load(f)
    log.info(f"Classes loaded: {len(class_names)}")

    model = build_model(num_classes=len(class_names)).to(device)
    ckpt  = torch.load(_CHECKPOINT_PATH, map_location=device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()
    log.info(
        f"Checkpoint loaded: {_CHECKPOINT_PATH}  "
        f"(val_acc={ckpt.get('val_acc', 0.0):.4f})"
    )

    app.state.model       = model
    app.state.gradcam     = GradCAM(model)
    app.state.class_names = class_names
    app.state.device      = device
    app.state.model_ready = True

    yield  # ── server running ─────────────────────────────────────────────────

    # ── shutdown ──────────────────────────────────────────────────────────────
    app.state.gradcam.remove_hooks()
    log.info("GradCAM hooks removed. Shutdown complete.")


# ── App ───────────────────────────────────────────────────────────────────────

app = FastAPI(title="AgroScan", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Internal helpers ──────────────────────────────────────────────────────────

def _bytes_to_pil(data: bytes) -> Image.Image:
    """Parse raw bytes → RGB PIL Image, or raise HTTP 400."""
    try:
        return Image.open(io.BytesIO(data)).convert("RGB")
    except (UnidentifiedImageError, Exception) as exc:
        raise HTTPException(status_code=400, detail=f"Invalid image: {exc}")


def _run_prediction(pil_image: Image.Image, state) -> dict:
    """
    Thread-safe prediction pipeline.
    Returns a dict matching the /predict response schema.
    """
    tensor = preprocess_image(pil_image, device=str(state.device))

    # GradCAM: one no_grad forward (confidence) + one backward (heatmap)
    with _predict_lock:
        heatmap, class_idx, confidence = state.gradcam.generate_top_class(tensor)

    class_name = state.class_names[class_idx]
    entry      = DISEASE_INFO[class_name]

    # ── Coming-soon crop: return early without Grad-CAM ───────────────────────
    if entry.get("is_coming_soon"):
        return {
            "class":          class_name,
            "confidence":     round(confidence * 100, 2),
            "severity":       "unknown",
            "is_coming_soon": True,
            "disease_info": {
                "name_en":    entry["name_en"],
                "name_hi":    entry["name_hi"],
                "message_en": entry["message_en"],
                "message_hi": entry["message_hi"],
                "contact_en": entry["contact_en"],
                "contact_hi": entry["contact_hi"],
            },
            "gradcam_image": None,
        }

    # Overlay heatmap on original image → base64 JPEG
    overlay = overlay_on_image(pil_image, heatmap)
    buf     = io.BytesIO()
    overlay.save(buf, format="JPEG", quality=85)
    gradcam_b64 = base64.b64encode(buf.getvalue()).decode()

    return {
        "class":      class_name,
        "confidence": round(confidence * 100, 2),
        "severity":   entry["severity"],
        "disease_info": {
            "name_en":       entry["name_en"],
            "name_hi":       entry["name_hi"],
            "cure_en":       entry["cure_en"],
            "cure_hi":       entry["cure_hi"],
            "prevention_en": entry["prevention_en"],
            "prevention_hi": entry["prevention_hi"],
            "pesticide_en":  entry["pesticide_en"],
            "pesticide_hi":  entry["pesticide_hi"],
        },
        "gradcam_image": gradcam_b64,
    }


# ── Endpoints ─────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    """Serve the frontend."""
    return FileResponse("index.html")


@app.get("/health")
def health():
    """Returns model status, device, and class count."""
    state = app.state
    return {
        "status":       "ok",
        "model_loaded": getattr(state, "model_ready", False),
        "num_classes":  len(getattr(state, "class_names", [])),
        "device":       str(getattr(state, "device", "unknown")),
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Upload an image file; receive class, confidence, disease info, and
    a base64-encoded Grad-CAM heatmap overlay.
    """
    if not getattr(app.state, "model_ready", False):
        raise HTTPException(status_code=503, detail="Model not loaded yet.")

    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty file.")

    pil_image = _bytes_to_pil(data)

    try:
        loop   = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None, _run_prediction, pil_image, app.state
        )
    except HTTPException:
        raise
    except Exception as exc:
        log.exception("Prediction failed")
        raise HTTPException(status_code=500, detail=f"Prediction error: {exc}")

    return result


@app.post("/whatsapp")
async def whatsapp(
    Body:      str = Form(default=""),
    MediaUrl0: str = Form(default=""),
    From:      str = Form(default=""),
    NumMedia:  str = Form(default="0"),
):
    """
    Twilio WhatsApp webhook.
    Downloads the farmer's photo, runs prediction, replies in Hindi via TwiML.
    """

    def twiml(msg: str) -> Response:
        xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            "<Response>"
            f"<Message>{msg}</Message>"
            "</Response>"
        )
        return Response(content=xml, media_type="application/xml")

    # No image attached
    if NumMedia == "0" or not MediaUrl0:
        return twiml(
            "नमस्ते! कृपया अपनी फसल की फोटो भेजें। 🌱\n"
            "(Hello! Please send a photo of your crop to detect the disease.)"
        )

    # Download image from Twilio CDN
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.get(MediaUrl0)
            resp.raise_for_status()
            image_data = resp.content
    except Exception as exc:
        log.error(f"WhatsApp image download failed: {exc}")
        return twiml(
            "फोटो डाउनलोड नहीं हो सकी। कृपया दोबारा भेजें। "
            "(Could not download the photo. Please try again.)"
        )

    pil_image = _bytes_to_pil(image_data)

    try:
        loop   = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None, _run_prediction, pil_image, app.state
        )
    except Exception as exc:
        log.exception("WhatsApp prediction error")
        return twiml(
            "विश्लेषण में त्रुटि। कृपया पुनः प्रयास करें। "
            "(Analysis failed. Please try again.)"
        )

    info    = result["disease_info"]
    sev_map = {
        "none":   "कोई नहीं ✅",
        "low":    "कम ⚠️",
        "medium": "मध्यम 🟠",
        "high":   "अधिक 🔴",
    }
    sev_hi = sev_map.get(result["severity"], result["severity"])

    reply = (
        f"🌿 *AgroScan — फसल रोग पहचान*\n\n"
        f"🔍 रोग: {info['name_hi']}\n"
        f"📊 विश्वास: {result['confidence']}%\n"
        f"⚠️ गंभीरता: {sev_hi}\n\n"
        f"💊 *उपचार:*\n{info['cure_hi']}\n\n"
        f"🛡️ *रोकथाम:*\n{info['prevention_hi']}\n\n"
        f"🧪 *कीटनाशक:*\n{info['pesticide_hi']}"
    )

    return twiml(reply)


# ── Dev entry point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
