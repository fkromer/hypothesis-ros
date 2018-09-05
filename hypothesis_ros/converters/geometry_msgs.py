# -*- coding: utf-8 -*-

"""
Provides converters for message field data generators which map
Python-only dependency data to rospy compatible publisher arguments.
"""

from hypothesis_ros.messages.geometry_msgs import (
    _Point,
    _Quaternion,
    _Pose,
    _Transform,
    _TransformStamped,
    _Vector3,
)
from hypothesis_ros.messages.std_msgs import _Header
from hypothesis_ros.converters.std_msgs import map_header

try:
    from geometry_msgs.msg import (
        Point,
        Quaternion,
        Pose,
        Transform,
        TransformStamped,
        Vector3,
    )
except ImportError:
    raise ImportError('Please install ROS1 package ros-{ROS-DISTRO}-common-msgs.')


def map_point(values):
    """
    Map the values generated with the hypothesis-ros point strategy to a rospy Point type.
    """
    if not isinstance(values, _Point):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_point = Point()
    ros_point.x = values.x
    ros_point.y = values.y
    ros_point.z = values.z
    return ros_point


def map_quaternion(values):
    """
    Map the values generated with the hypothesis-ros quaternion strategy to a rospy Quaternion type.
    """
    if not isinstance(values, _Quaternion):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_quaternion = Quaternion()
    ros_quaternion.x = values.x
    ros_quaternion.y = values.y
    ros_quaternion.z = values.z
    ros_quaternion.w = values.w
    return ros_quaternion


def map_pose(values):
    """
    Map the values generated with the hypothesis-ros pose strategy to a rospy Pose type.
    """
    if not isinstance(values, _Pose):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_pose = Pose()
    ros_pose.position = map_point(values.position)
    ros_pose.orientation = map_quaternion(values.orientation)
    return ros_pose


def map_transform(values):
    """
    Map the values generated with the hypothesis-ros transform strategy to a rospy Transform type.
    """
    if not isinstance(values, _Transform):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_transform = Transform()
    ros_transform.translation = map_vector3(values.translation)
    ros_transform.rotation = map_quaternion(values.rotation)
    return ros_transform


def map_transform_stamped(values):
    """
    Map the values generated with the hypothesis-ros transform_stamped strategy to a rospy TransformStamped type.
std_msgs/Header header
string child_frame_id
geometry_msgs/Transform transform
    """
    if not isinstance(values, _TransformStamped):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_transform_stamped = TransformStamped()
    ros_transform_stamped.header = map_header(values.header)
    ros_transform_stamped.child_frame_id = values.child_frame_id
    ros_transform_stamped.transform = map_transform(values.transform)
    return ros_transform_stamped


def map_vector3(values):
    """
    Map the values generated with the hypothesis-ros vector3 strategy to a rospy vector type.
    """
    if not isinstance(values, _Vector3):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_vector3 = Vector3()
    ros_vector3.x = values.x
    ros_vector3.y = values.y
    ros_vector3.z = values.z
    return ros_vector3
