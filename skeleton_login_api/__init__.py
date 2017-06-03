from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from skeleton_login_api import models
from skeleton_login_api.blueprints import register_blueprints
from skeleton_login_api.exceptions import register_exception_handlers

register_exception_handlers(app)
register_blueprints(app)
