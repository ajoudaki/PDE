"""Run only the two authorized routing suites; contain all temporary writes."""
import importlib.util
import os
from pathlib import Path
import sys
import tempfile
import unittest

BASE = Path('/tmp/pde-main-routing-round4.MZx4oZmk')
REPO = Path('/home/amir/Codes/PDE')
sys.dont_write_bytecode = True
tempfile.tempdir = str(BASE)
os.environ['TMPDIR'] = str(BASE)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
for key in list(os.environ):
    if key.startswith(('PDE_OPERATOR_', 'PDE_QUADRATIC_', 'PDE_LONG_HORIZON_')):
        del os.environ[key]

def check_write(path):
    if isinstance(path, (str, bytes, os.PathLike)):
        target = Path(os.fsdecode(path)).absolute()
        # The tests clean up their private temporary trees with directory fds.
        if not target.is_relative_to(BASE) and not (not Path(path).is_absolute()):
            raise RuntimeError(f'Out-of-scope write blocked: {target}')

def audit(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
            check_write(path)
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod'):
        check_write(args[0])
    elif event in ('os.rename', 'os.link', 'os.symlink'):
        check_write(args[1])

sys.addaudithook(audit)
os.chdir(BASE)
suite = unittest.TestSuite()
for name in ('test_resnet_routing', 'test_quadratic_routing'):
    path = REPO / 'studies/repository_refactor_2026_09_09' / (name + '.py')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
