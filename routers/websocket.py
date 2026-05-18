from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.csi_parser import generate_mock_csi, parse_csi_to_location, get_timestamp
from services.fall_detector import update_and_detect
from services import fcm_service
from models.schemas import LocationData
import asyncio

router = APIRouter()

active_connections: list[WebSocket] = []

@router.websocket("/ws/location")
async def websocket_location(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            csi = generate_mock_csi()
            x, y = parse_csi_to_location(csi)
            status = update_and_detect(x, y)

            if status == "danger":
                loop = asyncio.get_running_loop()
                loop.run_in_executor(None, fcm_service.send_fall_alert)

            data = LocationData(
                x=x,
                y=y,
                status=status,
                timestamp=get_timestamp(),
            )

            await websocket.send_text(data.model_dump_json())
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        active_connections.remove(websocket)
