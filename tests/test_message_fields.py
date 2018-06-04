# -*- coding: utf-8 -*-
"""
Unit tests for the message field strategies.
"""

from hypothesis import given
from hypothesis.errors import InvalidArgument
from pytest import raises

from hypothesis_ros.message_fields import (
    bool,
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
    string, STRING_MIN_SIZE, STRING_MAX_SIZE,
    time,
    duration,
    array,
)


@given(bool())
def test_bool_in_range_value_per_default(generated_value):
    """Verify default value range for bool."""
    assert generated_value in [False, True]


@given(int8())
def test_int8_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Int8."""
    assert generated_value >= INT8_MIN_VALUE
    assert generated_value <= INT8_MAX_VALUE


def test_int8_with_invalid_min_value_raises_exception():
    """Verifies validation of int8 min_value (lower limit)."""
    with raises(InvalidArgument):
        int8(min_value = INT8_MIN_VALUE - 1).example()


def test_int8_with_invalid_max_value_raises_exception():
    """Verifies validation of int8 max_value (upper limit)."""
    with raises(InvalidArgument):
        int8(max_value = INT8_MAX_VALUE + 1).example()


def test_int8_with_bigger_min_than_max_value_raises_exception():
    """Verifies validation of int8 min_value/max_value."""
    in_range_value = INT8_MAX_VALUE/2
    with raises(InvalidArgument):
        int8(min_value = in_range_value+1, max_value = in_range_value).example()


@given(uint8())
def test_uint8_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Uint8."""
    assert generated_value >= UINT8_MIN_VALUE
    assert generated_value <= UINT8_MAX_VALUE


def test_uint8_with_invalid_min_value_raises_exception():
    """Verifies validation of int8 min_value (lower limit)."""
    with raises(InvalidArgument):
        uint8(min_value = UINT8_MIN_VALUE - 1).example()


@given(int16())
def test_int16_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Int16."""
    assert generated_value >= INT16_MIN_VALUE
    assert generated_value <= INT16_MAX_VALUE


def test_int16_with_invalid_min_value_raises_exception():
    """Verifies validation of Int16 min_value (lower limit)."""
    with raises(InvalidArgument):
        int16(min_value = INT16_MIN_VALUE - 1).example()


@given(uint16())
def test_uint16_generates_expected_max_value_as_default(generated_value):
    """Verify default value range for Uint16."""
    assert generated_value >= UINT16_MIN_VALUE
    assert generated_value <= UINT16_MAX_VALUE


def test_uint16_with_invalid_min_value_raises_exception():
    """Verifies validation of Uint16 min_value (lower limit)."""
    with raises(InvalidArgument):
        uint16(min_value = UINT16_MIN_VALUE - 1).example()


@given(int32())
def test_int32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Int32."""
    assert generated_value >= INT32_MIN_VALUE
    assert generated_value <= INT32_MAX_VALUE


def test_int32_with_invalid_min_value_raises_exception():
    """Verifies validation of Int32 min_value (lower limit)."""
    with raises(InvalidArgument):
        int32(min_value = INT32_MIN_VALUE - 1).example()


@given(uint32())
def test_uint32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Uint32."""
    assert generated_value >= UINT32_MIN_VALUE
    assert generated_value <= UINT32_MAX_VALUE


def test_uint32_with_invalid_min_value_raises_exception():
    """Verifies validation of Uint32 min_value (lower limit)."""
    with raises(InvalidArgument):
        uint32(min_value = UINT32_MIN_VALUE - 1).example()


@given(int64())
def test_int64_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Int64."""
    assert generated_value >= INT64_MIN_VALUE
    assert generated_value <= INT64_MAX_VALUE


def test_int64_with_invalid_min_value_raises_exception():
    """Verifies validation of Int64 min_value (lower limit)."""
    with raises(InvalidArgument):
        int64(min_value = INT64_MIN_VALUE - 1).example()


@given(uint64())
def test_uint64_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Uint64."""
    assert generated_value >= UINT64_MIN_VALUE
    assert generated_value <= UINT64_MAX_VALUE


def test_uint64_with_invalid_min_value_raises_exception():
    """Verifies validation of Uint64 min_value (lower limit)."""
    with raises(InvalidArgument):
        uint64(min_value = UINT64_MIN_VALUE - 1).example()


@given(float32())
def test_float32_generates_in_range_value_per_default(generated_value):
    """Verify default value range for Float32."""
    assert generated_value >= FLOAT32_MIN_VALUE
    assert generated_value <= FLOAT32_MAX_VALUE


# def test_float32_with_invalid_min_value_raises_exception():
#     """Verifies validation of Float32 min_value (lower limit)."""
#     with raises(InvalidArgument):
#         float32(min_value = FLOAT32_MIN_VALUE - 0.1).example()


@given(float64())
def test_float64_generates_expected_min_value_as_default(generated_value):
    """Verify default min. generated value for Float64."""
    assert generated_value >= FLOAT64_MIN_VALUE
    assert generated_value <= FLOAT64_MAX_VALUE


# def test_float64_with_invalid_min_value_raises_exception():
#     """Verifies validation of Float64 min_value (lower limit)."""
#     with raises(InvalidArgument):
#         float64(min_value = FLOAT64_MIN_VALUE - 0.1).example()


@given(string())
def test_string_generates_in_range_size_per_default(generated_value):
    """Verify default generated string size."""
    assert len(generated_value) >= STRING_MIN_SIZE
    assert len(generated_value) <= STRING_MAX_SIZE


def test_string_with_bigger_min_than_max_size_raises_exception():
    """Verifies validation of String min_value/max_value."""
    with raises(InvalidArgument):
        string(min_size=STRING_MIN_SIZE+1, max_size=STRING_MIN_SIZE).example()


@given(time())
def test_time_generates_in_range_values_per_default(generated_value):
    """Verfiy default generated value range."""
    secs = generated_value.secs
    nsecs = generated_value.nsecs
    assert secs >= UINT32_MIN_VALUE
    assert secs <= UINT32_MAX_VALUE
    assert nsecs >= UINT32_MIN_VALUE
    assert nsecs <= UINT32_MAX_VALUE

@given(duration())
def test_duration_generates_in_range_values_per_default(generated_value):
    """Verfiy default generated value range."""
    secs = generated_value.secs
    nsecs = generated_value.nsecs
    assert secs >= INT32_MIN_VALUE
    assert secs <= INT32_MAX_VALUE
    assert nsecs >= INT32_MIN_VALUE
    assert nsecs <= INT32_MAX_VALUE

ARRAY_ELEMENT_COUNT = 5
ARRAY_ELEMENT_MIN_VALUE = 1
ARRAY_ELEMENT_MAX_VALUE = 3
@given(array(elements=int8(min_value=ARRAY_ELEMENT_MIN_VALUE, max_value=ARRAY_ELEMENT_MAX_VALUE),
             min_size=ARRAY_ELEMENT_COUNT,
             max_size=ARRAY_ELEMENT_COUNT
            )
      )
def test_fixed_length_array_element_values_customizable(generated_array):
    """Exemplary customized fixed length array."""
    assert len(generated_array) == ARRAY_ELEMENT_COUNT
    for element in generated_array:
        assert element >= ARRAY_ELEMENT_MIN_VALUE
        assert element <= ARRAY_ELEMENT_MAX_VALUE

ARRAY_MIN_LENGHT = 1
ARRAY_MAX_LENGHT = 5
ARRAY_ELEMENT_MIN_VALUE = 1
ARRAY_ELEMENT_MAX_VALUE = 3
@given(array(elements=int8(min_value=ARRAY_ELEMENT_MIN_VALUE, max_value=ARRAY_ELEMENT_MAX_VALUE),
             min_size=ARRAY_MIN_LENGHT,
             max_size=ARRAY_MAX_LENGHT
            )
      )
def test_variable_length_array_element_values_customizable(generated_array):
    """Exemplary customized variable length array."""
    assert len(generated_array) >= ARRAY_MIN_LENGHT
    assert len(generated_array) <= ARRAY_MAX_LENGHT
    for element in generated_array:
        assert element >= ARRAY_ELEMENT_MIN_VALUE
        assert element <= ARRAY_ELEMENT_MAX_VALUE
