# -*- coding: utf-8 -*-
"""
Unit tests for the generators of parameters.
"""

from hypothesis import given
from hypothesis_ros.parameters import date, DATE_MIN_VALUE, DATE_MAX_VALUE

@given(date())
def test_date_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Date."""
    assert generated_value >= DATE_MIN_VALUE
    assert generated_value <= DATE_MAX_VALUE