"""Bounded explicit-dataset extension of the initialization-only GPU sampler.

Physical inputs x=sqrt(d)*U have unit normalized directions U. The unhalved
mean-square loss contributes 2/m to every velocity. The original Heun kernel
is reused with step dt*2/m, exactly implementing this common scalar factor.
Dense reference/copy states are batched separately from the reduced states.
CLI scientific execution requires CUDA; tiny deterministic checks are callable.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
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
from gpu_sampling_experiment import (Batch, NetworkEngine, settings, fields,
    feature_motion, rhs as _rhs, heun as _heun, max_difference)
from gpu_rms_growth_experiment import (write_json, save_arrays, sha256,
    comparison_metrics, validate_metrics, check_budget, verify_sources,
    reduced_arrays, optimizer_summary)
from neuron_sampling_multidata import unit_rows, prepare_witness, build_sampler

DEFAULTS = dict(dt=.2, observe_every=1., horizon=120., max_horizon=1200.,
    settlement_every=120., tail_window=10., fit_tolerance=1e-6,
    settlement_tolerance=1e-5, mass_floor=.05, singular_tolerance=1e-10,
    max_allocation_gib=8., budget_seconds=1200., dtype='float64')


def rhs(state, U, labels, masses=None):
    return Batch(*(value*(2./len(U)) for value in _rhs(state, U, labels, masses).arrays()))


def heun(state, U, labels, dt, masses=None):
    return _heun(state, U, labels, dt*(2./len(U)), masses)


def make_dense(n, seed, device, dtype, d=2):
    engines = [NetworkEngine(d, n, s, device='cpu', dtype=torch.float64)
               for s in (seed, seed+10000)]
    A = np.stack([engine.initial.w.numpy() for engine in engines])
    M = np.stack([engine.initial.M.numpy() for engine in engines])
    return (Batch(torch.tensor(A, device=device, dtype=dtype),
                  torch.tensor(M, device=device, dtype=dtype),
                  torch.zeros((2, n), device=device, dtype=dtype)),
            A[0].copy(), M[0].copy())


def pack_samplers(samplers, device, dtype):
    if not samplers:
        return None, None
    count, size = len(samplers), max(len(s['mu']) for s in samplers)
    d = samplers[0]['A'].shape[1]
    A, K, w = np.zeros((count, size, d)), np.zeros((count, size, size)), np.zeros((count, size))
    mu, nu = np.zeros((count, size)), np.zeros((count, size))
    for j, sampler in enumerate(samplers):
        n1, n2 = len(sampler['mu']), len(sampler['nu'])
        A[j, :n1] = sampler['A']
        K[j, :n2, :n1] = sampler['B']/sampler['mu'][None, :]
        w[j, :n2], mu[j, :n1], nu[j, :n2] = sampler['w'], sampler['mu'], sampler['nu']
    tensor = lambda value: torch.tensor(value, device=device, dtype=dtype)
    return Batch(tensor(A), tensor(K), tensor(w)), (tensor(mu), tensor(nu))


def state_count(width, d, m):
    return dict(moving=width*width+(d+1)*width, fixed=2*width+m*(d+1),
                total=width*width+(d+3)*width+m*(d+1))


def sampler_specs(config, n, d, m):
    result = []
    for candidate in config['samplers']:
        row = dict(candidate)
        if 'coefficient_multiplier' in row:
            budget = row['coefficient_multiplier']*2550*(math.log(n)/math.log(512))**4
            discriminant = (d+3)**2+4*(budget-m*(d+1))
            width = math.floor((math.sqrt(max(0., discriminant))-(d+3))/2)
            width = min(n, max(0, width))
            while width > 0 and state_count(width, d, m)['total'] > budget+1e-10:
                width -= 1
            row.update(budget=budget, width=width)
        row.update(state_count(row['width'], d, m))
        result.append(row)
    return result


def _integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return value


def normalize_config(raw):
    if not isinstance(raw, dict):
        raise ValueError('configuration must be an object')
    allowed = set(DEFAULTS) | {'datasets', 'cases', 'samplers', 'description', 'stage', 'protocol', 'source_files'}
    if set(raw)-allowed:
        raise ValueError(f'unknown keys: {sorted(set(raw)-allowed)}')
    config = {**DEFAULTS, **raw}
    for name, value in DEFAULTS.items():
        if name == 'dtype':
            continue
        supplied = config[name]
        if isinstance(supplied, bool) or not isinstance(supplied, (int, float)) or not math.isfinite(supplied) or supplied <= 0:
            raise ValueError(f'{name} must be finite and positive')
    if config['dtype'] not in ('float32', 'float64'):
        raise ValueError('dtype must be float32 or float64')
    if max(config['mass_floor'], config['singular_tolerance']) >= 1:
        raise ValueError('mass_floor and singular_tolerance must be <1')
    if config['max_horizon'] < config['horizon'] or config['horizon'] < config['tail_window']:
        raise ValueError('require max_horizon >= horizon >= tail_window')
    for name in ('observe_every', 'horizon', 'max_horizon', 'settlement_every', 'tail_window'):
        ratio = config[name]/config['dt']
        if round(ratio) < 1 or not math.isclose(ratio, round(ratio), abs_tol=1e-8, rel_tol=0):
            raise ValueError(f'{name} must be a positive multiple of dt')
    datasets = config.get('datasets')
    if not isinstance(datasets, dict) or not datasets:
        raise ValueError('datasets must be a nonempty id-to-dataset map')
    for name, dataset in datasets.items():
        if not re.fullmatch(r'[A-Za-z0-9_-]+', name):
            raise ValueError('dataset ids must be filename-safe')
        required = {'U', 'labels', 'setup_probes', 'query_panel'}
        if not isinstance(dataset, dict) or not required <= set(dataset):
            raise ValueError('dataset requires U, labels, setup_probes, query_panel')
        if set(dataset)-required-{'description', 'metadata'}:
            raise ValueError(f'unknown dataset fields: {name}')
        U = unit_rows(dataset['U'], f'{name}.U')
        labels = np.asarray(dataset['labels'], dtype=np.float64)
        if labels.shape != (len(U),) or not np.isfinite(labels).all():
            raise ValueError(f'{name}: invalid labels')
        for key in ('setup_probes', 'query_panel'):
            unit_rows(dataset[key], f'{name}.{key}', U.shape[1])
    candidates = config.get('samplers')
    if not isinstance(candidates, list) or not candidates:
        raise ValueError('samplers must be nonempty')
    names = set()
    for row in candidates:
        if not isinstance(row, dict) or not {'name', 'rank'} <= set(row):
            raise ValueError('sampler requires name and rank')
        if ('width' in row) == ('coefficient_multiplier' in row):
            raise ValueError('specify exactly one of width and coefficient_multiplier')
        if set(row)-{'name', 'rank', 'width', 'coefficient_multiplier'}:
            raise ValueError('unknown sampler field')
        if not isinstance(row['name'], str) or not re.fullmatch(r'[A-Za-z0-9_-]+', row['name']) or row['name'] in names or row['name'].startswith('dense_'):
            raise ValueError('sampler names must be unique and filename-safe')
        names.add(row['name'])
        _integer(row['rank'], 'rank')
        if 'width' in row:
            _integer(row['width'], 'width', 4)
        else:
            value = row['coefficient_multiplier']
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
                raise ValueError('coefficient_multiplier must be finite and positive')
    cases, seen = config.get('cases'), set()
    if not isinstance(cases, list) or not cases:
        raise ValueError('cases must be a nonempty list')
    for case in cases:
        if not isinstance(case, dict) or set(case) != {'dataset_id', 'n', 'seed'}:
            raise ValueError('cases require exactly dataset_id, n, seed')
        if case['dataset_id'] not in datasets:
            raise ValueError('unknown dataset_id')
        _integer(case['n'], 'n', 4)
        _integer(case['seed'], 'seed', 0)
        key = case['dataset_id'], case['n'], case['seed']
        if key in seen:
            raise ValueError('duplicate case')
        seen.add(key)
    sources = list(config.get('source_files', []))
    if config.get('protocol'):
        sources.append(config['protocol'])
    for name in sources:
        path = (ROOT/name).resolve()
        if not path.is_relative_to(HERE) or not path.is_file():
            raise ValueError('source files/protocol must exist in this study')
    return config


def array_fingerprint(value):
    value = np.ascontiguousarray(value)
    return dict(shape=list(value.shape), dtype=str(value.dtype),
                sha256=hashlib.sha256(memoryview(value).cast('B')).hexdigest())


def archive_sources(out, args, config, raw_config):
    paths = {Path(__file__).resolve(), HERE/'neuron_sampling_multidata.py',
        HERE/'neuron_sampling_setup.py', HERE/'gpu_sampling_experiment.py',
        HERE/'gpu_rms_growth_experiment.py', ROOT/'code/README.md'}
    for module in tuple(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename:
            path = Path(filename).resolve()
            if path.is_relative_to(ROOT/'code/pde') and path.suffix == '.py':
                paths.add(path)
    paths.update((ROOT/name).resolve() for name in config.get('source_files', []))
    if config.get('protocol'):
        paths.add((ROOT/config['protocol']).resolve())
    hashes = {}
    for path in sorted(paths):
        relative, data = str(path.relative_to(ROOT)), path.read_bytes()
        target = out/'sources'/relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        hashes[relative] = hashlib.sha256(data).hexdigest()
    (out/'config.input.json').write_bytes(raw_config)
    write_json(out/'config.resolved.json', config)
    write_json(out/'provenance.json', dict(args=vars(args), argv=sys.argv,
        cwd=os.getcwd(), executable=sys.executable, python=sys.version,
        platform=platform.platform(), numpy=np.__version__, scipy=scipy.__version__,
        torch=torch.__version__, cuda=torch.version.cuda,
        gpu=torch.cuda.get_device_name(args.device), source_hashes=hashes,
        config_input_sha256=sha256(out/'config.input.json'),
        config_resolved_sha256=sha256(out/'config.resolved.json'),
        threads=torch.get_num_threads(), interop_threads=torch.get_num_interop_threads(),
        thread_environment={key: os.environ.get(key) for key in
            ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')},
        tf32_matmul=torch.backends.cuda.matmul.allow_tf32,
        tf32_cudnn=torch.backends.cudnn.allow_tf32,
        primary_metric='rms_of_time_sup', source_changes_policy='stop; preserve output'))
    return hashes


def load_reduced_restart(path, model_index, device='cpu'):
    """Load one model without source initialization, dense state, or history."""
    with np.load(path, allow_pickle=False) as arrays:
        if model_index not in arrays['model_indices']:
            raise ValueError('model_index absent from restart')
        prefix = f'model_{model_index}_'
        tensor = lambda key: torch.from_numpy(arrays[key].copy()).to(device)
        state = Batch(*(tensor(prefix+key)[None] for key in ('A', 'K', 'w')))
        masses = tuple(tensor(prefix+key)[None] for key in ('mu', 'nu'))
        U = tensor('U').to(state.A.dtype)
        labels = tensor('labels').to(state.A.dtype)
        return state, masses, U, labels, float(arrays['time'])


def settlement(times, predictions, residuals, config):
    times = np.asarray(times)
    tail_start = float(times[-1])-config['tail_window']
    mask = times >= tail_start-1e-10
    tail = np.max(np.abs(np.asarray(predictions)[mask]-predictions[-1]), axis=(0, 2))
    settled = ((np.asarray(residuals[-1]) <= config['fit_tolerance']) &
               (tail <= config['settlement_tolerance']) & (tail_start >= -1e-10))
    return tail, settled, float(times[mask][0])


def validate_archive(case_out, record):
    """Recompute metrics and reconstruct retained-state predictions independently."""
    case_out = Path(case_out)
    with np.load(case_out/'observations.npz', allow_pickle=False) as archive:
        arrays = {name: archive[name] for name in archive.files}
    times, predictions = arrays['times'], arrays['predictions']
    if times.ndim != 1 or times[0] != 0 or np.any(np.diff(times) <= 0):
        raise AssertionError('invalid saved times')
    if predictions.shape != (len(times), len(record['model_names']), len(arrays['panel'])):
        raise AssertionError('prediction shape mismatch')
    if not all(np.isfinite(value).all() for value in arrays.values()):
        raise AssertionError('nonfinite observation archive')
    if np.any(predictions[0] != 0) or np.any(arrays['training_predictions'][0] != 0):
        raise AssertionError('nonzero initial predictions')
    np.testing.assert_allclose(np.sqrt(np.mean((arrays['training_predictions']-arrays['labels'])**2, axis=2)), arrays['residual_rms'], rtol=2e-14, atol=2e-15)
    if comparison_metrics(predictions, record['n']) != record['metrics']:
        raise AssertionError('metrics do not recompute')
    expected = {'U', 'labels', 'time', 'model_indices'}
    errors = []
    with np.load(case_out/'reduced_restart.npz', allow_pickle=False) as restart:
        np.testing.assert_array_equal(restart['U'], arrays['U'])
        np.testing.assert_array_equal(restart['labels'], arrays['labels'])
        np.testing.assert_array_equal(restart['model_indices'], np.arange(2, 2+len(record['samplers'])))
        if float(restart['time']) != times[-1]:
            raise AssertionError('restart time mismatch')
        for j, spec in enumerate(record['samplers'], start=2):
            prefix, width = f'model_{j}_', spec['width']
            expected.update(prefix+key for key in ('A', 'K', 'w', 'mu', 'nu'))
            A, K, w, mu, nu = (restart[prefix+key] for key in ('A', 'K', 'w', 'mu', 'nu'))
            if (A.shape, K.shape, w.shape, mu.shape, nu.shape) != ((width, record['d']), (width, width), (width,), (width,), (width,)):
                raise AssertionError('incorrect retained shapes')
            if sum(value.size for value in (A, K, w, mu, nu))+arrays['U'].size+arrays['labels'].size != spec['total']:
                raise AssertionError('incorrect retained count')
            for mass in (mu, nu):
                if np.any(mass <= 0) or not np.isclose(mass.sum(), 1., rtol=1e-6):
                    raise AssertionError('invalid masses')
            for key, target in (('U', arrays['training_predictions'][-1, j]), ('panel', predictions[-1, j])):
                actual = (nu*w) @ np.tanh(K @ (mu[:, None]*np.tanh(A @ arrays[key].T)))
                errors.append(float(np.max(np.abs(actual-target))))
                tolerance = 3e-6 if record['dtype'] == 'float32' else 2e-11
                np.testing.assert_allclose(actual, target, rtol=tolerance, atol=tolerance)
        if set(restart.files) != expected:
            raise AssertionError('unexpected retained arrays')
    with np.load(case_out/'initial_setup.npz', allow_pickle=False) as initial:
        if np.any(initial['dense_w'] != 0):
            raise AssertionError('nonzero initial dense readout')
        for j, spec in enumerate(record['samplers'], start=2):
            if np.any(initial[f'model_{j}_w'] != 0):
                raise AssertionError('nonzero initial reduced readout')
            np.testing.assert_array_equal(initial[f'model_{j}_A'], initial['reference_setup_A0'][initial[f'model_{j}_selected_first']])
    return dict(metrics_recomputed=True, residuals_recomputed=True,
        initial_readouts_zero=True, retained_counts_verified=True,
        restart_contains_only_reduced_state=True,
        maximum_restart_prediction_error=max(errors, default=0.))


@torch.no_grad()
def run_case(case, config, device, out, deadline):
    begin = time.perf_counter()
    n, seed, dataset_id = case['n'], case['seed'], case['dataset_id']
    case_id = f'{dataset_id}_n{n}_s{seed}'
    case_out = Path(out)/case_id
    case_out.mkdir(exist_ok=False)
    dataset = config['datasets'][dataset_id]
    U_np, labels_np, probes_np, panel_np = (np.asarray(dataset[key], dtype=np.float64)
        for key in ('U', 'labels', 'setup_probes', 'query_panel'))
    m, d = U_np.shape
    requested = sampler_specs(config, n, d, m)
    specs, samplers, setup_failures = [], [], []
    metadata = dict(**case, d=d, m=m, copy_seed=seed+10000, dtype=config['dtype'],
        dt=config['dt'], physical_rhs_factor=2./m, mass_floor=config['mass_floor'],
        primary_metric='rms_of_time_sup', probe_count=len(probes_np),
        query_count=len(panel_np), requested_samplers=requested,
        restart_indexing='model index identical to prediction axis',
        settlement_definition='residual RMS and maximum endpoint-relative query excursion over all saved times in final tail window')
    write_json(case_out/'case_config.json', dict(case=case, config=config))
    times, predictions, training_predictions, residuals, motions = [], [], [], [], []
    dense = small = masses = None
    step = 0

    def observations():
        return dict(times=np.asarray(times), panel=panel_np, predictions=np.asarray(predictions),
            training_predictions=np.asarray(training_predictions), residual_rms=np.asarray(residuals),
            feature_motion=np.asarray(motions), labels=labels_np, U=U_np)

    try:
        check_budget(device, config, deadline)
        dtype = getattr(torch, config['dtype'])
        U, labels, panel = (torch.tensor(value, device=device, dtype=dtype)
                            for value in (U_np, labels_np, panel_np))
        dense, A0, W0 = make_dense(n, seed, device, dtype, d)
        metadata['dense_initialization_recipe'] = dict(
            factory='gpu_multidata_experiment.make_dense using maintained NetworkEngine',
            n=n, d=d, seed=seed, independent_seed=seed+10000,
            setup_dtype='float64', runtime_dtype=config['dtype'], initial_readout='exact zero',
            array_fingerprints={key: array_fingerprint(value) for key, value in
                (('reference_setup_A0', A0), ('reference_setup_W0', W0),
                 ('dense_A', dense.A.cpu().numpy()), ('dense_M', dense.M.cpu().numpy()),
                 ('dense_w', dense.w.cpu().numpy()), ('U', U_np), ('labels', labels_np),
                 ('setup_probes', probes_np), ('query_panel', panel_np))})
        write_json(case_out/'dense_initialization.json', metadata['dense_initialization_recipe'])
        initial = dict(reference_setup_A0=A0, U=U_np, labels=labels_np, panel=panel_np,
            dense_A=dense.A.cpu().numpy(), dense_w=dense.w.cpu().numpy(), setup_directions=probes_np)
        witness = prepare_witness(A0, W0, U_np, labels_np, setup_probes=probes_np)
        initial['setup_probes'] = witness['probes']
        save_arrays(case_out/'initial_setup.npz', **initial)
        for candidate_index, spec in enumerate(requested):
            check_budget(device, config, deadline)
            print(json.dumps(dict(case=case_id, phase='sampler_setup_started', candidate_index=candidate_index, sampler=spec)), flush=True)
            try:
                sampler = build_sampler(A0, W0, U_np, labels_np, spec['width'],
                    setup_probes=probes_np, basis_rank=spec['rank'], mass_floor=config['mass_floor'],
                    singular_tolerance=config['singular_tolerance'], witness=witness)
            except (TimeoutError, MemoryError):
                raise
            except Exception as exc:
                failure = dict(candidate_index=candidate_index, sampler=spec,
                    error=repr(exc), traceback=traceback.format_exc())
                setup_failures.append(failure)
                write_json(case_out/'setup_failures.json', setup_failures)
                print(json.dumps(dict(case=case_id, phase='sampler_setup_failed', **failure)), flush=True)
                continue
            check_budget(device, config, deadline)
            j = 2+len(specs)
            specs.append(dict(**spec, candidate_index=candidate_index, model_index=j))
            samplers.append(sampler)
            for key in ('A', 'B', 'w', 'mu', 'nu', 'selected_first', 'selected_second'):
                initial[f'model_{j}_{key}'] = sampler[key]
            initial[f'model_{j}_K'] = sampler['B']/sampler['mu'][None, :]
            save_arrays(case_out/'initial_setup.npz', **initial)
            write_json(case_out/'setup_diagnostics.json', dict(samplers=specs,
                sampler_diagnostics=[s['diagnostics'] for s in samplers],
                optimizer_and_frame_status=optimizer_summary(samplers), setup_failures=setup_failures))
        small, masses = pack_samplers(samplers, device, dtype)
        metadata.update(samplers=specs, schedule=specs, setup_failures=setup_failures,
            model_names=['dense_reference', 'dense_independent']+[s['name'] for s in specs],
            sampler_diagnostics=[s['diagnostics'] for s in samplers],
            optimizer_and_frame_status=optimizer_summary(samplers),
            distinct_sampler_configurations=len({(s['width'], s['rank']) for s in specs}),
            duplicate_sampler_aliases_are_independent_replicates=False)
        write_json(case_out/'setup_failures.json', setup_failures)
        write_json(case_out/'setup_diagnostics.json', dict(samplers=specs,
            sampler_diagnostics=metadata['sampler_diagnostics'],
            optimizer_and_frame_status=metadata['optimizer_and_frame_status'], setup_failures=setup_failures))
        save_arrays(case_out/'initial_reduced_runtime.npz', **reduced_arrays(small, masses, specs, U_np, labels_np, 0.))
        del witness, A0, W0, initial, samplers
        hd0, gd0, _ = fields(dense, U)
        hs0, gs0 = (fields(small, U, masses)[:2] if small is not None else (None, None))
        metadata['initial_gram_eigenvalues'] = np.linalg.eigvalsh((gd0[0].T @ gd0[0]/n).cpu().numpy()).tolist()
        metadata['setup_seconds'] = time.perf_counter()-begin

        def observe(t):
            check_budget(device, config, deadline)
            for state in (dense, small):
                if state is not None and not all(bool(torch.isfinite(value).all()) for value in state.arrays()):
                    raise FloatingPointError('nonfinite state')
            hd, gd, fd = fields(dense, U)
            prediction_parts = [fields(dense, panel)[2].cpu().numpy()]
            fit_parts, motion_parts = [fd.cpu().numpy()], [feature_motion(hd, gd, hd0, gd0).cpu().numpy()]
            if small is not None:
                hs, gs, fs = fields(small, U, masses)
                prediction_parts.append(fields(small, panel, masses)[2].cpu().numpy())
                fit_parts.append(fs.cpu().numpy())
                motion_parts.append(feature_motion(hs, gs, hs0, gs0, masses).cpu().numpy())
            prediction, fit, motion = map(np.concatenate, (prediction_parts, fit_parts, motion_parts))
            if not all(np.isfinite(value).all() for value in (prediction, fit, motion)):
                raise FloatingPointError('nonfinite observations')
            predictions.append(prediction)
            training_predictions.append(fit)
            residuals.append(np.sqrt(np.mean((fit-labels_np)**2, axis=1)))
            motions.append(motion)
            times.append(t)

        observe(0.)
        stride, first_steps, max_steps, settle_stride = (round(config[key]/config['dt'])
            for key in ('observe_every', 'horizon', 'max_horizon', 'settlement_every'))
        settlement_checks = []
        evolution_start = time.perf_counter()
        for next_step in range(1, max_steps+1):
            check_budget(device, config, deadline)
            dense = heun(dense, U, labels, config['dt'])
            if small is not None:
                small = heun(small, U, labels, config['dt'], masses)
            step = next_step
            checkpoint = step >= first_steps and (step-first_steps) % settle_stride == 0
            if step % stride == 0 or checkpoint or step == max_steps:
                observe(round(step*config['dt'], 12))
            if checkpoint or step == max_steps:
                tail, settled, tail_start = settlement(times, predictions, residuals, config)
                settlement_checks.append(dict(time=times[-1], residual_rms=residuals[-1].tolist(),
                    tail_excursion=tail.tolist(), settled=settled.tolist(), tail_start_time=tail_start))
                print(json.dumps(dict(case=case_id, phase='settlement_check', **settlement_checks[-1])), flush=True)
                if settled.all():
                    break
        if torch.device(device).type == 'cuda':
            torch.cuda.synchronize(device)
        metadata['evolution_seconds'] = time.perf_counter()-evolution_start
        tail, settled, tail_start = settlement(times, predictions, residuals, config)
        metadata.update(metrics=comparison_metrics(np.asarray(predictions), n),
            last_residual_rms=residuals[-1].tolist(), last_ten_time_change=tail.tolist(),
            tail_comparison_time=tail_start, settled=settled.tolist(), settlement_checks=settlement_checks,
            last_time=times[-1], horizon_extended=times[-1]>config['horizon'],
            feature_motion_final=motions[-1].tolist(), total_seconds=time.perf_counter()-begin)
        save_arrays(case_out/'observations.npz', **observations())
        save_arrays(case_out/'reduced_restart.npz', **reduced_arrays(small, masses, specs, U_np, labels_np, times[-1]))
        metadata['archive_validation'] = validate_archive(case_out, metadata)
        for name in ('observations.npz', 'reduced_restart.npz', 'initial_setup.npz',
            'initial_reduced_runtime.npz', 'setup_diagnostics.json', 'setup_failures.json', 'dense_initialization.json'):
            metadata[name+'_sha256'] = sha256(case_out/name)
        write_json(case_out/'record.json', metadata)
        print(json.dumps(dict(case=case_id, phase='complete', T=times[-1],
            seconds=metadata['total_seconds'], primary=[row['rms_of_time_sup'] for row in metadata['metrics']],
            settled=settled.tolist(), setup_failure_count=len(setup_failures))), flush=True)
        return metadata
    except BaseException as exc:
        failure = dict(**case, error=repr(exc), traceback=traceback.format_exc(),
            completed_step=step, state_time=round(step*config['dt'], 12),
            observation_count=len(times), wall_seconds=time.perf_counter()-begin,
            completed_samplers=specs, setup_failures=setup_failures)
        for filename, operation in (
            ('partial_observations.npz', observations),
            ('partial_reduced_restart.npz', lambda: reduced_arrays(small, masses, specs,
                U_np, labels_np, round(step*config['dt'], 12)) if small is not None else None)):
            try:
                arrays = operation()
                if arrays is not None:
                    save_arrays(case_out/filename, **arrays)
            except Exception as save_error:
                failure[filename+'_save_error'] = repr(save_error)
        write_json(case_out/'failure.json', failure)
        raise


def validate_core(device='cpu'):
    errors = {}
    for d, m in ((2, 2), (3, 4), (5, 8)):
        dtype = torch.float64
        rng = np.random.default_rng(100+d)
        U_np = rng.normal(size=(m, d)); U_np /= np.linalg.norm(U_np, axis=1)[:, None]
        U = torch.tensor(U_np, device=device, dtype=dtype)
        labels = torch.linspace(-.2, .2, m, device=device, dtype=dtype)
        engine = NetworkEngine(d, 7, 811, device=device, dtype=dtype)
        state = engine.initial_state()
        state.c.copy_(torch.linspace(-.3, .2, 7, device=device, dtype=dtype))
        data = engine.prepare_data(U, labels)
        s = Batch(state.w[None], state.M[None], state.c[None])
        public = engine.rhs(state, data)
        expected = Batch(public.w[None], public.M[None], public.c[None])
        row = dict(rhs_public=max_difference(rhs(s, U, labels), expected))
        public_next = engine.heun_step(state, data, .02)
        expected_next = Batch(public_next.w[None], public_next.M[None], public_next.c[None])
        row['heun_public'] = max_difference(heun(s, U, labels, .02), expected_next)
        mass = torch.full((1, 7), 1/7, device=device, dtype=dtype)
        weighted = Batch(s.A.clone(), s.M*7, s.w.clone())
        actual = rhs(weighted, U, labels, (mass, mass))
        row['uniform_weighted_rhs'] = max_difference(Batch(actual.A, actual.M/7, actual.w), expected)
        gen = torch.Generator(device=device).manual_seed(839)
        A = torch.randn((1, 4, d), generator=gen, device=device, dtype=dtype).requires_grad_()
        K = (.2*torch.randn((1, 3, 4), generator=gen, device=device, dtype=dtype)).requires_grad_()
        w = (.2*torch.randn((1, 3), generator=gen, device=device, dtype=dtype)).requires_grad_()
        mu = torch.tensor([[.1, .2, .3, .4]], device=device, dtype=dtype)
        nu = torch.tensor([[.2, .3, .5]], device=device, dtype=dtype)
        z = Batch(A, K, w)
        loss = (fields(z, U, (mu, nu))[2]-labels).square().mean()
        gradients = torch.autograd.grad(loss, (A, K, w))
        oracle = Batch(-gradients[0]/mu[:, :, None], -gradients[1]/(nu[:, :, None]*mu[:, None, :]), -gradients[2]/nu)
        row['weighted_autograd'] = max_difference(rhs(z, U, labels, (mu, nu)), oracle)
        if max(row.values()) > 2e-12:
            raise AssertionError(row)
        errors[f'd{d}_m{m}'] = row
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    parser.add_argument('--device', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--budget-seconds', type=float)
    args = parser.parse_args()
    if torch.device(args.device).type != 'cuda' or not torch.cuda.is_available():
        parser.error('scientific execution requires an available explicit CUDA device')
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
    begin = time.perf_counter()
    deadline = begin+config['budget_seconds']
    status = dict(completed=[], failures=[], unstarted_cases=config['cases'])

    def alarm_handler(signum, frame):
        raise TimeoutError('worker wall budget exceeded')

    previous = signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, config['budget_seconds'])
    try:
        write_json(out/'core_validation.json', dict(dynamics=validate_core(args.device), metrics=validate_metrics()))
        for index, case in enumerate(config['cases']):
            check_budget(args.device, config, deadline)
            verify_sources(sources)
            status['unstarted_cases'] = config['cases'][index+1:]
            try:
                record = run_case(case, config, args.device, out, deadline)
                status['completed'].append({key: record[key] for key in
                    ('dataset_id', 'n', 'seed', 'total_seconds', 'last_time', 'setup_failures')})
            except (TimeoutError, MemoryError):
                raise
            except Exception as exc:
                status['failures'].append(dict(**case, error=repr(exc)))
                torch.cuda.empty_cache()
            verify_sources(sources)
            write_json(out/'status.json', status)
    except BaseException as exc:
        status['worker_error'] = repr(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, previous)
        status['wall_seconds'] = time.perf_counter()-begin
        status['peak_gpu_allocated'] = torch.cuda.max_memory_allocated(args.device)
        write_json(out/'status.json', status)


if __name__ == '__main__':
    main()
