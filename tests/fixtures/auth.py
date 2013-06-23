import pytest

from pytest_bdd_example.auth.models import db
from pytest_bdd_example.auth import user_datastore

from tests.helpers.random import random_string


@pytest.fixture
def password():
    return 'asdasd'


@pytest.fixture
def user(password):
    """Dashboard user."""
    u = user_datastore.create_user(
        username=u'{0}'.format(random_string()),
        email="{0}@example.com".format(random_string(7)),
        password=password,
        active=True,
    )

    db.session.commit()
    return u


@pytest.fixture
def admin_user(user):
    admin_role = user_datastore.find_or_create_role(
        name='admin',
        description='Administrators',
    )
    user_datastore.add_role_to_user(user, admin_role)
    db.session.commit()


@pytest.fixture
def author_user(user):
    author_role = user_datastore.find_or_create_role(
        name='author',
        description='Book authors',
    )
    user_datastore.add_role_to_user(user, author_role)
    db.session.commit()
