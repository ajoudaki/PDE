"""Frozen two-GPU schedule for the 100-image width4096 continuation."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
from queue import Queue, Empty
import subprocess
import sys
import threading
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', choices=['pilot', 'primary', 'refine', 'repeat'], required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--dataset', type=Path, required=True)
    parser.add_argument('--models', nargs='+', choices=['dense', 'P1', 'P2', 'P3'])
    parser.add_argument('--level', type=int, choices=[0, 1, 2], default=2)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).with_name('mnist_moment_run.py')
    if args.phase == 'pilot':
        configs = [('dense', 0), ('P3', 0)]
    elif args.phase == 'primary':
        configs = [(name, level) for level in (0, 1) for name in ('dense', 'P3', 'P2', 'P1')]
    else:
        if not args.models:
            parser.error('--models required for refine/repeat')
        if args.phase == 'refine' and args.level != 2:
            parser.error('refine requires level2')
        configs = [(name, args.level) for name in args.models]
    jobs = Queue()
    for config in configs:
        jobs.put(config)
    records, lock = [], threading.Lock()

    def save():
        (args.out/'campaign.json').write_text(json.dumps(records, indent=2)+'\n')

    def worker(gpu):
        while True:
            try:
                name, level = jobs.get_nowait()
            except Empty:
                return
            target = f'{name}_level{level}'
            command = [sys.executable, '-B', str(source), '--dataset', str(args.dataset),
                '--out', str(args.out/target), '--model', 'dense' if name == 'dense' else 'moment',
                '--order', '1' if name == 'dense' else name[1:], '--width', '4096',
                '--device', f'cuda:{gpu}', '--rtol', str(1.25e-5/4**level),
                '--wall-seconds', '30' if args.phase == 'pilot' else '600']
            if args.phase == 'pilot':
                command += ['--max-steps', '30']
            record = dict(name=target, device=gpu, command=command,
                          started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
            with lock:
                records.append(record)
                save()
            print(json.dumps(dict(event='launch', **record)), flush=True)
            started = time.monotonic()
            with (args.out/(target+'.log')).open('w') as log:
                result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                        env=os.environ.copy())
            with lock:
                record.update(exit_code=result.returncode, process_seconds=time.monotonic()-started)
                save()
            print(json.dumps(dict(event='exit', **record)), flush=True)

    with ThreadPoolExecutor(max_workers=2) as pool:
        for future in [pool.submit(worker, gpu) for gpu in (0, 1)]:
            future.result()
    if any(record['exit_code'] != 0 for record in records):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
