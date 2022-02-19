import datetime
import sqlalchemy as sa
from babyday.data.modelbase import SqlAlchemyBase
import sqlalchemy.orm as orm
from dataclasses import dataclass


@dataclass
class Event(SqlAlchemyBase):
    __tablename__ = "events"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    description = sa.Column(sa.String, nullable=True)
    quantity = sa.Column(sa.Integer, nullable=True)
    event_time = sa.Column(sa.DateTime, nullable=True, default=datetime.datetime.now)

    # Relationships
    event_id = sa.Column(sa.String, sa.ForeignKey("eventtypes.id"))
    event_type = orm.relation("EventType")

    person_id = sa.Column(sa.String, sa.ForeignKey("persons.id"))
    person = orm.relation("Person", back_populates="events")

    account_id = sa.Column(sa.Integer, sa.ForeignKey("accounts.id"))

