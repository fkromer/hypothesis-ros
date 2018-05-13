# -*- coding: utf-8 -*-
"""
Unit tests for the generators of parameters.
"""

from hypothesis import given
from hypothesis_ros.parameters import (
    bool,
    int32,
    string,
    date, DATE_MIN_VALUE, DATE_MAX_VALUE
)


@given(bool())
def test_message_field_bool_works_as_parameter(generated_value):
    """Verify message field strategy bool is executable via parameter module."""
    assert generated_value in [False, True]


@given(int32())
def test_message_field_int32_works_as_parameter(generated_value):
    """Verify message field int32 strategy is executable via parameter module."""
    assert isinstance(generated_value, int)


@given(string())
def test_message_field_string_works_as_parameter(generated_value):
    """Verify message field strategy string is executable via parameter module."""
    assert isinstance(generated_value, basestring)


@given(date())
def test_date_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Date."""
    assert generated_value >= DATE_MIN_VALUE
    assert generated_value <= DATE_MAX_VALUE
