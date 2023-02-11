================
List of Commands
================

.. contents::

Code Commands
=============
Run the following from the top-level directory.

.. code-block:: bash

  python project/app.py

Check code

.. code-block:: bash

  flake8 --filename=*.py --ignore=E501,F401 --statistics project/

Clean code

.. code-block:: bash

  yapf --in-place --recursive --style="facebook" project/

Check docs

.. code-block:: bash

  pydocstyle --convention=numpy project/

Test code

.. code-block:: bash

  pytest -v --cov-config=setup.cfg --cov=package --cov-report=term-missing test/

Sphinx

.. code-block:: bash

  sphinx-build -v source build

Linux
=====
* https://unix.stackexchange.com/questions/37329/efficiently-delete-large-directory-containing-thousands-of-files

.. code-block:: bash

  mkdir empty_dir
  rsync -a --delete empty_dir/ yourdirectory/

Disk space check in linux

.. code-block:: bash

  df -H

Anaconda
========
Removes any packages not being used and do not have links (links point to anaconda environments) as well as caches.

.. code-block:: bash

  conda clean --all

Jupyter
=======
Jupyter nbconvert

.. code-block:: bash

  jupyter nbconvert file.ipynb --to file.py

Jupyter nb extension Black (enable/disable)

.. code-block:: bash

  jupyter nbextension enable jupyter-black/jupyter-black

.. code-block:: bash

  jupyter nbextension disbable jupyter-black/jupyter-black

Convert .py to .ipynb

.. code-block:: bash

  """Create a notebook containing code from a python script.
  Run as: python make_nb.py my_script.py
  """

  import sys
  import nbformat
  from nbformat.v4 import new_notebook, new_code_cell

  nb = new_notebook()

  with open(sys.argv[1]) as f:
    code = f.read()

  nb.cells.append(new_code_cell(code))
  nbformat.write(nb, sys.argv[1]+'.ipynb')

Open notebook under a different ip address and port

.. code-block:: bash

  jupyter notebook --ip=127.0.0.1 --port 8888

Openssl
=======

Convert PKCS#12 (.pfx, .p12) to PEM (.pem)
------------------------------------------

.. code-block:: bash

  openssl pkcs12 -in cert.p12 -out cert.pem -passin pass:pw -passout pass:pw -clcerts (for encrypted pem)

Convert PKCS#12 (.pfx, .p12) to CER (.cer)
------------------------------------------

.. code-block:: bash

  openssl pkcs12 -in cert.p12 -clcerts -nokeys -out cert.cer

Convert PKCS#12 (.pfx, .p12) to KEY (.key)
------------------------------------------

.. code-block:: bash

  openssl pkcs12 -in cert.p12 -nocerts -out cert.key -nodes (for unencrypted private key)

Others
------

.. code-block:: bash

  openssl x509 -subject -dates -noout -in file.crt
  keytool -printcert -file cert.pem

Git
===
Get feature branch in origin repo

.. code-block:: bash

  git checkout origin/feature

Removing a file with sensitive data
* https://stackoverflow.com/questions/872565/remove-sensitive-files-and-their-commits-from-git-history

This will:

* Force Git to process, but not checkout, the entire history of every branch and tag.
* Remove the specified file, as well as any empty commits generated as a result.
* Overwrite your existing tags.

.. code-block:: bash

  git filter-branch --force --indec-filter "git rm --cached --ignore-unmatch PATH-TO-YOUR-FILE-WITH-SENESITIVE-DATA" --prune-empty --tag-name-filter cat -- all

Forks
-----
Add forked branches upstream

.. code-block:: bash

  git remote add upstream ...

Check remote streams

.. code-block:: bash

  git remote -v

Pull and merge upstreams

.. code-block:: bash

  git fetch upstream
  git checkout master
  git merge upstream/master

SSH
===
Test ssh

.. code-block:: bash

  python -m SimpleHTTPServer 8000

SSH Key WARNING

.. code-block:: bash

  chmod 400 id_rsa
