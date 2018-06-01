.. hypothesis-ros documentation master file, created by
   sphinx-quickstart on Sun Apr 15 12:00:41 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to hypothesis-ros
=========================

.. image:: _static/logo_full.jpg
    :alt: hypothesis-ros: property based ROS node level testing
    :scale: 50 %
    :align: right

`hypothesis-ros` looks small and cute. But it is one of those libraries on the dark side of power.
It can be very powerful and very nasty. It enables property-based testing
on the ROS node level. It provides generators for message data fields, parameters
and message fields of a growing number of messages.

hypothesis-ros depends on property based testing framework `hypothesis`_.
The documentation for this library can be found in the `hypothesis documentation`_.

.. _hypothesis: https://github.com/HypothesisWorks/hypothesis
.. _hypothesis documentation: https://hypothesis.readthedocs.io/en/latest/index.html

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. include:: docu.rst
.. include:: modules.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
