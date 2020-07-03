{{ cookiecutter.package_name }}
{{ '=' * cookiecutter.package_name|length }}

.. container::

   |astropy| |Build Status| |License| |Code style: black|


Documentation
-------------

|Documentation Status| 

The documentation for ``{{ cookiecutter.package_name }}`` is hosted on `Read the docs <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest>`_.


Installation and Dependencies
-----------------------------

|PyPI|


The easiest way to get {{ cookiecutter.package_name }} is to install with pip. To install with pip::

    pip install {{ cookiecutter.package_name }}

See the `installation instructions <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/>`_ in the `documentation <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/>`_ for more information.


***********
Attribution
***********

|DOI| |License|

Copyright 2020 - {{author_name}}.

``{{ cookiecutter.package_name }}`` is free software made available under the BSD-3 License. For details see the `LICENSE <https://github.com/{{ github_project }}/blob/master/LICENSE>`_ file.

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


License
-------

|License|

Copyright 2018- {{ cookiecutter.author_name }} and contributors.

``{{ cookiecutter.package_name }}`` is free software made available under the BSD-3 License. For details see the `LICENSE <https://github.com/{{ cookiecutter.github_project }}/blob/master/LICENSE>`_ file.



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
