.. {{cookiecutter.module_name}}-module-index

{{ '*' * "%s on import"|format(cookiecutter.package_name)|length() }}
{{ cookiecutter.package_name }} Documentation
{{ '*' * "%s on import"|format(cookiecutter.package_name)|length() }}

This is the documentation for the import-level namespace of {{ cookiecutter.package_name }}.

Reference/API
=============

.. automodapi:: {{ cookiecutter.module_name }}


Subpackages
===========

.. toctree::
   :maxdepth: 1

   data/index