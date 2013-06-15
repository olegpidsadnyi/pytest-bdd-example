import pytest

from pytest_bdd_example.auth.models import User
from pytest_bdd_example.dashboard.app import db

from tests.helpers.random import random_string


@pytest.fixture
def password():
    return 'asdasd'


@pytest.fixture
def user(password):
    u = User(
        username=u'{0}'.format(random_string(7)),
        email="{0}@example.com".format(random_string(7)),
        password=password,
    )
    db.session.add(u)
    db.session.commit()
    return u
