from flask import current_app

from flask.ext.security import UserMixin, RoleMixin


db = current_app.extensions['sqlalchemy'].db


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))
    active = db.Column(db.Boolean, default=False)

    roles = db.relationship(
        Role,
        secondary=lambda: roles_users,
        backref=db.backref('users', lazy='dynamic'),
    )

    def get_id(self):
        return unicode(self.id)

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey(User.id)),
    db.Column('role_id', db.Integer(), db.ForeignKey(Role.id)),
)
