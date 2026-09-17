"""Prepare exact working inputs for the fixed thirty-degree comparison."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.dont_write_bytecode = True
import numpy as np

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT/'data/generated/wide_network_closure_comparison'
PLAN = STUDY/'ARC30_20260914_PLAN.md'
OLD = GENERATED/'GRAM_20260914_v1'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024**2), b''):
            h.update(block)
    return h.hexdigest()


def write(path, value):
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def encode(array):
    return dict(shape=list(array.shape), values=[float(v).hex() for v in array.flat])


def array_hash(array):
    return hashlib.sha256(json.dumps(encode(array), sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def configurations():
    net = [dict(name=f'arcs30_n{n}_s{s}', case='arcs30', width=n, seed=s,
                step=.01, dtype='float32', kind='primary')
           for n in (2048, 8192) for s in (11, 29, 47)]
    net += [dict(name='arcs30_n8192_s11_halfstep', case='arcs30', width=8192, seed=11,
                 step=.005, dtype='float32', kind='time_control'),
            dict(name='arcs30_n2048_s11_float64', case='arcs30', width=2048, seed=11,
                 step=.01, dtype='float64', kind='precision_control')]
    closure = []
    for n, q, p, h, suffix, kind in ((1,1024,512,'1/200','','primary'),
            (3,1024,512,'1/200','','primary'), (5,1024,512,'1/200','','primary'),
            (3,2048,1024,'1/200','_refined','quadrature_control'),
            (3,1024,512,'1/400','_halfstep','time_control'),
            (5,2048,1024,'1/200','_refined','quadrature_control'),
            (5,4096,2048,'1/200','_fine','quadrature_control'),
            (5,4096,2048,'1/400','_fine_halfstep','time_control')):
        closure.append(dict(id=f'arcs30_N{n}{suffix}', case='arcs30', order=n,
            initialization_nodes=q, population_nodes=p, step=h, refined=q>1024, kind=kind))
    return net, closure


def prepare(output):
    if output.exists():
        raise FileExistsError('Preparation requires a new destination')
    old_spec = json.loads((OLD/'inputs.json').read_text())
    if sha(OLD/'inputs.npz') != old_spec['npz_sha256']:
        raise ValueError('Historical input hash mismatch')
    with np.load(OLD/'inputs.npz') as old:
        arrays = {key: old[key].copy() for key in ('times', 'circle')}
        old_z = old['arcs_inputs'][:8,1] / (1+old['arcs_inputs'][:8,0])
    z = (2*np.arange(8)-7)/7 * math.tan(math.pi/12)
    positive = np.column_stack(((1-z*z)/(1+z*z), 2*z/(1+z*z)))
    negative = np.column_stack((-positive[:,1], positive[:,0]))
    u = np.concatenate((positive, negative))
    labels = np.r_[np.ones(8), -np.ones(8)]
    weights = np.full(16, 1/16)
    arrays.update(arcs30_inputs=u, arcs30_labels=labels, arcs30_probabilities=weights)
    angles = np.degrees(np.arctan2(u[:,1],u[:,0]))
    np.testing.assert_allclose(angles[[0,7,8,15]], [-30,30,60,120], atol=2e-14, rtol=0)
    np.testing.assert_allclose(u, np.column_stack((np.cos(np.radians(angles)), np.sin(np.radians(angles)))), atol=4e-16, rtol=0)
    np.testing.assert_allclose(np.sum(u*u,axis=1), 1, atol=4e-16, rtol=0)
    np.testing.assert_allclose(z/z[-1],old_z/old_z[-1],atol=3e-16,rtol=0)
    margin = np.min(labels*(u[:,0]-u[:,1])/math.sqrt(2))
    np.testing.assert_allclose(margin, math.sin(math.pi/12),atol=3e-16,rtol=0)
    gram = u@u.T
    metadata = dict(format='arc30-20260914-inputs-v1', plan_sha256=sha(PLAN),
        producer_sha256=sha(__file__), source_run=str(OLD), source_inputs_sha256=sha(OLD/'inputs.npz'),
        input_convention='Normalized u=x/sqrt(2); rows are samples',
        cases={'arcs30':dict(law_metadata=dict(scope='exploratory, no H4 time-40 guarantee',
            name='sixteen training directions with maximum 30-degree deviations',
            input_generation='z_j=(2j-7)/7*tan(pi/12), U(z); second cluster quarter-turn',
            labels='eight +1 then eight -1', weights='1/16', maximum_sample_deviation_degrees=30))},
        time_fractions=old_spec['time_fractions'], exact_arrays={k:encode(v) for k,v in arrays.items()},
        array_sha256={k:array_hash(v) for k,v in arrays.items()}, angles_degrees=angles.tolist(),
        validation=dict(status='passed', endpoint_degrees=angles[[0,7,8,15]].tolist(),
            max_unit_norm_error=float(np.max(np.abs(np.sum(u*u,axis=1)-1))),
            minimum_normalized_label_margin=float(margin), minimum_cross_cluster_dot=float(gram[:8,8:].min()),
            maximum_cross_cluster_dot=float(gram[:8,8:].max()), relative_parameter_spacing_preserved=True,
            circle_and_times_preserved=True))
    output.mkdir()
    with (output/'inputs.npz').open('xb') as stream:
        np.savez_compressed(stream, **arrays)
    metadata['npz_sha256']=sha(output/'inputs.npz')
    write(output/'inputs.json',metadata)
    net,closure=configurations()
    githead=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    gitstatus=subprocess.check_output(['git','status','--porcelain=v1'],cwd=ROOT,text=True)
    campaign=dict(status='prepared', plan_sha256=sha(PLAN), source_run=str(OLD),
        network_configs=net, closure_configs=closure, expected_runs=16,
        inputs_sha256=metadata['npz_sha256'], inputs_json_sha256=sha(output/'inputs.json'),
        experiment_started_epoch=None, prepared_utc=datetime.now(timezone.utc).isoformat(),
        prepare_command=sys.argv, prepare_source_sha256=sha(__file__), git_head=githead,git_status=gitstatus,
        preservation_manifest={str(p.relative_to(ROOT)):sha(p) for old_run in (OLD,GENERATED/'WIDE_GPU_20260914_202109Z')
                               for p in sorted(old_run.rglob('*')) if p.is_file()},
        old_study_sources={p.name:sha(p) for p in STUDY.iterdir() if p.is_file() and p.name!='README.md' and not p.name.startswith('ARC30_')},
        panel_order='16 training inputs then 128 original circle directions; no deduplication')
    write(output/'arc30_campaign.json',campaign)
    return dict(status='prepared', input_validation=metadata['validation'])


def transition(output, action):
    path=output/'arc30_campaign.json';value=json.loads(path.read_text())
    if action=='start':
        if value['status']!='prepared' or value['experiment_started_epoch'] is not None:
            raise ValueError('Cannot restart the campaign clock')
        paths=list(STUDY.glob('ARC30_20260914*.py'))+[PLAN]
        value.update(status='running',experiment_started_epoch=time.time(),
                     launch_source_hashes={p.name:sha(p) for p in paths})
    else:
        n=json.loads((output/'network_campaign.json').read_text())
        c=json.loads((output/'closure_campaign.json').read_text())
        value.update(status='complete' if n['status']==c['status']=='complete' else 'incomplete',
                     scientific_completion_recorded_epoch=time.time(),
                     network_campaign_sha256=sha(output/'network_campaign.json'),
                     closure_campaign_sha256=sha(output/'closure_campaign.json'))
    write(path,value)
    return dict(status=value['status'])


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--start',action='store_true');group.add_argument('--finish',action='store_true')
    args=parser.parse_args();output=args.output.resolve()
    if output.parent!=GENERATED.resolve() or not output.name.startswith('ARC30_'):
        raise ValueError('Output must be a fresh ARC30_* child of this study generated namespace')
    result=transition(output,'start' if args.start else 'finish') if args.start or args.finish else prepare(output)
    print(json.dumps(result,indent=2))
