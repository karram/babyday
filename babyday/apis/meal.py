import json

import flask
from babyday.models.meal import Meal
from babyday.models.person import Person
from babyday.models.mealentry import MealEntry
from babyday.service import person_service
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify


blueprint = flask.Blueprint("meal_api", "meal_api")


@blueprint.route("/api/addmeal", methods=["POST"])
def addmeal_direct():
    try:
        data = flask.request.get_json(force=True)
        mealentry = MealEntry(**data)

        db_meal_entry = person_service.add_meal(mealentry.person,
                                                mealentry.meal)

        return {"meal_entry_id": db_meal_entry.id}

    except ValidationError as ve:
        error_code = 422
        error_body = {"error": str(ve).replace("\n", " ")}
    except SQLAlchemyError as se:
        error_code = 500
        error_body = {"error": str(se).replace("\n", " ")}
    except Exception as x:
        error_code = 500
        error_body = {"error": str(x).replace("\n", " ")}

    return flask.Response(json.dumps(error_body),
                          status=error_code,
                          mimetype="application/json"
                          )


@blueprint.route("/api/user/<user_id>/meal", methods=["POST", "GET"])
def add_user_meal(user_id):
    if request.method == "POST":
        return add_meal_for_user(user_id)
    elif request.method == "GET":
        return get_user_meals(user_id)
    else:
        error_body = {"status": "Unknown request"}
        error_code = 500
        return flask.Response(json.dumps(error_body),
                              status=error_code,
                              mimetype="application/json"
                              )


def add_meal_for_user(user_id):
    try:
        data = flask.request.get_json(force=True)
        meal = Meal(**data)
        person = Person(id=user_id)
        db_meal_entry = person_service.add_meal(person, meal)
        return {"meal_id": db_meal_entry.id}

    except ValidationError as ve:
        error_code = 422
        error_body = {"error": str(ve).replace("\n", " ")}
    except SQLAlchemyError as se:
        error_code = 500
        error_body = {"error": str(se).replace("\n", " ")}
    except Exception as x:
        error_code = 500
        error_body = {"error": str(x).replace("\n", " ")}

    return flask.Response(json.dumps(error_body),
                          status=error_code,
                          mimetype="application/json"
                          )


def get_user_meals(user_id):
    person = Person(id=user_id)
    meal_entries = person_service.get_meals(person)
    return jsonify({"user_id": user_id, "meals": meal_entries})