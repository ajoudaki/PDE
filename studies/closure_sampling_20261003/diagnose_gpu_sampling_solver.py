"""CPU initialization/cubature replay only; wrapper never modifies optimizer results."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import sys
import time

for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
ROOT = Path('/home/amir/Codes/PDE')
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True, help='fresh diagnostic output directory')
args = parser.parse_args()
OUT = Path(args.output).resolve()
OUT.mkdir(parents=True, exist_ok=False)
sys.path.insert(0, str(ROOT/'studies/closure_sampling_20261003'))
import numpy as np
import scipy
import torch
from gpu_sampling_experiment import make_dense, settings

settings()
started = time.perf_counter()
report = dict(purpose='unchanged optimizer replay; no trajectory integration',
              numpy=np.__version__, scipy=scipy.__version__, torch=torch.__version__,
              cases=[], diagnostic_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

def save():
    report['wall_seconds'] = time.perf_counter()-started
    (OUT/'diagnostic.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')

def timeout(signum, frame):
    raise TimeoutError('60-second CPU setup diagnostic budget exceeded')

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 60.)
try:
    for angle, seed, sign, width, name in [(60,8512,-1,53,'p1'),(90,8514,1,59,'p2')]:
        run = ROOT/f'data/generated/closure_sampling_20261003/gpu_rms_growth_20261003_validation_{angle}'
        case_id = f'n2048_s{seed}_a{angle}_sign{sign:+d}'
        case_dir = run/case_id
        config = json.loads((run/'config.resolved.json').read_text())
        expected = json.loads((case_dir/'dense_initialization.json').read_text())['array_fingerprints']
        provenance = json.loads((run/'provenance.json').read_text())
        scientific_files = ['studies/closure_sampling_20261003/gpu_sampling_experiment.py',
                            'code/pde/finite_network.py','code/pde/finite_torch.py',
                            'code/pde/observable_torch_p1.py']
        for source in scientific_files:
            actual = hashlib.sha256((ROOT/source).read_bytes()).hexdigest()
            assert actual == provenance['source_hashes'][source], source
        source_name = 'studies/closure_sampling_20261003/neuron_sampling_setup.py'
        source_path = run/'sources'/source_name
        source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
        assert source_hash == provenance['source_hashes'][source_name]
        spec = importlib.util.spec_from_file_location(f'archived_sampler_{angle}', source_path)
        sampler = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sampler)
        dense, A0, W0 = make_dense(2048, seed, 'cpu', torch.float64)
        fingerprints = {key: hashlib.sha256(memoryview(np.ascontiguousarray(array)).cast('B')).hexdigest()
                        for key,array in [('reference_setup_A0',A0),('reference_setup_W0',W0)]}
        for key,value in fingerprints.items():
            assert value == expected[key]['sha256'], key
        del dense
        U = np.array([[1.,0.],[math.cos(math.radians(angle)),math.sin(math.radians(angle))]])
        labels = np.array([.2,.1*sign])
        record = dict(case=case_id, sampler=name, width=width, rank=16,
                      probe_count=config['probe_count'],mass_floor=config['mass_floor'],
                      archived_source_sha256=source_hash, initialization_hashes_match=True,
                      initialization_hashes=fingerprints, fits=[])
        report['cases'].append(record)
        original_minimize = sampler.minimize
        original_cubature = sampler._positive_cubature
        layer = [0]
        def cubature(*args, **kwargs):
            layer[0] += 1
            return original_cubature(*args, **kwargs)
        def minimize(*args, **kwargs):
            result = original_minimize(*args, **kwargs)
            weights = np.asarray(result.x)
            floor = float(kwargs['bounds'][0][0])
            finite = bool(np.isfinite(weights).all())
            sum_error = float(weights.sum()-1.)
            minimum_gap = float(weights.min()-floor)
            invalid = not finite or abs(sum_error)>1e-8 or minimum_gap < -1e-9
            row = dict(layer=layer[0], selected_count=len(weights), success=bool(result.success),
                status=int(result.status), message=str(result.message), iterations=int(result.nit),
                finite=finite, sum_minus_one=sum_error, min_minus_floor=minimum_gap,
                minimum_mass=float(weights.min()), floor=floor, objective=float(result.fun),
                initial_objective=float(args[0](args[1])), rejected_by_unchanged_guard=invalid)
            record['fits'].append(row)
            if invalid:
                np.savez_compressed(OUT/f'{case_id}_offending_fit.npz', weights=weights,
                                    starting_weights=args[1], floor=np.array(floor))
                record['offending_fit'] = row
                save()
                print(json.dumps(dict(case=case_id,offending_fit=row)), flush=True)
            return result
        sampler.minimize = minimize
        sampler._positive_cubature = cubature
        witness = sampler.prepare_witness(A0,W0,U,labels,probe_count=config['probe_count'])
        try:
            sampler.build_sampler(A0,W0,U,labels,width,basis_rank=16,
                probe_count=config['probe_count'],mass_floor=config['mass_floor'],
                singular_tolerance=1e-10,witness=witness)
            record['outcome'] = 'completed without reproducing rejection'
        except RuntimeError as exc:
            record['outcome'] = repr(exc)
        save()
except BaseException as exc:
    report['error'] = repr(exc)
    save()
    raise
finally:
    signal.setitimer(signal.ITIMER_REAL,0.)
    save()
print(json.dumps(dict(wall_seconds=report['wall_seconds'],output=str(OUT/'diagnostic.json'))),flush=True)
