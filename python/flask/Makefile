# Makefile for flask

# .RECIPEPREFIX =

# Put it first so that "make" without argument is like "make help".
.PHONY: help
help:
	@echo "Usage: $ make <target> [NAME=Flaskproject]"
	@echo " > create    : create flask project ${NAME}"
	@echo " > destroy   : destroy flask project ${NAME}"
	@echo " > deps      : install dependentcies via pip"

# .PHONY: style
# style:
# 	flake8 flaskr

# lint:
	# pylint --max-line-length=120 pypi_portal

# test:
	# py.test --cov-report term-missing --cov pypi_portal tests

# testpdb:
	# py.test --pdb tests

.PHONY: run
run:
	set FLASK_APP=flaskr
	set FLASK_ENV=development
	flask run
