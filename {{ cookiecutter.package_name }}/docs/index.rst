{{ '#' * "`%s` Documentation"|format(cookiecutter.package_name)|length() }}
`{{ cookiecutter.package_name }}` Documentation
{{ '#' * "`%s` Documentation"|format(cookiecutter.package_name)|length() }}

This is the documentation for {{ cookiecutter.package_name }}.

The package is being actively developed in a `public repository on GitHub <https://github.com/{{ cookiecutter.github_project }}>`_ so if you have any trouble, `open an issue <https://github.com/{{ cookiecutter.github_project }}/issues>`_ there.

.. image:: https://travis-ci.org/{{ cookiecutter.github_project }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_project }}


*************
Documentation
*************

.. toctree::
  :maxdepth: 1

  {{ cookiecutter.module_name }}/index.rst
  documentation/testing.rst


***********
Subpackages
***********

.. toctree::
   :maxdepth: 1

   {{ cookiecutter.module_name }}/data/index


*****************
How to contribute
*****************

We welcome contributions from anyone via pull requests on `GitHub
<https://github.com/{{ cookiecutter.github_project }}>`_. If you don't feel comfortable modifying or
adding functionality, we also welcome feature requests and bug reports as
`GitHub issues <https://github.com/{{ cookiecutter.github_project }}/issues>`_.


***********
Attribution
***********

|DOI|

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


***************
Project details
***************

.. toctree::
   :maxdepth: 1

   credits
   whatsnew/index.rst
