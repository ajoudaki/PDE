"""Independent NumPy-only replay of the preregistered trainable-p3 test.

Imports neither the model/runner nor another analysis module. No training.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DATA = ROOT / 'data/generated/adaptive_response_compression_20260922'
OLD = ROOT / 'data/generated/gradient_flow_probe_dictionary_20260921'
CIRCLE = ROOT / 'data/generated/random_dictionary_learned_circle_20260920'
CASE = 'two_outliers_alternating'
NAMES = ('w', 'c', 'M', 'b1', 'b2')
INITIAL = OLD / 'suite_refined01' / (CASE + '_new_p3') / 'arrays.npz'
REFERENCE = CIRCLE / 'scaling_discovery_refined01' / (CASE + '_full') / 'arrays.npz'
EXPECTED_INITIAL = '300b6ef7b3a60de6920f65d3ba1cddee5f447fa910f61bfa2c6fde712bf8905a'
EXPECTED_REFERENCE = '70d4c76f6817b7e0e2c24be3dad9b8883054d1ebdf031d66efdb2677106c5357'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def arr_sha(array):
    return hashlib.sha256(np.ascontiguousarray(array).tobytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def predict(state, inputs, block=256):
    n = len(state['c'])
    chunks = []
    for offset in range(0, len(inputs), block):
        h = np.tanh(state['w'] @ inputs[offset:offset + block].T)
        coefficients = (state['b1'].T @ h) / n
        hidden = np.tanh(state['b2'] @ (state['M'] @ coefficients))
        chunks.append((state['c'] @ hidden) / n)
    return np.concatenate(chunks)


def metrics(prediction, reference):
    residual = prediction - reference
    rms = float(np.sqrt(np.mean(residual ** 2)))
    grid_rms = float(np.sqrt(np.mean(residual[::2] ** 2)))
    maximum = float(np.max(np.abs(residual)))
    return dict(rms=rms, l1=float(np.mean(np.abs(residual))), max_abs=maximum,
                rms4096=grid_rms, rms_grid_change=abs(rms - grid_rms),
                max4096=float(np.max(np.abs(residual[::2]))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=DATA / 'independent_trainable01')
    args = parser.parse_args()
    out = args.out.resolve()
    assert DATA in out.parents
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    checks = []
    result = dict(checker_source=str(Path(__file__).resolve()),
                  checker_sha256=sha(__file__), numpy=np.__version__,
                  cpu_only=True, producer_imported=False, checks=checks,
                  input_hashes={}, runs={}, baselines={})

    def require(condition, description):
        checks.append(dict(check=description, passed=bool(condition)))
        if not condition:
            raise AssertionError(description)

    try:
        require(sha(INITIAL) == EXPECTED_INITIAL, 'p3 initialization archive pinned hash')
        require(sha(REFERENCE) == EXPECTED_REFERENCE, 'dense finer reference pinned hash')
        for path in (INITIAL, REFERENCE):
            result['input_hashes'][str(path)] = sha(path)
        with np.load(INITIAL, allow_pickle=False) as archive:
            original = {k: archive[k][0].copy() if k in ('w', 'c', 'M')
                        else archive[k].copy() for k in NAMES}
            training_inputs = archive['training_inputs'].copy()
            labels = archive['labels'].copy()
            endpoint_grid = archive['endpoint_inputs'].copy()
            endpoint_angles = archive['endpoint_angles'].copy()
            circle_grid = archive['circle_inputs'].copy()
            frozen_endpoint = archive['endpoint_prediction'].copy()
        with np.load(REFERENCE, allow_pickle=False) as archive:
            dense_endpoint = archive['endpoint_prediction'].copy()
            require(np.array_equal(endpoint_grid, archive['endpoint_inputs']), 'dense endpoint input grid')
            require(np.array_equal(endpoint_angles, archive['endpoint_angles']), 'dense endpoint angle grid')
            require(np.array_equal(training_inputs, archive['training_inputs']), 'dense training inputs')
            require(np.array_equal(labels, archive['labels']), 'dense training labels')
        require(np.array_equal(labels, np.array([1, -1, 1, -1, 1, -1, 1, -1])), 'literal task labels')
        radians = np.array([15, 27, 39, 51, 63, 75, 165, 285]) * np.pi / 180
        require(np.max(abs(training_inputs - np.column_stack((np.cos(radians), np.sin(radians))))) < 1e-14,
                'literal task angles')
        require(len(endpoint_grid) == 8192 and len(circle_grid) == 2048, 'grid counts')
        require(np.max(abs(endpoint_angles - np.arange(8192) * (2 * np.pi / 8192))) < 1e-14,
                'uniform endpoint circle')

        for model, cohort in [('p3', 'suite'), ('p7', 'p7')]:
            for level in ('primary', 'refined'):
                path = OLD / (cohort + '_' + level + '01') / (CASE + '_new_' + model) / 'arrays.npz'
                summary_path = path.with_name('summary.json')
                result['input_hashes'][str(path)] = sha(path)
                result['input_hashes'][str(summary_path)] = sha(summary_path)
                with np.load(path, allow_pickle=False) as archive:
                    require(np.array_equal(endpoint_grid, archive['endpoint_inputs']), model + ' ' + level + ' baseline grid')
                    endpoint = archive['endpoint_prediction'].copy()
                result['baselines'][model + '_' + level] = dict(
                    path=str(path), time=read(summary_path)['time'],
                    common_finer_reference_metrics=metrics(endpoint, dense_endpoint))

        endpoints = {}
        max_output_replay = max_loss_replay = 0.0
        snapshot_count = 0
        specifications = [('trainable_p3_primary01', True, 6.25e-5),
                          ('trainable_p3_refined01', True, 1.5625e-5),
                          ('frozen_p3_replay01', False, 1.5625e-5)]
        for name, train_basis, rtol in specifications:
            directory = DATA / name
            config, summary = (read(directory / f) for f in ('config.json', 'summary.json'))
            run = result['runs'][name] = dict(path=str(directory), source_hashes={},
                hashes={f: sha(directory / f) for f in ('config.json', 'summary.json', 'arrays.npz')},
                status=summary['status'], time=summary['time'], snapshot_replay=[], initial_exact={})
            for path, digest in config['source_hashes'].items():
                actual = sha(path)
                require(actual == digest, name + ' source hash ' + path)
                run['source_hashes'][path] = actual
            require(set(config['source_hashes']) == {str(HERE / f) for f in
                    ('trainable_dictionary.py', 'run_trainable_p3.py', 'TRAINABLE_P3_PROTOCOL.md')}, name + ' source set')
            require(config['initial_archive'] == str(INITIAL) and config['initial_archive_sha256'] == EXPECTED_INITIAL,
                    name + ' initial provenance')
            require(config['reference_archive'] == str(REFERENCE) and config['reference_sha256'] == EXPECTED_REFERENCE,
                    name + ' reference provenance')
            require(run['hashes']['arrays.npz'] == summary['arrays_sha256'], name + ' output hash')
            expected = dict(case=CASE, width=2048, p=3, k1=6, k2=12, seed=20260920,
                rtol=rtol, atol=rtol / 100, threshold=.001, train_basis=train_basis,
                initial_step=.05, max_step=2, min_step=1e-7, max_time=10000, max_steps=30000,
                dtype='float64', deterministic=True, tf32=False)
            require(all(config[k] == value for k, value in expected.items()), name + ' protocol config')
            require(config['mobilities'] == dict(w=2048, c=2048, M=1,
                    b1=2048 if train_basis else 0, b2=2048 if train_basis else 0), name + ' mobilities')
            require(summary['status'] == 'fitted', name + ' fit status')
            with np.load(directory / 'arrays.npz', allow_pickle=False) as z:
                arrays = {k: z[k] for k in z.files}
            require(all(np.isfinite(v).all() for v in arrays.values()), name + ' finite arrays')
            times, losses, steps = (arrays[k] for k in ('times', 'losses', 'accepted_steps'))
            snapshots = arrays['snapshot_times']
            require(len(times) == len(losses) == len(steps) + 1 == summary['steps'] + 1,
                    name + ' history lengths')
            require(times[0] == 0 and np.all(np.diff(times) > 0) and np.max(abs(np.diff(times) - steps)) < 1e-10,
                    name + ' accepted times and steps')
            require(np.all(steps > 0) and max(steps) <= 2 + 1e-12 and len(steps) <= 30000,
                    name + ' step bounds')
            require(np.all(arrays['local_error_ratios'] <= 1 + 1e-12), name + ' accepted error ratios')
            require(np.all(losses[:-1] > .001) and losses[-1] <= .001, name + ' first fitting crossing')
            require(times[-1] == summary['time'] and losses[-1] == summary['loss'], name + ' endpoint summary identity')
            require(np.all(np.diff(losses) <= losses[:-1] * 1e-8 + 1.01e-12), name + ' loss acceptance')
            for key in ('training_inputs', 'labels', 'endpoint_inputs', 'endpoint_angles', 'circle_inputs'):
                expected_array = dict(training_inputs=training_inputs, labels=labels, endpoint_inputs=endpoint_grid,
                                      endpoint_angles=endpoint_angles, circle_inputs=circle_grid)[key]
                require(np.array_equal(arrays[key], expected_array), name + ' exact ' + key)
            for key in NAMES:
                require(arrays[key].shape == (len(snapshots),) + original[key].shape, name + ' shape ' + key)
                exact = np.array_equal(arrays[key][0], original[key])
                require(exact and arr_sha(arrays[key][0]) == config['initial_array_sha256'][key],
                        name + ' exact initial ' + key)
                run['initial_exact'][key] = exact
            total = sum(arrays[k][0].size for k in NAMES)
            trained = total if train_basis else sum(arrays[k][0].size for k in ('w', 'c', 'M'))
            require(total == config['model_storage_scalars'] == 43080 and trained == config['trainable_scalars'],
                    name + ' parameter counts')
            run.update(trainable_scalars=trained, model_storage_scalars=total)
            for j, t in enumerate(snapshots):
                state = {k: arrays[k][j] for k in NAMES}
                output = predict(state, circle_grid)
                output_error = float(np.max(abs(output - arrays['circle_predictions'][j])))
                loss_value = float(np.mean((predict(state, training_inputs) - labels) ** 2))
                ix = int(np.argmin(abs(times - t)))
                require(abs(times[ix] - t) < 1e-10, name + ' snapshot time ' + str(j))
                loss_error = abs(loss_value - losses[ix])
                require(output_error <= 1e-10 and loss_error <= 1e-10, name + ' snapshot replay ' + str(j))
                run['snapshot_replay'].append(dict(time=float(t), output_error=output_error,
                                                    loss=loss_value, loss_error=loss_error))
                snapshot_count += 1
                max_output_replay = max(max_output_replay, output_error)
                max_loss_replay = max(max_loss_replay, loss_error)
            endpoint = predict({k: arrays[k][-1] for k in NAMES}, endpoint_grid)
            endpoint_error = float(np.max(abs(endpoint - arrays['endpoint_prediction'])))
            require(endpoint_error <= 1e-10, name + ' endpoint replay')
            max_output_replay = max(max_output_replay, endpoint_error)
            run['endpoint_replay_max'] = endpoint_error
            run['metrics'] = metrics(endpoint, dense_endpoint)
            require(run['metrics']['rms_grid_change'] <= .001, name + ' metric grid convergence')
            require(abs(run['metrics']['rms'] - summary['rms']) <= 1e-10 and
                    abs(run['metrics']['max_abs'] - summary['max_abs']) <= 1e-10, name + ' summary metrics')
            endpoints[name] = endpoint
            run['basis_motion_rms'] = {}
            run['basis_column_rms'] = {}
            for key in ('b1', 'b2'):
                motion = float(np.sqrt(np.mean((arrays[key][-1] - arrays[key][0]) ** 2)))
                column_rms = np.sqrt(np.mean(arrays[key][-1] ** 2, axis=0))
                require(abs(motion - summary['basis_motion_rms'][key]) < 1e-10, name + ' basis motion ' + key)
                require(np.max(abs(column_rms - summary['basis_column_rms'][key])) < 1e-10, name + ' basis norms ' + key)
                require(np.max(abs(np.linalg.eigvalsh(arrays[key][-1].T @ arrays[key][-1] / 2048) -
                            summary['basis_gram_eigenvalues'][key])) < 1e-10, name + ' basis spectrum ' + key)
                if not train_basis:
                    require(np.array_equal(arrays[key], np.broadcast_to(original[key], arrays[key].shape)),
                            name + ' basis frozen ' + key)
                run['basis_motion_rms'][key] = motion
                run['basis_column_rms'][key] = column_rms.tolist()

        refinement = float(np.max(abs(endpoints['trainable_p3_primary01'] - endpoints['trainable_p3_refined01'])))
        result['trainable_refinement_max'] = refinement
        require(refinement <= .01, 'trainable endpoint numerical refinement')
        result['extra_run_eligible'] = refinement > .01
        reproduction = float(np.max(abs(endpoints['frozen_p3_replay01'] - frozen_endpoint)))
        time_error = abs(result['runs']['frozen_p3_replay01']['time'] - result['baselines']['p3_refined']['time'])
        result.update(frozen_reproduction_max=reproduction, frozen_reproduction_time_error=time_error)
        require(reproduction <= .001 and time_error <= .001, 'frozen reproduction gate')
        verdicts = {}
        for baseline in ('p3', 'p7'):
            base = result['baselines'][baseline + '_refined']['common_finer_reference_metrics']['rms']
            differences = [base - result['runs'][name]['metrics']['rms'] for name in
                           ('trainable_p3_primary01', 'trainable_p3_refined01')]
            verdict = 'pass' if min(differences) >= .01 else 'fail' if max(differences) <= -.01 else 'inconclusive'
            verdicts[baseline] = dict(verdict=verdict, frozen_finer_rms=base,
                                      frozen_minus_trainable_rms=differences)
        result.update(passed=True, verdicts=verdicts, snapshot_count=snapshot_count,
                      maximum_prediction_replay_error=max_output_replay,
                      maximum_training_loss_replay_error=max_loss_replay)
    except Exception as exc:
        result.update(passed=False, exception=repr(exc))
        raise
    finally:
        result['cpu_seconds'] = time.monotonic() - started
        (out / 'checks.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
        print(json.dumps({k: result[k] for k in ('passed', 'cpu_seconds', 'snapshot_count',
            'maximum_prediction_replay_error', 'maximum_training_loss_replay_error',
            'trainable_refinement_max', 'frozen_reproduction_max', 'frozen_reproduction_time_error', 'verdicts')
            if k in result}, indent=2))


if __name__ == '__main__':
    main()
