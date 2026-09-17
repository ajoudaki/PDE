"""Replay the original dense network with passive input-index Gram observation."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import numpy as np
import torch
import WIDE_GPU_20260914_NETWORK as original

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
HISTORICAL = ROOT/"data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z"
PLAN = STUDY/"GRAM_20260914_PLAN.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    temporary = path.with_suffix(path.suffix+".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def gram_of(h):
    values = h.double()
    return values.T @ values / h.shape[0]


def verify():
    original.setup("float64")
    rng = np.random.default_rng(7421)
    h = np.tanh(rng.normal(size=(9, 7)))
    results = []
    for device in ["cpu", "cuda"]:
        for dtype in [torch.float32, torch.float64]:
            tensor = torch.tensor(h, dtype=dtype, device=device)
            source = tensor.cpu().double().numpy()
            actual = gram_of(tensor).cpu().numpy()
            expected = np.array([[sum(source[i,a]*source[i,b] for i in range(9))/9
                                  for b in range(7)] for a in range(7)])
            np.testing.assert_allclose(actual, expected, atol=1e-13, rtol=1e-12)
            permuted = gram_of(tensor[torch.tensor([5,2,8,0,4,7,1,6,3], device=device)]).cpu().numpy()
            np.testing.assert_allclose(actual, permuted, atol=1e-13, rtol=1e-12)
            np.testing.assert_allclose(actual, actual.T, atol=1e-13)
            assert np.linalg.eigvalsh(actual).min() > -1e-12 and abs(actual).max() <= 1
            q = np.arange(1,8,dtype=float); q /= q.sum()
            np.testing.assert_allclose(q@np.diag(actual), np.sum(source**2*q)/9, atol=1e-13)
            results.append(dict(device=device,dtype=str(dtype),max_entry_oracle_error=float(abs(actual-expected).max())))
    return dict(status="passed", checks=results, source_sha256=sha(__file__), plan_sha256=sha(PLAN))


@torch.no_grad()
def worker(base, config):
    directory = base/"network"/config["name"]
    count, buffer, shape = 0, None, None
    old_observe = original.observe
    specification = np.load(base/"inputs.npz")
    total = len(specification["times"])
    m = len(specification[config["case"]+"_labels"])
    tolerance = 2e-6 if config["dtype"] == "float32" else 2e-11
    def observe(state,u,y,p,circle,initial):
        nonlocal count,buffer,shape
        row = old_observe(state,u,y,p,circle,initial)
        train = original.fields(state,u)
        panel = original.fields(state,circle)
        grams = torch.stack([gram_of(torch.cat((train[j],panel[j]),dim=1)) for j in [1,3]])
        array = grams.cpu().numpy()
        if buffer is None:
            shape = (total,)+array.shape
            buffer = np.lib.format.open_memmap(directory/"gram.npy",mode="w+",dtype=np.float64,shape=shape)
        assert np.isfinite(array).all()
        np.testing.assert_allclose(array,array.transpose(0,2,1),atol=2e-11,rtol=0)
        assert abs(array).max() <= 1+2e-11
        diagonal = np.diagonal(array[:,:m,:m],axis1=1,axis2=2)
        q=p.cpu().double().numpy()
        np.testing.assert_allclose(diagonal@q,row['raw_rms']**2,atol=tolerance,rtol=tolerance)
        buffer[count] = array
        count += 1
        if count % 25 == 0 or count == total:
            buffer.flush()
            write(directory/"gram_progress.json",dict(completed_observations=count,shape=shape))
        return row
    original.observe = observe
    try:
        original.run(base,config)
    finally:
        original.observe = old_observe
        if buffer is not None:
            buffer.flush()
        record_path = directory/"record.json"
        if record_path.exists():
            record = json.loads(record_path.read_text())
            record.update(gram_source_sha256=sha(__file__),gram_plan_sha256=sha(PLAN),
                gram_dependency_sha256=sha(Path(original.__file__)),gram_completed_observations=count,
                gram_shape=shape,gram_dtype="float64",gram_accumulation="float64",
                gram_panel_order="training inputs, then 128 circle inputs; no deduplication")
            if (directory/"gram.npy").exists():record['gram_sha256']=sha(directory/"gram.npy")
            if record['status']=='complete':
                assert count==total
                with np.load(directory/'observations.npz') as now, np.load(HISTORICAL/'network'/config['name']/'observations.npz') as before:
                    errors={key:float(np.max(np.abs(now[key]-before[key]))) for key in before.files}
                limit=2e-6 if config['dtype']=='float32' else 1e-10
                record.update(replay_maximum_differences=errors,replay_tolerance=limit,
                              replay_consistent=max(errors.values())<=limit)
            write(record_path,record)


def campaign(base):
    check=verify()
    write(base/'gram_network_verification.json',check)
    metadata=json.loads((base/'gram_campaign.json').read_text())
    configs=metadata['network_configs']
    start=time.monotonic()
    start_epoch=metadata['experiment_started_epoch']
    results=[];active={};pending=list(configs);spent=0.0
    write(base/'gram_network_campaign.json',dict(status='running',source_sha256=sha(__file__),
        dependency_sha256=sha(original.__file__),plan_sha256=sha(PLAN),configs=configs,command=sys.argv))
    def size():
        total=0
        for path in base.rglob('*'):
            try:
                if path.is_file():total+=path.stat().st_size
            except FileNotFoundError:
                pass  # Another worker may have atomically replaced a record.
        return total
    while pending or active:
        now=time.monotonic()
        budget=(time.time()-start_epoch>2400 or spent+sum(now-v[2] for v in active.values())>3600 or size()>4*1024**3)
        for gpu,(proc,config,launched,log) in list(active.items()):
            timeout=now-launched>600
            if proc.poll() is None and (timeout or budget):
                proc.terminate()
                try:proc.wait(timeout=5)
                except subprocess.TimeoutExpired:proc.kill();proc.wait()
            if proc.poll() is not None:
                elapsed=time.monotonic()-launched;spent+=elapsed
                result=dict(name=config['name'],gpu=gpu,exit_code=proc.returncode,wall_seconds=elapsed,budget_stop=budget or timeout)
                results.append(result);log.close();del active[gpu]
                if proc.returncode!=0:
                    path=base/'network'/config['name']/'record.json'
                    record=json.loads(path.read_text()) if path.exists() else dict(config)
                    record.update(status='failed',supervisor=result)
                    path.parent.mkdir(parents=True,exist_ok=True);write(path,record)
                print(json.dumps(result),flush=True)
        if budget:break
        for gpu in [1,0]:
            if gpu not in active and pending:
                config=pending.pop(0)
                env=dict(os.environ,CUDA_VISIBLE_DEVICES=str(gpu),OPENBLAS_NUM_THREADS='1',
                    OMP_NUM_THREADS='4',MKL_NUM_THREADS='4',PYTHONDONTWRITEBYTECODE='1')
                log=(base/(config['name']+'.log')).open('x')
                cmd=[sys.executable,str(Path(__file__).resolve()),'--output',str(base),'--worker',json.dumps(config)]
                proc=subprocess.Popen(cmd,env=env,stdout=log,stderr=subprocess.STDOUT)
                active[gpu]=(proc,config,time.monotonic(),log)
                print('Started '+config['name']+' on GPU '+str(gpu),flush=True)
        time.sleep(1)
    outcome=dict(status='complete' if len(results)==16 and all(x['exit_code']==0 for x in results) else 'incomplete',
        results=results,unstarted=[c['name'] for c in pending],worker_wall_seconds=spent,
        wall_seconds=time.monotonic()-start,source_sha256=sha(__file__),plan_sha256=sha(PLAN))
    write(base/'gram_network_campaign.json',outcome)
    print(json.dumps(outcome),flush=True)
    return 0 if outcome['status']=='complete' else 1


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    action=parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--campaign',action='store_true')
    action.add_argument('--worker')
    action.add_argument('--verify-only',action='store_true')
    args=parser.parse_args()
    if args.worker:worker(args.output,json.loads(args.worker))
    elif args.verify_only:print(json.dumps(verify(),indent=2))
    else:raise SystemExit(campaign(args.output))
