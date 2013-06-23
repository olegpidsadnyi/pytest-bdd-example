from pytest_bdd_example.dashboard import app

from .steps.given import *


with app.app_context():
    """Initialize the application context."""
    pass
