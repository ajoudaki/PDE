"""Configurable, bounded RMS-growth sweep of the existing initialized sampler.

All dynamics and initialization are imported unchanged from the earlier runner.
The primary metric is RMS over query points of the timewise absolute maximum.
This is a finite saved-time/panel diagnostic, not a continuum error certificate.
CLI training requires CUDA; deterministic CPU checks are callable separately.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import signal
import sys
import time
import traceback

for _key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_key, '1')
import numpy as np
import scipy
import torch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from gpu_sampling_experiment import (
    Batch, settings, fields, heun, validate_core, make_dense, pack_samplers,
    feature_motion,
)
from neuron_sampling_setup import prepare_witness, build_sampler

DEFAULTS = dict(probe_count=32, mass_floor=.05, dt=.2, observe_every=1.,
                panel=257, panel_offset=.5, horizon=120., max_horizon=240.,
                max_allocation_gib=8., budget_seconds=1200., dtype='float64',
                include_frozen=True)
METRICS = ('rms_of_time_sup', 'sup_of_time_rms', 'endpoint_rms', 'sup_panel_time')


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def save_arrays(path, **arrays):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    with temporary.open('wb') as stream:
        np.savez_compressed(stream, **arrays)
    temporary.replace(path)


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def _integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return value


def normalize_config(raw):
    if not isinstance(raw, dict):
        raise ValueError('configuration must be a JSON object')
    raw = dict(raw)
    for alias, target in (('T', 'horizon'), ('maxT', 'max_horizon'),
                          ('wallbudget', 'budget_seconds')):
        if alias in raw:
            if target in raw:
                raise ValueError(f'specify only one of {alias} and {target}')
            raw[target] = raw.pop(alias)
    if 'maxallocation' in raw:
        if 'max_allocation_gib' in raw:
            raise ValueError('duplicate allocation limit')
        raw['max_allocation_gib'] = float(raw.pop('maxallocation')) / 2**30
    allowed = set(DEFAULTS) | {'cases', 'samplers', 'samplers_by_n', 'description', 'source_files', 'stage', 'protocol'}
    if set(raw) - allowed:
        raise ValueError(f'unknown configuration keys: {sorted(set(raw)-allowed)}')
    config = {**DEFAULTS, **raw}
    for name in ('dt', 'observe_every', 'horizon', 'max_horizon',
                 'max_allocation_gib', 'budget_seconds'):
        value = config[name]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(f'{name} must be finite and positive')
    for name, minimum in (('probe_count', 4), ('panel', 1)):
        _integer(config[name], name, minimum)
    if not isinstance(config['include_frozen'], bool):
        raise ValueError('include_frozen must be boolean')
    if config['dtype'] not in ('float32', 'float64'):
        raise ValueError('dtype must be float32 or float64')
    if not 0 < config['mass_floor'] < 1 or not math.isfinite(config['panel_offset']):
        raise ValueError('invalid mass_floor or panel_offset')
    if config['max_horizon'] < config['horizon']:
        raise ValueError('max_horizon must be >= horizon')
    for name in ('observe_every', 'horizon', 'max_horizon'):
        ratio = config[name] / config['dt']
        if round(ratio) < 1 or not math.isclose(ratio, round(ratio), rel_tol=0, abs_tol=1e-8):
            raise ValueError(f'{name} must be an integer multiple of dt')
    cases = config.get('cases')
    if not isinstance(cases, list) or not cases:
        raise ValueError('cases must be a nonempty list')
    if ('samplers' in config) == ('samplers_by_n' in config):
        raise ValueError('specify exactly one of samplers or samplers_by_n')
    if 'samplers_by_n' in config and not isinstance(config['samplers_by_n'], dict):
        raise ValueError('samplers_by_n must map dense widths to sampler lists')
    seen = set()
    for case in cases:
        if not isinstance(case, dict) or set(case) != {'n', 'seed', 'angle', 'sign'}:
            raise ValueError('each case must contain exactly n, seed, angle, sign')
        n = _integer(case['n'], 'n', 4)
        _integer(case['seed'], 'seed', 0)
        if isinstance(case['sign'], bool) or case['sign'] not in (-1, 1):
            raise ValueError('sign must be -1 or +1')
        if not isinstance(case['angle'], (int, float)) or not math.isfinite(case['angle']):
            raise ValueError('angle must be finite degrees')
        key = tuple(case[k] for k in ('n', 'seed', 'angle', 'sign'))
        if key in seen:
            raise ValueError(f'duplicate case: {key}')
        seen.add(key)
        specs = sampler_specs(config, n)
        if not isinstance(specs, list) or not specs:
            raise ValueError(f'no samplers configured for n={n}')
        names = set()
        for spec in specs:
            if not isinstance(spec, dict) or not {'name', 'width', 'rank'} <= set(spec):
                raise ValueError('each sampler must contain name, width, rank')
            name = spec['name']
            if not isinstance(name, str) or not name or name in names or name in (
                    'dense_reference', 'dense_independent', 'frozen_dense_hidden'):
                raise ValueError('sampler names must be nonempty, unique, and unreserved')
            names.add(name)
            width = _integer(spec['width'], 'width', 4)
            rank = _integer(spec['rank'], 'rank')
            if width > n or rank > width:
                raise ValueError('require rank <= width <= dense n')
    for name in config.get('source_files', []):
        path = (ROOT / name).resolve()
        if not path.is_relative_to(HERE) or not path.is_file():
            raise ValueError('extra source_files must be existing files in this study')
    return config


def sampler_specs(config, n):
    return config['samplers'] if 'samplers' in config else config['samplers_by_n'].get(str(n))


def comparison_metrics(predictions, n):
    predictions = np.asarray(predictions)
    if predictions.ndim != 3 or min(predictions.shape) < 1 or predictions.shape[1] < 2:
        raise ValueError('predictions must have shape (saved times, >=2 models, panel)')
    if not np.isfinite(predictions).all():
        raise ValueError('nonfinite predictions')
    errors = predictions - predictions[:, :1, :]
    records = []
    for j in range(errors.shape[1]):
        error = errors[:, j, :]
        record = dict(
            rms_of_time_sup=float(np.sqrt(np.mean(np.max(np.abs(error), axis=0)**2))),
            sup_of_time_rms=float(np.max(np.sqrt(np.mean(error**2, axis=1)))),
            endpoint_rms=float(np.sqrt(np.mean(error[-1]**2))),
            sup_panel_time=float(np.max(np.abs(error))),
        )
        record['old_max'] = record['sup_panel_time']
        record['root_scaled'] = {key: math.sqrt(n)*record[key] for key in METRICS}
        records.append(record)
    for record in records:
        record['dense_baseline'] = {key: records[1][key] for key in METRICS}
        record['ratio_to_dense_copy'] = {
            key: record[key]/records[1][key] if records[1][key] > 0 else None
            for key in METRICS}
    return records


def validate_metrics():
    # Different query points attain their maximum at different times.
    # RMS(max_t |e|) = sqrt(12.5), max_t RMS(e) = sqrt(8), endpoint RMS = sqrt(4.5).
    predictions = np.zeros((3, 3, 2))
    predictions[1, 1] = [1., 0.]
    predictions[2, 1] = [0., 1.]
    predictions[1, 2] = [4., 0.]
    predictions[2, 2] = [0., 3.]
    metric = comparison_metrics(predictions, 9)[2]
    expected = dict(rms_of_time_sup=math.sqrt(12.5), sup_of_time_rms=math.sqrt(8),
                    endpoint_rms=math.sqrt(4.5), sup_panel_time=4.)
    for name, value in expected.items():
        if not math.isclose(metric[name], value, rel_tol=0, abs_tol=1e-14):
            raise AssertionError((name, metric[name], value))
        if not math.isclose(metric['root_scaled'][name], 3*value, rel_tol=0, abs_tol=1e-14):
            raise AssertionError('incorrect root-width scaling')
    if not metric['rms_of_time_sup'] > metric['sup_of_time_rms']:
        raise AssertionError('max and RMS must not commute on this fixture')
    zero = comparison_metrics(np.zeros((1, 2, 2)), 9)[0]
    if any(value is not None for value in zero['ratio_to_dense_copy'].values()):
        raise AssertionError('zero baseline must produce null ratios')
    return dict(noncommuting_metric_oracle=True, root_scaling=True, zero_baseline=True)


def archive_sources(out, args, config, raw_config):
    paths = {Path(__file__).resolve(), HERE/'gpu_sampling_experiment.py',
             HERE/'neuron_sampling_setup.py', HERE/'GPU_SAMPLING_PROTOCOL.md',
             HERE/'GPU_SAMPLING_RESULTS.md', HERE/'GPU_RMS_GROWTH_PROTOCOL.md', ROOT/'code/README.md',
             ROOT/'code/pde/finite_network.py'}
    for module in tuple(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename:
            path = Path(filename).resolve()
            if path.is_relative_to(ROOT/'code/pde') and path.suffix == '.py':
                paths.add(path)
    paths.update((ROOT/path).resolve() for path in config.get('source_files', []))
    sources = {}
    for path in sorted(paths):
        relative = str(path.relative_to(ROOT))
        destination = out/'sources'/relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        destination.write_bytes(data)
        sources[relative] = hashlib.sha256(data).hexdigest()
    (out/'config.input.json').write_bytes(raw_config)
    write_json(out/'config.resolved.json', config)
    write_json(out/'provenance.json', dict(
        args=vars(args), argv=sys.argv, cwd=os.getcwd(), python=sys.version,
        executable=sys.executable, platform=platform.platform(),
        numpy=np.__version__, scipy=scipy.__version__, torch=torch.__version__,
        cuda=torch.version.cuda, gpu=torch.cuda.get_device_name(args.device),
        source_hashes=sources, config_input_sha256=sha256(out/'config.input.json'),
        config_resolved_sha256=sha256(out/'config.resolved.json'),
        threads=torch.get_num_threads(), interop_threads=torch.get_num_interop_threads(),
        thread_environment={key: os.environ.get(key) for key in
                            ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')},
        tf32_matmul=torch.backends.cuda.matmul.allow_tf32,
        tf32_cudnn=torch.backends.cudnn.allow_tf32,
        primary_metric='rms_of_time_sup', source_changes_policy='stop; preserve output'))
    return sources


def verify_sources(sources):
    changed = [path for path, digest in sources.items() if sha256(ROOT/path) != digest]
    if changed:
        raise RuntimeError(f'source changed after archival: {changed}; start a fresh output')


def check_budget(device, config, deadline):
    if time.perf_counter() >= deadline:
        raise TimeoutError('worker wall budget exceeded')
    if torch.device(device).type == 'cuda':
        if torch.cuda.max_memory_allocated(device) > config['max_allocation_gib']*2**30:
            raise MemoryError('GPU allocation budget exceeded')


def reduced_arrays(small, masses, specs, U, labels, t):
    result = dict(U=U, labels=labels, time=np.array(t),
                  model_indices=np.arange(2, 2+len(specs), dtype=np.int64))
    for j, spec in enumerate(specs):
        width = spec['width']
        prefix = f'model_{j+2}_'
        for name, tensor in (('A', small.A[j, :width]),
                             ('K', small.M[j, :width, :width]),
                             ('w', small.w[j, :width]),
                             ('mu', masses[0][j, :width]),
                             ('nu', masses[1][j, :width])):
            result[prefix+name] = tensor.detach().cpu().numpy().copy()
    return result


def optimizer_summary(samplers):
    result = []
    for index, sampler in enumerate(samplers, start=2):
        diagnostics = sampler['diagnostics']
        row = dict(model_index=index)
        for layer in (1, 2):
            fits = diagnostics[f'cubature{layer}']['fits']
            row[f'cubature{layer}'] = dict(final=fits[-1], all_fits=fits,
                                         all_success=all(fit['success'] for fit in fits))
            row[f'frame{layer}'] = diagnostics[f'frame{layer}']
        result.append(row)
    return result


def validate_archive(case_out, record):
    """Independent reconstruction of metrics, residuals and reduced predictions."""
    case_out = Path(case_out)
    with np.load(case_out/'observations.npz', allow_pickle=False) as archive:
        arrays = {name: archive[name] for name in archive.files}
    times, predictions = arrays['times'], arrays['predictions']
    model_count, panel_count = len(record['model_names']), len(arrays['panel'])
    if times.ndim != 1 or times[0] != 0 or np.any(np.diff(times) <= 0):
        raise AssertionError('invalid saved time axis')
    if predictions.shape != (len(times), model_count, panel_count):
        raise AssertionError('prediction axis mismatch')
    if np.any(predictions[0] != 0) or np.any(arrays['training_predictions'][0] != 0):
        raise AssertionError('nonzero initial prediction')
    if not all(np.isfinite(value).all() for value in arrays.values()):
        raise AssertionError('nonfinite observations')
    residual = np.sqrt(np.mean((arrays['training_predictions']-arrays['labels'])**2, axis=2))
    np.testing.assert_allclose(residual, arrays['residual_rms'], rtol=2e-14, atol=2e-15)
    recomputed = comparison_metrics(predictions, record['n'])
    if recomputed != record['metrics']:
        raise AssertionError('stored metrics disagree with observations')
    errors = []
    expected_keys = {'U', 'labels', 'time', 'model_indices'}
    with np.load(case_out/'reduced_restart.npz', allow_pickle=False) as restart:
        np.testing.assert_array_equal(restart['U'], arrays['U'])
        np.testing.assert_array_equal(restart['labels'], arrays['labels'])
        if float(restart['time']) != float(times[-1]):
            raise AssertionError('restart time mismatch')
        np.testing.assert_array_equal(restart['model_indices'], np.arange(2, 2+len(record['samplers'])))
        for j, spec in enumerate(record['samplers'], start=2):
            prefix, width = f'model_{j}_', spec['width']
            expected_keys.update(prefix+key for key in ('A', 'K', 'w', 'mu', 'nu'))
            A, K, w, mu, nu = (restart[prefix+key] for key in ('A', 'K', 'w', 'mu', 'nu'))
            if (A.shape, K.shape, w.shape, mu.shape, nu.shape) != (
                    (width, 2), (width, width), (width,), (width,), (width,)):
                raise AssertionError('restart has incorrect retained state dimensions')
            for mass in (mu, nu):
                if np.any(mass <= 0) or not np.isclose(mass.sum(), 1., rtol=1e-6):
                    raise AssertionError('invalid retained masses')
            for key, target in (('U', arrays['training_predictions'][-1, j]),
                                ('panel', predictions[-1, j])):
                hidden = np.tanh(A @ arrays[key].T)
                actual = (nu*w) @ np.tanh(K @ (mu[:, None]*hidden))
                error = float(np.max(np.abs(actual-target)))
                errors.append(error)
                tolerance = 3e-6 if record['dtype'] == 'float32' else 2e-11
                np.testing.assert_allclose(actual, target, rtol=tolerance, atol=tolerance)
        if set(restart.files) != expected_keys:
            raise AssertionError('restart contains unexpected state or source arrays')
    with np.load(case_out/'initial_setup.npz', allow_pickle=False) as initial:
        if np.any(initial['dense_w'] != 0):
            raise AssertionError('dense initial readout is not zero')
        for j, spec in enumerate(record['samplers'], start=2):
            if np.any(initial[f'model_{j}_w'] != 0):
                raise AssertionError('sampler initial readout is not zero')
            np.testing.assert_array_equal(initial[f'model_{j}_A'],
                initial['reference_setup_A0'][initial[f'model_{j}_selected_first']])
    return dict(metrics_recomputed=True, residuals_recomputed=True,
                initial_readouts_zero=True, restart_contains_only_reduced_state=True,
                maximum_restart_prediction_error=max(errors, default=0.))


@torch.no_grad()
def run_case(case, config, device, out, deadline):
    begin = time.perf_counter()
    n, seed, angle, sign = (case[key] for key in ('n', 'seed', 'angle', 'sign'))
    case_id = f'n{n}_s{seed}_a{angle:g}_sign{sign:+d}'
    case_out = out/case_id
    case_out.mkdir(exist_ok=False)
    specs = sampler_specs(config, n)
    model_names = ['dense_reference', 'dense_independent'] + [s['name'] for s in specs]
    if config['include_frozen']:
        model_names.append('frozen_dense_hidden')
    metadata = dict(**case, copy_seed=seed+10000, samplers=specs, model_names=model_names,
                    dtype=config['dtype'], dt=config['dt'], probe_count=config['probe_count'],
                    mass_floor=config['mass_floor'], primary_metric='rms_of_time_sup',
                    restart_indexing='model index, identical to prediction axis')
    metadata['schedule'] = [dict(**spec, model_index=j, moving=spec['width']**2+3*spec['width'],
        fixed=2*spec['width']+6, total=spec['width']**2+5*spec['width']+6)
        for j, spec in enumerate(specs, start=2)]
    metadata['distinct_sampler_configurations'] = len({(s['width'], s['rank']) for s in specs})
    metadata['duplicate_sampler_aliases_are_independent_replicates'] = False
    write_json(case_out/'case_config.json', dict(case=case, config=config, model_names=model_names))
    times, predictions, training_predictions, residuals, motions = [], [], [], [], []
    dense = small = masses = None
    samplers = []
    step = 0
    U_np = np.array([[1., 0.], [math.cos(math.radians(angle)), math.sin(math.radians(angle))]])
    labels_np = np.array([.2, .1*sign])
    phi = 2*np.pi*(np.arange(config['panel'])+config['panel_offset'])/config['panel']
    panel_np = np.column_stack((np.cos(phi), np.sin(phi)))

    def observations():
        return dict(times=np.asarray(times), panel=panel_np, predictions=np.asarray(predictions),
                    training_predictions=np.asarray(training_predictions), residual_rms=np.asarray(residuals),
                    feature_motion=np.asarray(motions), labels=labels_np, U=U_np)

    try:
        check_budget(device, config, deadline)
        dtype = getattr(torch, config['dtype'])
        U = torch.tensor(U_np, device=device, dtype=dtype)
        labels = torch.tensor(labels_np, device=device, dtype=dtype)
        panel = torch.tensor(panel_np, device=device, dtype=dtype)
        dense, A0, W0 = make_dense(n, seed, device, dtype)
        def array_fingerprint(array):
            array = np.ascontiguousarray(array)
            return dict(shape=list(array.shape), dtype=str(array.dtype),
                        sha256=hashlib.sha256(memoryview(array).cast('B')).hexdigest())
        metadata['dense_initialization_recipe'] = dict(
            factory='gpu_sampling_experiment.make_dense', n=n, seed=seed,
            independent_seed=seed+10000, setup_dtype='float64', runtime_dtype=config['dtype'],
            initial_readout='exact zero', source_hashes='../provenance.json',
            array_fingerprints=dict(reference_setup_A0=array_fingerprint(A0),
                reference_setup_W0=array_fingerprint(W0),
                dense_A=array_fingerprint(dense.A.cpu().numpy()),
                dense_M=array_fingerprint(dense.M.cpu().numpy()),
                dense_w=array_fingerprint(dense.w.cpu().numpy())))
        write_json(case_out/'dense_initialization.json', metadata['dense_initialization_recipe'])
        initial = dict(reference_setup_A0=A0, U=U_np,
                       labels=labels_np, panel=panel_np, dense_A=dense.A.cpu().numpy(),
                       dense_w=dense.w.cpu().numpy())
        witness = prepare_witness(A0, W0, U_np, labels_np, probe_count=config['probe_count'])
        initial['setup_probes'] = witness['probes']
        save_arrays(case_out/'initial_setup.npz', **initial)
        for j, spec in enumerate(specs, start=2):
            check_budget(device, config, deadline)
            print(json.dumps(dict(case=case_id, phase='sampler_setup_started', model_index=j,
                                  sampler=spec, wall_seconds=time.perf_counter()-begin)), flush=True)
            sampler = build_sampler(A0, W0, U_np, labels_np, spec['width'],
                basis_rank=spec['rank'], probe_count=config['probe_count'],
                mass_floor=config['mass_floor'], singular_tolerance=1e-10, witness=witness)
            check_budget(device, config, deadline)
            samplers.append(sampler)
            for key in ('A', 'B', 'w', 'mu', 'nu', 'selected_first', 'selected_second'):
                initial[f'model_{j}_{key}'] = sampler[key]
            initial[f'model_{j}_K'] = sampler['B']/sampler['mu'][None, :]
            save_arrays(case_out/'initial_setup.npz', **initial)
            write_json(case_out/'setup_diagnostics.json', dict(
                completed_samplers=len(samplers), sampler_diagnostics=[s['diagnostics'] for s in samplers],
                optimizer_and_frame_status=optimizer_summary(samplers)))
            print(json.dumps(dict(case=case_id, phase='sampler_setup_complete', model_index=j,
                                  wall_seconds=time.perf_counter()-begin)), flush=True)
        small, masses = pack_samplers(samplers, device, dtype)
        check_budget(device, config, deadline)
        # Preserve both float64 construction and exact working-dtype initialization.
        save_arrays(case_out/'initial_reduced_runtime.npz',
                    **reduced_arrays(small, masses, specs, U_np, labels_np, 0.))
        metadata['sampler_diagnostics'] = [s['diagnostics'] for s in samplers]
        metadata['optimizer_and_frame_status'] = optimizer_summary(samplers)
        del witness, A0, W0, initial, samplers
        hd0, gd0, _ = fields(dense, U)
        hs0, gs0, _ = fields(small, U, masses)
        gram = (gd0[0].T @ gd0[0]/n).cpu().numpy()
        evals, evecs = np.linalg.eigh(gram)
        cross = None
        if config['include_frozen']:
            cross = (gd0[0].T @ fields(dense, panel)[1][0]/n).cpu().numpy()
        metadata['initial_gram_eigenvalues'] = evals.tolist()
        metadata['setup_seconds'] = time.perf_counter()-begin

        def observe(t):
            check_budget(device, config, deadline)
            for state in (dense, small):
                if not all(bool(torch.isfinite(value).all()) for value in state.arrays()):
                    raise FloatingPointError('nonfinite state')
            hd, gd, fd = fields(dense, U)
            hs, gs, fs = fields(small, U, masses)
            prediction_parts = [fields(dense, panel)[2].cpu().numpy(),
                                fields(small, panel, masses)[2].cpu().numpy()]
            fit_parts = [fd.cpu().numpy(), fs.cpu().numpy()]
            motion_parts = [feature_motion(hd, gd, hd0, gd0).cpu().numpy(),
                            feature_motion(hs, gs, hs0, gs0, masses).cpu().numpy()]
            if cross is not None:
                # Continuous extension at zero eigenvalue avoids a 0/0 control.
                factor = np.full_like(evals, t)
                np.divide(-np.expm1(-evals*t), evals, out=factor, where=np.abs(evals)>1e-14)
                coeff = evecs @ (factor*(evecs.T @ labels_np))
                prediction_parts.append((coeff @ cross)[None])
                fit_parts.append((coeff @ gram)[None])
                motion_parts.append(np.zeros((1, 2)))
            prediction, fit, motion = map(np.concatenate, (prediction_parts, fit_parts, motion_parts))
            if not all(np.isfinite(value).all() for value in (prediction, fit, motion)):
                raise FloatingPointError('nonfinite observation')
            predictions.append(prediction)
            training_predictions.append(fit)
            residuals.append(np.sqrt(np.mean((fit-labels_np)**2, axis=1)))
            motions.append(motion)
            times.append(t)
            check_budget(device, config, deadline)

        observe(0.)
        stride = round(config['observe_every']/config['dt'])
        first_steps = round(config['horizon']/config['dt'])
        max_steps = round(config['max_horizon']/config['dt'])
        end_step = first_steps
        extended = False
        evolution_start = time.perf_counter()
        for next_step in range(1, max_steps+1):
            check_budget(device, config, deadline)
            dense_next = heun(dense, U, labels, config['dt'])
            small_next = heun(small, U, labels, config['dt'], masses)
            dense, small = dense_next, small_next
            step = next_step
            if step % stride == 0 or step in (first_steps, max_steps):
                observe(round(step*config['dt'], 12))
            if step == first_steps:
                if np.max(residuals[-1][:2+len(specs)]) > 1e-6:
                    end_step = max_steps
                    extended = max_steps > first_steps
                else:
                    break
            if step >= end_step:
                break
        if torch.device(device).type == 'cuda':
            torch.cuda.synchronize(device)
        if times[-1] != round(step*config['dt'], 12):
            observe(round(step*config['dt'], 12))
        metadata['evolution_seconds'] = time.perf_counter()-evolution_start
        target_tail_time = times[-1]-10.
        tail_index = int(np.argmin(np.abs(np.asarray(times)-max(0., target_tail_time))))
        tail = np.max(np.abs(predictions[-1]-predictions[tail_index]), axis=1)
        settled = (residuals[-1] <= 1e-6) & (tail <= 1e-5) & (times[-1] >= 10.)
        metadata.update(metrics=comparison_metrics(np.asarray(predictions), n),
            last_residual_rms=residuals[-1].tolist(), last_ten_time_change=tail.tolist(),
            tail_comparison_time=times[tail_index], settled=settled.tolist(),
            last_time=times[-1], horizon_extended=extended,
            feature_motion_final=motions[-1].tolist(), total_seconds=time.perf_counter()-begin)
        save_arrays(case_out/'observations.npz', **observations())
        save_arrays(case_out/'reduced_restart.npz',
                    **reduced_arrays(small, masses, specs, U_np, labels_np, times[-1]))
        metadata['archive_validation'] = validate_archive(case_out, metadata)
        for filename in ('observations.npz', 'reduced_restart.npz', 'initial_setup.npz',
                         'initial_reduced_runtime.npz', 'setup_diagnostics.json', 'dense_initialization.json'):
            metadata[filename+'_sha256'] = sha256(case_out/filename)
        write_json(case_out/'record.json', metadata)
        print(json.dumps(dict(case=case_id, T=times[-1], seconds=metadata['total_seconds'],
            primary=[row['rms_of_time_sup'] for row in metadata['metrics']],
            settled=settled.tolist())), flush=True)
        return metadata
    except BaseException as exc:
        failure = dict(**case, error=repr(exc), traceback=traceback.format_exc(),
                       completed_step=step, state_time=round(step*config['dt'], 12),
                       observation_count=len(times), wall_seconds=time.perf_counter()-begin)
        for filename, operation in (
            ('partial_observations.npz', lambda: observations()),
            ('partial_reduced_restart.npz', lambda: reduced_arrays(small, masses, specs,
                U_np, labels_np, round(step*config['dt'], 12)) if small is not None else None),
        ):
            try:
                arrays = operation()
                if arrays is not None:
                    save_arrays(case_out/filename, **arrays)
            except Exception as save_error:
                failure[filename+'_save_error'] = repr(save_error)
        write_json(case_out/'failure.json', failure)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    parser.add_argument('--device', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--budget-seconds', type=float)
    args = parser.parse_args()
    if torch.device(args.device).type != 'cuda':
        parser.error('training main requires an explicit CUDA device; CPU runs are forbidden')
    if not torch.cuda.is_available():
        parser.error('CUDA is unavailable')
    raw_config = Path(args.config).read_bytes()
    config = normalize_config(json.loads(raw_config))
    if args.budget_seconds is not None:
        if not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0:
            parser.error('--budget-seconds must be finite and positive')
        config['budget_seconds'] = args.budget_seconds
    settings()
    torch.cuda.set_device(args.device)
    torch.cuda.reset_peak_memory_stats(args.device)
    total_memory = torch.cuda.get_device_properties(args.device).total_memory
    torch.cuda.set_per_process_memory_fraction(min(1., config['max_allocation_gib']*2**30/total_memory), args.device)
    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=False)
    sources = archive_sources(out, args, config, raw_config)
    start = time.perf_counter()
    deadline = start+config['budget_seconds']
    status = dict(completed=[], failures=[], unstarted_cases=config['cases'])

    def alarm_handler(signum, frame):
        raise TimeoutError('worker wall budget alarm exceeded')

    previous_handler = signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, config['budget_seconds'])
    try:
        checks = dict(dynamics=validate_core(args.device), metrics=validate_metrics())
        write_json(out/'core_validation.json', checks)
        for index, case in enumerate(config['cases']):
            status['unstarted_cases'] = config['cases'][index+1:]
            try:
                verify_sources(sources)
                record = run_case(case, config, args.device, out, deadline)
                verify_sources(sources)
                status['completed'].append({key: record[key] for key in
                                           ('n', 'seed', 'angle', 'sign', 'total_seconds', 'last_time')})
            except BaseException as exc:
                status['failures'].append(dict(**case, error=repr(exc)))
                write_json(out/'status.json', status)
                raise
            write_json(out/'status.json', status)
    except BaseException as exc:
        status['worker_error'] = repr(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, previous_handler)
        status['wall_seconds'] = time.perf_counter()-start
        status['peak_gpu_allocated'] = torch.cuda.max_memory_allocated(args.device)
        write_json(out/'status.json', status)


if __name__ == '__main__':
    main()
