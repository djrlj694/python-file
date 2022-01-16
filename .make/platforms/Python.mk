#!/usr/bin/make -f
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
# REVISED: Jan 15, 2022
# =========================================================================== #


# =========================================================================== #
# PHONY TARGETS
# =========================================================================== #


# -- Python Targets -- #

.PHONY: python-clean python-dist python-install python-release

# Removes all Python artifacts.
python-clean: python-clean-build python-clean-pyc python-clean-test

# Builds Python source & wheel package.
python-dist: clean
	@python setup.py sdist
	@python setup.py bdist_wheel
	@ls -l dist

# Install the Python package to the active Python's site-packages.
python-install: clean
	@python setup.py install

# Packages & uploads a Python release.
python-release: dist
	@twine upload dist/*

# -- Prerequisites for "python-clean" Target -- #

.PHONY: python-clean-build python-clean-pyc python-clean-test

# Removes Python build artifacts.
python-clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

# Removes Python file artifacts.
python-clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.mypy_cache' -exec rm -rf {} +

# Removes Python test and coverage artifacts
python-clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache
