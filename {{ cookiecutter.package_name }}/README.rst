{{ cookiecutter.short_description }}
{{ '-' * cookiecutter.short_description|length }}

.. container::

   |astropy| |Build Status| |License| |Code style: black|

Documentation
-------------

|Documentation Status| 

The documentation for ``{{ cookiecutter.package_name }}`` is hosted on `Read the docs <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest>`_.

The `wiki <https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.package_name }}/wiki>`_ has miscellaneous coding / science tips and tricks.


Installation and Dependencies
-----------------------------

|PyPI|


The easiest way to get Gala is to install with pip. To install with pip::

    pip install {{ cookiecutter.package_name }}

See the `installation instructions <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/>`_ in the `documentation <https://readthedocs.org/projects/{{ cookiecutter.package_name }}/>`_ for more information.


Attribution
-----------

Example |DOI|

If you make use of this code, please consider citing the Zenodo DOI |DOI| as a software citation::

   @software{{{ cookiecutter.package_name }}:zenodo,
     author       = {{{ cookiecutter.author_name }}},
     title        = {{{ cookiecutter.package_name }} v1.0},
     month        = mar,
     year         = 2020,
     publisher    = {Zenodo},
     doi          = {10.5281/zenodo.3724822},
     url          = {https://doi.org/10.5281/zenodo.3724822}
   }

License
-------

|License|

Copyright 2018- {{ cookiecutter.author_name }} and contributors.

``{{ cookiecutter.package_name }}`` is free software made available under the BSD-3 License. For details see the `LICENSE <https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.package_name }}/blob/master/LICENSE>`_ file.



.. |astropy| image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :target: http://www.astropy.org/
.. |Build Status| image:: https://travis-ci.org/{{ cookiecutter.author_name }}/{{ cookiecutter.package_name }}.svg?branch=master
   :target: https://travis-ci.org/{{ cookiecutter.author_name }}/{{ cookiecutter.package_name }}
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Documentation Status| image:: https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest
   :target: https://{{ cookiecutter.package_name }}.readthedocs.io/en/latest/?badge=latest
.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3545178.svg
   :target: https://doi.org/10.5281/zenodo.3545178
.. |License| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause
.. |PyPI| image:: https://badge.fury.io/py/{{ cookiecutter.package_name }}.svg
   :target: https://badge.fury.io/py/{{ cookiecutter.package_name }}