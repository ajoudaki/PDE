"""Check exact C-H1 promotion and rerun its two static source checks.

Usage: python check_promoted_v3.py /absolute/fresh/generated/output
No training, source mutation or Git operation is performed.
"""
from pathlib import Path
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
sha = lambda b: hashlib.sha256(b).hexdigest()
manifest = json.loads((study / 'edition_manifest_v3.json').read_text())
inputs = json.loads((study / 'review_inputs_v3.json').read_text())['files']
sources = json.loads((study / 'source_hashes_v1.json').read_text())
for name, expected in inputs.items():
    assert sha((study / name).read_bytes()) == expected, name
reports = json.loads((study / 'review_acceptance_v3.json').read_text())['reports']
for name, expected in reports.items():
    assert sha((study / name).read_bytes()) == expected, name
for name, expected in sources.items():
    if name not in ('docs/global_nonlinear.md', 'docs/README.md'):
        assert sha((repo / name).read_bytes()) == expected, name

candidate = (study / 'candidate_v3.md').read_bytes()
insertion = candidate.rstrip() + b'\n\n'
chapter = (repo / 'docs/global_nonlinear.md').read_bytes()
guide = (repo / 'docs/README.md').read_bytes()
assert sha(chapter) == manifest['outputs']['docs/global_nonlinear.md']
assert sha(guide) == manifest['outputs']['docs/README.md']
assert guide == (study / 'README_proposed_v3.md').read_bytes()
assert chapter.count(insertion) == 1
start = chapter.index(insertion)
assert chapter[:start].count(b'\n') + 1 == 11441
base = chapter[:start] + chapter[start + len(insertion):]
assert sha(base) == sources['docs/global_nonlinear.md']
assert chapter[start + len(insertion):].startswith(
    b'#### C.4.8. Sampling fluctuations of the trained prediction\n')
definitions = re.findall(rb'^ {4}.*\(H(\d+)\)\s*$', candidate, re.M)
assert sorted(map(int, definitions)) == list(range(1, 20))
for target in re.findall(rb'\]\(([^)]+)\)', candidate):
    assert target == b'special_data_limits.md'
    assert (repo / 'docs' / target.decode()).is_file()

checks = out / 'checks'
checks.mkdir()
static = checks / 'check_weak_identity.py'
static.write_bytes((study / 'check_weak_identity.py').read_bytes())
# Extract the original certificate from the live established chapter.
text = chapter.decode()
section = text.split('###### 5. Reproducible rational Gaussian certificate', 1)[1]
section = section.split('##### C.4.5.2.', 1)[0]
blocks = re.findall(r'^```python\n(.*?)^```', section, re.M | re.S)
assert len(blocks) == 1
certificate = checks / 'reference_certificate.py'
certificate.write_text(blocks[0])
assert sha(certificate.read_bytes()) == manifest['outputs']['checks/reference_certificate.py']
runs = []
for index, command in enumerate([
    [sys.executable, '-I', '-B', str(static), str(out / 'static_identity')],
    [sys.executable, '-I', '-B', str(certificate)],
]):
    result = subprocess.run(command, cwd=out, text=True, capture_output=True, timeout=60)
    log = out / f'check_{index}.txt'
    log.write_text(result.stdout + result.stderr)
    assert result.returncode == 0, result.stderr
    assert sha(log.read_bytes()) == manifest['outputs'][f'check_{index}.txt']
    runs.append({'command': command, 'cwd': str(out), 'exit_code': result.returncode,
                 'output_sha256': sha(log.read_bytes()), 'matches_reviewed_output': True})
summary = {'status': 'PASS', 'scope': 'Exact approved live correspondence and two static checks; '
           'no whole-book proof/export audit or training', 'python': sys.version,
           'platform': platform.platform(), 'candidate_sha256': sha(candidate),
           'live_hashes': {'docs/global_nonlinear.md': sha(chapter), 'docs/README.md': sha(guide)},
           'restored_original_chapter_sha256': sha(base), 'candidate_lines': [11441, 12082],
           'separator_line': 12083, 'all_other_dependencies_unchanged': True,
           'frozen_review_inputs_and_reports_unchanged': True, 'checks': runs}
(out / 'result.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
