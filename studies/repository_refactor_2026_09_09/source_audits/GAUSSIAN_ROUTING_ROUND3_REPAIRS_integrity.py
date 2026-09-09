"""Byte-only implementation baseline; historical content is never interpreted."""
import difflib
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
NAMES = ('causal_flow_peeling_calculus d3_arctan_closure_program mfp_gaussian_calculus '
         'mfp_cubic_compiler mfp_identity_compiler mfp_linear_growth_uniform_counterexample '
         'mfp_sine_compiler mfp_quadratic_l2_order5 stieltjes_resolution mfp_program_history').split()
FROZEN = [ROOT / 'studies/_output_paths.py', ROOT / '.gitignore',
          Path('/tmp/pde-migration-acceptance.tTQJzxO5/REPORT.md'),
          Path('/tmp/pde-migration-acceptance.tTQJzxO5/EVIDENCE.md')]

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def files():
    paths = list(FROZEN)
    for name in NAMES:
        for parent in (ROOT / 'studies' / name, ROOT / 'data/historical/studies' / name):
            paths.extend(p for p in parent.rglob('*') if p.is_file())
    return sorted(paths)

phase = sys.argv[1]
entries = {str(path): sha(path) for path in files()}
(OUT / f'{phase}.json').write_text(json.dumps(entries, indent=2) + '\n')
(OUT / f'{phase}.sha256').write_text(''.join(f'{value}  {path}\n' for path, value in entries.items()))
if phase == 'before':
    for name in NAMES:
        for source in (ROOT / 'studies' / name).rglob('*.py'):
            target = OUT / 'originals' / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
else:
    before = json.loads((OUT / 'before.json').read_text())
    changed = {path: {'before': before.get(path), 'after': entries.get(path)}
               for path in sorted(before.keys() | entries.keys()) if before.get(path) != entries.get(path)}
    (OUT / 'changed-paths.json').write_text(json.dumps(changed, indent=2) + '\n')
    diffs = []
    for path in changed:
        source = Path(path)
        assert source.is_relative_to(ROOT / 'studies') and source.suffix == '.py', path
        assert source != ROOT / 'studies/_output_paths.py'
        original = OUT / 'originals' / source.relative_to(ROOT)
        old = original.read_text() if original.exists() else ''
        new = source.read_text() if source.exists() else ''
        diffs.extend(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=str(source) + ' (before)', tofile=str(source) + ' (after)'))
    (OUT / 'implementation.diff').write_text(''.join(diffs))
    print(json.dumps({'changed_paths': len(changed), 'retained_changes': 0, 'frozen_changes': 0}))
print(json.dumps({'phase': phase, 'files': len(entries), 'manifest_sha256': sha(OUT / f'{phase}.sha256'), 'helper_sha256': entries[str(ROOT / 'studies/_output_paths.py')]}))
assert entries[str(ROOT / 'studies/_output_paths.py')] == '8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e'
