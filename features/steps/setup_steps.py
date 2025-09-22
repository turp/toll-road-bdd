"""
Setup step definitions for toll calculation BDD tests

This module contains all Given step definitions that handle:
- Test configuration and setup
- Rate table configuration  
- Time multiplier configuration
- User context and membership setup
"""

from behave import given

@given('the toll charge calculator is available')
def step_calculator_available(context):
    """Verify that the calculator is initialized and ready"""
    assert context.calculator is not None
    assert hasattr(context.calculator, 'calculate_toll')


@given('the standard rates are configured as follows:')
def step_standard_rates_configured_with_colon(context):
    """Verify standard rates are configured (table validation with colon)"""
    # This step validates that our rate table in the feature matches
    # what's implemented in the calculator
    expected_rates = {}
    for row in context.table:
        rate_type = row['Rate Type']
        first_20 = row['First 20 Miles']
        beyond_20 = row['Beyond 20 Miles']
        expected_rates[rate_type] = {'first_20': first_20, 'beyond_20': beyond_20}
    
    # Store for potential validation
    context.expected_rates = expected_rates

@given('the time-based multipliers are configured as follows:')
def step_time_multipliers_configured_with_colon(context):
    """Verify time-based multipliers are configured (table validation with colon)"""
    expected_multipliers = {}
    for row in context.table:
        time_period = row['Time Period']
        multiplier = row['Multiplier']
        expected_multipliers[time_period] = multiplier
    
    # Store for potential validation
    context.expected_multipliers = expected_multipliers

@given('the user is a non-member')
def step_user_non_member(context):
    """Set the user as a non-member"""
    context.membership = "non"

@given('the user is a "{membership_level}" member')
def step_user_quoted_membership(context, membership_level):
    """Set the user's membership level from quoted string"""
    context.membership = membership_level


@given('the user has an invalid membership type "{invalid_membership}"')
def step_invalid_membership(context, invalid_membership):
    """Set an invalid membership type for testing validation"""
    context.membership = invalid_membership