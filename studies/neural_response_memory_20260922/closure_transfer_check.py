"""Independent CPU physical-matrix replay for the width-2048 closure transfer.

Saved-state replay and scalar scoring use NumPy/SciPy and do not import the
producer. The optional tiny self-test separately imports its implementation.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import zipfile

import numpy as np
from scipy.special import ndtr

STATE_NAMES = ('w', 'c', 'A2', 'B2', 'A3', 'B3', 's')
SELU_SCALE = 1.0507009873554804934193349852946
SELU_ALPHA = 1.6732632423543772848170429916717


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fresh_json(path, result):
    """Serialize before opening so a type error cannot leave a partial receipt."""
    encoded = json.dumps(result, indent=2, allow_nan=False) + '\n'
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as handle:
        handle.write(encoded)


def load_archive(path):
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise ValueError('CRC failure: ' + str(path) + ':' + bad)
    with np.load(path, allow_pickle=False) as archive:
        return {key: archive[key] for key in archive.files}


def initialization(width, seed, dimension=2):
    rng = np.random.default_rng(seed)
    return dict(w=rng.standard_normal((width, dimension)),
                W2=rng.standard_normal((width, width)) / math.sqrt(width),
                W3=rng.standard_normal((width, width)) / math.sqrt(width),
                c=rng.standard_normal(width) / width)


def raw_initialization_hash(parameters):
    digest = hashlib.sha256()
    for name in ('w', 'W2', 'W3', 'c'):
        digest.update(np.ascontiguousarray(parameters[name]).tobytes())
    return digest.hexdigest()


def activation(z, name):
    if name == 'relu':
        return np.maximum(z, 0.), (z > 0).astype(np.float64)
    if name == 'gelu':
        probability = ndtr(z)
        return z * probability, probability + z * np.exp(-.5 * z * z) / math.sqrt(2 * math.pi)
    if name == 'selu':
        negative = np.minimum(z, 0.)
        return (SELU_SCALE * np.where(z > 0, z, SELU_ALPHA * np.expm1(negative)),
                SELU_SCALE * np.where(z > 0, 1., SELU_ALPHA * np.exp(negative)))
    raise ValueError('Unsupported activation: ' + str(name))


def prefix(initial, inputs, order, name):
    width, count = len(initial['c']), len(inputs)
    h1 = activation(initial['w'] @ inputs.T, name)[0]
    h2 = activation(initial['W2'] @ h1, name)[0]
    state = dict(w=initial['w'].copy(), c=initial['c'].copy(),
                 **{key: np.zeros((order, width, count)) for key in ('A2', 'B2', 'A3', 'B3')},
                 s=np.asarray(0., dtype=np.float64))
    state['B2'][0] = h1
    state['B3'][0] = h2
    return state


def reconstructed_matrices(state, initial):
    width = len(state['c'])
    order, _, count = state['A2'].shape
    length = 1 + float(state['s'])
    if not math.isfinite(length) or length < 1:
        raise ValueError('Invalid activity clock')
    result = {}
    for layer in (2, 3):
        matrix = initial['W' + str(layer)].copy()
        # Explicit physical matrices; no producer factors/actions are used.
        for degree in range(order):
            coefficient = -2 * (2 * degree + 1) / (count * width * length)
            matrix += coefficient * (state['A' + str(layer)][degree] @ state['B' + str(layer)][degree].T)
        result[layer] = matrix
    return result


def physical_fields(state, matrices, inputs, labels, name):
    h1, d1 = activation(state['w'] @ inputs.T, name)
    h2, d2 = activation(matrices[2] @ h1, name)
    h3, d3 = activation(matrices[3] @ h2, name)
    prediction = state['c'] @ h3 / len(state['c'])
    residual = prediction - labels
    loss = float(np.mean(residual ** 2))
    delta3 = state['c'][:, None] * d3
    delta2 = d2 * (matrices[3].T @ delta3)
    delta1 = d1 * (matrices[2].T @ delta2)
    return dict(h1=h1, h2=h2, h3=h3, delta1=delta1, delta2=delta2, delta3=delta3,
                f=prediction, r=residual, loss=np.asarray(loss), rho=np.asarray(math.sqrt(loss)))


def physical_prediction(state, matrices, inputs, name):
    h1 = activation(state['w'] @ inputs.T, name)[0]
    h2 = activation(matrices[2] @ h1, name)[0]
    h3 = activation(matrices[3] @ h2, name)[0]
    return state['c'] @ h3 / len(state['c'])


def independent_rhs(state, initial, inputs, labels, name):
    fields = physical_fields(state, reconstructed_matrices(state, initial), inputs, labels, name)
    count = len(labels)
    velocity = dict(w=(-2 / count) * ((fields['delta1'] * fields['r']) @ inputs),
                    c=(-2 / count) * (fields['h3'] @ fields['r']), s=fields['rho'].copy())
    for layer in (2, 3):
        sources = {'A': fields['delta' + str(layer)] * fields['r'],
                   'B': fields['rho'] * fields['h' + str(layer - 1)]}
        for letter, source in sources.items():
            key = letter + str(layer)
            moments = state[key]
            derivative = np.empty_like(moments)
            for degree in range(len(moments)):
                lower = np.zeros_like(source)
                for earlier in range(degree):
                    lower += (2 * earlier + 1) * moments[earlier]
                derivative[degree] = source - fields['rho'] / (1 + state['s']) * (degree * moments[degree] + lower)
            velocity[key] = derivative
    return velocity, fields


def score_arrays(dense, closure):
    dense, closure = np.asarray(dense), np.asarray(closure)
    if dense.ndim != 1 or dense.shape != closure.shape or not dense.size:
        raise ValueError('Prediction vectors must have equal nonempty shape')
    if not np.isfinite(dense).all() or not np.isfinite(closure).all():
        raise ValueError('Nonfinite predictions')
    difference = closure - dense
    rms = float(np.sqrt(np.mean(difference * difference)))
    reference_rms = float(np.sqrt(np.mean(dense * dense)))
    nested_rms = float(np.sqrt(np.mean(difference[::2] ** 2)))
    return dict(rms=rms, max_abs=float(np.max(abs(difference))), reference_rms=reference_rms,
                relative_rms=rms / reference_rms if reference_rms else None,
                nested_half_grid_rms=nested_rms, nested_grid_sensitivity=abs(rms - nested_rms),
                nested_grid_passed=abs(rms - nested_rms) <= 1e-5,
                descriptive_agreement=rms <= .1)


def replay_run(run, *, allow_test_width=False):
    """Check hashes/metadata and replay physical matrices on 8+32 inputs."""
    run = Path(run).resolve()
    config = json.loads((run / 'config.json').read_text())
    manifest = json.loads((run / 'manifest.json').read_text())
    summary = json.loads((run / 'summary.json').read_text())
    saved = load_archive(run / 'state.npz')
    predictions = load_archive(run / 'predictions.npz')
    trace = load_archive(run / 'loss_trace.npz')
    source_names = {'closure_transfer_euler.py', 'activation_fast_engine.py', 'activation_moment_engine.py',
                    'deep_moment_engine.py', 'moment_engine.py'}
    checks = {}

    def check(key, value):
        checks[key] = bool(value)

    width, order = config['width'], config['P']
    check('configuration', (allow_test_width or width == 2048) and config['seed'] == 20260920
          and order in (1, 2, 3) and config['activation'] in ('relu', 'gelu', 'selu')
          and config['hidden_layers'] == 3 and config['dtype'] == 'float64'
          and config['mobilities'] == [width, 1, 1, width] and config['model'] == 'moment')
    check('summary_contains_identical_configuration', all(summary.get(key) == value for key, value in config.items()))
    check('summary_contains_identical_manifest', all(summary.get(key) == value for key, value in manifest.items()))
    check('config_hash', sha256(run / 'config.json') == manifest['config_sha256'])
    check('source_names', set(manifest['source_sha256']) == source_names)
    for name in source_names:
        check('source_hash_' + name, manifest['source_sha256'].get(name) == sha256(Path(__file__).parent / name))
    check('protocol_hash', manifest['protocol_sha256'] == sha256(Path(__file__).parent / 'CLOSURE_TRANSFER_2048_PROTOCOL.md'))
    cases_path = Path(config['cases_json'])
    check('cases_hash', sha256(cases_path) == manifest['cases_sha256'])
    for name in ('state.npz', 'predictions.npz', 'loss_trace.npz'):
        check('artifact_hash_' + name, sha256(run / name) == summary['artifact_sha256'][name])
    cases = json.loads(cases_path.read_text())
    literal = cases.get(config['activation'] + '__' + config['task'], cases.get(config['task']))
    angles = [degree * math.pi / 180 for degree in literal['angles_degrees']]
    inputs = np.asarray([[math.cos(a), math.sin(a)] for a in angles], dtype=np.float64)
    labels = np.asarray(literal['labels'], dtype=np.float64)
    check('literal_inputs_labels', np.array_equal(inputs, config['inputs'])
          and np.array_equal(inputs, predictions['train_inputs']) and np.array_equal(labels, config['labels'])
          and np.array_equal(labels, predictions['train_labels']) and inputs.shape == (8, 2) and labels.shape == (8,))
    state = {key: saved[key] for key in STATE_NAMES}
    shapes = dict(w=(width, 2), c=(width,), s=(), **{key: (order, width, 8) for key in ('A2', 'B2', 'A3', 'B3')})
    check('state_shapes_float64', all(state[key].shape == shapes[key] and state[key].dtype == np.float64 for key in STATE_NAMES))
    initial = initialization(width, config['seed'])
    check('initialization_hash', raw_initialization_hash(initial) == manifest['initialization_sha256'])
    initial_state = prefix(initial, inputs, order, config['activation'])
    initial_prediction = physical_prediction(initial_state, {2: initial['W2'], 3: initial['W3']}, inputs, config['activation'])
    initial_loss = float(np.mean((initial_prediction - labels) ** 2))
    check('initial_prefix_loss', np.isclose(initial_loss, trace['losses'][0], atol=2e-12, rtol=2e-9))
    updates, step = summary['updates'], config['step']
    expected_time = updates * step
    check('endpoint_clocks', summary['physical_time'] == float(saved['physical_time']) == float(predictions['physical_time']) == expected_time)
    check('endpoint_update_counts', summary['steps'] == int(saved['steps']) == int(predictions['steps']) == updates)
    check('trace_steps', np.array_equal(trace['steps'], np.arange(updates + 1)))
    check('trace_times', np.array_equal(trace['physical_times'], step * np.arange(updates + 1)))
    check('trace_lengths', len(trace['losses']) == len(trace['wall_seconds']) == updates + 1)
    check('trace_wall_monotone', np.isfinite(trace['wall_seconds']).all() and np.all(np.diff(trace['wall_seconds']) >= 0))
    circle_angles = 2 * np.pi * np.arange(8192) / 8192
    circle_inputs = np.column_stack((np.cos(circle_angles), np.sin(circle_angles)))
    check('circle_grid', np.array_equal(predictions['circle_angles'], circle_angles)
          and np.array_equal(predictions['circle_inputs'], circle_inputs)
          and predictions['circle_predictions'].shape == (8192,))
    finite = all(np.isfinite(value).all() for value in state.values())
    check('state_finite_flag', finite == summary['state_finite'])
    result = dict(run=str(run), checks=checks, passed=False, width=width, P=order, activation=config['activation'],
                  task=config['task'], fitted=summary['fitted'], status=summary['status'],
                  initialization_sha256=raw_initialization_hash(initial), initial_prefix_loss=initial_loss,
                  physical_time=expected_time, updates=updates, step=step,
                  file_sha256={name: sha256(run / name) for name in
                               ('config.json', 'manifest.json', 'summary.json', 'state.npz', 'predictions.npz', 'loss_trace.npz')})
    if not finite:
        check('raw_nonfinite_failure_declared', summary['status'] == 'diverged' and not summary['fitted'])
        result.update(replay_available=False, reason='Raw nonfinite terminal failure; no finite endpoint score',
                      failures=[key for key, value in checks.items() if not value])
        return result
    check('activity_clock', float(state['s']) >= 0 and float(state['s']) == summary['activity'])
    matrices = reconstructed_matrices(state, initial)
    train = physical_prediction(state, matrices, inputs, config['activation'])
    indices = np.arange(0, 8192, 256)
    circle = physical_prediction(state, matrices, circle_inputs[indices], config['activation'])
    train_error = float(np.max(abs(train - predictions['train_predictions'])))
    circle_error = float(np.max(abs(circle - predictions['circle_predictions'][indices])))
    mse = float(np.mean((train - labels) ** 2))
    check('train_replay', np.isfinite(train).all() and train_error <= 2e-9)
    check('circle32_replay', np.isfinite(circle).all() and circle_error <= 2e-9)
    for key, value in (('summary', summary['training_mse']), ('state', saved['training_mse']),
                       ('predictions', predictions['training_mse']), ('trace', trace['losses'][-1])):
        check('actual_mse_matches_' + key, value is not None and np.isclose(mse, value, atol=2e-12, rtol=2e-9))
    check('max_train_residual', np.isclose(np.max(abs(train - labels)), summary['max_train_residual'], atol=2e-9, rtol=2e-9))
    if summary['fitted']:
        check('actual_fitted_threshold', summary['status'] == 'target_loss' and mse <= config['target_mse'] * (1 + 2e-8))
        check('first_discrete_hit', np.all(trace['losses'][:-1] > config['target_mse']))
    result.update(passed=all(checks.values()), replay_available=True, actual_training_mse=mse,
                  train_prediction_max_abs_error=train_error, circle_prediction_max_abs_error=circle_error,
                  passive_indices=indices.tolist(), failures=[key for key, value in checks.items() if not value])
    return result


def score_files(dense_path, closure_path):
    dense_path, closure_path = Path(dense_path), Path(closure_path)
    dense, closure = load_archive(dense_path), load_archive(closure_path)
    for key in ('circle_angles', 'circle_inputs', 'train_inputs', 'train_labels'):
        if not np.array_equal(dense[key], closure[key]):
            raise ValueError('Comparison grids/tasks differ: ' + key)
    result = score_arrays(dense['circle_predictions'], closure['circle_predictions'])
    result.update(dense=str(dense_path.resolve()), closure=str(closure_path.resolve()),
                  dense_sha256=sha256(dense_path), closure_sha256=sha256(closure_path),
                  dense_training_mse_from_predictions=float(np.mean((dense['train_predictions'] - dense['train_labels']) ** 2)),
                  closure_training_mse_from_predictions=float(np.mean((closure['train_predictions'] - closure['train_labels']) ** 2)),
                  interpretation='Raw endpoint-array comparison. A fitted-score label additionally requires both run summaries to declare fitted endpoints.')
    return result


def self_test():
    """Tiny algebra checks using explicit matrices and independent transport."""
    import torch
    import torch.nn.functional as functional
    from activation_moment_engine import ActivationMomentEngine
    from activation_fast_engine import FastActivationMomentEngine
    from deep_moment_engine import DeepMomentState
    from closure_transfer_euler import CachedEulerEngine, EulerStage, euler_update

    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float32)
    torch.use_deterministic_algorithms(True)
    checks = []

    def close(name, actual, expected, atol=3e-12, rtol=3e-12):
        if isinstance(actual, torch.Tensor):
            actual = actual.detach().cpu().numpy()
        if isinstance(expected, torch.Tensor):
            expected = expected.detach().cpu().numpy()
        actual, expected = np.asarray(actual), np.asarray(expected)
        same_shape = actual.shape == expected.shape
        error = float(np.max(abs(actual - expected))) if same_shape and actual.size else None
        passed = same_shape and np.isfinite(actual).all() and np.isfinite(expected).all()
        passed = passed and np.allclose(actual, expected, atol=atol, rtol=rtol)
        checks.append(dict(name=name, passed=bool(passed), max_abs_error=error))

    width, seed = 7, 773
    angles = np.arange(8) * .37 + .11
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    labels = np.array([1., -1.] * 4)
    initial = initialization(width, seed)
    perturb = np.random.default_rng(849)
    for name in ('relu', 'gelu', 'selu'):
        z = torch.tensor([-100., -4., -.01, 0., .01, 4., 100.], dtype=torch.float64, requires_grad=True)
        value = (functional.relu(z) if name == 'relu' else functional.gelu(z, approximate='none')
                 if name == 'gelu' else functional.selu(z))
        derivative = torch.autograd.grad(value.sum(), z)[0]
        expected_value, expected_derivative = activation(z.detach().numpy(), name)
        close(name + '_activation_value', expected_value, value)
        close(name + '_activation_derivative_including_zero', expected_derivative, derivative)
        for order in (1, 2, 3):
            engines = [kind(2, width, order, inputs, labels, activation=name, seed=seed,
                            device='cpu', dtype=torch.float64)
                       for kind in (ActivationMomentEngine, FastActivationMomentEngine, CachedEulerEngine)]
            initial_state = prefix(initial, inputs, order, name)
            for backend, engine in zip(('original', 'fast', 'cached'), engines):
                tag = f'{name}_P{order}_{backend}'
                close(tag + '_initial_W20', engine.W20, initial['W2'], 0, 0)
                close(tag + '_initial_W30', engine.W30, initial['W3'], 0, 0)
                for key in STATE_NAMES:
                    close(tag + '_prefix_' + key, getattr(engine.initial, key), initial_state[key])
            moved = {key: value.copy() for key, value in initial_state.items()}
            for key in STATE_NAMES[:-1]:
                moved[key] += .08 * perturb.standard_normal(moved[key].shape)
            moved['s'] = np.asarray(.43)
            for state_name, values in (('prefix', initial_state), ('moved', moved)):
                matrices = reconstructed_matrices(values, initial)
                velocity, fields = independent_rhs(values, initial, inputs, labels, name)
                for backend, engine in zip(('original', 'fast', 'cached'), engines):
                    tag = f'{name}_P{order}_{backend}_{state_name}'
                    state = DeepMomentState(*(torch.tensor(values[key], dtype=torch.float64) for key in STATE_NAMES))
                    actual_fields = engine.fields(state)
                    for key in ('f', 'loss', 'rho', 'h1', 'h2', 'h3', 'delta1', 'delta2', 'delta3'):
                        close(tag + '_fields_' + key, actual_fields[key], fields[key])
                    actual_velocity = engine.rhs(state)
                    for key in STATE_NAMES:
                        close(tag + '_rhs_' + key, getattr(actual_velocity, key), velocity[key])
                    for layer in (2, 3):
                        for query_count in (8, 11):
                            query = perturb.standard_normal((width, query_count))
                            for transpose in (False, True):
                                actual = engine.apply_hidden(state, layer, torch.tensor(query, dtype=torch.float64), transpose=transpose)
                                matrix = matrices[layer].T if transpose else matrices[layer]
                                close(tag + f'_matrix{layer}_Q{query_count}_transpose{transpose}', actual, matrix @ query)
                    # Use exactly the producer's current prediction as labels,
                    # so zero residual is exact even across contraction orders.
                    saved_labels = engine.labels
                    engine.labels = actual_fields['f'].clone()
                    zero_velocity = engine.rhs(state)
                    for key in STATE_NAMES:
                        close(tag + '_absorbing_zero_residual_' + key, getattr(zero_velocity, key), np.zeros_like(values[key]), 0, 0)
                    engine.labels = saved_labels
                    if backend == 'cached':
                        stage = EulerStage(engine, state, backend='eager')
                        cached_velocity, cached_loss, valid = stage.evaluate()
                        checks.append(dict(name=tag + '_stage_valid', passed=valid))
                        close(tag + '_cached_current_loss', cached_loss, fields['loss'])
                        for key in STATE_NAMES:
                            close(tag + '_stage_preserves_state_' + key, getattr(state, key), values[key], 0, 0)
                            close(tag + '_cached_velocity_' + key, getattr(cached_velocity, key), velocity[key])
                        step = .0017
                        euler_update(state, cached_velocity, step)
                        after = {key: values[key] + step * velocity[key] for key in STATE_NAMES}
                        for key in STATE_NAMES:
                            close(tag + '_simultaneous_Euler_' + key, getattr(state, key), after[key])
                        _, post_loss, post_valid = stage.evaluate()
                        checks.append(dict(name=tag + '_post_stage_valid', passed=post_valid))
                        post_fields = physical_fields(after, reconstructed_matrices(after, initial), inputs, labels, name)
                        close(tag + '_post_current_loss', post_loss, post_fields['loss'])
            # The prefix gives the dense tangent, not exact equality of a
            # finite Euler update after nonlinear moment reconstruction.
            velocity, fields = independent_rhs(initial_state, initial, inputs, labels, name)
            for layer in (2, 3):
                tangent = np.zeros((width, width))
                for degree in range(order):
                    tangent += -2 * (2 * degree + 1) / (len(labels) * width) * (
                        velocity['A' + str(layer)][degree] @ initial_state['B' + str(layer)][degree].T)
                dense = -2 / (len(labels) * width) * ((fields['delta' + str(layer)] * fields['r']) @ fields['h' + str(layer - 1)].T)
                close(f'{name}_P{order}_prefix_dense_tangent{layer}', tangent, dense)
    return dict(passed=all(check['passed'] for check in checks), checks=checks,
                failures=[check for check in checks if not check['passed']],
                scientific_training=False, gpu_used=False, source_sha256=sha256(__file__),
                producer_sources={key: sha256(Path(__file__).parent / key) for key in
                                  ('closure_transfer_euler.py', 'activation_fast_engine.py', 'activation_moment_engine.py',
                                   'deep_moment_engine.py', 'moment_engine.py')})


def pipeline_test(scratch):
    """Tiny CPU execution checks; their saved fixtures remain in audit scratch."""
    import contextlib
    import io
    import closure_transfer_euler as runner

    scratch = Path(scratch).resolve()
    scratch.mkdir(parents=True, exist_ok=False)
    repository = Path(__file__).resolve().parents[2]
    cases = repository / 'data/generated/neural_response_memory_20260922/closure_transfer_2048_inputs01/provenance/cases.json'
    rows, update_checks = [], []
    fixtures = [('relu', 1, 'max_steps', 3, 260., 100., 1e-8),
                ('gelu', 2, 'max_steps', 3, 260., 100., 1e-8),
                ('selu', 3, 'max_steps', 3, 260., 100., 1e-8),
                ('selu', 3, 'max_time', 20, .004, 100., 1e-8),
                ('gelu', 2, 'wall_limit', 20, 260., 1e-12, 1e-8),
                ('relu', 1, 'target_loss', 20, 260., 100., 2.)]
    for index, (name, order, status, cap, horizon, seconds, target) in enumerate(fixtures):
        out = scratch / f'{index}_{name}_{status}'
        args = runner.parser().parse_args([
            '--activation', name, '--task', 'quadrant_alternating', '--P', str(order), '--step', '.002',
            '--device', 'cpu', '--out', str(out), '--cases-json', str(cases), '--max-seconds', str(seconds),
            '--max-time', str(horizon), '--max-steps', str(cap), '--target-mse', str(target), '--backend', 'eager'])
        with contextlib.redirect_stdout(io.StringIO()):
            summary = runner.run(args, width=7)
        row = replay_run(out, allow_test_width=True)
        row['expected_status'] = status
        row['checks']['stop_reason_matches_fixture'] = summary['status'] == status
        initial = initialization(7, 20260920)
        inputs, labels = np.asarray(summary['inputs']), np.asarray(summary['labels'])
        expected = prefix(initial, inputs, order, name)
        for _ in range(summary['updates']):
            velocity, _ = independent_rhs(expected, initial, inputs, labels, name)
            expected = {key: expected[key] + args.step * velocity[key] for key in STATE_NAMES}
        actual = load_archive(out / 'state.npz')
        for key in STATE_NAMES:
            error = float(np.max(abs(actual[key] - expected[key])))
            passed = bool(np.allclose(actual[key], expected[key], atol=3e-12, rtol=3e-12))
            row['checks']['independent_saved_Euler_' + key] = passed
            update_checks.append(dict(fixture=str(out), block=key, passed=passed, max_abs_error=error))
        row['passed'] = all(row['checks'].values())
        row['failures'] = [key for key, value in row['checks'].items() if not value]
        rows.append(row)
    # Preserve a deliberately damaged archive to show that replay rejects it.
    archive_path = scratch / '0_relu_max_steps/state.npz'
    damaged = bytearray(archive_path.read_bytes())
    with zipfile.ZipFile(archive_path) as archive:
        info = archive.infolist()[0]
        offset = info.header_offset + 30 + len(info.filename.encode()) + len(info.extra)
        offset += max(1, info.compress_size // 2)
    damaged[offset] ^= 0xFF
    damaged_path = scratch / 'intentional_corrupt_state.npz'
    damaged_path.write_bytes(damaged)
    rejected = False
    try:
        load_archive(damaged_path)
    except Exception:
        rejected = True
    return dict(passed=all(row['passed'] for row in rows) and rejected, rows=rows,
                update_checks=update_checks, intentionally_corrupted_archive_rejected=rejected,
                scientific_training=False, gpu_used=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='mode', required=True)
    algebra = commands.add_parser('self-test')
    algebra.add_argument('--out', required=True)
    pipeline = commands.add_parser('pipeline-test')
    pipeline.add_argument('--scratch', required=True)
    pipeline.add_argument('--out', required=True)
    replay = commands.add_parser('replay')
    replay.add_argument('--run', nargs='+', required=True)
    replay.add_argument('--out', required=True)
    score = commands.add_parser('score')
    score.add_argument('--dense', required=True)
    score.add_argument('--closure', required=True)
    score.add_argument('--out', required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if args.mode == 'self-test':
        result = self_test()
    elif args.mode == 'pipeline-test':
        result = pipeline_test(args.scratch)
    elif args.mode == 'replay':
        rows = []
        for run in args.run:
            try:
                rows.append(replay_run(run))
            except Exception as error:
                rows.append(dict(run=str(run), passed=False, exception=type(error).__name__, message=str(error)))
        result = dict(passed=all(row['passed'] for row in rows), runs=rows, gpu_used=False)
    else:
        result = dict(passed=True, score=score_files(args.dense, args.closure), gpu_used=False)
    result.update(checker_sha256=sha256(__file__), executable=sys.executable, numpy=np.__version__,
                  elapsed_seconds=time.monotonic() - started, command=sys.argv)
    fresh_json(args.out, result)
    print(json.dumps(dict(passed=result['passed'], output=str(Path(args.out).resolve()),
                          elapsed_seconds=result['elapsed_seconds']), indent=2))
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
