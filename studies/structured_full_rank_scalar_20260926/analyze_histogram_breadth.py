"""Analyze a completed six-task histogram screen; never run training.

Requires the driver's completion marker and verifies saved data/source hashes
before producing summary.csv, report.md and histogram_breadth.{png,pdf}.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, Rect, Circle, PolyLine
from reportlab.lib.colors import HexColor

from plot_block_continuation import text, line, INK, GRID


HIST = HexColor('#2563eb')
REF24 = HexColor('#d95f02')
REF16 = HexColor('#758195')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rms(a, b):
    return float(np.sqrt(np.mean((a-b)**2)))


def _close(actual, saved, name):
    if not np.isclose(actual, saved, atol=2e-12, rtol=2e-10):
        raise ValueError(f'{name}: recomputed {actual} differs from saved {saved}')


def load(directory):
    """Fail closed on incomplete output or a provenance/data mismatch."""
    decision = json.loads((directory/'decision.json').read_text())
    manifest = json.loads((directory/'manifest.json').read_text())
    rows = json.loads((directory/'results.json').read_text())
    tasks = manifest['tasks']
    if (len(tasks) != 6 or len(set(tasks)) != 6
            or decision['completed_tasks'] != 6 or decision['trajectories'] != 18
            or len(rows) != 18):
        raise ValueError('Require the completed six-task, eighteen-trajectory output')
    if manifest['k'] != 1 or manifest['memory_order'] != 1:
        raise ValueError('This report is specifically for the k=1, H=1 closure')
    for filename, expected in manifest['sources'].items():
        if digest(directory/'source_snapshot'/filename) != expected:
            raise ValueError(f'Frozen source hash mismatch: {filename}')
    if digest(directory/'histogram_multi_input.so') != manifest['library_sha256']:
        raise ValueError('Compiled library hash mismatch')
    indexed = {(row['task'], row['method']): row for row in rows}
    expected_keys = {(task, method) for task in tasks
                     for method in ('histogram', 'reference16', 'reference24')}
    if set(indexed) != expected_keys or len(indexed) != len(rows):
        raise ValueError('Missing, duplicate, or unexpected trajectory records')
    arrays = {}
    for key, row in indexed.items():
        path = directory/row['data_file']
        if path.parent != directory or digest(path) != row['data_sha256']:
            raise ValueError(f'Saved trajectory hash mismatch: {key}')
        if json.loads(path.with_suffix('.json').read_text()) != row:
            raise ValueError(f'Sidecar/results record mismatch: {key}')
        with np.load(path, allow_pickle=False) as saved:
            prediction = saved['prediction']
            angles, u, labels = saved['angles'], saved['u'], saved['labels']
            if key[1] == 'histogram':
                train_prediction = saved['train_prediction']
                if int(np.prod(saved['shape']))+1 != row['dynamic_scalars']:
                    raise ValueError(f'Histogram state-count mismatch: {key}')
            else:
                h = np.tanh(saved['w']@u.T)
                S = saved['b'].T@(saved['weights'][:, None]*h)
                H = np.tanh(saved['g'][:, None]*h-(2/len(labels))*(saved['A']@S))
                train_prediction = (saved['weights']*saved['c'])@H
            if (prediction.shape != angles.shape or prediction.ndim != 1
                    or len(prediction) != manifest['test_points']
                    or not np.all(np.isfinite(prediction))):
                raise ValueError(f'Invalid saved circle prediction: {key}')
            _close(float(np.mean((train_prediction-labels)**2)), row['train_mse'],
                   f'{key} training MSE')
            arrays[key] = {'prediction': prediction, 'angles': angles,
                           'u': u, 'labels': labels}
        if row['fitted'] and row['train_mse'] > manifest['target_mse']*(1+1e-7):
            raise ValueError(f'Fitted flag contradicts training MSE: {key}')
    summaries = []
    for task in tasks:
        hist, ref16, ref24 = [indexed[task, method]
                             for method in ('histogram', 'reference16', 'reference24')]
        h, r16, r24 = [arrays[task, method]
                       for method in ('histogram', 'reference16', 'reference24')]
        for candidate in (r16, r24):
            for key in ('angles', 'u', 'labels'):
                if not np.array_equal(h[key], candidate[key]):
                    raise ValueError(f'Unmatched {key} in task {task}')
        error = rms(h['prediction'], r24['prediction'])
        refinement = rms(r16['prediction'], r24['prediction'])
        _close(error, hist['rms_vs_reference24'], f'{task} circle RMS')
        _close(refinement, hist['reference16_vs24_rms'], f'{task} reference refinement')
        both = bool(hist['fitted'] and ref24['fitted'])
        refs_fit = bool(ref16['fitted'] and ref24['fitted'])
        if both != hist['fitted_pair']:
            raise ValueError(f'Fitted-pair flag mismatch: {task}')
        summaries.append({'task': task, 'm': hist['m'],
            'histogram_dynamic_scalars': hist['dynamic_scalars'],
            'histogram_fitted': bool(hist['fitted']),
            'reference24_fitted': bool(ref24['fitted']),
            'reference16_fitted': bool(ref16['fitted']),
            'histogram_train_mse': hist['train_mse'],
            'reference24_train_mse': ref24['train_mse'],
            'reference16_train_mse': ref16['train_mse'],
            'circle_rms_vs_reference24': error,
            'circle_comparison': 'fitted-pair RMS' if both else 'endpoint RMS; partial',
            'reference16_vs24_rms': refinement,
            'reference_comparison': 'fitted-reference refinement' if refs_fit
                                    else 'endpoint gap; reference partial',
            'histogram_training_seconds': hist['training_seconds'],
            'reference24_training_seconds': ref24['training_seconds'],
            'reference16_training_seconds': ref16['training_seconds'],
            'histogram_physical_time': hist['physical_time'],
            'reference24_physical_time': ref24['physical_time'],
            'reference16_physical_time': ref16['physical_time'],
            'histogram_stop_reason': hist['stop_reason'],
            'reference24_stop_reason': ref24['stop_reason'],
            'reference16_stop_reason': ref16['stop_reason'],
            'maximum_cutoff_zone_mass': hist['maximum_taper_zone_mass'],
            'mass': hist['mass'], 'minimum_mass': hist['minimum_mass'],
            'circle_grid_difference': hist['circle_grid_difference'],
            'screen_gates_passed': bool(hist['screen_gates_passed'])})
    return manifest, indexed, arrays, summaries


def plot(directory, manifest, indexed, arrays, summaries):
    drawing = Drawing(1500, 910)
    drawing.add(Rect(0, 0, 1500, 910, fillColor=HexColor('#ffffff'), strokeColor=None))
    text(drawing, 750, 874, 'Six-task Eulerian scalar histogram screen', 23, 'middle')
    text(drawing, 750, 848,
         'k=1, H=1 closure | numerical population references | target training MSE 0.01 | 50 s training budget',
         12, 'middle')
    for j, (label, color, dash) in enumerate((('Histogram', HIST, None),
                                            ('GH24 reference', REF24, None),
                                            ('GH16 reference', REF16, [4, 3]))):
        x = 370+280*j
        line(drawing, x, 821, x+40, 821, color, 2, dash)
        text(drawing, x+50, 817, label, 12)
    for panel, summary in enumerate(summaries):
        task = summary['task']
        column, row = panel % 3, panel // 3
        left, bottom, width, height = 66+column*500, 476-row*350, 400, 215
        sample = arrays[task, 'histogram']
        values = np.concatenate([arrays[task, method]['prediction']
                                 for method in ('histogram', 'reference16', 'reference24')]
                                +[sample['labels']])
        ymin, ymax = float(values.min()), float(values.max())
        span = max(ymax-ymin, .2)
        ymin -= .12*span
        ymax += .12*span
        xpos = lambda x: left+width*x/(2*np.pi)
        ypos = lambda y: bottom+height*(y-ymin)/(ymax-ymin)
        for yy in np.linspace(ymin, ymax, 5):
            line(drawing, left, ypos(yy), left+width, ypos(yy), GRID, .7)
            text(drawing, left-8, ypos(yy)-3, f'{yy:.2g}', 9, 'end')
        for angle, label in ((0., '0'), (np.pi, 'pi'), (2*np.pi, '2pi')):
            line(drawing, xpos(angle), bottom, xpos(angle), bottom-4, INK, .8)
            text(drawing, xpos(angle), bottom-17, label, 10, 'middle')
        line(drawing, left, bottom, left+width, bottom, INK, 1)
        line(drawing, left, bottom, left, bottom+height, INK, 1)
        for method, color, dash, stroke in (
                ('reference16', REF16, [4, 3], 1.2),
                ('reference24', REF24, None, 1.8), ('histogram', HIST, None, 2.)):
            data = arrays[task, method]
            points = []
            for xx, yy in zip(data['angles'], data['prediction']):
                points.extend((xpos(xx), ypos(yy)))
            points.extend((xpos(2*np.pi), ypos(data['prediction'][0])))
            drawing.add(PolyLine(points, strokeColor=color, strokeWidth=stroke,
                                 strokeDashArray=dash, fillColor=None))
        train_angles = np.mod(np.arctan2(sample['u'][:, 1], sample['u'][:, 0]), 2*np.pi)
        for angle, label in zip(train_angles, sample['labels']):
            drawing.add(Circle(xpos(angle), ypos(label), 3.5,
                               fillColor=INK, strokeColor=HexColor('#ffffff'), strokeWidth=.7))
        text(drawing, left+width/2, bottom+height+67, task.replace('_', ' '), 15, 'middle')
        statuses = ', '.join(f'{label}: {"fit" if indexed[task, method]["fitted"] else "PARTIAL"}'
                             for label, method in (('hist', 'histogram'), ('GH24', 'reference24'),
                                                   ('GH16', 'reference16')))
        text(drawing, left+width/2, bottom+height+47, statuses, 10, 'middle')
        error_label = 'Fitted-pair RMS' if summary['circle_comparison']=='fitted-pair RMS' else 'Endpoint RMS'
        text(drawing, left+width/2, bottom+height+28,
             f'{error_label} {summary["circle_rms_vs_reference24"]:.4g}; GH16/24 gap {summary["reference16_vs24_rms"]:.3g}',
             10, 'middle')
        text(drawing, left+width/2, bottom-37,
             f'MSE hist/GH24: {summary["histogram_train_mse"]:.4g} / {summary["reference24_train_mse"]:.4g}',
             10, 'middle')
        text(drawing, left+width/2, bottom-54,
             f'{summary["histogram_dynamic_scalars"]/1e6:.2f}M states; hist {summary["histogram_training_seconds"]:.1f}s; cutoff mass {summary["maximum_cutoff_zone_mass"]:.3g}',
             10, 'middle')
    text(drawing, 750, 41,
         'Dots: training labels. PARTIAL means target not reached; endpoint gaps then compare different stopping conditions.',
         11, 'middle')
    text(drawing, 750, 22,
         'GH16/24 is a numerical refinement check, not a certified error bound. This screen does not compare with dense Gaussian training.',
         11, 'middle')
    stem = directory/'histogram_breadth'
    renderPDF.drawToFile(drawing, str(stem.with_suffix('.pdf')))
    renderPM.drawToFile(drawing, str(stem.with_suffix('.png')), fmt='PNG', dpi=90)


def analyze(directory):
    manifest, indexed, arrays, summaries = load(directory)
    with (directory/'summary.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)
    passed = sum(row['screen_gates_passed'] for row in summaries)
    fitted = sum(row['histogram_fitted'] and row['reference24_fitted'] for row in summaries)
    lines = ['# Six-task scalar histogram breadth screen', '',
        f'{fitted}/6 histogram/GH24 pairs reach training MSE {manifest["target_mse"]:g}; '
        f'{passed}/6 pass all recorded numerical screen gates.', '',
        'Each task uses one fixed-grid Eulerian histogram for the k=1, H=1 closure, '
        'compared with independent moving-characteristic Gaussian quadrature references '
        'at orders 16 and 24. This is not a comparison with the unrestricted dense Gaussian network. '
        'Each trajectory has a 50-second training budget and physical-time cap 100; prediction and saving are outside the training runtime.', '',
        '| Task | States (M) | MSE hist / GH24 | Circle RMS vs GH24 | Comparison | GH16/24 gap | Reference check | Hist / GH24 train s | Max cutoff mass |',
        '|---|---:|---:|---:|---|---:|---|---:|---:|']
    for row in summaries:
        lines.append(f'| {row["task"]} | {row["histogram_dynamic_scalars"]/1e6:.2f} | '
            f'{row["histogram_train_mse"]:.5g} / {row["reference24_train_mse"]:.5g} | '
            f'{row["circle_rms_vs_reference24"]:.5g} | {row["circle_comparison"]} | '
            f'{row["reference16_vs24_rms"]:.5g} | {row["reference_comparison"]} | '
            f'{row["histogram_training_seconds"]:.2f} / {row["reference24_training_seconds"]:.2f} | '
            f'{row["maximum_cutoff_zone_mass"]:.4g} |')
    lines += ['', 'The circle RMS uses 1024 equally spaced angles and GH24 as the primary reference. '
        'A fitted-pair RMS compares endpoints at the common target. An endpoint RMS with a partial '
        'trajectory is a diagnostic at unmatched stopping conditions. The CSV records all fit flags, '
        'stop reasons, physical times, and GH16 runtimes and losses.', '',
        'The GH16/24 gap measures numerical reference sensitivity, not a certified error bound. '
        'If either reference is partial, it also mixes stopping-condition differences and cannot '
        'be interpreted as quadrature uncertainty alone. Maximum cutoff-zone mass is the maximum '
        'across accepted integration checkpoints of mass in the region where boundary transport is tapered.', '',
        'Recorded screen gates require fitted histogram and both references, circle RMS at most 0.01, '
        'GH16/24 gap at most 0.005, 1024/512-circle RMS change at most 0.0001, mass error at most 1e-10, '
        'minimum mass at least -1e-14, and cutoff-zone mass at most 0.001. A failure describes this '
        'fixed-grid, fixed-budget implementation. It does not establish global impossibility of scalar '
        'histograms, rule out other discretizations, or establish a dense-Gaussian approximation.', '',
        '![Six circle comparisons](histogram_breadth.png)', '',
        '[Vector figure](histogram_breadth.pdf) · [Full numerical table](summary.csv)', '',
        f'Provenance verified: all 18 saved NPZ hashes, matching JSON sidecars, '
        f'{len(manifest["sources"])} frozen source hashes, and the compiled library hash. '
        'Training MSE and primary circle discrepancies were recomputed from saved states/predictions.', '',
        f'Manifest SHA256: `{digest(directory/"manifest.json")}`.  ',
        f'Results SHA256: `{digest(directory/"results.json")}`.  ',
        f'Analysis source SHA256: `{digest(Path(__file__).resolve())}`.', '']
    (directory/'report.md').write_text('\n'.join(lines))
    plot(directory, manifest, indexed, arrays, summaries)
    return {'completed_tasks': len(summaries), 'fitted_pairs': fitted,
            'screen_gates_passed': passed, 'output': str(directory)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='Existing completed run_histogram_breadth.py output directory')
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_dir() or not (output/'decision.json').is_file():
        parser.error('--output must name a completed run directory containing decision.json')
    print(json.dumps(analyze(output), indent=2))
