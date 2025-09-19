# BDD Test Project - Python

This project follows Behavior-Driven Development (BDD) principles using Python and the `behave` framework for automated testing.

## Prompts

```
create a readme file with instructions for a BDD test project written in python. This should include, but not limited to naming conventions, folder structure, feature and scenario structure
```

```
create a copilot instruction file stating that it should use all readme files as a source for instructions
```

```
Create a set of BDD tests for the website https://apps.irs.gov/app/tax-withholding-estimator. When you have created the features, wait for me to validate them before implementing the test logic using python. Once I have validated the features, implement the scenarios one at a time, executing the tests and fixing linting issues as you go. Once you have implemented the first three scenarios and verified that they execute properly, ask for permission to implement the rest of the scenarios.
```

## Table of Contents

- [Setup and Installation](#setup-and-installation)
- [Project Structure](#project-structure)
- [Naming Conventions](#naming-conventions)
- [Feature File Structure](#feature-file-structure)
- [Scenario Structure](#scenario-structure)
- [Step Definitions](#step-definitions)
- [Running Tests](#running-tests)
- [Best Practices](#best-practices)
- [Examples](#examples)

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Required Dependencies
```txt
behave>=1.2.6
selenium>=4.0.0
requests>=2.28.0
pytest>=7.0.0
allure-behave>=2.12.0
```

## Project Structure

```
tax-calc-bdd/
├── features/
│   ├── steps/
│   │   ├── __init__.py
│   │   ├── common_steps.py
│   │   ├── calculation_steps.py
│   │   └── validation_steps.py
│   ├── support/
│   │   ├── __init__.py
│   │   ├── environment.py
│   │   ├── hooks.py
│   │   └── utilities.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   └── calculator_page.py
│   ├── data/
│   │   ├── test_data.json
│   │   └── config.yaml
│   ├── tax_calculation.feature
│   ├── user_interface.feature
│   └── api_validation.feature
├── reports/
│   └── allure-results/
├── config/
│   ├── test_config.py
│   └── environment_config.py
├── requirements.txt
├── behave.ini
└── README.md
```

## Naming Conventions

### Files and Directories
- **Feature files**: Use lowercase with underscores (`tax_calculation.feature`)
- **Step definition files**: Use lowercase with underscores ending in `_steps.py` (`calculation_steps.py`)
- **Page object files**: Use lowercase with underscores ending in `_page.py` (`calculator_page.py`)
- **Utility files**: Use lowercase with underscores (`utilities.py`)

### Variables and Functions
- **Python variables**: Use snake_case (`user_input`, `tax_amount`)
- **Functions**: Use snake_case (`calculate_tax`, `validate_result`)
- **Constants**: Use UPPER_SNAKE_CASE (`BASE_URL`, `DEFAULT_TIMEOUT`)

### Gherkin Keywords
- **Feature names**: Use Title Case (`Tax Calculation Validation`)
- **Scenario names**: Use descriptive sentences (`User calculates income tax for single filer`)
- **Step names**: Use natural language (`Given the user is on the tax calculator page`)

## Feature File Structure

### Feature Template
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

### Feature File Guidelines
- One feature per file
- Start with feature description using user story format
- Use Background for common setup steps
- Group related scenarios in the same feature
- Use meaningful tags for test organization

## Scenario Structure

### Scenario Best Practices
- **Given**: Set up the initial state (preconditions)
- **When**: Describe the action being performed
- **Then**: Verify the expected outcome
- **And/But**: Chain additional steps of the same type

### Good Scenario Examples
```gherkin
Scenario: Calculate tax for single filer with standard deduction
  Given the user is on the tax calculator page
  And the filing status is set to "Single"
  And the annual income is set to "50000"
  When the user clicks the calculate button
  Then the calculated tax should be "5739"
  And the effective tax rate should be "11.48%"
```

### Scenario Outline Usage
```gherkin
Scenario Outline: Validate tax calculation for different income levels
  Given the user is on the tax calculator page
  And the filing status is set to "<filing_status>"
  When the user enters annual income of "<income>"
  And clicks the calculate button
  Then the calculated tax should be "<expected_tax>"

  Examples:
    | filing_status    | income | expected_tax |
    | Single           | 30000  | 3219         |
    | Married Filing   | 60000  | 6878         |
    | Head of Household| 45000  | 4758         |
```

## Step Definitions

### Step Definition Structure
```python
from behave import given, when, then, step
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@given('the user is on the tax calculator page')
def step_user_on_calculator_page(context):
    """Navigate to the tax calculator page."""
    context.calculator_page = CalculatorPage(context.driver)
    context.calculator_page.navigate_to_page()

@when('the user enters annual income of "{income}"')
def step_enter_annual_income(context, income):
    """Enter the annual income value."""
    context.calculator_page.enter_income(income)
    context.entered_income = income

@then('the calculated tax should be "{expected_tax}"')
def step_verify_calculated_tax(context, expected_tax):
    """Verify the calculated tax amount."""
    actual_tax = context.calculator_page.get_calculated_tax()
    assert actual_tax == expected_tax, f"Expected {expected_tax}, but got {actual_tax}"
```

### Step Definition Guidelines
- One step definition per function
- Use descriptive function names
- Include docstrings for complex steps
- Store reusable data in context object
- Use parametrized steps for flexibility

## Running Tests

### Basic Commands
```bash
# Run all tests
behave

# Run specific feature
behave features/tax_calculation.feature

# Run tests with specific tags
behave --tags=@smoke
behave --tags=@regression
behave --tags="@priority_high and not @wip"

# Run with specific format
behave --format=pretty
behave --format=json --outfile=reports/results.json

# Run with Allure reporting
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

### Configuration File (behave.ini)
```ini
[behave]
default_format = pretty
show_timings = true
show_skipped = false
junit = true
junit_directory = reports/junit
tags = ~@skip
paths = features
```

## Best Practices

### Feature Writing
- Write features from user perspective
- Use domain language, not technical jargon
- Keep scenarios independent and atomic
- Use meaningful and descriptive names
- Avoid implementation details in scenarios

### Step Implementation
- Keep steps simple and focused
- Reuse common steps across features
- Use Page Object Model for UI interactions
- Implement proper error handling
- Use assertion libraries for validations

### Data Management
- Store test data in separate files (JSON, YAML)
- Use environment-specific configurations
- Parametrize scenarios for data-driven testing
- Keep sensitive data in environment variables

### Test Organization
- Group related scenarios in features
- Use tags for test categorization
- Implement proper setup/teardown in hooks
- Create reusable utility functions

## Examples

### Complete Feature Example
```gherkin
@tax_calculation @priority_high
Feature: Tax Calculation Validation
  As a taxpayer
  I want to calculate my income tax accurately
  So that I can plan my finances effectively

  Background:
    Given the tax calculator application is running
    And the current tax year is set to 2024

  @smoke @single_filer
  Scenario: Calculate tax for single filer with standard deduction
    Given the user selects "Single" filing status
    And the user has an annual income of "75000"
    And the user chooses standard deduction
    When the user calculates the tax
    Then the federal tax should be "8739"
    And the effective tax rate should be "11.65%"
    And the tax bracket should be "22%"

  @regression @married_filing
  Scenario Outline: Validate tax for married filing jointly
    Given the user selects "Married Filing Jointly" filing status
    And the user has an annual income of "<income>"
    When the user calculates the tax
    Then the federal tax should be "<expected_tax>"

    Examples:
      | income | expected_tax |
      | 50000  | 5147         |
      | 100000 | 14605        |
      | 150000 | 24905        |
```

### Environment Setup (environment.py)
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    """Setup before all tests."""
    context.base_url = "http://localhost:3000"
    
def before_feature(context, feature):
    """Setup before each feature."""
    if 'web' in feature.tags:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        context.driver = webdriver.Chrome(options=chrome_options)
        context.driver.implicitly_wait(10)

def after_feature(context, feature):
    """Cleanup after each feature."""
    if hasattr(context, 'driver'):
        context.driver.quit()
```

---

## Contributing

1. Follow the established naming conventions
2. Write clear, descriptive scenarios
3. Implement reusable step definitions
4. Add appropriate tags for test organization
5. Update documentation for new features

## Support

For questions or issues, please refer to the project documentation or contact the development team.
