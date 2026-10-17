# Tester: Sovatha Pann
# Function: F1 User Registration
# URL: https://ecommerce-playground.lambdatest.io/index.php?route=account/register

Feature: F1 User Registration
  As a new visitor to the store
  I want to create an account with my personal details
  So that I can log in, save a wishlist and check out faster

  Background:
    Given I open the "account/register" page

  # Test Scenario 1: valid registration (expected: success)
  Scenario: Register with valid details and a new email
    When I fill in the registration form with:
      | field      | value        |
      | first_name | Sovatha      |
      | last_name  | Tester       |
      | email      | NEW_EMAIL    |
      | telephone  | 0412345678   |
      | password   | Valid123!    |
      | confirm    | Valid123!    |
    And I agree to the Privacy Policy
    And I submit the registration form
    Then I should see "Your Account Has Been Created!"

  # Test Scenario 2: duplicate email (expected: failure message)
  Scenario: Register with an email that is already registered
    Given an account already exists with a new email
    And I open the "account/register" page
    When I fill in the registration form with:
      | field      | value            |
      | first_name | Sovatha          |
      | last_name  | Duplicate        |
      | email      | REGISTERED_EMAIL |
      | telephone  | 0412345678       |
      | password   | Valid123!        |
      | confirm    | Valid123!        |
    And I agree to the Privacy Policy
    And I submit the registration form
    Then I should see "E-Mail Address is already registered!"

  # Test Scenario 3: invalid inputs (expected: validation message for each row)
  Scenario Outline: Register with invalid input - <case>
    When I fill in the registration form with:
      | field      | value        |
      | first_name | <first_name> |
      | last_name  | Tester       |
      | email      | NEW_EMAIL    |
      | telephone  | 0412345678   |
      | password   | <password>   |
      | confirm    | <confirm>    |
    And I <agree_action> the Privacy Policy
    And I submit the registration form
    Then I should see "<expected_message>"

    Examples:
      | case                    | first_name                        | password  | confirm   | agree_action    | expected_message                                |
      | password mismatch       | Sovatha                           | Valid123! | Other456! | agree to        | Password confirmation does not match password!  |
      | privacy policy unticked | Sovatha                           | Valid123! | Valid123! | do not agree to | You must agree to the Privacy Policy!           |
      | first name too long     | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA | Valid123! | Valid123! | agree to        | First Name must be between 1 and 32 characters! |
