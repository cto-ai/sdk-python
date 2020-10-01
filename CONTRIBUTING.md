# Project Structure and Release Process

## Project Structure

The code is found in the `cto_ai` directory. The three files `sdk.py`,
`ux.py`, and `prompt.py` provide the public API of the SDK. These are
backed by the logic in `daemon_request.py`, which handles the
communication with the daemon when running in a container. This logic
is accessible in true Python fashion but is not intended for public
consumption.

## Release Process

This SDK is published to PyPI under the name `cto_ai`. This allows our
users to install it with `pip install cto_ai`.

The PyPI package is owned by an account named `ctoai`, whose password
is found in the "Shared-DevOps Team - Staging" folder in LastPass. To
make a release, you will need these credentials and also a way to run
the `pypi-release` Op. The source of this Op is at
https://github.com/cto-ai/pypi-release, and the last version Danielle
worked on is public on The Ops Platform as `@danielle/pypi-release`.

To make a release, increment the version number in the `setup.py`
script and commit it to the public repository. Then, invoke the Op and
pass it the Git path of this repository, plus the credentials for the
`ctoai` account. The Op will then build the artifacts and publish them
to PyPI.
