import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from babyday.data.modelbase import SqlAlchemyBase
from babyday.data.events import Event
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
    account_id = sa.Column(sa.Integer, sa.ForeignKey("accounts.id"))

    events = orm.relation("Event", order_by=[
        Event.event_time
    ], back_populates="person")

