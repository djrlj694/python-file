#!/usr/bin/make -f
# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: Docker.mk
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To facilitate Docker software project activities.
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


# Speed up builds (docker-compose >= 1.25).
export COMPOSE_DOCKER_CLI_BUILD=0
export DOCKER_BUILDKIT=0


# =========================================================================== #
# PHONY TARGETS
# =========================================================================== #


# -- Docker Targets -- #

.PHONY: docker-build docker-down docker-logs docker-test docker-up

# Rebuilds a Docker service’s Dockerfile or the contents of its build
# directory if it is changed.
docker-build:
	@docker-compose build

# Stops Docker containers & removes containers, networks, volumes, & images
# created by `docker-compose up`.
docker-down:
	@docker-compose down --remove-orphans

# Displays log output from Docker services.
docker-logs:
	@docker-compose logs app | tail -100

# Builds, (re)creates, starts, & attaches to Docker containers for a Docker
# service.
docker-up:
	@docker-compose up -d app
