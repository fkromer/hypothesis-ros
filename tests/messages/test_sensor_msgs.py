# -*- coding: utf-8 -*-
"""
Unit tests for the geometry_msgs strategies.
"""

from hypothesis import given
from hypothesis.strategies import just
from hypothesis_ros.messages.sensor_msgs import (
    imu,
    region_of_interest
)
from hypothesis_ros.messages.geometry_msgs import vector3, quaternion
from hypothesis_ros.messages.std_msgs import header
from hypothesis_ros.message_fields import (
    array,
    bool,
    float32,
    float64,
    time,
    uint32,
)


@given(region_of_interest(x_offset=uint32(min_value=0, max_value=0),
                          y_offset=uint32(min_value=0, max_value=0),
                          height=uint32(min_value=0, max_value=0),
                          width=uint32(min_value=0, max_value=0),
                          do_rectify=just(True)
                         )
      )
def test_region_of_interest_accepts_customized_strategies(generated_values):
    """Exemplary customized region_of_interest message fields."""
    assert generated_values == (0, 0, 0, 0, True)


@given(imu(header(seq=uint32(min_value=0, max_value=0),
                  stamp=time(secs=uint32(min_value=0, max_value=0),
                             nsecs=uint32(min_value=0, max_value=0)
                            ),
                  frame_id=float64(min_value=0.0, max_value=0.0)
                 ),
           quaternion(x=float64(min_value=0.0, max_value=0.0),
                      y=float64(min_value=0.0, max_value=0.0),
                      z=float64(min_value=0.0, max_value=0.0),
                      w=float64(min_value=0.0, max_value=0.0)
                     ),
           array(elements=float64(min_value=0.0, max_value=0.0), min_size=9, max_size=9),
           vector3(x=float64(min_value=0.0, max_value=0.0),
                   y=float64(min_value=0.0, max_value=0.0),
                   z=float64(min_value=0.0, max_value=0.0)
                  ),
           array(elements=float64(min_value=0.0, max_value=0.0), min_size=9, max_size=9),
           vector3(x=float64(min_value=0.0, max_value=0.0),
                   y=float64(min_value=0.0, max_value=0.0),
                   z=float64(min_value=0.0, max_value=0.0)
                  ),
           array(elements=float64(min_value=0.0, max_value=0.0), min_size=9, max_size=9)
          )
      )
def test_imu_accepts_customized_strategies(generated_values):
    """Exemplary customized imu message fields."""
    assert generated_values == ((0, (0, 0), 0.0),
                                (0.0, 0.0, 0.0, 0.0),
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                (0.0, 0.0, 0.0),
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                (0.0, 0.0, 0.0),
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
