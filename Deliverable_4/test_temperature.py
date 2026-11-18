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

"""Pytest tests for the Temperature class (Task 1).

Run with:  python -m pytest -v test_temperature.py
"""

import pytest

from temperature import Temperature

def test_initialization():
    """Test initialization with valid units and case insensitivity."""
    temp_c = Temperature(25, "C")
    temp_f = Temperature(77, "f")
    temp_k = Temperature(298.15, "K")

    assert temp_c.value == 25
    assert temp_c.unit == "C"
    assert temp_f.value == 77
    assert temp_f.unit == "F"
    assert temp_k.value == 298.15
    assert temp_k.unit == "K"

def test_invalid_unit():
    """Test that invalid unit strings raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(25, "X")    

def test_below_absolute_zero():
    """Test that temperatures below absolute zero raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(-274, "C")
    with pytest.raises(ValueError):
        Temperature(-460, "F")
    with pytest.raises(ValueError):
        Temperature(-1, "K")    

def test_conversion_accuracy():
    """Test conversion accuracy across reference points."""
    # Absolute zero
    abs_zero_c = Temperature(-273.15, "C")
    abs_zero_f = Temperature(-459.67, "F")
    abs_zero_k = Temperature(0, "K")

    assert abs(abs_zero_c.to_fahrenheit() + 459.67) < 1e-2
    assert abs(abs_zero_c.to_kelvin()) < 1e-2
    assert abs(abs_zero_f.to_celsius() + 273.15) < 1e-2
    assert abs(abs_zero_f.to_kelvin()) < 1e-2
    assert abs(abs_zero_k.to_celsius() + 273.15) < 1e-2
    assert abs(abs_zero_k.to_fahrenheit() + 459.67) < 1e-2

def test_round_trip_conversion():
    """Test that round-trip conversions reproduce the original Temperature."""
    original_temp = Temperature(25, "C")
    converted_temp = Temperature(original_temp.to_fahrenheit(), "F")
    round_trip_temp = Temperature(converted_temp.to_kelvin(), "K")

    assert abs(original_temp.value - round_trip_temp.to_celsius()) < 1e-2   

def test_cross_unit_comparisons():
    """Test equality and ordering across mixed units."""
    temp1 = Temperature(0, "C")
    temp2 = Temperature(32, "F")
    temp3 = Temperature(273.15, "K")

    assert temp1 == temp2
    assert temp1 == temp3
    assert temp2 == temp3

    temp4 = Temperature(100, "C")
    assert temp4 > temp1
    assert temp4 >= temp2
    assert not (temp4 < temp3)

def test_formatting():
    """Test the string and repr formatting of Temperature."""
    temp = Temperature(25, "C")
    assert str(temp) == "25.00 °C"
    assert repr(temp) == "Temperature(25, 'C')" 

def test_read_only_behavior():
    """Test that the value and unit attributes are read-only."""
    temp = Temperature(25, "C")
    with pytest.raises(AttributeError):
        temp.value = 30
    with pytest.raises(AttributeError):
        temp.unit = "F"

def test_case_insensitivity():
    """Test that the unit is case-insensitive."""
    temp_lower = Temperature(25, "c")
    temp_upper = Temperature(25, "C")
    assert temp_lower.unit == temp_upper.unit

def


