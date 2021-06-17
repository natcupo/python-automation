# Created by nataliacupo at 4/7/21
Feature: Error verification feature

  Scenario Outline: User gets verification errors without co-applicant
    Examples:
    |keyword |                                                     
    |Please enter name without numbers or special characters    |


    Given Open web page
    When User selects Financing
    When User selects Apply
    When User submits application
    Then User verifies <keyword>
    # When User selects co-applicant
    # Then User verifies co-application <F>, <L>,
