User's Guide
============

Compatibility with Python interpreters
--------------------------------------

`hypothesis-ros` uses `hypothesis` which implies the compatibility with Python interpreters.
Hypothesis is supported and tested on CPython 2.7 and CPython 3.4+ (`hypothesis docs python versions`_).

.. _hypothesis docs python versions: https://hypothesis.readthedocs.io/en/latest/supported.html#python-versions

Compatibility with Python test frameworks (test runners)
--------------------------------------------------------

`hypothesis-ros` uses `hypothesis` which implies the compatibility with Python test frameworks.
Hypothesis is compatible with

- `unittest` (supported, tested, no limitations),
- `pytest` (supported, tested, limitations: function based fixtures do not behave like expected),
- `nose` (supported, tested, yield based tests do not work)

(`hypothesis docs testing frameworks`_).

.. _hypothesis docs testing frameworks: https://hypothesis.readthedocs.io/en/latest/supported.html#testing-frameworks

Configuration of settings
-------------------------

`hypothesis` was initially designed for Python source code level testing.
Therefore the configuration of `settings` needs special care.

`deadline`: A deadline has either set to a very high value or should be disabled.

`perform_health_checks`: In case `perform_health_checks` is enabled some health checks
need to be selectively disabled with `suppress_health_check`.

`suppress_health_check`: Refer to :ref:`Configuration of health checks`.

`use_coverage`: `hypothesis` supports coverage based data generation when the tests
are executed on the Python source code level. `hypothesis-ros` does not support
coverage based data generation. Enabling it has no effect/could raise errors. 

A typical configuration of `timeout` and `deadline` in `@settings` looks like follows:

.. code-block:: python

    ...
    from hypothesis import settings, unlimited

    ...
    @settings(timeout=unlimited,
              deadline=None,
              ...)
    def test_node_does_not_crash(...):
        ...

The settings `database_file`, `database`, `buffer_size`, `derandomize`,
`max_examples`, `max_iterations`, `max_shrinks`, `min_satisfying_examples`,
`phases`, `stateful_step_count`, `strict`, ``
usually don't need special consideration and may be used as usual.

.. _Configuration of health checks:

Configuration of health checks
------------------------------

`hypothesis` was initially designed for Python source code level testing.
Therefore the configuration of `health checks` (`hypothesis docs health checks`_)
needs special care. In case health checks are performed (`perform_health_checks`)
the health ckeck `too_slow` and `hung_test` need to be disabled via
`suppress_healthcheck` usually.

.. _hypothesis docs health checks: https://hypothesis.readthedocs.io/en/latest/healthchecks.html

A typical configuration of `suppress_health_check` in `@settings` looks like follows:

.. code-block:: python

    ...
    from hypothesis import settings, HealthCheck

    ...
    @settings(...,
              suppress_health_check=[HealthCheck.too_slow,
                                     HealthCheck.hung_test]
             )
    def test_node_does_not_crash(...):
        ...

The health checks `data_too_large`, `filter_too_much`, `return_value` and `large_base_example`
don't need special consideration and may be used as usual.

Configuration of example database
---------------------------------

If a test fails hypothesis saves the test input in a atabase.
The next time hypothesis runs this conditions will be used first.
The configuration of the example database may be adjusted as usual
(`hypothesis docs example database`_).

.. _hypothesis docs example database: https://hypothesis.readthedocs.io/en/latest/database.html?highlight=example%20database#the-hypothesis-example-database
