import pytest

from flaskr import flaskr


@pytest.fixture
def db():
    """Database connection."""
    return flaskr.connect_db()
