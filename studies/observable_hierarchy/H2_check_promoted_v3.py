"""Check the approved live C-H2 mapping and rerun affected static checks.

The frozen pre-promotion assembly/checkers deliberately require old live hashes.
This checker uses the retained approval record and accepts only the approved
new hashes at its five destinations. No training or convergence experiment runs.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / 'studies/observable_hierarchy'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    allowed = (ROOT / 'data/generated/observable_hierarchy').resolve()
    require(allowed in out.parents and not out.exists(),
            'Use a fresh directory under data/generated/observable_hierarchy')
    record = json.loads((STUDY / 'H2_promotion_record_v3.json').read_text())
    require(record['approval']['user_message'] == 'I approve', 'Missing approval record')
    for name, expected in record['approved_artifact_hashes'].items():
        require(sha(ROOT / name) == expected, 'Approved artifact changed: ' + name)
    mapping = json.loads((STUDY / 'H2_promotion_mapping_v3.json').read_text())
    acceptance = json.loads((STUDY / 'H2_review_acceptance_v3.json').read_text())
    require(mapping == acceptance['proposal_mapping'] == record['mapping'],
            'Approval, review and final mapping differ')
    for name, item in mapping.items():
        require(sha(ROOT / name) == item['proposed_sha256'],
                'Live file differs from approved edition: ' + name)
    inputs = {}
    for manifest in acceptance['manifests'].values():
        require(sha(ROOT / manifest['path']) == manifest['sha256'], 'Manifest changed')
        packet = json.loads((ROOT / manifest['path']).read_text())
        for name, item in packet['inputs'].items():
            if name in inputs:
                require(inputs[name] == item['sha256'], 'Inconsistent frozen input')
            inputs[name] = item['sha256']
    for name, expected in inputs.items():
        if name in mapping:
            require(expected == mapping[name]['old_sha256'], 'Unexpected old input hash')
            expected = mapping[name]['proposed_sha256']
        require(sha(ROOT / name) == expected, 'Frozen input changed: ' + name)
    for report in acceptance['reports']:
        require(sha(ROOT / report['file']) == report['sha256'], 'Original report changed')

    book_path = ROOT / 'docs/global_nonlinear.md'
    book = book_path.read_bytes()
    section = (STUDY / 'H2_proposed_section_v3.md').read_bytes().rstrip() + b'\n\n'
    anchor = b'#### C.4.8. Sampling fluctuations of the trained prediction'
    require(book.count(section + anchor) == 1, 'Incorrect insertion or placement')
    restored = book.replace(section, b'', 1)
    require(hashlib.sha256(restored).hexdigest() ==
            mapping['docs/global_nonlinear.md']['old_sha256'], 'Old chapter changed')
    require((STUDY / 'candidate_v3.md').read_bytes().rstrip() in book,
            'Frozen C-H1 subsection changed')
    readme_prefix = (STUDY / 'README.md').read_bytes().split(
        b'## C-H2 continuation', 1)[0]
    require(hashlib.sha256(readme_prefix).hexdigest() == record['C_H1_README_prefix_sha256'],
            'Frozen C-H1 README content changed')
    excerpts = 0
    for part in (STUDY / 'dependencies_v1.md').read_text().split('\n---\n'):
        if not part.lstrip().startswith('Source:'):
            continue
        header, body = part.strip().split('\n\n', 1)
        source = header.split('`')[1]
        require(body.strip() in (ROOT / source).read_text(), 'Dependency changed: ' + source)
        excerpts += 1
    require(excerpts == 7, 'Unexpected dependency count')
    require((ROOT / 'code/pde/observable_closure.py').read_bytes() ==
            (STUDY / 'H2_prototype_v3.py').read_bytes(), 'Module relocation changed code')

    guide = (ROOT / 'code/README.md').read_text().split(
        '## Finite autonomous observable population closure\n', 1)[1]
    examples = re.findall(r'```python\n(.*?)```', guide, flags=re.S)
    require(len(examples) == 1, 'Expected one verbatim API example')
    link = re.search(r'\]\(([^)]+#c479-[^)]+)\)', guide).group(1)
    file_part, fragment = link.split('#', 1)
    target = (ROOT / 'code' / file_part).resolve()
    require(target == book_path, 'Incorrect new chapter link')
    headings = re.findall(r'^#+\s+(.+)$', target.read_text(), flags=re.M)
    slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
    require(fragment in slugs, 'Missing new chapter fragment')
    require('studies/' not in examples[0], 'Study dependency in API example')
    out.mkdir(parents=True)
    (out / 'guide_example.py').write_text(examples[0])
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', PYTHONPATH=str(ROOT / 'code'),
               H2_TEST_SCRATCH=str(out / 'scratch'))
    env.pop('H2_PROTOTYPE_MODULE', None)
    import_check = (
        'from pathlib import Path; import pde, pde.observable_closure, numpy; '
        f'assert Path(pde.observable_closure.__file__).resolve() == '
        f'Path({str(ROOT / "code/pde/observable_closure.py")!r}); '
        'print(numpy.__version__); print(pde.observable_closure.__file__)')
    commands = [
        [sys.executable, '-B', 'code/tests/test_observable_closure.py'],
        [sys.executable, '-B', '-c', examples[0]],
        [sys.executable, '-B', '-c', import_check],
    ]
    checks = []
    for i, command in enumerate(commands):
        run = subprocess.run(command, cwd=ROOT, env=env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = out / f'check_{i}.log'
        log.write_text(run.stdout)
        checks.append(dict(command=command, cwd=str(ROOT), exit=run.returncode,
                           output=str(log), sha256=sha(log)))
    summary = dict(
        status='PASS' if all(c['exit'] == 0 for c in checks) else 'FAIL',
        python=sys.version, platform=platform.platform(),
        environment={k: env[k] for k in ['PYTHONDONTWRITEBYTECODE',
            'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'PYTHONPATH', 'H2_TEST_SCRATCH']},
        checker_sha256=sha(Path(__file__)),
        final_hashes={name: sha(ROOT / name) for name in mapping},
        frozen_input_count=len(inputs), original_reports_unchanged=3,
        complete_dependency_excerpts=excerpts, frozen_C_H1_preserved=True,
        full_old_chapter_preserved=True, new_guide_fragment=fragment, checks=checks,
        scope='Exact approved mapping; installed static tests, API example, imports and link; no training.')
    (out / 'validation.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))
    if summary['status'] != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
