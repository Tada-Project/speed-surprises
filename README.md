# Speed-Surprises

This repository contains a package of Python 3 modules with functions for
further study in experiments with the "Tada!: auTomAtic orDer-of-growth
Analysis" tool. This documentation provides a brief overview about how to run
the provided test suite in different configurations.

## Installing and Testing Speed-Surprises

This package uses [Pipenv](https://github.com/pypa/pipenv) for installation.
Once you have installed `pipenv` you can run the test suite for the provided
modules and functions by typing the following in your terminal window:

- `pipenv install`
- `pipenv shell`
- `pytest`

Note that the provided tests suites automatically generate test data using
[Hypothesis](https://hypothesis.works/). Also, the provided test suites run
benchmarks using
[pytest-benchmark](https://github.com/ionelmc/pytest-benchmark).

If you want to exclude the test cases that run a pytest-benchmark you can type:

- `pytest -m "not benchmark"`

If you want to exclude the test cases that use Hypothesis you can type:

- `pytest -m "not hypothesisworks"`
