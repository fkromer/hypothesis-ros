#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for ROS builtin message field types. The
strategies generate and shrink failed examples. They implement the generic
message field types which are usable in both, ROS1 and ROS2
(`ROS1 message field types`_, `ROS2 message field types`_).

.. _ROS1 message field types:
   http://wiki.ros.org/msg#Fields

.. _ROS2 message field types:
   https://github.com/ros2/ros2/wiki/About-ROS-Interfaces#211-field-types

"""

import datetime
from hypothesis.strategies import (
    binary,
    booleans,
    datetimes,
    defines_strategy,
    floats,
    integers
)

INT8_MIN_VALUE = -1 * (2 ** 7)
"""int: Minimal Int8 value."""
INT8_MAX_VALUE = (2 ** 7) - 1
"""int: Maximal Int8 value."""

UINT8_MIN_VALUE = 0
"""int: Minimal UInt8 value."""
UINT8_MAX_VALUE = (2 ** 8) - 1
"""int: Maximal UInt8 value."""

INT16_MIN_VALUE = -1 * (2 ** 15)
"""int: Minimal Int16 value."""
INT16_MAX_VALUE = (2 ** 15) - 1
"""int: Maximal Int16 value."""

UINT16_MIN_VALUE = 0
"""int: Minimal UInt16 value."""
UINT16_MAX_VALUE = (2 ** 16) - 1
"""int: Maximal UInt16 value."""

INT32_MIN_VALUE = -1 * (2 ** 31)
"""int: Minimal Int32 value."""
INT32_MAX_VALUE = (2 ** 31) - 1
"""int: Maximal Int32 value."""

UINT32_MIN_VALUE = 0
"""int: Minimal UInt32 value."""
UINT32_MAX_VALUE = (2 ** 32) - 1
"""int: Maximal UInt32 value."""

INT64_MIN_VALUE = -1 * (2 ** 63)
"""long: Minimal Int64 value."""
INT64_MAX_VALUE = (2 ** 63) - 1
"""long: Maximal Int64 value."""

UINT64_MIN_VALUE = 0
"""long: Minimal UInt64 value."""
UINT64_MAX_VALUE = (2 ** 64) - 1
"""long: Maximal UInt64 value."""

FLOAT32_MIN_VALUE = -3.4e+38
"""float: Minimal Float32 value."""
FLOAT32_MAX_VALUE = +3.4e+38
"""float: Maximal Float32 value."""

FLOAT64_MIN_VALUE = -1.7E+308
"""float: Minimal Float32 value."""
FLOAT64_MAX_VALUE = +1.7E+308
"""float: Maximal Float32 value."""

DATE_MIN_VALUE = datetime.datetime(datetime.MINYEAR, 1, 1, 0, 0)
"""date: Minimal ISO8601 Date value (0001-01-01 00:00:00)."""
DATE_MAX_VALUE = datetime.datetime(datetime.MAXYEAR, 12, 31, 23, 59)
"""date: Maximal ISO8601 Date value (9999-12-31 23:59:00)."""

STRING_MIN_SIZE = 0
"""int: Minimal string size."""
STRING_MAX_SIZE = 1000
"""int: Maximal string size."""


@defines_strategy
def bool():  # pylint: disable=redefined-builtin
    """
    Generate value for ROS builtin message type "bool".

    Returns
    -------
    hypothesis.strategies.booleans()
        Strategy with preconfigured default values.

    """
    return booleans()


@defines_strategy
def int8(min_value=INT8_MIN_VALUE, max_value=INT8_MAX_VALUE):
    """
    Generate value for ROS builtin message type "int8".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def uint8(min_value=UINT8_MIN_VALUE, max_value=UINT8_MAX_VALUE):
    """
    Generate value for ROS builtin message type "uint8".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def int16(min_value=INT16_MIN_VALUE, max_value=INT16_MAX_VALUE):
    """
    Generate value for ROS builtin message type "int16".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def uint16(min_value=UINT16_MIN_VALUE, max_value=UINT16_MAX_VALUE):
    """
    Generate value for ROS builtin message type "uint16".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def int32(min_value=INT32_MIN_VALUE, max_value=INT32_MAX_VALUE):
    """
    Generate value for ROS builtin message type "int32".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def uint32(min_value=UINT32_MIN_VALUE, max_value=UINT32_MAX_VALUE):
    """
    Generate value for ROS builtin message type "uint32".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def int64(min_value=INT64_MIN_VALUE, max_value=INT64_MAX_VALUE):
    """
    Generate value for ROS builtin message type "int64".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def uint64(min_value=UINT64_MIN_VALUE, max_value=UINT64_MAX_VALUE):
    """
    Generate value for ROS builtin message type "uint64".

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return integers(min_value, max_value)


@defines_strategy
def float32(min_value=FLOAT32_MIN_VALUE, max_value=FLOAT32_MAX_VALUE,
            allow_nan=False, allow_infinity=False):
    """
    Generate value for ROS builtin message type "float32".

    TODO: Map Hypothesis values to YAML [.inf, -.Inf, .NAN].
          http://www.yaml.org/refcard.html

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.
    allow_nan : boolean
        Generate "not a number"? (Default: false)
    allow_infinity : boolean
        Generate "not a number"? (Default: false)

    Returns
    -------
    hypothesis.strategies.floats()
        Strategy with preconfigured default values.

    """
    return floats(min_value, max_value, allow_nan, allow_infinity)


@defines_strategy
def float64(min_value=FLOAT64_MIN_VALUE, max_value=FLOAT64_MAX_VALUE,
            allow_nan=False, allow_infinity=False):
    """
    Generate value for ROS builtin message type "float64".

    TODO: Map Hypothesis values to YAML [.inf, -.Inf, .NAN].
          http://www.yaml.org/refcard.html

    Parameters
    ----------
    min_value : int
        Minimal value to generate.
    max_value : int
        Maximal value to generate.
    allow_nan : boolean
        Generate "not a number"? (Default: false)
    allow_infinity : boolean
        Generate "not a number"? (Default: false)

    Returns
    -------
    hypothesis.strategies.floats()
        Strategy with preconfigured default values.

    """
    return floats(min_value, max_value, allow_nan, allow_infinity)


@defines_strategy
def date(min_value=DATE_MIN_VALUE, max_value=DATE_MAX_VALUE):
    """
    Generate value for ROS builtin message type "date".

    Parameters
    ----------
    min_value : datetime.datetime
        Minimal value to generate.
    max_value : datetime.datetime
        Maximal value to generate.

    Returns
    -------
    hypothesis.strategies.datetimes()
        Strategy with values taken from datetime library.

    """
    return datetimes(min_value, max_value)

@defines_strategy
def string(min_size=STRING_MIN_SIZE, max_size=STRING_MAX_SIZE):
    """
    Generate value for ROS builtin message type "string".

    Parameters
    ----------
    min_size : int
        Minimal size to generate.
    max_size : int
        Maximal size to generate.

    Returns
    -------
    hypothesis.strategies.binary()
        Strategy with preconfigured default values.

    """
    # average_size parameter is deprecated
    return binary(min_size=min_size, max_size=max_size)
