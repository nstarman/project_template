{{ cookiecutter.package_name }}
{{ '=' * cookiecutter.package_name|length }}

.. container::

   |astropy| |Build Status| |License| |Code style: black|


Notebooks
---------

Folder contains...

Further notebooks can be found in "docs/examples"


Papers and Presentations
------------------------

Look in folder for paper


CODE
----
The code is included in the ``{{ cookiecutter.module_name }}`` folder.


Documentation
-------------

|Documentation Status| 

The documentation for ``{{ cookiecutter.package_name }}`` is hosted on `Read the docs <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest>`_.


Installation and Dependencies
-----------------------------

|PyPI| |PyPI Format| |Code Size|


The easiest way to get {{ cookiecutter.package_name }} is to install with pip. To install with pip::

    pip install {{ cookiecutter.package_name }}

See the `installation instructions <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/>`_ in the `documentation <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/>`_ for more information.


*****************
How to contribute
*****************

|Milestones| |Open Issues| |Last Commit|

We welcome contributions from anyone via pull requests on `GitHub
<https://github.com/{{ cookiecutter.github_project }}>`_. If you don't feel comfortable modifying or
adding functionality, we also welcome feature requests and bug reports as
`GitHub issues <https://github.com/{{ cookiecutter.github_project }}/issues>`_.

The development process follows that of the `astropy-package-template <https://docs.astropy.org/en/latest/development/astropy-package-template.html>`_ from Astropy's `release procedure <https://docs.astropy.org/en/latest/development/releasing.html#release-procedure>`_.


***********
Attribution
***********

|DOI| |License|

Copyright 2020 - {{cookiecutter.author_name}} and contributors.

``{{ cookiecutter.package_name }}`` is free software made available under the BSD-3 License. For details see the `LICENSE <https://github.com/{{ cookiecutter.github_project }}/blob/master/LICENSE>`_ file.

If you make use of this code, consider citing the Zenodo DOI as a software citation

::

   @software{zenodo,
     author       = {{ cookiecutter.author_name }},
     title        = {{ cookiecutter.package_name }} v1.0,
     month        = month,
     year         = year,
     publisher    = {Zenodo},
     doi          = {},
     url          = {}
   }



.. |astropy| image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :target: http://www.astropy.org/

.. |Build Status| image:: https://travis-ci.org/{{ cookiecutter.github_project }}.svg?branch=master
   :target: https://travis-ci.org/{{ cookiecutter.github_project }}

.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |Documentation Status| image:: https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest
   :target: https://{{ cookiecutter.package_name }}.readthedocs.io/en/latest/?badge=latest

.. |DOI| replace:: GET FROM ZENODO

.. |License| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause

.. |PyPI| image:: https://badge.fury.io/py/{{ cookiecutter.package_name }}.svg
   :target: https://badge.fury.io/py/{{ cookiecutter.package_name }}

.. |PyPI Format| image:: https://img.shields.io/pypi/format/{{ cookiecutter.package_name }}?style=flat
   :alt: PyPI - Format

.. |Code Size| image:: https://img.shields.io/github/languages/code-size/{{ cookiecutter.github_project }}?style=flat
   :alt: GitHub code size in bytes

.. |Milestones| image:: https://img.shields.io/github/milestones/open/{{ cookiecutter.github_project }}?style=flat
   :alt: GitHub milestones

.. |Open Issues| image:: https://img.shields.io/github/issues-raw/{{ cookiecutter.github_project }}?style=flat
   :alt: GitHub issues

.. |Last Commit| image:: https://img.shields.io/github/last-commit/{{ cookiecutter.github_project }}/master?style=flat
   :alt: GitHub last commit (branch)