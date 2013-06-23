from flask import Blueprint
from .admin import admin

book = Blueprint('book', __name__)


__all__ = ['book', 'admin']
