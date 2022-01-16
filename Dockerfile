# syntax=docker/dockerfile:1

# REFERENCES:
# 1. https://github.com/cosmicpython/code/tree/appendix_project_structure
# 2. https://github.com/mrako/python-example-project

FROM python:3.9-slim-buster

# RUN apt install gcc libpq (no longer needed bc we use psycopg2-binary)

# Create app directory.
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source.
COPY . /usr/src/app
