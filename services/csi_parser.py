import random
import math
from datetime import datetime

# Jetson 연결 전 Mock CSI 데이터 생성기
def generate_mock_csi() -> list[float]:
    return [random.gauss(0, 1) for _ in range(64)]

def parse_csi_to_location(csi_data: list[float]) -> tuple[float, float]:
    # 실제 연결 시 이 함수에 CSI → 좌표 변환 알고리즘 삽입
    amplitude = [abs(v) for v in csi_data]
    x = (sum(amplitude[:32]) / 32) % 1.0
    y = (sum(amplitude[32:]) / 32) % 1.0
    return round(x, 3), round(y, 3)

def get_timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")
