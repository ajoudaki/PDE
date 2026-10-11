"""Compatibility alias for :mod:`dtdl.observable_p1_initialization`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.observable_p1_initialization")
