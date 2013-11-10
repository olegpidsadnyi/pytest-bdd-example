from urlparse import urljoin
import pytest


@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000/"


@pytest.fixture
def browser(browser, base_url, credentials):

    if credentials["login"]:
        browser.visit(urljoin(base_url, "/login"))

        browser.fill("username", credentials["username"])
        browser.fill("password", credentials["password"])
        button = browser.find_by_css("input[type=submit]").first
        button.click()
    else:
        browser.visit(base_url)
    return browser
