import os
from flask import Flask
from babyday.data.db_session import global_init


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    print(f"Instance path = {app.instance_path}")
    db_path = os.path.join(app.instance_path, 'db', 'bbdy.sqlite')
    print(f"DB path = {db_path}")
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db', 'bbdy.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from babyday.views import auth
    app.register_blueprint(auth.bp)

    from babyday.views import mainpage
    app.register_blueprint(mainpage.bp)
    app.add_url_rule('/', endpoint='index')

    from babyday.views import eat
    app.register_blueprint(eat.bp)

    global_init(db_path)
    return app
