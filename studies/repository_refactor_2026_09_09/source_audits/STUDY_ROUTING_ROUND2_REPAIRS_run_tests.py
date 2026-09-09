"""Only explicitly selected bounded unittest suites; writes stay private."""
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
tempfile.tempdir = str(OUT)

def confined(value, dir_fd=None):
    if isinstance(value, (str, bytes, os.PathLike)):
        path = Path(os.fsdecode(value))
        if dir_fd is not None and dir_fd != -1 and not path.is_absolute():
            path = Path(os.readlink(f'/proc/self/fd/{dir_fd}'))/path
        if not path.absolute().is_relative_to(OUT) or not path.resolve().is_relative_to(OUT):
            raise RuntimeError(f'out-of-scope fixture write: {path}')

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if not isinstance(path, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
            confined(path)
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.truncate'):
        confined(args[0], args[-1] if event != 'os.truncate' else None)
    elif event in ('os.rename', 'os.link'):
        confined(args[0]); confined(args[1])
    elif event == 'os.symlink':
        confined(args[1])
    elif event in ('subprocess.Popen', 'os.system'):
        raise RuntimeError('child execution is forbidden in bounded fixtures')

def main():
    os.chdir(OUT)
    # NumPy's test helper probes SVE via lscpu on import; suppress only that
    # optional platform probe. All subsequent subprocess execution is refused.
    with mock.patch.object(subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, stdout='', stderr='')):
        import numpy.testing
    sys.addaudithook(guard)
    relative = sys.argv[1]
    spec = importlib.util.spec_from_file_location('bounded_worker_suite', ROOT/relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
    label = relative.replace('/', '__').removesuffix('.py')
    (OUT/(label+'.log')).write_text(stream.getvalue())
    print(stream.getvalue(), end='')
    print(json.dumps(dict(suite=relative, tests=result.testsRun, failures=len(result.failures),
                          errors=len(result.errors), skipped=len(result.skipped))))
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    raise SystemExit(main())
