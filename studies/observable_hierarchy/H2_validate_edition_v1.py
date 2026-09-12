"""Static validation of a standalone proposed edition; no trajectory runs."""
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--edition', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    edition, out = args.edition.resolve(), args.output.resolve()
    allowed = (ROOT / 'data/generated/observable_hierarchy').resolve()
    if allowed not in out.parents or out.exists():
        raise SystemExit('Use a new study-owned generated output directory')
    out.mkdir(parents=True)
    assembly = json.loads((edition / 'ASSEMBLY.json').read_text())
    for relative, expected in assembly['outputs'].items():
        assert hashlib.sha256((edition / relative).read_bytes()).hexdigest() == expected, relative
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', PYTHONPATH=str(edition / 'code'),
               H2_TEST_SCRATCH=str(out / 'scratch'))
    env.pop('H2_PROTOTYPE_MODULE', None)
    guide = (edition / 'code/README.md').read_text()
    new_guide = guide.split('## Finite autonomous observable population closure\n', 1)[1]
    example = re.findall(r'```python\n(.*?)```', new_guide, flags=re.S)
    assert len(example) == 1
    # This executable input is copied verbatim from the assembled guide.
    (out / 'guide_example.py').write_text(example[0])
    commands = [
        [sys.executable, '-B', 'code/tests/test_observable_closure.py'],
        [sys.executable, '-B', '-c', example[0]],
        [sys.executable, '-B', '-c',
         'import pde, pde.observable_closure, numpy; print(numpy.__version__)'],
    ]
    records = []
    for i, command in enumerate(commands):
        run = subprocess.run(command, cwd=edition, env=env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = out / f'check_{i}.log'
        log.write_text(run.stdout)
        records.append(dict(command=command, cwd=str(edition), exit=run.returncode,
                            output=str(log), sha256=hashlib.sha256(log.read_bytes()).hexdigest()))
    link = re.search(r'\]\(([^)]+#c479-[^)]+)\)', new_guide).group(1)
    file_part, anchor = link.split('#', 1)
    target = (edition / 'code' / file_part).resolve()
    assert target.is_file()
    headings = re.findall(r'^#+\s+(.+)$', target.read_text(), flags=re.M)
    slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
    assert anchor in slugs, (anchor, slugs)
    assert 'studies/' not in example[0]
    summary = dict(status='PASS' if all(r['exit'] == 0 for r in records) else 'FAIL',
                   python=sys.version, platform=platform.platform(),
                   environment={k:env[k] for k in ['PYTHONDONTWRITEBYTECODE',
                     'OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','PYTHONPATH','H2_TEST_SCRATCH']},
                   edition=str(edition), assembly_sha256=hashlib.sha256(
                       (edition / 'ASSEMBLY.json').read_bytes()).hexdigest(),
                   checks=records, new_guide_fragment=anchor,
                   scope='New module/tests/example/imports/link only; no training or numerical convergence test.')
    (out / 'validation.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    if summary['status'] != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
