# hypothesis-ros

[![Build Status](https://travis-ci.org/fkromer/hypothesis-ros.svg?branch=master)](https://travis-ci.org/fkromer/hypothesis-ros)

Hypothesis strategies for ROS node level property based testing.

## Installation

    ❯ pip install git+https://github.com/ros-testing/hypothesis-ros

## Usage

    ❯ pip install ipython
    ❯ ipython
    In [1]: from hypothesis_ros.message_fields import int16
    In [2]: int16().example()
    Out[2]:-32183
    In [3]: int16(min_value=5, max_value=5).example()
    Out[3]: 5

## Examples

    ❯ pip install ipython
    ❯ pip install "ipython[notebook]"
    ❯ jupyter notebook docs/source/notebooks/core_pub_sub_hypothesis_ros.ipynb

## Documentation

    ❯ ipython
    In [1]: from hypothesis_ros import message_fields
    In [2]: message_fields?
    (module documentation)
    In [3]: message_fields.<TAB-replacement>?
    (documentation of strategies, etc.)
