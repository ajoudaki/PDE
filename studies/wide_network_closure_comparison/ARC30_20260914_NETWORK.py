"""Dense GPU trajectories for the fixed thirty-degree training data."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import numpy as np
import torch
import WIDE_GPU_20260914_NETWORK as original
import GRAM_20260914_NETWORK as previous_gram
import ARC30_20260914_PREPARE as preparation

STUDY=Path(__file__).resolve().parent
ROOT=STUDY.parents[1]
PLAN=STUDY/'ARC30_20260914_PLAN.md'
sha,write=preparation.sha,preparation.write
OUTPUT_CAP=4*1024**3


def sources():
    return {str(p.relative_to(ROOT)):sha(p) for p in (Path(__file__),PLAN,
        Path(original.__file__),Path(previous_gram.__file__),Path(preparation.__file__))}


def manifest(output, require_started=True):
    if output.parent!=preparation.GENERATED.resolve() or not output.name.startswith('ARC30_'):
        raise ValueError('Invalid ARC30 destination')
    value=json.loads((output/'arc30_campaign.json').read_text())
    if value['plan_sha256']!=sha(PLAN) or value['inputs_sha256']!=sha(output/'inputs.npz'):
        raise ValueError('Plan or input checksum mismatch')
    if value['network_configs']!=preparation.configurations()[0]:
        raise ValueError('Frozen network menu mismatch')
    if require_started and value['experiment_started_epoch'] is None:
        raise ValueError('Shared campaign clock has not started')
    return value


def size(output):
    total=0
    for p in output.rglob('*'):
        try:
            if p.is_file():total+=p.stat().st_size
        except FileNotFoundError:
            pass
    return total


def verification():
    original.setup('float64')
    finite=original.verification()
    grams=previous_gram.verify()
    return dict(status='passed', finite_equation_oracles=finite, gram_oracles=grams, source_hashes=sources())


@torch.no_grad()
def worker(output, config):
    shared=manifest(output)
    if config not in shared['network_configs']:
        raise ValueError('Configuration not in fixed menu')
    directory=output/'network'/config['name']
    original_observe,original_initialize=original.observe,original.initialize
    started=time.time();count=0;buffer=None;shape=(206,2,144,144)
    oldname=config['name'].replace('arcs30_','arcs_',1)
    historical=Path(shared['source_run'])/'network'/oldname/'record.json'
    old_record=json.loads(historical.read_text())
    tolerance=2e-6 if config['dtype']=='float32' else 2e-11

    def initialize(n,seed,dtype,device='cuda'):
        state,hashes=original_initialize(n,seed,dtype,device)
        if hashes!=old_record['initial_float64_block_hashes']:
            raise AssertionError('Changed-data experiment must retain the old random initialization')
        return state,hashes

    def observe(state,u,y,p,circle,initial):
        nonlocal buffer,count
        if time.time()-started>600 or time.time()-shared['experiment_started_epoch']>2400:
            raise TimeoutError('Frozen network/global wall cap')
        if size(output)>OUTPUT_CAP:
            raise RuntimeError('Frozen output cap')
        before=[v._version for v in state]
        row=original_observe(state,u,y,p,circle,initial)
        train=original.fields(state,u);panel=original.fields(state,circle)
        array=torch.stack([previous_gram.gram_of(torch.cat((train[j],panel[j]),dim=1))
                           for j in (1,3)]).cpu().numpy()
        assert before==[v._version for v in state]
        assert np.isfinite(array).all() and np.abs(array).max()<=1+2e-11
        np.testing.assert_allclose(array,array.transpose(0,2,1),atol=2e-11,rtol=0)
        diagonal=np.diagonal(array[:,:16,:16],axis1=1,axis2=2)
        np.testing.assert_allclose(diagonal@p.cpu().double().numpy(),row['raw_rms']**2,atol=tolerance,rtol=0)
        if buffer is None:
            buffer=np.lib.format.open_memmap(directory/'gram.npy',mode='w+',dtype=np.float64,shape=shape)
            buffer[:]=np.nan
        if count>=shape[0]:raise AssertionError('Too many observations')
        buffer[count]=array;count+=1
        if count%10==0 or count==shape[0]:
            buffer.flush()
            write(directory/'gram_progress.json',dict(completed_observations=count,shape=shape))
        return row

    original.observe,original.initialize=observe,initialize
    try:
        original.run(output,config)
    finally:
        original.observe,original.initialize=original_observe,original_initialize
        if buffer is not None:buffer.flush()
        record_path=directory/'record.json'
        if record_path.exists():
            record=json.loads(record_path.read_text())
            record.update(gram_source_sha256=sha(__file__),gram_plan_sha256=sha(PLAN),source_hashes=sources(),
                gram_completed_observations=count,gram_shape=shape,gram_accumulation='float64',
                gram_panel_order=shared['panel_order'],
                original_initialization_record=str(historical),original_initialization_record_sha256=sha(historical),
                original_initialization_matches=record.get('initial_float64_block_hashes')==old_record['initial_float64_block_hashes'],
                historical_scalar_replay='not applicable: training inputs changed',
                completed_at_epoch=time.time())
            if (directory/'gram.npy').exists():record['gram_sha256']=sha(directory/'gram.npy')
            if record['status']=='complete' and count!=206:
                record.update(status='failed',error='Incomplete Gram observation count')
            write(record_path,record)


def campaign(output):
    shared=manifest(output)
    path=output/'network_campaign.json'
    if path.exists():raise FileExistsError('Refusing to replace a prior campaign')
    check=verification();write(output/'network_verification.json',check)
    pending=list(shared['network_configs']);active={};finished=[];spent=0.;started=time.monotonic()
    write(path,dict(status='running',configs=pending,source_hashes=sources(),command=sys.argv))
    while pending or active:
        now=time.monotonic()
        budget=time.time()-shared['experiment_started_epoch']>2400 or spent+sum(now-v[2] for v in active.values())>2400 or size(output)>OUTPUT_CAP
        for gpu,(proc,config,launch,log) in list(active.items()):
            timeout=now-launch>600
            if proc.poll() is None and (budget or timeout):
                proc.terminate()
                try:proc.wait(timeout=5)
                except subprocess.TimeoutExpired:proc.kill();proc.wait()
            if proc.poll() is not None:
                elapsed=time.monotonic()-launch;spent+=elapsed
                row=dict(name=config['name'],gpu=gpu,exit_code=proc.returncode,wall_seconds=elapsed,budget_stop=budget or timeout)
                finished.append(row);log.close();del active[gpu]
                if proc.returncode!=0:
                    record_path=output/'network'/config['name']/'record.json'
                    record=json.loads(record_path.read_text()) if record_path.exists() else dict(config)
                    record.update(status='failed',supervisor=row)
                    record_path.parent.mkdir(parents=True,exist_ok=True);write(record_path,record)
                print(json.dumps(row),flush=True)
        if budget:break
        for gpu in (1,0):
            if gpu not in active and pending:
                config=pending.pop(0)
                env=dict(os.environ,CUDA_VISIBLE_DEVICES=str(gpu),OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='4',MKL_NUM_THREADS='4',PYTHONDONTWRITEBYTECODE='1')
                log=(output/(config['name']+'.log')).open('x')
                cmd=[sys.executable,str(Path(__file__).resolve()),'--output',str(output),'--worker',json.dumps(config)]
                proc=subprocess.Popen(cmd,env=env,stdout=log,stderr=subprocess.STDOUT,cwd=ROOT)
                active[gpu]=(proc,config,time.monotonic(),log)
                print('Started '+config['name']+' on GPU '+str(gpu),flush=True)
        time.sleep(1)
    result=dict(status='complete' if len(finished)==8 and all(r['exit_code']==0 for r in finished) else 'incomplete',
        results=finished,unstarted=[c['name'] for c in pending],worker_wall_seconds=spent,
        wall_seconds=time.monotonic()-started,completed_at_epoch=time.time(),source_hashes=sources(),command=sys.argv)
    write(path,result);print(json.dumps(result),flush=True)
    return 0 if result['status']=='complete' else 1


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--campaign',action='store_true');group.add_argument('--worker');group.add_argument('--verify-only',action='store_true')
    args=parser.parse_args();output=args.output.resolve()
    if args.worker:worker(output,json.loads(args.worker))
    elif args.verify_only:
        manifest(output,False);write(output/'network_verification.json',verification());print('Verification passed')
    else:raise SystemExit(campaign(output))
