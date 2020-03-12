import os

from flask import Flask, g, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow


db = MySQL()
ma = Marshmallow()


def create_app(config=None, debug=False):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.debug = debug

    # Initialize plugins.

    # ma.init_app(app)
    if config is not None:
        app.config.from_object(config)

    app.config['MYSQL_USER'] = 'foodApp'
    # 'food123.'
    app.config['MYSQL_PASSWORD'] = 'foodApp123.'
    # 'localhost'
    app.config['MYSQL_HOST'] = 'localhost'
    # 'foodDB'
    app.config['MYSQL_DB'] = 'foodDB'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    # Initialize plugins
    db.init_app(app)  # Initialize first the db context.
    ma.init_app(app)

    # Blueprints routes
    from .food import food_routes  # Then import the routes (bluprints)

    # # return app
    with app.app_context():
        # register Blueprints.
        app.register_blueprint(food_routes.food_bp, url_prefix="/v1/api")

    return app
