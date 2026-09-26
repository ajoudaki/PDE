"""Bounded, two-GPU execution of CLOSURE_TRANSFER_2048_PROTOCOL.md."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
STEPS = {
    ('relu', 'two_outliers_alternating'): .0078125,
    ('relu', 'quadrant_alternating'): .0009765625,
    ('gelu', 'two_outliers_alternating'): .015625,
    ('gelu', 'quadrant_alternating'): .00390625,
    ('selu', 'two_outliers_alternating'): .001953125,
    ('selu', 'quadrant_alternating'): .00048828125,
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    tmp.replace(path)


def needs_refinement(coarse, fine):
    if not all(r.get('fitted', False) for r in (coarse, fine)):
        return True
    with np.load(Path(coarse['run']) / 'predictions.npz') as a:
        x = a['circle_predictions']
    with np.load(Path(fine['run']) / 'predictions.npz') as b:
        y = b['circle_predictions']
    difference = x-y
    return (float(np.sqrt(np.mean(difference**2))) > .01
            or float(np.max(np.abs(difference))) > .05)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True)
    parser.add_argument('--inputs', required=True)
    parser.add_argument('--execution-receipt', required=True)
    parser.add_argument('--backend', choices=['eager', 'graphs'], required=True)
    args = parser.parse_args()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    (out/'runs').mkdir()
    (out/'logs').mkdir()
    receipt = json.loads(Path(args.execution_receipt).read_text())
    assert receipt['passed'] is True
    charged = float(receipt['integration_seconds'])
    sources = [HERE/n for n in ['closure_transfer_euler.py',
               'activation_fast_engine.py', 'activation_moment_engine.py',
               'deep_moment_engine.py', 'moment_engine.py',
               'CLOSURE_TRANSFER_2048_PROTOCOL.md', 'closure_transfer_campaign.py']]
    hashes = {str(p): sha(p) for p in sources}
    inputs = Path(args.inputs).resolve()
    inventory = json.loads((inputs/'inventory.json').read_text())
    progress = dict(status='running', phase=0, inputs=str(inputs),
                    execution_receipt=str(Path(args.execution_receipt).resolve()),
                    source_sha256=hashes, attempts=[], active=[], skipped=[],
                    integration_seconds=charged, global_cap_seconds=21600,
                    per_attempt_cap_seconds=1800, backend=args.backend,
                    command=sys.argv, started_epoch=time.time())
    env = dict(os.environ, CUBLAS_WORKSPACE_CONFIG=':4096:8',
               OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1',
               PYTHONDONTWRITEBYTECODE='1')
    cells = [(a,t,p) for a,t in sorted(STEPS, key=STEPS.get) for p in (1,2,3)]
    completed = {}
    for level in range(3):
        progress['phase'] = level
        queue = [c for c in cells if level < 2 or
                 ((c,0) in completed and (c,1) in completed
                  and needs_refinement(completed[c,0],completed[c,1]))]
        active = {}
        while queue or active:
            for gpu, rec in list(active.items()):
                code = rec['process'].poll()
                if code is None:
                    continue
                rec['log'].close()
                summ = Path(rec['run'])/'summary.json'
                row = dict(run=rec['run'], cell=list(rec['cell']), level=level,
                           device=f'cuda:{gpu}', returncode=code)
                if summ.exists():
                    summary = json.loads(summ.read_text())
                    row.update({k:summary.get(k) for k in (
                        'status','fitted','step','training_mse','physical_time',
                        'steps','integration_seconds','initialization_sha256')})
                    row['summary_sha256'] = sha(summ)
                    if row.get('integration_seconds') is None:
                        row['integration_seconds'] = min(1800.,time.monotonic()-rec['start'])
                    expected = inventory['cases'][rec['cell'][0]+'__'+rec['cell'][1]]['finest']['initialization_sha256']
                    if row.get('initialization_sha256') != expected:
                        raise RuntimeError('Initialization mismatch: '+rec['run'])
                else:
                    row.update(status='process_failed',fitted=False,
                               integration_seconds=min(1800.,time.monotonic()-rec['start']))
                charged += row['integration_seconds']
                progress['attempts'].append(row)
                completed[rec['cell'],level] = row
                del active[gpu]
                print(json.dumps(row), flush=True)
            for gpu in (0,1):
                if gpu in active or not queue:
                    continue
                if charged + 1800*(len(active)+1) > 21600:
                    if not active:
                        progress['skipped'].extend(dict(cell=list(c),level=level,
                                                       reason='global_budget') for c in queue)
                        queue.clear()
                    continue
                for source, expected in hashes.items():
                    if sha(source) != expected:
                        raise RuntimeError('Frozen source changed: '+source)
                cell = queue.pop(0)
                activation, task, order = cell
                step = STEPS[activation,task]/2**level
                tag = f'{activation}__{task}__P{order}__level{level}'
                run = out/'runs'/tag
                command = [sys.executable,str(HERE/'closure_transfer_euler.py'),
                    '--activation',activation,'--task',task,'--P',str(order),
                    '--step',str(step),'--device',f'cuda:{gpu}','--out',str(run),
                    '--backend',args.backend,'--max-seconds','1800',
                    '--max-time','260','--max-steps','2200000','--target-mse','1e-8',
                    '--cases-json',str(inputs/'provenance/cases.json')]
                log = (out/'logs'/f'{tag}.log').open('w')
                proc = subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,env=env)
                active[gpu] = dict(process=proc,log=log,cell=cell,run=str(run),
                                   start=time.monotonic(),command=command)
                print('START '+tag+' '+f'cuda:{gpu}',flush=True)
            progress['active'] = [dict(cell=list(r['cell']),run=r['run'],
                                      device=f'cuda:{g}',pid=r['process'].pid,
                                      elapsed=time.monotonic()-r['start']) for g,r in active.items()]
            progress['integration_seconds'] = charged
            progress['reserved_seconds'] = 1800*len(active)
            write(out/'progress.json',progress)
            if active:
                time.sleep(1)
        if progress['skipped']:
            break
    progress['status'] = 'complete' if not progress['skipped'] else 'budget_limited'
    progress['finished_epoch'] = time.time()
    write(out/'progress.json',progress)
    print('CAMPAIGN '+progress['status'],flush=True)


if __name__ == '__main__':
    main()
