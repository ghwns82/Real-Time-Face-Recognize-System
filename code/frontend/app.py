import streamlit as st
import requests
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import cv2
import threading
from PIL import Image
import numpy as np
import io

# FastAPI 주소 설정
RECOGNITION_API = "http://localhost:8000/predict"
UPLOAD_API = "http://localhost:8000/upload-image"  # 이미지 업로드 백엔드 API

st.title("🧠 얼굴 인식 시스템")
st.markdown("카메라 실시간 인식 또는 이미지 업로드 중 선택하세요.")

# ==========================
# 1️⃣ 이미지 업로드 모드
# ==========================

st.header("📷 이미지 업로드 얼굴 인식")

image_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])
if image_file is not None:
    # 이미지 보여주기
    st.image(image_file, caption="업로드된 이미지", use_container_width=True)

    if st.button("이미지로 얼굴 인식 요청"):
        # 이미지 데이터를 그대로 전송
        files = {"file": (image_file.name, image_file.read(), "image/jpeg")}
        response = requests.post(RECOGNITION_API, files=files)

        if response.status_code == 200:
            result = response.json()
            predictions = result.get("predictions", {})

            if predictions:
                st.success("✅ 모델별 인식 결과")
                for model, label in predictions.items():
                    st.write(f"🔍 **{model}** → {label}")
                # 또는 보기 좋게 표로 출력
                # st.table(predictions)
            else:
                st.warning("⚠️ 예측 결과가 비어 있습니다.")
        else:
            st.error("❌ 얼굴 인식 실패")

if st.toggle("📹 실시간 웹캠 얼굴 인식 켜기"):
    st.header("📹 실시간 웹캠 얼굴 인식")

    class VideoProcessor(VideoProcessorBase):
        def __init__(self):
            self.frame_count = 0
            self.result_label = "..."
            self.request_interval = 30
            self.lock = threading.Lock()

        def send_frame_to_backend(self, img):
            try:
                _, img_encoded = cv2.imencode('.jpg', img)
                response = requests.post(
                    RECOGNITION_API,
                    files={"file": ("frame.jpg", img_encoded.tobytes(), "image/jpeg")},
                    timeout=10  # ✅ 더 넉넉하게
                )
                if response.status_code == 200:
                    result = response.json()
                    predictions = result.get("predictions", {})
                    label = predictions.get("ResNet18", "Unknown")  # ✅ 대표 모델만 선택
                else:
                    label = "Error"
            except Exception as e:
                print("🔥 예외 발생:", e)  # ✅ 콘솔에 에러 메시지 출력
                label = "Error"

            with self.lock:
                self.result_label = label

        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")
            self.frame_count += 1

            if self.frame_count % self.request_interval == 0:
                threading.Thread(target=self.send_frame_to_backend, args=(img.copy(),)).start()

            with self.lock:
                label_to_display = self.result_label

            cv2.putText(img, label_to_display, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
            return frame.from_ndarray(img, format="bgr24")

    webrtc_streamer(key="face-recognition", video_processor_factory=VideoProcessor)
