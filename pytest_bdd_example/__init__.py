from flask import Flask
from flask.ext.admin import Admin
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('settings')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

db = SQLAlchemy(app)

from flask.ext.admin.contrib.sqlamodel import ModelView

from pytest_bdd_example import dashboard
from pytest_bdd_example.dashboard.models import User


app.register_blueprint(dashboard.bp, url_prefix='/dashboard')

login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    return User.get(userid)


admin_panel = Admin(app)
admin_panel.add_view(ModelView(User, db.session, endpoint='users'))
