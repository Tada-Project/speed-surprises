# Speed-Surprises

[![Build Status](https://api.travis-ci.org/Tada-Project/speed-surprises.svg?branch=master)](https://travis-ci.org/Tada-Project/speed-surprises) [![codecov.io](http://codecov.io/github/Tada-Project/speed-surprises/coverage.svg?branch=master)](http://codecov.io/github/Tada-Project/speed-surprises?branch=master) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

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
- `pipenv run pytest`

Note that the provided tests suites automatically generate test data using
[Hypothesis](https://hypothesis.works/). Also, the provided test suites run
benchmarks using
[pytest-benchmark](https://github.com/ionelmc/pytest-benchmark).

If you want to exclude the test cases that run a pytest-benchmark you can type:

- `pipenv run pytest -m "not benchmark"`

If you want to exclude the test cases that use Hypothesis you can type:

- `pipenv run pytest -m "not hypothesisworks"`

## Running Experiment with Speed-Surprises and Shell Script

Although you can certainly run experiments on any single function in
Speed-Surprises, we also provide you a [sample script](https://github.com/Tada-Project/speed-surprises/blob/master/speedsurprises/script/sort_experiment.sh)
that will allow you to easily run experiments on a set of functions with
different combinations of parameters.

To give execute permission to the script:

```bash
chmod +x /path/to/script.sh
```

To run the script:

```bash
/path/to/script.sh
```

We recommend you to download both repositories like this:

```
folder/
│
├── tada/
└── speed-surprises/
```

Then, move the script file into `tada` directory. After installing the
dependencies in `tada` successfully, you can type `./sort_experiment.sh` in
the terminal to run the experiment.

## Adding New Functions to the Speed-Surprises

You can follow these steps to add a new function for analysis if you are a
collaborator on the project. If you want to add a new function, please ensure
that it is accompanied by a benchmarking test case, a standard test case that
runs in `pytest`, and a test case that generates data values using Hypothesis.
First, you should type the following command, substituting the name of your
function for the word `functionname`.

- `git checkout -b new-function-functioname`
- `git checkout master`
- `git push -u origin new-function-functioname`

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. This pull request should describe the new function
that you are adding and, if possible, what you think is its worst-case time
complexity. Following the examples for the existing functions (e.g.,
`compute_factorial` in `speedsurpries.numbers` and `mcopies_of` in
`speedsurpisese.text`), your function should be accompanied by a test suite
written in the Pytest testing. In the case that you are not the original creator
of the submitted function, please ensure that you have permission to include it
in this repository and cite its source. Of course, if you are not a collaborator
on this project, then you will need to fork the repository, add your new
function, document and test it as required, and then create a pull request.

## Problems or Praise

If you have any problems with installing or using the test suite provided for
these functions, then please create an issue associated with this Git repository
using the "Issues" link at the top of this site. The contributors to
Speed-Surprises will do all that they can to resolve your issue and ensure that
all of the functions and test suites work well in your development environment.
