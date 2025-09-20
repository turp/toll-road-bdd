"""
Toll Calculator Implementation

This module provides the core business logic for calculating toll charges
based on distance, membership level, and time period.
"""

from enum import Enum
from typing import Dict, List, Tuple
from decimal import Decimal, ROUND_HALF_UP


class MembershipLevel(Enum):
    """Enum for different membership levels"""
    NON_MEMBER = "non"
    SILVER = "Silver"
    GOLD = "Gold"


class TimePeriod(Enum):
    """Enum for different time periods"""
    NORMAL = "normal"
    BUSY = "busy"
    PEAK = "peak"


class TollCalculationError(Exception):
    """Custom exception for toll calculation errors"""
    pass


class TollCalculator:
    """
    Main toll calculator class that handles all toll charge calculations
    """
    
    # Base rates per mile for first 20 miles
    BASE_RATES_FIRST_20 = {
        MembershipLevel.NON_MEMBER: Decimal("2.00"),
        MembershipLevel.SILVER: Decimal("1.00"),
        MembershipLevel.GOLD: Decimal("0.00")
    }
    
    # Base rates per mile for miles beyond 20
    BASE_RATES_BEYOND_20 = {
        MembershipLevel.NON_MEMBER: Decimal("1.00"),
        MembershipLevel.SILVER: Decimal("0.50"),
        MembershipLevel.GOLD: Decimal("0.00")
    }
    
    # Time period multipliers
    TIME_MULTIPLIERS = {
        TimePeriod.NORMAL: Decimal("1.0"),
        TimePeriod.BUSY: Decimal("2.0"),
        TimePeriod.PEAK: Decimal("3.0")
    }
    
    def __init__(self):
        self.last_calculation_breakdown = []
    
    def calculate_toll(self, distance: float, membership: str, time_period: str) -> Decimal:
        """
        Calculate toll charge for given parameters
        
        Args:
            distance: Distance in miles (must be > 0)
            membership: Membership level ("non", "Silver", "Gold")
            time_period: Time period ("normal", "busy", "peak")
            
        Returns:
            Total toll charge as Decimal
            
        Raises:
            TollCalculationError: If inputs are invalid
        """
        # Validate inputs
        self._validate_inputs(distance, membership, time_period)
        
        # Convert string inputs to enums
        membership_level = self._parse_membership(membership)
        time_period_enum = self._parse_time_period(time_period)
        
        # Convert distance to Decimal for precise calculations
        distance_decimal = Decimal(str(distance))
        
        # Calculate base charge
        base_charge = self._calculate_base_charge(distance_decimal, membership_level)
        
        # Apply time multiplier
        final_charge = self._apply_time_multiplier(
            base_charge, time_period_enum, membership_level, distance_decimal
        )
        
        # Round to 2 decimal places
        return final_charge.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    def get_charge_breakdown(self) -> List[Dict[str, str]]:
        """
        Get detailed breakdown of the last calculation
        
        Returns:
            List of dictionaries containing breakdown details
        """
        return self.last_calculation_breakdown.copy()
    
    def _validate_inputs(self, distance: float, membership: str, time_period: str):
        """Validate input parameters"""
        if distance <= 0:
            raise TollCalculationError("Distance must be greater than 0")
        
        valid_memberships = ["non", "Silver", "Gold"]
        if membership not in valid_memberships:
            raise TollCalculationError("Invalid membership type")
        
        valid_time_periods = ["normal", "busy", "peak"]
        if time_period not in valid_time_periods:
            raise TollCalculationError(f"Invalid time period: {time_period}")
    
    def _parse_membership(self, membership: str) -> MembershipLevel:
        """Parse membership string to enum"""
        if membership == "non":
            return MembershipLevel.NON_MEMBER
        elif membership == "Silver":
            return MembershipLevel.SILVER
        elif membership == "Gold":
            return MembershipLevel.GOLD
        else:
            raise TollCalculationError(f"Invalid membership: {membership}")
    
    def _parse_time_period(self, time_period: str) -> TimePeriod:
        """Parse time period string to enum"""
        if time_period == "normal":
            return TimePeriod.NORMAL
        elif time_period == "busy":
            return TimePeriod.BUSY
        elif time_period == "peak":
            return TimePeriod.PEAK
        else:
            raise TollCalculationError(f"Invalid time period: {time_period}")
    
    def _calculate_base_charge(self, distance: Decimal, membership: MembershipLevel) -> Decimal:
        """Calculate base charge before time multipliers"""
        self.last_calculation_breakdown = []
        
        if distance <= 20:
            # All miles are in the first tier
            rate = self.BASE_RATES_FIRST_20[membership]
            charge = distance * rate
            
            # Format distance to remove unnecessary decimal places
            if distance == int(distance):
                distance_str = str(int(distance))
            else:
                distance_str = str(distance)
            
            self.last_calculation_breakdown.append({
                "Description": f"Base charge",
                "Calculation": f"{distance_str} miles × ${rate}",
                "Amount": f"${charge:.2f}"
            })
            
            return charge
        else:
            # Split between first 20 miles and remaining miles
            first_20_rate = self.BASE_RATES_FIRST_20[membership]
            beyond_20_rate = self.BASE_RATES_BEYOND_20[membership]
            
            first_20_charge = Decimal("20") * first_20_rate
            remaining_miles = distance - Decimal("20")
            remaining_charge = remaining_miles * beyond_20_rate
            
            # Format remaining miles to remove unnecessary decimal places
            if remaining_miles == int(remaining_miles):
                remaining_str = str(int(remaining_miles))
            else:
                remaining_str = str(remaining_miles)
            
            self.last_calculation_breakdown.extend([
                {
                    "Description": "First 20 miles (base)",
                    "Calculation": f"20 miles × ${first_20_rate}",
                    "Amount": f"${first_20_charge:.2f}"
                },
                {
                    "Description": f"Next {remaining_str} miles (base)",
                    "Calculation": f"{remaining_str} miles × ${beyond_20_rate}",
                    "Amount": f"${remaining_charge:.2f}"
                }
            ])
            
            return first_20_charge + remaining_charge
    
    def _apply_time_multiplier(self, base_charge: Decimal, time_period: TimePeriod, 
                             membership: MembershipLevel, distance: Decimal) -> Decimal:
        """Apply time-based multipliers with special Gold member logic"""
        multiplier = self.TIME_MULTIPLIERS[time_period]
        
        # Special logic for Gold members during busy/peak times
        if membership == MembershipLevel.GOLD and time_period != TimePeriod.NORMAL:
            if distance <= 20:
                # Gold members are free for first 20 miles but we still show the calculation
                final_charge = Decimal("0.00")
                
                # Update breakdown to show time multiplier calculation
                multiplier_str = str(int(multiplier)) if multiplier == int(multiplier) else str(multiplier)
                self.last_calculation_breakdown.append({
                    "Description": f"{time_period.value.title()} time multiplier",
                    "Calculation": f"${base_charge:.2f} × {multiplier_str}",
                    "Amount": f"${final_charge:.2f}"
                })
                
                return final_charge
            else:
                # Gold members pay 25% of the normal rate for miles beyond 20
                # during busy/peak times
                remaining_miles = distance - Decimal("20")
                beyond_20_rate = Decimal("0.25")  # 25% of $1.00 base rate
                charge = remaining_miles * beyond_20_rate * multiplier
                
                # Format remaining miles and multiplier for display
                remaining_str = str(int(remaining_miles)) if remaining_miles == int(remaining_miles) else str(remaining_miles)
                multiplier_str = str(int(multiplier)) if multiplier == int(multiplier) else str(multiplier)
                
                # Update breakdown for Gold member special case
                self.last_calculation_breakdown = [
                    {
                        "Description": "First 20 miles (free)",
                        "Calculation": f"20 miles × $0.00",
                        "Amount": "$0.00"
                    },
                    {
                        "Description": f"Next {remaining_str} miles (base)",
                        "Calculation": f"{remaining_str} miles × $0.25",
                        "Amount": f"${remaining_miles * beyond_20_rate:.2f}"
                    },
                    {
                        "Description": f"{time_period.value.title()} time multiplier",
                        "Calculation": f"${remaining_miles * beyond_20_rate:.2f} × {multiplier_str}",
                        "Amount": f"${charge:.2f}"
                    }
                ]
                
                return charge
        
        # Normal time multiplier logic
        if time_period == TimePeriod.NORMAL:
            return base_charge
        
        final_charge = base_charge * multiplier
        
        # For long distance scenarios (beyond 20 miles), add total base charge breakdown item
        if len(self.last_calculation_breakdown) > 1:
            total_base = sum(Decimal(item["Amount"].replace("$", "")) for item in self.last_calculation_breakdown)
            self.last_calculation_breakdown.append({
                "Description": "Total base charge",
                "Calculation": " + ".join([item["Amount"] for item in self.last_calculation_breakdown]),
                "Amount": f"${total_base:.2f}"
            })
        
        # Update breakdown to show time multiplier
        if base_charge > 0:
            # Format multiplier to remove unnecessary decimal places
            if multiplier == int(multiplier):
                multiplier_str = str(int(multiplier))
            else:
                multiplier_str = str(multiplier)
            
            self.last_calculation_breakdown.append({
                "Description": f"{time_period.value.title()} time multiplier",
                "Calculation": f"${base_charge:.2f} × {multiplier_str}",
                "Amount": f"${final_charge:.2f}"
            })
        
        return final_charge