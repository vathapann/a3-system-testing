
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CONTACT_URL = (
    "https://opencart.abstracta.us/"
    "index.php?route=information/contact"
)


def field(context, selector):
    return WebDriverWait(
        context.helperfunc._driver, 10
    ).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, selector)
        )
    )


@given("I am on the F9 contact page")
def open_contact_page(context):
    context.helperfunc.open(CONTACT_URL)
    field(context, "input[name='name']")


@when('I enter F9 name "{name}"')
def enter_name(context, name):
    element = field(context, "input[name='name']")
    element.clear()
    element.send_keys(name)


@when('I enter F9 email "{email}"')
def enter_email(context, email):
    element = field(context, "input[name='email']")
    element.clear()
    element.send_keys(email)


@when('I enter F9 enquiry "{message}"')
def enter_enquiry(context, message):
    element = field(
        context, "textarea[name='enquiry']"
    )
    element.clear()
    element.send_keys(message)


@when("I submit the F9 contact form")
def submit_contact(context):
    driver = context.helperfunc._driver

    submit_button = WebDriverWait(
        driver, 10
    ).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "input[type='submit'], button[type='submit']"
        ))
    )

    submit_button.click()


@then("the F9 enquiry should be successful")
def verify_success(context):
    driver = context.helperfunc._driver

    WebDriverWait(driver, 10).until(
        lambda d: (
            "contact/success" in d.current_url
            or "successfully sent" in
            d.page_source.lower()
        )
    )

    assert (
        "contact/success" in driver.current_url
        or "successfully sent" in
        driver.page_source.lower()
    ), "Expected contact success confirmation"


@then("the F9 contact form should reject the submission")
def verify_rejected(context):
    driver = context.helperfunc._driver

    # Allow time for a server-side validation response.
    try:
        WebDriverWait(driver, 3).until(
            lambda d: (
                "error" in d.page_source.lower()
                or "contact/success" in d.current_url
            )
        )
    except Exception:
        pass

    # Check whether HTML5 form validation rejects inputs.
    invalid_fields = driver.find_elements(
        By.CSS_SELECTOR, "input:invalid, textarea:invalid"
    )

    error_messages = driver.find_elements(
        By.CSS_SELECTOR,
        ".text-danger, .invalid-feedback, .alert-danger"
    )

    visible_errors = [
        element for element in error_messages
        if element.is_displayed()
    ]

    assert (
        "contact/success" not in driver.current_url
        and (
            len(invalid_fields) > 0
            or len(visible_errors) > 0
        )
    ), "Expected validation errors, but none were found"
