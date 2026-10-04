"""Reference-split completion analysis; frozen calculations and CPU-only gates.

Example:
  python analyze_population_cost.py --candidate-dirs C0 C1 --reference-dirs R0 R1 \
      --out-dir data/generated/response_memory_fast_mixing_20261002/population_cost_analysis01

Each input directory contains fast_training.py config.json, summary.json and
per-trajectory NPZ files. Missing/incomplete inputs are reported, never imputed.
Only small normalized trajectory Gram matrices are retained for bootstrap.
"""
import os
for _thread_var in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_thread_var] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
from collections import Counter
import numpy as np

WIDTHS = (512, 2048, 8192, 16384)
KINDS = ('gaussian', 'quarter_circle')
CSEEDS = tuple(range(7601, 7617))
RSEEDS = tuple(range(8001, 8033))
KS = np.array([1, 2, 4, 8, 16])
OBS = {'predictions': (21, 357), 'train_second_gram': (21, 64, 64)}
TOLERANCES = (.0025, .00125, .005)
BOOTSTRAPS = 1000


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def data_digest(path):
    h = hashlib.sha256()
    with np.load(path, allow_pickle=False) as z:
        for key in ('X', 'y', 'indices'):
            a = np.ascontiguousarray(z[key])
            h.update(key.encode()); h.update(str(a.shape).encode())
            h.update(a.dtype.str.encode()); h.update(a.tobytes())
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def finite_number(value):
    return isinstance(value, (int, float, np.number)) and bool(np.isfinite(value))


def checked_nonnegative(value, label):
    """Only roundoff-size negative squared norms/variances may be clamped."""
    a = np.asarray(value, dtype=np.float64)
    if not np.isfinite(a).all() or np.min(a) < -1e-10:
        raise ValueError(f'{label}: invalid squared norm/variance: {np.min(a)}')
    return np.maximum(a, 0.)


def quadratic(weights, gram):
    return np.einsum('bi,ij,bj->b', weights, gram, weights, optimize=True)


def sample_variance(weights, gram, size):
    return checked_nonnegative((weights @ np.diag(gram) - quadratic(weights, gram))
                               * size / (size - 1), 'sample variance')


def squared_distance(weights, reference_weights, gram, cross, reference_gram):
    return checked_nonnegative(quadratic(weights, gram)
        - 2 * np.einsum('bi,ij,bj->b', weights, cross, reference_weights, optimize=True)
        + quadratic(reference_weights, reference_gram), 'mean distance')


def error_curves(weights, reference_weights, gram, cross, reference_gram):
    """Return B x 5 E_K, V and squared mean-reference distance."""
    variance = sample_variance(weights, gram, 16)
    distance = squared_distance(weights, reference_weights, gram, cross, reference_gram)
    errors = distance[:, None] + variance[:, None] * (1 / KS - 1 / 16)
    return checked_nonnegative(errors, 'E_K'), variance, distance


def load_directories(directories, role, failures, inventory):
    records = {}
    for directory in directories:
        directory = Path(directory).resolve()
        item = {'directory': str(directory), 'role': role}
        inventory.append(item)
        try:
            config = read_json(directory / 'config.json')
            item['config_sha256'] = digest(directory / 'config.json')
            item['sources'] = config.get('sources', {})
            item['gpu'] = config.get('gpu')
            item['versions'] = config.get('versions')
            args = config['arguments']
            item['device'] = args.get('device')
            if args.get('compact') is not True or args.get('tf32') is not True or args.get('dt') != .02:
                failures.append(f'{directory}: requires compact=True, tf32=True, dt=.02')
            if Path(args.get('protocol', '')).name != 'POPULATION_COST_PROTOCOL.md':
                failures.append(f'{directory}: wrong protocol in config')
            check = config['checks']
            for name, limit in [('forward_error', 3e-6), ('transpose_error', 3e-6),
                                ('autograd_error', 1e-11), ('defect_error', 1e-11)]:
                if not finite_number(check.get(name)) or not 0 <= check[name] <= limit:
                    failures.append(f'{directory}: failed/missing {name}')
            item['data_payload_sha256'] = data_digest(directory / 'data.npz')
            with np.load(directory / 'data.npz', allow_pickle=False) as data:
                if data['X'].shape != (357, 64) or data['y'].shape != (357,) or data['indices'].shape != (357,):
                    failures.append(f'{directory}: unexpected dataset shape')
                if not all(np.isfinite(data[k]).all() for k in ('X', 'y')):
                    failures.append(f'{directory}: nonfinite data')
            summary_file = directory / 'summary.json'
            if summary_file.exists():
                summary = read_json(summary_file)
                rows = summary['rows']
                item['summary_sha256'] = digest(summary_file)
                item['elapsed_seconds'] = summary.get('elapsed_seconds')
                if not finite_number(item['elapsed_seconds']) or item['elapsed_seconds'] <= 0:
                    failures.append(f'{directory}: invalid process runtime')
                    item['elapsed_seconds'] = None
            else:
                failures.append(f'{directory}: missing summary.json (partial campaign)')
                rows = [read_json(p) for p in sorted(directory.glob('*_n*_s*_dt*.json'))]
                item['elapsed_seconds'] = None
            for row in rows:
                key = (row['kind'], int(row['n']), int(row['seed']))
                tag = f"{key[0]}_n{key[1]}_s{key[2]}_dt{row['dt']:g}"
                if key in records:
                    failures.append(f'duplicate {role} record {key}')
                    continue
                row = dict(row)
                row['_path'] = str(directory / (tag + '.npz'))
                row['_directory'] = str(directory)
                row['_device'] = args.get('device')
                row['_valid'] = True
                if row.get('dt') != .02 or row.get('compact') is not True:
                    failures.append(f'{tag}: requires compact Heun dt=.02'); row['_valid'] = False
                if not finite_number(row.get('trajectory_seconds')) or row['trajectory_seconds'] <= 0:
                    failures.append(f'{tag}: missing/invalid complete trajectory_seconds'); row['_valid'] = False
                for name, limit in [('graph_error', 1e-6), ('hadamard_error', 3e-6), ('adjoint_error', 3e-6)]:
                    if not finite_number(row.get(name)) or not 0 <= row[name] <= limit:
                        failures.append(f'{tag}: failed/missing {name}'); row['_valid'] = False
                metrics = row.get('metrics', [])
                required = ('first_motion', 'second_motion', 'train_mse', 'test_mse', 'frozen_test_mse')
                if len(metrics) != 21 or any(not all(finite_number(m.get(k)) for k in required) for m in metrics):
                    failures.append(f'{tag}: missing/nonfinite feature-motion or loss diagnostics'); row['_valid'] = False
                records[key] = row
        except (OSError, ValueError, KeyError, TypeError) as error:
            failures.append(f'{directory}: cannot read campaign metadata: {error}')
    expected = ({(k, n, s) for k in KINDS for n in WIDTHS for s in CSEEDS} if role == 'candidate'
                else {('quarter_circle', 32768, s) for s in RSEEDS})
    missing, extra = sorted(expected - records.keys()), sorted(records.keys() - expected)
    if missing: failures.append(f'{role}: missing {len(missing)} records: {missing}')
    if extra: failures.append(f'{role}: unexpected records: {extra}')
    return {key: row for key, row in records.items() if key in expected}


def load_observables(rows, failures):
    outputs = {name: [] for name in OBS}
    okay = True
    for row in rows:
        if not row['_valid']: okay = False
        path = row['_path']
        try:
            with np.load(path, allow_pickle=False) as arrays:
                if not np.array_equal(arrays['times'], np.arange(21) * 2.):
                    raise ValueError('times differ from 0,2,...,40')
                for name, shape in OBS.items():
                    a = arrays[name]
                    if a.shape != shape or a.dtype != np.float32 or not np.isfinite(a).all():
                        raise ValueError(f'{name}: expected finite float32 {shape}, got {a.shape}/{a.dtype}')
                    outputs[name].append(a.astype(np.float64).ravel())
                for name, shape in [('frozen', (21, 357)), ('train_first_gram', (21, 64, 64)), ('initial_gram', (64, 64))]:
                    a = arrays[name]
                    if a.shape != shape or not np.isfinite(a).all():
                        raise ValueError(f'missing/invalid retained {name}')
                for name in ('train_first_gram', 'train_second_gram'):
                    a = arrays[name]
                    if np.max(np.abs(a - np.swapaxes(a, -1, -2))) > 1e-6:
                        raise ValueError(f'{name} is not symmetric within 1e-6')
        except (OSError, KeyError, ValueError) as error:
            failures.append(f'{path}: {error}'); okay = False
    return {k: np.stack(v) for k, v in outputs.items()} if okay else None


def choose(curves, costs, tolerance):
    """Both observables must meet tolerance; retain all points, even dominated."""
    eligible = np.all(curves <= tolerance, axis=-1)
    prices = np.where(eligible, costs, np.inf)
    best = np.argmin(prices.reshape(prices.shape[0], -1), axis=1)
    value = np.min(prices.reshape(prices.shape[0], -1), axis=1)
    return best, value, eligible


def comparisons(all_errors, all_costs, conditions, tolerance):
    chosen = {}
    for kind in KINDS:
        ids = [i for i, condition in enumerate(conditions) if condition['kind'] == kind]
        if not ids:
            chosen[kind] = (np.full(all_errors.shape[0], -1), np.full(all_errors.shape[0], np.inf), ids)
        else:
            best, value, _ = choose(all_errors[:, ids], all_costs[:, ids], tolerance)
            chosen[kind] = (best, value, ids)
    gcost, fcost = chosen['gaussian'][1], chosen['quarter_circle'][1]
    both = np.isfinite(gcost) & np.isfinite(fcost)
    success = both & (fcost <= .5 * gcost)
    ratios = np.divide(fcost, gcost, out=np.full_like(fcost, np.nan), where=both)
    statuses = np.where(both, 'both_eligible', np.where(np.isfinite(fcost), 'no_gaussian',
                        np.where(np.isfinite(gcost), 'no_fast', 'neither_eligible')))
    winners = {}
    for kind, (best, value, ids) in chosen.items():
        winners[kind] = []
        for b in range(len(value)):
            if not np.isfinite(value[b]): winners[kind].append(None); continue
            local, ki = divmod(int(best[b]), len(KS))
            ci = ids[local]
            winners[kind].append({'kind': kind, 'width': conditions[ci]['width'], 'K': int(KS[ki]),
                'cost_seconds': float(value[b]), 'prediction_rms': float(all_errors[b, ci, ki, 0]),
                'second_gram_rms': float(all_errors[b, ci, ki, 1])})
    valid_ratios = ratios[both]
    return {'tolerance': tolerance, 'draw_count': len(ratios),
        'success_fraction': float(np.mean(success)), 'success_draws': int(success.sum()),
        'eligibility_counts': dict(Counter(statuses.tolist())),
        'ratio_definition': 'fast cost / Gaussian cost; undefined unless both eligible',
        'ratio_quantiles_when_both_eligible': ({str(q): float(np.quantile(valid_ratios, q))
            for q in (0, .025, .05, .25, .5, .75, .9, .95, .975, 1)} if len(valid_ratios) else {}),
        'ratios': [float(x) if np.isfinite(x) else None for x in ratios],
        'eligibility_status': statuses.tolist(), 'twofold_success': success.tolist(), 'winners': winners}


def render_report(result):
    lines = ['# Population trajectory accuracy and cost', '',
        f"**Decision: {result['decision']}.**", '',
        'The target is the finite width-32768, 32-seed quarter-circle reference mean. '
        'It is not a certified infinite-width truth. Errors include reference sampling noise and finite-width bias; '
        'no reference-noise subtraction is made.', '',
        'The primary rule requires both laws eligible, both reference-resolution gates, observed fast/Gaussian '
        'cost ratio at most 0.5, and twofold success in at least 90% of all 1000 paired bootstrap draws. '
        'A draw with either law ineligible counts as failure, with an undefined ratio. K is restricted to 1,2,4,8,16.', '',
        'Complete trajectory cost includes initialization, graph setup, training, evaluation and NPZ serialization. '
        'Dataset loading/imports are shared overhead, not charged per averaged trajectory. Bootstrap costs use '
        'the resampled condition median. Runtime comparisons concern this recorded hardware/protocol.', '',
        'Upstream compact-producer bitwise/Gram verification and the documented IEEE/TF32 check must be '
        'reported separately; this script does not infer those comparisons from successful training artifacts.', '']
    if result.get('stop_reason'):
        lines += [result['stop_reason'], '']
    lines += ['Reference-only width32768 uses the verified split FWHT kernel. Candidate outputs and recorded costs are unchanged; reference runtime is campaign overhead, not a candidate speed measurement.', '']
    failures = result['input_failures']
    lines += ['## Input validity', '', f'{len(failures)} failure(s).']
    lines += [''] + [f'- {x}' for x in failures] if failures else ['All required candidate/reference records and numerical artifact checks passed.']
    lines += ['', '## Reference resolution', '', '| Observable | Reference sampling RMS SE | SE gate | Width difference RMS | Twice combined sampling SE | Width gate |',
              '|---|---:|:---:|---:|---:|:---:|']
    for name, r in result.get('reference_resolution', {}).items():
        if r.get('width_difference_rms') is None:
            delta = bound = 'unavailable'
        else: delta, bound = f"{r['width_difference_rms']:.8g}", f"{r['twice_combined_sampling_se']:.8g}"
        lines.append(f"| {name} | {r['sampling_rms_se']:.8g} | {r['sampling_gate']} | {delta} | {bound} | {r['width_gate']} |")
    lines += ['', 'Sampling SE must be at most 0.0025/3 for each observable. Width stability compares '
              'the independent fast width-16384 candidate mean with the reference. These are resolution diagnostics, '
              'not a bound on unknown reference bias.', '', '## All declared accuracy–cost choices', '',
              '| Law | Width | K | Prediction RMS | Second Gram RMS | Cost (s) | Both ≤0.0025 |',
              '|---|---:|---:|---:|---:|---:|:---:|']
    for point in result.get('points', []):
        lines.append(f"| {point['kind']} | {point['width']} | {point['K']} | {point['prediction_rms']:.8g} | "
                     f"{point['second_gram_rms']:.8g} | {point['cost_seconds']:.6g} | {point['eligible_primary']} |")
    for item in result.get('tolerance_results', []):
        obs, boot = item['observed'], item['bootstrap']
        label = 'Primary' if item['tolerance'] == .0025 else 'Descriptive secondary'
        lines += ['', f"## {label} tolerance {item['tolerance']}", '',
                  f"Observed eligibility: {obs['eligibility_status'][0]}; cost ratio: {obs['ratios'][0]}."]
        for kind in KINDS:
            win = obs['winners'][kind][0]
            lines += [f"- {kind}: " + (f"width {win['width']}, K={win['K']}, cost {win['cost_seconds']:.6g} s, "
                f"prediction RMS {win['prediction_rms']:.8g}, Gram RMS {win['second_gram_rms']:.8g}." if win else 'no eligible choice.')]
        lines += ['', f"Bootstrap twofold successes: {boot['success_draws']}/1000 ({100*boot['success_fraction']:.1f}%).",
                  f"Eligibility categories: {json.dumps(boot['eligibility_counts'], sort_keys=True)}.",
                  f"Ratio quantiles conditional on both laws eligible: {json.dumps(boot['ratio_quantiles_when_both_eligible'], sort_keys=True)}."]
    lines += ['', 'The JSON retains every bootstrap ratio, undefined-ratio category, winning condition, absolute cost '
              'and error. Conditional ratio quantiles omit eligibility failures; the success fraction includes them. '
              'This bootstrap fraction is not a rigorous confidence guarantee. All width/K choices are displayed; '
              'none is claimed globally optimal.', '', '## Timing and reproducibility', '',
              f"Analysis bootstrap seed: {result['bootstrap_seed']}. Shared paired candidate indices and independent "
              'reference indices are reproducible from that seed.', '',
              '| Process directory | Reported total process seconds | Sum complete trajectory seconds | Difference |',
              '|---|---:|---:|---:|']
    for item in result['inventory']:
        lines.append(f"| {item['directory']} | {item.get('elapsed_seconds')} | {item.get('sum_trajectory_seconds')} | {item.get('shared_overhead_seconds')} |")
    lines += ['', 'The difference is the producer-recorded shared process overhead; imports occur before its timer '
              'and require the external process log for end-to-end wall time. Concurrent GPU process totals must '
              'not be interpreted as elapsed campaign wall time.', '',
              'For a fixed reference r, E||xbar-r||² = ||E X-r||² + Var_RMS(X)/16 and E V = Var_RMS(X). '
              'Consequently E[E_K] = ||E X-r||² + Var_RMS(X)/K, the fresh K-run mean-square error. '
              'This is unbiased for squared error over candidate sampling; its square root is not asserted unbiased.', '',
              'A pass supports only this finite numerical population-trajectory comparison. It establishes no '
              'classifier-accuracy advantage, general-purpose architecture benefit, spectrum necessity, ODE limit '
              'or all-time theorem.', '']
    return '\n'.join(lines)


def analyze(candidate_dirs, reference_dirs, bootstrap_seed, allow_oracle_repair=False):
    failures, inventory = [], []
    candidates = load_directories(candidate_dirs, 'candidate', failures, inventory)
    references = load_directories(reference_dirs, 'reference', failures, inventory)
    hashes = {item.get('data_payload_sha256') for item in inventory}
    if len(hashes) != 1 or None in hashes: failures.append('datasets are missing or differ across processes')
    source_sets = [{Path(k).name: v for k, v in item.get('sources', {}).items()} for item in inventory]
    if allow_oracle_repair:
        study = Path(__file__).parent
        common = {'reuse_check.py': digest(study / 'reuse_check.py')}
        allowed = [common | {'fast_training.py': digest(study / producer),
                   'POPULATION_COST_PROTOCOL.md': digest(study / protocol)}
                   for producer, protocol in [('fast_training_v5.py', 'POPULATION_COST_PROTOCOL_V1.md'),
                                               ('fast_training.py', 'POPULATION_COST_PROTOCOL.md')]]
        reference_allowed = common | {
            'fast_training_split_reference.py': digest(study / 'fast_training_split_reference.py'),
            'POPULATION_COST_PROTOCOL.md': digest(study / 'POPULATION_COST_PROTOCOL.md'),
            'POPULATION_COST_SPLIT_REFERENCE_AMENDMENT.md': digest(study / 'POPULATION_COST_SPLIT_REFERENCE_AMENDMENT.md')}
        for item, source in zip(inventory, source_sets):
            valid = source == reference_allowed if item['role'] == 'reference' else source in allowed
            if not valid:
                failures.append(item['directory'] + ': source hashes do not match permitted role-specific frozen sources')
            item['source_version'] = ('reference_only_split_FWHT' if source == reference_allowed else
                'v5_before_oracle_precision_repair' if source == allowed[0] else
                'current_oracle_precision_repair' if source == allowed[1] else 'INVALID')
    elif not source_sets or any(s != source_sets[0] for s in source_sets) or len(source_sets[0]) != 3:
        failures.append('producer/reuse/protocol source hashes are missing or differ across processes')
    else:
        protocol = Path(__file__).with_name('POPULATION_COST_PROTOCOL.md')
        if source_sets[0].get(protocol.name) != digest(protocol): failures.append('recorded protocol hash differs from analyzed protocol')
    for item in inventory:
        rows = [r for r in list(candidates.values()) + list(references.values()) if r['_directory'] == item['directory']]
        times = [r.get('trajectory_seconds', np.nan) for r in rows]
        item['sum_trajectory_seconds'] = float(sum(times)) if all(finite_number(t) for t in times) else None
        item['shared_overhead_seconds'] = (item['elapsed_seconds'] - item['sum_trajectory_seconds']
            if item.get('elapsed_seconds') is not None and item['sum_trajectory_seconds'] is not None else None)
        item['record_count'] = len(rows)
    result = {'protocol_sha256': digest(Path(__file__).with_name('POPULATION_COST_PROTOCOL.md')),
              'analysis_source_sha256': digest(__file__), 'analysis_numpy_version': np.__version__,
              'bootstrap_seed': bootstrap_seed, 'allow_oracle_repair': allow_oracle_repair,
              'input_failures': failures, 'inventory': inventory, 'decision': 'BLOCKED',
              'observables': {k: list(v) for k, v in OBS.items()}, 'reference_resolution': {}, 'points': [],
              'cost_definition': 'K times condition median trajectory_seconds',
              'upstream_validation': 'Separate compact-producer and IEEE/TF32 evidence required.'}
    if not all(('quarter_circle', 32768, s) in references for s in RSEEDS):
        return result
    ref_rows = [references['quarter_circle', 32768, s] for s in RSEEDS]
    reference = load_observables(ref_rows, failures)
    if reference is None: return result
    # The authorized amendment requires resolution gates BEFORE any cost/error curves.
    study = Path(__file__).parent
    verification_path = study.parent.parent / 'data/generated/response_memory_fast_mixing_20261002/population_cost_split_verification01/verification.json'
    verification = read_json(verification_path)
    result['split_verification'] = verification
    if not verification.get('passed'):
        failures.append('split kernel verification did not pass')
    for source, expected in verification.get('source_hashes', {}).items():
        if digest(source) != expected:
            failures.append('source changed after split verification: ' + source)
    widest_keys = [('quarter_circle',16384,seed) for seed in CSEEDS]
    if not all(key in candidates for key in widest_keys): return result
    widest = load_observables([candidates[key] for key in widest_keys], failures)
    if widest is None: return result
    for name in OBS:
        ref_values, wide_values = reference[name], widest[name]
        ref_mean, wide_mean = ref_values.mean(axis=0), wide_values.mean(axis=0)
        ref_variance = float(np.mean(np.sum((ref_values-ref_mean)**2,axis=0)/31))
        wide_variance = float(np.mean(np.sum((wide_values-wide_mean)**2,axis=0)/15))
        se = float(np.sqrt(ref_variance/32))
        difference = float(np.sqrt(np.mean((wide_mean-ref_mean)**2)))
        bound = float(2*np.sqrt(wide_variance/16+ref_variance/32))
        result['reference_resolution'][name] = dict(sample_variance=ref_variance,
            sampling_rms_se=se,sampling_gate=se<=.0025/3,
            width_difference_rms=difference,twice_combined_sampling_se=bound,
            width_gate=difference<=bound)
    del widest
    reference_ok = all(v['sampling_gate'] and v['width_gate'] for v in result['reference_resolution'].values())
    result['gates'] = {'input_validity':not failures,'reference_resolution':reference_ok}
    if failures or not reference_ok:
        result['accuracy_cost_evaluated'] = False
        result['stop_reason'] = 'Input/reference-resolution gate failed; accuracy-cost comparisons were not calculated.'
        return result
    result['accuracy_cost_evaluated'] = True
    rng = np.random.default_rng(bootstrap_seed)
    candidate_indices = rng.integers(0, 16, size=(BOOTSTRAPS, 16))
    reference_indices = rng.integers(0, 32, size=(BOOTSTRAPS, 32))
    cp = np.stack([np.bincount(ix, minlength=16) / 16 for ix in candidate_indices])
    rp = np.stack([np.bincount(ix, minlength=32) / 32 for ix in reference_indices])
    cp = np.vstack([np.full(16, 1/16), cp]); rp = np.vstack([np.full(32, 1/32), rp])
    ref_grams = {name: x @ x.T / x.shape[1] for name, x in reference.items()}
    ref_vars = {name: sample_variance(rp[:1], gram, 32)[0] for name, gram in ref_grams.items()}
    for name, variance in ref_vars.items():
        se = float(np.sqrt(variance / 32))
        result['reference_resolution'][name] = {'sample_variance': float(variance), 'sampling_rms_se': se,
            'sampling_gate': se <= .0025 / 3, 'width_difference_rms': None,
            'twice_combined_sampling_se': None, 'width_gate': False}
    errors, costs, conditions = [], [], []
    for kind in KINDS:
        for width in WIDTHS:
            keys = [(kind, width, s) for s in CSEEDS]
            if not all(key in candidates for key in keys): continue
            rows = [candidates[key] for key in keys]
            x = load_observables(rows, failures)
            if x is None: continue
            error = []
            diagnostics = {}
            for name, values in x.items():
                gram = values @ values.T / values.shape[1]
                cross = values @ reference[name].T / values.shape[1]
                e, variance, distance = error_curves(cp, rp, gram, cross, ref_grams[name])
                error.append(np.sqrt(e))
                diagnostics[name] = {'sample_variance': float(variance[0]), 'squared_mean_reference_distance': float(distance[0])}
                if kind == 'quarter_circle' and width == 16384:
                    gate = result['reference_resolution'][name]
                    gate['width_difference_rms'] = float(np.sqrt(distance[0]))
                    gate['twice_combined_sampling_se'] = float(2*np.sqrt(variance[0]/16 + ref_vars[name]/32))
                    gate['width_gate'] = gate['width_difference_rms'] <= gate['twice_combined_sampling_se']
            errors.append(np.stack(error, axis=-1))
            times = np.array([row['trajectory_seconds'] for row in rows], dtype=float)
            medians = np.r_[np.median(times), np.median(times[candidate_indices], axis=1)]
            costs.append(medians[:, None] * KS)
            conditions.append({'kind': kind, 'width': width, 'seeds': list(CSEEDS),
                'trajectory_seconds': times.tolist(), 'median_trajectory_seconds': float(medians[0]),
                'diagnostics': diagnostics,
                'terminal_motion': {key: [float(row['metrics'][-1][key]) for row in rows]
                    for key in ('first_motion', 'second_motion')}})
            del x
    if not conditions: return result
    errors = np.stack(errors, axis=1); costs = np.stack(costs, axis=1)
    result['conditions'] = conditions
    for ci, condition in enumerate(conditions):
        for ki, count in enumerate(KS):
            result['points'].append({'kind': condition['kind'], 'width': condition['width'], 'K': int(count),
                'prediction_rms': float(errors[0, ci, ki, 0]), 'second_gram_rms': float(errors[0, ci, ki, 1]),
                'cost_seconds': float(costs[0, ci, ki]), 'eligible_primary': bool(np.all(errors[0, ci, ki] <= .0025))})
    result['tolerance_results'] = [{'tolerance': tolerance,
        'observed': comparisons(errors[:1], costs[:1], conditions, tolerance),
        'bootstrap': comparisons(errors[1:], costs[1:], conditions, tolerance)} for tolerance in TOLERANCES]
    primary = result['tolerance_results'][0]
    reference_ok = all(v['sampling_gate'] and v['width_gate'] for v in result['reference_resolution'].values())
    result['gates'] = {'input_validity': not failures, 'reference_resolution': reference_ok,
        'both_methods_eligible': primary['observed']['eligibility_status'][0] == 'both_eligible',
        'observed_twofold': primary['observed']['twofold_success'][0],
        'bootstrap_at_least_90_percent': primary['bootstrap']['success_fraction'] >= .9}
    result['decision'] = ('PASS' if all(result['gates'].values()) else
        'BLOCKED' if failures or not reference_ok else 'FAIL')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--candidate-dirs', nargs='+', type=Path, required=True)
    parser.add_argument('--reference-dirs', nargs='+', type=Path, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--bootstrap-seed', type=int, default=20261002)
    parser.add_argument('--allow-oracle-repair', action='store_true',
                        help='Accept exact original candidate sources and verified reference-only split producer sources by role.')
    args = parser.parse_args()
    if args.out_dir.exists(): parser.error('--out-dir must be new; retained analyses are not overwritten')
    args.out_dir.mkdir(parents=True)
    result = analyze(args.candidate_dirs, args.reference_dirs, args.bootstrap_seed, args.allow_oracle_repair)
    (args.out_dir / 'population_cost.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    (args.out_dir / 'population_cost.md').write_text(render_report(result))
    print(json.dumps({'decision': result['decision'], 'input_failures': len(result['input_failures']),
                      'gates': result.get('gates'), 'report': str(args.out_dir / 'population_cost.md')}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
