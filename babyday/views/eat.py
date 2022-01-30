import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import babyday.service.person_service as person_service
from babyday.views.auth import login_required

bp = Blueprint('eat', __name__, url_prefix='/person')


@bp.route('/eat', methods=('GET', 'POST'))
@login_required
def new_meal():
    if request.method == "POST":
        pass
    return render_template('eat/new_meal.html')

