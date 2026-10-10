"""Render one standalone edition format with retained logs and a time limit."""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / 'data/generated' / STUDY.name
TOOLING = GENERATED / 'promotion_tooling'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run')
    parser.add_argument('format', choices=('html', 'pdf', 'latex'))
    args = parser.parse_args()
    run = (GENERATED / args.run).resolve()
    assert run.is_relative_to(GENERATED) and (run / 'edition/docs/_quarto.yml').is_file()
    logs = run / 'render_logs'
    logs.mkdir(exist_ok=True)
    scratch = run / 'tmp'
    scratch.mkdir(exist_ok=True)
    env = dict(os.environ)
    env.update(XDG_CACHE_HOME=str(TOOLING/'cache'), XDG_DATA_HOME=str(TOOLING/'share'),
               XDG_CONFIG_HOME=str(TOOLING/'config'), TMPDIR=str(scratch),
               PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1')
    command = [str(TOOLING/'quarto-1.10.19/bin/quarto'), 'render', '--to', args.format]
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    start = time.monotonic()
    with (logs/f'{args.format}.log').open('w') as stream:
        try:
            result = subprocess.run(command, cwd=run/'edition/docs', env=env,
                                    stdout=stream, stderr=subprocess.STDOUT, timeout=900)
            code = result.returncode
        except subprocess.TimeoutExpired:
            code = 124
    report = {'command':command, 'cwd':str(run/'edition/docs'), 'started':started,
              'elapsed_seconds':time.monotonic()-start, 'exit_code':code,
              'environment':{k:env[k] for k in ('XDG_CACHE_HOME','XDG_DATA_HOME',
                  'XDG_CONFIG_HOME','TMPDIR','PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS',
                  'OMP_NUM_THREADS','MKL_NUM_THREADS')}}
    output = run / 'edition/data/generated/DTDL'
    if code == 0:
        archive = run / f'rendered_{args.format}'
        shutil.copytree(output, archive)
        report['outputs'] = {str(p.relative_to(archive)):hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(archive.rglob('*')) if p.is_file()}
    (logs/f'{args.format}.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='outputs'},indent=2))
    if code:
        print((logs/f'{args.format}.log').read_text()[-8000:])
    raise SystemExit(code)


if __name__ == '__main__':
    main()
