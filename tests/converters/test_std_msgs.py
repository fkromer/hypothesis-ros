# -*- coding: utf-8 -*-

from hypothesis_ros.messages.std_msgs import (
    header, _Header,
)
from hypothesis_ros.converters.std_msgs import map_header
try:
    from std_msgs.msg import Header
except ImportError:
    raise ImportError('Please install ROS1 package ros-{DISTRO}-common-msgs.')
import pytest


def test_map_header_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_header(invalid_type)


def test_map_hypothesis_header_to_rospy():
    hypothesis_type = header().example()
    rospy_type = map_header(hypothesis_type)
    assert isinstance(rospy_type, Header), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)