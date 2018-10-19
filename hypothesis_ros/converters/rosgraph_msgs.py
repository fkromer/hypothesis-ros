# -*- coding: utf-8 -*-

"""
Provides converters for rosgraph_msgs message field generators which map
internal data type to rospy compatible publisher arguments.
"""
from hypothesis_ros.messages.rosgraph_msgs import _Log
try:
    from rosgraph_msgs.msg import Log
except ImportError:
    raise ImportError('Please install ROS1 package ros-{ROS-DISTRO}-common-msgs.')


def map_log(values):
    """
    Map the values generated with the hypothesis-ros log strategy to a rospy header type.
    """
    if not isinstance(values, _Log):
        raise TypeError('Wrong type. Use appropriate hypothesis-ros type.')
    ros_log = Log()
    ros_log.header = values.header
    ros_log.level = values.level
    ros_log.name = values.name
    ros_log.msg = values.msg
    ros_log.file = values.file
    ros_log.function = values.function
    ros_log.topics = values.topics

    return ros_log
