# -*- coding: utf-8 -*-

from hypothesis_ros.messages.geometry_msgs import (
    point, _Point,
    quaternion, _Quaternion,
    pose, _Pose,
    vector3, _Vector3,
    transform, _Transform,
    transform_stamped, _TransformStamped,
)
from hypothesis_ros.converters.geometry_msgs import (
    map_point,
    map_quaternion,
    map_pose,
    map_vector3,
    map_transform,
    map_transform_stamped,
)
try:
    from geometry_msgs.msg import (
        Point,
        Quaternion,
        Pose,
        Vector3,
        Transform,
        TransformStamped,
    )
except ImportError:
    raise ImportError('Please install ROS1 package ros-{DISTRO}-common-msgs.')
import pytest


def test_map_point_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_point(invalid_type)


def test_map_hypothesis_point_to_rospy():
    hypothesis_type = point().example()
    rospy_type = map_point(hypothesis_type)
    assert isinstance(rospy_type, Point), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)


def test_map_quaternion_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_quaternion(invalid_type)


def test_map_hypothesis_quaternion_to_rospy():
    hypothesis_quaternion = quaternion().example()
    rospy_type = map_quaternion(hypothesis_quaternion)
    assert isinstance(rospy_type, Quaternion), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)


def test_map_pose_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_pose(invalid_type)


def test_map_hypothesis_pose_to_rospy():
    hypothesis_pose = pose().example()
    rospy_type = map_pose(hypothesis_pose)
    assert isinstance(rospy_type, Pose), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)


def test_map_vector3_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_vector3(invalid_type)


def test_map_hypothesis_vector3_to_rospy():
    hypothesis_vector3 = vector3().example()
    rospy_type = map_vector3(hypothesis_vector3)
    assert isinstance(rospy_type, Vector3), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)


def test_map_transform_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_transform(invalid_type)


def test_map_hypothesis_transform_to_rospy():
    hypothesis_type = transform().example()
    rospy_type = map_transform(hypothesis_type)
    assert isinstance(rospy_type, Transform), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)


def test_map_transform_stamped_asserts_in_case_of_wrong_type():
    invalid_type = 42
    with pytest.raises(TypeError):
        rospy_type = map_transform_stamped(invalid_type)


def test_map_hypothesis_transform_stamped_to_rospy():
    hypothesis_type = transform_stamped().example()
    rospy_type = map_transform_stamped(hypothesis_type)
    assert isinstance(rospy_type, TransformStamped), 'Hypothesis type ({}) could not be mapped to rospy type ({}).'.format(hypothesis_type, rospy_type)