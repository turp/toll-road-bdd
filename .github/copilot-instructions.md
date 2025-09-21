# GitHub Copilot Instructions

## General Guidelines

GitHub Copilot should use all README files in this repository as the primary source of instructions and conventions when providing code suggestions, completions, and recommendations.

## 📚 Onboarding

At the start of each session, read:
1. Any `**/README.md` docs across the project
2. Any `**/README.*.md` docs across the project

## BDD Development Guidelines

### Naming Conventions

#### Files and Directories
- **Feature files**: Use lowercase with underscores (`toll_calculation.feature`)
- **Step definition files**: Use lowercase with underscores ending in `_steps.py` (`calculation_steps.py`)
- **Page object files**: Use lowercase with underscores ending in `_page.py` (`calculator_page.py`)
- **Utility files**: Use lowercase with underscores (`utilities.py`)

#### Variables and Functions
- **Python variables**: Use snake_case (`user_input`, `toll_amount`)
- **Functions**: Use snake_case (`calculate_toll`, `validate_result`)
- **Constants**: Use UPPER_SNAKE_CASE (`BASE_URL`, `DEFAULT_TIMEOUT`)

#### Gherkin Keywords
- **Feature names**: Use Title Case (`Toll Calculation Validation`)
- **Scenario names**: Use descriptive sentences (`User calculates toll for non-member`)
- **Step names**: Use natural language (`Given the user is a non-member`)

### Feature File Structure

#### Feature Template
```gherkin
@feature_tag @priority_high
Feature: Feature Name
  As a [user type]
  I want to [perform action]
  So that [achieve goal]

  Background:
    Given common preconditions for all scenarios

  @scenario_tag @smoke
  Scenario: Scenario description
    Given initial conditions
    When user performs action
    Then expected outcome occurs

  @scenario_tag @regression
  Scenario Outline: Scenario with multiple data sets
    Given initial conditions with "<parameter>"
    When user performs action with "<input>"
    Then expected outcome is "<result>"

    Examples:
      | parameter | input | result |
      | value1    | data1 | exp1   |
      | value2    | data2 | exp2   |
```

#### Feature File Guidelines
- One feature per file
- Start with feature description using user story format
- Use Background for common setup steps
- Group related scenarios in the same feature
- Use meaningful tags for test organization

### Scenario Structure

#### Scenario Best Practices
- **Given**: Set up the initial state (preconditions)
- **When**: Describe the action being performed
- **Then**: Verify the expected outcome
- **And/But**: Chain additional steps of the same type

#### Good Scenario Examples
```gherkin
Scenario: Calculate toll for non-member short distance
  Given the toll charge calculator is available
  And the user is a non-member
  When the user calculates toll for 10 miles during normal times
  Then the total charge should be $20.00
  And the charge breakdown should show:
    | Description | Calculation      | Amount |
    | Base charge | 10 miles × $2.00 | $20.00 |
```

#### Scenario Outline Usage
```gherkin
Scenario Outline: Validate toll calculation for different membership levels
  Given the toll charge calculator is available
  And the user is a "<membership>" member
  When the user calculates toll for <distance> miles during <time_period> times
  Then the total charge should be $<expected_charge>

  Examples:
    | membership | distance | time_period | expected_charge |
    | non        | 5        | normal      | 10.00           |
    | Silver     | 5        | normal      | 5.00            |
    | Gold       | 5        | normal      | 0.00            |
```

### Step Definitions

#### Step Definition Structure
```python
from behave import given, when, then, step
from decimal import Decimal
from src.toll_calculator import TollCalculator

@given('the user is a {membership_level} member')
def step_user_membership(context, membership_level):
    """Set the user's membership level."""
    context.membership = membership_level

@when('the user calculates toll for {distance:f} miles during {time_period} times')
def step_calculate_toll(context, distance, time_period):
    """Calculate toll for given distance and time period."""
    context.last_charge = context.calculator.calculate_toll(
        distance, context.membership, time_period
    )
    context.calculation_breakdown = context.calculator.get_charge_breakdown()

@then('the total charge should be ${expected_amount:f}')
def step_verify_total_charge(context, expected_amount):
    """Verify the calculated toll amount."""
    expected = Decimal(str(expected_amount))
    assert context.last_charge == expected, f"Expected ${expected}, but got ${context.last_charge}"
```

#### Step Definition Guidelines
- One step definition per function
- Use descriptive function names
- Include docstrings for complex steps
- Store reusable data in context object
- Use parametrized steps for flexibility

### Test Organization

#### Environment Hooks and Setup
- **Use hooks for technical setup**: Implement `before_scenario` hooks in `environment.py` for technical initialization
- **Avoid redundant setup steps**: Do not include technical setup steps like "Given the toll charge calculator is available" in scenarios when they're handled by hooks
- **Keep scenarios business-focused**: Scenarios should focus on business behavior, not technical infrastructure
- **Use Background sparingly**: Only use Background for business domain setup that's relevant to all scenarios in a feature

#### Example: Proper Hook Usage
```python
# In environment.py
def before_scenario(context, scenario):
    """Setup performed before each scenario"""
    context.calculator = TollCalculator()  # Technical setup
    context.last_charge = None
    context.last_error = None
```

```gherkin
# In feature files - AVOID this redundant step
# Given the toll charge calculator is available  # ❌ Technical, handled by hook

# Instead focus on business context
Given the user is a non-member  # ✅ Business-focused
When the user calculates toll for 10 miles during normal times
Then the total charge should be $20.00
```

#### Business-Friendly Language
- **Use natural business language**: Prefer "report the" over "error message should be displayed"
- **Avoid technical jargon**: Write scenarios from user perspective, not system perspective
- **Focus on outcomes**: Describe what the business expects, not how the system implements it

#### Example: Business-Friendly Error Handling
```gherkin
# ❌ Technical language
Then an error message should be displayed saying "Distance must be greater than 0"

# ✅ Business-friendly language  
Then report the "Distance must be greater than 0"
```

#### Scenario Organization
- **Start with comprehensive scenarios**: Place broad test matrices first to set the foundation
- **Follow with boundary testing**: Add edge cases that test specific thresholds
- **End with specific validations**: Include detailed error cases and special conditions
- **Think like a book**: Explain simple concepts first, then build complexity

#### Best Practices
- Write features from user perspective
- Use domain language, not technical jargon
- Keep scenarios independent and atomic
- Use meaningful and descriptive names
- Avoid implementation details in scenarios

#### Step Implementation
- Keep steps simple and focused
- Reuse common steps across features
- Use proper error handling
- Use assertion libraries for validations

#### Data Management
- Store test data in separate files (JSON, YAML)
- Use environment-specific configurations
- Parametrize scenarios for data-driven testing
- Keep sensitive data in environment variables

#### Test Organization
- Group related scenarios in features
- Use tags for test categorization
- Implement proper setup/teardown in hooks
- Create reusable utility functions