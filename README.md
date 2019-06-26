# Algonaut Plugins

This repository contains our collection of Algonaut plugins.

## Installing

First, install the required dependencies using pip:

    pip install -r requirements.txt --no-index --find-links wheels

If you want to run tests, please also install test dependencies:

    pip install -r requirements-test.txt --no-index --find-links wheels

The plugins require a working Algonaut installation. To enable plugins, include
their settings directory in `ALGONAUT_SETTINGS_D`.

## Tests

To run tests

    make test

This will run all the tests for all the plugins.

## Upgrading packages

You can use the fabulous `pur` tool to upgrade packages in the requirements files:

    # will update normal requirements
    pur -v -r requirements.txt
    # will update test requirements
    pur -v -r requirements-test.txt

## Building Wheels

We install all packages from local wheels if possible (for security reasons), to
generate these wheels simply use the following commands:

    pip wheel --wheel-dir wheels -r requirements.txt
    pip wheel --wheel-dir wheels -r requirements-test.txt
