"""
Action step definitions for toll calculation BDD tests

This module contains all When step definitions that handle:
- User actions and toll calculations
- Error scenarios and invalid inputs
- Performance testing actions
- All calculation variations (parametrized and hardcoded)
"""

from behave import when
import time
from src.toll_calculator import TollCalculationError

@when('the user attempts to calculate toll for {distance:g} miles')
def step_attempt_calculate_toll_invalid_distance(context, distance):
    """Attempt to calculate toll with potentially invalid distance"""
    try:
        # Use normal time period as default for error testing
        context.last_charge = context.calculator.calculate_toll(
            distance, context.membership, "normal"
        )
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None

@when('the user calculates toll for {distance:g} miles during {time_period} times')
def step_calculate_toll(context, distance, time_period):
    """Calculate toll for given distance and time period"""
    try:
        context.last_charge = context.calculator.calculate_toll(
            distance, context.membership, time_period
        )
        context.calculation_breakdown = context.calculator.get_charge_breakdown()
        context.last_error = None
    except TollCalculationError as e:
        context.last_error = str(e)
        context.last_charge = None

@when('the user performs {count:d} toll calculations for {distance:g} miles during {time_period} times')
def step_multiple_calculations(context, count, distance, time_period):
    """Perform multiple rapid calculations for performance testing"""
    start_time = time.time()
    results = []
    
    for _ in range(count):
        try:
            charge = context.calculator.calculate_toll(distance, context.membership, time_period)
            results.append(charge)
        except TollCalculationError as e:
            context.last_error = str(e)
            return
    
    end_time = time.time()
    context.execution_time = end_time - start_time
    context.multiple_results = results
    context.last_charge = results[0] if results else None
    