# Tester: Tiwat Thiplakha
# Step definitions for F5 Wishlist.
# These steps use the existing HelperFunc methods and do not edit shared files.

from behave import given, when, then
from helper.helper_base import unique_email


def _search_product(context, product_name):
    context.helperfunc.open_route(
        f"product/search&search={product_name}"
    )
    context.helperfunc.wait_for_text(f"Search - {product_name}")


def _add_product_to_wishlist(context, product_name):
    _search_product(context, product_name)
    # OpenCart product cards use the wishlist.add() action.
    context.helperfunc.click_by_css('button[onclick*="wishlist.add"]')


@given("I am a guest visitor for F5")
def f5_guest_visitor(context):
    # environment.py clears cookies before each scenario.
    context.helperfunc.open_route("common/home")


@when('I add "{product_name}" to the wishlist as a guest')
def f5_guest_add_wishlist(context, product_name):
    _add_product_to_wishlist(context, product_name)


@then("I should be asked to log in to save the wishlist item")
def f5_guest_wishlist_login_message(context):
    context.helperfunc.wait_for_text(
        "You must login or create an account to save"
    )


@when("I open the wishlist as a guest")
def f5_open_wishlist_guest(context):
    context.helperfunc.open_route("account/wishlist")


@then("I should be taken to the account login page")
def f5_guest_redirected_to_login(context):
    # The guest should be sent to the login form before viewing a saved list.
    context.helperfunc.find_by_id("input-email")
    context.helperfunc.find_by_id("input-password")


@given("I have a new customer account for F5")
def f5_create_customer_account(context):
    # Create a unique account so the public demo site is not affected by
    # accounts created by other students.
    context.f5_email = unique_email("f5")
    password = "Valid123!"
    context.f5_password = password

    context.helperfunc.open_route("account/register")

    fields = {
        "input-firstname": "Tiwat",
        "input-lastname": "WishlistTester",
        "input-email": context.f5_email,
        "input-telephone": "0412345678",
        "input-password": password,
        "input-confirm": password,
    }
    for field_id, value in fields.items():
        field = context.helperfunc.find_by_id(field_id)
        field.clear()
        field.send_keys(value)

    context.helperfunc.find_by_name("agree").click()
    context.helperfunc.click_by_css("input.btn-primary[value='Continue']")
    context.helperfunc.wait_for_text("Your Account Has Been Created!")


@when('I add "{product_name}" to the wishlist as a logged-in customer')
def f5_logged_in_add_wishlist(context, product_name):
    _add_product_to_wishlist(context, product_name)


@then("the product should be added to my wishlist")
def f5_check_wishlist_added(context):
    context.helperfunc.wait_for_text("Success: You have added")
    context.helperfunc.open_route("account/wishlist")
    context.helperfunc.wait_for_text("MacBook")
