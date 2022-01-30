import datetime

import babyday.data.db_session
from babyday.models.person import Person
from babyday.models.meal import Meal
from babyday.models.bodyfn import BodyFn
from sqlalchemy.orm import Session
from babyday.data.person import Person as DbPerson
from babyday.data.meals import Meal as DbMeal
from babyday.data.bodyfn import BodyFunction as DbBodyFn


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


def get_meals(p: Person):
    meals = None
    with data.db_session.SessionContext(commit_on_success=True) as ctx:
        # find person
        person = ctx.session.query(DbPerson).filter(DbPerson.id == p.id).first()
        if not person:
            raise Exception("User not found")
        # get a list of meals
        meals = ctx.session.query(DbMeal.id,DbMeal.event_time,
                                  DbMeal.item, DbMeal.description,
                                  DbMeal.quantity, DbMeal.uom)\
                .filter(DbPerson.id == p.id)\
                .order_by(DbMeal.event_time.desc())\
                .all()
        m2 = [x._asdict() for x in meals]
        print(m2)
    # return status
    return m2


def add_bodyfn(p: Person, b: BodyFn):
    bodyfn = None
    with data.db_session.SessionContext(commit_on_success=True) as ctx:
        # find person
        person = ctx.session.query(DbPerson).filter(DbPerson.id == p.id).first()
        if not person:
            raise Exception("User not found")
        # add meal
        bodyfn = DbBodyFn(item=b.item, event_time=b.event_time, description=b.description)
        person.bodyfunctions.append(bodyfn)
    # return status
    return bodyfn


def get_bodyfns(p: Person):
    bodyfns = None
    with data.db_session.SessionContext(commit_on_success=True) as ctx:
        # find person
        person = ctx.session.query(DbPerson).filter(DbPerson.id == p.id).first()
        if not person:
            raise Exception("User not found")
        # get a list of meals
        bodyfns = ctx.session.query(DbBodyFn.id, DbBodyFn.item,
                                    DbBodyFn.description, DbBodyFn.event_time)\
                .filter(DbPerson.id == p.id)\
                .order_by(DbBodyFn.event_time.desc())\
                .all()
        m2 = [x._asdict() for x in bodyfns]
        print(m2)
    # return status
    return m2

