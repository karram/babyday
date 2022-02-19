import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import babyday.service.user_service as user_service
import babyday.service.person_service as person_service
import babyday.service.eventtype_service as eventtype_service
import babyday.service.event_service as event_service
from babyday.models.person import Person
from babyday.models.event import Event

bp = Blueprint('main', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        return process_post()
    else:
        return process_get()


def process_get():
    if 'user_id' in session:
        persons = person_service.get_persons(session['account_id'])
        event_types = eventtype_service.get_eventtypes(session['account_id'])
        return render_template('main/index.html', persons = persons, event_types = event_types)
    else:
        return redirect(url_for('auth.login'))

def process_post():
        person_id = request.form['person']
        event_type = request.form['event']
        event_time = request.form['event_time']
        quantity = request.form['quantity']
        description = request.form['description']
        account_id = session['account_id']

        person = Person(id=person_id, account_id=account_id)
        event = Event(event_type=event_type, person = person.id, description = description,\
            quantity = quantity, event_time = event_time, account_id = account_id)
        event_entry = event_service.add_event(person, event)
        flash(f"Added entry: {event_entry.id}")
        return process_get()