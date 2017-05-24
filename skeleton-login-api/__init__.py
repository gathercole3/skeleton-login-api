from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

from skeleton-login-api import models
from skeleton-login-api.blueprints import register_blueprints

register_blueprints(app)
