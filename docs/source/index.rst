hypothesis-ros
==============

Data generators for Property Based Testing and Fuzzy Testing of ROS nodes.

.. image:: https://img.shields.io/pypi/wheel/hypothesis-ros.svg
    :target: https://pypi.org/project/hypothesis-ros/

.. image:: https://img.shields.io/pypi/pyversions/hypothesis-ros.svg
    :target: https://pypi.org/project/hypothesis-ros/

.. image:: https://img.shields.io/pypi/l/hypothesis-ros.svg
    :target: https://pypi.org/project/hypothesis-ros/

`hypothesis-ros` looks small and cute. But it is one of those libraries on the dark side of power.
It can be very powerful and very nasty. It enables property-based testing
on the ROS node level. It provides generators for message data fields, parameters
and message fields of a growing number of messages.

`hypothesis-ros` depends on property based testing framework `hypothesis`_.
The documentation for this library can be found in the `hypothesis documentation`_.

.. _hypothesis: https://github.com/HypothesisWorks/hypothesis
.. _hypothesis documentation: https://hypothesis.readthedocs.io/en/latest/index.html

The naming of strategies is according to ROS notation to ease the mapping of the strategies
to the corresponding ROS data types, messages and parameters. Consider that this implies
some conflict with Python builtins (e.g. `bool`, `list`).

The User's Guide
----------------

This section is about configuration and integration considerations. To get hints about
how to use the data generators of this package refer to the API documentation and the
`tests directory of the package source code repository`_.

.. _tests directory of the package source code repository: https://github.com/ros-testing/hypothesis-ros/tree/master/tests

.. toctree::
   :maxdepth: 2

   docu

The API Documentation
---------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 3

   api

The Changelog
-------------

If you are interested in how this package evolved over time look into here.

.. toctree::
   :maxdepth: 1

   changes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
