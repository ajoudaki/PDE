"""Run only bounded migration tests; constrain every write to private scratch."""
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

BASE = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
sys.path.insert(0, str(BASE))
sys.dont_write_bytecode = True
tempfile.tempdir = str(OUT)
os.environ['TMPDIR'] = str(OUT)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def guard(event, args):
    if event == 'open':
        raw, mode, flags = args
        if isinstance(raw, int):
            return
        path = Path(os.fsdecode(raw)).absolute()
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
            if not path.is_relative_to(OUT):
                raise PermissionError(f'test write outside private scratch: {path}')
    if event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.rename', 'os.link', 'os.symlink'):
        raw = args[1] if event in ('os.link', 'os.symlink') else args[0]
        if isinstance(raw, (str, bytes)) and not Path(os.fsdecode(raw)).absolute().is_relative_to(OUT):
            raise PermissionError(f'test mutation outside private scratch: {event} {raw}')

sys.addaudithook(guard)
names = (
    'studies.mfp_gaussian_calculus.test_migration_paths',
    'studies.mfp_gaussian_calculus.test_migration_retired_interfaces',
    'studies.stieltjes_resolution.canonical_hidden_high_order.test_migration_paths',
)
suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromName(name) for name in names)
stream = io.StringIO()
result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
log = stream.getvalue()
(OUT / 'tests.txt').write_text(log)
summary = {'tests': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors), 'skipped': len(result.skipped)}
(OUT / 'tests.json').write_text(json.dumps(summary, indent=2) + '\n')
print(log)
print(json.dumps(summary))
sys.exit(not result.wasSuccessful())
