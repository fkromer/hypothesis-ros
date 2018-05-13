# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS parameter types`_.

.. _ROS1 message field types:
   http://wiki.ros.org/Parameter%20Server#Parameter_Types

"""

import datetime
from hypothesis.strategies import (
    datetimes,
    defines_strategy
)

DATE_MIN_VALUE = datetime.datetime(datetime.MINYEAR, 1, 1, 0, 0)
"""date: Minimal ISO8601 Date value (0001-01-01 00:00:00)."""
DATE_MAX_VALUE = datetime.datetime(datetime.MAXYEAR, 12, 31, 23, 59)
"""date: Maximal ISO8601 Date value (9999-12-31 23:59:00)."""

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
