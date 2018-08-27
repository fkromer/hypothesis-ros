# -*- coding: utf-8 -*-

from hypothesis_ros.messages.sensor_msgs import (
    imu, _Imu,
)
from hypothesis_ros.converters.sensor_msgs import map_imu
try:
    from sensor_msgs.msg import Imu
except ImportError:
    raise ImportError('Please install ROS package ros-{DISTRO}-common-msgs.')
import pytest


def test_map_imu_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_imu(invalid_type)


def test_map_hypothesis_imu_to_rospy():
    hypothesis_type = imu().example()
    rospy_type = map_imu(hypothesis_type)
    assert isinstance(rospy_type, Imu), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)