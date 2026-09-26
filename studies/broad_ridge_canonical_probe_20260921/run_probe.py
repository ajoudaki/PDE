"""Run only the eight precommitted integrations; preserve every attempt."""
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
OUT = ROOT / 'data/generated/broad_ridge_canonical_probe_20260921/run01'
DATA = ROOT / 'data/generated/broad_ridge_canonical_probe_20260921/data01/data.npz'
MODELS = ('closure1024', 'width244', 'width492', 'width1024')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=False)
    frozen = {str(p.relative_to(ROOT)): sha(p) for p in
              [STUDY/'PROTOCOL.md', STUDY/'probe.py', STUDY/'probe_check.py',
               STUDY/'run_probe.py', STUDY/'analyze.py', ROOT/'code/pde/finite_network.py']}
    record = {'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                                             text=True).strip(),
              'frozen_sources': frozen, 'data_sha256': sha(DATA),
              'attempts': [], 'wall_cap_seconds': 120, 'maximum_concurrency': 2,
              'worker_budget_seconds': 960, 'status': 'running'}

    def save():
        (OUT/'run_record.json').write_text(json.dumps(record, indent=2)+'\n')

    def worker(model, level):
        for p, h in frozen.items():
            assert sha(ROOT/p) == h, 'Frozen source changed: '+p
        assert sha(DATA) == record['data_sha256'], 'Data changed'
        directory = OUT/f'{model}_{level}'
        command = [sys.executable, '-B', str(STUDY/'probe.py'), 'run',
                   '--data', str(DATA), '--model', model, '--output', str(directory),
                   '--level', level, '--horizon', '5000', '--wall-seconds', '120']
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                   OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
                   PYTHONPATH=str(ROOT/'code'))
        started = time.monotonic()
        with (OUT/f'{model}_{level}.log').open('w') as log:
            try:
                done = subprocess.run(command, cwd=ROOT, env=env, stdout=log,
                                      stderr=subprocess.STDOUT, timeout=135)
                code = done.returncode
                timeout = False
            except subprocess.TimeoutExpired:
                code, timeout = -999, True
        seconds = time.monotonic()-started
        result = directory/'result.json'
        item = {'model': model, 'level': level, 'directory': str(directory.relative_to(ROOT)),
                'command': command, 'returncode': code, 'supervisor_timeout': timeout,
                'process_wall_seconds': seconds,
                'result_sha256': sha(result) if result.exists() else None}
        if result.exists():
            item['result'] = json.loads(result.read_text())
        return item

    save()
    for level in ('primary', 'fine'):
        with ThreadPoolExecutor(max_workers=2) as pool:
            jobs = [pool.submit(worker, model, level) for model in MODELS]
            for future in as_completed(jobs):
                item = future.result()
                record['attempts'].append(item)
                record['worker_process_wall_seconds'] = sum(
                    r['process_wall_seconds'] for r in record['attempts'])
                save()
                print(json.dumps({'model': item['model'], 'level': item['level'],
                                  'returncode': item['returncode'],
                                  'wall_seconds': item['process_wall_seconds'],
                                  'result': item.get('result', {})}), flush=True)
    for p, h in frozen.items():
        assert sha(ROOT/p) == h, 'Frozen source changed: '+p
    record['status'] = 'attempts_complete'
    record['within_worker_budget'] = record['worker_process_wall_seconds'] <= 960
    save()
    print(json.dumps({'status': record['status'],
                      'worker_seconds': record['worker_process_wall_seconds']}), flush=True)


if __name__ == '__main__':
    main()
