import datetime
import sqlalchemy as sa
from babyday.data.modelbase import SqlAlchemyBase
import sqlalchemy.orm as orm
from dataclasses import dataclass


@dataclass
class EventType(SqlAlchemyBase):
    __tablename__ = "eventtypes"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    name = sa.Column(sa.String, index=True)
    description = sa.Column(sa.String, nullable=True)

    account_id = sa.Column(sa.Integer, sa.ForeignKey("accounts.id"))

