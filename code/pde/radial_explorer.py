"""Compatibility alias and command for :mod:`dtdl.radial_explorer`."""
import importlib as _importlib
import sys as _sys

if __name__ == "__main__":
    _importlib.import_module("dtdl.radial_explorer").main()
else:
    _sys.modules[__name__] = _importlib.import_module("dtdl.radial_explorer")
