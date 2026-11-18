## Task 1: Temperatures

    # Create a `Temperature` class that supports Celsius ("C"), Fahrenheit ("F"), and Kelvin ("K"). This class should:
    # 1. Be initialised with a value and a unit (case-insensitive), and raise a `ValueError` if the unit is not one of "C", "F" or "K", or if the temperature is below absolute zero (0 K).
    # 2. Use a tolerance of 1e-9 for floating-point value comparisons
    # 3. Expose `value` and `unit` as read-only attributes
    # 4. Contain the following conversion methods:
    #     * `to_celsius(self) -> float`:
    #         * From Kelvin: $C = K - 273.15$
    #         * From Fahrenheit: $C = (F - 32) \times \frac{5}{9}$
    #     * `to_fahrenheit(self) -> float`:
    #         * From Celsius: $F = C \times \frac{9}{5} + 32$
    #         * From Kelvin: $F = (K - 273.15) \times \frac{9}{5} + 32$
    #     * `to_kelvin(self) -> float`:
    #         * From Celsius: $K = C + 273.15$
    #         * From Fahrenheit: $K = (F - 32) \times \frac{5}{9} + 273.15$
    # * `convert_to(self, target_unit: str) -> Temperature`:
    #         * Returns a new `Temperature` instance converted to `target_unit` (case-insensitive), raising `ValueError` if `target_unit` is invalid.
    # 5. Contain the following string representations:
    #     * `__repr__(self) -> str`: Returns an unambiguous representation, such as `Temperature(25.0, 'C')`.
    #     * `__str__(self) -> str`: Returns a human-readable string formatted to two decimal places, such as `25.00 °C`.
    # 6. Contain all six comparisons (==, !=, <, <=, >, >=) so temperatures can be compared across different units (`Temperature(0, "C") == Temperature(32, "F")`). Should return `NotImplemented` if a `Temperature` instance is compared to a non-Temperature instance.

    # Write a `test_temperature.py` script that imports the `Temperature` class and uses pytest for the following tests:
    # 1. Initialization: Default unit, case-insensitive units, and read-only behavior.
    # 2. Validation: Invalid unit strings and temperatures below absolute zero in "C", "F", and "K".
    # 3. Conversions: Test conversion accuracy across reference points:
    #     * Absolute zero ($-273.15^\circ\text{C} = -459.67^\circ\text{F} = 0\text{ K}$)
    #     * Celsius–Fahrenheit crossover ($-40^\circ\text{C} = -40^\circ\text{F} = 233.15\text{ K}$)
    #     * Freezing point of water ($0^\circ\text{C} = 32^\circ\text{F} = 273.15\text{ K}$)
    #     * Human body temperature ($37^\circ\text{C} = 98.6^\circ\text{F} = 310.15\text{ K}$)
    #     * Boiling point of water ($100^\circ\text{C} = 212^\circ\text{F} = 373.15\text{ K}$)
    # 4. Round-trip conversions: Converting "C" -> "F" -> "K" -> "C" reproduces the original Temperature.
    # 5. Cross-unit comparisons: Equality and ordering (<, <=, >, >=) across mixed units.
    # 6. Formatting: Outputs of `str()` and `repr()`

"""Temperature class with unit conversion and cross-unit comparison (Task 1)."""

# 1. IMPORTS

from __future__ import annotations

import math

# 2. CONSTANTS

VALID_UNITS = ("C", "F", "K")
TOLERANCE = 1e-9  # Task 1.2: tolerance for floating-point comparisons

ABSOLUTE_ZERO = {
    "C": -273.15,
    "F": -459.67,
    "K": 0
}

# 3. TEMPERATURE CLASS

class Temperature:
    """A temperature with a value and unit."""

    def __init__(self, value: float, unit: str) -> None:
        """
        Initialise Temperature.

        Args:
            value (float): The temperature value.
            unit (str): The unit of the temperature ("C", "F", or "K").

        Raises:
            ValueError: If the unit is not valid or if the temperature is below absolute zero.
        """

        # make unit case-insensitive
        unit = unit.upper()

        if unit not in VALID_UNITS:
            raise ValueError(f"Invalid unit '{unit}'. Valid units are {VALID_UNITS}.")
        self._value = value
        self.unit = unit

        #

        if value < ABSOLUTE_ZERO[unit]:
            raise ValueError(f"Temperature below absolute zero for unit '{unit}'.")

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    def to_celsius(self) -> float:
        """Convert the temperature to Celsius."""
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15

    def to_fahrenheit(self) -> float:
        """Convert the temperature to Fahrenheit."""
        if self.unit == "C":
            return self.value * 9 / 5 + 32
        elif self.unit == "F":
            return self.value
        elif self.unit == "K":
            return (self.value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """Convert the temperature to Kelvin."""
        if self.unit == "C":
            return self.value + 273.15
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9 + 273.15
        elif self.unit == "K":
            return self.value

    def convert_to(self, target_unit: str) -> Temperature:
        """Convert the temperature to the target unit and return a new Temperature instance."""
        target_unit = target_unit.upper()
        if target_unit not in VALID_UNITS:
            raise ValueError(f"Invalid target unit '{target_unit}'. Valid units are {VALID_UNITS}.")

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        elif target_unit == "K":
            return Temperature(self.to_kelvin(), "K")

    def __repr__(self) -> str:
        """Return an unambiguous string representation of the Temperature."""
        return f"Temperature({self.value}, '{self.unit}')"  

    def __str__(self) -> str:
        """Return a human-readable string representation of the Temperature."""
        return f"{self.value:.2f} °{self.unit}"

    #comparison methods
    def __eq__(self, other: object) -> bool:
        """Check if two Temperature instances are equal."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return math.isclose(self.to_kelvin(), other.to_kelvin(), abs_tol=TOLERANCE)   


