import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import babyday.service.person_service as person_service
from babyday.views.auth import login_required
from babyday.models.person import Person
from babyday.models.meal import Meal
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('eat', __name__, url_prefix='/person')


@bp.route('/eat', methods=('GET', 'POST'))
@login_required
def new_meal():

    if request.method == "POST":
        error = None
        try:
            person = request.form['person']
            item = request.form['item']
            quantity = request.form['quantity']
            uom = request.form['uom']
            event_time = request.form['event_time']

            meal = Meal(item=item, quantity=quantity, uom=uom, event_time=event_time)
            person = Person(id=person)
            db_meal_entry = person_service.add_meal(person, meal)
            flash(f"Added entry: {db_meal_entry.id}")

        except ValidationError as ve:
            error = {"Validation error": str(ve).replace("\n", " ")}
        except SQLAlchemyError as se:
            error = {"DB Row error": str(se).replace("\n", " ")}
        except Exception as x:
            error = {"Generic error": str(x).replace("\n", " ")}

        if error:
            flash(error)

    return render_template('eat/new_meal.html')

