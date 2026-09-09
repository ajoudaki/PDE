import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
suite = unittest.TestSuite()
counts = {}
for name in ('quadratic', 'resnet', 'metadata'):
    path = ROOT / f'studies/repository_refactor_2026_09_09/test_{name}_routing.py'
    spec = importlib.util.spec_from_file_location('supplied_' + name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tests = unittest.defaultTestLoader.loadTestsFromModule(module)
    counts[name] = tests.countTestCases()
    suite.addTests(tests)
with (PRIVATE / 'supplied-tests.log').open('w') as log:
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
summary = dict(counts=counts, total=result.testsRun, failures=len(result.failures),
               errors=len(result.errors), skipped=len(result.skipped))
(PRIVATE / 'supplied-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary))
sys.exit(not result.wasSuccessful())
