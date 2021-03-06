# hypothesis-ros

[![Build Status](https://travis-ci.org/ros-testing/hypothesis-ros.svg?branch=master)](https://travis-ci.org/ros-testing/hypothesis-ros)
[![Coverage Status](https://coveralls.io/repos/github/ros-testing/hypothesis-ros/badge.svg?branch=master)](https://coveralls.io/github/ros-testing/hypothesis-ros?branch=master)
[![codecov](https://codecov.io/gh/ros-testing/hypothesis-ros/branch/master/graph/badge.svg)](https://codecov.io/gh/ros-testing/hypothesis-ros)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e057bec073abefcab8ce/test_coverage)](https://codeclimate.com/github/ros-testing/hypothesis-ros/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/e057bec073abefcab8ce/maintainability)](https://codeclimate.com/github/ros-testing/hypothesis-ros/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/eb6e934da2554becb7923fd55c77fa3c)](https://www.codacy.com/project/fkromer/hypothesis-ros/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ros-testing/hypothesis-ros&amp;utm_campaign=Badge_Grade_Dashboard)
[![PyPI version](https://badge.fury.io/py/hypothesis-ros.svg)](https://badge.fury.io/py/hypothesis-ros)
[![Requirements Status](https://requires.io/github/ros-testing/hypothesis-ros/requirements.svg?branch=master)](https://requires.io/github/ros-testing/hypothesis-ros/requirements/?branch=master)
[![Read the Docs](https://img.shields.io/readthedocs/pip.svg)](http://hypothesis-ros.readthedocs.io/)
[![GitHub license](https://img.shields.io/github/license/fkromer/hypothesis-ros.svg)](https://github.com/fkromer/hypothesis-ros/blob/master/LICENSE)

Data generators for Property Based Testing and Fuzzy Testing of ROS1 nodes.

## Project status

This repository is unmaintained and has been archived. Refer to
[ros1_fuzzer](https://github.com/aliasrobotics/ros1_fuzzer) instead.

## Installation

    ❯ pip install hypothesis-ros

## Documentation

Refer to the documentation on [hypothesis-ros.readthedocs.io](https://hypothesis-ros.readthedocs.io), consult the interactive help in your IDE or the help in your interactive Python session:

    ❯ ipython
    In [1]: from hypothesis_ros import message_fields
    In [2]: message_fields?
    (module documentation)
    In [3]: message_fields.<TAB-replacement>?
    (documentation of strategies, etc.)
