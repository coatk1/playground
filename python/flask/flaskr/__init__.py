# set FLASK_APP=flaskr
# set FLASK_ENV=development
# flask run
# http://127.0.0.1:5000/hello

import os

from flask import Flask


def create_app(test_config=None):

    # Create Flask instance with relative paths.
    app = Flask(__name__, instance_relative_config=True)

    # Configure the app with a secret key and database.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Load the instance config, if it exists, when not testing.
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    # Load the test config if passed in.
    else:
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists.
    try:
        os.makedirs(app.instance_path)

    except OSError:
        pass

    # A simple page that says hello.
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
