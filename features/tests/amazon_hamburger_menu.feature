# Created by nataliacupo at 3/28/21
Feature: Hamburger menu
  # Enter feature description here

  Scenario: Menu
    Given Open Amazon page
    When Select hamburger menu
    When Select Amazon music menu item
    Then 8 menu items are present