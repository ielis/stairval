.. _installation:

=====
Setup
=====

The document describes how to install Stairval into your environment.

Stable release
**************

Installing Stairval is easy - we publish releases on `Python Package Index (PyPi) <https://pypi.org/project/stairval>`_.

Run the following to install the latest *stable* release::

  python3 -m pip install stairval


Latest release
**************

The *latest* release can be installed by cloning the GitHub repository::

  git clone https://github.com/ielis/stairval.git
  cd stairval

  # Switch to `develop` branch to access the latest features
  git checkout develop

  python3 -m pip install .

The code above will clone the source code from GitHub repository, switch to the `develop` branch with the latest features,
and install the library into the current Python (virtual) environment.


Run tests
^^^^^^^^^

Running tests can be done as an optional step after installation. However, some additional
libraries are required to run tests, hence we must do one more install, this time with `test` option enabled::

  python3 -m pip install .[test]

Then, running the tests is as simple as::

  pytest

That's all about testing!
