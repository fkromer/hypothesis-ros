# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS sensor_msgs`_.

.. _ROS sensor_msgs:
   http://wiki.ros.org/sensor_msgs

"""

from collections import namedtuple
from hypothesis.strategies import composite, sampled_from

from hypothesis_ros.messages.geometry_msgs import vector3, quaternion
from hypothesis_ros.messages.std_msgs import header
from hypothesis_ros.message_fields import (  # pylint: disable=redefined-builtin
    array,
    bool,
    float32,
    float64,
    time,
    uint8,
    uint32,
)

_RegionOfInterest = namedtuple('RegionOfInterest', 'x_offset y_offset height width do_rectify')
_Imu = namedtuple('Imu', 'header orientation orientation_covariance angular_velocity angular_velocity_covariance linear_acceleration linear_acceleration_covariance')
_CompressedImage = namedtuple('CompressedImage', 'header format data')

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


@composite
def imu(draw,
        header=header(),
        orientation=quaternion(),
        orientation_covariance=array(elements=float64(), min_size=9, max_size=9),
        angular_velocity=vector3(),
        angular_velocity_covariance=array(elements=float64(), min_size=9, max_size=9),
        linear_acceleration=vector3(),
        linear_acceleration_covariance=array(elements=float64(), min_size=9, max_size=9)
       ):
    """
    Generate values for ROS sensor_msgs/Imu.msg.

    Parameters
    ----------
    header : hypothesis_ros.std_msgs.header()
        Strategy to generate header value. (Default: Default hypothesis_ros strategy.)
    orientation : hypothesis_ros.geometry_msgs.Quaternion()
        Strategy to generate orientation value. (Default: Default hypothesis_ros strategy.)
    orientation_covariance : hypothesis_ros.message_fields.array()
        Strategy to generate orientation_covariance value. (Default: Customized to 9 elements of type float64().)
    angular_velocity : hypothesis_ros.messages.geometry_msgs.vector3()
        Strategy to generate angular_velocity value. (Default: Default hypothesis_ros strategy.)
    angular_velocity_covariance : hypothesis_ros.message_fields.array()
        Strategy to generate angular_velocity_covariance value. (Default: Customized to 9 elements of type float64().)
    linear_acceleration : hypothesis_ros.messages.geometry_msgs.vector3()
        Strategy to generate linear_acceleration value. (Default: Default hypothesis_ros strategy.)
    linear_acceleration_covariance : hypothesis_ros.messages.message_fields.array()
        Strategy to generate linear_acceleration_covariance value. (Default: Customized to 9 elements of type float64().)

    """
    header_value = draw(header)
    orientation_value = draw(orientation)
    orientation_covariance_value = draw(orientation_covariance)
    angular_velocity_value = draw(angular_velocity)
    angular_velocity_covariance_value = draw(angular_velocity_covariance)
    linear_acceleration_value = draw(linear_acceleration)
    linear_acceleration_covariance_value = draw(linear_acceleration_covariance)
    # TODO: add validation
    return _Imu(header_value,
                orientation_value,
                orientation_covariance_value,
                angular_velocity_value,
                angular_velocity_covariance_value,
                linear_acceleration_value,
                linear_acceleration_covariance_value
               )


@composite
def compressed_image(draw, header=header(), format=sampled_from(['jpg', 'png']), data=array(elements=uint8())):
    """
    Generate values for ROS sensor_msgs/CompressedImage.msg.

    Parameters
    ----------
    header : hypothesis_ros.std_msgs.header()
        Strategy to generate header value. (Default: Default hypothesis_ros strategy.)
    format : hypothesis.strategies.sampled_from()
        Strategy to generate format value. (Default: Customized hypothesis strategy.)
    data : hypothesis_ros.message_fields.array()
        Strategy to generate format value. (Default: Customized to elements of type uint8().)

    """
    header_value = draw(header)
    format_value = draw(format)
    data_value = draw(data)
    return _CompressedImage(header_value,
                            format_value,
                            data_value
                           )
