"""Compare one newly fitted Gaussian with the two saved matched baselines."""
import argparse
import json
from pathlib import Path
import numpy as np
from run_extra_gaussian import digest, write_json


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--new', required=True)
    p.add_argument('--base', required=True)
    p.add_argument('--output', required=True)
    a = p.parse_args()
    new, base, out = map(Path, (a.new, a.base, a.output))
    out.mkdir(parents=True, exist_ok=False)
    nm = json.loads((new / 'manifest.json').read_text())
    bm = json.loads((base / 'manifest.json').read_text())
    for field in ('width', 'target', 'grid', 'rtol', 'atol'):
        assert nm[field] == bm[field], field
    for core in ('dense_compare.py', 'dense_wide_integrator.py', 'circle_tasks.py'):
        assert nm['sources'][core] == bm['sources'][core], core
    assert nm['outer_seed'] == 0 and nm['middle_seed'] == 1
    assert nm['task'] == 'cluster_triple_cos9'
    predictions, fitting, inputs = {}, {}, {}
    common_angles = None
    sources = [('G1', base / 'cluster_triple_cos9__n8192__s00__gaussian.json'),
               ('G2', base / 'cluster_triple_cos9__n8192__s00__gaussian_control.json'),
               ('G3', new / 'result.json')]
    for label, path in sources:
        rec = json.loads(path.read_text())
        assert rec['status'] == 'ok' and rec['fitted'] and rec['stop_reason'] == 'target'
        assert rec['max_loss_rise'] <= 1e-7
        data = path.parent / rec['data_file']
        assert digest(data) == rec['data_sha256']
        with np.load(data) as z:
            angles = z['angles']
            if common_angles is None:
                common_angles = angles
            assert np.array_equal(common_angles, angles)
            loss = float(np.mean((z['train_prediction'] - z['train_labels']) ** 2))
            assert loss <= 1e-4 * (1 + 1e-7)
            assert abs(loss - rec['train_mse']) <= 1e-12
            predictions[label] = z['prediction']
            assert np.all(np.isfinite(predictions[label]))
        fitting[label] = {'train_mse': loss, 'physical_time': rec['time'],
                          'wall_minutes': rec['wall_seconds'] / 60}
        inputs[str(path)] = digest(path)
        inputs[str(data)] = rec['data_sha256']
    pairs = []
    for left, right in [('G1', 'G2'), ('G3', 'G1'), ('G3', 'G2')]:
        delta = predictions[left] - predictions[right]
        rms = float(np.sqrt(np.mean(delta ** 2)))
        grid = abs(rms - float(np.sqrt(np.mean(delta[::2] ** 2))))
        assert grid <= 1e-4
        pairs.append({'pair': f'{left}-{right}', 'circle_rms': rms, 'grid_delta': grid})
    result = {'width': nm['width'], 'task': nm['task'], 'target': nm['target'],
        'outer_seed': nm['outer_seed'], 'middle_rngs': {'G1': [0, 101], 'G2': [0, 102], 'G3': [1, 101]},
        'metric': 'absolute RMS of circle prediction difference; no amplitude normalization',
        'pairs': pairs, 'fitting': fitting, 'input_hashes': inputs,
        'analysis_source_sha256': digest(__file__),
        'scope': 'Three matched-outer draws; pairwise distances share samples and are not independent replicates.'}
    write_json(out / 'summary.json', result)
    lines = ['# Third Gaussian draw: clustered cosine9, width8192', '',
        'Same outer initialization, three independent Gaussian middle matrices; all train to MSE1e-4.', '',
        '| Pair | Absolute circle-function RMS |', '|---|---:|']
    lines += [f"| {r['pair']} | {r['circle_rms']:.9f} |" for r in pairs]
    lines += ['', 'G1 and G2 are the previously saved reference and control; G3 is the additional middle seed1.',
        'All saved data hashes, training MSEs, loss-monotonicity flags and nested circle quadrature checks pass.',
        result['scope'], 'This checks sensitivity to a third draw; it does not estimate a reliable outlier probability.', '']
    (out / 'report.md').write_text('\n'.join(lines))
    print(json.dumps({'pairs': pairs, 'fitting': fitting}, indent=2))


if __name__ == '__main__':
    main()
