# -*- coding: utf-8 -*-
"""
Unit tests for the generators of the built-in message field datatypes.
"""

import datetime
from hypothesis import given
from hypothesis_ros.ros1 import builtin_msg_field_types


@given(builtin_msg_field_types.int8())
def test_int8_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Int8."""
    assert generated_value >= builtin_msg_field_types.INT8_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.INT8_MAX_VALUE


@given(builtin_msg_field_types.uint8())
def test_uint8_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Uint8."""
    assert generated_value >= builtin_msg_field_types.UINT8_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.UINT8_MAX_VALUE


@given(builtin_msg_field_types.int16())
def test_int16_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Int16."""
    assert generated_value >= builtin_msg_field_types.INT16_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.INT16_MAX_VALUE


@given(builtin_msg_field_types.uint16())
def test_uint16_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Uint16."""
    assert generated_value >= builtin_msg_field_types.UINT16_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.UINT16_MAX_VALUE


@given(builtin_msg_field_types.int32())
def test_int32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Int32."""
    assert generated_value >= builtin_msg_field_types.INT32_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.INT32_MAX_VALUE


@given(builtin_msg_field_types.uint32())
def test_uint32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Uint32."""
    assert generated_value >= builtin_msg_field_types.UINT32_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.UINT32_MAX_VALUE


@given(builtin_msg_field_types.int64())
def test_int64_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Int64."""
    assert generated_value >= builtin_msg_field_types.INT64_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.INT64_MAX_VALUE


@given(builtin_msg_field_types.uint64())
def test_uint64_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Uint64."""
    assert generated_value >= builtin_msg_field_types.UINT64_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.UINT64_MAX_VALUE


@given(builtin_msg_field_types.float32())
def test_float32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Float32."""
    assert generated_value >= builtin_msg_field_types.FLOAT32_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.FLOAT32_MAX_VALUE


@given(builtin_msg_field_types.float64())
def test_float64_generates_expected_min_value_as_default(generated_value):
    """Verify default min. generated value for Float64."""
    assert generated_value >= builtin_msg_field_types.FLOAT64_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.FLOAT64_MAX_VALUE

@given(builtin_msg_field_types.date())
def test_date_generates_in_range_value_per_default(generated_value):
    """Verify default min. generated value for Date."""
    assert generated_value >= builtin_msg_field_types.DATE_MIN_VALUE
    assert generated_value <= builtin_msg_field_types.DATE_MAX_VALUE
