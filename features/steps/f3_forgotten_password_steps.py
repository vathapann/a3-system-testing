# Step definitions for F3 User Forgotten Password.
# Shared steps ("I open the ... page", "I should see ...") live in common_steps.py.
# "Given an account already exists with a new email" is reused from f1_register_steps.py.
from behave import when
from helper.helper_base import unique_email

# Element IDs found with Chrome DevTools (Inspect) on the forgotten password page
FIELD_IDS = {
    "email": "input-email",
}


def _resolve_value(context, value):
    # Replace placeholders in the feature file with real test data
    if value == "NEW_EMAIL":
        # an email that has never been registered
        return unique_email("f3")
    if value == "REGISTERED_EMAIL":
        # the email created in "Given an account already exists..."
        return context.registered_email
    return value


@when('I click the "{link_text}" link')
def click_link(context, link_text):
    # e.g. the "Forgotten Password" link under the login form
    context.helperfunc.find_by_xpath(f"//div[@id='content']//a[normalize-space()='{link_text}']").click()


@when("I fill in the forgotten password form with:")
def fill_forgotten_password_form(context):
    # context.table holds the | field | value | rows from the feature file
    for row in context.table:
        box = context.helperfunc.find_by_id(FIELD_IDS[row["field"]])
        box.clear()
        box.send_keys(_resolve_value(context, row["value"]))


@when("I submit the forgotten password form")
def submit_forgotten_password_form(context):
    # "Continue" button under the E-Mail Address field
    context.helperfunc.click_by_css("input.btn-primary[value='Continue']")
