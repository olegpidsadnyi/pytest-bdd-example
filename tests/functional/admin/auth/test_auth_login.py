from pytest_bdd import scenario, given, when, then


test_successful_login = scenario(
    'auth/admin_login.feature',
    'Successful login',
)


@given('I\'m an admin user')
def admin_user(user):
    pass


@when('I go to the admin login page')
def go_to_login_page(browser):
    pass


@when('I fill in the login credentials')
def fill_in_login_credentials():
    pass


@when('I post the form')
def post_the_form():
    pass


@then('I should see an error message')
def should_see_error_message():
    pass


@then('I shouldn\'t see an error message')
def shouldnt_see_error_message():
    pass


@then('I should see the Dashboard page')
def should_see_dashboard():
    pass


test_successful_login = scenario(
    'auth/admin_login.feature',
    'Unsuccessful login',
)


@when('I fill in wrong login credentials')
def fill_in_wrong_credentials():
    pass
