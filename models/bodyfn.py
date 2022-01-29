from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class BodyFn(BaseModel):
    item: str
    description = ""
    event_time: Optional[datetime] = None

    class Config:
        anystr_strip_whitespace = True

