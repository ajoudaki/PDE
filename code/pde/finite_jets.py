"""Compatibility alias for :mod:`dtdl.finite_jets`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.finite_jets")
