from flask import current_app

from pytest_bdd_example.auth import user_datastore


def create_initial_data():
    print 'Populating the initial data...'
    db = current_app.extensions['sqlalchemy'].db

    print 'Creating roles...'
    admin_role = user_datastore.create_role(
        name='admin',
        description='Administrators',
    )

    author_role = user_datastore.create_role(
        name='author',
        description='Book authors',
    )

    print 'Admin user: admin/asdasd'
    admin = user_datastore.create_user(
        username='admin',
        password='asdasd',
        active=True,
    )
    user_datastore.add_role_to_user(admin, admin_role)

    print 'Author user: author/asdasd'
    author = user_datastore.create_user(
        username='author',
        password='asdasd',
        active=True,
    )
    user_datastore.add_role_to_user(author, author_role)

    #TODO: add other data here...
    db.session.commit()
