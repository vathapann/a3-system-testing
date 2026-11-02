# Tester: Tiwat Thiplakha
# Function: F6 Product Compare

Feature: F6 Product Compare
  As a store visitor
  I want to compare products
  So that I can review product details before choosing what to buy

  Scenario: Add one product to product comparison
    Given I am on the home page for F6 comparison
    When I add "MacBook" to product comparison
    Then "MacBook" should appear on the comparison page

  Scenario: Compare two different products
    Given I am on the home page for F6 comparison
    When I add "MacBook" to product comparison
    And I add "iPhone" to product comparison
    Then both products should appear on the comparison page

  Scenario: Open product comparison without selecting products
    Given I am on the home page for F6 comparison
    When I open the product comparison page without selecting products
    Then the comparison page should say that no products were selected
