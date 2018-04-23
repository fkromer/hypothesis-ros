# -*- coding: utf-8 -*-
"""
Unit tests for the generators of the built-in message field datatypes.
"""

from rospbt.ros1.generators import builtin_msg_field_types


def test_float32_generates_expected_min_value_as_default():
    """Verify default min. generated value for Float32."""
    expected_min_value = builtin_msg_field_types.FLOAT32_MIN_VALUE
    generated_value = builtin_msg_field_types.float32(
        min_value=builtin_msg_field_types.FLOAT32_MIN_VALUE,
        max_value=builtin_msg_field_types.FLOAT32_MIN_VALUE).example()
    assert generated_value == expected_min_value


def test_float32_generates_expected_max_value_as_default():
    """Verify default max. generated value for Float32."""
    expected_min_value = builtin_msg_field_types.FLOAT32_MAX_VALUE
    generated_value = builtin_msg_field_types.float32(
        min_value=builtin_msg_field_types.FLOAT32_MAX_VALUE,
        max_value=builtin_msg_field_types.FLOAT32_MAX_VALUE).example()
    assert generated_value == expected_min_value


def test_float64_generates_expected_min_value_as_default():
    """Verify default min. generated value for Float64."""
    expected_min_value = builtin_msg_field_types.FLOAT64_MIN_VALUE
    generated_value = builtin_msg_field_types.float64(
        min_value=builtin_msg_field_types.FLOAT64_MIN_VALUE,
        max_value=builtin_msg_field_types.FLOAT64_MIN_VALUE).example()
    assert generated_value == expected_min_value


def test_float64_generates_expected_max_value_as_default():
    """Verify default max. generated value for Float64."""
    expected_min_value = builtin_msg_field_types.FLOAT64_MAX_VALUE
    generated_value = builtin_msg_field_types.float64(
        min_value=builtin_msg_field_types.FLOAT64_MAX_VALUE,
        max_value=builtin_msg_field_types.FLOAT64_MAX_VALUE).example()
    assert generated_value == expected_min_value
