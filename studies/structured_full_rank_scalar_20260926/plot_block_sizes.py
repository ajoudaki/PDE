"""Plot saved block sizes 8, 16, 32, 64, 128 without running training."""
import argparse
import json
import math
from pathlib import Path

from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, String, Circle, Group, Rect
from reportlab.lib.colors import HexColor

from plot_block_continuation import text, line, axis_top, INK, GRID


TASK = 'cluster_triple_cos9'
BLOCKS = (8, 16, 32, 64, 128)
BLUE = HexColor('#2563eb')
ORANGE = HexColor('#d95f02')
GREEN = HexColor('#15803d')


def plot(baseline, fill):
    manifest = json.loads((baseline / 'manifest.json').read_text())
    if (manifest['width'], manifest['seed'], manifest['target_mse']) != (2048, 1, .001):
        raise ValueError('The baseline must be width2048, seed1, target MSE0.001')
    records = {}
    for directory in (baseline, fill):
        rows = json.loads((directory / 'comparisons.json').read_text())
        records.update({r['method']: r for r in rows if r.get('task', TASK) == TASK})
    methods = tuple(f'block{k}' for k in BLOCKS) + ('hd', 'gaussian_control')
    for method in methods:
        if not math.isfinite(records[method]['rms_vs_gaussian']):
            raise ValueError(f'Nonfinite RMS for {method}')
    values = [records[m]['rms_vs_gaussian'] for m in methods if records[m]['fitted_pair']]
    if not values:
        raise ValueError('No fitted pairs to plot')
    step, count = axis_top(max(values))
    ymax = step * count
    drawing = Drawing(960, 640)
    drawing.add(Rect(0, 0, 960, 640, fillColor=HexColor('#ffffff'), strokeColor=None))
    text(drawing, 480, 606, 'Gaussian-block initialization across block sizes',
         size=20, anchor='middle')
    text(drawing, 480, 579,
         'Cluster triple cos9 | Width 2048 | Seed 1 | MSE 0.001',
         size=12, anchor='middle')
    left, bottom, width, height = 95, 170, 800, 350
    xs = [left + j * width / 4 for j in range(5)]
    ypos = lambda value: bottom + height * value / ymax
    for j in range(count + 1):
        value = j * step
        yy = ypos(value)
        line(drawing, left, yy, left + width, yy, GRID, .7)
        text(drawing, left - 12, yy - 4, f'{value:.3g}', anchor='end')
    line(drawing, left, bottom, left, bottom + height, INK, 1)
    line(drawing, left, bottom, left + width, bottom, INK, 1)
    for xx, k in zip(xs, BLOCKS):
        line(drawing, xx, bottom, xx, bottom - 5, INK, 1)
        text(drawing, xx, bottom - 22, str(k), anchor='middle')
    text(drawing, left + width / 2, bottom - 50, 'Block size k (log2 scale)', anchor='middle')
    label = Group()
    label.add(String(0, 0, 'Absolute circle RMS vs Gaussian', fontName='Helvetica',
                     fontSize=12, fillColor=INK, textAnchor='middle'))
    label.rotate(90)
    label.translate(bottom + height / 2, -(left - 65))
    drawing.add(label)
    for method, color, dash, title in (('hd', ORANGE, [8, 4], 'HD'),
                                      ('gaussian_control', GREEN, [2, 4], 'Gaussian control')):
        if records[method]['fitted_pair']:
            value = records[method]['rms_vs_gaussian']
            yy = ypos(value)
            line(drawing, left, yy, left + width, yy, color, 1.8, dash)
            text(drawing, left + 10, yy + 7, f'{title}: {value:.6f}',
                 color=color)
    ys = [ypos(records[f'block{k}']['rms_vs_gaussian'])
          if records[f'block{k}']['fitted_pair'] else None for k in BLOCKS]
    for j in range(4):
        if ys[j] is not None and ys[j+1] is not None:
            line(drawing, xs[j], ys[j], xs[j+1], ys[j+1], BLUE, 2.5)
    for xx, yy, k in zip(xs, ys, BLOCKS):
        if yy is None:
            continue
        drawing.add(Circle(xx, yy, 4.8, fillColor=BLUE,
                           strokeColor=HexColor('#ffffff'), strokeWidth=.8))
        offset = (11 if records[f'block{k}']['rms_vs_gaussian'] >
                  records['gaussian_control']['rms_vs_gaussian'] else -18)
        text(drawing, xx, yy + offset, f"{records[f'block{k}']['rms_vs_gaussian']:.6f}",
             anchor='middle', color=BLUE)
    for column, (title, color, dash) in enumerate((('Gaussian blocks', BLUE, None),
                                                   ('HD', ORANGE, [8, 4]),
                                                   ('Gaussian control', GREEN, [2, 4]))):
        xx = 100 + column * 280
        line(drawing, xx, 82, xx + 35, 82, color, 2, dash)
        if dash is None:
            drawing.add(Circle(xx + 17.5, 82, 3.5, fillColor=color, strokeColor=None))
        text(drawing, xx + 45, 78, title)
    omitted = [str(k) for k in BLOCKS if not records[f'block{k}']['fitted_pair']]
    note = ('Budget-limited points omitted: k=' + ', '.join(omitted) + '. '
            if omitted else 'New runs only at k=16 and 64; other points reused. ')
    text(drawing, 480, 44, note + 'All shown pairs reached MSE 0.001.',
         size=11, anchor='middle')
    text(drawing, 480, 24,
         'Same fitted Gaussian reference and matched outer weights; one draw per method.',
         size=11, anchor='middle')
    stem = fill / 'block_sizes'
    renderPDF.drawToFile(drawing, str(stem.with_suffix('.pdf')))
    renderPM.drawToFile(drawing, str(stem.with_suffix('.png')), fmt='PNG', dpi=72)
    return stem


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', required=True, type=Path)
    parser.add_argument('--fill', required=True, type=Path)
    args = parser.parse_args()
    if not args.fill.is_dir():
        parser.error('--fill must be an existing run directory')
    print(plot(args.baseline.resolve(), args.fill.resolve()))
