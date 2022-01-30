import datetime
import babyday.data.db_session as db_session
from sqlalchemy.orm import Session
from babyday.data.account import Account
from babyday.data.account_user import User


def add_user(username: str, password: str):
    print(f"username={username}, password={password}")

    with db_session.SessionContext(commit_on_success=True) as ctx:
        # # Check if user already exists. If so, return error
        user = ctx.session.query(User).filter(User.id == username).first()
        if user:
            print(f"User exists : {user.id}")
            raise Exception(f"User already exists: {username}")

        # Else, create a new account and add user to this account
        account = Account(name=f"{username}_account")
        ctx.session.add(account)
        user = User(id=username, password=password)
        account.users.append(user)
    # return status
    return user

