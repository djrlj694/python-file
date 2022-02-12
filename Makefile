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
# REVISED: Feb 12, 2022
# =========================================================================== #


# ============================================================================ #
# PHONY TARGETS
# ============================================================================ #


# -- Main Targets -- #

# Force the default target execution sequence to display the online help if no
# target is specified in the command line following "make".
.PHONY: all
all: help

## clean: Completes all cleanup activities.
.PHONY: clean
clean: py-clean

## dist: Completes all distribution activities.
.PHONY: dist
dist: py-dist

## install: Completes all installation activities.
.PHONY: install
install: py-install

## release: Completes all release activities.
.PHONY: release
release: py-release

## test: Completes all test activities.
.PHONY: test
test: test-file


# =========================================================================== #
# SECONDARY MAKEFILES
# =========================================================================== #


-include .make/features/*.mk
-include .make/platforms/*.mk
-include .make/tests/*.mk
