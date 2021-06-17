# Created by nataliacupo at 2/20/21
Feature: User verifies that certain amount of items were added to Cart
  # n/a

  Scenario: One item is added to Cart
    Given Open Amazon page
    When Put printer into search field
    And Select search button
    And Verify printer is available
    And Select a product
    And Select Add to Cart
    And Select Cart Icon
    Then Verify amount of items is one