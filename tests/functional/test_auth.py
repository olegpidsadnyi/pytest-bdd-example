import re
from urlparse import urljoin

from pytest_bdd import given, when, scenario


test_sucsessful_login = scenario(
    "auth/login.feature",
    "Successful login",
)

test_invalid_username = scenario(
    "auth/login.feature",
    "Invalid username",
)

test_ivalid_password = scenario(
    "auth/login.feature",
    "Invalid password",
)


@when("I go to login page")
def go_to_login_page(browser):
    browser.visit(urljoin(browser.url, "/login"))


@when(re.compile('I enter "(?P<username>\w+)" username'))
def enter_username(browser, username):
    browser.fill("username", username)


@when(re.compile('I enter "(?P<password>\w+)" password'))
def enter_password(browser, password):
    browser.fill("password", password)


@when('I click login button')
def click_login(browser):
    button = browser.find_by_css("input[type=submit]").first
    button.click()
