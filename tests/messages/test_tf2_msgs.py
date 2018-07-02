# -*- coding: utf-8 -*-
"""
Unit tests for the tf2_msgs strategies.
"""

from hypothesis import given
from hypothesis.strategies import just

from hypothesis_ros.messages.tf2_msgs import tfmessage
from hypothesis_ros.messages.geometry_msgs import (
    transform,
    transform_stamped,
    vector3,
    quaternion
)
from hypothesis_ros.messages.std_msgs import header
from hypothesis_ros.message_fields import (
    array,
    float64,
    uint32,
    time,
)


@given(array(elements=transform_stamped(
           header(seq=uint32(min_value=0, max_value=0),
                  stamp=time(
                      secs=uint32(min_value=1, max_value=1),
                      nsecs=uint32(min_value=2, max_value=2)
                  ),
                  frame_id=just('some_tf_frame_name')
                 ),
           just('some_child_frame_id'),
           transform(
               translation=vector3(
                   x=float64(min_value=1.0, max_value=1.0),
                   y=float64(min_value=2.0, max_value=2.0),
                   z=float64(min_value=3.0, max_value=3.0)
               ),
               rotation=quaternion(
                   x=float64(min_value=1.0, max_value=1.0),
                   y=float64(min_value=2.0, max_value=2.0),
                   z=float64(min_value=3.0, max_value=3.0),
                   w=float64(min_value=4.0, max_value=4.0)
               )
           )
            ), min_size=2, max_size=2
      )
)
def test_tfmessage_accepts_customized_strategies(generated_value):
    """Exemplary customized TFMessage."""
    assert generated_value == [((0, (1, 2), 'some_tf_frame_name'),
                               'some_child_frame_id',
                               ((1.0, 2.0, 3.0), (1.0, 2.0, 3.0, 4.0))),
                               ((0, (1, 2), 'some_tf_frame_name'),
                               'some_child_frame_id',
                               ((1.0, 2.0, 3.0), (1.0, 2.0, 3.0, 4.0)))]
