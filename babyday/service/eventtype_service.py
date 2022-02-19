import datetime

import babyday.data.db_session as db_session
from sqlalchemy.orm import Session
from babyday.data.eventtypes import EventType as DbEventType

def get_eventtypes(account_id):
    event_types = None
    with db_session.SessionContext(commit_on_success=True) as ctx:
        # find event types
        event_types = ctx.session.query(DbEventType.id,DbEventType.name)\
            .filter(DbEventType.account_id == account_id).all()
    return event_types