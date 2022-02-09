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
# REVISED: Feb 08, 2022
# =========================================================================== #


# =========================================================================== #
# PHONY TARGETS
# =========================================================================== #


# -- Python Targets -- #

.PHONY: py-clean py-dist py-install py-release

# Removes all Python artifacts.
py-clean: py-clean-build py-clean-pyc py-clean-test

# Builds Python source & wheel package.
py-dist: py-clean
	@python setup.py sdist
	@python setup.py bdist_wheel
	@ls -l dist

# Install the Python package to the active Python's site-packages.
py-install: py-clean
	@python setup.py install

# Packages & uploads a Python release.
py-release: py-dist
	@twine upload dist/*

# -- Prerequisites for "py-clean" Target -- #

.PHONY: py-clean-build py-clean-pyc py-clean-test

# Removes Python build artifacts.
py-clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

# Removes Python file artifacts.
py-clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.mypy_cache' -exec rm -fr {} +

# Removes Python test and coverage artifacts.
py-clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache
