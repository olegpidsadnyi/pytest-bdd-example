from flask import Blueprint

from .models import db
from .admin import admin

book = Blueprint('book', __name__, template_folder='../')


@book.record_once
def on_registered(state):
    db.init_app(state.app)
    admin.init_app(state.app)
