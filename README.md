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

## Adding New Functions to the Speed-Surprises

You can follow these steps to add a new function for analysis if you are a
collaborator on the project. If you want to add a new function, please ensure
that it is accompanied by a benchmarking test case, a standard test case that
runs in `pytest`, and a test case that generates data values using Hypothesis.
First, you should type the following command, substituting the name of your
function for the word `functionname`.

- `git checkout -b new-function-functioname`
- `git checkout master`
- `git push origin new-function-functioname`

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. If you are not a collaborator on this project,
then you will need to fork the repository, add your new function, and then
create a pull request.

## Problems or Praise

If you have any problems with installing or using the test suite provided for
these functions, then please create an issue associated with this Git repository
using the "Issues" link at the top of this site. The contributors to
Speed-Surprises will do all that they can to resolve your issue and ensure that
all of the functions and test suites work well in your development environment.
