import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import requests
from io import BytesIO

# 1. 사전 학습된 ResNet-18 모델 불러오기
model = models.resnet18(pretrained=True)
model.eval()

# 2. 이미지 로드 (인터넷에서 아무 이미지 사용)
url = "https://upload.wikimedia.org/wikipedia/commons/2/26/YellowLabradorLooking_new.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content)).convert("RGB")

# 3. 이미지 전처리
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),  # [0, 1]
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # ImageNet 기준
                         std=[0.229, 0.224, 0.225])
])

input_tensor = transform(img).unsqueeze(0)  # 배치 차원 추가

# 4. 예측 수행
with torch.no_grad():
    outputs = model(input_tensor)
    _, predicted = torch.max(outputs, 1)

# 5. 클래스 이름 로드
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = requests.get(LABELS_URL).text.strip().split("\n")

# 6. 결과 출력
print(f"예측된 클래스: {labels[predicted.item()]}")
