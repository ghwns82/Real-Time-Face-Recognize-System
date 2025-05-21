import torch
from torchvision.models import (
    resnet18, ResNet18_Weights,
    vit_b_16, ViT_B_16_Weights,
    vit_l_16, ViT_L_16_Weights,
    swin_t, Swin_T_Weights,
    convnext_tiny, ConvNeXt_Tiny_Weights,
)
from PIL import Image

# 🧠 사용할 모델 목록 정의
MODEL_CONFIGS = {
    "ResNet18": (resnet18, ResNet18_Weights.DEFAULT),
    "ViT-B/16": (vit_b_16, ViT_B_16_Weights.DEFAULT),
    "ViT-L/16": (vit_l_16, ViT_L_16_Weights.DEFAULT),
    "Swin-T": (swin_t, Swin_T_Weights.DEFAULT),
    "ConvNeXt-Tiny": (convnext_tiny, ConvNeXt_Tiny_Weights.DEFAULT),
}

# 🔍 여러 모델로 예측 수행 함수
def predict_all(image: Image.Image) -> dict:
    results = {}
    img = image.convert("RGB")

    for name, (model_fn, weights) in MODEL_CONFIGS.items():
        model = model_fn(weights=weights)
        model.eval()

        transform = weights.transforms()
        tensor = transform(img).unsqueeze(0)

        with torch.no_grad():
            outputs = model(tensor)
            _, predicted = torch.max(outputs, 1)

        label = weights.meta["categories"][predicted.item()]
        results[name] = label

    return results
