import os
import pytest

import pytest_bdd_example
from .fixtures.auth import *


@pytest.fixture
def pytestbdd_feature_base_dir():
    """Feature files base directory."""
    return os.path.join(
        os.path.dirname(
            os.path.dirname(pytest_bdd_example.__file__)
        ), 'features', 'shop',
    )
