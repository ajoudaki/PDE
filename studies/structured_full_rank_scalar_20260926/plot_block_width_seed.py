"""Plot the saved cluster width/seed comparisons; never run training.

Write PNG and vector PDF only in the new width-2048 seed-1 run directory.
Installed ReportLab supplies the renderer; plotting helpers are shared with
the preceding stopping-loss figure.
"""
import argparse
import json
import math
from pathlib import Path

from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, String, Circle, Group, Rect
from reportlab.lib.colors import HexColor

from plot_block_continuation import text, line, axis_top, INK, GRID


TASK = 'cluster_triple_cos9'
BLOCKS = (8, 32, 128)
COLORS = (HexColor('#2563eb'), HexColor('#d95f02'), HexColor('#15803d'))
LABELS = ('n1024 seed0', 'n2048 seed0', 'n2048 seed1')


def load(directory, width, seed):
    manifest = json.loads((directory / 'manifest.json').read_text())
    if (manifest['width'], manifest['seed'], manifest['target_mse']) != (width, seed, .001):
        raise ValueError(f'Unexpected configuration in {directory}')
    rows = json.loads((directory / 'comparisons.json').read_text())
    indexed = {r['method']: r for r in rows if r['task'] == TASK}
    for method in ('gaussian_control', 'hd', 'block8', 'block32', 'block128'):
        row = indexed[method]
        if not math.isfinite(row['rms_vs_gaussian']):
            raise ValueError(f'Invalid comparison: {directory}/{method}')
    return indexed


def plot(baseline, seed0, seed1):
    datasets = (load(baseline, 1024, 0), load(seed0, 2048, 0), load(seed1, 2048, 1))
    methods = ('block8', 'block32', 'block128', 'hd', 'gaussian_control')
    values = [data[method]['rms_vs_gaussian'] for data in datasets
              for method in methods if data[method]['fitted_pair']]
    if not values:
        raise ValueError('No valid matched-target comparisons to plot')
    has_missing = any(not data[method]['fitted_pair'] for data in datasets for method in methods)
    step, count = axis_top(max(values))
    ymax = step * count
    drawing = Drawing(1080, 700)
    drawing.add(Rect(0, 0, 1080, 700, fillColor=HexColor('#ffffff'), strokeColor=None))
    text(drawing, 540, 665, 'Gaussian-block initialization: width and seed check',
         size=20, anchor='middle')
    text(drawing, 540, 639,
         'Cluster triple cos9 | MSE 0.001 | Unrestricted dense canonical training',
         size=12, anchor='middle')
    for panel, (indices, title) in enumerate((((0, 1), 'Width comparison: seed 0'),
                                               ((1, 2), 'Seed comparison: width 2048'))):
        left, bottom, width, height = 85 + panel * 540, 220, 415, 345
        xs = [left + j * width / 2 for j in range(3)]
        ypos = lambda value: bottom + height * value / ymax
        for j in range(count + 1):
            value = j * step
            yy = ypos(value)
            line(drawing, left, yy, left + width, yy, GRID, .7)
            text(drawing, left - 10, yy - 4, f'{value:.3g}', anchor='end')
        line(drawing, left, bottom, left, bottom + height, INK, 1)
        line(drawing, left, bottom, left + width, bottom, INK, 1)
        for xx, k in zip(xs, BLOCKS):
            line(drawing, xx, bottom, xx, bottom - 5, INK, 1)
            text(drawing, xx, bottom - 22, str(k), anchor='middle')
        text(drawing, left + width / 2, bottom - 47, 'Block size k (log scale)', anchor='middle')
        text(drawing, left + width / 2, bottom + height + 21, title,
             size=15, anchor='middle')
        label = Group()
        label.add(String(0, 0, 'Absolute circle RMS vs Gaussian', fontName='Helvetica',
                         fontSize=11, fillColor=INK, textAnchor='middle'))
        label.rotate(90)
        label.translate(bottom + height / 2, -(left - 60))
        drawing.add(label)
        for index in indices:
            data, color = datasets[index], COLORS[index]
            for method, dash in (('hd', [8, 4]), ('gaussian_control', [2, 4])):
                if not data[method]['fitted_pair']:
                    continue
                yy = ypos(data[method]['rms_vs_gaussian'])
                line(drawing, left, yy, left + width, yy, color, 1.6, dash)
            ys = [ypos(data[f'block{k}']['rms_vs_gaussian'])
                  if data[f'block{k}']['fitted_pair'] else None for k in BLOCKS]
            for j in range(2):
                if ys[j] is not None and ys[j+1] is not None:
                    line(drawing, xs[j], ys[j], xs[j+1], ys[j+1], color, 2.3)
            for xx, yy in zip(xs, ys):
                if yy is None:
                    continue
                drawing.add(Circle(xx, yy, 4.3, fillColor=color,
                                   strokeColor=HexColor('#ffffff'), strokeWidth=.7))
            omitted = [str(k) for k in BLOCKS if not data[f'block{k}']['fitted_pair']]
            if omitted:
                text(drawing, left + 10, bottom + height - 17 - 15 * indices.index(index),
                     f'{LABELS[index]}: omitted k=' + ','.join(omitted),
                     size=10, color=color)
    for column, (label, color) in enumerate(zip(LABELS, COLORS)):
        xx = 90 + column * 335
        text(drawing, xx, 132, label, size=12)
        for row, (method, dash) in enumerate((('Blocks', None), ('HD', [8, 4]),
                                             ('Gaussian control', [2, 4]))):
            yy = 112 - row * 23
            line(drawing, xx, yy, xx + 35, yy, color, 2, dash)
            if dash is None:
                drawing.add(Circle(xx + 17.5, yy, 3.5, fillColor=color, strokeColor=None))
            text(drawing, xx + 45, yy - 4, method)
    text(drawing, 540, 24,
         ('Only matched MSE 0.001 pairs shown; budget-limited pairs omitted. One draw per configuration.'
          if has_missing else
          'Gaussian references match width, seed and stopping loss. One draw per method and configuration.'),
         size=11, anchor='middle')
    stem = seed1 / 'block_width_seed'
    renderPDF.drawToFile(drawing, str(stem.with_suffix('.pdf')))
    renderPM.drawToFile(drawing, str(stem.with_suffix('.png')), fmt='PNG', dpi=72)
    return stem


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', required=True, type=Path)
    parser.add_argument('--seed0', required=True, type=Path)
    parser.add_argument('--seed1', required=True, type=Path)
    args = parser.parse_args()
    if not args.seed1.is_dir():
        parser.error('--seed1 must be an existing completed run directory')
    print(plot(args.baseline.resolve(), args.seed0.resolve(), args.seed1.resolve()))
