from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

from skeleton_login_api import models
from skeleton_login_api.blueprints import register_blueprints

register_blueprints(app)
