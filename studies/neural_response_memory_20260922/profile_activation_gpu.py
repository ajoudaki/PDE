"""Bounded component profile at a saved closure state; GPU 0 only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
import numpy as np
import torch
from activation_moment_engine import ActivationMomentEngine, controlled_error
from activation_circle_run import heun_trial, training_loss
from deep_moment_engine import DeepMomentState


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.cuda.set_device(0)
    cfg = json.loads((args.run/'config.json').read_text())
    engine = ActivationMomentEngine(2,cfg['width'],cfg['order'],cfg['inputs'],cfg['labels'],
        activation=cfg['activation'],seed=cfg['seed'],device='cuda:0',dtype=torch.float64)
    with np.load(args.run/'arrays.npz') as saved:
        state = DeepMomentState(*(torch.as_tensor(saved[k],device='cuda:0')
                                  for k in engine.initial.names()))
        step = float(saved['accepted_steps'][-1])
    first,second,euler,candidate = heun_trial(engine,state,step)

    def whole():
        trial = heun_trial(engine,state,step)
        engine.validate_state(trial[3])
        error = controlled_error(engine,state,trial[2],trial[3],cfg['rtol'],cfg['atol'])
        loss = training_loss(engine,trial[3])
        return error,loss

    calls = {
        'whole_trial': whole,
        'one_rhs': lambda: engine.rhs(state),
        'candidate_validation': lambda: engine.validate_state(candidate),
        'physical_error_control': lambda: controlled_error(engine,state,euler,candidate,cfg['rtol'],cfg['atol']),
        'candidate_loss': lambda: training_loss(engine,candidate),
        'fixed_dense_forward': lambda: engine.W20 @ first.A2[0],
        'fixed_dense_transpose': lambda: engine.W20.T @ first.A2[0],
    }
    timings = {}
    with torch.no_grad():
        for name,call in calls.items():
            for _ in range(5): call()
            wall=[];device=[]
            for _ in range(3):
                torch.cuda.synchronize();a=torch.cuda.Event(enable_timing=True);b=torch.cuda.Event(enable_timing=True)
                start=time.perf_counter();a.record()
                for _ in range(20): call()
                b.record();torch.cuda.synchronize()
                wall.append((time.perf_counter()-start)/20)
                device.append(a.elapsed_time(b)/20000)
            timings[name]={'wall_seconds_median':float(np.median(wall)),
                'stream_elapsed_seconds_median':float(np.median(device)),
                'wall_replicates':wall}
        profile = torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU,
                                                     torch.profiler.ProfilerActivity.CUDA])
        with profile:
            for _ in range(3): whole()
            torch.cuda.synchronize()
        (args.out/'operator_profile.txt').write_text(profile.key_averages().table(
            sort_by='self_cuda_time_total',row_limit=35))
        events=[]
        for row in profile.key_averages():
            events.append({'name':row.key,'count':row.count,'self_cpu_us':row.self_cpu_time_total,
                'self_device_us':getattr(row,'self_device_time_total',0.),
                'device_us':getattr(row,'device_time_total',0.)})
        profile.export_chrome_trace(str(args.out/'trace.json'))
    result={'run':str(args.run.resolve()),'config_sha256':digest(args.run/'config.json'),
        'arrays_sha256':digest(args.run/'arrays.npz'),'source_sha256':digest(__file__),
        'device':'cuda:0','device_name':torch.cuda.get_device_name(0),'torch':torch.__version__,
        'dtype':'float64','step':step,'timings':timings,'profile_events':events,
        'stream_event_caveat':'CUDA event intervals include GPU idle gaps caused by host dispatch; inspect actual kernel events separately.',
        'scope':'Repeated trials at one saved mature state; no new training trajectory or hyperparameter change.'}
    (args.out/'profile.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'timings':timings,'out':str(args.out)},indent=2))


if __name__ == '__main__':
    main()
