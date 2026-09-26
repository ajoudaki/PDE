"""One preregistered task, archived initialization, simultaneous factor GF."""
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
for key in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS'):
    os.environ.setdefault(key, '1')
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
import numpy as np
import torch
from trainable_dictionary import NAMES, State, blend, heun_trial, loss, predict, validate

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
INITIAL = ROOT/'data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/two_outliers_alternating_new_p3/arrays.npz'
REFERENCE = ROOT/'data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/two_outliers_alternating_full/arrays.npz'
SNAPSHOTS = [0,1,2,5,10,20,40,80,160,300,600,1200,2500,5000,10000]


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def save_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def array_sha(x):
    return hashlib.sha256(np.ascontiguousarray(x).tobytes()).hexdigest()


@torch.no_grad()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', required=True)
    parser.add_argument('--rtol', type=float, required=True)
    parser.add_argument('--wall-limit', type=float, default=180)
    parser.add_argument('--frozen', action='store_true')
    args = parser.parse_args()
    if args.rtol not in (6.25e-5,1.5625e-5,3.90625e-6):
        parser.error('tolerance outside protocol')
    if not 0 < args.wall_limit <= (100 if args.frozen else 180):
        parser.error('wall limit outside protocol')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.cuda.reset_peak_memory_stats(device)
    worker_start = time.monotonic()
    with np.load(INITIAL, allow_pickle=False) as a:
        initial_arrays = {k:a[k][0].copy() if k in ('w','c','M') else a[k].copy() for k in NAMES}
        inputs_np, labels_np = a['training_inputs'].copy(), a['labels'].copy()
        grid_np, grid_angles = a['circle_inputs'].copy(), a['circle_angles'].copy()
        end_grid_np, end_angles = a['endpoint_inputs'].copy(), a['endpoint_angles'].copy()
        archived_initial_output = a['circle_predictions'][0].copy()
    initial = State(*(torch.tensor(initial_arrays[k], device=device) for k in NAMES))
    inputs = torch.tensor(inputs_np, device=device, dtype=torch.float64)
    labels = torch.tensor(labels_np, device=device, dtype=torch.float64)
    grid, end_grid = (torch.tensor(v,device=device) for v in (grid_np,end_grid_np))
    validate(initial)
    assert initial.w.shape == (2048,2) and initial.b1.shape == (2048,6) and initial.b2.shape == (2048,12)
    initial_error = float(np.max(np.abs(predict(initial,grid).cpu().numpy()-archived_initial_output)))
    assert initial_error <= 1e-12
    with np.load(REFERENCE, allow_pickle=False) as a:
        assert np.array_equal(end_grid_np,a['endpoint_inputs'])
        assert np.array_equal(inputs_np,a['training_inputs']) and np.array_equal(labels_np,a['labels'])
        reference_output = a['endpoint_prediction'].copy()
    config = dict(case='two_outliers_alternating',width=2048,p=3,k1=6,k2=12,seed=20260920,
        train_basis=not args.frozen,metric='population L2 w,c,b1,b2; Frobenius M; unhalved probability MSE',
        mobilities=dict(w=2048,c=2048,M=1,b1=0 if args.frozen else 2048,b2=0 if args.frozen else 2048),
        trainable_scalars=6216 if args.frozen else 43080,model_storage_scalars=43080,
        rtol=args.rtol,atol=args.rtol/100,threshold=.001,initial_step=.05,max_step=2,min_step=1e-7,
        max_time=10000,max_steps=30000,integration_wall_limit=args.wall_limit,block_size=256,
        initial_archive=str(INITIAL),initial_archive_sha256=sha(INITIAL),
        initial_array_sha256={k:array_sha(v) for k,v in initial_arrays.items()},
        initial_prediction_replay_max=initial_error,reference_archive=str(REFERENCE),reference_sha256=sha(REFERENCE),
        source_hashes={str(HERE/name):sha(HERE/name) for name in
            ('trainable_dictionary.py','run_trainable_p3.py','TRAINABLE_P3_PROTOCOL.md')},
        python=sys.version,executable=sys.executable,torch=str(torch.__version__),numpy=np.__version__,
        device=str(device),gpu=torch.cuda.get_device_name(device),dtype='float64',threads=1,
        deterministic=True,tf32=False,command=sys.argv,cwd=str(Path.cwd()),
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(args.out/'config.json',config)
    state = initial.clone()
    snapshot_times, outputs, states = [], [], []
    times, losses, steps, errors = [0.], [float(loss(state,inputs,labels))], [], []
    t,h,rejected,next_snapshot = 0.,.05,0,1
    start,next_progress = time.monotonic(),time.monotonic()+25
    status = 'time_cap'
    def snapshot():
        snapshot_times.append(t)
        outputs.append(predict(state,grid).cpu().numpy())
        states.append(state.numpy())
    snapshot()
    try:
        while t < 10000-1e-9 and losses[-1] > .001:
            if time.monotonic()-start > args.wall_limit:
                status = 'wall_cap'
                break
            if len(steps) >= 30000:
                status = 'step_cap'
                break
            if time.monotonic() >= next_progress:
                print(json.dumps(dict(progress=args.out.name,time=t,loss=losses[-1],steps=len(steps),seconds=time.monotonic()-start)),flush=True)
                next_progress = time.monotonic()+25
            h = min(h,2.,10000-t,SNAPSHOTS[next_snapshot]-t)
            try:
                candidate,error = heun_trial(state,inputs,labels,h,initial.M,args.rtol,args.rtol/100,train_basis=not args.frozen)
                candidate_loss = float(loss(candidate,inputs,labels))
                if not math.isfinite(candidate_loss) or not math.isfinite(error):
                    raise ValueError('nonfinite trial')
            except (ValueError,RuntimeError):
                rejected += 1
                h *= .25
                if h < 1e-7:
                    raise
                continue
            if error > 1 or candidate_loss > losses[-1]*(1+1e-8)+1e-12:
                rejected += 1
                h *= max(.1,min(.5,.9/math.sqrt(max(error,1e-16))))
                if h < 1e-7:
                    raise RuntimeError('adaptive step below protocol minimum')
                continue
            used_h = h
            if candidate_loss <= .001:
                lo,hi = 0.,1.
                for _ in range(30):
                    mid = .5*(lo+hi)
                    if float(loss(blend(state,candidate,mid),inputs,labels)) <= .001:
                        hi = mid
                    else:
                        lo = mid
                state = blend(state,candidate,hi)
                used_h = h*hi
                candidate_loss = float(loss(state,inputs,labels))
                status = 'fitted'
            else:
                state = candidate
            t += used_h
            times.append(t)
            losses.append(candidate_loss)
            steps.append(used_h)
            errors.append(error)
            if t >= SNAPSHOTS[next_snapshot]-1e-9:
                snapshot()
                next_snapshot += 1
            h *= min(2.,max(.5,.9/math.sqrt(max(error,1e-16))))
        if abs(snapshot_times[-1]-t) > 1e-12:
            snapshot()
    except (ValueError,RuntimeError) as exc:
        status = 'numerical_failure'
        save_json(args.out/'exception.json',dict(type=type(exc).__name__,message=str(exc)))
        if abs(snapshot_times[-1]-t) > 1e-12:
            snapshot()
    endpoint = predict(state,end_grid).cpu().numpy()
    arrays = dict(snapshot_times=np.asarray(snapshot_times),circle_inputs=grid_np,circle_angles=grid_angles,
        circle_predictions=np.asarray(outputs),endpoint_inputs=end_grid_np,endpoint_angles=end_angles,
        endpoint_prediction=endpoint,times=np.asarray(times),losses=np.asarray(losses),accepted_steps=np.asarray(steps),
        local_error_ratios=np.asarray(errors),training_inputs=inputs_np,labels=labels_np)
    arrays.update({k:np.stack([s[k] for s in states]) for k in NAMES})
    np.savez(args.out/'arrays.npz',**arrays)
    difference = endpoint-reference_output
    result = dict(status=status,time=t,loss=losses[-1],steps=len(steps),rejected_steps=rejected,
        rms=float(np.sqrt(np.mean(difference**2))),max_abs=float(np.max(np.abs(difference))),
        rms_grid_change=abs(float(np.sqrt(np.mean(difference**2))-np.sqrt(np.mean(difference[::2]**2)))),
        initial_loss=losses[0],integration_seconds=time.monotonic()-start,
        basis_motion_rms={k:float((getattr(state,k)-getattr(initial,k)).square().mean().sqrt()) for k in ('b1','b2')},
        basis_column_rms={k:getattr(state,k).square().mean(0).sqrt().cpu().tolist() for k in ('b1','b2')},
        basis_gram_eigenvalues={k:torch.linalg.eigvalsh(getattr(state,k).T@getattr(state,k)/2048).cpu().tolist() for k in ('b1','b2')},
        loss_increases_above_1e10=int(np.sum(np.diff(losses)>1e-10)),arrays_sha256=sha(args.out/'arrays.npz'),
        peak_cuda_bytes=torch.cuda.max_memory_allocated(device))
    torch.cuda.synchronize(device)
    result['worker_seconds'] = time.monotonic()-worker_start
    save_json(args.out/'summary.json',result)
    print(json.dumps(dict(completed=args.out.name,**result)),flush=True)


if __name__ == '__main__':
    main()
