# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS sensor_msgs`_.

.. _ROS sensor_msgs:
   http://wiki.ros.org/sensor_msgs

"""

from collections import namedtuple
from hypothesis.strategies import composite

from hypothesis_ros.message_fields import (  # pylint: disable=redefined-builtin
    bool,
    uint32,
)

_RegionOfInterest = namedtuple('RegionOfInterest', 'x_offset y_offset height width do_rectify')


@composite
def region_of_interest(draw,  # pylint: disable=too-many-arguments
                       x_offset=uint32(),
                       y_offset=uint32(),
                       height=uint32(),
                       width=uint32(),
                       do_rectify=bool()):  # pylint: disable=no-value-for-parameter
    """
    Generate values for ROS sensor_msgs/RegionOfInterest.msg.

    Parameters
    ----------
    x_offset : hypothesis_ros.message_fields.uint32()
        Strategy to generate x_offset value. (Default: Default hypothesis_ros strategy.)
    y_offset : hypothesis_ros.message_fields.uint32()
        Strategy to generate y_offset value. (Default: Default hypothesis_ros strategy.)
    height : hypothesis_ros.message_fields.uint32()
        Strategy to generate height value. (Default: Default hypothesis_ros strategy.)
    width : hypothesis_ros.message_fields.uint32()
        Strategy to generate width value. (Default: Default hypothesis_ros strategy.)
    do_rectify : hypothesis_ros.message_fields.bool()
        Strategy to generate do_rectify value. (Default: Default hypothesis_ros strategy.)

    """
    x_offset_value = draw(x_offset)
    y_offset_value = draw(y_offset)
    height_value = draw(height)
    width_value = draw(width)
    do_rectify_value = draw(do_rectify)
    assert isinstance(x_offset_value, int), 'drew invalid x_offset={x_offset_value} from {x_offset} for uint32 field'.format(x_offset_value, x_offset)
    assert isinstance(y_offset_value, int), 'drew invalid y_offset={y_offset_value} from {y_offset} for uint32 field'.format(y_offset_value, y_offset)
    assert isinstance(height_value, int), 'drew invalid height={height_value} from {height} for uint32 field'.format(height_value, height)
    assert isinstance(width_value, int), 'drew invalid width={width_value} from {width} for uint32 field'.format(width_value, width)
    assert isinstance(do_rectify_value, int), 'drew invalid do_rectify={do_rectify_value} from {do_rectify} for bool field'.format(do_rectify_value, do_rectify)  # bool is subclass of int
    return _RegionOfInterest(x_offset_value, y_offset_value, height_value, width_value, do_rectify_value)
