# hypothesis-ros

[![Build Status](https://travis-ci.org/ros-testing/hypothesis-ros.svg?branch=master)](https://travis-ci.org/ros-testing/hypothesis-ros)
[![PyPI version](https://badge.fury.io/py/hypothesis-ros.svg)](https://badge.fury.io/py/hypothesis-ros)
[![Read the Docs](https://img.shields.io/readthedocs/pip.svg)](http://hypothesis-ros.readthedocs.io/)
[![GitHub license](https://img.shields.io/github/license/fkromer/hypothesis-ros.svg)](https://github.com/fkromer/hypothesis-ros/blob/master/LICENSE)

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

    ❯ pip install jupyter
    ❯ cd docs/source/notebooks/
    ❯ jupyter lab

## Documentation

### Sphinx documentation (user's guide, API reference)

Build the documentation.

    ❯ tox -e docs

Open the documentation.

    ❯ xdg-open ./docs/build/index.html

### Interactive documentation (API reference)

    ❯ ipython
    In [1]: from hypothesis_ros import message_fields
    In [2]: message_fields?
    (module documentation)
    In [3]: message_fields.<TAB-replacement>?
    (documentation of strategies, etc.)
