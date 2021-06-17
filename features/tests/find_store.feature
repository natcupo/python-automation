# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open web page
    When Select Find Store
    When Verify Find a Store is available
    And Enter 13031 into zip code field
    And Store is available
    And Select Store
    Then My Store is available

