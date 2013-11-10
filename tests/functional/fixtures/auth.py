import pytest


@pytest.fixture
def credentials():
    """Login credentials."""
    return {
        'username': 'admin',
        'password': 'default',
        'login': True,
    }
