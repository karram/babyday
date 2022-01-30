import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from babyday.data.modelbase import SqlAlchemyBase
from babyday.data.account_user import User
from dataclasses import dataclass


@dataclass
class Account(SqlAlchemyBase):
    __tablename__ = "accounts"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    name = sa.Column(sa.String, index=True)

    # Relationships
    users = orm.relation("User", order_by=[
        User.created_at
    ], back_populates="account")


