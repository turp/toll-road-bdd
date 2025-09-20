@edge_cases @comprehensive
Feature: Toll Calculation Edge Cases and Validation
  As a toll road system administrator
  I want to ensure the calculator handles edge cases correctly
  So that the system is robust and reliable

  Background:
    Given the toll charge calculator is available

  @validation @negative_testing
  Scenario: Invalid distance input
    Given the user is a non-member
    When the user attempts to calculate toll for 0 miles
    Then an error message should be displayed saying "Distance must be greater than 0"
    And no charge should be calculated

  @validation @negative_testing
  Scenario: Negative distance input
    Given the user is a non-member
    When the user attempts to calculate toll for -5 miles
    Then an error message should be displayed saying "Distance must be greater than 0"
    And no charge should be calculated

  @validation @membership_validation
  Scenario: Invalid membership type
    Given the user has an invalid membership type "Platinum"
    When the user attempts to calculate toll for 10 miles during normal times
    Then an error message should be displayed saying "Invalid membership type"
    And no charge should be calculated

  @edge_cases @large_numbers
  Scenario: Very large distance calculation
    Given the user is a non-member
    When the user calculates toll for 1000 miles during normal times
    Then the total charge should be $1020.00
    And the charge breakdown should show:
      | Description         | Calculation        | Amount   |
      | First 20 miles (base) | 20 miles × $2.00   | $40.00   |
      | Next 980 miles (base) | 980 miles × $1.00  | $980.00  |

  @edge_cases @precision
  Scenario: Fractional distance calculation
    Given the user is a Silver member
    When the user calculates toll for 10.5 miles during normal times
    Then the total charge should be $10.50
    And the charge breakdown should show:
      | Description | Calculation       | Amount |
      | Base charge | 10.5 miles × $1.00 | $10.50 |

  @edge_cases @boundary_testing
  Scenario Outline: Boundary testing for 20-mile threshold
    Given the user is a "<membership_level>" member
    When the user calculates toll for <distance> miles during normal times
    Then the total charge should be $<expected_total>

    Examples:
      | membership_level | distance | expected_total |
      | non             | 19.99    | 39.98          |
      | non             | 20.00    | 40.00          |
      | non             | 20.01    | 40.01          |
      | Silver          | 19.99    | 19.99          |
      | Silver          | 20.00    | 20.00          |
      | Silver          | 20.01    | 20.01          |

  @comprehensive @all_combinations
  Scenario Outline: Comprehensive toll calculation matrix
    Given the user is a "<membership>" member
    When the user calculates toll for <distance> miles during <time_period> times
    Then the total charge should be $<expected_charge>

    Examples:
      | membership | distance | time_period | expected_charge |
      | non        | 5        | normal      | 10.00           |
      | non        | 5        | busy        | 20.00           |
      | non        | 5        | peak        | 30.00           |
      | non        | 20       | normal      | 40.00           |
      | non        | 20       | busy        | 80.00           |
      | non        | 20       | peak        | 120.00          |
      | non        | 25       | normal      | 45.00           |
      | non        | 25       | busy        | 90.00           |
      | non        | 25       | peak        | 135.00          |
      | Silver     | 5        | normal      | 5.00            |
      | Silver     | 5        | busy        | 10.00           |
      | Silver     | 5        | peak        | 15.00           |
      | Silver     | 20       | normal      | 20.00           |
      | Silver     | 20       | busy        | 40.00           |
      | Silver     | 20       | peak        | 60.00           |
      | Silver     | 25       | normal      | 22.50           |
      | Silver     | 25       | busy        | 45.00           |
      | Silver     | 25       | peak        | 67.50           |
      | Gold       | 5        | normal      | 0.00            |
      | Gold       | 5        | busy        | 0.00            |
      | Gold       | 5        | peak        | 0.00            |
      | Gold       | 20       | normal      | 0.00            |
      | Gold       | 20       | busy        | 0.00            |
      | Gold       | 20       | peak        | 0.00            |
      | Gold       | 25       | normal      | 0.00            |
      | Gold       | 25       | busy        | 2.50            |
      | Gold       | 25       | peak        | 3.75            |

  @performance @stress_testing
  Scenario: Multiple rapid calculations
    Given the user is a non-member
    When the user performs 100 toll calculations for 15 miles during normal times
    Then each calculation should return $30.00
    And all calculations should complete within 5 seconds

  @integration @system_limits
  Scenario: System handles maximum reasonable distance
    Given the user is a non-member
    When the user calculates toll for 9999 miles during peak times
    Then the system should handle the calculation successfully
    And the total charge should be $30057.00
    And the response time should be less than 2 seconds