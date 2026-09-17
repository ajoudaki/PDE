#!/usr/bin/env python3
"""Declared XOR inputs and immutable experiment preparation; no trajectories."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def write(path, obj):
    with Path(path).open('x') as f:
        json.dump(obj, f, indent=2, allow_nan=False); f.write('\n')


def prepare(output):
    output.mkdir(parents=True, exist_ok=False)
    centers = np.array([0., 90., 150., 240.])
    offsets = np.array([-5., -5/3, 5/3, 5.])
    degrees = (centers[:, None] + offsets).ravel()
    angles = np.deg2rad(degrees)
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    labels = np.repeat([1., -1., 1., -1.], 4)
    weights = np.full(16, 1/16)
    circle_angles = np.arange(128)*2*np.pi/128
    circle = np.column_stack((np.cos(circle_angles), np.sin(circle_angles)))
    panel = np.vstack((inputs, circle))
    times = np.arange(201)/2
    assert np.max(np.abs(np.sum(inputs**2, axis=1)-1)) < 1e-14
    same_label = (labels[:, None] == labels[None, :]) & ~np.eye(16, dtype=bool)
    antipodal_distance = np.linalg.norm(inputs[:, None] + inputs[None, :], axis=2)
    assert antipodal_distance[same_label].min() > 0.3
    poles = inputs.reshape(4, 4, 2).mean(axis=1)
    a, b, c, d = poles[0], poles[2], poles[1], poles[3]
    fractions = np.linalg.solve(np.column_stack((b-a, -(d-c))), c-a)
    assert np.all((0 < fractions) & (fractions < 1))
    intersection_error = float(np.max(np.abs(a+fractions[0]*(b-a)-c-fractions[1]*(d-c))))
    assert intersection_error < 1e-14
    derivative_bound = 4 + 4/math.sqrt(3)
    margin_bound = 1-derivative_bound*math.pi/36
    assert margin_bound > 0.4
    np.savez(output/'inputs.npz', inputs=inputs, labels=labels, weights=weights,
             panel=panel, times=times, angles_degrees=degrees, circle_angles=circle_angles)
    write(output/'inputs.json', {
        'centers_degrees': centers.tolist(), 'offsets_degrees': ['-5','-5/3','5/3','5'],
        'angles_degrees': degrees.tolist(), 'labels': labels.tolist(),
        'inputs_hex': [[float(v).hex() for v in row] for row in inputs],
        'weights_hex': [float(v).hex() for v in weights],
        'panel_order': 'training 0:16; uniform passive circle 16:144',
        'physical_input': 'x=sqrt(2)*u; stored directions u have unit norm',
        'seed': None, 'sampling': 'fixed equally spaced offsets; no random input draws',
        'same_label_antipodal_minimum_distance': float(antipodal_distance[same_label].min()),
        'same_label_arc_minimum_angular_distance_from_antipodes_degrees': 20,
        'linear_nonseparability': {
            'method': 'Segments between class pole means intersect strictly internally.',
            'segment_fractions': fractions.tolist(), 'residual': intersection_error,
            'intersection': (a+fractions[0]*(b-a)).tolist()},
        'odd_nonlinear_separator': {
            'formula': 's(theta)=cos(theta)+sin(theta)/sqrt(3)+(1+1/sqrt(3))*sin(3*theta)',
            'center_values': [1,-1,1,-1], 'global_derivative_bound': derivative_bound,
            'signed_margin_lower_bound_on_all_four_arcs': margin_bound,
            'meaning': 'Parity-compatible nonlinear classification; not a fitted network or learning guarantee.'},
        'source_sha256': sha(__file__), 'numpy_version': np.__version__})
    networks = [dict(name=f'n{n}_s{s}', width=n, seed=s, step=0.01, dtype='float32')
                for n in (2048,8192) for s in (11,29,47)]
    networks += [dict(name='n8192_s11_half', width=8192, seed=11, step=0.005, dtype='float32'),
                 dict(name='n2048_s11_float64', width=2048, seed=11, step=0.01, dtype='float64')]
    closures = [dict(name=f'N{n}_{suffix}', order=n, initialization_nodes=q,
                     population_nodes=p, step=0.01)
                for n in (1,3,5) for suffix,q,p in [('base',2048,1024),('fine',4096,2048)]]
    closures += [dict(name='N3_base_half', order=3, initialization_nodes=2048,population_nodes=1024,step=0.005),
                 dict(name='N5_fine_half', order=5, initialization_nodes=4096,population_nodes=2048,step=0.005)]
    manifest = {
        'status': 'prepared', 'scientific_start_epoch': None,
        'network_runs': networks, 'closure_runs': closures,
        'inputs_sha256': sha(output/'inputs.npz'), 'inputs_json_sha256': sha(output/'inputs.json'),
        'plan_sha256': sha(STUDY/'EXPERIMENT_PLAN.md'), 'source_hashes': {},
        'git_head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'git_status': subprocess.check_output(['git','status','--short','--','code/pde','docs','studies/xor_network_closure'],cwd=ROOT,text=True),
        'prepare_command': ['python',str(Path(__file__).relative_to(ROOT)),'--output',str(output),'--prepare'],
        'cwd': str(ROOT), 'horizon':100, 'time_count':201,
        'limits': {'global_seconds':1200,'worker_seconds':600,'generated_bytes':8*1024**3,'minimum_disk_free_bytes':3*1024**3}}
    write(output/'manifest.json',manifest)
    print(json.dumps({'status':'prepared','output':str(output),'geometry': 'nonlinear and parity-compatible',
                      'odd_separator_margin_bound':margin_bound,'network_runs':8,'closure_runs':8}))


def freeze(output):
    path = output/'manifest.json'
    m = json.loads(path.read_text())
    assert m['status']=='prepared' and m['scientific_start_epoch'] is None
    assert sha(output/'inputs.npz') == m['inputs_sha256']
    assert sha(STUDY/'EXPERIMENT_PLAN.md') == m['plan_sha256']
    files = [STUDY/name for name in ['PREPARE.py','SUPERVISE.py','NETWORK.py','CLOSURE.py','EXPERIMENT_PLAN.md']]
    files += [ROOT/'docs/NOTATION.md', ROOT/'code/README.md']
    files += sorted((ROOT/'code/pde').glob('*.py'))
    m['source_hashes'] = {str(p.relative_to(ROOT)): sha(p) for p in files}
    m['scientific_start_epoch'] = time.time()
    m['status'] = 'frozen'
    write(output/'manifest_prepared.json',json.loads(path.read_text()))
    path.write_text(json.dumps(m,indent=2)+'\n')
    write(output/'manifest_frozen.json',m)
    print(json.dumps({'status':'frozen','producer_count':len(files),'scientific_start_epoch':m['scientific_start_epoch']}))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True)
    mode=parser.add_mutually_exclusive_group(required=True); mode.add_argument('--prepare',action='store_true'); mode.add_argument('--freeze',action='store_true')
    args=parser.parse_args(); (prepare if args.prepare else freeze)(args.output.resolve())
