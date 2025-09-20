"""
Specific step definitions for toll calculation scenarios

This module contains step definitions that handle the specific
calculation scenarios in our feature files.
"""

from behave import given, when, then
from decimal import Decimal
import time
from src.toll_calculator import TollCalculationError


# Specific calculation steps
@when('the user calculates toll for {distance:f} miles during normal times')
def step_calculate_toll_normal(context, distance):
    """Calculate toll for normal times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            distance, context.membership, "normal"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for {distance:f} miles during busy times')
def step_calculate_toll_busy(context, distance):
    """Calculate toll for busy times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            distance, context.membership, "busy"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for {distance:f} miles during peak times')
def step_calculate_toll_peak(context, distance):
    """Calculate toll for peak times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            distance, context.membership, "peak"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


# Specific distance calculations for exact scenarios
@when('the user calculates toll for 10 miles during normal times')
def step_calculate_10_miles_normal(context):
    """Calculate toll for 10 miles during normal times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            10.0, context.membership, "normal"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 25 miles during normal times')
def step_calculate_25_miles_normal(context):
    """Calculate toll for 25 miles during normal times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            25.0, context.membership, "normal"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 20 miles during normal times')
def step_calculate_20_miles_normal(context):
    """Calculate toll for 20 miles during normal times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            20.0, context.membership, "normal"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 5 miles during normal times')
def step_calculate_5_miles_normal(context):
    """Calculate toll for 5 miles during normal times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            5.0, context.membership, "normal"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 15 miles during normal times')
def step_calculate_15_miles_normal(context):
    """Calculate toll for 15 miles during normal times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            15.0, context.membership, "normal"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 30 miles during normal times')
def step_calculate_30_miles_normal(context):
    """Calculate toll for 30 miles during normal times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            30.0, context.membership, "normal"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


# Specific calculations for busy and peak times
@when('the user calculates toll for 10 miles during busy times')
def step_calculate_10_miles_busy(context):
    """Calculate toll for 10 miles during busy times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            10.0, context.membership, "busy"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 10 miles during peak times')
def step_calculate_10_miles_peak(context):
    """Calculate toll for 10 miles during peak times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            10.0, context.membership, "peak"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 25 miles during busy times')
def step_calculate_25_miles_busy(context):
    """Calculate toll for 25 miles during busy times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            25.0, context.membership, "busy"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 25 miles during peak times')
def step_calculate_25_miles_peak(context):
    """Calculate toll for 25 miles during peak times"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            25.0, context.membership, "peak"
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


# Error testing steps
@when('the user attempts to calculate toll for 0 miles')
def step_attempt_calculate_zero_miles(context):
    """Attempt to calculate toll for 0 miles (should fail)"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            0.0, context.membership, "normal"
        )
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for 1000 miles during normal times')
def step_calculate_toll_1000_miles_normal(context):
    """Calculate toll for 1000 miles during normal times"""
    context.last_charge = context.calculator.calculate_toll(
        1000.0, context.membership, "normal"
    )
    context.calculation_breakdown = context.calculator.get_charge_breakdown()


@when('the user attempts to calculate toll for -5 miles')
def step_attempt_calculate_negative_miles(context):
    """Attempt to calculate toll for negative miles (should fail)"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            -5.0, context.membership, "normal"
        )
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user calculates toll for {distance:g} miles during busy times')
def step_calculate_toll_busy_times(context, distance):
    """Calculate toll for specific distance during busy times"""
    context.last_charge = context.calculator.calculate_toll(
        distance, context.membership, "busy"
    )


@when('the user calculates toll for {distance:g} miles during peak times')
def step_calculate_toll_peak_times(context, distance):
    """Calculate toll for specific distance during peak times"""
    import time
    start_time = time.time()
    
    context.last_charge = context.calculator.calculate_toll(
        distance, context.membership, "peak"
    )
    
    end_time = time.time()
    context.calculation_time = end_time - start_time


@when('the user attempts to calculate toll for {distance:g} miles during normal times')
def step_attempt_calculate_toll_normal_times(context, distance):
    """Attempt to calculate toll (may fail for invalid inputs)"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            distance, context.membership, "normal"
        )
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None


@when('the user performs {count:d} toll calculations for {distance:g} miles during normal times')
def step_perform_multiple_calculations(context, count, distance):
    """Perform multiple toll calculations for performance testing"""
    import time
    start_time = time.time()
    
    context.calculation_results = []
    for i in range(count):
        charge = context.calculator.calculate_toll(distance, context.membership, "normal")
        context.calculation_results.append(charge)
    
    end_time = time.time()
    context.calculation_time = end_time - start_time
    context.last_charge = context.calculation_results[-1] if context.calculation_results else None


@then('each calculation should return ${amount:g}')
def step_verify_each_calculation_amount(context, amount):
    """Verify that each calculation returns the expected amount"""
    expected_amount = Decimal(str(amount))
    for result in context.calculation_results:
        assert result == expected_amount, f"Expected ${expected_amount}, got ${result}"


@then('all calculations should complete within {seconds:g} seconds')
def step_verify_calculation_time(context, seconds):
    """Verify that all calculations complete within the specified time"""
    assert context.calculation_time <= seconds, f"Calculations took {context.calculation_time:.3f}s, expected <= {seconds}s"


@then('the system should handle the calculation successfully')
def step_verify_system_handles_calculation(context):
    """Verify that the system handles the calculation without errors"""
    assert context.last_charge is not None, "System failed to handle the calculation"
    assert isinstance(context.last_charge, Decimal), f"Expected Decimal result, got {type(context.last_charge)}"


@then('the response time should be less than {seconds:g} seconds')
def step_verify_response_time(context, seconds):
    """Verify that the response time is within acceptable limits"""
    assert hasattr(context, 'calculation_time'), "No calculation time recorded"
    assert context.calculation_time < seconds, f"Response time {context.calculation_time:.3f}s exceeded limit of {seconds}s"