from typing import TypedDict, List


class LogisticsState(TypedDict):
    order_id: str
    current_driver: str
    delay_minutes: int
    logs: List[str]
    final_decision: str # "REASSIGN", "KEEP_AND_NOTIFY", "CANCEL"