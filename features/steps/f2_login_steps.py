# Step definitions for F2 User Login.
# Shared steps ("I open the ... page", "I should see ...") live in common_steps.py.
# "Given an account already exists with a new email" is reused from f1_register_steps.py.
from behave import when
from helper.helper_base import unique_email

# Element IDs found with Chrome DevTools (Inspect) on the login page
FIELD_IDS = {
    "email": "input-email",
    "password": "input-password",
}


def _resolve_value(context, value):
    # Replace placeholders in the feature file with real test data
    if value == "NEW_EMAIL":
        # an email that has never been registered
        return unique_email("f2")
    if value == "REGISTERED_EMAIL":
        # the email created in "Given an account already exists..."
        return context.registered_email
    return value


@when("I fill in the login form with:")
def fill_login_form(context):
    # context.table holds the | field | value | rows from the feature file
    for row in context.table:
        box = context.helperfunc.find_by_id(FIELD_IDS[row["field"]])
        box.clear()
        box.send_keys(_resolve_value(context, row["value"]))


@when("I submit the login form")
def submit_login_form(context):
    # "Login" button under the Returning Customer form
    context.helperfunc.click_by_css("input.btn-primary[value='Login']")
