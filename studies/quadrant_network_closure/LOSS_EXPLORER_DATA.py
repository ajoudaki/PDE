#!/usr/bin/env python3
"""Prepare the existing quadrant runs for a loss-controlled inline plot.

No training or new scientific comparison. Use all saved half-time-unit output
observations, match the MSE of the displayed three-seed mean network, and use
each closure's own output MSE. Interpolate adjacent observations with the unique
convex-combination coefficient attaining the requested loss. Evaluate the mean
of the three frozen NTK flows at its own shared physical time, stopping at the
MSE of that mean prediction. This ensemble convention is explicit and differs
slightly from the earlier endpoint figure's mean per-seed losses/stopping times.

The view supports 0.99 >= loss >= 0.0026, within all saved trajectories. Periodic
cubic interpolation connects the saved 128 passive angles plus training inputs;
NTK uses exact saved cross-kernels at 360 uniform angles plus training inputs.
Checks: loss matching <1e-8, kernel spectral regrouping <1e-6, float32 packing
<1e-6, and endpoint angular interpolation max error <0.001 for the network and
closures, <0.001 for NTK. A held-out-observation check reports temporal
interpolation error (not a rigorous bound). Budget: one CPU pass, no retraining.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline


def packed(a, dtype):
    return base64.b64encode(np.asarray(a, dtype=dtype).tobytes()).decode('ascii')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def match_observations(f, times, indices, labels, target):
    loss = np.mean((f[:, indices] - labels) ** 2, axis=1)
    k = int(np.flatnonzero(loss <= target)[0])
    if k == 0:
        return f[0], times[0]
    a, b = f[k - 1], f[k]
    r, d = a[indices] - labels, b[indices] - a[indices]
    qa, qb, qc = np.mean(d*d), 2*np.mean(r*d), np.mean(r*r) - target
    alpha = 2*qc / (-qb + np.sqrt(max(0., qb*qb - 4*qa*qc))) if qc else 0.
    assert 0 <= alpha <= 1 + 1e-10
    return a + alpha*(b-a), times[k-1] + alpha*(times[k]-times[k-1])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--ntk', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    inputs = np.load(args.run / 'inputs.npz')
    ntk = np.load(args.ntk / 'ntk_predictions.npz')
    labels, times = inputs['labels'], inputs['times']
    theta, selection = np.unique(inputs['panel_theta'], return_index=True)
    indices = np.searchsorted(theta, inputs['train_theta'])
    assert np.array_equal(theta[indices], inputs['train_theta'])
    paths = [args.run / 'inputs.npz', args.ntk / 'ntk_predictions.npz']
    network, dense_network = [], []
    full = {}
    dense = {}
    for seed in [11, 29, 47]:
        path = args.run / f'net_n8192_s{seed}' / 'trajectories.npz'
        paths.append(path)
        z = np.load(path)
        network.append(z['predictions'].astype(float)[:, selection])
        dense_network.append(z['dense_predictions'].astype(float))
    full['actual'] = np.mean(network, axis=0)
    dense['actual'] = np.mean(dense_network, axis=0)
    for n in [1, 3, 5]:
        path = args.run / f'cl_N{n}_base' / 'trajectories.npz'
        paths.append(path)
        z = np.load(path)
        full[f'N{n}'] = z['predictions'][:, selection]
        dense[f'N{n}'] = z['dense_predictions']

    report = {'purpose': 'Interpolation of existing trajectories for interactive loss matching',
              'loss_convention': 'MSE of each displayed prediction; network and NTK are three-seed means at shared times within each ensemble',
              'loss_range': [0.99, 0.0026], 'observations': len(times),
              'panel_angles': len(theta), 'checks': {},
              'source_sha256': digest(Path(__file__).resolve()),
              'input_sha256': {str(p.resolve()): digest(p) for p in paths}}
    targets = np.geomspace(.99, .0026, 101)
    payload = {'theta': np.rad2deg(inputs['dense_theta']).tolist(),
               'panelTheta': np.rad2deg(theta).tolist(),
               'trainTheta': inputs['train_degrees'].tolist(),
               'trainIndices': indices.tolist(), 'labels': labels.tolist(),
               'times': times.tolist(), 'lossRange': [.99, .0026],
               'series': {}, 'provenance': report}
    for key, original in full.items():
        f = original.astype('<f4').astype(float)
        loss = np.mean((f[:, indices] - labels)**2, axis=1)
        assert np.all(np.diff(loss) < 0) and loss[-1] < .0026 < .99 < loss[0]
        packing_error = float(np.max(abs(original-f)))
        assert packing_error < 1e-6
        matched = [match_observations(f, times, indices, labels, x) for x in targets]
        loss_error = max(abs(np.mean((p[indices]-labels)**2)-x) for (p, _), x in zip(matched, targets))
        assert loss_error < 1e-8
        spline = CubicSpline(np.r_[theta, 2*np.pi], np.r_[f[-1], f[-1, 0]], bc_type='periodic')
        gap = spline(inputs['dense_theta']) - dense[key]
        angular_max = float(np.max(abs(gap)))
        assert angular_max < .001
        temporal_errors = []
        for i in range(1, len(times)-1, 2):
            p, _ = match_observations(f[::2], times[::2], indices, labels, loss[i])
            temporal_errors.append([np.sqrt(np.mean((p-f[i])**2)), np.max(abs(p-f[i]))])
        report['checks'][key] = {
            'packing_max_error': packing_error, 'loss_match_max_error': float(loss_error),
            'endpoint_angular_rmse': float(np.sqrt(np.mean(gap**2))),
            'endpoint_angular_max_error': angular_max,
            'held_out_observation_max_rmse_and_pointwise_error': np.max(temporal_errors, axis=0).tolist(),
            'time_at_min_loss': float(matched[-1][1])}
        payload['series'][key] = packed(f, '<f4')

    keep = np.unique(np.r_[ntk['dense_uniform_indices'][::4], ntk['training_indices']])
    train_in_keep = np.searchsorted(keep, ntk['training_indices'])
    rates, residual_modes, initial, modes, eigenvectors, coefficients = [], [], [], [], [], []
    for seed in [11, 29, 47]:
        kernel = ntk[f'kernel_blocks_seed_{seed}'].sum(axis=0)
        values, vectors = np.linalg.eigh(kernel)
        assert values.min() > 0
        f0 = ntk[f'f0_seed_{seed}']
        coeff = vectors.T @ (f0[ntk['training_indices']]-labels)
        rates.append(2*values/len(labels))
        residual_modes.append(vectors*coeff)
        initial.append(f0[keep])
        modes.append((ntk[f'cross_kernel_seed_{seed}'][keep] @ vectors)*(coeff/values))
        eigenvectors.append(vectors)
        coefficients.append(coeff)
    rates, residual_modes, initial, modes = map(np.asarray, (rates, residual_modes, initial, modes))

    def training_prediction(t):
        return labels + np.mean(np.einsum('sij,sj->si', residual_modes, np.exp(-rates*t)), axis=0)

    def kernel_loss(t):
        return np.mean((training_prediction(t)-labels)**2)

    def kernel_stop(target):
        low, high = 0., 100.
        while kernel_loss(high) > target:
            high *= 2
            assert high < 1e12
        for _ in range(70):
            mid = (low+high)/2
            if kernel_loss(mid) > target:
                low = mid
            else:
                high = mid
        return high

    match_errors, regroup_errors, angular_errors = [], [], []
    kernel_times = []
    for target in targets:
        t = kernel_stop(target)
        kernel_times.append(t)
        prediction = np.mean(initial - np.einsum('sij,sj->si', modes, -np.expm1(-rates*t)), axis=0)
        match_errors.append(abs(np.mean((prediction[train_in_keep]-labels)**2)-target))
        direct = []
        for s, seed in enumerate([11, 29, 47]):
            factor = -np.expm1(-rates[s]*t)/(8*rates[s])
            alpha = eigenvectors[s] @ (factor*coefficients[s])
            direct.append(ntk[f'f0_seed_{seed}'] - ntk[f'cross_kernel_seed_{seed}'] @ alpha)
        direct = np.mean(direct, axis=0)
        regroup_errors.append(np.max(abs(prediction-direct[keep])))
        spline = CubicSpline(np.r_[ntk['dense_theta'][keep], 2*np.pi],
                             np.r_[prediction, prediction[0]], bc_type='periodic')
        angular_errors.append(np.max(abs(spline(ntk['dense_theta'])-direct)))
    assert max(match_errors) < 1e-8
    assert max(regroup_errors) < 1e-6
    assert max(angular_errors) < .001
    scan_losses = [kernel_loss(t) for t in np.r_[0., np.geomspace(1e-6, max(kernel_times), 1000)]]
    assert np.max(np.diff(scan_losses)) <= 1e-13
    report['checks']['NTK'] = {'loss_match_max_error': float(max(match_errors)),
                                'spectral_regroup_max_error': float(max(regroup_errors)),
                                'angular_max_error': float(max(angular_errors)),
                                'time_at_min_loss': float(kernel_times[-1]),
                                'sampled_mean_loss_monotone': True}
    payload['ntk'] = {'theta': np.rad2deg(ntk['dense_theta'][keep]).tolist(),
                      'rates': rates.tolist(), 'trainIndices': train_in_keep.tolist(),
                      'residualModes': packed(residual_modes, '<f8'),
                      'initial': packed(initial, '<f8'), 'modes': packed(modes, '<f8')}
    (args.out/'data.json').write_text(json.dumps(payload, separators=(',', ':')))
    (args.out/'checks.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'bytes': (args.out/'data.json').stat().st_size, 'checks': report['checks']}, indent=2))


if __name__ == '__main__':
    main()
