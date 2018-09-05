.. currentmodule:: hypothesis-ros

Changelog
=========

v1.0.0
------

- add rospy converters for std_msgs Header
- add rospy converters for geometry_msgs

 - Point
 - Quaternion
 - Pose
 - Transform
 - TransformStamped
 - Vector3

- add rospy converters for sensor_msgs

 - Imu
 - Image

- fix typo in geometry_msgs _TransformStamped
- add test coverage analysis
- add CI tool integration
- add source code docs

v0.3.0
------

- add strategies for

 - CameraInfo.msg
 - PoseWithCovarianceStamped.msg

- improve tests

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
for ROS1 msg field types, ROS1 parameter types and ROS1 msgs.

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
