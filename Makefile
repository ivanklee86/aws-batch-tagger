SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = builderporo

#-----------------------------------------------------------------------
# Rules of Rules : Grouped rules that _doathing_
#-----------------------------------------------------------------------

test: lint pytest

install: clean install-package

build: clean generate-requirements build-package upload

build-local: clean build-package

#-----------------------------------------------------------------------
# Testing & Linting
#-----------------------------------------------------------------------

lint:
	pylint ${PROJECT_NAME} && \
	mypy ${PROJECT_NAME};

pytest:
	export PYTHONPATH=${ROOT_DIR}:$$PYTHONPATH && \
	py.test --cov ${PROJECT_NAME} tests

#-----------------------------------------------------------------------
# Distribution
#-----------------------------------------------------------------------
clean:
	rm -rf build && \
	rm -rf dist && \
	rm -rf ${PROJECT_NAME}/local_config.py && \
	rm -rf ${PROJECT_NAME}.egg-info && \
	pip uninstall -y ${PROJECT_NAME};

install-package:
	poetry install

build-package:
	poetry build

upload:
	poetry publish -r pypiserver
