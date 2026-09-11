"""Build and check the exact proposed C.4.7 edition; no training is run.

This validates frozen inputs, complete dependency correspondence, preservation,
and deterministic supplied-state algebra. It is not a proof verifier.
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
    assert not output.exists(), 'Use a fresh generated directory.'
    manifest_path = study/'P2_PROMOTION_MANIFEST.json'
    manifest = json.loads(manifest_path.read_text())
    result = dict(scope='proposed-edition correspondence and supplied-state algebra only',
                  python=platform.python_version(), inputs={}, excerpts=[], commands=[])
    for name, expected in manifest['inputs'].items():
        assert '/' not in name and name not in ('.', '..'), name
        assert sha((study/name).read_bytes()) == expected, name
        result['inputs'][name] = expected
    for name, expected in manifest['established_sha256'].items():
        assert name.startswith('docs/') and '..' not in Path(name).parts
        assert sha((repo/name).read_bytes()) == expected, name

    dependencies = (study/'P2_PROMOTION_DEPENDENCIES.md').read_text()
    pattern = (r'<!-- BEGIN ([^:]+):(\d+)-(\d+); SHA256 ([0-9a-f]+) -->\n'
               r'(.*?)\n<!-- END CANONICAL DEPENDENCY -->')
    for match in re.finditer(pattern, dependencies, re.S):
        name, first, last, expected, body = match.groups()
        source = (repo/name).read_bytes()
        assert sha(source) == expected
        exact = ''.join(source.decode().splitlines(keepends=True)[int(first)-1:int(last)])
        assert body == exact, (name, first, last)
        result['excerpts'].append(dict(path=name, first=int(first), last=int(last),
                                      sha256=sha(body.encode())))
    assert len(result['excerpts']) == 7

    output.mkdir(parents=True)
    env = dict(os.environ, PYTHONPATH='', PYTHONDONTWRITEBYTECODE='1',
               OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')

    def execute(command, cwd, label):
        run = subprocess.run(command, cwd=cwd, env=env, text=True, capture_output=True)
        log = output/(label+'.log')
        log.write_text(run.stdout+run.stderr)
        result['commands'].append(dict(command=command, cwd=str(cwd),
                                       exit=run.returncode, log_sha256=sha(log.read_bytes())))
        # Retain the failure record, including the precise command, on assertion.
        (output/'validation.json').write_text(json.dumps(result, indent=2)+'\n')
        assert run.returncode == 0, (label, run.returncode)

    execute([sys.executable, '-B', str(study/'P2_EDITION_BUILD.py'),
             '--output', str(output/'edition'), '--manifest', str(manifest_path)],
            repo, 'edition')
    standalone = output/'edition/standalone'
    assert (standalone/'docs/README.md').read_bytes() == (study/'P2_PROPOSED_GUIDE.md').read_bytes()
    checks = standalone/'validation'
    checks.mkdir()
    scripts = ['P2_PROMOTION_TANGENT_CHECK.py', 'P2_PROMOTION_REFERENCE_CHECK.py',
               'P2_PROMOTION_RADIAL_CHECK.py']
    for name in scripts:
        (checks/name).write_bytes((study/name).read_bytes())
    data = standalone/'data/generated/trained_data_response/checks'
    execute([sys.executable, '-B', scripts[0], '--output', str(data/'tangent')],
            checks, 'tangent')
    execute([sys.executable, '-B', scripts[1]], checks, 'reference')
    execute([sys.executable, '-B', scripts[2], '--output', str(data/'radial')],
            checks, 'radial')
    assert not (standalone/'studies').exists()
    assert not (standalone/'.git').exists()
    for name, expected in manifest['inputs'].items():
        assert sha((study/name).read_bytes()) == expected, name
    for name in scripts:
        assert sha((checks/name).read_bytes()) == manifest['inputs'][name]
    result['edition_validation_sha256'] = sha((output/'edition/validation.json').read_bytes())
    result['result'] = 'PASS'
    (output/'validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
