"""Plot preserved fitted outputs; performs no fitting or initialization."""
import csv
import hashlib
import json
from pathlib import Path
import numpy as np
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, String, Line
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.lib import colors

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/'data/generated/structured_full_rank_scalar_20260926'
OUT = DATA/'current_correlation_20260930'
TASKS = ['near_pair_sin9', 'cluster_triple_cos9', 'cluster_triple_cos1']


def main():
    dest = OUT/'figure'
    dest.mkdir(exist_ok=False)
    fig = Drawing(1110, 430)
    fig.add(String(555, 404, 'Current-correlation closures: fitted circle outputs',
                   textAnchor='middle', fontSize=17))
    fig.add(String(555, 382, 'Same Gaussian n=1024, seed=1; each model stops at training MSE 0.001',
                   textAnchor='middle', fontSize=11))
    sources, rows = {}, []
    palette = ['#161616', '#168575', '#d98724', '#a83f83']
    for j, task in enumerate(TASKS):
        paths = [DATA/'cubic_feedback_repair_20260930/round2'/f'{task}__bounded.npz',
                 OUT/'focus_projected'/f'{task}__projected.npz',
                 OUT/'focus_gaussian'/f'{task}__gaussian.npz']
        archives = []
        for path in paths:
            sources[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
            with np.load(path) as data:
                archives.append(dict(data))
        dense = archives[0]['dense']
        vals = [dense]+[a['prediction'][:256] for a in archives]
        phase = (archives[0]['angles'][:256]+np.pi) % (2*np.pi)-np.pi
        order = np.argsort(phase)
        angle = np.r_[phase[order], np.pi]
        chart = LinePlot()
        chart.x, chart.y, chart.width, chart.height = 55+j*365, 102, 294, 228
        chart.data = [list(zip(angle, np.r_[v[order], v[order][0]])) for v in vals]
        for k, color in enumerate(palette):
            chart.lines[k].strokeColor = colors.HexColor(color)
            chart.lines[k].strokeWidth = 1.8 if k == 0 else 1.5
        chart.lines[2].strokeDashArray = [5, 2]
        chart.lines[3].strokeDashArray = [2, 2]
        chart.xValueAxis.valueMin, chart.xValueAxis.valueMax = -np.pi, np.pi
        chart.xValueAxis.valueSteps = [-np.pi, 0, np.pi]
        chart.xValueAxis.labelTextFormat = lambda x: '-pi' if x < -1 else ('pi' if x > 1 else '0')
        chart.yValueAxis.maximumTicks = 6
        chart.yValueAxis.visibleGrid = 1
        chart.yValueAxis.gridStrokeColor = colors.HexColor('#e6e6e6')
        fig.add(chart)
        title = ['Close opposite-label pair', 'Oscillating cluster', 'Smooth-label cluster control'][j]
        fig.add(String(chart.x+147, 354, title, textAnchor='middle', fontSize=11))
        errors = [float(np.sqrt(np.mean((v-dense)**2))) for v in vals[1:]]
        fig.add(String(chart.x+147, 337, 'RMS: '+ ' / '.join(f'{e:.4f}' for e in errors),
                       textAnchor='middle', fontSize=10))
        fig.add(String(chart.x+147, 71, 'Circle angle (radians)', textAnchor='middle', fontSize=9))
        for name, error in zip(['bounded_baseline', 'projected', 'gaussian'], errors):
            rows.append(dict(task=task, method=name, circle_rms=error))
    for x, color, label in zip([68, 268, 545, 834], palette,
            ['Dense reference', 'Bounded-Gram baseline', 'Projected gate (A)', 'Gaussian transport (B)']):
        fig.add(Line(x, 27, x+25, 27, strokeColor=colors.HexColor(color), strokeWidth=2))
        fig.add(String(x+31, 23, label, fontSize=10))
    for extension in ['pdf', 'png']:
        path = dest/f'current_correlation_functions.{extension}'
        if extension == 'pdf':
            renderPDF.drawToFile(fig, str(path))
        else:
            renderPM.drawToFile(fig, str(path), fmt='PNG', dpi=96)
    with (dest/'comparison.csv').open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=['task','method','circle_rms'])
        writer.writeheader()
        writer.writerows(rows)
    (dest/'manifest.json').write_text(json.dumps(dict(
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        inputs=sources, outputs={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in dest.iterdir()}), indent=2)+'\n')
    print(dest/'current_correlation_functions.png')


if __name__ == '__main__':
    main()
