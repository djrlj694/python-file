# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: Python.mk
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To facilitate Python software project activities.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 15, 2022
# REVISED: Feb 12, 2022
# =========================================================================== #


# =========================================================================== #
# CONDITIONAL VARIABLES
# =========================================================================== #


# Python virtual environment directory
VENV ?= .venv


# =========================================================================== #
# SIMPLY EXPANDED VARIABLES
# =========================================================================== #


# PATH version of `python3` command
PYTHON := $(shell command -v python3 2> /dev/null)

# Python virtual environment version of the `activate` command
VACTIVATE := $(VENV)/bin/activate

# Python virtual environment version of the `python` command
VPYTHON := $(VENV)/bin/python

# Python virtual environment version of the `pip` command
VPIP := $(VENV)/bin/pip


# =========================================================================== #
# PHONY TARGETS
# =========================================================================== #


# -- Python Targets -- #

# Checks to see if Python is available from the PATH.
.PHONY: py-check
py-check:
	@if [ -z $(PYTHON) ]; then \
		echo "'python3' could not be found."; \
		echo "See https://docs.python.org/3/."; \
		exit 2; \
	fi

# Removes all Python artifacts.
.PHONY: py-clean
py-clean: py-clean-build py-clean-pyc py-clean-test

# Builds Python source & wheel package.
.PHONY: py-dist
py-dist: py-clean
	@python setup.py sdist
	@python setup.py bdist_wheel
	@ls -l dist

# Install the Python package to the active Python's site-packages.
.PHONY: py-install
py-install: py-clean
	@python setup.py install

# Packages & uploads a Python release.
.PHONY: py-release
py-release: py-dist
	@twine upload dist/*

# Sets up a Python package installation via pip.
.PHONY: py-setup
py-setup: requirements.txt
	@pip install -r requirements.txt

# Tests a Python package in a Python virtual environment.
.PHONY: py-test
py-test: $(VACTIVATE)
	@$(VPYTHON) -m unittest discover tests

# -- Prerequisites for "py-clean" Target -- #

# Removes Python build artifacts.
.PHONY: py-clean-build
py-clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

# Removes Python file artifacts.
.PHONY: py-clean-pyc
py-clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.mypy_cache' -exec rm -fr {} +

# Removes Python test and coverage artifacts.
.PHONY: py-clean-test
py-clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache

# Removes Python virtual environment artifacts.
.PHONY: py-clean-venv
py-clean-venv:
	@rm -fr $(VENV)


# =========================================================================== #
# NON-PHONY TARGETS
# =========================================================================== #


$(VACTIVATE): $(VPIP) requirements.txt
	@$(VPIP) install -r requirements.txt

$(VPIP): $(VPYTHON)

$(VPYTHON): py-check
	$(PYTHON) -m venv $(VENV)
