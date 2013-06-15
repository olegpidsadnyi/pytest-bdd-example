from flask import current_app

from flask.ext.security import UserMixin


db = current_app.extensions['sqlalchemy'].db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    active = db.Column(db.Boolean, default=False)

    def get_id(self):
        return unicode(self.id)

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False
