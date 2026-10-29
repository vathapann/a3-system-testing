# Tiwat Thiplakha
# Step definitions for F4 Product Search.

from behave import given, when, then


@given("I am on the home page for F4 search")
def open_f4_home(context):
    context.helperfunc.open_route("common/home")


@when('I search for "{keyword}" using the header search')
def search_for_keyword(context, keyword):
    search_box = context.helperfunc.find_by_name("search")
    search_box.clear()
    search_box.send_keys(keyword)

    context.helperfunc.click_by_css(
        "#search .input-group-btn button"
    )
    context.helperfunc.wait_for_text(f"Search - {keyword}")


@when("I submit an empty header search for F4")
def submit_empty_search(context):
    search_box = context.helperfunc.find_by_name("search")
    search_box.clear()

    context.helperfunc.click_by_css(
        "#search .input-group-btn button"
    )
    context.helperfunc.wait_for_text("Search")


@then("matching products should be shown for F4")
def check_matching_products(context):
    page = context.helperfunc.page_source
    assert "product-thumb" in page, (
        "Expected product cards, but none were found."
    )


@then("no product cards should be shown for F4")
def check_no_product_cards(context):
    page = context.helperfunc.page_source
    assert "product-thumb" not in page, (
        "Unexpected product cards appeared for a nonexistent search."
    )


@then("the F4 search page should open without product cards")
def check_empty_search(context):
    page = context.helperfunc.page_source
    assert "product-thumb" not in page, (
        "Unexpected product cards appeared for an empty search."
    )