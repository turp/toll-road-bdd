# Toll Road BDD Calculator

A comprehensive toll charge calculation system built using Behavior-Driven Development (BDD) principles with Python and the `behave` framework.

## Project Overview

This project implements a robust toll calculation system that handles:

- **Multiple membership tiers**: Non-member, Silver, and Gold with different pricing structures
- **Distance-based pricing**: Different rates for first 20 miles vs. beyond 20 miles
- **Time-based multipliers**: Normal (1x), Busy (2x), and Peak (3x) pricing periods
- **Comprehensive validation**: Edge cases, boundary testing, and error handling
- **Detailed breakdowns**: Itemized charge calculations for transparency

### Business Rules

| Membership | First 20 Miles | Beyond 20 Miles | Special Rules |
|------------|----------------|-----------------|---------------|
| Non-member | $2.00/mile     | $1.00/mile      | Standard rates apply |
| Silver     | $1.00/mile     | $0.50/mile      | 50% discount on base rates |
| Gold       | $0.00/mile     | $0.00/mile*     | Free during normal times |

*Gold members pay 25% of base rate during busy/peak times for miles beyond 20.

### Time Multipliers
- **Normal times**: 1x base rate
- **Busy times**: 2x base rate  
- **Peak times**: 3x base rate

*Note: Gold members are exempt from time multipliers during normal times only.*

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # On Linux/Mac:
   source .venv/bin/activate
   # On Windows:
   # .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Required Dependencies
- `behave>=1.2.6` - BDD testing framework
- `decimal` - Precise decimal calculations (built-in)

## Running Tests

### Prerequisites
Make sure your virtual environment is activated before running tests:

```bash
# Activate virtual environment
source .venv/bin/activate
# On Windows: .venv\Scripts\activate
```

### Basic Commands

```bash
# Activate environment first
source .venv/bin/activate

# Run all tests
behave

# Run specific feature
behave features/toll_calculation.feature

# Run tests with specific tags
behave --tags=@smoke
behave --tags=@edge_cases
behave --tags="@priority_high and not @wip"

# Run with verbose output
behave --format=pretty

# Run without capture for debugging
behave --no-capture
```

### Alternative: Using Python Module

If `behave` command is not found, use the Python module directly:

```bash
# Activate environment first
source .venv/bin/activate

# Run all tests using Python module
python -m behave

# Run specific feature
python -m behave features/toll_calculation.feature

# Run with tags
python -m behave --tags=@smoke
```

### Test Categories

The test suite includes comprehensive coverage:

- **🔥 Smoke Tests** (`@smoke`): Core functionality validation
- **🔍 Edge Cases** (`@edge_cases`): Boundary conditions and error handling  
- **⚡ Performance** (`@performance`): Stress testing and timing validation
- **🔄 Regression** (`@regression`): Full feature validation
- **🏆 Priority High** (`@priority_high`): Critical path scenarios

### Configuration File (behave.ini)
```ini
[behave]
default_format = pretty
show_timings = true
show_skipped = false
paths = features
```

## Test Results

The current test suite achieves **100% pass rate**:

- ✅ **7 features passed, 0 failed**
- ✅ **81 scenarios passed, 0 failed**  
- ✅ **378 steps passed, 0 failed**

### Coverage Includes:
- Basic toll calculations for all membership levels
- Distance-based pricing (under/over 20 miles)
- Time-based multipliers (normal/busy/peak)
- Edge cases (invalid inputs, large numbers, fractional distances)
- Boundary testing (exactly 20 miles, 19.99 vs 20.01)
- Performance validation (100 rapid calculations)
- System limits (maximum reasonable distances)
- Comprehensive error handling

## Example Usage

### Basic Calculation
```python
from src.toll_calculator import TollCalculator

calculator = TollCalculator()

# Non-member, 15 miles, normal times
charge = calculator.calculate_toll(15.0, "non", "normal")
print(f"Charge: ${charge}")  # Output: Charge: $30.00

# Get detailed breakdown
breakdown = calculator.get_charge_breakdown()
for item in breakdown:
    print(f"{item['Description']}: {item['Amount']}")
```

### Sample BDD Scenario
```gherkin
Scenario: Silver member calculates toll for long distance during peak times
  Given the toll charge calculator is available
  And the user is a "Silver" member
  When the user calculates toll for 25 miles during peak times
  Then the total charge should be $67.50
  And the charge breakdown should show:
    | Description           | Calculation      | Amount |
    | First 20 miles (base) | 20 miles × $1.00 | $20.00 |
    | Next 5 miles (base)   | 5 miles × $0.50  | $2.50  |
    | Total base charge     | $20.00 + $2.50   | $22.50 |
    | Peak time multiplier  | $22.50 × 3       | $67.50 |
```

## Contributing

1. Follow the BDD principles and naming conventions in `.github/copilot-instructions.md`
2. Write clear, descriptive scenarios using Gherkin syntax
3. Implement reusable step definitions
4. Add appropriate tags for test organization
5. Ensure all tests pass before committing

## License

This project is for educational and demonstration purposes.
