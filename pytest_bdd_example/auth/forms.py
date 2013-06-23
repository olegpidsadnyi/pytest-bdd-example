from flask.ext.wtf import Form

from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required
from flask.ext.security.forms import NextFormMixin
from flask.ext.security.utils import verify_and_update_password, get_message
from flask.ext.security.confirmable import requires_confirmation

from .security import user_datastore


class LoginForm(Form, NextFormMixin):
    username = TextField('Username', [Required()])
    password = PasswordField('Password', [Required()])
    remember = BooleanField('Remember me')

    def validate(self):
        if not super(LoginForm, self).validate():
            return False

        username = self.username.data.strip()
        password = self.password.data.strip()
        if username == '':
            self.username.errors.append(get_message('EMAIL_NOT_PROVIDED')[0])
            return False

        if password == '':
            self.password.errors.append(get_message('PASSWORD_NOT_PROVIDED')[0])
            return False

        self.user = user_datastore.find_user(username=username)

        if self.user is None:
            self.username.errors.append(get_message('USER_DOES_NOT_EXIST')[0])
            return False

        if not verify_and_update_password(password, self.user):
            self.password.errors.append(get_message('INVALID_PASSWORD')[0])
            return False

        if requires_confirmation(self.user):
            self.username.errors.append(get_message('CONFIRMATION_REQUIRED')[0])
            return False
        if not self.user.is_active():
            self.username.errors.append(get_message('DISABLED_ACCOUNT')[0])
            return False
        return True
