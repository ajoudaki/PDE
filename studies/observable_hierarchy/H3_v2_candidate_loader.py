"""Load the flat study candidate under its proposed canonical package names.

Only a validation aid; maintained library code never imports this module.
"""
import importlib.util
from pathlib import Path
import sys


def load_candidate():
    here = Path(__file__).resolve().parent
    code = here.parents[1]/"code"
    if str(code) not in sys.path:
        sys.path.insert(0, str(code))
    import pde
    modules = {}
    for suffix in ("fixed", "arithmetic", "words", "compiler", "initialization", "solver"):
        name = "pde.observable_"+suffix
        spec = importlib.util.spec_from_file_location(name, here/("H3_v2_"+suffix+".py"))
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        setattr(pde, "observable_"+suffix, module)
        spec.loader.exec_module(module)
        modules[suffix] = module
    return modules


if __name__ == "__main__":
    import runpy
    load_candidate()
    script, *arguments = sys.argv[1:]
    sys.argv = [script]+arguments
    runpy.run_path(script, run_name="__main__")
