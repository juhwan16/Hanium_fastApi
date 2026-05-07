from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import websocket, status

app = FastAPI(
    title="Hanium CSI Safety API",
    description="WiFi CSI 기반 어르신 안전 모니터링 서버",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(status.router)
app.include_router(websocket.router)
