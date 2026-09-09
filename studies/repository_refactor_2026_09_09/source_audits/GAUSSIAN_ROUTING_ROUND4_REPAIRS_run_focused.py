"""Record the exact focused suite and private fixture hashes, without science."""
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

PRIVATE = Path(__file__).resolve().parent
REPO = Path('/home/amir/Codes/PDE')
os.chdir(PRIVATE)
os.environ['TMPDIR'] = str(PRIVATE)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
tempfile.tempdir = str(PRIVATE)
sys.dont_write_bytecode = True
sys.path.insert(0, str(REPO))

write_checks = 0


def check_write(path, dir_fd=None):
    global write_checks
    if isinstance(path, int):
        return
    value = Path(os.fsdecode(path))
    if not value.is_absolute():
        parent = Path(os.readlink(f'/proc/self/fd/{dir_fd}')) if dir_fd not in (None, -1) else Path.cwd()
        value = parent / value
    if not value.resolve().is_relative_to(PRIVATE):
        raise AssertionError(f'write outside private test directory: {value}')
    write_checks += 1


def audit(event, args):
    if event == 'open' and isinstance(args[0], (str, bytes)):
        flags = args[2]
        if isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
            check_write(args[0])
    elif event in ('os.remove', 'os.rmdir'):
        check_write(args[0], args[1])
    elif event == 'os.mkdir':
        check_write(args[0], args[2])
    elif event in ('os.rename', 'os.link'):
        check_write(args[0], args[2])
        check_write(args[1], args[3])
    elif event == 'os.symlink':
        check_write(args[1], args[2])


sys.addaudithook(audit)
from studies.mfp_gaussian_calculus import test_migration_sibling_consumers as consumers
from studies.mfp_gaussian_calculus import test_migration_replay_helpers as replay

fixture_hashes = []
original_hashes = consumers.hashes


def record_hashes(paths):
    result = original_hashes(paths)
    fixture_hashes.append(result)
    return result


consumers.hashes = record_hashes


class Result(unittest.TextTestResult):
    successful_subtests = 0

    def addSubTest(self, test, subtest, err):
        if err is None:
            self.successful_subtests += 1
        super().addSubTest(test, subtest, err)


suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(module) for module in (consumers, replay))
stream = io.StringIO()
result = unittest.TextTestRunner(stream=stream, verbosity=2, resultclass=Result).run(suite)
assert result.wasSuccessful(), stream.getvalue()
assert len(fixture_hashes) % 2 == 0
for index in range(0, len(fixture_hashes), 2):
    assert fixture_hashes[index] == fixture_hashes[index + 1]
(PRIVATE / 'test-output.txt').write_text(stream.getvalue())
(PRIVATE / 'fixture-hashes.json').write_text(json.dumps([
    {'before': fixture_hashes[i], 'after': fixture_hashes[i + 1]}
    for i in range(0, len(fixture_hashes), 2)
], indent=2) + '\n')
summary = {
    'tests': result.testsRun,
    'successful_subtests': result.successful_subtests,
    'failures': len(result.failures),
    'errors': len(result.errors),
    'unchanged_private_fixture_hash_snapshots': len(fixture_hashes) // 2,
    'writes_restricted_to': str(PRIVATE),
    'checked_private_write_operations': write_checks,
    'bytecode_disabled': sys.dont_write_bytecode,
}
(PRIVATE / 'test-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary))
