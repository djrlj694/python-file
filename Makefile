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


# =========================================================================== #
# MACROS
# =========================================================================== #


# -- Help Strings -- #

# `Targets` section header of the `make` command's online help.
define targets_help
  $(FG_CYAN)clean$(RESET)    Completes all cleanup activities.
  $(FG_CYAN)dist$(RESET)     Completes all distribution activities.
  $(FG_CYAN)help$(RESET)     Shows the `make` command's online help.
  $(FG_CYAN)install$(RESET)  Completes all installation activities.
  $(FG_CYAN)release$(RESET)  Completes all release activities.
  $(FG_CYAN)test$(RESET)     Completes all test activities.

endef
export targets_help

# `Usage` section of the `make` command's online help.
define usage_help
make [$(FG_CYAN)options$(RESET)] [$(FG_CYAN)target$(RESET)]

endef
export usage_help


# ============================================================================ #
# PHONY TARGETS
# ============================================================================ #


# -- Main Targets -- #

# Force the default target execution sequence to display the online help if no
# target is specified in the command line following the `make` command.
.PHONY: all
all: help

# Completes all cleanup activities.
.PHONY: clean
clean: py-clean

# Completes all distribution activities.
.PHONY: dist
dist: py-dist

# Shows the `make` command's online help.
.PHONY: help
help:
	@printf "Usage: $$usage_help"
	@echo "Target:"
	@printf "$$targets_help"

# Completes all installation activities.
.PHONY: install
install: py-install

# Completes all release activities.
.PHONY: release
release: py-release

# Completes all test activities.
.PHONY: test
test: test-file


# =========================================================================== #
# SECONDARY MAKEFILES
# =========================================================================== #


-include .make/features/*.mk
-include .make/platforms/*.mk
-include .make/tests/*.mk
