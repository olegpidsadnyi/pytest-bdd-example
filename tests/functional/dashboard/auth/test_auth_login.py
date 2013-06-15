import pytest
from pytest_bdd import scenario, given, when, then


@pytest.fixture
def pytestbdd_close_browser():
    """Close browser fixture."""
    return False


test_successful_login = scenario(
    'auth/admin_login.feature',
    'Successful login',
)


@given('I\'m an admin user')
def admin_user(user):
    return user


@when('I go to the admin login page')
def go_to_login_page(browser):
    browser.visit('http://127.0.0.1:5000')


@when('I fill in the login credentials')
def fill_in_login_credentials(browser, user, password):
    browser.fill('username', user.username)
    browser.fill('password', password)


@when('I post the form')
def post_the_form(browser):
    browser.find_by_css('button[type=submit]').first.click()


@then('I should see an error message')
def should_see_error_message():
    pass


@then('I shouldn\'t see an error message')
def shouldnt_see_error_message(browser):
    pass


@then('I should see the Dashboard page')
def should_see_dashboard(browser):
    assert not browser.is_text_present('Please sign in')


# test_successful_login = scenario(
#     'auth/admin_login.feature',
#     'Unsuccessful login',
# )


@when('I fill in wrong login credentials')
def fill_in_wrong_credentials():
    pass
