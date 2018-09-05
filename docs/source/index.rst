hypothesis-ros
==============

Data generators for Property Based Testing and Fuzzy Testing of ROS1 nodes.

.. image:: https://img.shields.io/pypi/wheel/hypothesis-ros.svg
    :target: https://pypi.org/project/hypothesis-ros/

.. image:: https://img.shields.io/pypi/pyversions/hypothesis-ros.svg
    :target: https://pypi.org/project/hypothesis-ros/

.. image:: https://img.shields.io/pypi/l/hypothesis-ros.svg
    :target: https://pypi.org/project/hypothesis-ros/

`hypothesis-ros` looks small and cute. But it is one of those libraries on the dark side of power.
It can be very powerful and very nasty. It enables property-based testing
on the ROS1 node level. It provides generators for message data fields, parameters
and message fields of a growing number of messages.

`hypothesis-ros` depends on the property based testing framework `hypothesis`_.
The documentation for this library can be found in the `hypothesis documentation`_.

.. _hypothesis: https://github.com/HypothesisWorks/hypothesis
.. _hypothesis documentation: https://hypothesis.readthedocs.io/en/latest/index.html

The naming of strategies is according to ROS1 notation to ease the mapping of the strategies
to the corresponding ROS1 data types, messages and parameters. Consider that this implies
some conflict with Python builtins (e.g. `bool`, `list`).

.. toctree::
   :maxdepth: 2

   docu
   api
   about

.. toctree::
   :maxdepth: 1

   changes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
