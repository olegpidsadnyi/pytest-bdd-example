import pytest

from pytest_bdd_example.dashboard.models import User
from pytest_bdd_example.dashboard import db

from tests.helpers.random import random_string


@pytest.fixture
def password():
    return 'asdasd'


@pytest.fixture
def user(password):
    u = User(
        username=random_string(),
        password=password,
    )
    db.session.add(u)
    db.session.commit()
    return u
