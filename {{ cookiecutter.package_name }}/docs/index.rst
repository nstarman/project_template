{{ '#' * "`%s` Documentation"|format(cookiecutter.package_name)|length() }}
`{{ cookiecutter.package_name }}` Documentation
{{ '#' * "`%s` Documentation"|format(cookiecutter.package_name)|length() }}

This is the documentation for {{ cookiecutter.package_name }}.

All code and data is available on a `public repository on GitHub <https://github.com/{{ cookiecutter.github_project }}>`_ so if you have any trouble, `open an issue <https://github.com/{{ cookiecutter.github_project }}/issues>`_ there.

.. container::

    |DOI| |PyPI| |Build Status| |Codecov| |astropy|


.. _index-documentation:

*************
Documentation
*************

.. toctree::
  :maxdepth: 1

  documentation/installation.rst
  {{ cookiecutter.module_name }}/index.rst
  documentation/testing.rst

.. _index-modules:

*******
Modules
*******

.. toctree::
   :maxdepth: 1

   {{ cookiecutter.module_name }}/data/index


.. _index-examples:

********
Examples
********

Document example notebooks here


.. _index-contributing:

*****************
How to contribute
*****************

|Milestones| |Open Issues| |Last Commit|

We welcome contributions from anyone via pull requests on `GitHub
<https://github.com/{{ cookiecutter.github_project }}>`_. If you don't feel comfortable modifying or
adding functionality, we also welcome feature requests and bug reports as
`GitHub issues <https://github.com/{{ cookiecutter.github_project }}/issues>`_.

The development process follows that of the `astropy-package-template <https://docs.astropy.org/en/latest/development/astropy-package-template.html>`_ from Astropy's `release procedure <https://docs.astropy.org/en/latest/development/releasing.html#release-procedure>`_.


.. _index-attribution:

***********
Attribution
***********

|DOI| |License|

Copyright 2020 - {{cookiecutter.author_name}} and contributors.

``{{ cookiecutter.package_name }}`` is free software made available under the BSD-3 License. For details see the `LICENSE <https://github.com/{{ cookiecutter.github_project }}/blob/master/LICENSE>`_ file.

If you make use of this code, please consider citing the Zenodo DOI as a software citation

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

.. |DOI| replace:: GET FROM ZENODO


.. _index-project_details:

***************
Project details
***************

.. toctree::
   :maxdepth: 1

   credits
   whatsnew/index.rst
   documentation/code_quality


.. |astropy| image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :target: http://www.astropy.org/

.. |Build Status| image:: https://travis-ci.com/{{ cookiecutter.github_project }}.svg?branch=master
    :target: https://travis-ci.com/{{ cookiecutter.github_project }}

.. |Documentation Status| image:: https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest
   :target: https://{{ cookiecutter.package_name }}.readthedocs.io/en/latest/?badge=latest

.. |License| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause

.. |PyPI| image:: https://badge.fury.io/py/{{ cookiecutter.package_name }}.svg
   :target: https://badge.fury.io/py/{{ cookiecutter.package_name }}

.. |Milestones| image:: https://img.shields.io/github/milestones/open/{{ cookiecutter.github_project }}?style=flat
   :alt: GitHub milestones

.. |Open Issues| image:: https://img.shields.io/github/issues-raw/{{ cookiecutter.github_project }}?style=flat
   :alt: GitHub issues

.. |Last Commit| image:: https://img.shields.io/github/last-commit/{{ cookiecutter.github_project }}/master?style=flat
   :alt: GitHub last commit (branch)

.. |Codecov| image:: https://codecov.io/gh/{{ cookiecutter.github_project }}/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/{{ cookiecutter.github_project }}
