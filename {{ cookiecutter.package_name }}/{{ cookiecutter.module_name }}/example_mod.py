# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   :
# AUTHOR  :
# PROJECT :
#
# ----------------------------------------------------------------------------

"""**DOCSTRING**.

description

Routine Listings
----------------

"""

__author__ = ""
# __credits__ = [""]
# __maintainer__ = ""


__all__ = ['primes', 'do_primes', ]

##############################################################################
# IMPORTS

# GENERAL

import warnings
import argparse
from typing import Optional

# CUSTOM

# PROJECT-SPECIFIC


##############################################################################
# PARAMETERS


##############################################################################
# CODE
##############################################################################


def primes(imax):
    """
    Returns prime numbers up to imax.

    Parameters
    ----------
    imax: int
        The number of primes to return. This should be less or equal to 10000.

    Returns
    -------
    result: list
        The list of prime numbers.
    """

    p = list(range(10000))
    result = []
    k = 0
    n = 2

    if imax > 10000:
        raise ValueError("imax should be <= 10000")

    while len(result) < imax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
            if k > 10000:
                break
        n = n + 1

    return result


# ------------------------------------------------------------------------


def do_primes(n, usecython=False):
    if usecython:
{% if cookiecutter.use_compiled_extensions != 'y' %}
        raise Exception("This template does not have the example C code included.")
{% else %}
        from .example_c import primes as cprimes
        print('Using cython-based primes')
        return cprimes(n)
{% endif %}
    else:
        print('Using pure python primes')
        return primes(n)


##############################################################################
# Command Line
##############################################################################


def make_parser(inheritable=False):
    """Expose parser for ``main``.

    Parameters
    ----------
    inheritable: bool
        whether the parser can be inherited from (default False).
        if True, sets ``add_help=False`` and ``conflict_hander='resolve'``

    Returns
    -------
    parser: ArgumentParser

    """
    parser = argparse.ArgumentParser(
        description="",
        add_help=~inheritable,
        conflict_handler="resolve" if ~inheritable else 'error'
    )
    parser.add_argument('-c', '--use-cython', dest='cy', action='store_true',
                        help='Use the Cython-based Prime number generator.')
    parser.add_argument('-t', '--timing', dest='time', action='store_true',
                        help='Time the Fibonacci generator.')
    parser.add_argument('-p', '--print', dest='prnt', action='store_true',
                        help='Print all of the Prime numbers.')
    parser.add_argument('n', metavar='N', type=int,
                        help='Get Prime numbers up to this number.')

    return parser

# /def


# ------------------------------------------------------------------------


def main(
    args: Optional[list] = None, opts: Optional[argparse.Namespace] = None
):
    """Script Function.

    Parameters
    ----------
    args : list, optional
        an optional single argument that holds the sys.argv list,
        except for the script name (e.g., argv[1:])
    opts : Namespace, optional
        pre-constructed results of parsed args
        if not None, used ONLY if args is None

    """
    if opts is not None and args is None:
        pass
    else:
        if opts is not None:
            warnings.warn('Not using `opts` because `args` are given')
        parser = make_parser()
        opts = parser.parse_args(args)

    from time import time

    pre = time()
    primes = do_primes(opts.n, opts.cy)
    post = time()

    print('Found {0} prime numbers'.format(len(primes)))
    print('Largest prime: {0}'.format(primes[-1]))

    if opts.time:
        print('Running time: {0} s'.format(post - pre))

    if opts.prnt:
        print('Primes: {0}'.format(primes))

    return

# /def


# ------------------------------------------------------------------------

if __name__ == "__main__":

    main(args=None, opts=None)  # all arguments except script name

# /if


##############################################################################
# END
