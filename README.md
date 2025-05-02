# 디렉토리 구조

```sql
C:\Real Time Face Recognize System\
├── face_api_project\             ← FastAPI 프로젝트
├── mediamtx\                     ← RTSP 서버 (mediamtx.exe 위치)
├── ffmpeg\                       ← FFmpeg (압축 풀어서 bin 포함)
├── video.mp4                     ← 테스트용 영상
```


# 1. FastAPI서버 실행
```bash
cd "C:\Real Time Face Recognize System\face_api_project"
uvicorn app.main:app --reload
```

브라우저에서 Swagger 열기
http://localhost:8000/docs

# 2. FastAPI에 RTSP 스트림 요청 확인

swagger에서 post/start-stream 선택

rtsp url 삽입

아래는 예시입니다.

```sql
"rtsp_url": "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"
```

# APPENDIX 만약 로컬에서 테스트해보고 싶다면
1. video.mp4 준비
2. RTSP 서버 실행 (MediaMTX)
```bash
cd "C:\Real Time Face Recognize System\mediamtx"
mediamtx.exe
```

성공메시지 예
```bash
[INF] rtsp server opened on :8554
```

3.  FFmpeg로 영상 송출
```bash
"C:\Real Time Face Recognize System\ffmpeg\bin\ffmpeg.exe" -re -stream_loop -1 -i "C:\Real Time Face Recognize System\video.mp4" -c copy -f rtsp rtsp://localhost:8554/mystream
```

4. FastAPI 서버 실행
```bash
cd "C:\Real Time Face Recognize System\face_api_project"
uvicorn app.main:app --reload
```
