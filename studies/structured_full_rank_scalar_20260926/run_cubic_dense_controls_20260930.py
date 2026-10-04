"""Run only the two predeclared, bounded pair_cos3 dense controls.

Never overwrite or resume a run. Preserve the last accepted state on budget
expiry or a numerical exception. No experiment runs on import.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import resource
import signal
import sys
import time

import numpy as np
import scipy

import circle_tasks
import dense_compare as dense
import dense_wide_integrator as wide
import true_aggregate_references as refs


STUDY = Path(__file__).resolve().parent
DATA = STUDY.parents[1] / 'data/generated/structured_full_rank_scalar_20260926'
DEFAULT_OUTPUT = DATA / 'cubic_scalar_20260930/dense_controls'
REFERENCE = DATA / 'all_tasks_j2_20260927/references/pair_cos3__gaussian.npz'
CONFIG = {'task': 'pair_cos3', 'width': 1024, 'seed': 1,
          'target_mse': .001, 'rtol': 1e-6, 'atol': 1e-9,
          'time_cap': 3000., 'max_step': 10., 'first_step': .05,
          'grid': 256, 'training_wall_cap_seconds': 40.,
          'address_space_limit_bytes': 2 * 1024**3, 'blas_threads': 1}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_digest(array):
    return hashlib.sha256(np.ascontiguousarray(array).tobytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


class TrainingBudget(Exception):
    pass


def fit_one(readout, output, manifest_hash):
    total_started = time.monotonic()
    task = circle_tasks.BY_NAME[CONFIG['task']]
    u, labels = task.data()
    initial = dense.initialize(CONFIG['width'], CONFIG['seed'], 'gaussian')
    if readout == 'zero':
        initial.c[:] = 0.
    initial_hashes = {name: array_digest(getattr(initial, name))
                      for name in ('w', 'W', 'c')}
    initial_train = dense._forward(initial, u).output
    initial_mse = float(np.mean((initial_train-labels)**2))
    accepted = [0., initial, initial_mse]
    history = []
    count = [0]
    original_rhs = wide.flat_rhs

    def callback(at, state, mse):
        saved_state = state.copy()
        accepted[:] = [float(at), saved_state, float(mse)]
        history.append((float(at), float(mse)))

    def counted_rhs(*args):
        count[0] += 1
        return original_rhs(*args)

    def alarm(signum, frame):
        raise TrainingBudget('40-second dense training limit')

    result = None
    exception = None
    old_handler = signal.signal(signal.SIGALRM, alarm)
    wide.flat_rhs = counted_rhs
    started = time.monotonic()
    signal.setitimer(signal.ITIMER_REAL, CONFIG['training_wall_cap_seconds'])
    try:
        result = wide.integrate(
            initial, u, labels, time_cap=CONFIG['time_cap'],
            rtol=CONFIG['rtol'], atol=CONFIG['atol'],
            target_train_mse=CONFIG['target_mse'],
            max_step=CONFIG['max_step'], first_step=CONFIG['first_step'],
            deadline=time.time()+CONFIG['training_wall_cap_seconds']-.5,
            callback=callback)
        endpoint_time, state, mse = result.time, result.state, result.train_mse
        reason = result.stop_reason
    except Exception as error:
        endpoint_time, state, mse = accepted
        reason = 'training_wall_limit' if isinstance(error, TrainingBudget) else 'exception'
        exception = {'type': type(error).__name__, 'message': str(error)}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, old_handler)
        wide.flat_rhs = original_rhs
    training_seconds = time.monotonic()-started
    angles = 2*np.pi*np.arange(CONFIG['grid'])/CONFIG['grid']
    model = refs.GaussianCheckpoint(state)
    prediction = model.predict(angles, batch=64)
    train_prediction = model.predict(task.angles, batch=64)
    recomputed_mse = float(np.mean((train_prediction-labels)**2))
    initial_prediction = refs.GaussianCheckpoint(initial).predict(angles, batch=64)
    finite = all(np.all(np.isfinite(value)) for value in
                 (state.w, state.W, state.c, prediction, train_prediction))
    fitted = bool(reason == 'target' and finite and
                  recomputed_mse <= CONFIG['target_mse'])
    path = output / f'pair_cos3__{readout}_tight.npz'
    np.savez(path, kind='gaussian', w=state.w, W=state.W, c=state.c,
             angles=angles, prediction=prediction,
             train_angles=np.asarray(task.angles), train_labels=labels,
             train_prediction=train_prediction, history=np.asarray(history),
             initial_prediction=initial_prediction,
             initial_train_prediction=initial_train)
    info = {
        **CONFIG, 'method': 'gaussian', 'readout': readout,
        'initial_readout': 'N(0,1/n^2)' if readout == 'canonical' else 'exact zero',
        'initialization_modifications': [] if readout == 'canonical' else ['c set to zero'],
        'initial_array_sha256': initial_hashes,
        'initial_train_mse': initial_mse,
        'initial_circle_output_rms': float(np.sqrt(np.mean(initial_prediction**2))),
        'physical_time': endpoint_time, 'train_mse': recomputed_mse,
        'integrator_reported_train_mse': mse,
        'stop_reason': reason, 'exception': exception, 'fitted': fitted,
        'endpoint_status': 'fitted threshold endpoint' if fitted else 'partial accepted endpoint',
        'finite': bool(finite), 'nfev': count[0],
        'nsteps': result.nsteps if result is not None else max(0, len(history)-1),
        'nreject': result.nreject if result is not None else None,
        'target_bracket': result.first_target_bracket if result is not None else None,
        'max_loss_rise': result.max_loss_rise if result is not None else
            max([0.]+[b[1]-a[1] for a,b in zip(history,history[1:])]),
        'training_seconds': training_seconds,
        'solver': result.settings if result is not None else None,
        'peak_resident_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
        'data_file': path.name, 'data_sha256': digest(path),
        'endpoint_array_sha256': {name: array_digest(getattr(state, name))
                                  for name in ('w', 'W', 'c')},
        'source_manifest_sha256': manifest_hash,
        'total_seconds': time.monotonic()-total_started,
    }
    write_json(path.with_suffix('.json'), info)
    print(json.dumps({key: info[key] for key in
                     ('readout', 'fitted', 'train_mse', 'stop_reason',
                      'physical_time', 'training_seconds', 'data_file')}), flush=True)
    return info


def differences(left, right):
    difference = left-right
    rms = float(np.sqrt(np.mean(difference**2)))
    coarse = float(np.sqrt(np.mean(difference[::2]**2)))
    return {'circle_rms_256': rms, 'circle_max_absolute': float(np.max(np.abs(difference))),
            'circle_rms_128': coarse, 'grid_change_256_128': abs(rms-coarse)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    # Hard process address-space bound, stricter than a resident-memory cap.
    previous_limits = resource.getrlimit(resource.RLIMIT_AS)
    hard = previous_limits[1]
    limit = CONFIG['address_space_limit_bytes'] if hard == resource.RLIM_INFINITY else min(
        CONFIG['address_space_limit_bytes'], hard)
    resource.setrlimit(resource.RLIMIT_AS, (limit, hard))
    reference_meta = json.loads(REFERENCE.with_suffix('.json').read_text())
    if digest(REFERENCE) != reference_meta['data_sha256']:
        raise ValueError('Cached reference hash mismatch')
    if not (reference_meta['width'] == 1024 and reference_meta['seed'] == 1
            and reference_meta['target_mse'] == .001 and reference_meta['fitted']):
        raise ValueError('Cached reference configuration mismatch')
    manifest = {
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'config': CONFIG, 'readout_order': ['canonical', 'zero'],
        'maximum_runs': 2, 'reruns': 0, 'command': sys.argv,
        'cwd': str(Path.cwd()), 'python': platform.python_version(),
        'numpy': np.__version__, 'scipy': scipy.__version__,
        'platform': platform.platform(),
        'environment': {key: os.environ[key] for key in
                        ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                         'NUMEXPR_NUM_THREADS')},
        'address_space_limit_bytes': limit,
        'cached_reference': str(REFERENCE), 'cached_reference_sha256': digest(REFERENCE),
        'cached_reference_metadata_sha256': digest(REFERENCE.with_suffix('.json')),
        'sources': {name: digest(STUDY/name) for name in
                    (Path(__file__).name, 'CUBIC_SCALAR_EXPERIMENT_PROTOCOL_20260930.md',
                     'circle_tasks.py', 'dense_compare.py', 'dense_wide_integrator.py',
                     'true_aggregate_references.py', 'block_scalar_closure.py')},
        'metric': 'unnormalized circle RMS at separately stopped first MSE=.001 endpoints',
        'interpretation': 'pair_cos3-only numerical/reference and initial-readout controls',
    }
    write_json(output/'manifest.json', manifest)
    started = time.monotonic()
    rows = []
    for readout in manifest['readout_order']:
        rows.append(fit_one(readout, output, digest(output/'manifest.json')))
        write_json(output/'results.json', rows)
    with np.load(REFERENCE, allow_pickle=False) as saved:
        reference_prediction = saved['prediction'].copy()
        angles = saved['angles'].copy()
    predictions = {}
    for row in rows:
        with np.load(output/row['data_file'], allow_pickle=False) as saved:
            if not np.array_equal(saved['angles'], angles):
                raise ValueError('Control and cached query grids differ')
            predictions[row['readout']] = saved['prediction'].copy()
    comparisons = {
        'canonical_tight_vs_cached': differences(predictions['canonical'], reference_prediction),
        'zero_tight_vs_canonical_tight': differences(predictions['zero'], predictions['canonical']),
        'zero_tight_vs_cached': differences(predictions['zero'], reference_prediction),
    }
    # The frozen protocol permits passive 512-point evaluation only if needed.
    if any(value['grid_change_256_128'] > .001 for value in comparisons.values()):
        fine_angles = 2*np.pi*np.arange(512)/512
        fine = {'cached': refs.load_checkpoint(REFERENCE).predict(fine_angles,batch=64)}
        for row in rows:
            fine[row['readout']] = refs.load_checkpoint(output/row['data_file']).predict(fine_angles,batch=64)
        for key, left, right in (
                ('canonical_tight_vs_cached','canonical','cached'),
                ('zero_tight_vs_canonical_tight','zero','canonical'),
                ('zero_tight_vs_cached','zero','cached')):
            comparisons[key]['circle_rms_512'] = float(np.sqrt(np.mean((fine[left]-fine[right])**2)))
        np.savez(output/'passive_refinement512.npz', angles=fine_angles, **fine)
    comparisons['valid_fitted_endpoint_comparison'] = all(row['fitted'] for row in rows)
    comparisons['identical_initial_input_and_middle_weights'] = all(
        rows[0]['initial_array_sha256'][name] == rows[1]['initial_array_sha256'][name]
        for name in ('w','W'))
    comparisons['cached_reference_unchanged'] = digest(REFERENCE) == manifest['cached_reference_sha256']
    comparisons['physical_time_difference_canonical_tight_minus_cached'] = rows[0]['physical_time']-reference_meta['physical_time']
    comparisons['physical_time_difference_zero_minus_canonical_tight'] = rows[1]['physical_time']-rows[0]['physical_time']
    write_json(output/'comparison.json', comparisons)
    write_json(output/'completion.json', {
        'runs': len(rows), 'all_fitted': all(row['fitted'] for row in rows),
        'training_seconds': sum(row['training_seconds'] for row in rows),
        'wall_seconds': time.monotonic()-started, 'reruns': 0,
        'artifact_sha256': {path.name: digest(path) for path in sorted(output.iterdir())
                            if path.is_file()},
    })
    print(json.dumps(comparisons), flush=True)


if __name__ == '__main__':
    main()
