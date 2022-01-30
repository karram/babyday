import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from babyday.data.modelbase import SqlAlchemyBase
from dataclasses import dataclass


@dataclass
class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sa.Column(sa.String, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    password = sa.Column(sa.String, primary_key=True)
    firstname = sa.Column(sa.String, index=True)
    lastname = sa.Column(sa.String, index=True, nullable=True)

    # Relationships
    account_id = sa.Column(sa.Integer, sa.ForeignKey("accounts.id"))
    account = orm.relation("Account", back_populates="users")

