"""Compatibility alias for :mod:`dtdl.prediction_views`."""
import importlib as _importlib
import sys as _sys

_sys.modules[__name__] = _importlib.import_module("dtdl.prediction_views")
