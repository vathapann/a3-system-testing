# Tester: Sovatha Pann
# Function: F3 User Forgotten Password
# URL: https://opencart.abstracta.us/index.php?route=account/forgotten

Feature: F3 User Forgotten Password
  As a registered customer who has forgotten my password
  I want to request a password reset using my email address
  So that I can regain access to my account

  # Test Scenario 1: open the page from the login page (expected: forgotten password form shown)
  Scenario: Open Forgotten Password from the login page
    Given I open the "account/login" page
    When I click the "Forgotten Password" link
    Then I should see "Forgot Your Password?"

  # Test Scenario 2: registered email (expected: success message)
  Scenario: Request a password reset with a registered email
    Given an account already exists with a new email
    And I open the "account/forgotten" page
    When I fill in the forgotten password form with:
      | field | value            |
      | email | REGISTERED_EMAIL |
    And I submit the forgotten password form
    Then I should see "An email with a confirmation link has been sent your email address."

  # Test Scenario 3: invalid inputs (expected: warning message for each row)
  Scenario Outline: Request a password reset with invalid input - <case>
    Given I open the "account/forgotten" page
    When I fill in the forgotten password form with:
      | field | value   |
      | email | <email> |
    And I submit the forgotten password form
    Then I should see "Warning: The E-Mail Address was not found in our records, please try again!"

    Examples:
      | case               | email          |
      | unregistered email | NEW_EMAIL      |
      | empty email        |                |
      | invalid format     | not-an-email   |
