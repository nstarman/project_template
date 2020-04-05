{{ '*' * "%s.data"|format(cookiecutter.package_name)|length() }}
{{ cookiecutter.package_name }}.data
{{ '*' * "%s.data"|format(cookiecutter.package_name)|length() }}

This is the documentation for {{ cookiecutter.package_name }}.data.

Reference/API
=============

.. automodapi:: {{ cookiecutter.module_name }}.data
