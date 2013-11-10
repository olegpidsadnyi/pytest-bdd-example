import pytest

from flaskr import flaskr


@pytest.fixture
def app():
    """Flask application."""
    return flaskr.app
