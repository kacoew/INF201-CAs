"""Fraction class with comparisons and arithmetic special methods (Task 2)."""

from __future__ import annotations
import math

class Fraction:
    """A fraction with a numerator and denominator"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initialise the Fraction.

        Args:
            numerator (int): The numerator
            denominator (int): The denominator

        Raises:
            ValueError: If the denominator is zero.
        """
        if denominator <= 0:
            raise ValueError("Denominator cannot be zero")
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
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other: "Fraction") -> bool:
        """
        Check if two fractions are not equal

        Args:
            other (Fraction): The fraction to compare with

        Returns:
            bool: True if the fractions are not equal, otherwise False
        """
        return not self.__eq__(other)

    def __lt__(self, other: "Fraction") -> bool:
        """
        Check if this fraction is less than another fraction

        Args:
            other (Fraction): The fraction to compare with

        Returns:
            bool: True if this fraction is less than the other fraction
        """
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: "Fraction") -> bool:
        """
        Check if this fraction is less than or equal to another fraction

        Args:
            other (Fraction): The fraction to compare with

        Returns:
            bool: True if this fraction is less than or equal to the other fraction
        """
        return self < other or self == other

    def __gt__(self, other: "Fraction") -> bool:
        """
        Check if this fraction is greater than another fraction

        Args:
            other (Fraction): The fraction to compare with

        Returns:
            bool: True if this fraction is greater than the other fraction
        """
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: "Fraction") -> bool:
        """
        Check if this fraction is greater than or equal to another fraction

        Args:
            other (Fraction): The fraction to compare with

        Returns:
            bool: True if this fraction is greater than or equal to the other fraction
        """
        return not self < other

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Add two fractions

        Args:
            other (Fraction): The fraction to add

        Returns:
            Fraction: The result of the addition
        """
        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Subtract one fraction from another

        Args:
            other (Fraction): The fraction to subtract

        Returns:
            Fraction: The result of the subtraction
        """
        numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )

        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Multiply two fractions

        Args:
            other (Fraction): The fraction to multiply by

        Returns:
            Fraction: The result of the multiplication
        """
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        Divide one fraction by another

        Args:
            other (Fraction): The divisor fraction

        Returns:
            Fraction: The result of the division

        Raises:
            ValueError: If attempting to divide by zero
        """
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")

        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )
