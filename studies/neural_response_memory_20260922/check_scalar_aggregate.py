"""Independent deterministic checks for the scalar observable hierarchy.

The Torch reference below is written directly from the network definition;
it does not call the candidate's differentiation or dense-flow routines.
Research trajectories are outside this program's algebra-check mode.
"""

import argparse
import hashlib
import importlib
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np
import torch


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def flatten(parts):
    return np.concatenate([np.asarray(part).ravel() for part in parts])


def shifted(parts, direction, amount):
    return tuple(part + amount * change for part, change in zip(parts, direction))


class IndependentNetwork:
    def __init__(self, params, inputs):
        self.shapes = [part.shape for part in params]
        self.sizes = [part.size for part in params]
        self.n = params[0].shape[0]
        self.inputs = torch.tensor(inputs, dtype=torch.float64)
        self.point = torch.tensor(flatten(params), dtype=torch.float64,
                                  requires_grad=True)
        scales = [self.n] + [1] * (len(params) - 2) + [self.n]
        self.mobility = torch.cat([torch.full((size,), float(scale),
                                             dtype=torch.float64)
                                   for size, scale in zip(self.sizes, scales)])

    def parts(self, point):
        return tuple(value.reshape(shape) for value, shape in
                     zip(point.split(self.sizes), self.shapes))

    def evaluate(self, point):
        params = self.parts(point)
        value = self.inputs.T
        activations = []
        for matrix in params[:-1]:
            value = torch.tanh(matrix @ value)
            activations.append(value)
        return params[-1] @ value / self.n, activations

    def scalars(self):
        point = self.point
        outputs, activations = self.evaluate(point)
        count = len(outputs)
        gradients = [torch.autograd.grad(output, point, create_graph=True,
                                         retain_graph=True)[0]
                     for output in outputs]
        directions = [self.mobility * gradient for gradient in gradients]
        kernel = [[torch.dot(gradients[a], directions[b])
                   for b in range(count)] for a in range(count)]
        kernel_gradients = [[torch.autograd.grad(kernel[a][b], point,
                              create_graph=True, retain_graph=True)[0]
                             for b in range(count)] for a in range(count)]
        cubic = [[[torch.dot(kernel_gradients[a][b], directions[c])
                   for c in range(count)] for b in range(count)]
                 for a in range(count)]
        quartic = np.empty((count,) * 4)
        frozen_direction_quartic = np.empty_like(quartic)
        for a in range(count):
            for b in range(count):
                for c in range(count):
                    derivative = torch.autograd.grad(cubic[a][b][c], point,
                                       retain_graph=True)[0]
                    fixed = torch.dot(kernel_gradients[a][b],
                                      directions[c].detach())
                    fixed_derivative = torch.autograd.grad(fixed, point,
                                             retain_graph=True)[0]
                    for d in range(count):
                        quartic[a, b, c, d] = float(torch.dot(
                            derivative, directions[d]).detach())
                        frozen_direction_quartic[a, b, c, d] = float(torch.dot(
                            fixed_derivative, directions[d]).detach())
        as_array = lambda values: torch.stack(values).detach().numpy()
        kernel_array = as_array([torch.stack(row) for row in kernel])
        cubic_array = as_array([torch.stack([torch.stack(row) for row in slab])
                               for slab in cubic])
        return dict(f=outputs.detach().numpy(),
                    h=[value.detach().numpy() for value in activations],
                    g=as_array(directions), Theta=kernel_array, C=cubic_array,
                    Q=quartic, Q_frozen_last_direction=frozen_direction_quartic)

    def derivative_of_direction(self, sample, direction):
        hessian = torch.autograd.functional.hessian(
            lambda point: self.evaluate(point)[0][sample], self.point)
        vector = torch.tensor(flatten(direction), dtype=torch.float64)
        return (self.mobility * (hessian @ vector)).detach().numpy()


class Checks:
    def __init__(self):
        self.rows = []

    def close(self, name, actual, expected, atol=2e-10, rtol=2e-8):
        actual, expected = np.asarray(actual), np.asarray(expected)
        error = float(np.max(np.abs(actual - expected))) if actual.size else 0.
        ok = actual.shape == expected.shape and np.allclose(
            actual, expected, atol=atol, rtol=rtol)
        self.rows.append(dict(name=name, passed=bool(ok), max_abs_error=error,
                              atol=atol, rtol=rtol))
        if not ok:
            raise AssertionError(name + ': maximum error ' + str(error))

    def require(self, name, condition, **detail):
        self.rows.append(dict(name=name, passed=bool(condition), **detail))
        if not condition:
            raise AssertionError(name)


def check_one_depth(module, depth, checks):
    width, count, seed = 3, 3, 92761
    angles = np.asarray([.2, 1.1, 2.4])
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    labels = np.asarray([1., -.5, .7])
    params = tuple(module.initialize_network(width, 2, depth=depth, seed=seed))
    rng = np.random.default_rng(seed)
    wanted = [rng.standard_normal((width, 2))]
    wanted += [rng.standard_normal((width, width)) / np.sqrt(width)
               for _ in range(depth - 1)]
    wanted += [rng.standard_normal(width) / width]
    checks.close(f'depth{depth}_initialization', flatten(params), flatten(wanted),
                 atol=0., rtol=0.)
    # A non-small readout makes moving-direction and ordered-index mistakes
    # observable without relying on a cancellation at initialization.
    params = params[:-1] + (params[-1] + np.asarray([.31, -.27, .43]),)
    reference = IndependentNetwork(params, inputs)
    expected = reference.scalars()
    actual = module.initialize_coefficients(params, inputs, order=4)
    for name in ('f', 'Theta', 'C', 'Q'):
        checks.close(f'depth{depth}_{name}_independent_autograd', actual[name],
                     expected[name])
    fields = module.network_fields(params, inputs)
    checks.close(f'depth{depth}_field_outputs', fields['f'], expected['f'])
    checks.close(f'depth{depth}_field_kernel', fields['Theta'], expected['Theta'])
    for layer, (actual_h, expected_h) in enumerate(zip(fields['h'], expected['h'])):
        checks.close(f'depth{depth}_activation_{layer+1}', actual_h, expected_h)
    directions = [tuple(module.sample_direction(params, inputs, sample))
                  for sample in range(count)]
    for sample, direction in enumerate(directions):
        checks.close(f'depth{depth}_direction_{sample}', flatten(direction),
                     expected['g'][sample])
        derivative = module.direction_derivative(params, inputs, sample,
                                                 directions[(sample+1) % count])
        checks.close(f'depth{depth}_moving_direction_{sample}', flatten(derivative),
                     reference.derivative_of_direction(
                         sample, directions[(sample+1) % count]))
    residual = expected['f'] - labels
    velocity = (-2/count) * np.einsum('a,ap->p', residual, expected['g'])
    checks.close(f'depth{depth}_dense_rhs_independent_autograd',
                 flatten(module.network_rhs(params, inputs, labels)), velocity)
    forward_derivative = np.stack([
        torch.autograd.grad(reference.evaluate(reference.point)[0][a],
                            reference.point)[0].detach().numpy()
        for a in range(count)]) @ velocity
    checks.close(f'depth{depth}_kernel_physical_time_normalization',
                 forward_derivative, (-2/count) * expected['Theta'] @ residual)
    ordered_gap = float(np.max(np.abs(expected['C'] - expected['C'].swapaxes(1, 2))))
    moving_gap = float(np.max(np.abs(expected['Q'] -
                                     expected['Q_frozen_last_direction'])))
    checks.require(f'depth{depth}_noncommuting_example', ordered_gap > 1e-7,
                   ordered_index_gap=ordered_gap)
    quartic_ordered_gap = float(np.max(np.abs(expected['Q'] -
                                             expected['Q'].swapaxes(2, 3))))
    checks.require(f'depth{depth}_Q_ordered_derivatives',
                   quartic_ordered_gap > 1e-7,
                   ordered_index_gap=quartic_ordered_gap)
    checks.require(f'depth{depth}_last_direction_derivative_required',
                   moving_gap > 1e-7, omitted_term_gap=moving_gap)
    epsilon = 2e-5
    for sample in (0, count-1):
        plus = module.initialize_coefficients(shifted(params, directions[sample], epsilon),
                                              inputs, order=3)
        minus = module.initialize_coefficients(shifted(params, directions[sample], -epsilon),
                                               inputs, order=3)
        checks.close(f'depth{depth}_C_directional_difference_{sample}',
                     (plus['Theta']-minus['Theta'])/(2*epsilon),
                     expected['C'][..., sample], atol=2e-8, rtol=3e-6)
        checks.close(f'depth{depth}_Q_directional_difference_{sample}',
                     (plus['C']-minus['C'])/(2*epsilon),
                     expected['Q'][..., sample], atol=2e-8, rtol=3e-6)
    return actual, labels


def check_scalar_rhs(module, coefficients, labels, checks):
    from scipy.integrate import solve_ivp

    names = ('f', 'Theta', 'C', 'Q')
    count = len(labels)
    for order in (2, 3, 4):
        system = module.ScalarHierarchy(coefficients, labels, order)
        state = system.initial_state()
        unpacked = system.unpack(state)
        derivative = system.unpack(system.rhs(123.5, state))
        residual = unpacked['f'] - labels
        for level in range(order-1):
            expected = (-2/count) * np.tensordot(
                coefficients[names[level+1]], residual, axes=([-1], [0]))
            checks.close(f'order{order}_rhs_{names[level]}',
                         derivative[names[level]], expected)
        checks.close(f'order{order}_pack_roundtrip', system.pack(unpacked), state,
                     atol=0., rtol=0.)
        checks.close(f'order{order}_autonomy', system.rhs(0., state),
                     system.rhs(99., state), atol=0., rtol=0.)
        zero = dict(coefficients, f=np.asarray(labels).copy())
        absorbed = module.ScalarHierarchy(zero, labels, order)
        checks.close(f'order{order}_zero_residual',
                     absorbed.rhs(0., absorbed.initial_state()),
                     np.zeros_like(absorbed.initial_state()), atol=0., rtol=0.)
        expected_moving = sum(count**degree for degree in range(1, order))
        checks.require(f'order{order}_moving_scalar_count',
                       state.size == expected_moving, actual=int(state.size),
                       expected=expected_moving)
        checks.require(f'order{order}_terminal_count',
                       system.terminal.size == count**order,
                       actual=int(system.terminal.size), expected=count**order)
        terminal_before = system.terminal.copy()
        whole = solve_ivp(system.rhs, (0., .1), state, method='DOP853',
                          rtol=1e-11, atol=1e-13, max_step=.02)
        first = solve_ivp(system.rhs, (0., .04), state, method='DOP853',
                          rtol=1e-11, atol=1e-13, max_step=.02)
        resumed = solve_ivp(system.rhs, (.04, .1), first.y[:, -1], method='DOP853',
                            rtol=1e-11, atol=1e-13, max_step=.02)
        checks.require(f'order{order}_tiny_integration_success',
                       whole.success and first.success and resumed.success)
        checks.close(f'order{order}_own_state_restart', resumed.y[:, -1],
                     whole.y[:, -1], atol=2e-10, rtol=2e-9)
        checks.close(f'order{order}_terminal_immutable', system.terminal,
                     terminal_before, atol=0., rtol=0.)
        checks.require(f'order{order}_terminal_read_only',
                       not system.terminal.flags.writeable)


def run_checks(out):
    started = time.monotonic()
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    module = importlib.import_module('scalar_aggregate_engine')
    checks = Checks()
    receipt = dict(status='running', python=sys.version, executable=sys.executable,
                   platform=platform.platform(), numpy=np.__version__,
                   torch=torch.__version__, cuda_available=torch.cuda.is_available(),
                   source_sha256={name:digest(Path(__file__).with_name(name))
                                  for name in ('check_scalar_aggregate.py',
                                               'scalar_aggregate_engine.py',
                                               'SCALAR_AGGREGATE_PROTOCOL.md')})
    try:
        for depth in (2, 3):
            coefficients, labels = check_one_depth(module, depth, checks)
            if depth == 3:
                check_scalar_rhs(module, coefficients, labels, checks)
        receipt['status'] = 'pass'
    except Exception as exc:
        receipt.update(status='fail', exception=type(exc).__name__, error=str(exc))
        raise
    finally:
        receipt.update(checks=checks.rows, wall_seconds=time.monotonic()-started)
        (out/'check.json').write_text(json.dumps(receipt, indent=2)+'\n')
        print(json.dumps(dict(status=receipt['status'], checks=len(checks.rows),
                              wall_seconds=receipt['wall_seconds'], out=str(out))))
    return receipt


def archive(path):
    with np.load(path, allow_pickle=False) as saved:
        return {name:saved[name].copy() for name in saved.files}


def arrays_digest(values):
    result = hashlib.sha256()
    for value in values:
        value = np.ascontiguousarray(value)
        result.update(str(value.shape).encode())
        result.update(value.tobytes())
    return result.hexdigest()


def measured_pair(left, right, horizon=None):
    """Independent scoring: compare only identical sampled observation times."""
    count = min(len(left['times']), len(right['times']))
    if not np.array_equal(left['times'][:count], right['times'][:count]):
        raise AssertionError('different observation times')
    selected = np.arange(count)
    if horizon is not None:
        selected = selected[left['times'][selected] <= horizon]
    if not len(selected):
        raise AssertionError('no common observations')
    delta = left['f'][selected] - right['f'][selected]
    rms = np.linalg.norm(delta, axis=1) / np.sqrt(delta.shape[1])
    return dict(prediction_error=float(rms.max()),
                loss_error=float(np.abs(left['loss'][selected]-right['loss'][selected]).max()),
                last_compared_time=float(left['times'][selected[-1]]),
                observations=len(selected))


def measured_gate(left, right, paired_error):
    comparison = measured_pair(left, right)
    change, loss_change = comparison['prediction_error'], comparison['loss_error']
    return dict(pass_gate=bool(change <= .002 and
                              change <= .1*max(paired_error, 1e-6) and
                              loss_change <= .002),
                prediction_change=change, loss_change=loss_change,
                paired_error=paired_error)


def independent_dense_observation(engine, vector):
    from deep_moment_engine import DeepDenseState

    n, d = engine.n, engine.d
    sizes = (n*d, n*n, n*n, n)
    cuts = np.cumsum((0,)+sizes)
    shapes = ((n,d), (n,n), (n,n), (n,))
    parts = [torch.tensor(vector[a:b].reshape(shape), dtype=torch.float64)
             for a,b,shape in zip(cuts[:-1], cuts[1:], shapes)]
    fields = engine.fields(DeepDenseState(*parts))
    h = [fields['h'+str(layer)].numpy() for layer in (1,2,3)]
    delta = [fields['delta'+str(layer)].numpy() for layer in (1,2,3)]
    inputs = engine.inputs.numpy()
    kernel = (inputs @ inputs.T) * (delta[0].T @ delta[0])/n
    for layer in (1,2):
        kernel += (h[layer-1].T @ h[layer-1]) * (delta[layer].T @ delta[layer])/(n*n)
    kernel += h[-1].T @ h[-1]/n
    initial = engine.fields(engine.initial_state())
    movement = np.asarray([np.sqrt(np.mean((value-initial['h'+str(layer)].numpy())**2))
                           for layer,value in enumerate(h, 1)])
    return dict(f=fields['f'].numpy(), kernel=kernel, motion=movement)


def audit_configuration(folder, sources, cases, checks):
    from deep_moment_engine import DeepDenseEngine

    prefix = folder.name
    meta = json.loads((folder/'configuration.json').read_text())
    summary = json.loads((folder/'summary.json').read_text())
    coefficients = archive(folder/'coefficients.npz')
    data = cases[meta['case']]
    radians = np.asarray(data['angles_degrees']) * np.pi/180
    inputs = np.column_stack((np.cos(radians), np.sin(radians)))
    labels = np.asarray(data['labels'], dtype=float)
    checks.close(prefix+'_inputs', coefficients['inputs'], inputs, atol=2e-15, rtol=0.)
    checks.close(prefix+'_labels', coefficients['labels'], labels, atol=0., rtol=0.)
    checks.require(prefix+'_source_hashes',
                   all(digest(sources/name) == value
                       for name,value in meta['source_hashes'].items()))
    checks.require(prefix+'_coefficient_hash', arrays_digest(
        [coefficients[name] for name in ('f','Theta','C','Q')]) == meta['coefficients_hash'])
    engine = DeepDenseEngine(2, meta['width'], inputs, labels, seed=meta['seed'])
    initial = engine.initial_state()
    initial_parts = [part.numpy() for part in initial.tensors()]
    checks.require(prefix+'_network_initialization_hash',
                   arrays_digest(initial_parts) == meta['initialization_hash'])
    initial_observation = independent_dense_observation(engine, flatten(initial_parts))
    checks.close(prefix+'_initial_coefficients_f', coefficients['f'], initial_observation['f'])
    checks.close(prefix+'_initial_coefficients_kernel', coefficients['Theta'],
                 initial_observation['kernel'])
    records, trajectories, files = {}, {}, {}
    observations, checkpoints = 0, 0
    for trajectory_path in sorted(folder.glob('*_resolution*/trajectory.npz')):
        identifier = trajectory_path.parent.name
        model, raw_level = identifier.rsplit('_resolution', 1)
        key = model, int(raw_level)
        record = json.loads((trajectory_path.parent/'result.json').read_text())
        trajectory = archive(trajectory_path)
        records[key], trajectories[key] = record, trajectory
        files[str(trajectory_path.relative_to(folder))] = digest(trajectory_path)
        stem = prefix+'_'+identifier
        count, sample_count = trajectory['f'].shape
        observations += count
        checks.require(stem+'_dimensions', sample_count == len(labels) and
                       len(trajectory['times']) == count == record['observations'])
        checks.require(stem+'_ordered_finite_times',
                       np.isfinite(trajectory['times']).all() and
                       np.all(np.diff(trajectory['times']) > 0))
        checks.close(stem+'_loss', trajectory['loss'],
                     ((trajectory['f']-labels)**2).mean(axis=1), atol=2e-11, rtol=2e-11)
        checks.close(stem+'_kernel_eigenvalue', trajectory['eigenmin'],
                     np.linalg.eigvalsh((trajectory['kernel']+
                                        trajectory['kernel'].swapaxes(1,2))/2)[:,0],
                     atol=2e-10, rtol=2e-9)
        checks.require(stem+'_tolerances', record['rtol'] == (1e-7,1e-9,1e-11)[key[1]] and
                       record['atol'] == record['rtol']/100 and record['max_step'] == 2.)
        if record['status'] == 'complete':
            checks.close(stem+'_complete_horizon',
                         [record['final_time'],trajectory['times'][-1]],
                         [meta['end'],meta['end']], atol=1e-12, rtol=0.)
        if model != 'dense':
            order = int(model[-1])
            m = len(labels)
            moving = sum(m**degree for degree in range(1,order))
            checks.require(stem+'_moving_dimensions', trajectory['states'].shape == (count,moving))
            checks.close(stem+'_state_outputs', trajectory['states'][:,:m], trajectory['f'],
                         atol=0., rtol=0.)
            expected_kernel = (np.broadcast_to(coefficients['Theta'],(count,m,m)) if order == 2
                               else trajectory['states'][:,m:m+m*m].reshape(count,m,m))
            checks.close(stem+'_state_kernel', trajectory['kernel'], expected_kernel,
                         atol=0., rtol=0.)
            initial_state = np.concatenate([coefficients[name].ravel()
                            for name in ('f','Theta','C')[:order-1]])
            checks.close(stem+'_initial_state', trajectory['states'][0], initial_state,
                         atol=0., rtol=0.)
            storage = record['storage']
            checks.require(stem+'_storage', storage['state_scalars'] == moving and
                           storage['terminal_scalars'] == m**order and
                           storage['aggregate_scalars'] == moving+m**order and
                           storage['neuron_scalars'] == storage['network_parameter_scalars'] == 0)
        for name, value in trajectory.items():
            if not name.startswith('checkpoint_'):
                continue
            at = float(name[len('checkpoint_'):].replace('_','.'))
            matches = np.flatnonzero(trajectory['times'] == at)
            checks.require(stem+'_'+name+'_observed', len(matches) == 1)
            index = int(matches[0]); checkpoints += 1
            if model == 'dense':
                observed = independent_dense_observation(engine, value)
                for quantity in ('f','kernel','motion'):
                    checks.close(stem+'_'+name+'_'+quantity, trajectory[quantity][index],
                                 observed[quantity], atol=2e-10, rtol=2e-9)
            else:
                checks.close(stem+'_'+name+'_state', value, trajectory['states'][index],
                             atol=0., rtol=0.)
        if record['status'] == 'complete':
            if model == 'dense':
                observed = independent_dense_observation(engine, trajectory['final_state'])
                checks.close(stem+'_final_state_f', trajectory['f'][-1], observed['f'])
            else:
                checks.close(stem+'_final_state', trajectory['states'][-1],
                             trajectory['final_state'], atol=2e-10, rtol=2e-9)
    latest = {model:max(level for name,level in trajectories if name == model)
              for model in ('dense','order2','order3','order4')}
    checks.require(prefix+'_latest_resolution', latest == summary['latest_resolution'])
    dense = trajectories['dense',latest['dense']]
    checks.close(prefix+'_dense_motion_max', summary['dense_motion_max'],
                 dense['motion'].max(axis=0))
    outcome = {}
    for model in ('order2','order3','order4'):
        level = latest[model]
        scalar = trajectories[model,level]
        comparison = measured_pair(scalar,dense)
        produced = summary['orders'][model]
        stem = prefix+'_'+model
        for metric in ('prediction_error','loss_error'):
            checks.close(stem+'_'+metric, produced[metric], comparison[metric],
                         atol=1e-12,rtol=1e-12)
        scalar_gate = measured_gate(trajectories[model,level-1],scalar,comparison['prediction_error'])
        dense_gate = measured_gate(trajectories['dense',latest['dense']-1],dense,
                                   comparison['prediction_error'])
        for kind,expected in (('scalar_gate',scalar_gate),('dense_gate',dense_gate)):
            checks.require(stem+'_'+kind+'_decision', produced[kind]['pass_gate'] == expected['pass_gate'])
            for metric in ('prediction_change','loss_change','paired_error'):
                checks.close(stem+'_'+kind+'_'+metric, produced[kind][metric],expected[metric],
                             atol=1e-12,rtol=1e-12)
        complete = all(records[name,latest[name]]['status'] == 'complete'
                       for name in ('dense',model))
        valid = scalar_gate['pass_gate'] and dense_gate['pass_gate']
        failure_statuses = {'state_escape','nonfinite','solver_failure'}
        repeated_failure = not complete and all(records[model,k]['status'] in failure_statuses
                                                for k in (0,1))
        expected_verdict = 'adverse' if repeated_failure else 'inconclusive'
        if complete and valid:
            if comparison['prediction_error'] <= .1 and comparison['loss_error'] <= .05:
                expected_verdict = 'practical_agreement'
            elif comparison['prediction_error'] > .2 or comparison['loss_error'] > .1:
                expected_verdict = 'adverse'
        checks.require(stem+'_verdict', produced['verdict'] == expected_verdict and
                       produced['full_horizon_complete'] == complete and
                       produced['validity_pass'] == valid)
        for raw_horizon, prefix_metrics in produced['prefixes'].items():
            horizon = float(raw_horizon)
            values = measured_pair(scalar,dense,horizon)
            for metric in ('prediction_error','loss_error','last_compared_time'):
                checks.close(stem+'_prefix'+raw_horizon+'_'+metric,
                             prefix_metrics[metric],values[metric],atol=1e-12,rtol=1e-12)
            covered = scalar['times'][-1] >= horizon and dense['times'][-1] >= horizon
            checks.require(stem+'_prefix'+raw_horizon+'_coverage',
                           prefix_metrics['prefix_complete'] == covered)
        checks.close(stem+'_min_eigenvalue', produced['min_kernel_eigenvalue'],
                     scalar['eigenmin'].min(),atol=1e-12,rtol=1e-12)
        movement = float(dense['motion'].max())
        checks.require(stem+'_nonlinear_gate', produced['nonlinear_gate'] == (movement >= .1))
        outcome[model] = dict(**comparison, verdict=expected_verdict, complete=complete,
                             valid=valid, dense_motion=movement,
                             scalar_status=records[model,level]['status'])
    o4,o2 = outcome['order4'],outcome['order2']
    improvement = bool(o4['complete'] and o4['valid'] and
                       o4['prediction_error'] <= o2['prediction_error']/2 and
                       o2['prediction_error'] >= .05 and o4['dense_motion'] >= .1)
    checks.require(prefix+'_nonlinear_improvement',
                   summary['orders']['order4']['nonlinear_improvement'] == improvement)
    return dict(configuration=prefix, trajectories=len(trajectories),
                observations=observations, checkpoints=checkpoints,
                trajectory_sha256=files, orders=outcome,
                nonlinear_improvement=improvement)


def audit_reproduction(run_root, reproduction_root, outcomes, checks):
    reproduction_root = Path(reproduction_root)
    original_root = run_root/'equal_mixed_odd_n128_seed20260920'
    producer = json.loads((reproduction_root/'check.json').read_text())
    original_coefficients = archive(original_root/'coefficients.npz')
    repeated_coefficients = archive(reproduction_root/'recomputed_coefficients.npz')
    original = archive(original_root/'order4_resolution1'/'trajectory.npz')
    repeated = archive(reproduction_root/'repeat.npz')
    resumed = archive(reproduction_root/'restart.npz')
    for name,value in repeated_coefficients.items():
        checks.close('reproduction_coefficient_'+name,value,original_coefficients[name],
                     atol=0.,rtol=0.)
    checks.require('reproduction_archive_keys', set(original) == set(repeated))
    for name,value in repeated.items():
        checks.require('reproduction_bitwise_'+name,
                       np.array_equal(value,original[name],equal_nan=True))
    mask = original['times'] >= 1.
    expected = {name:original[name][mask] for name in ('times','f','loss','states')}
    changes = measured_pair(resumed,expected)
    state_difference = float(np.max(np.abs(resumed['states']-expected['states'])))
    checks.close('restart_initial_state', resumed['states'][0], original['checkpoint_1_0'],
                 atol=0.,rtol=0.)
    checks.close('restart_prediction_error_receipt', producer['restart_prediction_rms_max'],
                 changes['prediction_error'],atol=1e-15,rtol=1e-12)
    checks.close('restart_loss_error_receipt', producer['restart_loss_max'],
                 changes['loss_error'],atol=1e-15,rtol=1e-12)
    checks.close('restart_state_error_receipt', producer['restart_state_abs_max'],
                 state_difference,atol=1e-15,rtol=1e-12)
    checks.require('restart_numerical_gate', changes['prediction_error'] <= .002 and
                   changes['loss_error'] <= .002)
    refinement_count = len(list(run_root.glob('*/*_resolution2/result.json')))
    qualified = sorted(item['configuration'] for item in outcomes
                       if item['orders']['order4']['dense_motion'] >= .1 and
                       item['orders']['order2']['prediction_error'] >= .05)
    receipt_qualified = sorted(item['case']+'_n'+str(item['width'])+'_seed'+str(item['seed'])
                               for item in producer['nonlinear_qualified_configurations'])
    checks.require('reproduction_refinement_count',
                   producer['conditional_refinement_runs'] == refinement_count)
    checks.require('reproduction_qualified_configurations',qualified == receipt_qualified)
    checks.require('reproduction_extension_decision',
                   producer['extension_triggered'] == (len(qualified) == 0))
    checks.require('reproduction_source_hashes',
                   all(digest(Path(__file__).with_name(name)) == value
                       for name,value in producer['source_hashes'].items()))
    checks.require('reproduction_complete', producer['repeat_run']['status'] ==
                   producer['restart_run']['status'] == 'complete' and
                   repeated['times'][-1] == resumed['times'][-1] == 128.)
    checks.require('reproduction_report_status', producer['status'] == 'pass')
    return dict(status='pass', scientific_arrays_bitwise_equal=len(repeated),
                coefficients_bitwise_equal=len(repeated_coefficients),
                restart_prediction_rms_max=changes['prediction_error'],
                restart_loss_max=changes['loss_error'],
                restart_state_abs_max=state_difference,
                conditional_refinements=refinement_count,
                nonlinear_qualified_configurations=qualified,
                extension_triggered=not bool(qualified),
                file_sha256={name:digest(reproduction_root/name) for name in
                              ('check.json','recomputed_coefficients.npz','repeat.npz','restart.npz')})


def audit_runs(run_root, out, reproduction_root=None):
    started = time.monotonic()
    run_root,out = Path(run_root),Path(out)
    out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    checks = Checks()
    receipt = dict(status='running', run_root=str(run_root.resolve()),
                   checker_sha256=digest(__file__), configurations=[])
    try:
        source_root = run_root/'sources'
        cases = json.loads((source_root/'deep_circle_cases.json').read_text())
        folders = sorted(path.parent for path in run_root.glob('*/configuration.json'))
        checks.require('all_eight_configurations', len(folders) == 8,
                       count=len(folders))
        for folder in folders:
            result = audit_configuration(folder, source_root, cases, checks)
            receipt['configurations'].append(result)
        if reproduction_root is not None:
            receipt['reproduction'] = audit_reproduction(
                run_root,reproduction_root,receipt['configurations'],checks)
        receipt['status'] = 'pass'
    except Exception as exc:
        receipt.update(status='fail', exception=type(exc).__name__, error=str(exc))
        raise
    finally:
        receipt.update(checks=checks.rows,wall_seconds=time.monotonic()-started)
        (out/'check.json').write_text(json.dumps(receipt,indent=2)+'\n')
        print(json.dumps(dict(status=receipt['status'],checks=len(checks.rows),
                              configurations=len(receipt['configurations']),
                              wall_seconds=receipt['wall_seconds'],out=str(out))))
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True)
    parser.add_argument('--runs', help='Independently rescore an eight-configuration campaign')
    parser.add_argument('--reproduction', help='Also audit existing reproduction/restart arrays')
    args = parser.parse_args()
    if args.runs:
        audit_runs(args.runs, args.out, args.reproduction)
    else:
        run_checks(args.out)
