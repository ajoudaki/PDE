"""Compatibility imports for the renamed :mod:`dtdl` package.

New code should import dtdl. Submodule shims share its implementation objects
and load optional dependencies only when that submodule is requested.
"""
from dtdl import *  # noqa: F401,F403
from dtdl import __all__
