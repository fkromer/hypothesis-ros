# rospbt
ROS node level property based testing.

## Installation

    ❯ pip install rospbt

## Usage

    ❯ ipython
    In [1]: from rospbt.ros1.generators import builtin_msg_field_types
    In [2]: builtin_msg_field_types.int16().example()
    Out[2]:-32183
    In [3]: builtin_msg_field_types.int16(min_value=5, max_value=5).example()
    Out[3]: 5

## Documentation

    ❯ ipython
    In [1]: from rospbt.ros1.generators import builtin_msg_field_types
    In [2]: builtin_msg_field_types?
    (module documentation)
    In [3]: builtin_msg_field_types.<TAB-replacement>?
    (documentation of generators, etc.)
