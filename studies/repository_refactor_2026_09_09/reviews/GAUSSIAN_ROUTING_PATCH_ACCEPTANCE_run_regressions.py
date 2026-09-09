import importlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import types
import unittest

PRIVATE = Path(__file__).parent
SNAPSHOT = PRIVATE / 'snapshot'
sys.path.insert(0, str(SNAPSHOT))
os.chdir(SNAPSHOT)
sys.dont_write_bytecode = True
for key in ('TMPDIR', 'XDG_CACHE_HOME', 'MPLCONFIGDIR', 'PYTHONPYCACHEPREFIX'):
    value = PRIVATE / ('cache-' + key.lower())
    value.mkdir(exist_ok=True)
    os.environ[key] = str(value)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def boundary(event, args):
    if event == 'open' and isinstance(args[0], (str, bytes, os.PathLike)):
        path = Path(os.fsdecode(args[0])).absolute()
        mode, flags = args[1:3]
        writing = isinstance(mode, str) and any(x in mode for x in 'wax+')
        writing = writing or isinstance(flags, int) and bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
        if writing and not path.is_relative_to(PRIVATE):
            raise AssertionError('nonprivate write blocked: ' + str(path))
        if str(path).startswith('/home/amir/Codes/PDE/'):
            raise AssertionError('live repository read blocked: ' + str(path))
        if '/data/historical/' in str(path):
            raise AssertionError('historical read blocked: ' + str(path))
    if event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.rename', 'os.symlink', 'os.link'):
        targets = args[:2] if event in ('os.rename', 'os.link') else args[1:2] if event == 'os.symlink' else args[:1]
        for target in targets:
            if isinstance(target, (str, bytes, os.PathLike)) and os.path.isabs(target):
                if not Path(os.fsdecode(target)).is_relative_to(PRIVATE):
                    raise AssertionError('nonprivate mutation blocked: ' + str(target))
    if event == 'subprocess.Popen':
        argv = args[1]
        if not (isinstance(argv, (list, tuple)) and '-B' in argv and '-I' in argv and '-S' in argv
                and str(argv[-1]).startswith(str(SNAPSHOT)) and str(argv[-1]).endswith('.py')):
            raise AssertionError('unapproved subprocess blocked: ' + repr(argv))
sys.addaudithook(boundary)

stubs = []
if importlib.util.find_spec('scipy') is None:
    scipy, stats = types.ModuleType('scipy'), types.ModuleType('scipy.stats')
    def forbidden(*args, **kwargs):
        raise AssertionError('optional scientific dependency invoked')
    stats.chi2 = types.SimpleNamespace(sf=forbidden)
    scipy.stats = stats
    sys.modules.update({'scipy': scipy, 'scipy.stats': stats})
    stubs.append('scipy.stats.chi2: import-only; sf raises')

modules = [
 'studies.mfp_gaussian_calculus.test_migration_sibling_consumers',
 'studies.mfp_gaussian_calculus.test_migration_replay_helpers',
 'studies.mfp_gaussian_calculus.test_migration_input_aliases',
 'studies.repository_refactor_2026_09_09.test_gaussian_consumer_routing',
 'studies.mfp_gaussian_calculus.test_migration_paths',
 'studies.mfp_gaussian_calculus.test_migration_retired_interfaces',
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

class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subtests = 0
        self.passed = []
    def addSubTest(self, test, subtest, outcome):
        self.subtests += 1
        super().addSubTest(test, subtest, outcome)
    def addSuccess(self, test):
        self.passed.append(test.id())
        super().addSuccess(test)

suite = unittest.TestSuite(test for name in modules
    for test in flatten(unittest.defaultTestLoader.loadTestsFromName(name))
    if test.id().rsplit('.', 1)[-1] not in excluded)
with (PRIVATE / 'regressions.log').open('w') as log:
    result = unittest.TextTestRunner(stream=log, verbosity=2, resultclass=RecordedResult).run(suite)
payload = {'tests': result.testsRun, 'subtests': result.subtests, 'passed': result.passed,
           'failures': [(t.id(), detail) for t, detail in result.failures],
           'errors': [(t.id(), detail) for t, detail in result.errors],
           'skipped': [(t.id(), why) for t, why in result.skipped],
           'excluded': sorted(excluded), 'stubs': stubs}
(PRIVATE / 'regressions.json').write_text(json.dumps(payload, indent=2) + '\n')
print(json.dumps({k: v if k not in ('passed',) else len(v) for k, v in payload.items()}, indent=2))
sys.exit(not result.wasSuccessful())
