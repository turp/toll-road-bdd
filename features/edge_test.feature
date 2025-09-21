@edge_test
Feature: Edge Case Test
  Scenario: Invalid distance
    Given the user is a non-member
    When the user attempts to calculate toll for 0 miles
    Then an error message should be displayed saying "Distance must be greater than 0"
    And no charge should be calculated