@basic_test
Feature: Simple Test
  Scenario: Basic calculation
    Given the toll charge calculator is available
    Given the user is a non-member
    When the user calculates toll for 10 miles during normal times
    Then the total charge should be $20.00