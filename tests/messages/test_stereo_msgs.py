# -*- coding: utf-8 -*-
"""
Unit tests for the stereo_msgs strategies.
"""

from hypothesis import given
from hypothesis.strategies import just

from hypothesis_ros.messages.stereo_msgs import disparity_image
from hypothesis_ros.messages.geometry_msgs import transform_stamped
from hypothesis_ros.messages.sensor_msgs import image, region_of_interest
from hypothesis_ros.messages.std_msgs import header
from hypothesis_ros.message_fields import (
    array,
    float32,
    uint8,
    uint32,
    time
)


@given(disparity_image(header(seq=uint32(min_value=0.0, max_value=0.0),
              stamp=time(
                        secs=uint32(min_value=0.0, max_value=0.0),
                        nsecs=uint32(min_value=0.0, max_value=0.0)
                    ),
              frame_id=just('some_tf_frame_name')
             ),
       image(header(seq=uint32(min_value=0, max_value=0),
                    stamp=time(secs=uint32(min_value=0, max_value=0),
                               nsecs=uint32(min_value=0, max_value=0)
                              ),
                    frame_id=just('some_tf_frame_name')
                   ),
             uint32(min_value=2, max_value=2),
             uint32(min_value=2, max_value=2),
             just('rgb8'),
             uint32(min_value=0, max_value=0),
             uint8(min_value=0, max_value=0),
             array(elements=uint8(min_value=0, max_value=0), min_size=4, max_size=4)
            ),
       float32(min_value=0.0, max_value=0.0),
       float32(min_value=0.0, max_value=0.0),
       region_of_interest(x_offset=uint32(min_value=0, max_value=0),
                          y_offset=uint32(min_value=0, max_value=0),
                          height=uint32(min_value=0, max_value=0),
                          width=uint32(min_value=0, max_value=0),
                          do_rectify=just(True)
                         ),
       float32(min_value=0.0, max_value=0.0),
       float32(min_value=0.0, max_value=0.0),
       float32(min_value=0.0, max_value=0.0)
      )
)
def test_disparity_image_accepts_customized_strategies(generated_value):
    """Exemplary customized disparity_image."""
    assert generated_value == ((0, (0, 0), 'some_tf_frame_name'),
                               ((0, (0, 0), 'some_tf_frame_name'),
                                2,
                                2,
                                'rgb8',
                                0,
                                0,
                                [0, 0,
                                 0, 0]),
                               0.0,
                               0.0,
                               (0, 0, 0, 0, True),
                               0.0,
                               0.0,
                               0.0
                              )
