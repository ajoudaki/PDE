"""Replay declared multidata setup failures with an observational solver wrapper.

No training, changed optimizer arguments, extra optimizer calls, or repaired
weights. A single process is limited to 58 CPU seconds (60 hard) and 60 wall
seconds. Only the first invalid mass result of each declared candidate is saved.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time
import traceback

resource.setrlimit(resource.RLIMIT_CPU, (58, 60))
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT/'code'))
import neuron_sampling_setup as original
from neuron_sampling_multidata import prepare_witness, build_sampler
from pde.finite_network import initialize


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fingerprint(value):
    value = np.ascontiguousarray(value)
    return dict(shape=list(value.shape), dtype=str(value.dtype),
                sha256=hashlib.sha256(memoryview(value).cast('B')).hexdigest())


def write_json(path, value):
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    begin, cpu_begin = time.perf_counter(), time.process_time()
    out, run = Path(args.output).resolve(), Path(args.run).resolve()
    out.mkdir(parents=True, exist_ok=False)
    case_name = 'embedded_circle8_d5_n2048_s9411'
    case_out = run/case_name
    config = json.loads((run/'config.resolved.json').read_text())
    provenance = json.loads((run/'provenance.json').read_text())
    failures = json.loads((case_out/'setup_failures.json').read_text())
    dataset = config['datasets']['embedded_circle8_d5']
    expected = json.loads((case_out/'dense_initialization.json').read_text())['array_fingerprints']
    source_names = ('neuron_sampling_setup.py', 'neuron_sampling_multidata.py')
    source_paths = [HERE/name for name in source_names]+[ROOT/'code/pde/finite_network.py']
    source_hashes = {str(path.relative_to(ROOT)): digest(path) for path in source_paths}
    for name, actual in source_hashes.items():
        if provenance['source_hashes'][name] != actual:
            raise RuntimeError(f'original source changed: {name}')
    for name in ('config.input.json', 'config.resolved.json', 'provenance.json'):
        (out/name).write_bytes((run/name).read_bytes())
    (out/'original_setup_failures.json').write_bytes((case_out/'setup_failures.json').read_bytes())
    (out/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    record = dict(case=case_name, source_run=str(run.relative_to(ROOT)), argv=sys.argv,
        python=sys.version, executable=sys.executable, numpy=np.__version__, scipy=scipy.__version__,
        source_hashes=source_hashes, diagnostic_source_sha256=digest(__file__),
        config_sha256=digest(run/'config.resolved.json'),
        cpu_limit_seconds=60, wall_limit_seconds=60, training_steps=0,
        optimizer_arguments_unchanged=True, candidate_results=[], unstarted_candidates=[])
    raw_minimize, raw_cubature = original.minimize, original._positive_cubature
    active = {}

    def stop(signum, frame):
        raise TimeoutError('bounded diagnostic time limit')

    def capture_minimize(*positional, **kwargs):
        result = raw_minimize(*positional, **kwargs)
        masses = np.asarray(result.x)
        floor = kwargs['bounds'][0][0]
        finite = bool(np.isfinite(masses).all())
        invalid = (not finite or abs(masses.sum()-1.) > 1e-8 or masses.min() < floor-1e-9)
        summary = dict(layer=active['layer'], selected_count=len(masses),
            success=bool(result.success), status=int(result.status), message=str(result.message),
            iterations=int(result.nit), finite=finite, original_validity_gate_failed=bool(invalid))
        if finite:
            summary.update(min_mass=float(masses.min()), max_mass=float(masses.max()),
                all_strictly_positive=bool(np.all(masses > 0)),
                sum_numpy=float(masses.sum()), sum_numpy_minus_one=float(masses.sum()-1.),
                sum_fsum=math.fsum(map(float, masses)),
                prescribed_floor=float(floor), min_mass_minus_floor=float(masses.min()-floor),
                sum_numpy_minus_one_hex=float(masses.sum()-1.).hex(),
                min_mass_minus_floor_hex=float(masses.min()-floor).hex(),
                objective=float(result.fun))
        active['optimizer_calls'].append(summary)
        if invalid and 'first_invalid' not in active:
            if finite:
                exact_drift = sum((Fraction.from_float(float(value)) for value in masses), Fraction())-1
                summary['exact_sum_of_stored_masses_minus_one'] = str(exact_drift)
                summary['exact_sum_drift_float'] = float(exact_drift)
            active['first_invalid'] = dict(summary)
            filename = active['sampler']['name']+'_first_invalid.npz'
            np.savez_compressed(out/filename, masses=masses, initial_weights=np.asarray(positional[1]),
                                prescribed_floor=np.asarray(floor))
            active['first_invalid_mass_archive'] = filename
            active['first_invalid_mass_archive_sha256'] = digest(out/filename)
            write_json(out/'partial_diagnostic.json', record)
        return result

    def capture_cubature(*positional, **kwargs):
        active['layer'] += 1
        return raw_cubature(*positional, **kwargs)

    signal.signal(signal.SIGALRM, stop)
    signal.signal(signal.SIGXCPU, stop)
    signal.setitimer(signal.ITIMER_REAL, 60.)
    original.minimize, original._positive_cubature = capture_minimize, capture_cubature
    try:
        initialized = initialize(2048, 2, 5, seed=9411)
        A0, W0 = initialized.weights
        actual = dict(reference_setup_A0=fingerprint(A0), reference_setup_W0=fingerprint(W0))
        if any(actual[name] != expected[name] for name in actual):
            raise AssertionError('reconstructed initialization fingerprint differs')
        record['initialization_fingerprints'] = actual
        record['original_initialization_reproduced_exactly'] = True
        witness = prepare_witness(A0, W0, dataset['U'], dataset['labels'], setup_probes=dataset['setup_probes'])
        record['witness_seconds'] = time.perf_counter()-begin
        for index, failure in enumerate(failures):
            if time.process_time() >= 48. or time.perf_counter()-begin >= 48.:
                record['unstarted_candidates'] = [item['sampler']['name'] for item in failures[index:]]
                break
            spec = failure['sampler']
            active = dict(sampler=spec, layer=0, optimizer_calls=[])
            record['candidate_results'].append(active)
            candidate_start = time.perf_counter()
            try:
                build_sampler(A0, W0, dataset['U'], dataset['labels'], spec['width'],
                    setup_probes=dataset['setup_probes'], basis_rank=spec['rank'],
                    mass_floor=config['mass_floor'], singular_tolerance=config['singular_tolerance'], witness=witness)
                active['construction_completed'] = True
            except TimeoutError:
                raise
            except Exception as exc:
                active['construction_completed'] = False
                active['error'] = repr(exc)
                active['traceback'] = traceback.format_exc()
                active['original_failure_reproduced'] = repr(exc) == failure['error']
            active['wall_seconds'] = time.perf_counter()-candidate_start
            write_json(out/'partial_diagnostic.json', record)
            print(json.dumps({key: value for key, value in active.items() if key not in ('optimizer_calls', 'traceback')}), flush=True)
    except BaseException as exc:
        record['diagnostic_error'] = repr(exc)
        record['diagnostic_traceback'] = traceback.format_exc()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        original.minimize, original._positive_cubature = raw_minimize, raw_cubature
        record['wall_seconds'] = time.perf_counter()-begin
        record['cpu_seconds_excluding_imports'] = time.process_time()-cpu_begin
        record['process_cpu_seconds_including_imports'] = time.process_time()
        record['source_hashes_unchanged'] = all(digest(ROOT/name) == value for name, value in source_hashes.items())
        write_json(out/'diagnostic.json', record)


if __name__ == '__main__':
    main()
