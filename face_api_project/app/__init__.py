"""
===============================================
 Real Time Face Recognition - 실행 순서 안내
===============================================

[환경]
- Windows + VSCode
- 루트 폴더: C:\Real Time Face Recognize System

[프로젝트 구조]
C:\Real Time Face Recognize System\
├── face_api_project\             ← FastAPI 프로젝트 폴더
├── mediamtx\                     ← RTSP 서버 (mediamtx.exe 위치)
├── ffmpeg\                       ← FFmpeg 실행파일 (ffmpeg.exe 포함)
├── video.mp4                     ← 테스트용 영상 파일

-------------------------------------------------
  1단계. RTSP 서버 실행 (MediaMTX)
-------------------------------------------------

1. mediamtx.exe 실행

# 명령어:
cd "C:\Real Time Face Recognize System\mediamtx"
mediamtx.exe

# 성공 메시지 예시:
[INF] rtsp server opened on :8554

-------------------------------------------------
  2단계. FFmpeg로 영상 파일을 RTSP로 송출
-------------------------------------------------

# 명령어:
"C:\Real Time Face Recognize System\ffmpeg\bin\ffmpeg.exe" -re -stream_loop -1 -i "C:\Real Time Face Recognize System\video.mp4" -c copy -f rtsp rtsp://localhost:8554/mystream

- 영상이 무한 반복되며 RTSP 스트림으로 송출됩니다.
- 위 명령은 계속 켜두어야 합니다.

-------------------------------------------------
  3단계. FastAPI 서버 실행
-------------------------------------------------

# 명령어:
cd "C:\Real Time Face Recognize System\face_api_project"
uvicorn app.main:app --reload

# Swagger 접속:
http://localhost:8000/docs

-------------------------------------------------
  4단계. Swagger UI에서 /start-stream 호출
-------------------------------------------------

# 요청 본문(JSON):
{
  "rtsp_url": "rtsp://localhost:8554/mystream"
}

- 호출 후 터미널에 프레임 처리 로그가 출력되면 성공입니다.

-------------------------------------------------
  종료 방법
-------------------------------------------------

- FastAPI 종료:        Ctrl + C
- FFmpeg 송출 종료:   Ctrl + C
- MediaMTX 종료:       Ctrl + C

"""
