@comprehensive_test
Feature: Comprehensive Toll Calculator Test
  Scenario: Non-member basic calculation
    Given the user is a non-member
    When the user calculates toll for 10 miles during normal times
    Then the total charge should be $20.00

  Scenario: Silver member calculation
    Given the user is a "Silver" member
    When the user calculates toll for 15 miles during normal times
    Then the total charge should be $15.00

  Scenario: Gold member during normal times
    Given the user is a "Gold" member
    When the user calculates toll for 25 miles during normal times
    Then the total charge should be $0.00

  Scenario: Non-member during peak times
    Given the user is a non-member
    When the user calculates toll for 10 miles during peak times
    Then the total charge should be $60.00

  Scenario: Gold member during busy times (special case)
    Given the user is a "Gold" member
    When the user calculates toll for 25 miles during busy times
    Then the total charge should be $2.50

  Scenario: Invalid distance handling
    Given the user is a non-member
    When the user attempts to calculate toll for 0 miles
    Then report the "Distance must be greater than 0"
    And no charge should be calculated