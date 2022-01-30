import json

import flask
from babyday.models.person import Person
from babyday.models.bodyfn import BodyFn
from babyday.service import person_service
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify


blueprint = flask.Blueprint("bodyfn_api", "bodyfn_api")


@blueprint.route("/api/user/<user_id>/bodyfn", methods=["POST", "GET"])
def add_bodyfn(user_id):
    if request.method == "POST":
        return add_bodyfn_for_user(user_id)
    elif request.method == "GET":
        return get_user_bodyfns(user_id)
    else:
        error_body = {"status": "Unknown request"}
        error_code = 500
        return flask.Response(json.dumps(error_body),
                              status=error_code,
                              mimetype="application/json"
                              )


def add_bodyfn_for_user(user_id):
    try:
        data = flask.request.get_json(force=True)
        bodyfn = BodyFn(**data)
        person = Person(id=user_id)
        db_bodyfn_entry = person_service.add_bodyfn(person, bodyfn)
        return {"bodyfn_id": db_bodyfn_entry.id}

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


def get_user_bodyfns(user_id):
    person = Person(id=user_id)
    bodyfn_entries = person_service.get_bodyfns(person)
    return jsonify({"user_id": user_id, "bodyfns": bodyfn_entries})