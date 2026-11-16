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
        if denominator <= 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

        if not isinstance(numerator, int):
            raise TypeError('Numerator must be an integer')

        if not isinstance(denominator, int):
            raise TypeError('Denominator must be an interger')

    def __str__(self) -> str:
        '''
        Return a human-readable string representation of the fraction

        Returns:
            str: The fraction in the format numerator/denominator
        '''
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self) -> str:
        """
        Return an official string representation of the fraction

        Returns:
            str: A string representation of the Fraction object
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other: 'Fraction') -> bool:
        '''
        Check if two fractions are equal

        Args:
            other (Fraction): The fraction to compare with

        Returns:
            bool: True if the fractions are equal, otherwise False
        '''
        return (
            self.numerator * other.denominator ==
            other.denominator * self.numerator
        )

    def __ne__(self, value):
        pass

    

    
