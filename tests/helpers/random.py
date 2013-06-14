from __future__ import absolute_import

import random
import string


def random_string(length=20):
    """Create a random string."""
    alphanums = string.ascii_lowercase + string.digits
    return ''.join(random.choice(alphanums) for _ in xrange(length))
