from fastapi import FastAPI, File, UploadFile
from .inference.classifier import predict_all
from PIL import Image
import io

app = FastAPI()

@app.post("/predict")
async def classify_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    results = predict_all(image)
    print(results)  # 콘솔 로그에 전체 결과 출력

    return {"predictions": results}
