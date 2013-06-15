from flask.ext.wtf import Form

from wtforms import TextField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    username = TextField('Username', [Required()])
    password = PasswordField('Password', [Required()])
