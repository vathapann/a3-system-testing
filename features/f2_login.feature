# Tester: Sovatha Pann
# Function: F2 User Login
# URL: https://opencart.abstracta.us/index.php?route=account/login

Feature: F2 User Login
  As a registered customer
  I want to log in to the website with my email and password
  So that I can view my account and check out faster

  # Test Scenario 1: valid credentials (expected: success)
  Scenario: Login with valid credentials
    Given an account already exists with a new email
    And I open the "account/login" page
    When I fill in the login form with:
      | field    | value            |
      | email    | REGISTERED_EMAIL |
      | password | Valid123!        |
    And I submit the login form
    Then I should see "Logout"

  # Test Scenario 2: wrong password for a registered email (expected: warning message)
  Scenario: Login with a wrong password
    Given an account already exists with a new email
    And I open the "account/login" page
    When I fill in the login form with:
      | field    | value            |
      | email    | REGISTERED_EMAIL |
      | password | Wrong999!        |
    And I submit the login form
    Then I should see "Warning: No match for E-Mail Address and/or Password."

  # Test Scenario 3: invalid inputs (expected: warning message for each row)
  Scenario Outline: Login with invalid input - <case>
    Given I open the "account/login" page
    When I fill in the login form with:
      | field    | value      |
      | email    | <email>    |
      | password | <password> |
    And I submit the login form
    Then I should see "Warning: No match for E-Mail Address and/or Password."

    Examples:
      | case               | email     | password  |
      | unregistered email | NEW_EMAIL | Valid123! |
      | empty fields       |           |           |
