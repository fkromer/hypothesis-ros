# Contributing guidelines

## How to become a contributor and submit your own code

### Contributing code

If you have improvements to `rospbt`, send your pull requests! For those
just getting started, Github has a
[howto "using pull requests"](https://help.github.com/articles/using-pull-requests/).

Your pull requests will be reviewed. Please create an issue about your future pull
request that others know that you are working on it and to avoid dublicate effort.
Once the pull requests are approved and pass continuous integration checks, the
pull requests will be merged. Please squash all commits in a pull request into a
single commit. For those just getting started, there is a
[section "Git tools - Rewiting history" in the git docs](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).

If you want to contribute but you're not sure where to start, take a look at the
[issues with the "contributions welcome" label](https://github.com/fkromer/rospbt/labels/stat%3Acontributions%20welcome). These are issues that are particularly well suited for outside contributions,
often because already existing code inspires how to implement the issue. If you
decide to start on an issue, leave a comment so that other people know that
you're working on it. If you want to help out, but not alone, use the issue
comment thread to coordinate.

### Contribution guidelines and standards

Before sending your pull request for [review](https://github.com/fkromer/rospbt/pulls),
make sure your changes are consistent with the guidelines and follow the
`rospbt` coding style.

#### General guidelines and philosophy for contribution

#### Bug fixes

Bug fixes for other code than Hypothesis strategies also generally require unit
tests.

#### Testing

There are no best practices for testing custom Hypothesis strategies
[(hypothesis developer answer on stackoverflow](https://stackoverflow.com/a/49683721/5308983).
(Due to the nature of strategies it makes not sense as well.) For everything else:
Please provide tests to (a) prove that your code works correctly, and b) guard
against future breaking changes. Please use `pytest` as test framework/runner.
In case you want pull request "property based tests" please use `Hypothesis`.

#### Versioning

`rospbt` uses [Semantic Versioning 2.0.0](https://semver.org/) for releases.
Keep API compatibility in mind when you add, change or remove features. If you
create pull requests please provide a note how it impacts versioning after merge.

For information about the compatibility of semantic versioning with the Python
PEP specification refer to
[PEP 440 -- Version Identification and Dependency Specification (Semantic versioning)](https://www.python.org/dev/peps/pep-0440/#id48].

#### License

Do not include any license other than MIT. Adding a new license should not be
required anyway (because already existing).

#### Python coding style

Changes to `rospbt` code should conform to
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
BUT: For the docstring style guide refer to the section below.

#### Python docstring style

Docstring documentation should be written according to NumPy style guide. For
those just getting started, there is a section
["Example NumPy Style Python Docstrings" (Sphinx documentation)](http://www.sphinx-doc.org/en/master/ext/example_numpy.html) and
["A Guide to NumPy/SciPy Documentation" (NumPy on GitHub)](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt).

#### Running pre-release checks

Please run the following [`tox`](https://github.com/tox-dev/tox) environments before
creating a pull request:

- `lint`: Static analysis with `pylint`
- `code_style`: Code style checks.
- `docs_style`: Docstring style checks.
- `docs`: Sphinx documentation integrity checks. (The cocumentation resides in `/.tox/docs/tmp/html`.)


    tox -e lint
    tox -e code_style
    tox -e docs_style
    tox -e docs

In case you add tests feel free to add a new environment `[testenv:test]` to `tox.ini`.
