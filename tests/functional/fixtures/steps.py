"""Common steps."""

import re
from urlparse import urljoin

from pytest_bdd import given, when, then


@then(re.compile('I should see "(?P<text>.+)"'))
def i_should_see(browser, text):
    assert browser.is_text_present(text)


@given("I'm not logged in")
@given("I'm a visitor")  # Step alias
def not_logged_in(credentials):
    """99%% of the cases you test logged in.

    Specify not logged in state to be explicit.

    """
    credentials['login'] = False


@given("I'm an admin")
def logged_in(credentials):
    credentials['login'] = True


# Re-use of the fixture
given("I have an entry", fixture="entry")


@when("I go to the blog")
def go_to_blog(browser):
    browser.visit(urljoin(browser.url, "/"))
