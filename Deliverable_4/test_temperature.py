"""
INF201 - Deliverable 4 - test_temperature.py
Task 1: Temperature Class Tests

Tests:
    1. Initialization: Default unit, case-insensitive units, and read-only behavior.
    2. Validation: Invalid unit strings and temperatures below absolute zero in "C", "F", and "K".
    3. Conversions: Test conversion accuracy across the five reference points.
    4. Round-trip conversions: Converting "C" -> "F" -> "K" -> "C" reproduces the original Temperature.
    5. Cross-unit comparisons: Equality and ordering (<, <=, >, >=) across mixed units.
    6. Formatting: Outputs of `str()` and `repr()`

Run with:
    python -m pytest test_temperature.py -v
"""


# IMPORTS

# pytest runs the tests, Temperature is the class we test
import pytest

from temperature import Temperature


# CONSTANTS

# reference points from the task: (celsius, fahrenheit, kelvin)
# used by the conversion test, so the numbers are only written once
REFERENCE_POINTS = [
    (-273.15, -459.67, 0.0),   # absolute zero
    (-40.0, -40.0, 233.15),    # celsius-fahrenheit crossover
    (0.0, 32.0, 273.15),       # freezing point of water
    (37.0, 98.6, 310.15),      # human body temperature
    (100.0, 212.0, 373.15),    # boiling point of water
]


# 1. INITIALIZATION

# no unit given -> celsius
def test_default_unit():
    """Test that Celsius is the default unit."""

    assert Temperature(25).unit == "C"


# parametrize runs the same test once for each unit in the list
# small letters should be saved as capital letters
@pytest.mark.parametrize("unit", ["c", "f", "k", "C", "F", "K"])
def test_case_insensitivity(unit):
    """Test that temperature units are case-insensitive."""

    assert Temperature(300, unit).unit == unit.upper()


# pytest.raises checks that the code inside gives the expected error
# changing value or unit should give an AttributeError
def test_read_only_behavior():
    """Test that value and unit cannot be modified."""

    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"


# 2. VALIDATION

# wrong text and wrong types (5, None) should both give ValueError
@pytest.mark.parametrize("unit", ["X", "Celsius", "", 5, None])
def test_invalid_unit(unit):
    """Test that invalid units raise ValueError."""

    with pytest.raises(ValueError):
        Temperature(25, unit)


# one value just below absolute zero in each unit
@pytest.mark.parametrize("value, unit", [(-273.16, "C"), (-459.68, "F"), (-0.01, "K")])
def test_below_absolute_zero(value, unit):
    """Test that temperatures below absolute zero are rejected."""

    # just below the limit, so a small bug is caught
    with pytest.raises(ValueError):
        Temperature(value, unit)


# absolute zero itself is the limit, so it must be allowed
def test_absolute_zero_boundaries():
    """Test that absolute zero itself is valid."""

    # no error should be raised
    Temperature(-273.15, "C")
    Temperature(-459.67, "F")
    Temperature(0, "K")


# convert_to uses the same unit check as __init__
def test_invalid_target_unit():
    """Test that convert_to rejects invalid target units."""

    with pytest.raises(ValueError):
        Temperature(25).convert_to("X")


# 3. TEMPERATURE CONVERSIONS

# runs once for each of the five reference points
# pytest.approx allows tiny rounding errors in floats
@pytest.mark.parametrize("celsius, fahrenheit, kelvin", REFERENCE_POINTS)
def test_conversion_accuracy(celsius, fahrenheit, kelvin):
    """Test conversions at five reference temperatures."""

    # start in each unit, and check all three conversions
    for temp in [Temperature(celsius, "C"), Temperature(fahrenheit, "F"), Temperature(kelvin, "K")]:
        assert temp.to_celsius() == pytest.approx(celsius)
        assert temp.to_fahrenheit() == pytest.approx(fahrenheit)
        assert temp.to_kelvin() == pytest.approx(kelvin)


# convert_to should give a new object with the right unit and value
def test_convert_to():
    """Test conversion to a new Temperature instance."""

    temp = Temperature(25, "C")
    converted = temp.convert_to("f")  # lowercase on purpose

    assert converted.unit == "F"
    assert converted.value == pytest.approx(77)

    # original object must remain unchanged
    assert temp.unit == "C"
    assert temp.value == 25


# 4. ROUND-TRIP CONVERSIONS

# converting through all three units should give back the same temperature
@pytest.mark.parametrize("value", [-40.0, 0.0, 25.0, 37.0, 100.0])
def test_round_trip_conversion(value):
    """Test C -> F -> K -> C."""

    original = Temperature(value, "C")
    converted = original.convert_to("F").convert_to("K").convert_to("C")

    assert converted == original


# 5. CROSS-UNIT COMPARISONS

# the same temperature in different units should be equal
def test_equal_temperatures():
    """Test equality and inequality across different units."""

    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") == Temperature(273.15, "K")
    assert Temperature(0, "C") != Temperature(100, "C")


# colder is smaller, warmer is bigger, even when the units are different
def test_ordering():
    """Test the <, <=, > and >= operators across units."""

    assert Temperature(0, "C") < Temperature(100, "F")
    assert Temperature(100, "C") > Temperature(273.15, "K")
    assert Temperature(0, "C") <= Temperature(32, "F")     # equal also counts
    assert Temperature(100, "C") >= Temperature(212, "F")  # equal also counts


# a difference smaller than 1e-9 counts as equal, a bigger one does not
def test_floating_point_tolerance():
    """Test equality within and outside the tolerance."""

    assert Temperature(25) == Temperature(25 + 1e-10)
    assert Temperature(25) != Temperature(25 + 1e-7)


# we call each method directly, because that is where NotImplemented is visible
def test_comparison_with_other_type():
    """Test that non-Temperature comparisons return NotImplemented."""

    temp = Temperature(25, "C")

    assert temp.__eq__(25) is NotImplemented
    assert temp.__ne__(25) is NotImplemented
    assert temp.__lt__(25) is NotImplemented
    assert temp.__le__(25) is NotImplemented
    assert temp.__gt__(25) is NotImplemented
    assert temp.__ge__(25) is NotImplemented


# 6. STRING FORMATTING

# str() is what print() shows: two decimals and the unit
def test_str():
    """Test human-readable temperature formatting."""

    assert str(Temperature(25, "C")) == "25.00 °C"
    assert str(Temperature(98.6, "F")) == "98.60 °F"
    assert str(Temperature(300, "K")) == "300.00 K"  # kelvin without °


# repr() shows how the object was made, with 25.0 (float)
def test_repr():
    """Test unambiguous object representation."""

    assert repr(Temperature(25, "C")) == "Temperature(25.0, 'C')"
