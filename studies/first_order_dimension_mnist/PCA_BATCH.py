"""Bounded PCA98 waves; one child process per GPU, preserved run directories."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'data/generated/first_order_dimension_mnist'
STEPS = {'network': .25, 'closure': .125}
MODELS = ('network', 'closure')


def job(model, dataset, output, *, seed=1729, horizon=600, half=False):
    return dict(task='mnist', model=model, width=4096, dtype='float32',
                step=STEPS[model] / (2 if half else 1), horizon=horizon,
                seed=seed, dataset=dataset, block=2048,
                max_seconds=850 if half else (180 if horizon == 100 else 600),
                output=output)


def execute(jobs, gpu):
    records = []
    for opts in jobs:
        log = BASE / (opts['output'].replace('/', '__') + '.log')
        command = [sys.executable, '-B', str(HERE / 'RUN.py'), '--gpu', str(gpu)]
        for key, value in opts.items():
            command.extend(['--' + key.replace('_', '-'), str(value)])
        start = time.perf_counter()
        with log.open('x') as handle:
            child = subprocess.run(command, stdout=handle, stderr=subprocess.STDOUT,
                                   timeout=opts['max_seconds'] + 90)
        record = dict(output=opts['output'], gpu=gpu, returncode=child.returncode,
                      seconds=time.perf_counter() - start, log=str(log), command=command)
        records.append(record)
        print(json.dumps(record), flush=True)
        if child.returncode:
            raise RuntimeError(f'Failed child: {log}')
        summary = json.loads((BASE / opts['output'] / 'summary.json').read_text())
        if summary['final_time'] != opts['horizon']:
            raise RuntimeError(f'Incomplete horizon: {log}')
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('wave', choices=['benchmark', 'gate', 'remaining'])
    args = parser.parse_args()
    groups = [[], []]
    if args.wave == 'benchmark':
        for repetition in (1, 2):
            representations = ('original', 'pca') if repetition == 1 else ('pca', 'original')
            for index, model in enumerate(('network', 'closure')):
                gpu = index if repetition == 1 else 1 - index
                for representation in representations:
                    data_name = 'data_3_5' if representation == 'original' else 'data_pca98'
                    groups[gpu].append(job(model, data_name,
                        f'pca_speed/{representation}_{model}_r{repetition}', horizon=100))
    elif args.wave == 'gate':
        for model, gpu in (('network', 1), ('closure', 0)):
            groups[gpu].append(job(model, 'data_pca98', f'pca4096/{model}_1729'))
            groups[gpu].append(job(model, 'data_pca98', f'pca_controls/{model}_halfstep', half=True))
    else:
        gate = json.loads((BASE / 'pca_checks/halfstep_gate.json').read_text())
        assert gate['passed'], 'Full-horizon numerical gate must pass before remaining seeds'
        # After the numerical gate, balance the two expensive network runs
        # across both devices, followed by one short closure run on each.
        for gpu, seed in enumerate((2718, 3141)):
            for model in MODELS:
                groups[gpu].append(job(model, 'data_pca98', f'pca4096/{model}_{seed}', seed=seed))
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(execute, jobs, gpu) for gpu, jobs in enumerate(groups)]
        result = [future.result() for future in futures]
    with (BASE / f'pca_{args.wave}_execution.json').open('x') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')


if __name__ == '__main__':
    main()
