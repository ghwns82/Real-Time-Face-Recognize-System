# classifier.py

import torch
from torchvision.models import resnet18, ResNet18_Weights
from PIL import Image

# 1. 모델 및 가중치 불러오기 (새로운 방식)
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)
model.eval()

# 2. 전처리 정의 (가중치 기준 권장 transform 사용)
transform = weights.transforms()

# 3. 클래스 라벨 목록
imagenet_labels = weights.meta["categories"]

# 4. 예측 함수
def predict(image: Image.Image) -> str:
    img = image.convert("RGB")
    tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        outputs = model(tensor)
        _, predicted = torch.max(outputs, 1)

    return imagenet_labels[predicted.item()]
