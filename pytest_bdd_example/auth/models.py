from flask.ext.security import UserMixin

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    is_active = db.Column(db.Boolean, default=False)
