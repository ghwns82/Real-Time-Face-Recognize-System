from fastapi import APIRouter
from app.rtsp_reader import read_rtsp_stream
import threading
from app.face_inference import run_face_inference


router = APIRouter()
stream_threads = {}


@router.post("/start-stream")
async def start_stream(rtsp_url: str):
    if rtsp_url in stream_threads:
        return {"message": "이미 실행 중인 스트림입니다."}

    thread = threading.Thread(
        target=read_rtsp_stream,
        args=(rtsp_url, run_face_inference),
        daemon=True
    )
    thread.start()
    stream_threads[rtsp_url] = thread
    

    return {"message": f"스트림 시작: {rtsp_url}"}
