from flask import current_app

from pytest_bdd_example.auth.models import User


def create_initial_data():
    print 'Populating the initial data...'
    db = current_app.extensions['sqlalchemy'].db

    print 'Dashboard user: admin/asdasd'
    admin = User(
        username='admin',
        password='asdasd',
        active=True,
    )
    db.session.add(admin)

    #TODO: add other data here...

    db.session.commit()
