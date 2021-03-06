import datetime
import sqlalchemy as sa
from babyday.data.modelbase import SqlAlchemyBase
import sqlalchemy.orm as orm
from dataclasses import dataclass


@dataclass
class Meal(SqlAlchemyBase):
    __tablename__ = "meals"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    item = sa.Column(sa.String, index=True)
    description = sa.Column(sa.String, nullable=True)
    quantity = sa.Column(sa.Integer, nullable=True)
    uom = sa.Column(sa.String)
    event_time = sa.Column(sa.DateTime, nullable=True)

    # Relationships
    person_id = sa.Column(sa.String, sa.ForeignKey("persons.id"))
    person = orm.relation("Person", back_populates="meals")

    account_id = sa.Column(sa.Integer, sa.ForeignKey("accounts.id"))

