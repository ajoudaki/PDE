"""Export all four primary higher-order handoffs and check standalone evaluation."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(run, output):
    begin = time.perf_counter()
    output.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).resolve()
    evaluator = source.parent/'evaluate_circle_scalar.py'
    shutil.copy2(source, output/source.name)
    shutil.copy2(evaluator, output/evaluator.name)
    records = json.loads((run/'results.json').read_text())['results']
    results = []
    environment = os.environ.copy()
    for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS'):
        environment[name] = '2'
    for record in records:
        case, order = record['case'], int(record['order'])
        directory = run/case/f'q{order}'/record['selected']
        handoff_path = directory/'handoff_0.01.npz'
        h = np.load(handoff_path)
        curves = np.load(directory/'curves.npz')
        model = {key: h[key] for key in ('matrix','drift','fourier')}
        model['initial_state'] = np.r_[h['residual'], np.zeros(9)]
        assert sum(a.size for a in model.values()) == 729
        destination = output/case/f'q{order}'
        destination.mkdir(parents=True)
        np.savez_compressed(destination/'model.npz', **model)
        np.save(destination/'angles.npy', curves['angles'])
        times = curves['scalar_times_0.01']
        duration = float(times[-1]-times[0])
        command = [sys.executable, str((output/evaluator.name).resolve()), 'evaluate',
                   '--model', 'model.npz', '--duration', str(duration),
                   '--angles', 'angles.npy', '--samples', str(len(times)),
                   '--output', 'evaluation.npz']
        child = subprocess.run(command, cwd=destination, env=environment,
                               capture_output=True, text=True, check=True, timeout=60)
        (destination/'evaluation.stdout.txt').write_text(child.stdout)
        result = np.load(destination/'evaluation.npz')
        errors = dict(endpoint_state_max=float(np.max(np.abs(result['state'][-1]-curves['scalar_state_0.01'][-1]))),
                      endpoint_circle_max=float(np.max(np.abs(result['circle_output']-curves['scalar_output_0.01']))))
        assert max(errors.values()) < 1e-8, errors
        metadata = dict(case=case, order=order, moving_numbers=17, fixed_numbers=712,
                        total_numbers=729, elapsed_duration=duration, errors=errors,
                        model_sha256=digest(destination/'model.npz'),
                        handoff_sha256=digest(handoff_path),
                        evaluator_sha256=digest(evaluator),
                        limitation='Terminal continuation; the full order-q closure produced the handoff.',
                        standalone_command=command)
        (destination/'provenance.json').write_text(json.dumps(metadata, indent=2)+'\n')
        results.append(metadata)
    payload = dict(passed=True, models=results, source_sha256=digest(source),
                   wall_seconds=time.perf_counter()-begin)
    (output/'checks.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    main(arguments.run.resolve(), arguments.output.resolve())
