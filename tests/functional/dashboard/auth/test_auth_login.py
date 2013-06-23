import pytest
import splinter

from pytest_bdd import scenario, when, then


test_successful_login = scenario(
    'auth/dashboard_login.feature',
    'Successful login',
)


@when('I go to the admin login page')
def go_to_login_page(browser):
    browser.visit('http://127.0.0.1:5000/login')


@when('I fill in the login credentials')
def fill_in_login_credentials(browser, user, password):
    browser.fill('username', user.username)
    browser.fill('password', password)


@when('I post the form')
def post_the_form(browser):
    browser.find_by_css('button[type=submit]').first.click()


@then('I should see an error message')
def should_see_error_message(browser):
    assert browser.find_by_css('.alert-error').first


@then('I shouldn\'t see an error message')
def shouldnt_see_error_message(browser):
    with pytest.raises(splinter.exceptions.ElementDoesNotExist):
        browser.find_by_css('.alert-error').first


@then('I should see the Dashboard page')
def should_see_dashboard(browser):
    assert not browser.is_text_present('Please sign in')


test_unsuccessful_login = scenario(
    'auth/dashboard_login.feature',
    'Unsuccessful login',
)


@when('I fill in wrong login credentials')
def fill_in_wrong_credentials(browser):
    browser.fill('username', 'HELP!')
    browser.fill('password', 'I pressed any key')
