"""Tests for the Fraction class."""

import pytest
from fraction import Fraction


def test_fraction_creation():
    """Test creating a valid fraction."""
    f = Fraction(3, 4)

    assert f.numerator == 3
    assert f.denominator == 4


def test_zero_denominator():
    """Test that a denominator of zero raises ValueError."""
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_negative_denominator():
    """Test that a negative denominator raises ValueError."""
    with pytest.raises(ValueError):
        Fraction(1, -2)


def test_non_integer_numerator():
    """Test that a non-integer numerator raises TypeError."""
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


def test_non_integer_denominator():
    """Test that a non-integer denominator raises TypeError."""
    with pytest.raises(TypeError):
        Fraction(1, 2.5)


def test_string_representation():
    """Test the __str__ method."""
    assert str(Fraction(3, 4)) == "3/4"


def test_repr_representation():
    """Test the __repr__ method."""
    assert repr(Fraction(3, 4)) == "Fraction(3, 4)"


def test_equal():
    """Test equality comparison."""
    assert Fraction(1, 2) == Fraction(2, 4)


def test_not_equal():
    """Test inequality comparison."""
    assert Fraction(1, 2) != Fraction(3, 4)


def test_less_than():
    """Test less than comparison."""
    assert Fraction(1, 3) < Fraction(1, 2)


def test_less_than_or_equal():
    """Test less than or equal comparison."""
    assert Fraction(1, 2) <= Fraction(2, 4)


def test_greater_than():
    """Test greater than comparison."""
    assert Fraction(3, 4) > Fraction(1, 2)


def test_greater_than_or_equal():
    """Test greater than or equal comparison."""
    assert Fraction(3, 4) >= Fraction(3, 4)


def test_addition():
    """Test fraction addition."""
    result = Fraction(1, 2) + Fraction(1, 3)

    assert result == Fraction(5, 6)


def test_subtraction():
    """Test fraction subtraction."""
    result = Fraction(3, 4) - Fraction(1, 4)

    assert result == Fraction(8, 16)


def test_multiplication():
    """Test fraction multiplication."""
    result = Fraction(2, 3) * Fraction(3, 4)

    assert result == Fraction(6, 12)


def test_division():
    """Test fraction division."""
    result = Fraction(2, 3) / Fraction(4, 5)

    assert result == Fraction(10, 12)


def test_division_by_zero_fraction():
    """Test division by a zero fraction."""
    with pytest.raises(ValueError):
        Fraction(1, 2) / Fraction(0, 1)
