# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS stereo_msgs`_.

.. _ROS stereo_msgs:
   http://wiki.ros.org/stereo_msgs

"""

from collections import namedtuple
from hypothesis.strategies import composite

from hypothesis_ros.messages.geometry_msgs import transform_stamped
from hypothesis_ros.messages.sensor_msgs import image, region_of_interest
from hypothesis_ros.messages.std_msgs import header
from hypothesis_ros.message_fields import (
    array,
    float32
)


_DisparityImage = namedtuple('DisparityImage', 'header image f T valid_window min_disparity max_disparity delta_d')


@composite
def disparity_image(draw, header=header(), image=image(), f=float32(), t=float32(), valid_window=region_of_interest(), min_disparity=float32(), max_disparity=float32(), delta_d=float32()):
    """
    Generate value for ROS DisparityImage.msg.

    Parameters
    ----------
    header : hypothesis_ros.messages.std_msgs.header()
        Strategy to generate header value. (Default: Default hypothesis-ros strategy.)
    image : hypothesis_ros.messages.sensor_msgs.image()
        Strategy to generate image value. (Default: Default hypothesis-ros strategy.)
    f : hypothesis_ros.message_field.float32()
        Strategy to generate f value. (Default: Default hypothesis-ros strategy.)
    t : hypothesis_ros.message_field.float32()
        Strategy to generate T value. (Default: Default hypothesis-ros strategy.)
    valid_window : hypothesis_ros.messages.sensor_msgs.region_of_interest()
    min_disparity : hypothesis_ros.message_field.float32()
        Strategy to generate T value. (Default: Default hypothesis-ros strategy.)
    max_disparity : hypothesis_ros.message_field.float32()
        Strategy to generate T value. (Default: Default hypothesis-ros strategy.)
    delta_d : hypothesis_ros.message_field.float32()
        Strategy to generate T value. (Default: Default hypothesis-ros strategy.)

    """
    header_value = draw(header)
    image_value = draw(image)
    f_value = draw(f)
    t_value = draw(t)
    valid_window_value = draw(valid_window)
    min_disparity_value = draw(min_disparity)
    max_disparity_value = draw(max_disparity)
    delta_d_value = draw(delta_d)
    return _DisparityImage(header_value,
                           image_value,
                           f_value,
                           t_value,
                           valid_window_value,
                           min_disparity_value,
                           max_disparity_value,
                           delta_d_value)
