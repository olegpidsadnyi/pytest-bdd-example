from flask import Flask, Blueprint
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)

from pytest_bdd_example import admin
from pytest_bdd_example.admin.models import User

app.register_blueprint(admin.bp, url_prefix='/admin')

login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)


