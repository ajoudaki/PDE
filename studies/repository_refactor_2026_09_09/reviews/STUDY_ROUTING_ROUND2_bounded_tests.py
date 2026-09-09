"""Run only named, inspected unittest fixtures with all writes confined here."""
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
import subprocess

from read_inputs import BASE, OUT, allowed, read

sys.dont_write_bytecode = True
sys.path.insert(0, str(BASE))
tempfile.tempdir = str(OUT)

def confined(value, dir_fd=None):
    if isinstance(value, (str, bytes, os.PathLike)):
        p = Path(os.fsdecode(value))
        if dir_fd is not None and dir_fd != -1 and not p.is_absolute():
            p = Path(os.readlink(f'/proc/self/fd/{dir_fd}')) / p
        p = p.absolute()
        if not p.is_relative_to(OUT) or not p.resolve().is_relative_to(OUT):
            raise RuntimeError(f'diagnostic attempted out-of-scope write: {p}')

inside = False
def guard(event, args):
    global inside
    if inside:
        return
    if event == 'open':
        path, mode, flags = args
        if isinstance(path, int):
            return
        writing = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writing:
            confined(path)
        else:
            p = Path(os.fsdecode(path)).absolute()
            if p.is_relative_to(BASE):
                if not allowed(p.resolve()):
                    raise RuntimeError(f'diagnostic attempted out-of-scope read: {p}')
                if p.suffix == '.pyc':
                    raise RuntimeError('Use PYTHONPYCACHEPREFIX to avoid untracked cached source')
                if p.is_file():
                    inside = True
                    try:
                        read(str(p.relative_to(BASE)))
                    finally:
                        inside = False
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.truncate'):
        dir_fd = args[-1] if event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod') else None
        confined(args[0], dir_fd)
    elif event in ('os.rename', 'os.link'):
        confined(args[0]); confined(args[1])
    elif event == 'os.symlink':
        confined(args[1])
    elif event in ('subprocess.Popen', 'os.system'):
        raise RuntimeError('No child execution in bounded fixtures')

def main():
    os.chdir(OUT)
    # NumPy's assertion module optionally probes CPU SVE with lscpu. Stub only
    # that import-time platform probe; no subprocess runs in these diagnostics.
    with mock.patch.object(subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, stdout='', stderr='')):
        import numpy.testing
    sys.addaudithook(guard)
    rel = sys.argv[1]
    # Record the exact test bytes before Python executes them.
    read(rel)
    spec = importlib.util.spec_from_file_location('selected_acceptance_test', BASE / rel)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    label = rel.replace('/', '__').removesuffix('.py')
    log = OUT / (label + '.log')
    if log.exists():
        log.rename(OUT / (label + '.harness-initial.log'))
    log.write_text(stream.getvalue())
    print(stream.getvalue(), end='')
    print(json.dumps({'suite': rel, 'tests': result.testsRun, 'failures': len(result.failures),
                      'errors': len(result.errors), 'skipped': len(result.skipped)}))
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    raise SystemExit(main())
