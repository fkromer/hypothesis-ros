# -*- coding: utf-8 -*-
"""
Unit tests for the message field strategies.
"""

from hypothesis import given
from hypothesis_ros.message_fields import (
    int8, INT8_MIN_VALUE, INT8_MAX_VALUE,
    uint8, UINT8_MIN_VALUE, UINT8_MAX_VALUE,
    int16, INT16_MIN_VALUE, INT16_MAX_VALUE,
    uint16, UINT16_MIN_VALUE, UINT16_MAX_VALUE,
    int32, INT32_MIN_VALUE, INT32_MAX_VALUE,
    uint32, UINT32_MIN_VALUE, UINT32_MAX_VALUE,
    int64, INT64_MIN_VALUE, INT64_MAX_VALUE,
    uint64, UINT64_MIN_VALUE, UINT64_MAX_VALUE,
    float32, FLOAT32_MIN_VALUE, FLOAT32_MAX_VALUE,
    float64, FLOAT64_MIN_VALUE, FLOAT64_MAX_VALUE,
    string, STRING_MIN_SIZE, STRING_MAX_SIZE
)


@given(int8())
def test_int8_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Int8."""
    assert generated_value >= INT8_MIN_VALUE
    assert generated_value <= INT8_MAX_VALUE


@given(uint8())
def test_uint8_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Uint8."""
    assert generated_value >= UINT8_MIN_VALUE
    assert generated_value <= UINT8_MAX_VALUE


@given(int16())
def test_int16_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Int16."""
    assert generated_value >= INT16_MIN_VALUE
    assert generated_value <= INT16_MAX_VALUE


@given(uint16())
def test_uint16_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Uint16."""
    assert generated_value >= UINT16_MIN_VALUE
    assert generated_value <= UINT16_MAX_VALUE


@given(int32())
def test_int32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Int32."""
    assert generated_value >= INT32_MIN_VALUE
    assert generated_value <= INT32_MAX_VALUE


@given(uint32())
def test_uint32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Uint32."""
    assert generated_value >= UINT32_MIN_VALUE
    assert generated_value <= UINT32_MAX_VALUE


@given(int64())
def test_int64_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Int64."""
    assert generated_value >= INT64_MIN_VALUE
    assert generated_value <= INT64_MAX_VALUE


@given(uint64())
def test_uint64_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Uint64."""
    assert generated_value >= UINT64_MIN_VALUE
    assert generated_value <= UINT64_MAX_VALUE


@given(float32())
def test_float32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Float32."""
    assert generated_value >= FLOAT32_MIN_VALUE
    assert generated_value <= FLOAT32_MAX_VALUE


@given(float64())
def test_float64_generates_expected_min_value_as_default(generated_value):
    """Verify default min. generated value for Float64."""
    assert generated_value >= FLOAT64_MIN_VALUE
    assert generated_value <= FLOAT64_MAX_VALUE


@given(string())
def test_string_generates_in_range_size_per_default(generated_value):
    """Verify default generated string size."""
    assert len(generated_value) >= STRING_MIN_SIZE
    assert len(generated_value) <= STRING_MAX_SIZE
