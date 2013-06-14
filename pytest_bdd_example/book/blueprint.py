from flask import Blueprint

from .models import db

book = Blueprint('book', __name__, template_folder='../')


@book.record_once
def on_registered(state):
    db.init_app(state.app)
