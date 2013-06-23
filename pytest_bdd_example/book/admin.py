from flask import current_app
from flask.ext.admin.contrib.sqlamodel import ModelView

from flask.ext.principal import Permission, RoleNeed

from pytest_bdd_example.book import db, Book, Author


admin = current_app.extensions['admin'][0]


class AuthorView(ModelView):

    def is_visible(self):
        return Permission(RoleNeed('admin')).can()


admin.add_view(
    AuthorView(
        Author,
        db.session,
        'authors',
        endpoint='authors',
    )
)


admin.add_view(
    ModelView(
        Book,
        db.session,
        'books',
        endpoint='books',
    )
)


