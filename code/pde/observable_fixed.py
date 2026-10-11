"""Compatibility alias for :mod:`dtdl.observable_fixed`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.observable_fixed")
