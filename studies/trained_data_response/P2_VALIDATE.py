"""Frozen-input and standalone deterministic checks; never run training.

Use --output with a fresh path under data/generated/trained_data_response/.
This validates provenance and algebra, not the unresolved A-C assertions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    study = Path(__file__).resolve().parent
    repo = study.parent.parent
    output = Path(args.output).resolve()
    allowed = (repo / 'data/generated/trained_data_response').resolve()
    assert output != allowed and allowed in output.parents
    output.mkdir(parents=True, exist_ok=False)
    manifest = json.loads((study / 'P1_MANIFEST.json').read_text())
    result = dict(scope='provenance and standalone deterministic algebra only',
                  python=platform.python_version(),
                  validator_sha256=digest(Path(__file__).read_bytes()),
                  frozen={}, bases={}, excerpts=[], commands=[])
    for name, metadata in manifest['inputs'].items():
        data = (study / name).read_bytes()
        actual = digest(data)
        assert actual == metadata['sha256'], name
        result['frozen'][name] = actual

    section = (study / 'P1_SECTION.md').read_text()
    bases = {}
    for name, expected in manifest['base_sha256'].items():
        current = (repo / name).read_text()
        text = current
        if name == 'docs/global_nonlinear.md':
            assert text.count(section) == 1
            text = text.replace(section, '')
        for edit in reversed(manifest['ancillary_edits']):
            if edit['path'] == name:
                assert text.count(edit['new']) == 1
                text = text.replace(edit['new'], edit['old'])
        if name == 'docs/global_nonlinear.md':
            # The approved assembly appended one blank separator and P1.
            text = text.rstrip('\n') + '\n'
        actual = digest(text.encode())
        assert actual == expected, name
        bases[name] = text
        result['bases'][name] = dict(live_sha256=digest(current.encode()),
                                    restored_pre_promotion_sha256=actual)

    dependencies = (study / 'P1_DEPENDENCIES.md').read_text()
    pattern = r'<!-- BEGIN ([^:]+):(\d+)-(\d+) -->\n(.*?)<!-- END EXCERPT -->'
    for match in re.finditer(pattern, dependencies, re.S):
        name, start, end, body = match.groups()
        expected = '\n'.join(bases[name].splitlines()[int(start)-1:int(end)])
        assert expected.strip('\n') == body.strip('\n'), (name, start, end)
        result['excerpts'].append(dict(path=name, start=int(start), end=int(end),
                                       sha256=digest(body.strip('\n').encode())))
    assert len(result['excerpts']) == 7

    standalone = output / 'standalone'
    standalone.mkdir()
    for name in ('P1_SECTION.md', 'P1_DEPENDENCIES.md',
                 'P1_CHECK_IDENTITIES.py', 'P1_REFERENCE_CERTIFICATE.py'):
        (standalone / name).write_bytes((study / name).read_bytes())
    env = dict(os.environ, PYTHONPATH='', PYTHONDONTWRITEBYTECODE='1',
               OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    commands = [
        [sys.executable, '-B', 'P1_CHECK_IDENTITIES.py', '--output', 'algebra'],
        [sys.executable, '-B', 'P1_REFERENCE_CERTIFICATE.py'],
    ]
    for index, command in enumerate(commands):
        run = subprocess.run(command, cwd=standalone, env=env,
                             capture_output=True, text=True)
        log = output / f'command_{index+1}.log'
        log.write_text(run.stdout + run.stderr)
        result['commands'].append(dict(command=command, cwd=str(standalone),
                                       returncode=run.returncode,
                                       log_sha256=digest(log.read_bytes())))
        assert run.returncode == 0, command
    result['result'] = 'PASS'
    (output / 'validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
