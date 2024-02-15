# server_fastapi_cnn.py
import uvicorn   # pip install uvicorn 
from fastapi import FastAPI   # pip install fastapi 
from fastapi.middleware.cors import CORSMiddleware # 추가된부분 cors 문제 해결을 위한

# 예측 모듈 가져오기
import cnn_prediction_model

# Create the FastAPI application
app = FastAPI()

# cors 이슈
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# A simple example of a GET request
@app.get("/")
async def read_root():
    print("url was requested")
    return "CNN모델을 사용하는 API를 만들어 봅시다."

@app.get('/sample')
async def sample_prediction():
    result = await cnn_prediction_model.prediction_model()
    print("prediction was requested and done")
    return result


# Run the server
if __name__ == "__main__":
    uvicorn.run("server_fastapi_cnn:app",
            reload= True,   # Reload the server when code changes
            host="127.0.0.1",   # Listen on localhost 
            port=8080,   # Listen on port 8080 
            log_level="info"   # Log level
            )