import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import babyday.service.user_service as user_service

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html')
