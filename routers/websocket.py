from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.csi_parser import generate_mock_csi, parse_csi_to_location, get_timestamp
from services.fall_detector import update_and_detect
from models.schemas import LocationData
import asyncio
import json

router = APIRouter()

# 연결된 앱 클라이언트 목록
active_connections: list[WebSocket] = []

@router.websocket("/ws/location")
async def websocket_location(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            # Mock CSI 데이터 생성 → 좌표 변환 → 낙상 감지
            csi = generate_mock_csi()
            x, y = parse_csi_to_location(csi)
            status = update_and_detect(x, y)

            data = LocationData(
                x=x,
                y=y,
                status=status,
                timestamp=get_timestamp(),
            )

            await websocket.send_text(data.model_dump_json())
            await asyncio.sleep(1)  # 1초마다 전송

    except WebSocketDisconnect:
        active_connections.remove(websocket)
