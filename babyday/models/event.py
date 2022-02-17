from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Event(BaseModel):
    event: str
    description = ""
    event_time: Optional[datetime] = None
    quantity: int
    uom: Optional[str] = None
    account_id: str

    class Config:
        anystr_strip_whitespace = True

