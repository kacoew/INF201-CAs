"""
INF201 - Deliverable 4
Task 1: Temperature Class

A Python class for representing, converting, and comparing
temperatures in Celsius (C), Fahrenheit (F), and Kelvin (K).

Features:
    1. Initialization and validation:
       - Default unit: Celsius
       - Case-insensitive units, only C, F and K are accepted
       - Rejects temperatures below absolute zero (0 K)

    2. Tolerance:
       - Uses an absolute tolerance of 1e-9 for float comparisons

    3. Expose value and unit as read-only attributes

    4. Temperature conversions:
       - to_celsius(), to_fahrenheit(), to_kelvin()
       - convert_to(target_unit)

    5. String representations:
       - __str__(): Human-readable temperature
       - __repr__(): Unambiguous object representation

    6. Comparison operators:
       - ==, !=, <, <=, >, >= across different units
"""


# IMPORTS

# lets us write "-> Temperature" inside the class before the class is finished
from __future__ import annotations


# CONSTANTS

# the only units the class accepts
VALID_UNITS = ("C", "F", "K")

# two temperatures closer than this count as equal (floats are never exact)
TOLERANCE = 1e-9


# TEMPERATURE CLASS

class Temperature:
    """A temperature with a value and unit."""


    # 1. INITIALIZATION AND VALIDATION

    # runs when a new Temperature is made, e.g. Temperature(25, "c")
    def __init__(self, value: float, unit: str = "C") -> None:
        """
        Initialise Temperature.

        Args:
            value (float): The temperature value.
            unit (str): The unit of the temperature ("C", "F", or "K"). Default is "C".

        Raises:
            ValueError: If the unit is not valid or if the temperature is below absolute zero.
        """

        # saves unit and value as private attributes (_ = not meant to be changed)
        # float = 25 becomes 25.0
        self._unit = self._check_unit(unit)
        self._value = float(value)

        # temp must not be below absolute zero (0 K)
        if self.to_kelvin() < -TOLERANCE:
            raise ValueError("Temperature below absolute zero.")


    def _check_unit(self, unit: str) -> str:
        """Check that the unit is valid and return it in upper case."""

        # unit must be a string, and must be one of the valid units
        if not isinstance(unit, str) or unit.upper() not in VALID_UNITS:
            raise ValueError(f"Invalid unit {unit!r}. Valid units are {VALID_UNITS}.")

        # make unit case-insensitive
        return unit.upper()


    # 2. TOLERANCE

    def _is_close(self, a: float, b: float) -> bool:
        """Check if two values/floats are close enough to be considered equal."""
        return abs(a - b) <= TOLERANCE


    # 3. READ-ONLY PROPERTIES

    # @property lets us read temp.value and temp.unit,
    # but there is no setter, so temp.value = 5 gives an AttributeError

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit


    # 4. TEMPERATURE CONVERSIONS

    # one formula for each unit
    def to_celsius(self) -> float:
        """Convert the temperature to Celsius."""
        if self.unit == "F":
            return (self.value - 32) * 5 / 9
        if self.unit == "K":
            return self.value - 273.15
        return self.value  # already celsius

    # if already fahrenheit: return as it is, else go via celsius
    def to_fahrenheit(self) -> float:
        """Convert the temperature to Fahrenheit."""
        if self.unit == "F":
            return self.value  # already fahrenheit
        return self.to_celsius() * 9 / 5 + 32  # via celsius

    # if already kelvin: return as it is, else go via celsius
    def to_kelvin(self) -> float:
        """Convert the temperature to Kelvin."""
        if self.unit == "K":
            return self.value  # already kelvin
        return self.to_celsius() + 273.15  # via celsius

    # makes a NEW Temperature in the target unit, the original is not changed
    # convert_to uses the same unit check as __init__, so it will raise ValueError for invalid units
    def convert_to(self, target_unit: str) -> Temperature:
        """Convert the temperature to the target unit and return a new Temperature instance."""
        target_unit = self._check_unit(target_unit)

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        if target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        return Temperature(self.to_kelvin(), "K")


    # 5. STRING REPRESENTATIONS

    # for programmers: shows how the object was made, used by repr() and in lists
    def __repr__(self) -> str:
        """Return an unambiguous string representation of the Temperature."""
        return f"Temperature({self.value!r}, {self.unit!r})"

    # for people: two decimals and a unit sign, used by print() and str()
    def __str__(self) -> str:
        """Return a human-readable string representation of the Temperature."""
        if self.unit == "K":
            return f"{self.value:.2f} K"  # kelvin is written without °
        return f"{self.value:.2f} °{self.unit}"


    # 6. COMPARISON METHODS

    # all comparisons are done in kelvin, so different units can be compared
    # NotImplemented is returned if other is not a Temperature,
    # then python decides (== gives False, < gives TypeError)

    # ==  equal within the tolerance
    def __eq__(self, other: object) -> bool:
        """Check if two Temperature instances are equal."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._is_close(self.to_kelvin(), other.to_kelvin())

    # !=  the opposite of ==
    def __ne__(self, other: object) -> bool:
        """Check if two Temperature instances are not equal."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self == other

    # <  colder, and not equal within the tolerance
    def __lt__(self, other: object) -> bool:
        """Check if this Temperature instance is less than another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() < other.to_kelvin() and not self == other

    # <=  colder or equal (reuses < and ==)
    def __le__(self, other: object) -> bool:
        """Check if this Temperature instance is less than or equal to another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self < other or self == other

    # >  warmer, and not equal within the tolerance
    def __gt__(self, other: object) -> bool:
        """Check if this Temperature instance is greater than another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() > other.to_kelvin() and not self == other

    # >=  warmer or equal (reuses > and ==)
    def __ge__(self, other: object) -> bool:
        """Check if this Temperature instance is greater than or equal to another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self > other or self == other
