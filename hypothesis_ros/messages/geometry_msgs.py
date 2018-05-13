# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS geometry_msgs`_.

.. _ROS geometry_msgs:
   http://wiki.ros.org/geometry_msgs

"""

from collections import namedtuple
from hypothesis.strategies import composite

from hypothesis_ros.message_fields import float64

_Point = namedtuple('Point', 'x y z')
_Quaternion = namedtuple('Quaternion', 'x y z w')
_Pose = namedtuple('Pose', 'position orientation')
_Transform = namedtuple('Transform', 'translation rotation')
_Vector3 = namedtuple('Vector3', 'x y z')

@composite
def point(draw, x=float64(), y=float64(), z=float64()):
    """
    Generate value for ROS geometry message type "point".

    Parameters
    ----------
    x : hypothesis.strategies.floats()
        Strategy to generate x value. (Default: Default hypothesis strategy.)
    y : hypothesis.strategies.floats()
        Strategy to generate y value. (Default: Default hypothesis strategy.)
    z : hypothesis.strategies.floats()
        Strategy to generate z value. (Default: Default hypothesis strategy.)

    """
    x_value, y_value, z_value = draw(x), draw(y), draw(z)
    assert isinstance(x_value, float), 'drew invalid x={x_value} from {x} for float64 field'.format(x_value, x)
    assert isinstance(y_value, float), 'drew invalid y={y_value} from {y} for float64 field'.format(y_value, y)
    assert isinstance(z_value, float), 'drew invalid y={z_value} from {z} for float64 field'.format(z_value, z)
    return _Point(x_value, y_value, z_value)


@composite
def quaternion(draw, x=float64(), y=float64(), z=float64(), w=float64()):
    """
    Generate value for ROS geometry message type "quaternion".

    Parameters
    ----------
    x : hypothesis.strategies.floats()
        Strategy to generate x value. (Default: Default hypothesis strategy.)
    y : hypothesis.strategies.floats()
        Strategy to generate y value. (Default: Default hypothesis strategy.)
    z : hypothesis.strategies.floats()
        Strategy to generate z value. (Default: Default hypothesis strategy.)
    w : hypothesis.strategies.floats()
        Strategy to generate w value. (Default: Default hypothesis strategy.)

    """
    x_value, y_value, z_value, w_value = draw(x), draw(y), draw(z), draw(w)
    assert isinstance(x_value, float), 'drew invalid x={x_value} from {x} for float64 field'.format(x_value, x)
    assert isinstance(y_value, float), 'drew invalid y={y_value} from {y} for float64 field'.format(y_value, y)
    assert isinstance(z_value, float), 'drew invalid y={z_value} from {z} for float64 field'.format(z_value, z)
    assert isinstance(w_value, float), 'drew invalid y={w_value} from {w} for float64 field'.format(w_value, w)
    return _Quaternion(x_value, y_value, z_value, w_value)


@composite
def pose(draw, position=point(), orientation=quaternion()):
    """
    Generate value for ROS geometry message type "pose".

    Parameters
    ----------
    position : hypothesis_ros.ros1.point()
        Strategy to generate position value. (Default: Default hypothesis_ros strategy.)
    orientation : hypothesis_ros.ros1.quaternion()
        Strategy to generate orientation value. (Default: Default hypothesis-ros strategy.)

    """
    position_value, orientation_value = draw(position), draw(orientation)
    assert isinstance(position_value, _Point), 'drew invalid position={position_value} from {position} for _Point field'.format(position_value, position)
    assert isinstance(orientation_value, _Quaternion), 'drew invalid orientation={orientation_value} from {orientation} for _Quaternion field'.format(orientation_value, orientation)
    return _Pose(position_value, orientation_value)


@composite
def vector3(draw, x=float64(), y=float64(), z=float64()):
    """
    Generate value for ROS geometry message type "vector3".

    Parameters
    ----------
    x : hypothesis.strategies.floats()
        Strategy to generate x value. (Default: Default hypothesis strategy.)
    y : hypothesis.strategies.floats()
        Strategy to generate y value. (Default: Default hypothesis strategy.)
    z : hypothesis.strategies.floats()
        Strategy to generate z value. (Default: Default hypothesis strategy.)

    """
    x_value, y_value, z_value = draw(x), draw(y), draw(z)
    assert isinstance(x_value, float), 'drew invalid x={x_value} from {x} for float64 field'.format(x_value, x)
    assert isinstance(y_value, float), 'drew invalid y={y_value} from {y} for float64 field'.format(y_value, y)
    assert isinstance(z_value, float), 'drew invalid y={z_value} from {z} for float64 field'.format(z_value, z)
    return _Vector3(x_value, y_value, z_value)


@composite
def transform(draw, translation=vector3(), rotation=quaternion()):
    """
    Generate value for ROS geometry message type "transform".

    Parameters
    ----------
    position : hypothesis_ros.ros1.vector3()
        Strategy to generate translation value. (Default: Default hypothesis_ros strategy.)
    orientation : hypothesis_ros.ros1.quaternion()
        Strategy to generate rotation value. (Default: Default hypothesis-ros strategy.)

    """
    translation_value, rotation_value = draw(translation), draw(rotation)
    assert isinstance(translation_value, _Vector3), 'drew invalid translation={translation_value} from {translation} for _Vector3 field'.format(translation_value, translation)
    assert isinstance(rotation_value, _Quaternion), 'drew invalid rotation={rotation_value} from {rotation} for _Quaternion field'.format(rotation_value, rotation)
    return _Transform(translation_value, rotation_value)