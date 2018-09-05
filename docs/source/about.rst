.. _about:

About hypothesis-ros
====================

In April 2018 began the implementation of the low level library `hypothesis-ros` to lay a foundation to enable
robustness testing of ROS1 C++ nodes/nodelets using a property based (instead of an example based) approach.
This package provides ROS1 independent functionality to generate pseudo-random data for ROS1 message fields and
ROS1 parameters. In the beginning `hypothesis-ros` contained Python dependent functionality only. The ROS1
dependent functionality was separated into the package `rospbt` (not existing anymore). Because the test code
depends on ROS1 messages in some point in time anyway `rospbt` was merged into `hypothesis-ros`. All message
package specific generators (`geometry msgs`_, `sensor msgs`_ , etc.) have been migrated into `hypothesis-ros` as well.
The easier package handling of separate packages (with `hypothesis-ros` having Python-only dependencies only) in the
beginning has not outweighted increased maintenance effort due to separate packages and all implications going along with it.

.. _geometry msgs: http://wiki.ros.org/geometry_msgs
.. _sensor msgs: http://wiki.ros.org/sensor_msgs