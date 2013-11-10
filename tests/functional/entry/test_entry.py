from pytest_bdd import scenario, when, then

test_entry_is_displayed = scenario(
    "entry/entry.feature",
    "Entry is displayed",
)

test_no_form_for_visitors = scenario(
    "entry/entry.feature",
    "No form for visitors",
)

test_create_entry = scenario(
    "entry/entry.feature",
    "Create an entry",
)


@then("I should see my entry")
def should_see_entry(browser, title):
    assert browser.is_text_present(title)


@then("I shouldn't see an entry form")
def shoudnt_see_entry_form(browser):
    assert not browser.find_by_css(".add-entry")


@when("I enter entry title")
def enter_entry_title(browser, title):
    browser.fill('title', title)


@when("I enter entry text")
def enter_entry_text(browser, text):
    browser.fill('text', text)


@when("I click the Share button")
def click_share_button(browser):
    button = browser.find_by_css("input[type=submit]").first
    button.click()


@then("I should see the entry title")
def should_see_entry_title(browser, title):
    assert browser.is_text_present(title)


@then("I should see the entry text")
def should_see_entry_text(browser, text):
    assert browser.is_text_present(text)
