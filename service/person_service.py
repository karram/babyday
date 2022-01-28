import datetime

import data.db_session
from models.person import Person
from models.meal import Meal
from sqlalchemy.orm import Session
from data.person import Person as DbPerson
from data.meals import Meal as DbMeal


def add_meal(p: Person, m: Meal):
    meal = None
    with data.db_session.SessionContext(commit_on_success=True) as ctx:
        # find person
        person = ctx.session.query(DbPerson).filter(DbPerson.id == p.id).first()
        if not person:
            raise Exception("User not found")
        # add meal
        meal = DbMeal(item=m.item, quantity=m.quantity, uom=m.uom,
                      event_time=m.event_time, description=m.description)
        person.meals.append(meal)
    # return status
    return meal

