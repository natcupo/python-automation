# Created by nataliacupo at 3/29/21
Feature: Price selection
  # Enter feature description here

  Scenario: User can select a price
    Given Open webpage
    When Select item
    And Select Price department
    Then BEST SELLING is selected
