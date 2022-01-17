# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: sources.sh
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To source Bash objects.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 16, 2022
# REVISED: Jan 16, 2022
# =========================================================================== #


# =========================================================================== #
# SOURCES
# =========================================================================== #


# -- Optional -- #

# Settings & secrets
[ -f "${PREFIX}/.env" ] && . "${PREFIX}/.env"

# -- Required -- #

# Utilities
. "${PREFIX}/src/bash/variables.env"
. "${PREFIX}/src/bash/functions.sh"
