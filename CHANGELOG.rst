.. currentmodule:: hypothesis-ros

Changelog
=========

v0.2.1
------

- fix invalid classifier for License

v0.2.0
------

- add strategies for
  - CompressedImage.msg
  - DisparityImage.msg
  - Image.msg
  - Imu.msg
  - PoseWithCovariance.msg
  - RegionOfInterest.msg
  - TFMessage.msg
  - TransformStamped.msg
- fix field frame_id in strategy Header.msg
- add validation in message field strategies
- refactor dublication of parameter strategies
- add missing tests for geometry_msgs
- add and cleanup tox environments
- change license to Apache 2
- fix docstrings
- improve docs

v0.1.0
------

Initial quick and dirty implementation of hypothesis strategies
for ROS msg field types, ROS parameter types and ROS msgs.

buildin msg field types:

- bool
- int8
- uint8
- int16
- uint16
- int32
- uint32
- int64
- uint64
- float32
- float64
- string
- time
- duration
- array

parameter types:

- bool
- int32
- string
- date
- list
- double

std_msgs:

- Header

geometry_msgs:

- Point
- Quaternion
- Pose
- Transform
- Vector3
