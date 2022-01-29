from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Meal(BaseModel):
    item: str
    description = ""
    quantity: int
    uom: str
    event_time: Optional[datetime] = None

    class Config:
        anystr_strip_whitespace = True

