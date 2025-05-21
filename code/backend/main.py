from fastapi import FastAPI, File, UploadFile
from .inference.classifier import predict
from PIL import Image
import io

app = FastAPI()

@app.post("/predict")
async def classify_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    label = predict(image)
    print(label)
    return {"name": label}
