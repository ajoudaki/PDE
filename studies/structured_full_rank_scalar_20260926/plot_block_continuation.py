"""Plot saved before/after block comparisons without running training.

Uses the installed ReportLab renderer; saves PNG and vector PDF in the
continuation directory. Both inputs are comparisons.json files from the
quick comparison driver.
"""
import argparse
import json
import math
from pathlib import Path

from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, Line, String, Circle, Group, Rect
from reportlab.lib.colors import HexColor


TASKS = ('cluster_triple_cos9', 'alternating5')
BLOCKS = (8, 32, 128)
BEFORE = HexColor('#2563eb')
AFTER = HexColor('#d95f02')
INK = HexColor('#172033')
GRID = HexColor('#e2e6ed')


def load(directory):
    rows = json.loads((directory / 'comparisons.json').read_text())
    indexed = {(r['task'], r['method']): r for r in rows}
    for task in TASKS:
        for method in ('gaussian_control', 'hd', 'block8', 'block32', 'block128'):
            row = indexed[task, method]
            if not row['fitted_pair']:
                raise ValueError(f'Unfitted comparison: {task}/{method}')
            if not math.isfinite(row['rms_vs_gaussian']):
                raise ValueError('Nonfinite circle RMS')
    return indexed


def text(drawing, x, y, value, size=11, anchor='start', color=INK):
    drawing.add(String(x, y, value, fontName='Helvetica', fontSize=size,
                       textAnchor=anchor, fillColor=color))


def line(drawing, x1, y1, x2, y2, color, width=1.5, dash=None):
    drawing.add(Line(x1, y1, x2, y2, strokeColor=color,
                     strokeWidth=width, strokeDashArray=dash))


def axis_top(maximum):
    rough = max(maximum, 1e-8) / 5
    power = 10 ** math.floor(math.log10(rough))
    step = next(s * power for s in (1, 2, 2.5, 5, 10) if s * power >= rough)
    count = max(1, math.ceil(maximum * 1.08 / step))
    return step, count


def plot(previous, continuation):
    old, new = load(previous), load(continuation)
    drawing = Drawing(1080, 650)
    drawing.add(Rect(0, 0, 1080, 650, fillColor=HexColor('#ffffff'), strokeColor=None))
    text(drawing, 540, 617, 'Gaussian-block initialization: tighter stopping loss',
         size=20, anchor='middle')
    text(drawing, 540, 591, 'Width 1024 | Same saved trajectories | Dense canonical training',
         size=12, anchor='middle')
    for panel, task in enumerate(TASKS):
        left, bottom, width, height = 85 + panel * 540, 185, 415, 345
        xs = [left + j * width / 2 for j in range(3)]
        values = [data[task, method]['rms_vs_gaussian'] for data in (old, new)
                  for method in ('block8', 'block32', 'block128', 'hd', 'gaussian_control')]
        step, count = axis_top(max(values))
        ymax = step * count
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
        text(drawing, left + width / 2, bottom + height + 19,
             task.replace('_', ' '), size=15, anchor='middle')
        label = Group()
        label.add(String(0, 0, 'Absolute circle RMS vs Gaussian', fontName='Helvetica',
                         fontSize=11, fillColor=INK, textAnchor='middle'))
        label.rotate(90)
        label.translate(bottom + height / 2, -(left - 60))
        drawing.add(label)
        for data, color in ((old, BEFORE), (new, AFTER)):
            for method, dash in (('hd', [8, 4]), ('gaussian_control', [2, 4])):
                yy = ypos(data[task, method]['rms_vs_gaussian'])
                line(drawing, left, yy, left + width, yy, color, 1.6, dash)
            ys = [ypos(data[task, f'block{k}']['rms_vs_gaussian']) for k in BLOCKS]
            for j in range(2):
                line(drawing, xs[j], ys[j], xs[j+1], ys[j+1], color, 2.3)
            for xx, yy in zip(xs, ys):
                drawing.add(Circle(xx, yy, 4.3, fillColor=color,
                                   strokeColor=HexColor('#ffffff'), strokeWidth=.7))
    for row, (color, loss) in enumerate(((BEFORE, '0.01'), (AFTER, '0.001'))):
        yy = 100 - 25 * row
        for column, (label, dash) in enumerate((('Blocks', None), ('HD', [8, 4]),
                                               ('Gaussian control', [2, 4]))):
            xx = 95 + column * 330
            line(drawing, xx, yy, xx + 35, yy, color, 2, dash)
            if dash is None:
                drawing.add(Circle(xx + 17.5, yy, 3.5, fillColor=color, strokeColor=None))
            text(drawing, xx + 45, yy - 4, f'{label}, MSE {loss}')
    text(drawing, 540, 34,
         'Each curve uses the Gaussian reference at its own stopping loss. One draw per method.',
         size=11, anchor='middle')
    stem = continuation / 'block_continuation'
    renderPDF.drawToFile(drawing, str(stem.with_suffix('.pdf')))
    renderPM.drawToFile(drawing, str(stem.with_suffix('.png')), fmt='PNG', dpi=72)
    return stem


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', required=True, type=Path)
    parser.add_argument('--continuation', required=True, type=Path)
    args = parser.parse_args()
    if not args.continuation.is_dir():
        parser.error('--continuation must be an existing completed run directory')
    print(plot(args.previous.resolve(), args.continuation.resolve()))
