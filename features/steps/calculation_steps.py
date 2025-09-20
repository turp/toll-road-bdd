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