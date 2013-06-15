import pytest

from pytest_bdd_example.auth.models import User

from tests.helpers.random import random_string


@pytest.fixture
def password():
    return 'asdasd'


@pytest.fixture
def user(password):
    session = User.query.session
    u = User(
        username=u'{0}'.format(random_string(7)),
        email="{0}@example.com".format(random_string(7)),
        password=password,
    )
    session.add(u)
    session.commit()
    return u
