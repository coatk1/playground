Run the following from the top-level directory.

::

    python project/app.py

Check Code
==========

::

    flake8 --filename=*.py --ignore=E501,F401 --statistics project/

Clean Code
----------

::

    yapf --in-place --recursive --style="facebook" project/

Check Docs
==========

::

    pydocstyle --convention=numpy project/

Test Code
=========

::

    pytest -v --cov-config=setup.cfg --cov=package --cov-report=term-missing test/
