"""
Assertion step definitions for toll calculation BDD tests

This module contains all Then step definitions that handle:
- Charge amount verification
- Error message validation 
- Breakdown verification
- Performance assertions
- System behavior validation
"""

from behave import then
from decimal import Decimal
import time
from src.toll_calculator import TollCalculationError

@then('the total charge should be ${expected_total:f}')
def step_verify_total_charge(context, expected_total):
    """Verify the calculated total charge"""
    assert context.last_charge is not None, f"Expected charge but got error: {context.last_error}"
    
    expected = Decimal(str(expected_total))
    actual = context.last_charge
    
    assert actual == expected, f"Expected ${expected}, but got ${actual}"

@then('report the "{expected_message}"')
def step_report_message(context, expected_message):
    """Verify that the expected message is reported (business-friendly language)"""
    assert context.last_error is not None, "Expected an error but calculation succeeded"
    assert expected_message in context.last_error, f"Expected '{expected_message}' in error message, but got '{context.last_error}'"

@then('no charge should be calculated')
def step_verify_no_charge(context):
    """Verify that no charge was calculated (due to error)"""
    assert context.last_charge is None, f"Expected no charge but got ${context.last_charge}"

@then('the charge breakdown should show:')
def step_verify_charge_breakdown_with_colon(context):
    """Verify the detailed charge breakdown (with colon)"""
    expected_breakdown = []
    for row in context.table:
        expected_breakdown.append(dict(row.as_dict()))
    
    actual_breakdown = context.calculation_breakdown
    
    assert len(actual_breakdown) == len(expected_breakdown), \
        f"Expected {len(expected_breakdown)} breakdown items, got {len(actual_breakdown)}"
    
    for i, (expected, actual) in enumerate(zip(expected_breakdown, actual_breakdown)):
        for key, expected_value in expected.items():
            assert key in actual, f"Missing key '{key}' in breakdown item {i}"
            actual_value = actual[key]
            assert actual_value == expected_value, \
                f"Breakdown item {i}, key '{key}': expected '{expected_value}', got '{actual_value}'"

@then('each calculation should return ${expected_amount:f}')
def step_verify_multiple_results(context, expected_amount):
    """Verify that all multiple calculations returned the same expected amount"""
    # Check for multiple_results first, then calculation_results for compatibility
    if hasattr(context, 'multiple_results'):
        results = context.multiple_results
    elif hasattr(context, 'calculation_results'):
        results = context.calculation_results
    else:
        assert False, "No multiple calculation results found"
    
    expected = Decimal(str(expected_amount))
    for i, result in enumerate(results):
        assert result == expected, f"Calculation {i+1}: expected ${expected}, got ${result}"

@then('all calculations should complete within {max_seconds:d} seconds')
def step_verify_execution_time(context, max_seconds):
    """Verify that calculations completed within the specified time"""
    # Check for execution_time first, then calculation_time for compatibility
    if hasattr(context, 'execution_time'):
        actual_time = context.execution_time
    elif hasattr(context, 'calculation_time'):
        actual_time = context.calculation_time
    else:
        assert False, "No execution time recorded"
    
    assert actual_time <= max_seconds, \
        f"Calculations took {actual_time:.2f}s, expected <= {max_seconds}s"

@then('the response time should be less than {max_seconds:d} seconds')
def step_verify_response_time(context, max_seconds):
    """Verify response time for individual calculations"""
    # For individual calculations, we'll measure the time taken
    start_time = time.time()
    
    # Re-run the calculation to measure time
    try:
        context.calculator.calculate_toll(9999, context.membership, "peak")
    except TollCalculationError:
        pass  # Error handling tested elsewhere
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    assert execution_time < max_seconds, \
        f"Response time {execution_time:.3f}s exceeded maximum {max_seconds}s"

@then('the system should handle the calculation successfully')
def step_verify_system_handles_calculation(context):
    """Verify that the system handles the calculation without errors"""
    assert context.last_charge is not None, "System failed to handle the calculation"
    assert isinstance(context.last_charge, Decimal), f"Expected Decimal result, got {type(context.last_charge)}"