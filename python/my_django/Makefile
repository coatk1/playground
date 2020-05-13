# Makefile for polls

# .RECIPEPREFIX =

# Global variables
NAME          = polls
PYTHON        = python
FLAKE8        = flake8
PYDOCSTYLE    = pydocstyle
PYTEST        = pytest
BANDIT        = bandit
SDIST         = sdist
BDIST         = bdist_wheel
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs/source
BUILDDIR      = docs/build

# ANSI Colors
# https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
#BLUE          = \e[1;34m
#BACK          = $<\e[0m
BLUE          = \033[1;36m
RED           = \033[1;31m
YELLOW        = \033[1;33m
BACK          = \033[0m

# User-friendly check for sphinx-build
# ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
# 	$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don\'t have Sphinx installed, grab it from http://sphinx-doc.org/)
# endif

# First target is default.
.PHONY: help
help:
# @echo prints inside quotes only.
#@echo -e "$(RED)error $(BACK)"
#@echo -e "$(YELLOW)warning $(BACK)"
	@echo ""
	@echo -e "Usage: make $(BLUE)target $(BACK) where $(BLUE)target $(BACK) is one of the following:"
	@echo -e "$(BLUE)help $(BACK)                     : help for make commands $(NAME)"
	@echo ""
	@echo "Check code and docstrings"
	@echo -e "$(BLUE)style $(BACK)                    : check PEP8 on project $(NAME)"
	@echo -e "$(BLUE)docstyle $(BACK)                 : check PEP257 on project $(NAME)"
	@echo ""
	@echo "Run, test and check code"
	@echo -e "$(BLUE)run $(BACK)                      : run project $(NAME)"
	@echo -e "$(BLUE)test $(BACK)                     : test project $(NAME)"
	@echo -e "$(BLUE)security $(BACK)                 : run bandit on project $(NAME)"
	@echo ""
	@echo "Build"
	@echo -e "$(BLUE)build_dist $(BACK)               : build source distribution for project $(NAME)"
	@echo -e "$(BLUE)build_wheel $(BACK)              : build source wheel for project $(NAME)"
	@echo -e "$(BLUE)sphinx_help $(BACK)              : help for $(SPHINXBUILD)"
	@echo -e "$(BLUE)sphinx $(BACK)                   : build sphinx docs for project $(NAME)"

# @VARIABLE gets rid of displaying command in command line.

# Check code and docstrings
.PHONY: style
style:
	@$(FLAKE8) --statistics $(NAME)/

.PHONY: docstyle
docstyle:
	@$(PYDOCSTYLE) $(NAME)/

# Run, test, check code
.PHONY: run
run:
	@$(PYTHON) $(NAME)/cli.py run

.PHONY: test
test:
# pytest -v --cov-config=setup.cfg --cov=$(NAME) --cov-report=term-missing test/
	@$(PYTEST)

.PHONY: security
security:
	@$(BANDIT) --recursive --verbose --exclude $(NAME)/_version.py --skip=B101 $(NAME)/ test/

# Build
.PHONY: build_dist
build_dist:
	$(PYTHON) setup.py $(SDIST)

.PHONY: build_wheel
build_wheel:
	$(PYTHON) setup.py $(BDIST)

.PHONY: sphinx_help
sphinx_help:

	@$(SPHINXBUILD) -M help $(SOURCEDIR) $(BUILDDIR)

.PHONY: sphinx
sphinx:
	@$(SPHINXBUILD) -v $(SOURCEDIR) $(BUILDDIR)

# Catch all other targets not listed and re-route to help target.
%:
	@$(MAKE) help
