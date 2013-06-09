from flask import request, current_app

from flask.ext.login import LoginManager, current_user

from .models import User


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def check_valid_login():
    if 'static' == request.endpoint:
        return

    if getattr(current_app.view_functions.get(request.endpoint), 'is_public', False):
        return

    if not current_user.is_authenticated():
        return current_app.login_manager.unauthorized()


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
