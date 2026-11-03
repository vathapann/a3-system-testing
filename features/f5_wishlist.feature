# Tester: Tiwat Thiplakha
# Function: F5 Wishlist

Feature: F5 Wishlist
  As a store visitor
  I want to save products to a wishlist
  So that I can find products I may want to buy later

  Scenario: Guest tries to add a product to the wishlist
    Given I am a guest visitor for F5
    When I add "MacBook" to the wishlist as a guest
    Then I should be asked to log in to save the wishlist item

  Scenario: Guest opens the wishlist
    Given I am a guest visitor for F5
    When I open the wishlist as a guest
    Then I should be taken to the account login page

  Scenario: Logged-in customer adds a product to the wishlist
    Given I have a new customer account for F5
    When I add "MacBook" to the wishlist as a logged-in customer
    Then the product should be added to my wishlist
