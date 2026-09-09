import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

PRIVATE = Path(__file__).parent
REPO = Path('/home/amir/Codes/PDE')
LONG = REPO / 'studies/resnet_dense_long_horizon'

if os.environ.get('MIGRATION_RECORDER_CHILD') == '1':
    arguments = sys.argv[1:]
    with Path(os.environ['MIGRATION_WRAPPER_LOG']).open('a') as stream:
        stream.write(json.dumps(arguments) + '\n')
    if arguments[0] == 'run_all.py':
        spec = importlib.util.spec_from_file_location('manifest_path_check', LONG / 'make_manifest.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.validate_output_root(Path(arguments[arguments.index('--output-root') + 1]))
    # Every test/scientific/manifest command is recorded only. The sole executed
    # study function above is the stdlib output-root validator.
    sys.exit(0)

root = Path(tempfile.mkdtemp(prefix='wrapper-', dir=PRIVATE))
record_dir = root / 'bin'
record_dir.mkdir()
# The launcher is copied as bytes from this private script; no repository edits.
launcher = record_dir / 'python'
launcher.write_bytes(('#!' + sys.executable + '\n').encode() + Path(__file__).read_bytes())
launcher.chmod(0o700)
results = []
for label, output in (('valid', root / 'out with spaces'), ('protected-source', LONG)):
    log = root / (label + '.jsonl')
    env = {**os.environ, 'PATH': str(record_dir) + os.pathsep + os.environ['PATH'], 'TMPDIR': str(root), 'PYTHONDONTWRITEBYTECODE': '1', 'MIGRATION_RECORDER_CHILD': '1', 'MIGRATION_WRAPPER_LOG': str(log), 'PDE_LONG_HORIZON_OUTPUT_ROOT': str(output)}
    proc = subprocess.run(['bash', str(LONG / 'reproduce.sh')], env=env, cwd=root, text=True, capture_output=True, timeout=10)
    calls = [json.loads(line) for line in log.read_text().splitlines()]
    if label == 'valid':
        assert proc.returncode == 0 and len(calls) == 3
        assert calls[1][-2:] == calls[2][-2:] == ['--output-root', str(output)]
        assert not output.exists()
    else:
        assert proc.returncode != 0 and len(calls) == 2
        assert calls[0] == ['-m', 'unittest', 'discover', '-s', 'tests', '-v']
        assert 'Select fresh output' in proc.stderr
    results.append({'case': label, 'returncode': proc.returncode, 'calls': calls, 'science_tests_and_manifest': 'recorded only, never dispatched'})
(PRIVATE / 'wrapper_probe_results.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
