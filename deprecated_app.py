import flask
import os
import babyday.data.db_session as db_session
from babyday import auth


app = flask.Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
        SECRET_KEY='dev',
    )
#app.register_blueprint(meal.blueprint)
#app.register_blueprint(bodyfn.blueprint)
app.register_blueprint(auth.bp)


def main():
    db_init()
    app.run()


def db_init():
    db_file = os.path.join(app.instance_path, 'db', 'bbdy.sqlite')
    db_session.global_init(db_file)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == '__main__':
    main()