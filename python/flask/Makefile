# Makefile for flask

# .RECIPEPREFIX =
# Global variables
NAME = flaskr

# First target is default.
.PHONY: help
help:
# @echo prints inside quotes only.
# @echo "Usage: $ make <target> [NAME=${NAME}]"

	@echo " > style  : check PEP8 on flask project ${NAME}"
	@echo " > run    : run flask project ${NAME}"
	@echo " > test   : test flask project ${NAME}"

.PHONY: style
style:
	flake8 ${NAME}

# lint:
#	pylint --max-line-length=120 pypi_portal

# test:
# 	py.test --cov-report term-missing --cov pypi_portal tests

# testpdb:
# 	py.test --pdb tests

# Not sure if this works
.PHONY: run
run:
	set FLASK_APP=${NAME}
	set FLASK_ENV=development
	flask run
	python ${NAME}/cli.py run
