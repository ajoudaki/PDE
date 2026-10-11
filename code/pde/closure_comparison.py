"""Compatibility alias for :mod:`dtdl.closure_comparison`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.closure_comparison")
