import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.modelbase import SqlAlchemyBase
from data.meals import Meal
from data.bodyfn import BodyFunction
from dataclasses import dataclass


@dataclass
class Person(SqlAlchemyBase):
    __tablename__ = "persons"

    id = sa.Column(sa.String, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    firstname = sa.Column(sa.String, index=True)
    lastname = sa.Column(sa.String, index=True, nullable=True)
    date_of_birth = sa.Column(sa.Date, nullable=True)

    # Relationships
    meals = orm.relation("Meal", order_by=[
        Meal.event_time
    ], back_populates="person")

    bodyfunctions = orm.relation("BodyFunction", order_by=[
        BodyFunction.event_time
    ], back_populates="person")

