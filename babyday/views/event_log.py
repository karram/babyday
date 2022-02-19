import functools
from typing import List

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import babyday.service.person_service as person_service
import babyday.service.eventtype_service as eventtype_service
import babyday.service.event_service as event_service
from babyday.data.events import Event

bp = Blueprint('event', __name__)

@bp.route('/eventlog', methods=['GET'])
def get_full_log():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    account_id = session['account_id']
    events:List[Event] = event_service.get_all_events(account_id)
    for event in events:
        print(event.person.firstname)
    return render_template('event/event_log.html', events = events)
