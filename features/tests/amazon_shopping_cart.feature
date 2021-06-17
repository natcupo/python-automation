# Created by nataliacupo at 3/28/21
Feature: Amazon cart is empty
  # Enter feature description here

  Scenario: Amazon cart is empty is no products are added
    Given Open Amazon page
    When Select Cart
    Then Verify Your Amazon Cart is empty text is present