@time_based_pricing @priority_high
Feature: Time-Based Toll Pricing
  As a toll road user
  I want toll charges to vary based on traffic time periods
  So that pricing reflects demand and encourages off-peak travel

  Background:
    Given the time-based multipliers are configured as follows:
      | Time Period | Multiplier |
      | Normal      | 1x         |
      | Busy        | 2x         |
      | Peak        | 3x         |

  @regression @data_driven
  Scenario Outline: Calculate toll for different time periods and membership levels
    Given the user is a "<membership_level>" member
    When the user calculates toll for <distance> miles during <time_period> times
    Then the total charge should be <expected_total>

    Examples:
      | membership_level | distance | time_period | expected_total |
      | non             | 10       | normal      | 20.00          |
      | non             | 10       | busy        | 40.00          |
      | non             | 10       | peak        | 60.00          |
      | Silver          | 10       | normal      | 10.00          |
      | Silver          | 10       | busy        | 20.00          |
      | Silver          | 10       | peak        | 30.00          |
      | Gold            | 10       | normal      | 0.00           |
      | Gold            | 10       | busy        | 0.00           |
      | Gold            | 10       | peak        | 0.00           |
      | Gold            | 25       | busy        | 2.50           |
      | Gold            | 25       | peak        | 3.75           |

  @smoke @time_multiplier
  Scenario: Non-member calculates toll during busy times
    Given the user is a non-member
    When the user calculates toll for 10 miles during busy times
    Then the total charge should be 40.00
    And the charge breakdown should show:
      | Description         | Calculation        | Amount |
      | Base charge         | 10 miles x $2.00   | $20.00 |
      | Busy time multiplier| $20.00 x 2         | $40.00 |

  @smoke @time_multiplier
  Scenario: Non-member calculates toll during peak times
    Given the user is a non-member
    When the user calculates toll for 10 miles during peak times
    Then the total charge should be 60.00
    And the charge breakdown should show:
      | Description         | Calculation        | Amount |
      | Base charge         | 10 miles x $2.00   | $20.00 |
      | Peak time multiplier| $20.00 x 3         | $60.00 |

  @smoke @membership_time
  Scenario: Silver member calculates toll during busy times
    Given the user is a "Silver" member
    When the user calculates toll for 10 miles during busy times
    Then the total charge should be 20.00
    And the charge breakdown should show:
      | Description         | Calculation        | Amount |
      | Base charge         | 10 miles x $1.00   | $10.00 |
      | Busy time multiplier| $10.00 x 2         | $20.00 |

  @priority_high @gold_membership
  Scenario: Gold member calculates toll during busy times
    Given the user is a "Gold" member
    When the user calculates toll for 10 miles during busy times
    Then the total charge should be 0.00
    And the charge breakdown should show:
      | Description         | Calculation        | Amount |
      | Base charge         | 10 miles x $0.00   | $0.00  |
      | Busy time multiplier| $0.00 x 2          | $0.00  |

  @critical @gold_membership
  Scenario: Gold member calculates toll during peak times with distance over 20 miles
    Given the user is a "Gold" member
    When the user calculates toll for 25 miles during peak times
    Then the total charge should be 3.75
    And the charge breakdown should show:
      | Description              | Calculation         | Amount |
      | First 20 miles (free)    | 20 miles x $0.00    | $0.00  |
      | Next 5 miles (base)      | 5 miles x $0.25     | $1.25  |
      | Peak time multiplier     | $1.25 x 3           | $3.75  |

  @regression @long_distance_time
  Scenario: Non-member calculates toll for long distance during peak times
    Given the user is a non-member
    When the user calculates toll for 25 miles during peak times
    Then the total charge should be 135.00
    And the charge breakdown should show:
      | Description              | Calculation         | Amount |
      | First 20 miles (base)    | 20 miles x $2.00    | $40.00 |
      | Next 5 miles (base)      | 5 miles x $1.00     | $5.00  |
      | Total base charge        | $40.00 + $5.00      | $45.00 |
      | Peak time multiplier     | $45.00 x 3          | $135.00|