"""Overlay saved seed-1 width-1024/2048 block curves; never run training.

Read comparison rows in fill_block_sizes format, validate their saved arrays,
and save PNG plus vector PDF inside the fresh width-1024 run directory.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, Circle, Group, Rect, String
from reportlab.lib.colors import HexColor

from plot_block_continuation import text, line, axis_top, INK, GRID


TASK = 'cluster_triple_cos9'
BLOCKS = (8, 16, 32, 64, 128)
METHODS = ('gaussian_control',) + tuple(f'block{k}' for k in BLOCKS)
COLORS = {1024: HexColor('#2563eb'), 2048: HexColor('#d95f02')}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_curve(directory, width, baseline=None):
    """Validate one fitted curve against its own saved Gaussian reference."""
    manifest = json.loads((directory / 'manifest.json').read_text())
    if (manifest['width'], manifest['seed'], manifest['target_mse']) != (width, 1, .001):
        raise ValueError(f'Expected width {width}, seed 1, target MSE 0.001')
    reference_directory = baseline if baseline is not None else directory
    reference_rows = json.loads((reference_directory / 'results.json').read_text())
    reference_row = next(r for r in reference_rows
                         if r['task'] == TASK and r['method'] == 'gaussian')
    allowed_directories = {directory, reference_directory}

    def arrays(source, row):
        path = source / row['data_file']
        if path.parent != source or digest(path) != row['data_sha256']:
            raise ValueError(f'Invalid data path or hash: {path}')
        metadata = json.loads(path.with_suffix('.json').read_text())
        if (metadata['task'], metadata['method'], metadata['width'], metadata['seed'],
                metadata['target_mse']) != (TASK, row['method'], width, 1, .001):
            raise ValueError(f'Unexpected saved run metadata: {path}')
        if not metadata['fitted'] or metadata['stop_reason'] != 'target':
            raise ValueError(f'Unfitted trajectory: {path}')
        with np.load(path) as saved:
            angles, prediction = saved['angles'], saved['prediction']
            mse = float(np.mean((saved['train_prediction'] - saved['train_labels'])**2))
            if (angles.shape != (2048,) or prediction.shape != angles.shape or
                    not np.all(np.isfinite(prediction)) or
                    not np.isfinite(mse) or mse > .001 * (1 + 1e-7)):
                raise ValueError(f'Invalid predictions or training MSE: {path}')
            if mse != row['train_mse'] or mse != metadata['train_mse']:
                raise ValueError(f'Training MSE changed: {path}')
        return angles, prediction

    angles, reference = arrays(reference_directory, reference_row)
    raw_rows = json.loads((directory / 'comparisons.json').read_text())
    rows = {r['method']: r for r in raw_rows if r.get('task', TASK) == TASK}
    values = {}
    for method in METHODS:
        row = rows[method]
        source = Path(row['source_directory']).resolve()
        if source not in allowed_directories or not row['fitted_pair']:
            raise ValueError(f'Invalid fitted comparison: {method}')
        other_angles, prediction = arrays(source, row)
        if not np.array_equal(other_angles, angles):
            raise ValueError(f'Circle grid changed: {method}')
        error = prediction - reference
        rms = float(np.sqrt(np.mean(error**2)))
        if rms != row['rms_vs_gaussian']:
            raise ValueError(f'Circle RMS changed: {method}')
        values[method] = rms
    return values


def marker(drawing, x, y, width, radius=4.5):
    color = COLORS[width]
    if width == 1024:
        shape = Circle(x, y, radius, fillColor=color,
                       strokeColor=HexColor('#ffffff'), strokeWidth=.8)
    else:
        shape = Rect(x-radius, y-radius, 2*radius, 2*radius,
                     fillColor=color, strokeColor=HexColor('#ffffff'), strokeWidth=.8)
    drawing.add(shape)


def plot(n1024, n2048, baseline2048):
    curves = {1024: load_curve(n1024, 1024),
              2048: load_curve(n2048, 2048, baseline2048)}
    drawing = Drawing(1040, 680)
    drawing.add(Rect(0, 0, 1040, 680, fillColor=HexColor('#ffffff'), strokeColor=None))
    text(drawing, 520, 643, 'Gaussian-block initialization across widths',
         size=21, anchor='middle')
    text(drawing, 520, 615, 'Cluster triple cos9 | Seed 1 | Training MSE 0.001',
         size=13, anchor='middle')
    left, bottom, width, height = 110, 190, 860, 365
    xs = [left + j * width / (len(BLOCKS)-1) for j in range(len(BLOCKS))]
    step, count = axis_top(max(v for values in curves.values() for v in values.values()))
    ymax = step * count
    ypos = lambda value: bottom + height * value / ymax
    for j in range(count + 1):
        value = j * step
        yy = ypos(value)
        line(drawing, left, yy, left + width, yy, GRID, .7)
        text(drawing, left - 13, yy - 4, f'{value:.3g}', size=12, anchor='end')
    line(drawing, left, bottom, left, bottom + height, INK, 1)
    line(drawing, left, bottom, left + width, bottom, INK, 1)
    for xx, k in zip(xs, BLOCKS):
        line(drawing, xx, bottom, xx, bottom - 5, INK, 1)
        text(drawing, xx, bottom - 24, str(k), size=12, anchor='middle')
    text(drawing, left + width/2, bottom - 52, 'Block size k (log2 scale)',
         size=13, anchor='middle')
    label = Group()
    label.add(String(0, 0, 'Absolute circle RMS vs Gaussian', fontName='Helvetica',
                     fontSize=13, fillColor=INK, textAnchor='middle'))
    label.rotate(90)
    label.translate(bottom + height/2, -(left - 71))
    drawing.add(label)
    for n, values in curves.items():
        yy = ypos(values['gaussian_control'])
        line(drawing, left, yy, left + width, yy, COLORS[n], 1.6, [5, 5])
    for n, values in curves.items():
        ys = [ypos(values[f'block{k}']) for k in BLOCKS]
        for j in range(len(BLOCKS)-1):
            line(drawing, xs[j], ys[j], xs[j+1], ys[j+1], COLORS[n], 2.5)
        for xx, yy in zip(xs, ys):
            marker(drawing, xx, yy, n)
    for column, n in enumerate((1024, 2048)):
        xx = 168 + column * 440
        line(drawing, xx, 102, xx + 36, 102, COLORS[n], 2.5)
        marker(drawing, xx + 18, 102, n, 3.8)
        text(drawing, xx + 49, 98, f'n = {n}: Gaussian blocks', size=12)
        line(drawing, xx, 77, xx + 36, 77, COLORS[n], 1.6, [5, 5])
        text(drawing, xx + 49, 73,
             f'n = {n}: Gaussian control ({curves[n]["gaussian_control"]:.5f})', size=12)
    text(drawing, 520, 38,
         'Each width uses its own fitted Gaussian reference. All shown pairs reached MSE 0.001.',
         size=11, anchor='middle')
    text(drawing, 520, 20,
         'One draw per method; matched outer weights within each width. Lines connect sampled block sizes.',
         size=11, anchor='middle')
    stem = n1024 / 'block_width_overlay'
    renderPDF.drawToFile(drawing, str(stem.with_suffix('.pdf')))
    renderPM.drawToFile(drawing, str(stem.with_suffix('.png')), fmt='PNG', dpi=72)
    return stem


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n1024', required=True, type=Path)
    parser.add_argument('--n2048', required=True, type=Path)
    parser.add_argument('--baseline2048', required=True, type=Path)
    args = parser.parse_args()
    for path in (args.n1024, args.n2048, args.baseline2048):
        if not path.is_dir():
            parser.error(f'Expected an existing completed run directory: {path}')
    print(plot(args.n1024.resolve(), args.n2048.resolve(), args.baseline2048.resolve()))
