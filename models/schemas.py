from pydantic import BaseModel
from typing import Literal

class LocationData(BaseModel):
    x: float
    y: float
    status: Literal["normal", "out", "danger"]
    timestamp: str

class CSIData(BaseModel):
    raw: list[float]
    device_id: str
    timestamp: str

class DeviceTokenRegister(BaseModel):
    token: str
