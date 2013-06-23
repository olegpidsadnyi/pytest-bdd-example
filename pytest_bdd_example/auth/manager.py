from flask import request, current_app

from flask.ext.login import LoginManager, current_user

from .security import user_datastore


login_manager = LoginManager()
login_manager.login_view = 'security.login'


PUBLIC_ENDPOINTS = [
    'static',
    'security.login',
]


def check_valid_login():
    if request.endpoint in PUBLIC_ENDPOINTS:
        return

    if getattr(current_app.view_functions.get(request.endpoint), 'is_public', False):
        return

    if not current_user.is_authenticated():
        return current_app.login_manager.unauthorized()


@login_manager.user_loader
def load_user(userid):
    return user_datastore.find_user(id=userid)
