import datetime

import babyday.data.db_session as db_session
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from babyday.data.eventtypes import EventType as DbEventType
from babyday.data.events import Event as DbEvent
from babyday.data.person import Person as DbPerson
from babyday.models.person import Person
from babyday.models.event import Event

def add_event(p: Person, e: Event ):
    evt = None
    with db_session.SessionContext(commit_on_success=True) as ctx:
        # find person
        person = ctx.session.query(DbPerson)\
            .filter(DbPerson.id == p.id, DbPerson.account_id == p.account_id).first()
        if not person:
            raise Exception(f"Person {p.id} does not exist in account {p.account_id}")
        # add event
        evt = DbEvent(event_id = e.event_type, person_id = p.id, \
            description = e.description, quantity = e.quantity, \
            event_time = e.event_time, account_id = e.account_id)
        person.events.append(evt)
    # return status
    return evt

def get_all_events(account_id):
    events = None
    with db_session.SessionContext(commit_on_success=True) as ctx:
        # find person
        events = ctx.session.query(DbEvent).\
            options(joinedload(DbEvent.person, innerjoin=True)).\
            options(joinedload(DbEvent.event_type, innerjoin=True)).\
            order_by(DbEvent.event_time.desc()).\
            filter(DbEvent.account_id == account_id).all()
    return events