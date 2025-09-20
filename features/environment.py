"""
Behave environment setup and configuration

This module sets up the test environment for BDD tests,
including any necessary setup and teardown operations.
"""

import sys
import os

# Add the src directory to the Python path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.toll_calculator import TollCalculator


def before_all(context):
    """
    Setup performed before all tests
    """
    # Initialize any global test configuration here
    context.config.setup_logging()


def before_scenario(context, scenario):
    """
    Setup performed before each scenario
    """
    # Create a fresh calculator instance for each scenario
    context.calculator = TollCalculator()
    context.last_charge = None
    context.last_error = None
    context.calculation_breakdown = []


def after_scenario(context, scenario):
    """
    Cleanup performed after each scenario
    """
    # Clean up any resources if needed
    context.calculator = None
    context.last_charge = None
    context.last_error = None
    context.calculation_breakdown = []