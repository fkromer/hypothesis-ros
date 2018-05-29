# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS parameter types`_.

.. _ROS1 message field types:
   http://wiki.ros.org/Parameter%20Server#Parameter_Types

"""

import datetime
from hypothesis.strategies import (
    datetimes,
    defines_strategy,
    lists
)
from hypothesis_ros.message_fields import bool as common_bool
from hypothesis_ros.message_fields import int32 as common_int32
from hypothesis_ros.message_fields import string as common_string
from hypothesis_ros.message_fields import (
    INT32_MIN_VALUE, INT32_MAX_VALUE,
    STRING_MIN_SIZE, STRING_MAX_SIZE
)


DATE_MIN_VALUE = datetime.datetime(datetime.MINYEAR, 1, 1, 0, 0)
"""date: Minimal ISO8601 Date value (0001-01-01 00:00:00)."""
DATE_MAX_VALUE = datetime.datetime(datetime.MAXYEAR, 12, 31, 23, 59)
"""date: Maximal ISO8601 Date value (9999-12-31 23:59:00)."""


def bool():
    """
    Generate value for ROS parameter type "bool".

    Returns
    -------
    hypothesis.strategies.booleans()
        Strategy with preconfigured default values.

    """
    return common_bool()


def int32(min_value=INT32_MIN_VALUE, max_value=INT32_MAX_VALUE):
    """
    Generate value for ROS parameter type "int32".

    Returns
    -------
    hypothesis.strategies.integers()
        Strategy with preconfigured default values.

    """
    return common_int32(min_value, max_value)


def string(min_size=STRING_MIN_SIZE, max_size=STRING_MAX_SIZE):
    """
    Generate value for ROS parameter "string".

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
    return common_string(min_size, max_size)


@defines_strategy
def date(min_value=DATE_MIN_VALUE, max_value=DATE_MAX_VALUE):
    """
    Generate value for ROS parameter type "date".

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
def list(elements=None, min_size=None, max_size=None, unique_by=None, unique=None):
    """
    Generate variable length list with ROS parameter types as elements.
    To generate a fixed length list define `min_size == max_size`.

    Parameters
    ----------
    elements: hypothesis_ros.parameters
        Strategies for types from hypothesis_ros.parameters.
    min_size: integer
        Minimal size of the list.
    max_size: integer
        Maximal size of the list.
    unique_by: function
        Function returning a hashable type when given a value from elements.
        The resulting list will satisfy `unique_by(result[i]) != unique_by(result[j])`.
    unique: function
        Function returning a hashable type. For comparison of directy object equality.

    Returns
    -------
    list
        A variable or fixed length list containing values drawn from elements with
        length in the interval [min_size, max_size] (no bounds in that direction
        if these are None).

    """
    return lists(elements=elements, min_size=min_size, max_size=max_size, unique_by=unique_by, unique=unique)