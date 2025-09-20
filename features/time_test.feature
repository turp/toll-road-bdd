@time_test
Feature: Time-Based Test
  Scenario: Non-member busy time
    Given the toll charge calculator is available
    Given the user is a non-member
    When the user calculates toll for 10 miles during busy times
    Then the total charge should be $40.00