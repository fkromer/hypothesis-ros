# -*- coding: utf-8 -*-

from hypothesis_ros.messages.sensor_msgs import (
    _Image,
    _Imu,
)
try:
    from sensor_msgs.msg import Image, Imu
except ImportError:
    raise ImportError('Please install ROS package ros-{ROS-DISTRO}-common-msgs.')


def map_imu(values):
    """
    Map the values generated with the hypothesis-ros imu strategy to a rospy imu type.
    """
    if not isinstance(values, _Imu):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_imu = Imu()
    ros_imu.header = values.header
    ros_imu.orientation = values.orientation
    ros_imu.orientation_covariance = values.orientation_covariance
    ros_imu.angular_velocity = values.angular_velocity
    ros_imu.angular_velocity_covariance = values.angular_velocity_covariance
    ros_imu.linear_acceleration = values.linear_acceleration
    ros_imu.linear_acceleration_covariance = values.linear_acceleration_covariance
    return ros_imu


def map_image(values):
    """
    Map the values generated with the hypothesis-ros image strategy to a rospy Image type.
    """
    if not isinstance(values, _Image):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_image = Image()
    ros_image.header = values.header
    ros_image.height = values.height
    ros_image.width = values.width
    ros_image.encoding = values.encoding
    ros_image.is_bigendian = values.is_bigendian
    ros_image.data = values.data
    return ros_image
