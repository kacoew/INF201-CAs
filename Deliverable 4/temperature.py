"""Temperature class with unit conversion and cross-unit comparison (Task 1)."""

from __future__ import annotations

import math

VALID_UNITS = ("C", "F", "K")
TOLERANCE = 1e-9  # Task 1.2: tolerance for floating-point comparisons


class Temperature:

