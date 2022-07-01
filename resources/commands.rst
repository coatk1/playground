========
Commands
========

.. contents::

Linux
=====

* https://unix.stackexchange.com/questions/37329/efficiently-delete-large-directory-containing-thousands-of-files

::

  mkdir empty_dir
  rsync -a --delete empty_dir/    yourdirectory/
