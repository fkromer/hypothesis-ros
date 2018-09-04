# -*- coding: utf-8 -*-

"""
Provides converters for std_msgs message field generators which map
internal data type to rospy compatible publisher arguments.
"""

from hypothesis_ros.messages.std_msgs import _Header
try:
    from std_msgs.msg import Header
except ImportError:
    raise ImportError('Please install ROS1 package ros-{ROS-DISTRO}-common-msgs.')


def map_header(values):
    """
    Map the values generated with the hypothesis-ros header strategy to a rospy header type.
    """
    if not isinstance(values, _Header):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_header = Header()
    ros_header.seq = values.seq
    ros_header.stamp = values.stamp
    ros_header.frame_id = values.frame_id
    return ros_header
