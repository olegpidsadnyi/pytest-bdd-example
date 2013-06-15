from flask import current_app

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from pytest_bdd_example.book import Book

db = current_app.config['db']

admin = Admin()
admin.add_view(ModelView(Book, db.session, 'books', endpoint='books'))
