"""Validate and assemble the frozen P2 proof packet; run no training."""
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


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    study = Path(__file__).resolve().parent
    repo = study.parent.parent
    output = Path(args.output).resolve()
    allowed = (repo/'data/generated/trained_data_response').resolve()
    assert allowed in output.parents and output != allowed
    assert not output.exists(), 'use a fresh generated directory'
    manifest = json.loads((study/'P2_MANIFEST.json').read_text())
    result = dict(scope='frozen correspondence and standalone algebra; no proof certification',
                  python=platform.python_version(), inputs={}, excerpts=[], commands=[])
    for name, expected in manifest['inputs'].items():
        assert '/' not in name and name not in ('.', '..'), name
        data = (study/name).read_bytes()
        assert sha(data) == expected, name
        result['inputs'][name] = expected
    for name, expected in manifest['established_sha256'].items():
        assert name.startswith('docs/')
        assert sha((repo/name).read_bytes()) == expected, name
    dependencies = (study/'P2_DEPENDENCIES.md').read_text()
    pattern = r'<!-- BEGIN ([^:]+):(\d+)-(\d+); SHA256 ([0-9a-f]+) -->\n(.*?)\n<!-- END P2 EXCERPT -->'
    for match in re.finditer(pattern, dependencies, re.S):
        name, first, last, expected, body = match.groups()
        source = (repo/name).read_bytes()
        assert sha(source) == expected, name
        exact = ''.join(source.decode().splitlines(keepends=True)[int(first)-1:int(last)])
        assert body == exact, (name, first, last)
        result['excerpts'].append(dict(path=name, first=int(first), last=int(last),
                                      sha256=sha(body.encode())))
    assert len(result['excerpts']) == 4
    p1 = json.loads((study/'P1_MANIFEST.json').read_text())
    for name in ('P1_SECTION.md', 'P1_DEPENDENCIES.md',
                 'P1_CHECK_IDENTITIES.py', 'P1_REFERENCE_CERTIFICATE.py'):
        assert sha((study/name).read_bytes()) == p1['inputs'][name]['sha256'], name
    assert (repo/'docs/global_nonlinear.md').read_text().count(
        (study/'P1_SECTION.md').read_text()) == 1

    output.mkdir(parents=True)
    standalone = output/'standalone'
    packet = standalone/'studies/trained_data_response'
    packet.mkdir(parents=True)
    for name in manifest['inputs']:
        (packet/name).write_bytes((study/name).read_bytes())
    (packet/'P2_MANIFEST.json').write_bytes((study/'P2_MANIFEST.json').read_bytes())
    env = dict(os.environ, PYTHONPATH='', PYTHONDONTWRITEBYTECODE='1',
               OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    commands = [
        [sys.executable, '-B', 'P1_CHECK_IDENTITIES.py', '--output', 'algebra'],
        [sys.executable, '-B', 'P1_REFERENCE_CERTIFICATE.py'],
        [sys.executable, '-B', 'P2_CHECK_RADIAL.py', '--output',
         str(standalone/'data/generated/trained_data_response/radial')],
    ]
    for i, command in enumerate(commands):
        run = subprocess.run(command, cwd=packet, env=env, text=True, capture_output=True)
        log = output/f'command_{i+1}.log'
        log.write_text(run.stdout+run.stderr)
        result['commands'].append(dict(command=command, cwd=str(packet),
                                       exit=run.returncode, log_sha256=sha(log.read_bytes())))
        assert run.returncode == 0, command
    for name, expected in manifest['inputs'].items():
        assert sha((study/name).read_bytes()) == expected, name
        assert sha((packet/name).read_bytes()) == expected, name
    result['result'] = 'PASS'
    (output/'validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
