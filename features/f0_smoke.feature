# Smoke test to check everyone's environment works. Delete once real tests exist.
Feature: F0 Environment check

  Scenario: Home page loads
    Given I open the "common/home" page
    Then I should see "This is a dummy website for Web Automation Testing"
