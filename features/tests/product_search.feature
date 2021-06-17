# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario Outline: User can search for a product
    Examples:
    |keyword |expected_result   |
    |shoes   |shoes             |
    |dress   |dress             |
    |printer |printer           |

    Given Open Google page
    When Input <keyword> into search field
    And Product results for <expected_result> are shown
    Then First result contains <expected_result>