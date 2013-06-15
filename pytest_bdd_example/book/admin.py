from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from pytest_bdd_example.book import db, Book

admin = Admin()
admin.add_view(ModelView(Book, db.session, 'books', endpoint='books'))
