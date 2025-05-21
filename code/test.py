import torch
from torchvision import models
from torchvision.models import (
    vit_b_16, ViT_B_16_Weights,
    vit_l_16, ViT_L_16_Weights,
    swin_t, Swin_T_Weights,
    convnext_tiny, ConvNeXt_Tiny_Weights,
)
from PIL import Image
import requests
from io import BytesIO

# 🔧 비교할 모델들 (모두 동일한 흐름 적용)
MODEL_CONFIGS = {
    "ViT-B/16": (vit_b_16, ViT_B_16_Weights.DEFAULT),
    "ViT-L/16": (vit_l_16, ViT_L_16_Weights.DEFAULT),
    "Swin-T": (swin_t, Swin_T_Weights.DEFAULT),
    "ConvNeXt-Tiny": (convnext_tiny, ConvNeXt_Tiny_Weights.DEFAULT),
}

# 🖼️ 이미지 로드
def load_image_from_url(url: str) -> Image.Image:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    return image

# 🚀 예측 수행
def predict(model_fn, weights, image: Image.Image) -> str:
    model = model_fn(weights=weights)
    model.eval()

    transform = weights.transforms()
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        pred_idx = outputs.argmax(1).item()

    labels = weights.meta["categories"]
    return labels[pred_idx]

# 🧪 전체 모델에 대해 예측 실행
if __name__ == "__main__":
    # 1. 이미지 로드
    image_url = "https://upload.wikimedia.org/wikipedia/commons/2/26/YellowLabradorLooking_new.jpg"
    image = load_image_from_url(image_url)

    # 2. 모델별 예측 수행 및 결과 출력
    print("🧠 모델별 예측 결과:\n")
    for name, (model_fn, weights) in MODEL_CONFIGS.items():
        label = predict(model_fn, weights, image)
        print(f"[{name}] → {label}")
