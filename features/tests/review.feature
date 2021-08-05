# Created by nataliacupo at 8/4/21
Feature: Review Product
  # Enter feature description here

  Scenario: Test review product functionality
    Given Open Gettop page
    When Select MacBook Pro 13-inch
    And MacBook Pro 13-inch opens
    And Item has no reviews
    And Select Reviews link
    And Submit comment, name and email
    Then Review was submitted

