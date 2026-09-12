"""Assemble and validate the proposed C-H1 edition without editing live docs.

Usage: python assemble_edition_v3.py /absolute/fresh/output
Only named established documents are copied, not a repository or Git checkout.
No training or empirical research is performed.
"""
from pathlib import Path
import difflib
import hashlib
import json
import platform
import re
import subprocess
import sys

study = Path(__file__).resolve().parent
repo = study.parent.parent
out = Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=False)
(out / 'docs').mkdir()
(out / 'checks').mkdir()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
sources = json.loads((study / 'source_hashes_v1.json').read_text())
inputs = json.loads((study / 'review_inputs_v3.json').read_text())['files']
for name, expected in inputs.items():
    assert sha(study / name) == expected, name
names = ['global_nonlinear.md', 'special_data_limits.md',
         'gaussian_calculus.md', 'NOTATION.md', 'README.md']
for name in names:
    src = repo / 'docs' / name
    assert sha(src) == sources['docs/' + name], name
    (out / 'docs' / name).write_bytes(src.read_bytes())

base = (out / 'docs/global_nonlinear.md').read_text()
candidate = (study / 'candidate_v3.md').read_text()
anchor = '#### C.4.8. Sampling fluctuations of the trained prediction'
assert base.count(anchor) == 1
insertion = candidate.rstrip() + '\n\n'
assembled = base.replace(anchor, insertion + anchor)
assert assembled.replace(insertion, '', 1) == base
assert assembled.count('##### C.4.7.8. Current bounded-probe hierarchy') == 1
assert 'studies/' not in candidate and 'data/generated/' not in candidate
assert '^(H' not in candidate
labels = re.findall(r'\(H(\d+)\)', candidate)
assert set(labels) == {str(i) for i in range(1, 20)}
for target in re.findall(r'\]\(([^)]+)\)', candidate):
    filename, _, fragment = target.partition('#')
    assert (out / 'docs' / filename).is_file(), target
    assert not fragment, 'No new fragments expected; add an explicit checker if changed.'
(out / 'docs/global_nonlinear.md').write_text(assembled)
old_guide = (out / 'docs/README.md').read_text()
new_guide = (study / 'README_proposed_v3.md').read_text()
(out / 'docs/README.md').write_text(new_guide)
for name, before, after in [('global_nonlinear.md', base, assembled),
                            ('README.md', old_guide, new_guide)]:
    diff = ''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                      fromfile='docs/' + name, tofile='docs/' + name))
    (out / (name + '.patch')).write_text(diff)

# The static proof check runs using only its copied standalone source.
static = out / 'checks/check_weak_identity.py'
static.write_bytes((study / 'check_weak_identity.py').read_bytes())
assert sha(static) == inputs['check_weak_identity.py']
packet = (study / 'dependencies_v1.md').read_text()
blocks = re.findall(r'^```python\n(.*?)^```', packet, flags=re.M | re.S)
assert len(blocks) == 1
certificate = out / 'checks/reference_certificate.py'
certificate.write_text(blocks[0])
assert sha(certificate) == '112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e'
commands = [[sys.executable, str(static), str(out / 'results/static_identity')],
            [sys.executable, str(certificate)]]
runs = []
for i, command in enumerate(commands):
    result = subprocess.run(command, cwd=out, text=True, capture_output=True)
    log = out / f'check_{i}.txt'
    log.write_text(result.stdout + result.stderr)
    runs.append({'command': command, 'cwd': str(out), 'exit_code': result.returncode,
                 'output': log.name, 'sha256': sha(log)})
    assert result.returncode == 0, result.stderr

manifest = {'kind': 'standalone proposed edition, no live established edits',
            'python': sys.version, 'platform': platform.platform(),
            'frozen_inputs': inputs, 'established_sources': {k: v for k, v in sources.items()
                if k.startswith('docs/')},
            'checks': runs,
            'new_material': {'start_line': assembled[:assembled.index(insertion)].count('\n') + 1,
                             'line_count': len(candidate.splitlines())},
            'scope': 'Exact insertion/removal preservation, exact guide diff, new local link, '
                     'equation labels, standalone static identity and rational certificate. '
                     'Existing untouched book links and unread scientific complement are not audited.',
            'outputs': {str(p.relative_to(out)): sha(p) for p in sorted(out.rglob('*'))
                        if p.is_file()}, 'status': 'PASS'}
(out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'edition': str(out), 'checks': runs}, indent=2))
