# -*- coding: utf-8 -*-
"""
Unit tests for the geometry_msgs strategies.
"""

from hypothesis import given
from hypothesis.strategies import just
from hypothesis_ros.messages.geometry_msgs import (
    point,
    pose,
    pose_with_covariance,
    vector3,
    quaternion,
    transform
)
from hypothesis_ros.message_fields import (
    array,
    float64
)


@given(point(x=float64(min_value=0.0, max_value=0.0),
             y=float64(min_value=0.0, max_value=0.0),
             z=float64(min_value=0.0, max_value=0.0)
            )
      )
def test_point_accepts_customized_strategies(generated_value):
    """Exemplary customized point."""
    assert generated_value == (0.0, 0.0, 0.0)


@given(quaternion(x=float64(min_value=0.0, max_value=0.0),
                  y=float64(min_value=0.0, max_value=0.0),
                  z=float64(min_value=0.0, max_value=0.0),
                  w=float64(min_value=0.0, max_value=0.0)
                 )
      )
def test_quaternion_accepts_customized_strategies(generated_value):
    """Exemplary customized quaternion."""
    assert generated_value == (0, 0, 0, 0)


@given(pose(position=point(x=float64(min_value=0.0, max_value=0.0),
                  y=float64(min_value=0.0, max_value=0.0),
                  z=float64(min_value=0.0, max_value=0.0)
                 ),
            orientation=quaternion(x=float64(min_value=0.0, max_value=0.0),
                       y=float64(min_value=0.0, max_value=0.0),
                       z=float64(min_value=0.0, max_value=0.0),
                       w=float64(min_value=0.0, max_value=0.0)
                      )
           )
       )
def test_pose_accepts_customized_strategies(generated_value):
    """Exemplary customized pose."""
    assert generated_value == ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))


@given(pose_with_covariance(pose(position=point(x=float64(min_value=0.0, max_value=0.0),
                                                y=float64(min_value=0.0, max_value=0.0),
                                                z=float64(min_value=0.0, max_value=0.0)
                                               ),
                                 orientation=quaternion(x=float64(min_value=0.0, max_value=0.0),
                                                        y=float64(min_value=0.0, max_value=0.0),
                                                        z=float64(min_value=0.0, max_value=0.0),
                                                        w=float64(min_value=0.0, max_value=0.0)
                                                       )
                                ),
                            array(elements=float64(min_value=0.0, max_value=0.0), min_size=36, max_size=36)
                           )
       )
def test_pose_with_covariance_accepts_customized_strategies(generated_value):
    """Exemplary customized pose_with_covariance."""
    assert generated_value == (((0.0, 0.0, 0.0),
                                (0.0, 0.0, 0.0, 0.0)
                               ),
                               [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0
                               ]
                              )


@given(transform(translation=vector3(
                  x=float64(min_value=0.0, max_value=0.0),
                  y=float64(min_value=0.0, max_value=0.0),
                  z=float64(min_value=0.0, max_value=0.0)
                 ),
                 rotation=quaternion(
                     x=float64(min_value=0.0, max_value=0.0),
                     y=float64(min_value=0.0, max_value=0.0),
                     z=float64(min_value=0.0, max_value=0.0),
                     w=float64(min_value=0.0, max_value=0.0)
                 )
                )
       )
def test_translation_accepts_customized_strategies(generated_value):
    """Exemplary customized pose."""
    assert generated_value == ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))


@given(vector3(x=float64(min_value=0.0, max_value=0.0),
               y=float64(min_value=0.0, max_value=0.0),
               z=float64(min_value=0.0, max_value=0.0)
              )
      )
def test_vector3_accepts_customized_strategies(generated_value):
    """Exemplary customized vector3."""
    assert generated_value == (0.0, 0.0, 0.0)