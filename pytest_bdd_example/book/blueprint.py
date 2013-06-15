from flask import Blueprint

from .admin import admin

book = Blueprint('book', __name__)


@book.record_once
def on_registered(state):
    admin.init_app(state.app)
