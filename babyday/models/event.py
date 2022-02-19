from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Event(BaseModel):
    event_type: int
    person: int
    description: Optional[str] = ""
    event_time: Optional[datetime] = None
    quantity: Optional[int] = 0
    account_id: int

    class Config:
        anystr_strip_whitespace = True

