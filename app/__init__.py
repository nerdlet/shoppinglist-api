
# include third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import from instance folder
from config import app_config

# initialize db
db = SQLAlchemy()

#wrap everything up in a flask object
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app