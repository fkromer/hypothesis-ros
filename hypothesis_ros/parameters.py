# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS parameter types`_.

.. _ROS parameter types:
   http://wiki.ros.org/Parameter%20Server#Parameter_Types

"""

import datetime
from hypothesis.strategies import (
    datetimes,
    defines_strategy,
    lists,
    floats
)
from hypothesis_ros.message_fields import int32, string, bool, array as list

__all__ = ['int32', 'string', 'bool', 'list']
"""Make strategies from hypothesis_ros.message_fields available in this module."""

DATE_MIN_VALUE = datetime.datetime(datetime.MINYEAR, 1, 1, 0, 0)
"""date: Minimal ISO8601 Date value (0001-01-01 00:00:00)."""
DATE_MAX_VALUE = datetime.datetime(datetime.MAXYEAR, 12, 31, 23, 59)
"""date: Maximal ISO8601 Date value (9999-12-31 23:59:00)."""

DOUBLE_MIN_VALUE = -3.4028235e+38
"""float: Minimal Double value."""
DOUBLE_MAX_VALUE = +3.4028235e+38
"""float: Maximal Double value."""


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
def double(min_value=DOUBLE_MIN_VALUE, max_value=DOUBLE_MAX_VALUE,
            allow_nan=False, allow_infinity=False):
    """
    Generate value for ROS paramter type "double".

    Parameters
    ----------
    min_value : float
        Minimal value to generate.
    max_value : float
        Maximal value to generate.
    allow_nan : boolean
        Generate "not a number"? (Default: false)
    allow_infinity : boolean
        Generate "infinity"? (Default: false)

    Returns
    -------
    hypothesis.strategies.floats()
        Strategy with preconfigured default values.

    """
    return floats(min_value, max_value, allow_nan, allow_infinity)
