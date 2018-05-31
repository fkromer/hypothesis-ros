# -*- coding: utf-8 -*-
"""
Unit tests for the geometry_msgs strategies.
"""

from hypothesis import given
from hypothesis.strategies import just
from hypothesis_ros.messages.sensor_msgs import (
    region_of_interest
)
from hypothesis_ros.message_fields import (
    bool,
    uint32
)


@given(region_of_interest(x_offset=uint32(min_value=0, max_value=0),
                          y_offset=uint32(min_value=0, max_value=0),
                          height=uint32(min_value=0, max_value=0),
                          width=uint32(min_value=0, max_value=0),
                          do_rectify=just(True)
                         )
      )
def test_region_of_interest_accepts_customized_strategies(generated_values):
    """Exemplary customized point."""
    assert generated_values == (0, 0, 0, 0, True)
