from flask import Blueprint
from flask.ext.security import Security

from .manager import login_manager, check_valid_login
from .security import user_datastore
from .forms import LoginForm

auth = Blueprint('auth', __name__, template_folder='../')


@auth.record_once
def on_registered(state):
    state.app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'auth/login.html'
    Security(
        state.app,
        user_datastore,
        login_form=LoginForm,
    )

    login_manager.init_app(state.app)
    state.app.before_request(check_valid_login)
