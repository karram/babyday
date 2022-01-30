import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from babyday.data.modelbase import SqlAlchemyBase
from dataclasses import dataclass


@dataclass
class BodyFunction(SqlAlchemyBase):
    __tablename__ = "bodyfunctions"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    item = sa.Column(sa.String, index=True)
    description = sa.Column(sa.String, nullable=True)
    event_time = sa.Column(sa.DateTime)

    # Relationships
    person_id = sa.Column(sa.Integer, sa.ForeignKey("persons.id"))
    person = orm.relation("Person", back_populates="bodyfunctions")

