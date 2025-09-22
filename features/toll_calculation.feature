@toll_calculation @priority_high
Feature: Toll Charge Calculation
  As a toll road user
  I want to calculate toll charges based on distance and membership level
  So that I can understand the cost of my trip

  Background:
    Given the standard rates are configured as follows:
      | Rate Type  | First 20 Miles | Beyond 20 Miles |
      | Non-member | $2.00/mile     | $1.00/mile      |
      | Silver     | $1.00/mile     | $0.50/mile      |
      | Gold       | $0.00/mile     | $0.00/mile      |

  @regression @data_driven
  Scenario Outline: Calculate toll for different membership levels and distances
    Given the user is a "<membership>" member
    When the user calculates toll for <distance> miles during normal times
    Then the total charge should be $<total>

    Examples:
      | membership | distance | total |
      | non        | 5        | 10.00 |
      | non        | 15       | 30.00 |
      | non        | 30       | 50.00 |
      | Silver     | 5        | 5.00  |
      | Silver     | 15       | 15.00 |
      | Silver     | 30       | 25.00 |
      | Gold       | 5        | 0.00  |
      | Gold       | 15       | 0.00  |
      | Gold       | 30       | 0.00  |

  @smoke @basic_calculation
  Scenario: Non-member calculates toll for short distance
    Given the user is a non-member
    When the user calculates toll for 10 miles during normal times
    Then the total charge should be $20.00
    And the charge breakdown should show:
      | Description | Calculation      | Amount |
      | Base charge | 10 miles × $2.00 | $20.00 |

  @smoke @basic_calculation
  Scenario: Non-member calculates toll for long distance
    Given the user is a non-member
    When the user calculates toll for 25 miles during normal times
    Then the total charge should be $45.00
    And the charge breakdown should show:
      | Description        | Calculation       | Amount |
      | First 20 miles (base) | 20 miles × $2.00 | $40.00 |
      | Next 5 miles (base)   | 5 miles × $1.00  | $5.00  |

  @smoke @membership
  Scenario: Silver member calculates toll for short distance
    Given the user is a "Silver" member
    When the user calculates toll for 10 miles during normal times
    Then the total charge should be $10.00
    And the charge breakdown should show:
      | Description | Calculation      | Amount |
      | Base charge | 10 miles × $1.00 | $10.00 |

  @smoke @membership
  Scenario: Silver member calculates toll for long distance
    Given the user is a "Silver" member
    When the user calculates toll for 25 miles during normal times
    Then the total charge should be $22.50
    And the charge breakdown should show:
      | Description        | Calculation       | Amount |
      | First 20 miles (base) | 20 miles × $1.00 | $20.00 |
      | Next 5 miles (base)   | 5 miles × $0.50  | $2.50  |

  @smoke @membership
  Scenario: Gold member calculates toll during normal times
    Given the user is a "Gold" member
    When the user calculates toll for 25 miles during normal times
    Then the total charge should be $0.00
    And the charge breakdown should show:
      | Description        | Calculation       | Amount |
      | First 20 miles (base) | 20 miles × $0.00 | $0.00  |
      | Next 5 miles (base)   | 5 miles × $0.00  | $0.00  |

  @regression @edge_cases
  Scenario: Calculate toll for exactly 20 miles
    Given the user is a non-member
    When the user calculates toll for 20 miles during normal times
    Then the total charge should be $40.00
    And the charge breakdown should show:
      | Description | Calculation       | Amount |
      | Base charge | 20 miles × $2.00  | $40.00 |