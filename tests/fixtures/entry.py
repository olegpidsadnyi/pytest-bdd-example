import pytest

import datetime


@pytest.fixture
def title():
    return "Entry for {0}".format(datetime.datetime.now())


@pytest.fixture
def text():
    """Entry text."""
    return "Hello world text!"


@pytest.fixture
def entry(db, title, text):
    """Blog entry."""
    db.execute('insert into entries (title, text) values (?, ?)', [title, text])
    db.commit()
    return title, text
