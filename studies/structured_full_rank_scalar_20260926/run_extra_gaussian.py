"""One extra matched-outer Gaussian draw; live loss and cooperative stop.

Uses the existing dense vector field and RK45 integrator without changes.
Create OUTPUT/STOP to save the next accepted state and end training.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'

import argparse
import hashlib
import json
import platform
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import scipy
import dense_compare as dense
from circle_tasks import BY_NAME, directions
from dense_wide_integrator import integrate


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def write_json(path, value):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    tmp.replace(path)


def initialize(width, outer_seed, middle_seed):
    state = dense.initialize(width, middle_seed, 'gaussian')
    w = dense._rng(outer_seed, 1).standard_normal((width, 2))
    c = dense._rng(outer_seed, 2).standard_normal(width) / width
    return dense.State(w, state.W, c)


class StopRequested(Exception):
    pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    p.add_argument('--width', type=int, default=8192)
    p.add_argument('--outer-seed', type=int, default=0)
    p.add_argument('--middle-seed', type=int, default=1)
    p.add_argument('--wall-minutes', type=float, default=40.)
    args = p.parse_args()
    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=False)
    started = time.time()
    deadline = started + 60 * args.wall_minutes
    source = Path(__file__).resolve().parent
    snapshot = out / 'source_snapshot'
    snapshot.mkdir()
    files = ('run_extra_gaussian.py', 'dense_compare.py', 'dense_wide_integrator.py', 'circle_tasks.py')
    for name in files:
        shutil.copyfile(source / name, snapshot / name)
    task = BY_NAME['cluster_triple_cos9']
    u, y = task.data()
    config = vars(args) | {
        'output': str(out), 'task': task.name, 'started': started, 'deadline': deadline,
        'command': sys.argv, 'cwd': str(Path.cwd()), 'target': 1e-4, 'grid': 4096,
        'rtol': 1e-5, 'atol': 1e-8, 'blas_threads': 1,
        'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__,
        'cpu_count': os.cpu_count(), 'middle_rng': [args.middle_seed, 101],
        'outer_rngs': [[args.outer_seed, 1], [args.outer_seed, 2]],
        'train_angles': list(task.angles), 'train_labels': y.tolist(),
        'sources': {name: digest(source / name) for name in files},
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    }
    write_json(out / 'manifest.json', config)
    requested = False

    def request_stop(signum, frame):
        nonlocal requested
        requested = True

    signal.signal(signal.SIGINT, request_stop)
    signal.signal(signal.SIGTERM, request_stop)
    state = initialize(args.width, args.outer_seed, args.middle_seed)
    offset = 0.
    last = {'time': 0., 'state': state}
    history, segments = [], []
    last_log = 0.
    max_rise = 0.
    previous_loss = None

    def callback(t, accepted, mse):
        nonlocal last_log, max_rise, previous_loss
        at = offset + t
        last.update(time=at, state=accepted)
        if previous_loss is not None:
            max_rise = max(max_rise, mse - previous_loss)
        previous_loss = mse
        history.append((at, mse))
        stopping = requested or (out / 'STOP').exists()
        now = time.time()
        if now - last_log >= 30 or stopping or mse <= 1e-4:
            live = {'time': at, 'train_mse': mse, 'wall_minutes': (now - started) / 60,
                    'stop_requested': stopping, 'accepted_callbacks': len(history)}
            write_json(out / 'live.json', live)
            print(json.dumps(live), flush=True)
            last_log = now
        if stopping:
            raise StopRequested()

    reason = 'time_cap'
    bracket = None
    try:
        for horizon in (3000., 10000.):
            result = integrate(state, u, y, time_cap=horizon - offset,
                rtol=1e-5, atol=1e-8, target_train_mse=1e-4, deadline=deadline,
                max_step=10., callback=callback)
            segments.append({'start_time': offset, 'duration': result.time,
                'nfev': result.nfev, 'nsteps': result.nsteps, 'nreject': result.nreject,
                'stop_reason': result.stop_reason, 'settings': result.settings})
            if result.first_target_bracket is not None:
                bracket = [offset + t for t in result.first_target_bracket]
            offset += result.time
            state, reason = result.state, result.stop_reason
            max_rise = max(max_rise, result.max_loss_rise)
            if reason != 'time_cap':
                break
    except StopRequested:
        offset, state, reason = last['time'], last['state'], 'user_stop'

    training = dense._forward(state, u).output
    mse = float(np.mean((training - y) ** 2))
    angles = 2 * np.pi * np.arange(4096) / 4096
    points = directions(angles)
    prediction = np.concatenate([dense._forward(state, points[j:j+256]).output
                                 for j in range(0, len(points), 256)])
    data = out / 'gaussian_third.npz'
    np.savez(data, angles=angles, prediction=prediction, train_angles=task.angles,
        train_labels=y, train_prediction=training, history=np.asarray(history),
        final_w=state.w, final_W=state.W, final_c=state.c)
    fitted = bool(reason == 'target' and mse <= 1e-4 * (1 + 1e-7))
    record = {'status': 'ok' if fitted else 'partial', 'fitted': fitted, 'time': offset,
        'train_mse': mse, 'stop_reason': reason, 'first_target_bracket': bracket,
        'max_loss_rise': max_rise, 'segments': segments, 'data_file': data.name,
        'data_sha256': digest(data), 'wall_seconds': time.time() - started}
    write_json(out / 'result.json', record)
    write_json(out / 'artifact_hashes.json', {q.name: digest(q) for q in out.iterdir()
        if q.is_file() and q.name != 'artifact_hashes.json'})
    print(json.dumps(record), flush=True)


if __name__ == '__main__':
    main()
