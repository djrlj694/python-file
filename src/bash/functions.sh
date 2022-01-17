# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: functions.sh
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To define Bash functions.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 16, 2022
# REVISED: Jan 16, 2022
# =========================================================================== #


# =========================================================================== #
# FUNCTIONS
# =========================================================================== #


# -- Filesystem -- #

# Renders a template file ($1) with shell variables.
function __render
{
  # Set local variables.
  local -r tmpl=$(cat "${1}")

  # Render template file.
  eval "echo \"${tmpl}\""
}

# -- Python -- #

# Wraps the Python interpreter with shell variables before running a given
# Python script ($1).
function __python
{
  # Run the Python interpreter.
  PREFIX="${PREFIX}" PYTHONPATH="${PYTHONPATH}" ${PYTHON} -B "$@"
}

# Prints the Python path.
function __python_path
{
  # Run the Python interpreter.
  __python -c "import sys; print('\n'.join(sys.path))"
}
