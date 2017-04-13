.PHONY: image \
	clean clean-pyc clean-build \
	test test-tox \
	bump/major bump/minor bump/patch \
	release

PYCHEMY_HOME ?= /usr/src/pychemy
SETUP = python setup.py

all: test-tox

clean: clean-build clean-pyc

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	python setup.py nosetests

test-tox:
	tox

bump/major bump/minor bump/patch:
	bumpversion --verbose $(@F)


release: clean sdist bdist_wheel
	twine upload dist/*

sdist:
	${SETUP} sdist
	ls -l dist

bdist_wheel:
	${SETUP} bdist_wheel
	ls -l dist

MAKE_EXT = docker-compose run --rm pychemy make -C ${PYCHEMY_HOME}

# Generically execute make targets from outside the Docker container
%-ext: image
	${MAKE_EXT} $*

# Build the image
image:
	GIT_USER_NAME=`git config user.name` GIT_USER_EMAIL=`git config user.email` docker-compose build --pull
