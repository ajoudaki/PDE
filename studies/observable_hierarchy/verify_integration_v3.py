"""Independent scoped integration verification; no training or live writes."""
from pathlib import Path
import ast
import collections
import difflib
import hashlib
import json
import platform
import re
import subprocess
import sys

ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/observable_hierarchy'
EDITION = ROOT / 'data/generated/observable_hierarchy/edition_v3'
OUT = Path(__file__).resolve().parent
sha = lambda b: hashlib.sha256(b).hexdigest()
study_names = [
    'integration_assignment_v3.md', 'candidate_v3.md', 'README_proposed_v3.md',
    'notation_v3.md', 'guide_current_v3.md', 'instructions_v3.md',
    'workflow_v3.md', 'review_inputs_v3.json', 'assemble_edition_v3.py',
    'edition_manifest_v3.json',
]
edition_names = [
    'docs/README.md', 'docs/NOTATION.md', 'docs/global_nonlinear.md',
    'docs/special_data_limits.md', 'docs/gaussian_calculus.md',
    'README.md.patch', 'global_nonlinear.md.patch',
    'checks/check_weak_identity.py', 'checks/reference_certificate.py',
    'manifest.json', 'check_0.txt', 'check_1.txt',
]
sb = {n: (STUDY / n).read_bytes() for n in study_names}
eb = {n: (EDITION / n).read_bytes() for n in edition_names}
manifest = json.loads(eb['manifest.json'])
inputs = json.loads(sb['review_inputs_v3.json'])
assert sb['edition_manifest_v3.json'] == eb['manifest.json']
for name in study_names:
    if name in inputs['files']:
        assert sha(sb[name]) == inputs['files'][name], name
for name in edition_names:
    if name in manifest['outputs']:
        assert sha(eb[name]) == manifest['outputs'][name], name

candidate = sb['candidate_v3.md']
insertion = candidate.rstrip() + b'\n\n'
assembled = eb['docs/global_nonlinear.md']
assert assembled.count(insertion) == 1
pos = assembled.index(insertion)
assert assembled[:pos].count(b'\n') + 1 == 11441
assert b''.join(assembled.splitlines(keepends=True)[11440:12083]) == insertion
assert len(candidate.splitlines()) == 642
assert len(insertion.splitlines()) == 643
base = assembled[:pos] + assembled[pos + len(insertion):]
assert sha(base) == manifest['established_sources']['docs/global_nonlinear.md']
assert base[pos:].startswith(b'#### C.4.8. Sampling fluctuations of the trained prediction\n')
assert sb['README_proposed_v3.md'] == eb['docs/README.md']
assert sha(sb['guide_current_v3.md']) == manifest['established_sources']['docs/README.md']
assert sb['notation_v3.md'] == eb['docs/NOTATION.md']
for name in ('NOTATION.md', 'special_data_limits.md', 'gaussian_calculus.md'):
    assert sha(eb['docs/' + name]) == manifest['established_sources']['docs/' + name]

for name, before, after in [
    ('global_nonlinear.md', base, assembled),
    ('README.md', sb['guide_current_v3.md'], eb['docs/README.md']),
]:
    expected = ''.join(difflib.unified_diff(
        before.decode().splitlines(True), after.decode().splitlines(True),
        fromfile='docs/' + name, tofile='docs/' + name)).encode()
    assert expected == eb[name + '.patch'], name

text = candidate.decode()
labels = re.findall(r'^ {4}.*\(H(\d+)\)\s*$', text, flags=re.M)
assert collections.Counter(labels) == {str(i): 1 for i in range(1, 20)}
refs = re.findall(r'\(H(\d+)\)', text)
assert set(refs) <= set(labels)
headings = [line for line in text.splitlines() if line.startswith('#')]
assert headings[0] == '##### C.4.7.8. Current bounded-probe hierarchy'
assert len(headings) == 10
assert all(h.startswith('###### ' + str(i) + '.') for i, h in enumerate(headings[1:], 1))
assert assembled.count(headings[0].encode()) == 1
assert '```' not in text
for token in ('studies/', 'data/generated/', 'integration_v', 'review_', '/home/', '.npy', '.npz'):
    assert token not in text, token
links = re.findall(r'\]\(([^)]+)\)', text)
for link in links:
    filename, sep, fragment = link.partition('#')
    assert not sep
    assert filename in ('special_data_limits.md',)
    assert (EDITION / 'docs' / filename).is_file()
old_guide_links = collections.Counter(re.findall(r'\]\(([^)]+)\)', sb['guide_current_v3.md'].decode()))
new_guide_links = collections.Counter(re.findall(r'\]\(([^)]+)\)', eb['docs/README.md'].decode()))
assert old_guide_links == new_guide_links

checks_dir = OUT / 'copied_checks'
checks_dir.mkdir(exist_ok=False)
runs = []
for index, name in enumerate(('check_weak_identity.py', 'reference_certificate.py')):
    src = eb['checks/' + name]
    ast.parse(src, filename=name)
    assert 'studies/' not in src.decode() and 'data/generated/' not in src.decode()
    copied = checks_dir / name
    copied.write_bytes(src)
    assert sha(copied.read_bytes()) == sha(src)
    command = [sys.executable, '-I', '-B', str(copied)]
    if index == 0:
        command.append(str(OUT / 'fresh_static_identity'))
    result = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=60)
    log = OUT / ('fresh_check_' + str(index) + '.txt')
    log.write_text(result.stdout + result.stderr)
    runs.append({'command': command, 'cwd': str(OUT), 'exit_code': result.returncode,
                 'log': str(log), 'sha256': sha(log.read_bytes()),
                 'matches_frozen_output': log.read_bytes() == eb['check_' + str(index) + '.txt']})
    assert result.returncode == 0, result.stderr

# Outside assigned scientific ranges, only preservation/label metadata is inspected.
old_label_counts = {str(i): len(re.findall(rb'\(H' + str(i).encode() + rb'\)', base))
                    for i in range(1, 20)}
old_tag_counts = {str(i): len(re.findall(rb'\\tag\{H' + str(i).encode() + rb'\}', base))
                  for i in range(1, 20)}
hashes = {str(STUDY / n): sha(b) for n, b in sb.items()}
hashes.update({str(EDITION / n): sha(b) for n, b in eb.items()})
summary = {
    'status': 'PASS', 'scope': 'Independent integration checks only, not a whole-book proof audit',
    'python': sys.version, 'platform': platform.platform(), 'cwd': str(OUT),
    'hashes': hashes, 'preserved_base_sha256': sha(base),
    'candidate_line_count': 642, 'insertion_line_count_including_separator': 643,
    'assembled_line_count': len(assembled.splitlines()),
    'new_line_range': [11441, 12083],
    'older_scientific_read_ranges': [[4208,4631],[8978,9170],[11398,11440],[12084,12172]],
    'unread_older_scientific_ranges': [[1,4207],[4632,8977],[9171,11397],[12173,19396]],
    'new_headings': headings, 'equation_definitions': labels,
    'old_parenthesized_H_labels': old_label_counts, 'old_tagged_H_labels': old_tag_counts,
    'new_links': links, 'guide_link_changes': [],
    'checks': runs,
    'not_inspected': ['dependencies_v1.md', 'source_hashes_v1.json',
                      'other review reports or study history',
                      'bodies of special_data_limits.md and gaussian_calculus.md',
                      'retained results/static_identity/result.json'],
}
(OUT / 'verification.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
