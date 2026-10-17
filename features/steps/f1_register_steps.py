# Step definitions for F1 User Registration.
# Shared steps ("I open the ... page", "I should see ...") live in common_steps.py.
from behave import given, when
from helper.helper_base import unique_email

# Element IDs found with Chrome DevTools (Inspect) on the register page
FIELD_IDS = {
    "first_name": "input-firstname",
    "last_name": "input-lastname",
    "email": "input-email",
    "telephone": "input-telephone",
    "password": "input-password",
    "confirm": "input-confirm",
}


def _resolve_value(context, value):
    # Replace placeholders in the feature file with real test data
    if value == "NEW_EMAIL":
        # a fresh email for every run, because the demo site is shared by many users
        return unique_email("f1")
    if value == "REGISTERED_EMAIL":
        # the email created in "Given an account already exists..."
        return context.registered_email
    return value


def _fill_form(context, rows):
    # rows: list of (field, value) pairs
    for field, value in rows:
        box = context.helperfunc.find_by_id(FIELD_IDS[field])
        box.clear()
        box.send_keys(_resolve_value(context, value))


def _tick_privacy_policy(context):
    # The checkbox is styled by the theme, so clicking its <label> is more
    # reliable than clicking the hidden <input> itself
    context.helperfunc.click_by_css("label[for='input-agree']")


def _submit(context):
    # "Continue" button at the bottom of the form
    context.helperfunc.click_by_css("input.btn-primary[value='Continue']")


@when("I fill in the registration form with:")
def fill_registration_form(context):
    # context.table holds the | field | value | rows from the feature file
    _fill_form(context, [(row["field"], row["value"]) for row in context.table])


@when("I agree to the Privacy Policy")
def agree_privacy_policy(context):
    _tick_privacy_policy(context)


@when("I do not agree to the Privacy Policy")
def do_not_agree_privacy_policy(context):
    # leave the checkbox unticked on purpose (negative test)
    pass


@when("I submit the registration form")
def submit_registration_form(context):
    _submit(context)


@given("an account already exists with a new email")
def create_existing_account(context):
    # Precondition for the duplicate-email scenario:
    # register a brand-new account, remember its email, then log out
    context.registered_email = unique_email("f1dup")
    context.helperfunc.open_route("account/register")
    _fill_form(context, [
        ("first_name", "Existing"),
        ("last_name", "User"),
        ("email", context.registered_email),
        ("telephone", "0412345678"),
        ("password", "Valid123!"),
        ("confirm", "Valid123!"),
    ])
    _tick_privacy_policy(context)
    _submit(context)
    context.helperfunc.wait_for_text("Your Account Has Been Created!")
    # clearing cookies logs the new user out before the real test starts
    context.helperfunc.delete_cookies()
