# Tiwat Thiplakha
Feature: F4 Product Search

  Scenario: Search for an existing product
    Given I am on the home page for F4 search
    When I search for "MacBook" using the header search
    Then matching products should be shown for F4

  Scenario: Search for a product that does not exist
    Given I am on the home page for F4 search
    When I search for "xyznonexistent123" using the header search
    Then no product cards should be shown for F4

  Scenario: Submit an empty search
    Given I am on the home page for F4 search
    When I submit an empty header search for F4
    Then the F4 search page should open without product cards