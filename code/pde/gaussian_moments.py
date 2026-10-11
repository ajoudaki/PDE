"""Compatibility alias for :mod:`dtdl.gaussian_moments`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.gaussian_moments")
