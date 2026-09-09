"""Run only an inspected fail-closed CLI, blocking all writes and subprocesses."""
import os
from pathlib import Path
import runpy
import sys

ROOT = Path('/home/amir/Codes/PDE')
sys.path.insert(0, str(ROOT))
target = ROOT/sys.argv[1]
sys.path.insert(0, str(target.parent))
sys.argv = [str(target)]
events = []

def guard(event, args):
    mutation = event in {'os.mkdir', 'os.remove', 'os.rename', 'os.rmdir', 'os.system', 'subprocess.Popen', 'os.fork'}
    if event == 'open':
        _, mode, flags = args
        mutation = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
    if mutation:
        events.append(event)
        raise AssertionError(f'guarded entrypoint attempted {event}: {args}')

sys.addaudithook(guard)
try:
    runpy.run_path(str(target), run_name='__main__')
except RuntimeError as exc:
    assert 'archive-only' in str(exc), str(exc)
    assert not events
    if 'fp64_successor' in str(target) or target.name == 'run_block.py':
        assert 'torch' not in sys.modules
    print('PASS: refusal before writes/subprocesses:', target, str(exc))
else:
    raise AssertionError('legacy entrypoint did not refuse')
