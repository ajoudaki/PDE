"""Bounded joint evolution of a shared aggregate core and passive queries.

Compile one symbolic passive-query template. Its query-free contractions and
clock evolve once, while each circle angle has only its passive contractions.
The initial finite pool is used for contractions then discarded; no sampled
population, trajectory replay, or Fourier interpolation is used at runtime.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import copy
import json
from pathlib import Path
import pickle
import signal
import sys
import time

import numpy as np
from scipy.optimize import brentq

from circle_tasks import BY_NAME, directions
from dense_wide_integrator import _BlockRK45
from true_aggregate_ode import flatten
from true_aggregate_references import digest, initial_block_pool, write_json
from true_aggregate_selective import compile_selective


class BudgetReached(Exception):
    pass


class SharedQueryClosure:
    """One autonomous state: [shared core, passive angle blocks, L]."""

    def __init__(self, template, angles):
        if template.M != template.m+1:
            raise ValueError('A single-passive-color template is required')
        self.template = template
        self.angles = np.asarray(angles)
        self.models = []
        for point in directions(self.angles):
            model = copy.copy(template)
            model.queries = np.vstack((template.u, point))
            self.models.append(model)
        passive_colors = {i for i, name in enumerate(template.colors)
                          if name[0] in ('x', 'h') and name[1] >= template.m}
        is_passive = [any(col in passive_colors for _, decs in flatten(tree)[0]
                          for col in decs) for tree in template.trees]
        self.core_ids = np.flatnonzero(np.logical_not(is_passive))
        self.passive_ids = np.flatnonzero(is_passive)
        self.ncore, self.npassive = len(self.core_ids), len(self.passive_ids)
        self.size = self.ncore+len(self.angles)*self.npassive+1
        core_lookup = {int(j): i for i, j in enumerate(self.core_ids)}
        passive_lookup = {int(j): i for i, j in enumerate(self.passive_ids)}
        self.train_ids = np.array([core_lookup[int(j)] for j in template.Fids[:template.m]])
        self.output_id = passive_lookup[int(template.Fids[-1])]
        self.slices = [slice(0, self.ncore)]
        self.slices += [slice(self.ncore+i*self.npassive, self.ncore+(i+1)*self.npassive)
                        for i in range(len(self.angles))]
        self.slices += [slice(self.size-1, self.size)]

    def unpack(self, state):
        return (state[:self.ncore], state[self.ncore:-1].reshape(len(self.angles), self.npassive),
                float(state[-1]))

    def assemble(self, core, passive, clock):
        state = np.empty(len(self.template.trees)+1)
        state[self.core_ids] = core
        state[self.passive_ids] = passive
        state[-1] = clock
        return state

    def initialize(self, pool):
        started = time.monotonic()
        result = np.empty(self.size)
        core, passive, _ = self.unpack(result)
        metadata = []
        max_core_difference = 0.
        for i, model in enumerate(self.models):
            state, info = model.initialize_from_pool(pool)
            if i == 0:
                core[:] = state[self.core_ids]
            else:
                max_core_difference = max(max_core_difference,
                    float(np.max(np.abs(core-state[self.core_ids]))))
            passive[i] = state[self.passive_ids]
            metadata.append(info)
        result[-1] = 1.
        if max_core_difference > 1e-13:
            raise ValueError('Initial shared core depends on passive query')
        return result, {'seconds': time.monotonic()-started,
            'max_query_core_initialization_difference': max_core_difference,
            'first_query_metadata': metadata[0],
            'runtime_initial_pool_retained': False}

    def rhs_loop(self, at, state):
        core, passive, clock = self.unpack(state)
        output = np.empty_like(state)
        dcore, dpassive, _ = self.unpack(output)
        full = self.assemble(core, passive[0], clock)
        for i, model in enumerate(self.models):
            full[self.passive_ids] = passive[i]
            velocity = model.rhs(at, full)
            if i == 0:
                dcore[:] = velocity[self.core_ids]
                output[-1] = velocity[-1]
            dpassive[i] = velocity[self.passive_ids]
        return output

    def rhs(self, at, state):
        """Vectorize template evaluations; no query enters another's fields."""
        model = self.template
        core, passive, clock = self.unpack(state)
        count, size = len(self.angles), len(model.trees)
        raw = np.empty((count, size))
        raw[:, self.core_ids] = core
        raw[:, self.passive_ids] = passive
        q = np.clip(raw, -1., 1.)
        fields = np.ones((count, len(model.field_names)))
        residual = 2*q[:, model.Fids[:model.m]]-model.labels/clock
        fields[:, model.R] = residual
        fields[:, model.sig] = np.sqrt(np.mean(residual*residual, axis=1))
        for (a, b), fid in model.C.items():
            fields[:, fid] = directions(self.angles)@model.u[b]
        for key, index in model.sids.items():
            fields[:, model.s[key]] = q[:, index]
        for key, (a, b) in model.tids.items():
            fields[:, model.t[key]] = q[:, a]-q[:, b]
        def coefficient(key):
            power, indices = key
            return clock**power*np.prod(fields[:, indices], axis=1)
        for key, terms in model.Dpacked.items():
            fields[:, model.D[key]] = sum(c*coefficient(ck)*q[:, index]
                                         for c, ck, index in terms)
        coefficients = np.column_stack([coefficient(key) for key in model.coeff_keys])
        weights = model.values*coefficients[:, model.coeff_index]
        offsets = size*np.arange(count)[:, None]
        indices = (model.row_index+offsets).ravel()
        result = np.bincount(indices, weights=(weights*q[:, model.child_index]).ravel(),
                             minlength=count*size).reshape(count, size)
        envelope = np.bincount(indices, weights=np.abs(weights).ravel(),
                               minlength=count*size).reshape(count, size)
        if model.boundary == 'current_gate_product':
            padded = np.column_stack((q, np.ones(count)))
            reconstructed = np.clip(np.prod(padded[:, model.recipe_indices], axis=2), -1., 1.)
            boundary_weights = model.boundary_values*coefficients[:, model.boundary_coeff_index]
            indices = (model.boundary_row_index+offsets).ravel()
            result += np.bincount(indices,
                weights=(boundary_weights*reconstructed[:, model.boundary_recipe_index]).ravel(),
                minlength=count*size).reshape(count, size)
            envelope += np.bincount(indices, weights=np.abs(boundary_weights).ravel(),
                                    minlength=count*size).reshape(count, size)
        result -= envelope*(raw-q)
        output = np.empty_like(state)
        dcore, dpassive, _ = self.unpack(output)
        dcore[:] = result[0, self.core_ids]
        dpassive[:] = result[:, self.passive_ids]
        output[-1] = fields[0, model.sig]*clock
        return output

    def prediction(self, state):
        return 2*float(state[-1])*np.clip(state[self.train_ids], -1., 1.)

    def circle_prediction(self, state):
        _, passive, clock = self.unpack(state)
        return 2*clock*np.clip(passive[:, self.output_id], -1., 1.)

    def check_independence(self):
        """A nonzero synthetic state tests structural passive independence."""
        rng = np.random.default_rng(97531)
        core = rng.uniform(-.15, .15, self.ncore)
        clock = 1.3
        first = None
        maximum = 0.
        for model in self.models:
            passive = rng.uniform(-.3, .3, self.npassive)
            velocity = model.rhs(0., self.assemble(core, passive, clock))
            current = np.r_[velocity[self.core_ids], velocity[-1]]
            if first is None:
                first = current
            maximum = max(maximum, float(np.max(np.abs(current-first))))
        if maximum > 1e-12:
            raise ValueError(f'Passive query affects core derivative: {maximum}')
        return {'random_nonzero_state_core_rhs_difference': maximum,
                'angles_checked': len(self.models)}

    def check_vectorization(self):
        rng = np.random.default_rng(13579)
        state = rng.uniform(-.02, .02, self.size)
        state[-1] = 1.2
        expected, actual = self.rhs_loop(0., state), self.rhs(0., state)
        error = float(np.max(np.abs(expected-actual)))
        relative = error/max(1., float(np.max(np.abs(expected))))
        if relative > 1e-12:
            raise ValueError(f'Vectorized RHS mismatch: {error}')
        return {'nonzero_state_max_absolute_error': error, 'scaled_error': relative}


def integrate(model, initial, labels, seconds, target=.01):
    state = initial.copy()
    mse_at = lambda value: float(np.mean((model.prediction(value)-labels)**2))
    mse = mse_at(state)
    history = [[0., mse, float(state[-1]), float(np.max(np.abs(state[:-1]))),
                float(np.mean(np.abs(state[:-1]) > 1.))]]
    time_value, steps, nfev = 0., 0, 0
    reason, bracket, max_rise = 'time_cap', None, 0.
    started, last_log = time.monotonic(), time.monotonic()
    solver = None

    def rhs(at, current):
        nonlocal nfev
        nfev += 1
        if time.monotonic()-started >= seconds-.25:
            raise BudgetReached()
        return model.rhs(at, current)

    def alarm(signum, frame):
        raise BudgetReached()

    old_handler = signal.signal(signal.SIGALRM, alarm)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        if mse <= target:
            reason = 'target'
        else:
            solver = _BlockRK45(rhs, 0., state, 3000., rtol=1e-5, atol=1e-7,
                first_step=.01, max_step=1., block_slices=model.slices)
            while solver.status == 'running':
                old_time, old_mse = time_value, mse
                solver.step()
                if solver.status == 'failed':
                    reason = 'solver_failed'
                    break
                candidate = solver.y
                trial_mse = mse_at(candidate)
                if not np.all(np.isfinite(candidate)) or not np.isfinite(trial_mse):
                    reason = 'nonfinite'
                    break
                if np.max(np.abs(candidate[:-1])) > 2.0001:
                    reason = 'moment_box_violation'
                    break
                if trial_mse <= target:
                    interpolant = solver.dense_output()
                    bracket = [old_time, float(solver.t)]
                    root = brentq(lambda at: mse_at(interpolant(at))-target,
                                  *bracket, xtol=1e-12)
                    root = min(float(solver.t), root+1e-11*max(1., root))
                    candidate = interpolant(root)
                    trial_mse = mse_at(candidate)
                    if trial_mse > target*(1+1e-7):
                        reason = 'event_refinement_failed'
                        break
                    time_value, reason = float(root), 'target'
                else:
                    time_value = float(solver.t)
                state, mse = candidate, trial_mse
                steps += 1
                max_rise = max(max_rise, mse-old_mse)
                history.append([time_value, mse, float(state[-1]),
                    float(np.max(np.abs(state[:-1]))), float(np.mean(np.abs(state[:-1]) > 1.))])
                if time.monotonic()-last_log >= 10:
                    print(json.dumps({'phase': 'training', 'seconds': time.monotonic()-started,
                        'physical_time': time_value, 'train_mse': mse, 'nfev': nfev,
                        'steps': steps}), flush=True)
                    last_log = time.monotonic()
                if reason == 'target':
                    break
    except BudgetReached:
        reason = 'training_wall_limit'
    except (FloatingPointError, OverflowError) as exc:
        reason = type(exc).__name__
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.)
        signal.signal(signal.SIGALRM, old_handler)
    history = np.asarray(history)
    return state, history, {'stop_reason': reason, 'physical_time': time_value,
        'train_mse': mse, 'fitted': reason == 'target' and mse <= target*(1+1e-7),
        'training_seconds': time.monotonic()-started, 'nsteps': steps, 'nfev': nfev,
        'max_loss_rise': max_rise, 'target_bracket': bracket,
        'max_abs_q_accepted': float(np.max(history[:, 3])),
        'max_clipped_fraction_accepted': float(np.max(history[:, 4]))}


def compare_reference(path, angles, prediction, fitted):
    if not path.exists():
        return None
    metadata = json.loads(path.with_suffix('.json').read_text())
    with np.load(path, allow_pickle=False) as reference:
        stride = len(reference['angles'])//len(angles)
        if stride < 1 or not np.allclose(reference['angles'][::stride], angles,
                                        rtol=0., atol=1e-14):
            raise ValueError('Reference angle grid mismatch')
        reference_prediction = reference['prediction'][::stride]
    difference = prediction-reference_prediction
    rms = float(np.sqrt(np.mean(difference**2)))
    coarse = float(np.sqrt(np.mean(difference[::2]**2)))
    return {'raw_circle_rms': rms, 'circle_grid_change_64_vs_32': abs(rms-coarse),
        'fitted_pair': fitted and metadata['fitted'], 'reference_train_mse': metadata['train_mse'],
        'reference_physical_time': metadata['physical_time'], 'data_sha256': digest(path)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--references', required=True, type=Path)
    parser.add_argument('--task', choices=('pair_cos1', 'triple_mixed', 'cluster_triple_cos9'), required=True)
    parser.add_argument('--boundary', choices=('zero', 'current_gate_product'), required=True)
    parser.add_argument('--depth', type=int, default=0)
    parser.add_argument('--output-depth', type=int, choices=(1, 2), default=1)
    parser.add_argument('--fit-seconds', type=float, default=45.)
    parser.add_argument('--compile-seconds', type=float, default=60.)
    parser.add_argument('--compile-only', action='store_true')
    args = parser.parse_args()
    if not (0 < args.fit_seconds <= 45 and 0 < args.compile_seconds <= 60 and args.depth >= 0):
        parser.error('Invalid budget or dependency depth')
    args.output.mkdir(parents=True, exist_ok=True)
    tag = f'{args.task}__{args.boundary}__depth{args.depth}'
    if args.output_depth != 1:
        tag += f'__out{args.output_depth}'
    report_path = args.output/f'{tag}.json'
    if report_path.exists():
        raise FileExistsError('No reruns: report already exists')
    used_seconds = sum(json.loads(p.read_text()).get('training_seconds', 0.)
                       for p in args.output.glob('*__depth*.json'))
    if used_seconds+args.fit_seconds > 300.:
        raise BudgetReached('The additional five-minute training budget would be exceeded')
    started = time.monotonic()
    task = BY_NAME[args.task]
    u, labels = task.data()
    angles = 2*np.pi*np.arange(64)/64
    source = Path(__file__).resolve().parent
    report = {'task': args.task, 'boundary': args.boundary, 'dependency_depth': args.depth,
        'output_dependency_depth': args.output_depth,
        'initial_width': 1024, 'seed': 1, 'k': 4, 'order': 1, 'mark_bound': 3.,
        'target_mse': .01, 'circle_grid': 64, 'command': sys.argv,
        'sources': {name: digest(source/name) for name in ('run_true_aggregate_selective.py',
            'true_aggregate_selective.py', 'true_aggregate_ode.py', 'true_aggregate_references.py',
            'block_scalar_closure.py', 'circle_tasks.py', 'dense_wide_integrator.py')},
        'primary_metric': 'raw circle RMS vs canonical Gaussian; no amplitude normalization',
        'runtime_state': 'shared scalar contractions, passive scalar contractions, one clock',
        'solver': {'rtol': 1e-5, 'atol': 1e-7, 'first_step': .01, 'max_step': 1.,
            'physical_time_cap': 3000., 'training_wall_cap': args.fit_seconds,
            'error_norm': 'maximum scaled RMS over core, each passive block, and clock'},
        'prior_added_training_seconds': used_seconds}
    template = compile_selective(u, labels, k=4, order=1,
        queries=np.vstack((u, directions([.123])[0])), mark_bound=3.,
        dependency_depth=args.depth, augment_outputs=True, boundary=args.boundary,
        preserve_essential=True, output_depth=args.output_depth,
        seconds=args.compile_seconds, max_states=100000, max_terms=1000000)
    report['compile'] = template.report
    if not template.compiled:
        report.update(stop_reason='compile_limit', fitted=False, training_seconds=0.)
        write_json(report_path, report)
        print(json.dumps(report), flush=True)
        return
    model = SharedQueryClosure(template, angles)
    report['state_counts'] = {'shared_core': model.ncore, 'passive_per_angle': model.npassive,
        'angles': len(angles), 'total_dynamic_scalars': model.size,
        'single_query_template': len(template.trees)+1}
    report['passive_independence'] = model.check_independence()
    report['vectorization_check'] = model.check_vectorization()
    template_path = args.output/f'{tag}__compiled.pkl'
    with template_path.open('wb') as handle:
        pickle.dump(template, handle, protocol=pickle.HIGHEST_PROTOCOL)
    report['compiled_template_file'] = template_path.name
    report['compiled_template_sha256'] = digest(template_path)
    print(json.dumps({'phase': 'compiled', **report['state_counts'],
                      'compile': template.report}), flush=True)
    if args.compile_only:
        write_json(args.output/f'{tag}__counts.json', report)
        return
    pool = initial_block_pool(1024, 4, 1, 3.)
    initial, report['initialization'] = model.initialize(pool)
    report['initial_pool_entry_redraws'] = pool['entry_redraws']
    del pool
    benchmark = time.monotonic()
    velocity = model.rhs(0., initial)
    report['initial_rhs_seconds'] = time.monotonic()-benchmark
    if not np.all(np.isfinite(velocity)):
        raise ValueError('Initial RHS is not finite')
    report['initial_train_mse'] = float(np.mean((model.prediction(initial)-labels)**2))
    print(json.dumps({'phase': 'initialized', 'initial_mse': report['initial_train_mse'],
                      'rhs_seconds': report['initial_rhs_seconds']}), flush=True)
    if report['initial_rhs_seconds'] > 1.:
        report.update(stop_reason='rhs_cost_gate', fitted=False, training_seconds=0.,
                      total_seconds=time.monotonic()-started)
        write_json(report_path, report)
        print(json.dumps(report), flush=True)
        return
    state, history, info = integrate(model, initial, labels, args.fit_seconds)
    report.update(info)
    prediction = model.circle_prediction(state)
    train_prediction = model.prediction(state)
    report['train_mse'] = float(np.mean((train_prediction-labels)**2))
    report['gaussian_comparison'] = compare_reference(args.references/f'{args.task}__gaussian.npz',
                                                       angles, prediction, report['fitted'])
    report['block_comparison'] = compare_reference(args.references/f'{args.task}__block_k4_P1_canonical.npz',
                                                    angles, prediction, report['fitted'])
    report['train_prediction'] = train_prediction.tolist()
    report['endpoint_status'] = 'fitted threshold endpoint' if report['fitted'] else 'partial endpoint'
    report['history_columns'] = ['physical_time', 'train_mse', 'L', 'max_abs_q', 'fraction_outside_unit_box']
    path = args.output/f'{tag}.npz'
    np.savez_compressed(path, state=state, initial_state=initial, history=history,
        angles=angles, prediction=prediction, train_prediction=train_prediction,
        train_angles=task.angles, train_labels=labels, core_ids=model.core_ids,
        passive_ids=model.passive_ids, template_Fids=template.Fids)
    report.update(data_file=path.name, data_sha256=digest(path), total_seconds=time.monotonic()-started)
    write_json(report_path, report)
    print(json.dumps(report, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
