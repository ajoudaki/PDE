"""Run a real study entrypoint with only unavailable plotting imports stubbed."""
import runpy
import sys
from pathlib import Path
from types import ModuleType

matplotlib = ModuleType('matplotlib')
matplotlib.use = lambda *args, **kwargs: None
pyplot = ModuleType('matplotlib.pyplot')
matplotlib.pyplot = pyplot
sys.modules.update({'matplotlib': matplotlib, 'matplotlib.pyplot': pyplot})
target = Path(sys.argv[1])
sys.argv = sys.argv[1:]
sys.path[0] = str(target.parent)
runpy.run_path(str(target), run_name='__main__')
