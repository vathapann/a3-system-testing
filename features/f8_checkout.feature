
Feature: F8 Checkout
  As a returning customer
  I want to complete the checkout process
  So that I can purchase products online

  Scenario: F8_S1 Attempt checkout with an empty cart
    Given my F8 shopping cart is empty
    When I open the F8 checkout page
    Then I should see the F8 empty cart message

  Scenario: F8_S2 Checkout login with an invalid password
    Given I have an iPhone in my F8 shopping cart
    When I open the F8 checkout page
    And I enter invalid F8 login credentials
    Then I should see an F8 login error

  Scenario: F8_S3 Complete checkout as a returning customer
    Given I have an iPhone in my F8 shopping cart
    When I open the F8 checkout page
    And I log in with my valid F8 account
    And I complete the F8 checkout details
    And I confirm the F8 order
    Then the F8 order should be successful
