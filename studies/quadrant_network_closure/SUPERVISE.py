"""Execute the fixed job menu with two GPU and two single-BLAS CPU workers."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def supervise(run):
    run = Path(run).resolve()
    if (run / 'supervision.json').exists():
        raise RuntimeError('Run was already supervised; do not overwrite')
    manifest = json.loads((run / 'manifest.json').read_text())
    for source, expected in manifest['sources_sha256'].items():
        if sha(ROOT / source) != expected:
            raise RuntimeError('Source changed after freeze: ' + source)
    if sha(run / 'inputs.npz') != manifest['inputs_sha256']:
        raise RuntimeError('Input hash changed')
    for name in ['network_check', 'closure_check']:
        report = json.loads((run / 'checks' / name / 'check.json').read_text())
        if not report.get('passed', False):
            raise RuntimeError('Correctness check missing or failed: ' + name)
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
               PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg', CUBLAS_WORKSPACE_CONFIG=':4096:8')
    slots = [('gpu0', 'network', 'cuda:0'), ('gpu1', 'network', 'cuda:1'),
             ('cpu0', 'closure', None), ('cpu1', 'closure', None)]
    queue = list(manifest['jobs'])
    active, results = {}, []
    start = time.monotonic()
    budget = manifest['budget']
    stop_reason = None
    try:
        hardware = subprocess.check_output(['nvidia-smi', '--query-gpu=index,name,memory.total,memory.free',
                                            '--format=csv'], text=True)
        (run / 'hardware.txt').write_text(hardware)
        while queue or active:
            elapsed = time.monotonic() - start
            size = sum(p.stat().st_size for p in run.rglob('*') if p.is_file())
            if elapsed > budget['total_seconds']:
                stop_reason = 'total_time_limit'
            if size > budget['output_bytes']:
                stop_reason = 'disk_output_limit'
            if shutil.disk_usage(run).free < budget['minimum_disk_free']:
                stop_reason = 'minimum_free_disk'
            if stop_reason:
                break
            for slot, kind, device in slots:
                if slot in active:
                    continue
                found = next((i for i, j in enumerate(queue) if j['kind'] == kind), None)
                if found is None:
                    continue
                job = queue.pop(found)
                command = [manifest['python'], '-B', str(HERE / ('NETWORK.py' if kind == 'network' else 'CLOSURE.py')),
                           '--inputs', str(run / 'inputs.npz'), '--out', str(run / job['id']), '--step', str(job['step'])]
                if kind == 'network':
                    command += ['--width', str(job['width']), '--seed', str(job['seed']),
                                '--dtype', job['dtype'], '--device', device]
                else:
                    command += ['--order', str(job['order']), '--initialization-nodes', str(job['initialization_nodes']),
                                '--population-nodes', str(job['population_nodes'])]
                log = open(run / (job['id'] + '.log'), 'w')
                process = subprocess.Popen(command, cwd=ROOT, env=env, stdout=log,
                                           stderr=subprocess.STDOUT, start_new_session=True)
                active[slot] = dict(job=job, command=command, log=log, process=process, started=time.monotonic())
                print(json.dumps(dict(event='started', id=job['id'], slot=slot)), flush=True)
            for slot, item in list(active.items()):
                age = time.monotonic() - item['started']
                process = item['process']
                timed_out = age > budget['worker_seconds']
                if timed_out and process.poll() is None:
                    os.killpg(process.pid, signal.SIGTERM)
                code = process.poll()
                if code is None:
                    continue
                item['log'].close()
                record = dict(id=item['job']['id'], command=item['command'], elapsed_seconds=age,
                              exit_code=code, timed_out=timed_out)
                results.append(record)
                del active[slot]
                print(json.dumps(dict(event='finished', **record)), flush=True)
                if code != 0:
                    stop_reason = 'worker_failed:' + record['id']
                    break
            if stop_reason:
                break
            time.sleep(1)
    finally:
        for item in active.values():
            if item['process'].poll() is None:
                os.killpg(item['process'].pid, signal.SIGTERM)
        for item in active.values():
            try:
                code = item['process'].wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(item['process'].pid, signal.SIGKILL)
                code = item['process'].wait()
            item['log'].close()
            results.append(dict(id=item['job']['id'], command=item['command'], exit_code=code,
                                elapsed_seconds=time.monotonic()-item['started'], interrupted=True))
        summary = dict(elapsed_seconds=time.monotonic()-start, results=results,
                       stop_reason=stop_reason, pending=[x['id'] for x in queue],
                       complete=stop_reason is None and len(results)==16 and all(x['exit_code']==0 for x in results))
        (run / 'supervision.json').write_text(json.dumps(summary, indent=2)+'\n')
        print(json.dumps(summary), flush=True)
    if not summary['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--run', required=True)
    supervise(p.parse_args().run)
