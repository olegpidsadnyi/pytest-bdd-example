from flask import request, url_for, redirect, render_template
from flask.ext.login import login_user

from .blueprint import auth
from .decorators import public_endpoint
from .forms import LoginForm
from .models import User


@auth.route('/login/', methods=['GET', 'POST'])
@public_endpoint
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        return redirect(request.args.get('next') or url_for('index'))

    return render_template('auth/login.html', form=form,)
