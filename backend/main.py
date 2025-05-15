from fastapi import FastAPI, File, UploadFile, WebSocket
import cv2
import numpy as np

app = FastAPI()


@app.post("/recognize-face/")
async def recognize_face(file: UploadFile = File(...)):
    image = np.frombuffer(await file.read(), np.uint8)
    frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # (예시) 실제 얼굴 인식 로직은 생략
    return {"name": "test"}