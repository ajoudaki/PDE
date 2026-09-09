import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import unittest

PRIVATE = Path(__file__).parent
REPO = Path('/home/amir/Codes/PDE')
STUDIES = tuple(REPO / 'studies' / n for n in ('resnet_dense_long_horizon', 'resnet_dense_early_audit', 'resnet_operator_core', 'mfp_quadratic_compiler'))
TEST_ROOT = REPO / 'studies/repository_refactor_2026_09_09'
TESTS = tuple(TEST_ROOT / ('test_' + n + '_routing.py') for n in ('resnet', 'quadratic', 'metadata'))
GUIDE_TESTS = {
    REPO / 'studies/mfp_quadratic_compiler/campaign6_f13_threshold/CAMPAIGN_REPORT.md': 'test_campaign6_documented_build_routes',
    REPO / 'studies/mfp_quadratic_compiler/SECTOR_ENGINE.md': 'test_sector_guide_uses_current_sources_and_generated_products',
}
for name in ('tmp', 'cache', 'mpl'):
    (PRIVATE / name).mkdir(exist_ok=True)
os.environ.update(TMPDIR=str(PRIVATE / 'tmp'), XDG_CACHE_HOME=str(PRIVATE / 'cache'), MPLCONFIGDIR=str(PRIVATE / 'mpl'), PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
for name in tuple(os.environ):
    if name.startswith(('PDE_OPERATOR_', 'PDE_QUADRATIC_', 'PDE_LONG_HORIZON_')) or name == 'GALERKIN_OUT':
        os.environ.pop(name)
sys.dont_write_bytecode = True
accesses = {}
busy = False
active_test = ''

def audit(event, args):
    global busy
    if event != 'open' or busy or not isinstance(args[0], (str, bytes, os.PathLike)):
        return
    p = Path(os.fsdecode(args[0])).absolute()
    mode, flags = args[1], args[2]
    writing = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
    if writing:
        if not p.is_relative_to(PRIVATE):
            raise PermissionError(f'bounded tests can write private fixtures only: {p}')
        return
    if not p.is_relative_to(REPO):
        return
    relative = p.relative_to(REPO).as_posix()
    source = any(p.is_relative_to(base) for base in STUDIES) and p.suffix in {'.py', '.cpp', '.h', '.c', '.sh'}
    guides = any(p.is_relative_to(base) for base in STUDIES) and p.name in {'README.md', 'REPRODUCE.md', 'REPRODUCTION.md'}
    path_guide = p in GUIDE_TESTS and active_test.endswith('.' + GUIDE_TESTS[p])
    historical = relative.startswith('data/historical/studies/mfp_quadratic_compiler/campaign4/') and p.suffix == '.json'
    if not (source or guides or path_guide or historical or p in TESTS or relative in {'.gitignore', 'studies/_output_paths.py'}):
        raise PermissionError(f'outside bounded test inputs: {p}')
    if p.is_file() and str(p) not in accesses:
        busy = True
        try:
            accesses[str(p)] = hashlib.sha256(p.read_bytes()).hexdigest()
        finally:
            busy = False

class Result(unittest.TextTestResult):
    def startTest(self, test):
        global active_test
        active_test = test.id()
        super().startTest(test)

sys.addaudithook(audit)
suite = unittest.TestSuite()
for path in TESTS:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = module
    spec.loader.exec_module(module)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))
with (PRIVATE / 'bounded_tests.log').open('w') as stream:
    result = unittest.TextTestRunner(stream=stream, verbosity=2, resultclass=Result).run(suite)
busy = True
after = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in accesses}
(PRIVATE / 'test_inputs_before_sha256.json').write_text(json.dumps(accesses, indent=2) + '\n')
(PRIVATE / 'test_inputs_after_sha256.json').write_text(json.dumps(after, indent=2) + '\n')
summary = {'run': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors), 'skipped': [(str(test), reason) for test, reason in result.skipped], 'input_count': len(accesses), 'changed_test_inputs': [p for p in accesses if accesses[p] != after[p]]}
(PRIVATE / 'bounded_results.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
print((PRIVATE / 'bounded_tests.log').read_text())
sys.exit(not result.wasSuccessful())
