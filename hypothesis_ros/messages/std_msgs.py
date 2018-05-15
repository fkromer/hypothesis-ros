# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS std_msgs`_.

.. _ROS std_msgs:
   http://wiki.ros.org/std_msgs

"""

from collections import namedtuple
from hypothesis.strategies import composite

from hypothesis_ros.message_fields import (
    float64,
    uint32,
    time
)

_Header = namedtuple('Header', 'seq stamp frame_id')

@composite
def header(draw, seq=uint32(), stamp=time(), frame_id=float64()):
    """
    Generate value for ROS standard message type "header".

    Parameters
    ----------
    seq : hypothesis_ros.message_fields.uint32()
        Strategy to generate seq value. (Default: Default hypothesis_ros strategy.)
    stamp : hypothesis_ros.message_fields.time()
        Strategy to generate stamp value. (Default: Default hypothesis_ros strategy.)
    frame_id : hypothesis_ros.ros1.float64()
        Strategy to generate frame_id value. (Default: Default hypothesis_ros strategy.)

    """
    seq_value = draw(seq)
    stamp_value = draw(stamp)
    frame_id_value = draw(frame_id)
    assert isinstance(seq_value, int), 'drew invalid seq={seq_value} from {seq} for uint32 field'.format(seq_value, seq)
    assert isinstance(stamp_value.secs, int), 'drew invalid stamp.secs={stamp_value} from {stamp} for int field'.format(stamp_value.secs, stamp)
    assert isinstance(stamp_value.nsecs, int), 'drew invalid stamp.nsecs={stamp_value} from {stamp} for int field'.format(stamp_value.nsecs, stamp)
    assert isinstance(frame_id_value, float), 'drew invalid frame_id={frame_id_value} from {frame_id} for float64 field'.format(frame_id_value, frame_id)
    return _Header(seq_value, stamp_value, frame_id_value)
