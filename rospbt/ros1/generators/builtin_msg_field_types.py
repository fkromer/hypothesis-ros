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

from hypothesis.strategies import booleans, floats, integers

INT8_MIN_VALUE = -128
"""int: Minimal Int8 value (−1 × 2^7)."""
INT8_MAX_VALUE = 127
"""int: Maximal Int8 value (2^7 - 1)."""

UINT8_MIN_VALUE = 0
"""int: Maximal UInt8 value."""
UINT8_MAX_VALUE = 255
"""int: Maximal UInt8 value (2^8 - 1)."""

INT16_MIN_VALUE = -32768
"""int: Minimal Int16 value (−1 × 2^15)."""
INT16_MAX_VALUE = 32767
"""int: Maximal Int16 value (2^15 − 1)."""

UINT16_MIN_VALUE = 0
"""int: Minimal UInt16 value."""
UINT16_MAX_VALUE = 65535
"""int: Maximal UInt16 value (2^16 − 1)."""

INT32_MIN_VALUE = -2147483648
"""int: Minimal Int32 value (−1 x 2^31)."""
INT32_MAX_VALUE = 2147483647
"""int: Maximal Int32 value (2^31 − 1)."""

UINT32_MIN_VALUE = 0
"""int: Minimal UInt32 value."""
UINT32_MAX_VALUE = 4294967295
"""int: Minimal Int32 value (2^32 − 1)."""

INT64_MIN_VALUE = -9223372036854775808
"""long: Minimal Int64 value (−1 x 2^63)."""
INT64_MAX_VALUE = 9223372036854775807
"""long: Maximal Int64 value (2^63 − 1)."""

UINT64_MIN_VALUE = 0
"""long: Minimal UInt64 value."""
UINT64_MAX_VALUE = 18446744073709551615
"""long: Maximal UInt64 value (2^64 − 1)."""


def bool():
    """
    Generates and shrinks values for ROS builtin message type "bool".

    Returns
    -------
    hypothesis.strategies.booleans()
        Strategy with preconfigured default values.
    """
    return booleans()


def int8(min_value=INT8_MIN_VALUE, max_value=INT8_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "int8".

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


def uint8(min_value=UINT8_MIN_VALUE, max_value=UINT8_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "uint8".

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


def int16(min_value=INT16_MIN_VALUE, max_value=INT16_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "int16".
        hypothesis strategy with preconfigured default values

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


def uint16(min_value=UINT16_MIN_VALUE, max_value=UINT16_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "uint16".

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


def int32(min_value=INT32_MIN_VALUE, max_value=INT32_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "int32".

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


def uint32(min_value=UINT32_MIN_VALUE, max_value=UINT32_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "uint32".

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


def int64(min_value=INT64_MIN_VALUE, max_value=INT64_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "int64".

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


def uint64(min_value=UINT64_MIN_VALUE, max_value=UINT64_MAX_VALUE):
    """
    Generates and shrinks values for ROS builtin message type "uint64".

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
