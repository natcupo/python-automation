# Created by nataliacupo at 2/20/21
Feature: Scenario for cancelling order
  # See above

  Scenario: Cancel order
    Given Open Amazon page
    When Input Cancel order into text field
    And Select search button
    Then Word Cancel order is available
