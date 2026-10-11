"""Compatibility alias for :mod:`dtdl.compression_data`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.compression_data")
