from fastapi import FastAPI, WebSocket, Header, Response, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
import real_time_object_detection as rt

app = FastAPI()
templates = Jinja2Templates(directory="templates")
CHUNK_SIZE = 1024*1024
video_path = Path("video.mp4")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/video")
async def video_endpoint(range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")

@app.websocket('/stream')
# @app.get("/stream")
async def websocket_endpoint(websocket: WebSocket) -> None:
    # real_time = rt.RealTime()
    # await real_time.real_time_show(websocket)
    await websocket.accept()
    await websocket.send_text("It's working!")
    await websocket.close()


# @app.websocket('/stream')
# async def websocket_endpoint(websocket: WebSocket):
#     # WebSocket 연결을 유지하는 동안 실시간 데이터를 전송
#     async for data in rt.RealTime().real_time_data_generator():
#         await websocket.send_text(data)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse
# import cv2
# import base64
# import numpy as np
# from real_time_object_detection import RealTime  # RealTime 클래스를 임포트해야 합니다.
#
# app = FastAPI()
#
# html_content = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Object Detection</title>
# </head>
# <body>
#     <img id="objectDetection" width="640" height="480">
#     <script>
#         var ws = new WebSocket("ws://localhost:8000/stream");
#
#         ws.onmessage = function(event) {
#             document.getElementById("objectDetection").src = "data:image/jpeg;base64," + event.data;
#         };
#     </script>
# </body>
# </html>
# """
#
# @app.get("/")
# async def get():
#     return HTMLResponse(content=html_content, status_code=200)
#
# @app.websocket("/stream")
# async def stream(websocket: WebSocket):
#     await websocket.accept()
#     real_time = RealTime()
#
#     cap = cv2.VideoCapture(0)
#     cap.set(3, 960)
#     cap.set(4, 640)
#
#     while True:
#         ret, img = cap.read()
#         if not ret:
#             break
#
#         try:
#             results = real_time.model(img, stream=True)
#         except Exception as e:
#             print("Error processing frame with YOLO:", e)
#             continue
#
#         for r in results:
#             for box in r.boxes:
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#
#         _, buffer = cv2.imencode('.jpg', img)
#         image_as_text = base64.b64encode(buffer).decode('utf-8')
#
#         await websocket.send_text(image_as_text)
#
#     cap.release()
