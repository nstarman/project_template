# -*- coding: utf-8 -*-
# see LICENSE.rst

# ----------------------------------------------------------------------------
#
# TITLE   : {{ cookiecutter.package_name }}
# AUTHOR  : {{ cookiecutter.author_name }}
# PROJECT : {{ cookiecutter.package_name }}
#
# ----------------------------------------------------------------------------

"""{{ cookiecutter.package_name }}.

Routine Listings
----------------

"""

__author__ = "{{ cookiecutter.author_name }}"
# __copyright__ = "Copyright 2018, "
# __credits__ = [""]
# __license__ = ""
# __version__ = "0.0.0"
# __maintainer__ = ""
# __email__ = ""
# __status__ = "Production"

__all__ = [
    # modules
    # functions
]


##############################################################################
# IMPORTS

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._{{ cookiecutter._parent_project }}_init import *   # noqa
# ----------------------------------------------------------------------------

{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import *   # noqa
# Then you can be explicit to control what ends up in the namespace,
# __all__ += ['do_primes']   # noqa
# or you can keep everything from the subpackage with the following instead
# __all__ += example_mod.__all__
{%- endif %}

# PROJECT-SPECIFIC

# modules

# functions

##############################################################################
# END
