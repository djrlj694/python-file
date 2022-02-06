# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: Makefile
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To support the phases of software project development leading to
#   production-quality releases.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 15, 2022
# REVISED: Feb 06, 2022
# =========================================================================== #


# ============================================================================ #
# PHONY TARGETS
# ============================================================================ #


# -- Main Targets -- #

.PHONY: all clean dist install release test

# Force the default target execution sequence to display the online help if no
# target is specified in the command line following "make".
all: help

## clean: Completes all cleanup activities.
clean: python-clean

## dist: Completes all distribution activities.
dist: python-dist

## install: Completes all installation activities.
install: python-install

## release: Completes all release activities.
release: python-release

## test: Completes all test activities.
test: test-file


# =========================================================================== #
# SECONDARY MAKEFILES
# =========================================================================== #


-include .make/features/*.mk
-include .make/platforms/*.mk
-include .make/tests/*.mk
