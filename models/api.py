from pydantic import BaseModel


class AlertTrafficInput(BaseModel):
    order_id: str
    current_driver: str
    delay_minutes: int