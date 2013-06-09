import os
import pytest

import pytest_bdd_example as main_pkg
from tests.fixtures.auth import *


@pytest.fixture
def pytestbdd_feature_base_dir():
    """Feature files base directory."""
    return os.path.join(
        os.path.dirname(
            os.path.dirname(main_pkg.__file__)
        ), 'features',
    )
