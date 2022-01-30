from pydantic import BaseModel
from typing import List, Optional
import datetime


class User(BaseModel):
    id: str
    firstname: Optional[str]
    lastname: Optional[str]
    dob: Optional[datetime.datetime]

    class Config:
        anystr_strip_whitespace = True


