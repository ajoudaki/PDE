"""Compatibility alias for :mod:`dtdl.exact_calculus`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.exact_calculus")
