"""
Grad-CAM (Gradient-weighted Class Activation Mapping) for EfficientNet-B0.

Usage:
    cam     = GradCAM(model)
    heatmap = cam.generate(image_tensor, class_idx)   # np.ndarray (H,W) in [0,1]
    overlay = overlay_on_image(pil_image, heatmap)    # PIL Image with colored overlay
    cam.remove_hooks()
"""

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
import cv2


class GradCAM:
    """
    Hooks into the target layer of an EfficientNet-B0 to compute Grad-CAM heatmaps.

    Parameters
    ----------
    model        : CropDiseaseModel  (must be in eval() before calling generate)
    target_layer : nn.Module         defaults to model.gradcam_layer (features[-1])
    """

    def __init__(self, model, target_layer=None):
        self.model  = model
        self._layer = target_layer if target_layer is not None else model.gradcam_layer

        self._activations = None
        self._gradients   = None

        self._fwd_hook = self._layer.register_forward_hook(self._save_activations)
        self._bwd_hook = self._layer.register_full_backward_hook(self._save_gradients)

    # ── hooks ──────────────────────────────────────────────────────────────

    def _save_activations(self, module, inp, output):
        self._activations = output.detach()

    def _save_gradients(self, module, grad_input, grad_output):
        self._gradients = grad_output[0].detach()

    def remove_hooks(self):
        """Call when done to avoid memory leaks."""
        self._fwd_hook.remove()
        self._bwd_hook.remove()

    # ── core ───────────────────────────────────────────────────────────────

    def generate(self, image_tensor: torch.Tensor, class_idx: int = None) -> np.ndarray:
        """
        Compute Grad-CAM heatmap.

        Parameters
        ----------
        image_tensor : torch.Tensor  shape (1, 3, H, W), normalised
        class_idx    : int | None    target class; None → uses argmax(logits)

        Returns
        -------
        heatmap : np.ndarray  shape (H, W), float32 in [0, 1]
        """
        self.model.eval()
        device = next(self.model.parameters()).device
        image_tensor = image_tensor.to(device)

        logits = self.model(image_tensor)           # (1, C)

        if class_idx is None:
            class_idx = int(logits.argmax(dim=1).item())

        self.model.zero_grad()
        logits[0, class_idx].backward()

        grads   = self._gradients                           # (1, C, h, w)
        acts    = self._activations                         # (1, C, h, w)
        weights = grads.mean(dim=(2, 3), keepdim=True)      # (1, C, 1, 1)
        cam     = F.relu((weights * acts).sum(dim=1, keepdim=True))  # (1,1,h,w)

        h, w = image_tensor.shape[2], image_tensor.shape[3]
        cam  = F.interpolate(cam, size=(h, w), mode="bilinear", align_corners=False)
        cam  = cam.squeeze().cpu().numpy()

        mn, mx = cam.min(), cam.max()
        cam = (cam - mn) / (mx - mn + 1e-8)
        return cam.astype(np.float32)

    def generate_top_class(self, image_tensor: torch.Tensor):
        """
        Returns (heatmap, predicted_class_idx, confidence).
        """
        self.model.eval()
        device = next(self.model.parameters()).device
        with torch.no_grad():
            probs = torch.softmax(self.model(image_tensor.to(device)), dim=1)
            conf, idx = probs.max(dim=1)
        class_idx  = int(idx.item())
        confidence = float(conf.item())
        heatmap    = self.generate(image_tensor, class_idx)
        return heatmap, class_idx, confidence


# ── overlay ───────────────────────────────────────────────────────────────────

def overlay_on_image(
    original_image,
    heatmap: np.ndarray,
    alpha: float = 0.45,
    colormap: int = cv2.COLORMAP_JET,
) -> Image.Image:
    """
    Blend a Grad-CAM heatmap onto the original image.

    Parameters
    ----------
    original_image : PIL.Image or np.ndarray (H, W, 3) uint8
    heatmap        : np.ndarray (H, W) float32 in [0, 1]
    alpha          : float  heatmap opacity (0=original only, 1=heatmap only)
    colormap       : OpenCV colormap constant (default COLORMAP_JET)

    Returns
    -------
    PIL.Image with colored heatmap overlaid
    """
    if isinstance(original_image, Image.Image):
        orig = np.array(original_image.convert("RGB"), dtype=np.uint8)
    else:
        orig = np.asarray(original_image, dtype=np.uint8)

    h, w = orig.shape[:2]
    if heatmap.shape != (h, w):
        heatmap = cv2.resize(heatmap, (w, h), interpolation=cv2.INTER_LINEAR)

    colored_bgr = cv2.applyColorMap((heatmap * 255).astype(np.uint8), colormap)
    colored_rgb = cv2.cvtColor(colored_bgr, cv2.COLOR_BGR2RGB)
    blended     = (alpha * colored_rgb + (1 - alpha) * orig).astype(np.uint8)
    return Image.fromarray(blended)


def save_gradcam(original_image, heatmap: np.ndarray, out_path: str, alpha: float = 0.45):
    overlay_on_image(original_image, heatmap, alpha=alpha).save(out_path)


if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from src.model import build_model

    model = build_model(num_classes=87)
    model.eval()

    dummy_tensor = torch.randn(1, 3, 224, 224)
    cam = GradCAM(model)

    heatmap = cam.generate(dummy_tensor, class_idx=0)
    print("Heatmap shape :", heatmap.shape)
    print("Heatmap range :", round(float(heatmap.min()), 4), "–", round(float(heatmap.max()), 4))

    dummy_pil = Image.fromarray(np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8))
    overlay   = overlay_on_image(dummy_pil, heatmap)
    print("Overlay size  :", overlay.size)
    print("gradcam.py OK")
    cam.remove_hooks()
