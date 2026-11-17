"""Temperature class with unit conversion and cross-unit comparison (Task 1)."""

from __future__ import annotations

import math

VALID_UNITS = ("C", "F", "K")
TOLERANCE = 1e-9  # Task 1.2: tolerance for floating-point comparisons


class Temperature:
    """A temperature with a value and unit."""

    def __init__(self, value: float, unit: str) -> None:
        """
        Initialise the Temperature.

        Args:
            value (float): The temperature value.
            unit (str): The unit of the temperature ("C", "F", or "K").

        Raises:
            ValueError: If the unit is not valid.
        """
        if unit not in VALID_UNITS:
            raise ValueError(f"Invalid unit '{unit}'. Valid units are {VALID_UNITS}.")
        self.value = value
        self.unit = unit
