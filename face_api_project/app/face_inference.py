import time

def run_face_inference(frame):
    """
    RTSP 스트림에서 받은 프레임을 얼굴인식 모델에 전달하여 예측을 수행합니다.
    현재는 예시로, 프레임 크기 출력만 하고 있습니다.
    """
    # 여기에 얼굴 인식 모델 예측 코드를 삽입하면 됩니다
    print(f"[얼굴인식] 프레임 크기: {frame.shape}")
    time.sleep(0.05)  # 처리 지연 시뮬레이션
