"""Compatibility alias for :mod:`dtdl.finite_reductions`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.finite_reductions")
