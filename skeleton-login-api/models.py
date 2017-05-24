from skeleton-login-api import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm.session import Session

class Test_table_1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    info = db.Column(db.String(64))

class Test_table_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    col_1 = db.Column(db.String(64))
    col_2 = db.Column(db.String(64))
    col_3 = db.Column(db.String(64))

class Test_table_3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    col_1 = db.Column(db.String(64))
    col_2 = db.Column(db.String(64))
    col_3 = db.Column(db.String(64))
