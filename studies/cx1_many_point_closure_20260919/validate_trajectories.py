"""Execute only the configurations predeclared in VALIDATION_PLAN.md."""
import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import sys
import time

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('360 second limit')))
signal.alarm(360)

import numpy as np
import cx1_closure as closure


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path.cwd()
    expected = root/'data/generated/cx1_many_point_closure_20260919'
    output = args.output.resolve()
    if output.parent != expected.resolve():
        raise ValueError('output must be a fresh direct study-owned run directory')
    output.mkdir(parents=True, exist_ok=False)
    here = Path(__file__).resolve().parent
    sources = [here/'validate_trajectories.py', here/'VALIDATION_PLAN.md', here/'cx1_closure.py']
    sources += [root/'code/pde'/name for name in ('observable_solver.py', 'observable_arithmetic.py',
        'observable_compiler.py', 'observable_closure.py', 'observable_fixed.py')]
    sources = [p for p in sources if p.exists()]
    config = [('reference_o1',1,256,64,1500), ('reference_o3',3,256,64,1500),
        ('reference_o3_time',3,256,64,3000), ('reference_o3_integration',3,512,128,1500),
        ('perturbed_o3',3,256,64,1500)]
    record = dict(status='running', command=sys.argv, cwd=str(root),
        python=platform.python_version(), numpy=np.__version__, platform=platform.platform(),
        threads={k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        sources={str(p.relative_to(root)):digest(p) for p in sources}, configurations=config, results=[])
    (output/'record.json').write_text(json.dumps(record,indent=2)+'\n')
    start = time.monotonic()
    probes = np.concatenate([np.eye(3),-np.eye(3), np.array([[1,1,1],[-1,1,1]])/np.sqrt(3)])
    final_predictions = {}
    try:
        for name,order,Q,P,steps in config:
            run_start = time.monotonic()
            initial = closure.initialize(3,order,initialization_nodes=Q,population_nodes=P)
            inputs = np.eye(3)
            if name == 'perturbed_o3':
                inputs[0] = [399/401,40/401,0]
            law = closure.DataLaw(inputs,np.array([1.,-1.,1.]),np.full(3,1/3)).validate(initial.arithmetic)
            shapes = {key:getattr(initial,key).shape for key in closure._ARRAYS}
            half = closure.evolve(initial,law,steps=steps//2,step_size=Fraction(15,steps))
            path = output/(name+'_midpoint.json')
            closure.save_restart(path,half,law)
            restored,restored_law = closure.load_restart(path)
            end = closure.evolve(half,law,steps=steps//2,step_size=Fraction(15,steps))
            restarted = closure.evolve(restored,restored_law,steps=steps//2,step_size=Fraction(15,steps))
            exact = all(np.array_equal(getattr(end,key),getattr(restarted,key)) for key in closure._ARRAYS)
            fixed_shapes = all(getattr(end,key).shape == shape for key,shape in shapes.items())
            prediction = closure.predict(end,probes)
            pairs = closure.paired_observations(end,law,include_pairs=False)
            assert exact and fixed_shapes and np.isfinite(prediction).all()
            final_predictions[name] = prediction
            result = dict(name=name,seconds=time.monotonic()-run_start,metadata=initial.metadata,
                loss_initial=float(closure.loss(initial,law)), loss_midpoint=float(closure.loss(half,law)),
                loss_final=float(closure.loss(end,law)),paired_rms=[float(pairs['rms1']),float(pairs['rms2'])],
                passive_predictions=prediction.tolist(), own_state_restart_exact=exact,
                unchanged_shapes=fixed_shapes, retained_bytes=closure.state_bytes(end),
                peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            record['results'].append(result)
            print(json.dumps(result),flush=True)
            np.savez(output/(name+'_observations.npz'),probes=probes,predictions=prediction,inputs=inputs)
            (output/'record.json').write_text(json.dumps(record,indent=2)+'\n')
        base = final_predictions['reference_o3']
        record['descriptive_prediction_differences'] = {name:float(np.max(np.abs(base-final_predictions[name])))
            for name in ('reference_o1','reference_o3_time','reference_o3_integration')}
        record['status'] = 'passed_operational_checks_only'
        record['exit_status'] = 0
    except BaseException as exc:
        record['status'] = 'failed_or_interrupted'
        record['error'] = repr(exc)
        record['exit_status'] = 1
        raise
    finally:
        record['seconds'] = time.monotonic()-start
        record['outputs'] = {p.name:digest(p) for p in output.iterdir() if p.is_file() and p.name!='record.json'}
        (output/'record.json').write_text(json.dumps(record,indent=2)+'\n')
        signal.alarm(0)


if __name__ == '__main__':
    main()
