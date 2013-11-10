import os
import pytest

from .fixtures.browser import *
from .fixtures.auth import *
from .fixtures.steps import *


@pytest.fixture(scope='session')
def pytestbdd_selenium_speed():
    return 0.5


@pytest.fixture
def pytestbdd_feature_base_dir():
    """Feature files base directory."""
    return os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            '..',
            'features',
        )
    )
