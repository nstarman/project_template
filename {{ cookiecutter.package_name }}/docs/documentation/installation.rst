.. _{{ cookiecutter.module_name }}-installation:

============
Installation
============

|Code Size|

**********
With `pip`
**********

.. container::

	|PyPI| |PyPI Format|

The easiest way to get *{{ cookiecutter.module_name }}* is to install with `pip <https://pypi.org/project/{{ cookiecutter.module_name }}/>`_. To install with pip::

    pip install {{ cookiecutter.module_name }}


***********
From source
***********

To install the latest version, or from a branch, *{{ cookiecutter.package_name }}* can be installed from `source <https://github.com/{{ cookiecutter.github_project }}.git>`_.

From the command line.
::

	cd folder/in/which/to/install

	git clone https://github.com/cwru-pat/{{ cookiecutter.package_name }}.git

	cd {{ cookiecutter.package_name }}

	python setup.py install




.. |PyPI| image:: https://badge.fury.io/py/{{ cookiecutter.module_name }}.svg
   :target: https://badge.fury.io/py/{{ cookiecutter.module_name }}

.. |PyPI Format| image:: https://img.shields.io/pypi/format/{{ cookiecutter.module_name }}?style=flat
   :alt: PyPI - Format

.. |Code Size| image:: https://img.shields.io/github/languages/code-size/{{ cookiecutter.author_name }}/{{ cookiecutter.module_name }}?style=flat
   :alt: GitHub code size in bytes