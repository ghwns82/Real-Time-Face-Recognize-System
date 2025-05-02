import cv2
import threading

def read_rtsp_stream(rtsp_url: str, callback=None):
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print(f"[!] RTSP 연결 실패: {rtsp_url}")
        return

    print("[*] RTSP 스트림 수신 중...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[!] 프레임 수신 실패")
            break

        # 여기서 얼굴 인식 등 원하는 작업 수행
        if callback:
            callback(frame)

        # 디버깅용: 화면에 프레임 띄우기 (원격 서버일 경우 주석)
        cv2.imshow("RTSP Stream", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
