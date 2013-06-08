from flask import Blueprint, Flask, url_for, redirect

from flask.ext.admin import Admin
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

from pytest_bdd_example.dashboard import settings

login_manager = LoginManager()

app = Flask(__name__, static_folder=settings.MEDIA_ROOT, template_folder=settings.TEMPLATES_ROOT)
app.config.from_object('pytest_bdd_example.dashboard.settings')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

db = SQLAlchemy(app)

from flask.ext.admin.contrib.sqlamodel import ModelView

from pytest_bdd_example.dashboard.models import User

from pytest_bdd_example.dashboard.views import *

app.register_blueprint(bp, url_prefix='/dashboard')

admin_panel = Admin(app)
admin_panel.add_view(ModelView(User, db.session, endpoint='users'))

login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('dashboard.login'))



