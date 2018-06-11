# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS tf2_msgs`_.

.. _ROS tf2_msgs:
   http://wiki.ros.org/tf2_msgs

"""


from collections import namedtuple
from hypothesis.strategies import composite

from hypothesis_ros.messages.geometry_msgs import transform_stamped
from hypothesis_ros.message_fields import array


_TFMessage = namedtuple('TFMessage', 'transforms')


@composite
def tfmessage(draw, transforms=array(elements=transform_stamped())):
    """
    Generate value for ROS TFMessage.

    Parameters
    ----------
    transforms : hypothesis_ros.message_field.array()
        Strategy to generate transforms value. (Default: Default hypothesis_ros strategy
        with elements of type hypothesis_ros.message.geometry_msgs.transform_stamped().)

    """
    transforms_value = draw(transforms_value)
    return _TFMessage(transforms_value)
