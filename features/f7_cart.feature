
Feature: F7 Shopping Cart
  As a customer
  I want to manage products in my shopping cart
  So that I can purchase the correct items and quantities

  Scenario: F7_S1 Add a product to the shopping cart
    Given I am on the F7 product page
    When I add the F7 product to the cart
    And I open the F7 shopping cart
    Then the F7 cart should contain "MacBook"

  Scenario: F7_S2 Update product quantity
    Given I am on the F7 product page
    When I add the F7 product to the cart
    And I open the F7 shopping cart
    And I update the F7 quantity to "2"
    Then the F7 product quantity should be "2"

  Scenario: F7_S3 Remove a product from the shopping cart
    Given I am on the F7 product page
    When I add the F7 product to the cart
    And I open the F7 shopping cart
    And I remove the F7 product
    Then the F7 shopping cart should be empty
