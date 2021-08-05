# Created by nataliacupo at 2/16/21
Feature: Code for how to loop
  # In this scenario we are learning how to loop

  Scenario: Jeans colors are available
    Given Open Amazon page
    When Enter Jeans into search field
    And Click on search button
    And Select product
    Then Verify sizes are available