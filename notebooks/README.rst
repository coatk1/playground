========
Commands
========

.. contents::

Code Commands
=============

Run the following from the top-level directory.

.. code-block::bash

    python project/app.py

Check Code
----------

.. code-block::bash

    flake8 --filename=*.py --ignore=E501,F401 --statistics project/

Clean Code
++++++++++

.. code-block::bash

    yapf --in-place --recursive --style="facebook" project/

Check Docs
----------

::

    pydocstyle --convention=numpy project/

Test Code
---------

::

    pytest -v --cov-config=setup.cfg --cov=package --cov-report=term-missing test/

Sphinx
------

::

    sphinx-build -v source build

Linux
=====

* https://unix.stackexchange.com/questions/37329/efficiently-delete-large-directory-containing-thousands-of-files

::

  mkdir empty_dir
  rsync -a --delete empty_dir/    yourdirectory/

