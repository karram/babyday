import json

import flask
from models.meal import Meal
from models.person import Person
from models.mealentry import MealEntry
from service import person_service
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

blueprint = flask.Blueprint("meal_api", "meal_api")


@blueprint.route("/api/addmeal", methods=["POST"])
def addmeal():
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
