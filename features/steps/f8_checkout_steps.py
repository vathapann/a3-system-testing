
import os

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://opencart.abstracta.us/"
CART_URL = BASE_URL + "index.php?route=checkout/cart"
CHECKOUT_URL = BASE_URL + "index.php?route=checkout/checkout"

TIMEOUT = 20


# =====================================
# Helper Functions
# =====================================

def get_driver(context):
    return context.helperfunc._driver


def wait_visible(context, by, value):
    return WebDriverWait(
        get_driver(context), TIMEOUT
    ).until(
        EC.visibility_of_element_located((by, value))
    )


def click_id(context, element_id):
    driver = get_driver(context)

    button = WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.ID, element_id)
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        button
    )
    button.click()


def fill_field(context, element_id, value):
    element = wait_visible(
        context, By.ID, element_id
    )
    element.clear()
    element.send_keys(value)


def test_email():
    email = os.environ.get("OPENCART_EMAIL")
    if not email:
        raise AssertionError(
            "Set OPENCART_EMAIL before running F8 tests"
        )
    return email


def test_password():
    password = os.environ.get("OPENCART_PASSWORD")
    if not password:
        raise AssertionError(
            "Set OPENCART_PASSWORD before running F8 tests"
        )
    return password


def add_iphone(context):
    driver = get_driver(context)

    driver.get(BASE_URL)

    product = WebDriverWait(
        driver, TIMEOUT
    ).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "iPhone")
        )
    )
    product.click()

    click_id(context, "button-cart")

    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")
        )
    )

    driver.get(CART_URL)

    WebDriverWait(driver, TIMEOUT).until(
        lambda d: "iPhone" in
        d.find_element(By.ID, "content").text
    )


# =====================================
# F8 Scenario 1 - Empty Cart
# =====================================

@given("my F8 shopping cart is empty")
def empty_cart(context):
    driver = get_driver(context)

    # The shared before_scenario hook deletes cookies.
    # Open the cart and verify it is empty.
    driver.get(CART_URL)

    WebDriverWait(driver, TIMEOUT).until(
        lambda d: (
            "Your shopping cart is empty!"
            in d.find_element(By.ID, "content").text
        )
    )

    print("PASS: Cart is empty")


@when("I open the F8 checkout page")
def open_checkout(context):
    driver = get_driver(context)
    driver.get(CHECKOUT_URL)


@then("I should see the F8 empty cart message")
def verify_empty_cart(context):
    driver = get_driver(context)

    WebDriverWait(driver, TIMEOUT).until(
        lambda d: (
            "Your shopping cart is empty!"
            in d.find_element(By.ID, "content").text
        )
    )

    assert "Your shopping cart is empty!" in (
        driver.find_element(By.ID, "content").text
    )

    print("PASS: Empty cart checkout prevented")


# =====================================
# F8 - Add iPhone to Cart
# =====================================

@given("I have an iPhone in my F8 shopping cart")
def iphone_in_cart(context):
    add_iphone(context)
    print("PASS: iPhone added to cart")


# =====================================
# F8 Scenario 2 - Invalid Login
# =====================================

@when("I enter invalid F8 login credentials")
def invalid_login(context):
    wait_visible(context, By.ID, "input-email")

    fill_field(
        context,
        "input-email",
        test_email()
    )

    fill_field(
        context,
        "input-password",
        "WrongPassword_For_Assignment3"
    )

    click_id(context, "button-login")


@then("I should see an F8 login error")
def verify_invalid_login(context):
    driver = get_driver(context)

    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".alert-danger")
        )
    )

    error_text = driver.find_element(
        By.CSS_SELECTOR,
        ".alert-danger"
    ).text

    assert error_text.strip(), (
        "Expected a login error message"
    )

    assert "checkout/success" not in driver.current_url

    print("PASS: Invalid login was rejected")
    print("Error message:", error_text)


# =====================================
# F8 Scenario 3 - Valid Login
# =====================================

@when("I log in with my valid F8 account")
def valid_login(context):
    driver = get_driver(context)

    wait_visible(context, By.ID, "input-email")

    fill_field(
        context,
        "input-email",
        test_email()
    )

    fill_field(
        context,
        "input-password",
        test_password()
    )

    click_id(context, "button-login")

    # Existing customers should reach address selection.
    WebDriverWait(driver, TIMEOUT).until(
        lambda d: (
            len(d.find_elements(
                By.ID, "button-payment-address"
            )) > 0
            or len(d.find_elements(
                By.ID, "button-shipping-address"
            )) > 0
        )
    )

    print("PASS: Returning customer logged in")


# =====================================
# F8 - Checkout Details
# =====================================

@when("I complete the F8 checkout details")
def complete_checkout_details(context):
    driver = get_driver(context)

    # Step 2: Existing billing address.
    click_id(context, "button-payment-address")

    # Step 3: Existing delivery address.
    click_id(context, "button-shipping-address")

    # Step 4: Delivery method.
    click_id(context, "button-shipping-method")

    # Step 5: Payment method.
    wait_visible(
        context,
        By.ID,
        "collapse-payment-method"
    )

    # Accept the store terms if the checkbox is present.
    agree_boxes = driver.find_elements(
        By.CSS_SELECTOR,
        "input[name='agree']"
    )

    if agree_boxes:
        checkbox = agree_boxes[0]

        if not checkbox.is_selected():
            driver.execute_script(
                "arguments[0].click();",
                checkbox
            )

    click_id(context, "button-payment-method")

    # Step 6: Confirm Order.
    wait_visible(
        context,
        By.ID,
        "button-confirm"
    )

    print("PASS: Checkout details completed")


# =====================================
# F8 - Confirm Order
# =====================================

@when("I confirm the F8 order")
def confirm_order(context):
    click_id(context, "button-confirm")

    print("Order confirmation button clicked")


@then("the F8 order should be successful")
def verify_order_success(context):
    driver = get_driver(context)

    WebDriverWait(driver, TIMEOUT).until(
        lambda d: (
            "checkout/success" in d.current_url
            and "Your order has been placed!"
            in d.page_source
        )
    )

    assert "checkout/success" in driver.current_url
    assert "Your order has been placed!" in (
        driver.page_source
    )

    print("PASS: Order successfully placed")
