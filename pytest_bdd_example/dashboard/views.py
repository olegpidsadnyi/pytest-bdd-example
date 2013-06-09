from flask import render_template, Blueprint, url_for, redirect
from flask.ext.login import login_required, login_user

from pytest_bdd_example.dashboard import User
from pytest_bdd_example.dashboard.forms import LoginForm

bp = Blueprint('dashboard', __name__)


@bp.route('/')
@login_required
def index(template='dashboard.html'):
    return render_template(template)


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        login_user(user)
        return redirect(url_for('dashboard.index'))

    return render_template("login.html", **{
        'form': login_form,
    })