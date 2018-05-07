# hypothesis-ros

[![Build Status](https://travis-ci.org/fkromer/hypothesis-ros.svg?branch=master)](https://travis-ci.org/fkromer/hypothesis-ros)

Hypothesis strategies for ROS node level property based testing.

## Installation

    ❯ pip install git+https://github.com/fkromer/hypothesis-ros

## Usage

    ❯ pip install ipython
    ❯ ipython
    In [1]: from hypothesis_ros.ros1 import builtin_msg_field_types
    In [2]: builtin_msg_field_types.int16().example()
    Out[2]:-32183
    In [3]: builtin_msg_field_types.int16(min_value=5, max_value=5).example()
    Out[3]: 5

## Examples

    ❯ pip install ipython
    ❯ pip install "ipython[notebook]"
    ❯ jupyter nbconvert --execute docs/source/notebooks/core_pub_sub_hypothesis_ros.ipynb
    ❯ xdg-open docs/source/notebooks/core_pub_sub_hypothesis_ros.html

## Documentation

    ❯ ipython
    In [1]: from hypothesis_ros.ros1 import builtin_msg_field_types
    In [2]: builtin_msg_field_types?
    (module documentation)
    In [3]: builtin_msg_field_types.<TAB-replacement>?
    (documentation of generators, etc.)
