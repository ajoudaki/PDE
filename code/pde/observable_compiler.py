"""Compatibility alias for :mod:`dtdl.observable_compiler`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.observable_compiler")
