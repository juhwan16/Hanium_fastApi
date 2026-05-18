from fastapi import APIRouter
from services import fcm_service

router = APIRouter(prefix="/alarm", tags=["alarm"])

@router.post("/test")
def test_alarm():
    count = fcm_service.send_test_alert()
    return {"status": "sent", "recipients": count}
