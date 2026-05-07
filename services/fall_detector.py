from collections import deque

# 최근 위치 기록 (낙상 감지용)
_history: deque = deque(maxlen=10)

def update_and_detect(x: float, y: float) -> str:
    _history.append((x, y))

    if len(_history) < 3:
        return "normal"

    # 실제 연결 시 CSI 기반 낙상 판단 알고리즘으로 교체
    # 현재는 위치 변화가 거의 없으면 낙상 의심 (Mock 로직)
    recent = list(_history)[-3:]
    diffs = [
        abs(recent[i][0] - recent[i-1][0]) + abs(recent[i][1] - recent[i-1][1])
        for i in range(1, len(recent))
    ]
    avg_movement = sum(diffs) / len(diffs)

    if avg_movement < 0.01:
        return "danger"
    elif avg_movement > 0.5:
        return "out"
    return "normal"
