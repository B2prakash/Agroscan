# AgroScan — AI Crop Disease Detector

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-red)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Accuracy](https://img.shields.io/badge/Accuracy-96.11%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

## About
AgroScan is an AI-powered crop disease detector built for Indian farmers. Upload a leaf photo or scan live with camera to get instant disease diagnosis, treatment advice, and farming guidance.

## Features
- 96.11% accuracy on 87 disease classes
- EfficientNet-B0 + Grad-CAM visualization
- Hindi and English support
- Live camera scan
- WhatsApp bot integration
- Harvest calendar (23 crops)
- Indoor growing guide (23 crops)
- What to Buy — pesticide recommendations
- Find nearest KVK and Agri Market
- Kisan Helpline: 1800-180-1551
- Dark and Light mode

## Tech Stack
- Model: EfficientNet-B0 (PyTorch)
- Backend: FastAPI
- Frontend: Vanilla HTML/CSS/JS
- Training: 67,368 images, 87 classes
- Hosting: Hugging Face Spaces

## Dataset Sources
- PlantVillage (54,303 images)
- Rice Leaf Diseases (Kaggle)
- Wheat Plant Diseases (Kaggle)
- Multi-Crop Disease Dataset (Kaggle)

## Disease Info Sources
- ICAR (Indian Council of Agricultural Research)
- PAU Ludhiana guidelines

## Setup
```bash
pip install -r requirements.txt
python train.py --data data/merged --epochs_stage1 5 --epochs_stage2 15
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Results
| Stage | Val Accuracy |
|-------|-------------|
| Stage 1 (frozen) | 87.08% |
| Stage 2 (fine-tune) | 96.11% |

## Built By
Bittu (B2prakash) — BE-IT, Chandigarh University
GSoC 2026 contributor — Mesa/NumFOCUS
