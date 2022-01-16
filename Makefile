#!/usr/bin/make -f
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
# REVISED: Jan 15, 2022
# =========================================================================== #


# =========================================================================== #
# DEFAULT CONSTANTS
# =========================================================================== #


# -- Make -- #

# Name of the main makefile
MAKEFILE ?= $(firstword $(MAKEFILE_LIST))

# Path of the directory containing the main makefile
MAKEFILE_DIR ?= $(dir $(realpath $(MAKEFILE)))

# Path of the directory containing secondary makefiles
MAKE_DIR ?= $(MAKEFILE_DIR).make/


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


# -- Feature Dependencies -- #

-include $(MAKE_DIR)features/formatting.mk
-include $(MAKE_DIR)features/helping.mk

# -- Platform Dependencies -- #

-include $(MAKE_DIR)platforms/Docker.mk
-include $(MAKE_DIR)platforms/Python.mk

# -- Test Dependencies -- #

-include $(MAKE_DIR)tests/file.mk
