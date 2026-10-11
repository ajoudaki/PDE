"""Compatibility alias for :mod:`dtdl.mfp_expr`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.mfp_expr")
