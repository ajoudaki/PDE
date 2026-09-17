"""Finalize the saved tiny simulation without performing any further training.

The original producer completed both ODE integrations and all validity gates,
then failed to import optional matplotlib. This reads its saved CSV/NPZ files,
rechecks observations and draws a static chart with the available Cairo backend.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import shutil

import cairo
import numpy as np
import scipy


def main():
    study = Path(__file__).resolve().parent
    root = study.parent.parent
    out = root/'data/generated/trained_data_response/p2_side_01a09144_tiny_01'
    assert out.exists() and not (out/'summary.json').exists()
    log = Path('/tmp/p2_side_01a09144_sim_stdout.log')
    shutil.copyfile(log, out/'original_run.log')
    shutil.copyfile(__file__, out/Path(__file__).name)
    plan = json.loads((out/'P2_SIDE_01a09144_SIM_PLAN.json').read_text())
    solver_records = [json.loads(line) for line in log.read_text().splitlines()
                      if line.startswith('{')]
    assert len(solver_records) == 2
    tables = []
    for name in ('primary', 'refinement'):
        with (out/(name+'.csv')).open() as f:
            reader = csv.reader(f)
            columns = next(reader)
            tables.append(np.array([[float(v) for v in row] for row in reader]))
    base, fine = tables
    gap = float(np.max(np.abs(base[:, 1:-1]-fine[:, 1:-1])))
    assert gap <= plan['validity']['refinement_max_abs_metric_difference']
    n = plan['model']['width']

    def forward(state):
        w = state[:2*n].reshape(n, 2)
        A = state[2*n:2*n+n*n].reshape(n, n)
        c = state[2*n+n*n:-1]
        h1 = np.tanh(w)
        h2 = np.tanh(A@h1)
        return h1, h2, c@h2/n

    snapshots = np.load(out/'refinement_states.npz')
    h10, h20, f0 = forward(snapshots['states'][:, 0])
    initial_rms = [float(np.sqrt(np.mean(h*h))) for h in (h10, h20)]
    snapshot_error = 0.
    for t, state in zip(snapshots['times'], snapshots['states'].T):
        h1, h2, f = forward(state)
        expected = np.array([np.mean((f-[1., -1.])**2), *f,
                             np.sqrt(np.mean((h1-h10)**2)),
                             np.sqrt(np.mean((h2-h20)**2))])
        row = fine[np.flatnonzero(fine[:, 0] == t)[0]]
        snapshot_error = max(snapshot_error, float(np.max(np.abs(row[1:6]-expected))))
    assert snapshot_error < 1e-12
    for table in tables:
        assert np.isfinite(table).all()
        assert np.max(np.diff(table[:, 1])) <= plan['validity']['sampled_loss_increase_max']
        assert np.max(np.abs(table[:, -1]))/max(1., table[0, 1]) <= plan['validity']['normalized_energy_balance_error_max']

    # Cairo supplies a local vector/raster plotting backend without downloads.
    width, height = 1360, 560
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(1., 1., 1.)
    context.paint()
    context.select_font_face('Sans', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    def text(x, y, value, size=18, color=(.16, .19, .23)):
        context.set_source_rgb(*color)
        context.set_font_size(size)
        context.move_to(x, y)
        context.show_text(value)

    text(70, 40, 'Hidden layers move visibly in this finite reference run', 26)
    text(70, 72, f'Width {n} · seed {plan["seed"]} · numerical physical GF · one initialization', 17)
    panels = [(95, 130, 520, 320), (775, 130, 520, 320)]
    for i, (left, top, pw, ph) in enumerate(panels):
        ymin, ymax = (-16., .1) if i == 0 else (0., .5)
        ticks = [-16., -12., -8., -4., 0.] if i == 0 else [0., .1, .2, .3, .4, .5]

        def point(t, value):
            return left+pw*t/40., top+ph*(1-(value-ymin)/(ymax-ymin))

        for t in [0., 10., 20., 30., 40.]:
            x, _ = point(t, ymin)
            context.set_source_rgb(.88, .90, .92)
            context.set_line_width(1.)
            context.move_to(x, top)
            context.line_to(x, top+ph)
            context.stroke()
            text(x-8, top+ph+28, f'{t:g}', 16)
        for v in ticks:
            _, y = point(0., v)
            context.set_source_rgb(.88, .90, .92)
            context.move_to(left, y)
            context.line_to(left+pw, y)
            context.stroke()
            label = f'1e{int(v)}' if i == 0 else f'{v:.1f}'
            text(left-70, y+5, label, 15)
        text(left, top-20, 'Mean squared training loss' if i == 0 else 'RMS activation change from initialization', 19)
        text(left+160, top+ph+62, 'Physical training time', 18)
        curves = [(np.log10(np.maximum(fine[:, 1], 1e-16)), (.21, .30, .63))] if i == 0 else [
            (fine[:, 4], (.03, .49, .55)), (fine[:, 5], (.79, .36, .21))]
        for values, color in curves:
            context.set_source_rgb(*color)
            context.set_line_width(3.5)
            for j, (t, value) in enumerate(zip(fine[:, 0], values)):
                x, y = point(t, value)
                context.move_to(x, y) if j == 0 else context.line_to(x, y)
            context.stroke()
    text(825, 395, 'Hidden 1: 0.304', 18, (.03, .49, .55))
    text(1045, 395, 'Hidden 2: 0.421', 18, (.79, .36, .21))
    text(95, 547, 'Tighter-tolerance repeat checks the solver; it is not an independent seed or a width-limit test.', 16)
    surface.write_to_png(str(out/'hidden_motion.png'))

    summary = dict(result='VALID_EXPLORATORY_FINITE_RUN',
                   outcome='visible_both_layers_in_this_single_finite_run',
                   width=n, seed=plan['seed'], initial_activation_rms=initial_rms,
                   initial_predictions=f0.tolist(), solver_records=solver_records,
                   refinement_max_absolute_metric_gap=gap,
                   saved_state_observation_error=snapshot_error,
                   final=dict(zip(columns, map(float, fine[-1]))),
                   landmarks=[dict(zip(columns, map(float, fine[np.flatnonzero(fine[:, 0] == t)[0]])))
                              for t in snapshots['times']],
                   original_command='PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 180s python -B studies/trained_data_response/P2_SIDE_01a09144_SIM_RUN.py',
                   original_exit=1,
                   original_failure='Both integrations and scientific validity assertions completed; optional matplotlib import failed before summary/plot creation.',
                   recovery='This finalizer rechecked saved observations and made the plot with Cairo; no further integration was performed.',
                   finalizer_command='python -B studies/trained_data_response/P2_SIDE_01a09144_SIM_FINISH.py',
                   cwd=str(root),
                   environment=dict(python=platform.python_version(), numpy=np.__version__,
                                    scipy=scipy.__version__, cairo=cairo.version,
                                    platform=platform.platform(), training_threads=1),
                   limitations=plan['claim_scope'])
    summary['output_sha256'] = {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in out.iterdir() if p.is_file()}
    (out/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
