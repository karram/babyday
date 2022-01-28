import flask
import os
import data.db_session as db_session
from apis import meal


app = flask.Flask(__name__)
app.register_blueprint(meal.blueprint)

def main():
    db_init()
    app.run()


def db_init():
    db_file = os.path.join(os.path.dirname(__file__), 'db', 'bbdy.sqlite')
    db_session.global_init(db_file)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == '__main__':
    main()