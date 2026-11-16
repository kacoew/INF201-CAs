"""Fraction class with comparisons and arithmetic special methods (Task 2)."""

from __future__ import annotations

import math

class Fraction:
    """A fraction with a numerator and denominator."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initialise the Fraction.

        Args:
            numerator (int): The numerator.
            denominator (int): The denominator.

        Raises:
            ValueError: If the denominator is zero.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator