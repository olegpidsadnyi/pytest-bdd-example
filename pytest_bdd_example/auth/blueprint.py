from flask import Blueprint

from .manager import login_manager, check_valid_login

auth = Blueprint('auth', __name__, template_folder='../')


@auth.record_once
def on_registered(state):
    login_manager.init_app(state.app)
    state.app.before_request(check_valid_login)
