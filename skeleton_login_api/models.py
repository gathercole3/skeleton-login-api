from skeleton_login_api import db
from sqlalchemy.orm.session import Session

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    google_id = db.Column(db.String(64))

    def to_dict(self):
        return {
            "id" : self.id,
            "email" : self.email
        }
