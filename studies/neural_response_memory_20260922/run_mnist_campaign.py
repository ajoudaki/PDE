"""Two-device launcher with fixed jobs; logs and receipts remain study-owned."""
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--phase', choices=['pilot', 'primary'], required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--dataset', type=Path, required=True)
    parser.add_argument('--width', type=int, default=1024)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).with_name('mnist_moment_run.py')
    jobs = Queue()
    if args.phase == 'pilot':
        configs = [('dense', 1, 0), ('moment', 3, 0)]
    else:
        configs = [('dense', 1, 0), ('moment', 3, 0), ('moment', 2, 0),
                   ('moment', 1, 0), ('dense', 1, 1), ('moment', 3, 1),
                   ('moment', 2, 1), ('moment', 1, 1)]
    for config in configs:
        jobs.put(config)
    records = []
    lock = threading.Lock()

    def save():
        (args.out/'campaign.json').write_text(json.dumps(records, indent=2)+'\n')

    def worker(gpu):
        while True:
            try:
                model, order, level = jobs.get_nowait()
            except Empty:
                return
            name = (f'P{order}' if model == 'moment' else 'dense')+f'_level{level}'
            command = [sys.executable, '-B', str(source), '--dataset', str(args.dataset),
                '--out', str(args.out/name), '--model', model, '--order', str(order),
                '--width', str(args.width), '--device', f'cuda:{gpu}',
                '--rtol', str(2e-4/4**level), '--wall-seconds',
                '30' if args.phase == 'pilot' else '600']
            if args.phase == 'pilot':
                command += ['--max-steps', '30']
            record = dict(name=name, device=gpu, command=command,
                          started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
            with lock:
                records.append(record)
                save()
            print(json.dumps(dict(event='launch', **record)), flush=True)
            started = time.monotonic()
            with (args.out/(name+'.log')).open('w') as log:
                result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                        env=os.environ.copy())
            with lock:
                record.update(exit_code=result.returncode, process_seconds=time.monotonic()-started)
                save()
            print(json.dumps(dict(event='exit', **record)), flush=True)

    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(worker, gpu) for gpu in (0, 1)]
        for future in futures:
            future.result()
    if any(record['exit_code'] != 0 for record in records):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
