# Tester: Tiwat Thiplakha
# Step definitions for F6 Product Compare.
# These steps use the existing HelperFunc methods and do not edit shared files.

from behave import given, when, then


def _add_product_to_compare(context, product_name):
    context.helperfunc.open_route(
        f"product/search&search={product_name}"
    )
    context.helperfunc.wait_for_text(f"Search - {product_name}")

    # OpenCart product cards use the compare.add() action.
    context.helperfunc.click_by_css('button[onclick*="compare.add"]')
    context.helperfunc.wait_for_text("Success: You have added")


def _open_compare_page(context):
    context.helperfunc.open_route("product/compare")


@given("I am on the home page for F6 comparison")
def f6_open_home(context):
    context.helperfunc.open_route("common/home")


@when('I add "{product_name}" to product comparison')
def f6_add_product(context, product_name):
    _add_product_to_compare(context, product_name)


@then('"{product_name}" should appear on the comparison page')
def f6_one_product_on_compare_page(context, product_name):
    _open_compare_page(context)
    context.helperfunc.wait_for_text(product_name)


@then("both products should appear on the comparison page")
def f6_both_products_on_compare_page(context):
    _open_compare_page(context)
    page = context.helperfunc.page_source
    assert "MacBook" in page, "MacBook was not found on the comparison page."
    assert "iPhone" in page, "iPhone was not found on the comparison page."


@when("I open the product comparison page without selecting products")
def f6_open_empty_compare_page(context):
    _open_compare_page(context)


@then("the comparison page should say that no products were selected")
def f6_check_empty_compare_page(context):
    page = context.helperfunc.page_source.lower()
    expected_message = "you have not chosen any products to compare"
    assert expected_message in page, (
        "The expected empty-comparison message was not displayed."
    )
