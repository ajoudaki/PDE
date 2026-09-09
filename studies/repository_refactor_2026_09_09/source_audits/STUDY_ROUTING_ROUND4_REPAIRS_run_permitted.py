from pathlib import Path
import concurrent.futures
import importlib.util
import json
import os
import subprocess
import sys
import unittest

PRIVATE = Path(__file__).resolve().parent
ROOT = Path('/home/amir/Codes/PDE')
TESTS = json.loads((PRIVATE / 'permitted-tests.json').read_text())

if len(sys.argv) > 1:
    relative = sys.argv[1]
    if relative not in TESTS:
        raise ValueError('not in inspected named-suite allowlist')
    def guard(event, args):
        if event in {'subprocess.Popen', 'os.system', 'socket.connect', 'socket.bind'}:
            raise RuntimeError(f'acceptance forbids {event}')
        targets = []
        if event == 'open' and isinstance(args[0], (str, bytes, os.PathLike)):
            path, mode, flags = args
            writing = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
            if writing:
                targets.append(path)
            elif '/data/historical/' in os.fsdecode(path) and Path(path).suffix in {'.npz', '.npy'}:
                raise RuntimeError('historical arrays prohibited')
        elif event in {'os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.utime'}:
            targets.append(args[0])
        elif event in {'os.rename', 'os.link'}:
            targets.extend(args[:2])
        elif event == 'os.symlink':
            targets.append(args[1])
        for target in targets:
            if isinstance(target, int):
                continue
            lexical = Path(os.fsdecode(target)).absolute()
            if not lexical.is_relative_to(PRIVATE):
                raise RuntimeError(f'write outside private acceptance directory: {event} {lexical}')
    sys.addaudithook(guard)
    if True:
        # NumPy's assertion helpers probe CPU features through a subprocess.
        # The acceptance harness supplies an inert feature response only while
        # loading these helpers; the inspected tests and numerical assertions
        # remain unchanged and all later subprocesses remain prohibited.
        from types import SimpleNamespace
        from unittest import mock
        with mock.patch('subprocess.run', return_value=SimpleNamespace(stdout='', returncode=0)):
            import numpy.testing
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location('_inspected_acceptance_suite', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
    record = {'module': relative, 'tests': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors), 'skipped': len(result.skipped)}
    print('ACCEPTANCE_RESULT', json.dumps(record), flush=True)
    raise SystemExit(0 if result.wasSuccessful() else 1)

def run(item):
    index, relative = item
    prefix = os.environ.get('PATCH_PASS', 'retry' if os.environ.get('ACCEPTANCE_RETRY') == '1' else 'suite')
    directory = PRIVATE / f'{prefix}-{index:02d}'
    directory.mkdir()
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=str(ROOT), TMPDIR=str(directory),
               XDG_CACHE_HOME=str(directory / 'cache'), MPLCONFIGDIR=str(directory / 'mpl'),
               PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', CUDA_VISIBLE_DEVICES='')
    result = subprocess.run([sys.executable, '-B', str(Path(__file__).resolve()), relative], cwd=directory,
                            env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=60)
    (directory / 'test.log').write_text(result.stdout)
    records = [line.removeprefix('ACCEPTANCE_RESULT ') for line in result.stdout.splitlines() if line.startswith('ACCEPTANCE_RESULT ')]
    record = json.loads(records[-1]) if records else {'module': relative, 'tests': 0, 'import_failed': True}
    record.update(exit_code=result.returncode, log=str(directory / 'test.log'))
    print(json.dumps(record), flush=True)
    return record

selected = list(enumerate(TESTS))
retry = os.environ.get('ACCEPTANCE_RETRY') == '1'
if retry:
    failed = {row['module'] for row in json.loads((PRIVATE / 'test-results.json').read_text()) if row['exit_code']}
    selected = [(index, name) for index, name in selected if name in failed]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(run, selected))
(PRIVATE / (os.environ.get('PATCH_PASS', 'retry' if retry else 'test') + '-results.json')).write_text(json.dumps(records, indent=2) + '\n')
print('TOTAL', sum(record['tests'] for record in records), 'tests;', sum(record['exit_code'] != 0 for record in records), 'unsuccessful modules')
