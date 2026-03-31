---
title: AgroScan
emoji: 🌿
colorFrom: green
colorTo: green
sdk: docker
app_port: 7860
---

# 🌿 AgroScan — AI-Powered Crop Disease Detector

<div align="center">

![AgroScan Banner](https://img.shields.io/badge/AgroScan-AI%20Crop%20Disease%20Detector-2dbe6c?style=for-the-badge&logo=leaf)

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.11-red?style=flat-square&logo=pytorch)](https://pytorch.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![Accuracy](https://img.shields.io/badge/Accuracy-96.11%25-brightgreen?style=flat-square)](/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

**AgroScan helps Indian farmers instantly detect crop diseases using AI — in Hindi and English.**

[Live Demo](#) · [WhatsApp Bot](#) · [Report Bug](https://github.com/B2prakash/Agroscan/issues) · [Request Feature](https://github.com/B2prakash/Agroscan/issues)

</div>

---

## 📖 About The Project

India loses **₹50,000 crore+** worth of crops every year due to diseases that go undetected until it's too late. Farmers in rural areas don't have easy access to agricultural experts, and by the time they identify a disease, it has already spread.

**AgroScan solves this problem.**

A farmer standing in their field can:
1. Open AgroScan on their phone browser (no app download needed)
2. Take a live photo of the diseased leaf OR upload from gallery
3. Get instant AI diagnosis in **Hindi or English** within 3 seconds
4. See **which pesticide to buy**, at what dose, from which store
5. Get the result directly on **WhatsApp** without even opening a website

Built specifically for Indian farmers with data from **ICAR** and **PAU Ludhiana**.

---

## ✨ Features

### 🔬 Core AI Features
- **96.11% accuracy** on 87 crop disease classes
- **EfficientNet-B0** — lightweight model, fast on mobile
- **Grad-CAM heatmap** — shows exactly which part of leaf the AI analyzed
- **Confidence score** — how sure the model is about its prediction
- **2-stage transfer learning** — ImageNet pretrained + fine-tuned

### 🌐 Website Features
- **Live camera scan** — point phone camera at leaf, instant result
- **Drag & drop upload** — upload from gallery
- **Hindi / English toggle** — entire UI switches language instantly
- **Dark / Light mode** — comfortable in any lighting condition
- **Mobile responsive** — works on any phone browser

### 🌾 Farming Advisory
- **Disease cure** — exact treatment steps
- **Prevention tips** — how to avoid next season
- **Pesticide recommendations** — name, dose, application method
- **Cause analysis** — why the disease happened

### 📅 Harvest Calendar
- Select crop + planting date
- Get expected harvest date
- Days remaining countdown
- Signs of readiness
- Best harvest time
- **23 crops supported**

### 🏠 Indoor Growing Guide
- Temperature, humidity, light, watering for each crop
- Pot/container size recommendations
- Do's and Don'ts
- **23 crops with Hindi + English support**

### 🛒 What to Buy
- Recommended pesticide name
- Exact dose per litre
- Available at local agri store
- **Kisan Call Centre: 1800-180-1551** (Free, 24/7, Hindi)
- Find nearest KVK (Krishi Vigyan Kendra)
- Find nearest Agri Market/Mandi

### 📱 WhatsApp Bot
- Farmer sends leaf photo on WhatsApp
- Bot replies in Hindi with disease + cure + pesticide
- No app download, no website — just WhatsApp
- Works on any basic Android phone

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| ML Model | EfficientNet-B0 (PyTorch) | Disease classification |
| Explainability | Grad-CAM | Heatmap visualization |
| Backend | FastAPI + Uvicorn | REST API server |
| Frontend | Vanilla HTML/CSS/JS | Web interface |
| WhatsApp | Twilio | Bot integration |
| Training | Apple Silicon MPS | GPU acceleration |
| Deployment | Hugging Face Spaces | Free cloud hosting |

---

## 📊 Model Performance

### Training Results

| Stage | Description | Val Accuracy | Val Loss |
|-------|-------------|-------------|---------|
| Stage 1 | Frozen backbone, head only | 87.08% | 0.4070 |
| Stage 2 Ep 1 | Full fine-tune starts | 91.46% | 0.2559 |
| Stage 2 Ep 5 | Continued improvement | 94.91% | 0.1603 |
| Stage 2 Ep 10 | Strong convergence | 95.63% | 0.1401 |
| **Stage 2 Ep 14** | **Best checkpoint** | **96.11%** | **0.1309** |

### Dataset Summary

| Dataset | Crops | Images | Classes |
|---------|-------|--------|---------|
| PlantVillage | 14 crops | 54,303 | 38 |
| Rice Leaf Diseases | Rice | 1,500 | 3 |
| Wheat Plant Diseases | Wheat | 13,104 | 15 |
| Multi-Crop Disease | 5 crops | 42,638 | 30 |
| **Total (merged)** | **20+ crops** | **67,368** | **87** |

### Training Configuration

| Parameter | Stage 1 | Stage 2 |
|-----------|---------|---------|
| Backbone | Frozen | Unfrozen |
| Epochs | 5 | 15 |
| Learning Rate | 1e-3 | 1e-4 |
| Scheduler | CosineAnnealingLR | CosineAnnealingLR |
| Optimizer | Adam | Adam |
| Early Stopping | patience=5 | patience=5 |
| Image Size | 224×224 | 224×224 |
| Batch Size | 32 | 32 |
| Class Weighting | Balanced | Balanced |

---

## 🚀 Setup & Running

### 1. Clone the repo
```bash
git clone https://github.com/B2prakash/Agroscan.git
cd Agroscan
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare dataset
```bash
# Place your datasets under data/
# Then merge them:
python scripts/merge_datasets.py
```

### 4. Train the model
```bash
# Both stages in one go:
python train.py --data data/merged --epochs_stage1 5 --epochs_stage2 15

# Or stage by stage (recommended — review Stage 1 before fine-tuning):
python train.py --data data/merged --epochs_stage1 5 --epochs_stage2 15 --stage 1
python train.py --data data/merged --epochs_stage1 5 --epochs_stage2 15 --stage 2
```

Training outputs saved to `models/`:
- `best_model.pth` — best checkpoint (by val accuracy)
- `class_names.json` — ordered class list
- `stage1_history.json` — Stage 1 metrics
- `training_curves.png` — loss / accuracy plots

### 5. Start the API server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 6. Open the frontend
Open `index.html` in a browser, or serve it:
```bash
python -m http.server 3000
# then visit http://localhost:3000
```

---

## 🔌 API Reference

### `GET /health`
Returns model status and device info.

```json
{
  "status": "ok",
  "model_loaded": true,
  "num_classes": 87,
  "device": "mps"
}
```

### `POST /predict`
Upload a leaf image, get disease diagnosis.

**Request:** `multipart/form-data` with field `file` (image)

**Response:**
```json
{
  "class": "Tomato___Late_blight",
  "confidence": 94.37,
  "severity": "high",
  "disease_info": {
    "name_en": "Late Blight",
    "name_hi": "पछेती झुलसा",
    "cure_en": "...",
    "cure_hi": "...",
    "prevention_en": "...",
    "prevention_hi": "...",
    "pesticide_en": "...",
    "pesticide_hi": "..."
  },
  "gradcam_image": "<base64 JPEG>"
}
```

### `POST /whatsapp`
Twilio WhatsApp webhook. Accepts a multipart form with `Body`, `MediaUrl0`, `From`, `NumMedia`. Returns TwiML with Hindi diagnosis reply.

---

## 📁 Project Structure

```
agroscan/
├── main.py                  # FastAPI app — /health, /predict, /whatsapp
├── train.py                 # 2-stage training script
├── index.html               # Single-file frontend (HTML + CSS + JS)
├── requirements.txt         # Python dependencies
│
├── src/
│   ├── model.py             # EfficientNet-B0 model builder
│   ├── gradcam.py           # Grad-CAM implementation
│   ├── utils.py             # DataLoaders, preprocessing, class weights
│   └── disease_info.py      # Bilingual disease info for 87 classes
│
├── scripts/
│   ├── merge_datasets.py    # Merge multiple datasets into one folder
│   ├── augment_rice.py      # Data augmentation for rice classes
│   ├── augment_weak_classes.py  # Augment under-represented classes
│   └── convert_multicrop.py # Convert multi-crop dataset to standard format
│
└── models/
    ├── best_model.pth       # Trained weights (not in repo — large file)
    ├── class_names.json     # 87 class names in order
    ├── stage1_history.json  # Stage 1 training history
    └── training_curves.png  # Loss/accuracy plot
```

---

## 🌱 Supported Crops & Diseases

87 disease classes across 20+ crops including:

| Crop | # Diseases |
|------|-----------|
| Tomato | 10 |
| Potato | 3 |
| Corn/Maize | 4 |
| Rice | 3 |
| Wheat | 15 |
| Apple | 4 |
| Grape | 4 |
| Peach | 2 |
| Cherry | 2 |
| Pepper | 2 |
| Strawberry | 2 |
| Squash | 1 |
| Soybean | 1 |
| Raspberry | 1 |
| + more | ... |

Each disease entry includes: English name, Hindi name, cure, prevention, cause, and pesticide recommendation.

---

## 📱 WhatsApp Bot Setup

1. Create a [Twilio](https://twilio.com) account and enable WhatsApp Sandbox
2. Add your Twilio credentials to `.env`:
```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
```
3. Set your Twilio webhook URL to:
```
https://your-domain.com/whatsapp
```
4. Farmers can now send leaf photos to your WhatsApp number and receive Hindi diagnosis replies instantly.

---

## 🚧 Roadmap

### v2 — Upcoming Crops
Currently collecting field datasets from Haryana farmers:
- 🧅 Onion
- 🧄 Garlic
- 🍆 Brinjal/Eggplant
- 🥒 Cucumber
- 🌻 Mustard (Sarson)
- 🫘 Pulses: Chana, Moong Dal, Arhar Dal
- 🥕 Carrot
- 🥬 Spinach

### v3 — Planned Features
- Flutter mobile app (Android + iOS)
- Offline mode (works without internet)
- Visual maturity detection (harvest readiness)
- Soil health analysis
- Weather-based disease prediction

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

1. Fork the repo
2. Create your branch: `git checkout -b feature/my-feature`
3. Commit: `git commit -m "Add my feature"`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Built By

**Bittu (B2prakash)**
BE-IT, Chandigarh University
GSoC 2026 Contributor — Mesa / NumFOCUS

---

## 🙏 Acknowledgements

- [PlantVillage Dataset](https://plantvillage.psu.edu/) — Penn State University
- [ICAR](https://icar.org.in/) — Indian Council of Agricultural Research
- [PAU Ludhiana](https://pau.edu/) — Punjab Agricultural University
- [EfficientNet](https://arxiv.org/abs/1905.11946) — Tan & Le, Google Brain
- [Grad-CAM](https://arxiv.org/abs/1610.02391) — Selvaraju et al.
- [Twilio](https://twilio.com) — WhatsApp API
