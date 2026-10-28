
Feature: F9 Contact Us
  As a customer
  I want to contact the store owner
  So that I can send enquiries through the website

  Scenario: F9_S1 Submit a valid enquiry
    Given I am on the F9 contact page
    When I enter F9 name "Yiyang Chen"
    And I enter F9 email "yiyang.test@example.com"
    And I enter F9 enquiry "This is an automated system testing enquiry for Assignment 3."
    And I submit the F9 contact form
    Then the F9 enquiry should be successful

  Scenario: F9_S2 Submit an invalid email
    Given I am on the F9 contact page
    When I enter F9 name "Yiyang Chen"
    And I enter F9 email "invalid-email"
    And I enter F9 enquiry "This enquiry is testing invalid email validation."
    And I submit the F9 contact form
    Then the F9 contact form should reject the submission

  Scenario: F9_S3 Submit an empty contact form
    Given I am on the F9 contact page
    When I submit the F9 contact form
    Then the F9 contact form should reject the submission
