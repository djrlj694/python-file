# syntax=docker/dockerfile:1
# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: Dockerfile
# PROJECT: File
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To define Docker images for testing File, both its nstallation and
#   operation as a Python package.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 15, 2022
# REVISED: Jan 30, 2022
#
# REFERENCES:
# - https://docs.docker.com/engine/reference/builder/
# =========================================================================== #


# =========================================================================== #
# BUILDER IMAGE
# =========================================================================== #


# Use Ubuntu (LTS) as the operation system.
FROM ubuntu:20.04 AS builder-image

# Avoid a stuck build due to a user prompt.
ARG DEBIAN_FRONTEND=noninteractive

# Install the toolchain.
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel \
        build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create & activate a Python virtual environment.
# Use the final directory name to avoid path issues with Python packages.
RUN python3.9 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

# Install the Python package's requirements.
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt


# =========================================================================== #
# RUNNER IMAGE
# =========================================================================== #


# Use Ubuntu (LTS) for the "runner" image.
FROM ubuntu:20.04 AS runner-image

# Install the toolchain.
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        make \
        python3.9 python3-venv && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a user for testing.
RUN useradd --create-home myuser

# Install the Python virtual environment.
COPY --from=builder-image /home/myuser/venv /home/myuser/venv

# Create a directory for developing/testing the software project.
USER myuser
RUN mkdir /home/myuser/python-file
WORKDIR /home/myuser/python-file

# Bundle the Python package.
COPY . .

# Ensure all messages always reach the console.
ENV PYTHONUNBUFFERED=1

# Set Python virtualenv environment variables.
# This is equivalent to running source /env/bin/activate, & it ensures:
# 1. The application is executed within the context of the virtualenv;
# 2. It will have access to its dependencies.
# Note that the final directory name avoids path issues w/ Python packages.
ENV VIRTUAL_ENV=/home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"
