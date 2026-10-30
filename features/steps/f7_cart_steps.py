
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://opencart.abstracta.us/"
CART_URL = BASE_URL + "index.php?route=checkout/cart"

TIMEOUT = 15


# =====================================
# Helper Functions
# =====================================

def get_driver(context):
    return context.helperfunc._driver


def wait_visible(context, by, value):
    driver = get_driver(context)

    return WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (by, value)
        )
    )


def wait_clickable(context, by, value):
    driver = get_driver(context)

    return WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(
            (by, value)
        )
    )


# =====================================
# F7 - Open Product Page
# =====================================

@given("I am on the F7 product page")
def open_product_page(context):
    driver = get_driver(context)

    driver.get(BASE_URL)

    product_link = wait_clickable(
        context,
        By.LINK_TEXT,
        "MacBook"
    )

    product_link.click()

    wait_visible(
        context,
        By.ID,
        "button-cart"
    )

    print("PASS: MacBook product page opened")


# =====================================
# F7 - Add Product to Cart
# =====================================

@when("I add the F7 product to the cart")
def add_product(context):
    driver = get_driver(context)

    add_button = wait_clickable(
        context,
        By.ID,
        "button-cart"
    )

    add_button.click()

    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")
        )
    )

    print("PASS: Product added to cart")


# =====================================
# F7 - Open Shopping Cart
# =====================================

@when("I open the F7 shopping cart")
def open_cart(context):
    driver = get_driver(context)

    driver.get(CART_URL)

    wait_visible(
        context,
        By.ID,
        "content"
    )

    print("PASS: Shopping cart page opened")


# =====================================
# F7 Scenario 1 - Add Product
# =====================================

@then('the F7 cart should contain "{product}"')
def verify_product(context, product):
    driver = get_driver(context)

    WebDriverWait(driver, TIMEOUT).until(
        lambda d: product in
        d.find_element(By.ID, "content").text
    )

    cart_text = driver.find_element(
        By.ID,
        "content"
    ).text

    assert product in cart_text, (
        f"Expected product '{product}' "
        "was not found in shopping cart"
    )

    print(f"PASS: {product} found in shopping cart")


# =====================================
# F7 Scenario 2 - Update Quantity
# =====================================

@when('I update the F7 quantity to "{quantity}"')
def update_quantity(context, quantity):
    driver = get_driver(context)

    quantity_input = wait_visible(
        context,
        By.CSS_SELECTOR,
        "input[name^='quantity']"
    )

    quantity_input.clear()
    quantity_input.send_keys(quantity)

    # Blue Update button beside quantity input.
    update_button = quantity_input.find_element(
        By.XPATH,
        "./ancestor::div[contains(@class,'input-group')][1]"
        "//button[contains(@class,'btn-primary')]"
    )

    update_button.click()

    # Wait for the cart to refresh.
    WebDriverWait(driver, TIMEOUT).until(
        lambda d: any(
            element.get_attribute("value") == quantity
            for element in d.find_elements(
                By.CSS_SELECTOR,
                "input[name^='quantity']"
            )
        )
    )

    print(f"PASS: Quantity updated to {quantity}")


@then('the F7 product quantity should be "{quantity}"')
def verify_quantity(context, quantity):
    quantity_input = wait_visible(
        context,
        By.CSS_SELECTOR,
        "input[name^='quantity']"
    )

    actual_quantity = quantity_input.get_attribute(
        "value"
    )

    assert actual_quantity == quantity, (
        f"Expected quantity {quantity}, "
        f"but found {actual_quantity}"
    )

    print(f"PASS: Verified quantity {quantity}")


# =====================================
# F7 Scenario 3 - Remove Product
# =====================================

@when("I remove the F7 product")
def remove_product(context):
    driver = get_driver(context)

    # Find the shopping cart quantity field.
    quantity_input = wait_visible(
        context,
        By.CSS_SELECTOR,
        "input[name^='quantity']"
    )

    # Find the red Remove button next to quantity.
    remove_button = quantity_input.find_element(
        By.XPATH,
        "./ancestor::div[contains(@class,'input-group')][1]"
        "//button[contains(@class,'btn-danger')]"
    )

    # Click Remove.
    remove_button.click()

    # Wait until the shopping cart becomes empty.
    WebDriverWait(driver, TIMEOUT).until(
        lambda d: (
            "Your shopping cart is empty!"
            in d.find_element(By.ID, "content").text
        )
    )

    print("PASS: Product removed from shopping cart")


@then("the F7 shopping cart should be empty")
def verify_empty_cart(context):
    driver = get_driver(context)

    cart_content = wait_visible(
        context,
        By.ID,
        "content"
    ).text

    expected_message = "Your shopping cart is empty!"

    assert expected_message in cart_content, (
        "FAIL: Shopping cart is not empty"
    )

    print("PASS: Shopping cart is empty")
