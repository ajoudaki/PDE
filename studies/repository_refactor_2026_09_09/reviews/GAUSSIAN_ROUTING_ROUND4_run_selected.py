import hashlib
import importlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).parent
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
os.chdir(PRIVATE)
tempfile.tempdir = str(PRIVATE)
os.environ.update(TMPDIR=str(PRIVATE), PYTHONDONTWRITEBYTECODE='1', XDG_CACHE_HOME=str(PRIVATE / 'cache'))
allowed = {str(ROOT / p) for p in json.loads((PRIVATE / 'before.json').read_text())}
retained = [ROOT / 'data/historical/studies/stieltjes_resolution/canonical_hidden_high_order' / name
            for name in ('PRODUCTION_HIDDEN_RESULT.json', 'INDEPENDENT_HIDDEN_RESULT.json')]
allowed.update(map(str, retained))
reads = set()
mutations = []

def check_path(value, write=False, dir_fd=None):
    if not isinstance(value, (str, bytes, os.PathLike)):
        return
    value = os.fsdecode(value)
    if dir_fd is not None and dir_fd != -1 and not os.path.isabs(value):
        value = os.path.join(os.readlink('/proc/self/fd/' + str(dir_fd)), value)
    path = os.path.abspath(value)
    if write:
        if not path.startswith(str(PRIVATE) + '/'):
            raise PermissionError('review write boundary: ' + path)
        mutations.append(path)
    elif path.startswith(str(ROOT) + '/'):
        if path not in allowed:
            raise PermissionError('review read boundary: ' + path)
        reads.add(path)

def audit(event, args):
    if event == 'open':
        check_path(args[0], bool(args[2] & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)))
    elif event in ('os.remove', 'os.rmdir'):
        check_path(args[0], True, args[1])
    elif event in ('os.mkdir', 'os.chmod', 'os.utime'):
        check_path(args[0], True, args[-1])
    elif event in ('os.rename', 'os.link', 'os.symlink'):
        check_path(args[1], True)
        if event == 'os.rename':
            check_path(args[0], True)

sys.addaudithook(audit)

def hashes(paths):
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}

retained_before = hashes(retained)
if not (PRIVATE / 'retained-before.json').exists():
    (PRIVATE / 'retained-before.json').write_text(json.dumps(retained_before, indent=2) + '\n')
modules = [
    'studies.causal_flow_peeling_calculus.test_migration_input_aliases',
    'studies.d3_arctan_closure_program.test_migration_input_aliases',
    'studies.mfp_gaussian_calculus.test_migration_input_aliases',
    'studies.stieltjes_resolution.canonical_hidden_high_order.test_migration_input_aliases',
    'studies.mfp_program_history.report.test_migration_paths',
    'studies.mfp_gaussian_calculus.test_migration_paths',
    'studies.mfp_gaussian_calculus.test_migration_retired_interfaces',
    'studies.stieltjes_resolution.canonical_hidden_high_order.test_migration_paths',
]
excluded = {
    'test_selected_sine_fixture_to_separate_fresh_result',
    'test_freeze_refuses_existing_seal_without_any_writes',
    'test_compiler_package_dispatches_retained_gate_before_science',
}

def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item

suite = unittest.TestSuite()
for name in modules:
    if len(sys.argv) > 1 and name != 'studies.mfp_program_history.report.test_migration_paths':
        continue
    module = importlib.import_module(name)
    for test in flatten(unittest.defaultTestLoader.loadTestsFromModule(module)):
        if test._testMethodName not in excluded and (len(sys.argv) == 1 or test._testMethodName == 'test_valid_plain_text_pipeline_preserves_sources_and_intermediates'):
            suite.addTest(test)
test_ids = [test.id() for test in flatten(suite)]

class CountResult(unittest.TextTestResult):
    subtests = 0
    def addSubTest(self, test, subtest, err):
        self.subtests += 1
        super().addSubTest(test, subtest, err)

label = 'selected-tests' if len(sys.argv) == 1 else sys.argv[1]
with (PRIVATE / (label + '.log')).open('w') as stream:
    result = unittest.TextTestRunner(stream=stream, verbosity=2, resultclass=CountResult).run(suite)
retained_after = hashes(retained)
(PRIVATE / 'retained-after.json').write_text(json.dumps(retained_after, indent=2) + '\n')
assert retained_before == retained_after
summary = dict(tests=result.testsRun, subtests=result.subtests, failures=len(result.failures), errors=len(result.errors),
               skipped=len(result.skipped), test_ids=test_ids, excluded=sorted(excluded),
               repository_reads=sorted(reads), mutation_paths=sorted(set(mutations)))
(PRIVATE / (label + '.json')).write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({k: summary[k] for k in ('tests', 'subtests', 'failures', 'errors', 'skipped')}))
for test, message in result.failures + result.errors:
    print(test.id(), message)
sys.exit(not result.wasSuccessful())
