from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from pytest_bdd_example.book import Book, db

admin = Admin()
admin.add_view(ModelView(Book, db.Session(), 'books', endpoint='books'))