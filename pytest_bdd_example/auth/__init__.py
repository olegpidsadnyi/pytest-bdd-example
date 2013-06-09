from flask import Blueprint

from .decorators import public_endpoint
from .manager import login_manager, check_valid_login
from .models import db

__all__ = ['bp', 'db', 'public_endpoint']

bp = Blueprint('auth', __name__, template_folder='auth')


@bp.record_once
def on_registered(state):
    db.init_app(state.app)

    login_manager.init_app(state.app)
    state.app.before_request(check_valid_login)


from .views import *
