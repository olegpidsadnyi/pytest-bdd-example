from flask import render_template
from flask.ext.login import current_user

from pytest_bdd_example.dashboard import bp

# @bp.route('/')
# def index(template='dashboatd.html'):
#
#     if not current_user.is_authenticated():
#         template = "login.html"
#
#     return render_template(template)
