from flask import current_app
from flask.ext.admin.contrib.sqlamodel import ModelView

from flask.ext.principal import Permission, RoleNeed

from pytest_bdd_example.book import db, Book, Author


admin = current_app.extensions['admin'][0]

admin_role = Permission(RoleNeed('admin'))


class AuthorView(ModelView):
    """Author view.

    Only admin can see it.
    """
    def is_visible(self):
        return admin_role.can()

    def is_accessible(self):
        return admin_role.can()


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


