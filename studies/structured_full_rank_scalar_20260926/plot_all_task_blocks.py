"""Audit and plot the bounded all-circle-task block comparison; no training.

Saved predictions supply every MSE/RMS calculation. Only two predetermined
states are forwarded again, on four circle points and their training inputs.
The plot includes fitted pairs only and labels unavailable comparisons.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import zipfile

import numpy as np
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, Circle, Rect
from reportlab.lib.colors import HexColor

import dense_compare as dense
from circle_tasks import TASKS, directions
from plot_block_continuation import text, line, axis_top, INK, GRID


BLOCKS = (8, 16, 32)
METHODS = ('gaussian', 'gaussian_control', 'block8', 'block16', 'block32')
WIDTH, SEED, TARGET, CIRCLE_GRID = 2048, 1, .01, 2048
BLUE, ORANGE, RED = map(HexColor, ('#2563eb', '#cf680c', '#b42318'))
SPOTCHECKS = ((TASKS[0].name, 'gaussian'), (TASKS[-1].name, 'block32'))
SPOT_INDICES = np.asarray([0, 137, 1024, 1901])


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def close(actual, expected, message, *, atol=1e-14):
    require(math.isfinite(actual) and math.isfinite(expected) and
            math.isclose(actual, expected, rel_tol=1e-12, abs_tol=atol), message)


def array_header(archive, name):
    """Inspect a saved weight's shape/dtype without loading its dense payload."""
    with archive.open(name + '.npy') as stream:
        version = np.lib.format.read_magic(stream)
        require(version in ((1, 0), (2, 0)), f'Unsupported NPY version: {version}')
        read = (np.lib.format.read_array_header_1_0 if version == (1, 0)
                else np.lib.format.read_array_header_2_0)
        shape, _, dtype = read(stream)
    return shape, dtype


def audit(directory):
    manifest = json.loads((directory / 'manifest.json').read_text())
    require((manifest['width'], manifest['seed'], manifest['target_mse']) ==
            (WIDTH, SEED, TARGET), 'Unexpected width, seed, or target MSE')
    require(manifest['tasks'] == [task.name for task in TASKS],
            'The manifest must contain all circle tasks in their declared order')
    require(tuple(manifest['methods']) == METHODS, 'Unexpected method set/order')
    require(manifest['grid'] == CIRCLE_GRID, 'Unexpected circle grid')
    require(manifest['blas_threads'] == 1, 'Expected one BLAS thread')
    require((manifest['deadline_seconds'], manifest['interrupt_seconds'],
             manifest['per_run_ceiling_seconds']) == (50, 55, 60),
            'Unexpected training deadlines')
    require((manifest['rtol'], manifest['atol']) == (1e-5, 1e-8),
            'Unexpected solver tolerance')
    source_hashes = {}
    source = Path(__file__).resolve().parent
    for name, expected in manifest['sources'].items():
        require(Path(name).name == name, f'Unexpected source path: {name}')
        frozen = directory / 'source_snapshot' / name
        require(digest(frozen) == expected, f'Frozen source hash mismatch: {name}')
        require(digest(source / name) == expected, f'Current source changed: {name}')
        source_hashes[name] = expected

    raw_rows = json.loads((directory / 'results.json').read_text())
    rows = {(row['task'], row['method']): row for row in raw_rows}
    require(len(rows) == len(raw_rows), 'Duplicate result keys')
    expected_keys = {(task.name, method) for task in TASKS for method in METHODS}
    require(set(rows) <= expected_keys, 'Unexpected result key')
    saved, checks, missing = {}, [], []
    expected_angles = 2 * np.pi * np.arange(CIRCLE_GRID) / CIRCLE_GRID
    for task in TASKS:
        for method in METHODS:
            key = task.name, method
            row = rows.get(key)
            if row is None or not row.get('data_file'):
                require(row is None or not row.get('fitted'),
                        f'A missing checkpoint cannot be fitted: {key}')
                missing.append({'task': task.name, 'method': method})
                continue
            path = directory / row['data_file']
            require(path.parent == directory and path.suffix == '.npz',
                    f'Unexpected data path: {path}')
            require(digest(path) == row['data_sha256'], f'Data hash mismatch: {key}')
            metadata = json.loads(path.with_suffix('.json').read_text())
            for field in ('task', 'method', 'width', 'seed', 'target_mse', 'fitted',
                          'stop_reason', 'train_mse', 'data_file', 'data_sha256'):
                require(metadata[field] == row[field],
                        f'Result/metadata mismatch: {key}/{field}')
            require((row['width'], row['seed'], row['target_mse']) ==
                    (WIDTH, SEED, TARGET), f'Unexpected run metadata: {key}')
            require(row['block_size'] == (int(method[5:]) if method.startswith('block')
                                           else None), f'Unexpected block size: {key}')
            with zipfile.ZipFile(path) as archive:
                for name, shape in (('w', (WIDTH, 2)), ('W', (WIDTH, WIDTH)),
                                    ('c', (WIDTH,))):
                    require(array_header(archive, name) == (shape, np.dtype('float64')),
                            f'Unexpected weight shape/dtype: {key}/{name}')
            with np.load(path, allow_pickle=False) as arrays:
                require(set(arrays.files) == {'angles', 'prediction', 'train_angles',
                        'train_labels', 'train_prediction', 'history', 'w', 'W', 'c'},
                        f'Unexpected saved array schema: {key}')
                require(np.array_equal(arrays['angles'], expected_angles),
                        f'Circle grid mismatch: {key}')
                require(np.array_equal(arrays['train_angles'], task.angles),
                        f'Training angles mismatch: {key}')
                require(np.array_equal(arrays['train_labels'], task.target(task.angles)),
                        f'Training labels mismatch: {key}')
                prediction = arrays['prediction']
                train_prediction = arrays['train_prediction']
                require(prediction.shape == (CIRCLE_GRID,) and
                        train_prediction.shape == (len(task.angles),) and
                        np.all(np.isfinite(prediction)) and
                        np.all(np.isfinite(train_prediction)),
                        f'Invalid saved predictions: {key}')
                mse = float(np.mean((train_prediction - arrays['train_labels']) ** 2))
                require(mse == row['train_mse'], f'Saved training MSE mismatch: {key}')
                fitted = row['stop_reason'] == 'target' and mse <= TARGET * (1 + 1e-7)
                require(row['fitted'] == fitted, f'Incorrect fitted flag: {key}')
                history = arrays['history']
                if history.size:
                    require(history.ndim == 2 and history.shape[1] == 2 and
                            np.all(np.isfinite(history)) and
                            np.all(np.diff(history[:, 0]) > 0),
                            f'Invalid accepted-state history: {key}')
                    close(float(history[-1, 0]), row['physical_time'],
                          f'Final history time mismatch: {key}')
                    close(float(history[-1, 1]), mse,
                          f'Final history MSE mismatch: {key}')
                saved[key] = prediction
                if key in SPOTCHECKS:
                    state = dense.State(arrays['w'], arrays['W'], arrays['c'])
                    checked = dense.forward(state, directions(expected_angles[SPOT_INDICES])).output
                    checked_train = dense._forward(state, task.data()[0]).output
                    circle_difference = float(np.max(np.abs(checked - prediction[SPOT_INDICES])))
                    train_difference = float(np.max(np.abs(checked_train - train_prediction)))
                    require(circle_difference <= 1e-12 and train_difference <= 1e-12,
                            f'Weight-forward spotcheck failed: {key}')
                    checks.append({'task': task.name, 'method': method,
                        'circle_indices': SPOT_INDICES.tolist(),
                        'max_circle_absolute_difference': circle_difference,
                        'max_training_absolute_difference': train_difference})

    raw_comparisons = json.loads((directory / 'comparisons.json').read_text())
    comparisons = {(row['task'], row['method']): row for row in raw_comparisons}
    require(len(comparisons) == len(raw_comparisons), 'Duplicate comparison keys')
    require(set(comparisons) <= expected_keys, 'Unexpected comparison key')
    values, quadrature_changes = {}, []
    for task in TASKS:
        reference_key = task.name, 'gaussian'
        reference = saved.get(reference_key)
        for method in METHODS[1:]:
            key = task.name, method
            row, comparison = rows.get(key), comparisons.get(key)
            fitted = bool(row and rows.get(reference_key) and row.get('fitted') and
                          rows[reference_key].get('fitted') and key in saved and
                          reference is not None)
            if comparison is not None:
                require(bool(comparison['fitted_pair']) == fitted,
                        f'Incorrect comparison fitted flag: {key}')
                require(row is not None, f'Comparison without a result: {key}')
                for field in ('data_file', 'data_sha256', 'train_mse'):
                    require(comparison[field] == row[field],
                            f'Comparison/result mismatch: {key}/{field}')
                require(Path(comparison['source_directory']).resolve() == directory,
                        f'Unexpected comparison source directory: {key}')
                require(comparison['reference_train_mse'] == rows[reference_key]['train_mse'],
                        f'Unexpected reference training MSE: {key}')
            if reference is not None and key in saved:
                require(comparison is not None, f'Missing saved comparison: {key}')
                difference = saved[key] - reference
                rms = float(np.sqrt(np.mean(difference ** 2)))
                quadrature = abs(rms - float(np.sqrt(np.mean(difference[::2] ** 2))))
                require(rms == comparison['rms_vs_gaussian'], f'RMS mismatch: {key}')
                close(quadrature, comparison['quadrature_change'],
                      f'Quadrature diagnostic mismatch: {key}')
                quadrature_changes.append(quadrature)
                values[key] = rms if fitted else None
            else:
                require(not fitted, f'Missing fitted arrays: {key}')
                values[key] = None
    present = [row for row in rows.values() if row.get('data_file')]
    result = {'status': 'passed', 'expected_runs': len(expected_keys),
        'saved_runs': len(saved), 'fitted_runs': sum(bool(r.get('fitted')) for r in present),
        'fitted_block_pairs': sum(values[t.name, f'block{k}'] is not None
                                  for t in TASKS for k in BLOCKS),
        'fitted_control_pairs': sum(values[t.name, 'gaussian_control'] is not None for t in TASKS),
        'missing_checkpoints': missing, 'source_sha256': source_hashes,
        'plot_source_sha256': digest(Path(__file__).resolve()),
        'nonfitted_runs': [{field: row[field] for field in
            ('task', 'method', 'train_mse', 'stop_reason', 'physical_time',
             'training_seconds', 'total_seconds')} for row in present if not row['fitted']],
        'spotcheck_rule': 'First declared task/Gaussian and last declared task/block32; '
                          'circle indices 0,137,1024,1901 and each full training set; atol 1e-12.',
        'weight_forward_spotchecks': checks,
        'max_saved_total_seconds': max((r['total_seconds'] for r in present), default=None),
        'max_training_seconds': max((r['training_seconds'] for r in present), default=None),
        'max_loss_rise': max((r['max_loss_rise'] for r in present), default=None),
        'max_quadrature_change': max(quadrature_changes, default=None),
        'validation_scope': 'All source/data hashes, schemas, circle/training grids, labels, '
            'saved-output training MSEs, fitted flags and nonreference circle RMSs checked. '
            'All dense weight shapes/dtypes inspected; two predetermined saved states '
            'checked for finite weights and forwarded on sparse inputs. No solver refinement.'}
    if (directory / 'completion.json').is_file():
        completion = json.loads((directory / 'completion.json').read_text())
        require(completion['new_trajectories'] == len(rows), 'Completion run-count mismatch')
        require(completion['fitted_trajectories'] == result['fitted_runs'],
                'Completion fitted-count mismatch')
        require(completion['all_fitted'] == all(r.get('fitted') for r in rows.values()),
                'Completion all-fitted flag mismatch')
        require(completion['max_new_run_seconds'] == result['max_saved_total_seconds'],
                'Completion timing mismatch')
        close(completion['max_quadrature_change'], result['max_quadrature_change'],
              'Completion quadrature diagnostic mismatch')
    return rows, values, result


def plot(directory, rows, values):
    drawing = Drawing(1200, 1380)
    drawing.add(Rect(0, 0, 1200, 1380, fillColor=HexColor('#ffffff'), strokeColor=None))
    text(drawing, 600, 1348, 'Gaussian-block initialization across all circle tasks',
         size=22, anchor='middle')
    text(drawing, 600, 1322, 'n = 2048 | Training MSE = 0.01 | Seed 1 | 2048 circle angles',
         size=13, anchor='middle')
    text(drawing, 600, 1301, 'Absolute RMS difference from each task\'s Gaussian reference; independent linear y scales',
         size=11, anchor='middle')
    for index, task in enumerate(TASKS):
        col, row_number = index % 3, index // 3
        left, top, width, height = 65 + 398 * col, 1249 - 289 * row_number, 290, 193
        bottom = top - height
        xs = [left + j * width / 2 for j in range(3)]
        text(drawing, left + width / 2, top + 25, task.name.replace('_', ' '),
             size=14, anchor='middle')
        text(drawing, left, top + 7, 'RMS (linear)', size=9)
        available = [values[task.name, method] for method in METHODS[1:]
                     if values[task.name, method] is not None]
        if available:
            step, count = axis_top(max(available))
            ymax = step * count
            ypos = lambda value: bottom + height * value / ymax
            for j in range(count + 1):
                value = j * step
                yy = ypos(value)
                line(drawing, left, yy, left + width, yy, GRID, .65)
                text(drawing, left - 9, yy - 3, f'{value:.3g}', size=9, anchor='end')
            control = values[task.name, 'gaussian_control']
            if control is not None:
                yy = ypos(control)
                line(drawing, left, yy, left + width, yy, ORANGE, 1.5, [5, 4])
            ys = [None if values[task.name, f'block{k}'] is None else
                  ypos(values[task.name, f'block{k}']) for k in BLOCKS]
            for j in range(2):
                if ys[j] is not None and ys[j + 1] is not None:
                    line(drawing, xs[j], ys[j], xs[j + 1], ys[j + 1], BLUE, 2)
            for xx, yy in zip(xs, ys):
                if yy is not None:
                    drawing.add(Circle(xx, yy, 3.8, fillColor=BLUE,
                                       strokeColor=HexColor('#ffffff'), strokeWidth=.6))
        else:
            reference = rows.get((task.name, 'gaussian'))
            message = ('Gaussian reference missing' if reference is None else
                       'Gaussian reference not fitted' if not reference.get('fitted')
                       else 'No fitted comparison')
            text(drawing, left + width / 2, bottom + height / 2,
                 message, size=12, anchor='middle', color=RED)
        line(drawing, left, bottom, left, top, INK, .9)
        line(drawing, left, bottom, left + width, bottom, INK, .9)
        for xx, k in zip(xs, BLOCKS):
            line(drawing, xx, bottom, xx, bottom - 4, INK, .9)
            text(drawing, xx, bottom - 18, str(k), size=10, anchor='middle')
        text(drawing, left + width / 2, bottom - 35, 'Block size k (log2 scale)',
             size=10, anchor='middle')
        excluded = [f'k={k}' for k in BLOCKS if values[task.name, f'block{k}'] is None]
        if values[task.name, 'gaussian_control'] is None:
            excluded.append('control')
        if excluded:
            text(drawing, left + width / 2, bottom - 52,
                 'Excluded / not fitted: ' + ', '.join(excluded),
                 size=8.5, anchor='middle', color=RED)
    line(drawing, 243, 101, 282, 101, BLUE, 2)
    drawing.add(Circle(262.5, 101, 3.8, fillColor=BLUE, strokeColor=None))
    text(drawing, 293, 97, 'Gaussian blocks: k = 8, 16, 32', size=12)
    line(drawing, 660, 101, 700, 101, ORANGE, 1.5, [5, 4])
    text(drawing, 711, 97, 'Independent Gaussian middle matrix', size=12)
    text(drawing, 600, 66, 'Unrestricted dense training; outer weights matched at initialization. One draw per method.',
         size=11, anchor='middle')
    text(drawing, 600, 45, 'Only pairs reaching the common training-MSE target are plotted. Lines connect sampled block sizes.',
         size=11, anchor='middle')
    stem = directory / 'all_task_block_curves'
    renderPDF.drawToFile(drawing, str(stem.with_suffix('.pdf')))
    renderPM.drawToFile(drawing, str(stem.with_suffix('.png')), fmt='PNG', dpi=72)
    return stem


def write_summary(directory, rows, values, result, report):
    table = []
    for task in TASKS:
        row = {'task': task.name}
        for method in METHODS[1:]:
            row[f'{method}_rms'] = values[task.name, method]
        for method in METHODS:
            saved = rows.get((task.name, method), {})
            row[f'{method}_mse'] = saved.get('train_mse')
            row[f'{method}_status'] = saved.get('stop_reason', 'missing')
        table.append(row)
    with (directory / 'all_task_summary.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(table[0]))
        writer.writeheader()
        writer.writerows(table)
    (directory / 'plot_audit.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    lines = ['# All-circle-task block comparison: internal data check', '',
        f"The saved run contains {result['saved_runs']}/{result['expected_runs']} checkpoints; "
        f"{result['fitted_runs']} reached training MSE 0.01. The plot includes "
        f"{result['fitted_block_pairs']}/36 fitted block/reference pairs and "
        f"{result['fitted_control_pairs']}/12 fitted control/reference pairs.", '',
        'Width 2048, seed 1, all 12 declared circle tasks, blocks 8/16/32. '
        'Each method uses its own first refined MSE-0.01 crossing and is compared '
        'with the Gaussian reference for the same task. These are different '
        'physical stopping times. The Gaussian control changes only the initial '
        'middle matrix; outer weights are matched. Every middle matrix is trained '
        'without a block restriction.', '',
        '| Task | k = 8 RMS | k = 16 RMS | k = 32 RMS | Gaussian-control RMS |',
        '|---|---:|---:|---:|---:|']
    for task in TASKS:
        numeric = [values[task.name, method] for method in
                   ('block8', 'block16', 'block32', 'gaussian_control')]
        cells = ['excluded' if value is None else f'{value:.7f}' for value in numeric]
        lines.append('| ' + task.name + ' | ' + ' | '.join(cells) + ' |')
    if result['nonfitted_runs']:
        lines += ['', 'The following saved runs did not reach the target. '
            'When a task\'s Gaussian reference is nonfitted, all its comparison '
            'pairs are excluded, including any fitted candidate. These checkpoints '
            'are retained; no extension or rerun is included.', '',
            '| Task | Method | Partial training MSE | Stop reason |',
            '|---|---|---:|---|']
        for partial in result['nonfitted_runs']:
            lines.append(f"| {partial['task']} | {partial['method']} | "
                         f"{partial['train_mse']:.8f} | {partial['stop_reason']} |")
    lines += ['', 'RMS means the unnormalized root mean square of the difference '
        'between saved trained functions over 2048 uniform circle angles. '
        'The figure uses a separate linear y scale in each panel and a log2 x scale. '
        'A missing or nonfitted member excludes the corresponding pair; raw partial '
        'results remain in the run directory.', '',
        '**Internal audit:** ' + result['validation_scope'], '',
        f"Maximum 2048-versus-1024-grid RMS change: {result['max_quadrature_change']:.3g}. "
        f"Maximum saved training time: {result['max_training_seconds']:.3f} s; "
        f"maximum saved total time: {result['max_saved_total_seconds']:.3f} s. "
        f"Maximum recorded accepted-step loss rise: {result['max_loss_rise']:.3g}.", '',
        'The sparse weight-forward check was fixed before run completion: '
        + result['spotcheck_rule'], '']
    for check in result['weight_forward_spotchecks']:
        lines.append(f"- `{check['task']}/{check['method']}`: maximum circle difference "
            f"{check['max_circle_absolute_difference']:.3g}; maximum training-output "
            f"difference {check['max_training_absolute_difference']:.3g}.")
    lines += ['', 'This check verifies saved data and plotting consistency. It does '
        'not certify global integration error. One seed, one width and three block '
        'sizes do not establish a convergence rate or a population limit; MSE 0.01 '
        'is a finite-loss endpoint. This remains study-local evidence, without '
        'independent promotion review.', '', f'Run directory: `{directory}`.', '',
        'Outputs: `all_task_block_curves.png`, `all_task_block_curves.pdf`, '
        '`all_task_summary.csv`, `plot_audit.json`.']
    report.write_text('\n'.join(lines) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', required=True, type=Path)
    parser.add_argument('--report', type=Path,
                        default=Path(__file__).with_name('QUICK_ALL_TASK_BLOCK_CHECK.md'))
    args = parser.parse_args()
    directory = args.directory.resolve()
    rows, values, result = audit(directory)
    stem = plot(directory, rows, values)
    write_summary(directory, rows, values, result, args.report.resolve())
    print(json.dumps({'figure': str(stem.with_suffix('.png')), **result}, indent=2))


if __name__ == '__main__':
    main()
