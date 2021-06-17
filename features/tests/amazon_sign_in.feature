# Created by nataliacupo at 3/28/21
Feature: Logged out user selects Orders and Sign In page opens
  Description: Logged out user is not able to order anything unless he logs himself in

  Scenario: User selects Orders and Sign in page opens
    Given Open Amazon page
    When Select Orders link
    Then Verify Sign-In is opened
