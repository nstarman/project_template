# -*- coding: utf-8 -*-

"""Initiation Tests for `~{{ cookiecutter.module_name }}`."""

__all__ = [
    "test_has_version",
]


##############################################################################
# IMPORTS

# BUILT-IN

import importlib

# THIRD PARTY

# PROJECT-SPECIFIC


##############################################################################
# PARAMETERS


##############################################################################
# TESTS
##############################################################################


def test_has_version():
    """The most basic test."""
    module = importlib.import_module("{{ cookiecutter.module_name }}")

    assert hasattr(module, "__version__"), "No version!"


# /def


# -------------------------------------------------------------------


##############################################################################
# END
