"""Freeze the four-cluster inputs, job menu and source provenance."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PYTHON = '/home/amir/miniconda3/bin/python'


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def prepare(out):
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    if shutil.disk_usage(out).free < 5 * 1024**3:
        raise RuntimeError('Insufficient free disk for the declared run')
    for name in ('NETWORK.py', 'CLOSURE.py', 'SUPERVISE.py'):
        if not (HERE / name).is_file():
            raise RuntimeError('Finish implementation before freezing: ' + name)
    degrees = np.concatenate([np.linspace(a, b, 4) for a, b in
                              [(0, 5), (25, 35), (55, 65), (85, 90)]])
    theta = np.deg2rad(degrees)
    labels = np.repeat([1., -1., 1., -1.], 4)
    circle = np.arange(128) * (2 * np.pi / 128)
    panel = np.concatenate([theta, circle])
    uniform_dense = np.arange(1440) * (2 * np.pi / 1440)
    dense = np.unique(np.concatenate([uniform_dense, theta]))
    unit = lambda x: np.column_stack([np.cos(x), np.sin(x)])
    times = np.arange(201) * .5
    assert len(np.unique(theta)) == 16 and theta.min() >= 0 and theta.max() <= np.pi / 2
    np.savez(out / 'inputs.npz', train_u=unit(theta), labels=labels,
             train_theta=theta, train_degrees=degrees, probabilities=np.full(16, 1/16),
             panel_u=unit(panel), panel_theta=panel, dense_u=unit(dense), dense_theta=dense,
             dense_uniform_indices=np.searchsorted(dense, uniform_dense), times=times)
    jobs = []
    # Start the larger primary networks first, evenly occupying the two GPUs.
    for width in (8192, 2048):
        for seed in (11, 29, 47):
            jobs.append(dict(id=f'net_n{width}_s{seed}', kind='network',
                             width=width, seed=seed, step=.01, dtype='float32'))
    jobs.extend([
        dict(id='net_n8192_s11_half', kind='network', width=8192, seed=11, step=.005, dtype='float32'),
        dict(id='net_n2048_s11_double', kind='network', width=2048, seed=11, step=.01, dtype='float64')])
    for resolution, q, p in [('base', 2048, 1024), ('fine', 4096, 2048)]:
        for order in (1, 3, 5):
            jobs.append(dict(id=f'cl_N{order}_{resolution}', kind='closure', order=order,
                             initialization_nodes=q, population_nodes=p, step=.01))
    jobs.extend([
        dict(id='cl_N3_base_half', kind='closure', order=3, initialization_nodes=2048, population_nodes=1024, step=.005),
        dict(id='cl_N5_fine_half', kind='closure', order=5, initialization_nodes=4096, population_nodes=2048, step=.005)])
    sources = [HERE / name for name in ('NETWORK.py', 'CLOSURE.py', 'PREPARE.py',
               'SUPERVISE.py', 'README.md', 'EXPERIMENT_PLAN.md')]
    sources += list((ROOT / 'code/pde').glob('*.py'))
    sources += [ROOT / 'AGENTS.md', ROOT / 'RESEARCH_WORKFLOW.md', ROOT / 'docs/README.md',
                ROOT / 'docs/NOTATION.md', ROOT / 'code/README.md']
    manifest = dict(created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                    cwd=str(ROOT), python=PYTHON, python_version=sys.version, numpy=np.__version__,
                    platform=platform.platform(), jobs=jobs,
                    inputs_sha256=sha(out / 'inputs.npz'),
                    sources_sha256={str(p.relative_to(ROOT)): sha(p) for p in sorted(sources)},
                    head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
                    status=subprocess.check_output(['git', 'status', '--short'], cwd=ROOT, text=True),
                    preparation_command=[sys.executable, '-B', str(Path(__file__).resolve()), '--out', str(out)],
                    budget=dict(total_seconds=1200, worker_seconds=600, max_jobs=16,
                                output_bytes=8*1024**3, minimum_disk_free=3*1024**3),
                    data=dict(train_degrees=degrees.tolist(), labels=labels.tolist(),
                              unit_directions=True, physical_input_factor=float(np.sqrt(2))))
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(dict(output=str(out), jobs=len(jobs), dense_points=len(dense),
                          input_hash=manifest['inputs_sha256'])), flush=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    prepare(ap.parse_args().out)
