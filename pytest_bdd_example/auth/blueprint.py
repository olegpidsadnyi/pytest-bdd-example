from flask import Blueprint

from .manager import login_manager, check_valid_login
from .models import db

auth = Blueprint('auth', __name__, template_folder='auth')


@auth.record_once
def on_registered(state):
    db.init_app(state.app)

    login_manager.init_app(state.app)
    state.app.before_request(check_valid_login)
