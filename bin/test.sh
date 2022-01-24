#!/bin/bash
# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: test.sh
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To run Python test suites.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 16, 2022
# REVISED: Jan 23, 2022
# =========================================================================== #


# =========================================================================== #
# SETUP
# =========================================================================== #


# Path to this script's project root
PREFIX="$(dirname $(dirname $0))"

# Sourced Bash objects
. "${PREFIX}/src/bash/sources.sh"


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# Run a Python package as if it were a Python script.
__python -m unittest discover ${VERBOSEOPT} tests "*_test.py"
