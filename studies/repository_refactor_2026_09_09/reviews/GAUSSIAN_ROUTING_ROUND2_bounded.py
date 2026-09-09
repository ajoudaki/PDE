"""Guard rails for private interface diagnostics, not a scientific test runner."""
import importlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from inventory import BASE, NAMES, OUT

sys.dont_write_bytecode = True
sys.path.insert(0, str(BASE))
tempfile.tempdir = str(OUT)
os.environ['TMPDIR'] = str(OUT)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
ALLOWED = [BASE / 'studies' / n for n in NAMES] + [BASE / 'data/historical/studies' / n for n in NAMES]
ALLOWED_FILES = {BASE / 'studies/_output_paths.py', BASE / '.gitignore'}

def guard(event, args):
    if event == 'open':
        raw, mode, flags = args
        if isinstance(raw, int):
            return
        path = Path(os.fsdecode(raw)).absolute()
        write = flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
        if write and not path.is_relative_to(OUT):
            raise PermissionError(f'PRIVATE DIAGNOSTIC denied write: {path}')
        if not write and path.is_relative_to(BASE) and path not in ALLOWED_FILES and not any(path.is_relative_to(root) for root in ALLOWED):
            raise PermissionError(f'PRIVATE DIAGNOSTIC denied out-of-scope repository read: {path}')
    if event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.truncate', 'os.rename', 'os.symlink', 'os.link'):
        raw = args[1] if event == 'os.symlink' else args[0]
        if isinstance(raw, (str, bytes)):
            path = Path(os.fsdecode(raw)).absolute()
            if not path.is_relative_to(OUT):
                raise PermissionError(f'PRIVATE DIAGNOSTIC denied mutation: {event} {path}')
    if event == 'subprocess.Popen':
        command = args[1]
        approved = (isinstance(command, list) and len(command) >= 5 and
                    command[0] == sys.executable and command[1:4] == ['-B', '-I', '-S'] and
                    any(Path(command[4]).is_relative_to(root) for root in ALLOWED))
        if not approved:
            raise PermissionError(f'PRIVATE DIAGNOSTIC denied subprocess: {command}')

sys.addaudithook(guard)

def regressions():
    modules = (
        'studies.mfp_gaussian_calculus.test_migration_paths',
        'studies.mfp_gaussian_calculus.test_migration_retired_interfaces',
        'studies.mfp_linear_growth_uniform_counterexample.test_migration_paths',
        'studies.mfp_cubic_compiler.two_input_plus_gaussian_program.test_migration_paths',
    )
    stream = io.StringIO()
    suite = unittest.TestSuite()
    for name in modules:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromName(name))
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    log = stream.getvalue()
    (OUT / 'regressions.txt').write_text(log)
    print(log)
    print(json.dumps({'tests': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors), 'skips': len(result.skipped)}))

if __name__ == '__main__':
    regressions()
