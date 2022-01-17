#!/bin/bash
# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: debug.sh
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To debug Bash variables.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 16, 2022
# REVISED: Jan 16, 2022
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


# Set local variables
declare -r tmpl_dir="${PREFIX}/etc/content"

# Print debugging info.
__render "${tmpl_dir}/debug_set.txt.tmpl"
__render "${tmpl_dir}/debug_standard.txt.tmpl"
__render "${tmpl_dir}/debug_custom.txt.tmpl"
__render "${tmpl_dir}/debug_path.txt.tmpl"
