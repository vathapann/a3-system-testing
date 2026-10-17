# Shared steps used by more than one member.
# Add a step here ONLY if two or more feature files need the same wording,
# otherwise Behave raises an AmbiguousStep error when two files define it.
from behave import given, then


@given('I open the "{route}" page')
def open_page(context, route):
    # e.g. Given I open the "account/login" page
    context.helperfunc.open_route(route)


@then('I should see "{text}"')
def see_text(context, text):
    # passes if the text becomes visible on the page within 10 seconds
    context.helperfunc.wait_for_text(text)
