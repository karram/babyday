from pydantic import BaseModel
from typing import List, Optional
import datetime
from models.meal import Meal
from models.person import Person


class MealEntry(BaseModel):
    person: Person
    meal: Meal

    class Config:
        anystr_strip_whitespace = True


