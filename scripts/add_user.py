import babyday.data.db_session
from babyday.data.person import Person
import datetime
import os


def db_init():
    db_file = os.path.join(os.path.dirname(__file__), '../babyday', 'db', 'bbdy.sqlite')
    data.db_session.global_init(db_file)


db_init()

with data.db_session.SessionContext(commit_on_success=True) as ctx:
    # find person
    person = Person(id="niam")

    ctx.session.add(person)

print("Added user.")


def db_init():
    db_file = os.path.join(os.path.dirname(__file__), '../babyday', 'db', 'bbdy.sqlite')
    data.db_session.global_init(db_file)

