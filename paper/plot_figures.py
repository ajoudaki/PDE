#!/usr/bin/env python3
"""Render the selected paper inventory from saved inputs, never from training.

No arguments renders all figures into a fresh, study-owned output directory.
Use --list, --check, --only NAME..., or --out DIR. --export-data DIR packages
the plotting inputs; --data-dir DIR subsequently renders from that package.
Every figure is drawn with Matplotlib in one shared style (below): a method
keeps one colour and marker everywhere, baselines stay grey, and curves are
labelled directly. Needs NumPy, Matplotlib, SciPy and threadpoolctl; no
PyTorch, GPU or LaTeX.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / 'paper'
STUDY_DATA = ROOT / 'data/generated/paper_appendix_pilots_20261009'
INPUTS = {
    'response': PAPER / 'figures/response_memory_source.npz',
    'radial': PAPER / 'figures/radial_source_data.npz',
    'sphere': PAPER / 'figures/sphere_source_data.npz',
    'moments': STUDY_DATA / 'plotting_inputs/moments.npz',
    'storage': STUDY_DATA / 'mean_task_comparison/metrics.json',
    'accuracy': STUDY_DATA / 'figure3_paired_seeds/figures_final/metrics.json',
    'trajectory': STUDY_DATA / 'figure4_three_seeds/figures_raw_rms/metrics.json',
    'spectra': STUDY_DATA / 'feedback/figures/appendix_saved_metrics.json',
    'query_distance': STUDY_DATA / 'feedback/scope/report.json',
    'fixed_budget': STUDY_DATA / 'refresh_20261010/fixed_budget_final/metrics.json',
    'robustness': STUDY_DATA / 'refresh_20261010/robustness/metrics.json',
    'scope': STUDY_DATA / 'refresh_20261010/scope/metrics.json',
    'costs': STUDY_DATA / 'refresh_20261010/costs_final/metrics.json',
    'dense_pairs_sphere': STUDY_DATA / 'feedback/pairs_sphere3/report.json',
    'dense_pairs_mnist': STUDY_DATA / 'feedback/pairs_mnist/report.json',
}

# id: (input key, renderer, placement, caption). None denotes a schematic.
FIGURES = {
    'radial_trajectory': ('response', 'draw_radial_trajectory', 'main',
        'Earlier Legendre circle experiment: two tanh hidden layers, width 2048, '
        'orders 1/3/7 at common physical times 0/5/20/80. Radius is 3 + signed '
        'prediction. The saved replay has 39 checkpoints and two Heun tolerances; '
        'these snapshots are not a continuous-time certificate.'),
    'storage': ('storage', 'draw_storage', 'main',
        'Three-seed mean learned storage of smallest TESTED passing models. '
        'Pass means maximum-recorded query RMS <= the paired dense maximum, '
        'not pointwise ratios or an extra endpoint gate. Fits are descriptive; '
        'fixed storage and full-horizon source setup are additional.'),
    'accuracy': ('accuracy', 'draw_accuracy', 'main',
        'Endpoint query RMS versus learned storage. Compressions have three '
        'fresh coupled repetitions; small-dense/low-rank controls retain their '
        'original-reference protocol. Sphere dense bars are median/range; other '
        'paired bars are mean/sample SD. Missing Taylor budget remains missing. '
        'Hollow markers are inputs withheld from setup. Fixed storage is additional.'),
    'trajectory': ('trajectory', 'draw_trajectory', 'main',
        'Selected fixed-data Figure 4: three independent coupled repetitions, '
        'mean raw query RMS and dotted dense-pair error. Only declared inputs and '
        'recorded positive times are shown. Sources use full-horizon rollout.'),
    'moments': ('moments', 'draw_moments', 'methods',
        'Cached deterministic small-network illustration of history reconstruction '
        'by one, two and three Legendre coefficients. Median errors are normalized '
        'by each neuron\'s history range. This older nonzero-readout example is '
        'illustrative, not validation of the canonical initialization theorem.'),
    'spectra': ('spectra', 'draw_spectra', 'appendix',
        'Actual saved dense-history spectra and reconstruction ranks at five widths. '
        'The mandatory initial span is additional. Single-seed reconstruction '
        'evidence, not a prediction-error or asymptotic-rate guarantee.'),
    'query_distance': ('query_distance', 'draw_query_distance', 'appendix',
        'Endpoint RMS along six fixed geodesic paths away from declared inputs. '
        'One seed, ambient dimension 10, toy target depending on three coordinates. '
        'These sampled paths do not establish arbitrary unseen-query accuracy.'),
    'fixed_budget': ('fixed_budget', 'draw_fixed_budget', 'appendix',
        'Fixed compact width 512: mean of per-pair ratios of maximum-recorded '
        'compression RMS to maximum-recorded dense-pair RMS; dots show all three '
        'pairs. All complete candidates are included regardless of passing. Source '
        'settings can vary with dense width. Saved finite-grid observations, with '
        'no smoothing or new training.'),
    'robustness': ('robustness', 'draw_robustness', 'appendix',
        'Corrected dimension candidates and five single-seed architecture cases. '
        'Dimension selection uses max(error)/max(dense pair) <= 1; endpoint '
        'agreement is not an additional selection filter. Filled markers are '
        'learned and hollow markers total storage of the same model; d = 784 uses '
        'the panel projection. Architecture uses one shared regularized empirical '
        'configuration, not a new theorem certificate.'),
    'sphere_orders': ('sphere', 'draw_sphere_orders', 'appendix',
        'Earlier population response-memory endpoint experiment: four ReLU layers, '
        'width 2048, 64 training points, 8192 equal-area queries, one seed and '
        'Euler step 1/128. Models stop individually at training RMS <= 0.01, '
        'not common times. Both hemispheres and shared error scales are shown. '
        'ReLU is outside the analytic-activation theorem; saved-data replotting '
        'does not reproduce the unavailable historical training producer.'),
    'radial_gallery': ('radial', 'draw_radial_gallery', 'appendix',
        'Five earlier Legendre tasks, three tanh hidden layers, width 4096, '
        'orders 1/2/3. Each model is at its own training-MSE 0.001 endpoint, '
        'not a shared time. RMS uses all 8192 angles; radius is 3 + prediction.'),
    'same_rank': ('response', 'draw_same_rank', 'appendix',
        'Older paired-label endpoint comparison: Legendre order 3 and two '
        'trained-factor seeds, both with correction rank bound 24. Equal rank '
        'does not mean equal total storage. Each fits training MSE 0.001 at its '
        'own time; RMS compares predictions against dense on 8192 circle queries.'),
    'paired_projection': (None, 'draw_paired_projection', 'proof appendix',
        'Schematic projection identity: both histories use the same orthogonal '
        'projection and integration measure. Mixed terms vanish; feedback '
        'stability is separately needed for a trajectory guarantee.'),
    'panel_size': ('scope', 'draw_panel_size', 'appendix',
        'Declared panels of 8/30/60 inputs, scored on the SAME original eight '
        'queries. Larger-panel degradation at fixed source rank is retained. '
        'Labels of the declared query inputs are never used during setup.'),
    'costs': ('costs', 'draw_costs', 'appendix',
        'Recorded costs of the actual selected fixed-data Figure 4 models: '
        'three-seed timing means/sample SD, full-rollout setup, learned and '
        'fixed payloads. Process GPU peaks are not isolated model memory. '
        'Legendre retains dense mixers. No training-time speedup is demonstrated.'),
    'transfer': ('scope', 'draw_transfer', 'appendix',
        'Changed-label source-transfer test with rebuilt, transferred and pooled '
        'sources. Poor transfer remains visible. The fixed-labelled-dataset '
        'theorem does not promise label-independent sources.'),
    'dense_pairs_sphere': ('dense_pairs_sphere', 'draw_dense_pairs', 'appendix',
        'Three independent dense pairs per width on sphere data. Mean and '
        'individual pairs; fitted inverse-square-root curves are descriptive.'),
    'dense_pairs_mnist': ('dense_pairs_mnist', 'draw_dense_pairs', 'appendix',
        'Three independent dense pairs per width on MNIST. Mean and individual '
        'pairs; fitted inverse-square-root curves are descriptive.'),
    'radial_shallow': ('radial', 'draw_radial_shallow', 'alternative',
        'Earlier two-hidden-layer tanh circle gallery, width 2048, orders 1/3/7. '
        'Individually fitted training-MSE 0.001 endpoints; not common-time errors.'),
    'sphere_comparison': ('sphere', 'draw_sphere_comparison', 'alternative',
        'Alternative rendering of the same sphere endpoint data as sphere_orders: '
        'dense, order-3 closure and signed difference. Same individual stopping '
        'times, ReLU scope limitation and shared error scale.'),
}


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _module(relative):
    path = PAPER / relative
    name = '_paper_plot_' + path.stem
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


def _save(figure, prefix, dpi):
    for extension in ('pdf', 'png'):
        figure.savefig(prefix.with_suffix('.'+extension), dpi=max(dpi, 300) if extension == 'png' else dpi)
    if getattr(figure, 'latex_table', None):
        prefix.with_suffix('.tex').write_text(figure.latex_table)
    plt.close(figure)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument('--only', nargs='+', choices=FIGURES)
    selection.add_argument('--all', action='store_true', help='Render the complete inventory (default)')
    parser.add_argument('--list', action='store_true', help='List figures and source paths without plotting')
    parser.add_argument('--check', action='store_true', help='Check selected input files without plotting')
    parser.add_argument('--out', type=Path, help='Fresh output directory; default is a timestamped data/ directory')
    parser.add_argument('--data-dir', type=Path, help='Load an exported plotting-data package')
    parser.add_argument('--export-data', type=Path, help='Export selected data files and checksums, then stop')
    parser.add_argument('--dpi', type=int, default=300)
    args = parser.parse_args(argv)
    names = args.only or list(FIGURES)
    keys = sorted({FIGURES[name][0] for name in names if FIGURES[name][0] is not None})
    inputs = {key: (args.data_dir/(key+INPUTS[key].suffix) if args.data_dir else INPUTS[key]) for key in keys}
    if args.list:
        for name in names:
            key, _, placement, _ = FIGURES[name]
            print(f'{name:22} {placement:15} {inputs[key] if key else "schematic; no data"}')
        return 0
    missing = [str(path) for path in inputs.values() if not path.is_file()]
    if missing:
        parser.error('Missing plotting inputs (training is never automatic):\n'+'\n'.join(missing))
    if args.data_dir:
        manifest = json.loads((args.data_dir/'manifest.json').read_text())
        for key, path in inputs.items():
            if _sha(path) != manifest['inputs'][key]['sha256']:
                parser.error(f'Input checksum mismatch: {path}')
    if args.export_data:
        args.export_data.mkdir(parents=True, exist_ok=False)
        exported = {}
        for key, path in inputs.items():
            target = args.export_data/(key+path.suffix)
            shutil.copyfile(path, target)
            exported[key] = dict(file=target.name, original=str(path), sha256=_sha(target))
        (args.export_data/'manifest.json').write_text(json.dumps(dict(inputs=exported,
            figures=names, training_performed=False), indent=2)+'\n')
        print(f'Exported {len(inputs)} inputs to {args.export_data}')
        return 0
    if args.check:
        print(f'All {len(inputs)} input files exist for {len(names)} selected figures; no training needed.')
        return 0
    if args.dpi <= 0:
        parser.error('--dpi must be positive')
    output = args.out or STUDY_DATA/'paper_plots'/datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    output.mkdir(parents=True, exist_ok=False)
    os.environ.setdefault('MPLCONFIGDIR', str((output/'.matplotlib').resolve()))
    global np, plt, mpl
    import numpy as np
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt
    from threadpoolctl import threadpool_limits
    record = dict(command=[sys.executable, str(Path(__file__).resolve()), *(argv or sys.argv[1:])],
                  python=platform.python_version(), numpy=np.__version__, matplotlib=mpl.__version__,
                  plotting_source_sha256=_sha(__file__), training_performed=False, gpu_used=False,
                  inputs={key: dict(path=str(path), sha256=_sha(path)) for key, path in inputs.items()},
                  figures={}, errors={})
    cache = {}
    with threadpool_limits(limits=1), mpl.rc_context(RC):
        for name in names:
            key, renderer, placement, caption = FIGURES[name]
            prefix = output/name
            try:
                if key is not None and key not in cache:
                    if inputs[key].suffix == '.json':
                        cache[key] = json.loads(inputs[key].read_text())
                    else:
                        with np.load(inputs[key], allow_pickle=False) as archive:
                            cache[key] = {field: archive[field].copy() for field in archive.files}
                _save(globals()[renderer](cache.get(key)), prefix, args.dpi)
                prefix.with_suffix('.caption.txt').write_text(caption+'\n')
                record['figures'][name] = dict(placement=placement, caption=caption,
                    outputs={path.name: _sha(path) for path in output.glob(name+'.*')})
                print(f'[{len(record["figures"])}/{len(names)}] {name}', flush=True)
            except Exception as error:
                record['errors'][name] = f'{type(error).__name__}: {error}'
                print(f'FAILED {name}: {error}', file=sys.stderr, flush=True)
            (output/'manifest.json').write_text(json.dumps(record, indent=2)+'\n')
    print(f'Figures and captions: {output}')
    return int(bool(record['errors']))


# ----------------------------------------------------------------------------- shared style
# Methods carry the colour (validated categorical slots, all-pairs colour-vision
# check); baselines stay neutral grey. Text is ink, never a series colour.
INK, MUTED, LIGHT = '#1f1f1e', '#6b6b68', '#e4e3de'
TEXT_WIDTH = 6.5  # inches, article class with 1 in margins
METHOD = {
    'legendre': dict(label='Legendre', color='#2a78d6', marker='s'),
    'harmonic': dict(label='Harmonic', color='#1baf7a', marker='D'),
    'taylor': dict(label='Taylor', color='#eb6834', marker='o'),
}
FAMILY = {'legendre': 'legendre', 'harmonic': 'harmonic', 'logarithmic': 'taylor', 'taylor': 'taylor'}
LEGENDRE_ORDERS = {1: '#9bbfea', 2: '#6aa0e2', 3: '#3f84d8', 7: '#1d5ba6'}  # light to dark: more moments
CONTROL = {
    'dense': dict(color='#55554f', marker='d', linestyle='-'),
    'low_rank': dict(color='#8f8e88', marker='v', linestyle=(0, (4, 2))),
    'frozen': dict(color='#a3a29c', linestyle=(0, (6, 2, 1.5, 2))),
    'pair': dict(color=INK, linestyle=(0, (1, 1.8))),
}
DIVERGING = ('#346e9f', '#f7f6f2', '#c45538')  # signed values: blue, off-white, red
RC = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['Nimbus Sans', 'Liberation Sans', 'DejaVu Sans'],
    'mathtext.fontset': 'custom', 'mathtext.rm': 'Nimbus Sans',
    'mathtext.it': 'Nimbus Sans:italic', 'mathtext.bf': 'Nimbus Sans:bold',
    'font.size': 8, 'axes.labelsize': 8, 'axes.titlesize': 8,
    'xtick.labelsize': 7, 'ytick.labelsize': 7, 'legend.fontsize': 7,
    'text.color': INK, 'axes.labelcolor': INK, 'axes.edgecolor': MUTED,
    'axes.linewidth': .6, 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': False, 'axes.facecolor': 'white',
    'xtick.color': MUTED, 'ytick.color': MUTED, 'xtick.labelcolor': INK, 'ytick.labelcolor': INK,
    'xtick.major.width': .6, 'ytick.major.width': .6, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5,
    'xtick.minor.visible': False, 'ytick.minor.visible': False,
    'lines.linewidth': 1.4, 'lines.markersize': 3.6, 'lines.markeredgewidth': 0,
    'legend.frameon': False, 'legend.handlelength': 1.8,
    'pdf.fonttype': 42, 'savefig.facecolor': 'white', 'figure.facecolor': 'white',
}


def _panels(columns=2, height=2.45, sharey=False, **adjust):
    figure, axes = plt.subplots(1, columns, figsize=(TEXT_WIDTH, height), sharey=sharey)
    figure.subplots_adjust(**{**dict(left=.085, right=.985, bottom=.17, top=.87, wspace=.28), **adjust})
    return figure, axes


def _single(width=3.2, height=2.3, **adjust):
    figure, axis = plt.subplots(figsize=(width, height))
    figure.subplots_adjust(**{**dict(left=.17, right=.97, bottom=.19, top=.95), **adjust})
    return figure, axis


def _panel(axis, letter, title):
    """Bold panel letter and a short name, left-aligned above the axes."""
    axis.set_title(rf'$\mathbf{{{letter}}}$   {title}' if letter else title, loc='left', pad=6)


def _log_ticks(axis, narrow=False):
    """Decade ticks as powers of ten; within one decade use 1-2-5 steps instead."""
    if narrow:
        axis.set_major_locator(mpl.ticker.LogLocator(base=10, subs=(1, 2, 3, 4, 5), numticks=12))
        axis.set_major_formatter(mpl.ticker.FormatStrFormatter('%g'))
    else:
        axis.set_major_locator(mpl.ticker.LogLocator(base=10, numticks=12))
        axis.set_major_formatter(mpl.ticker.LogFormatterMathtext())
    axis.set_minor_locator(mpl.ticker.NullLocator())


def _width_ticks(axis, widths):
    """Dense widths on a log axis, written compactly (512, 1k, 2k, ...)."""
    axis.set_xscale('log')
    axis.set_xticks(widths, [str(n) if n < 1000 else f'{n // 1024}k' for n in widths])
    axis.xaxis.set_minor_locator(mpl.ticker.NullLocator())


def _label(axis, x, y, text, dx=4, dy=0, ha='left', va='center', color=INK, **kwargs):
    axis.annotate(text, (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va=va,
                  color=color, annotation_clip=False, **kwargs)


def _direct_labels(axis, items, x, line=9.6, dx=0., ha='left'):
    """Label curve ends at (x, y), nudged apart vertically so labels never overlap.

    items: (y, text, colour) or (y, text, colour, note); a note is set smaller and
    muted under its label. Call after the axis limits and the layout are final.
    """
    if not items:
        return
    to_display, to_data = axis.transData, axis.transData.inverted()
    scale = axis.figure.dpi/72
    order = sorted(range(len(items)), key=lambda i: items[i][0])
    ys = np.array([to_display.transform((x, items[i][0]))[1] for i in order], dtype=float)
    heights = np.array([line*scale*(items[i][1].count('\n')+1+(.85 if len(items[i]) > 3 else 0))
                        for i in order])
    for _ in range(400):
        moved = False
        for i in range(1, len(ys)):
            overlap = (heights[i-1]+heights[i])/2-(ys[i]-ys[i-1])
            if overlap > .01:
                ys[i-1] -= overlap/2
                ys[i] += overlap/2
                moved = True
        if not moved:
            break
    x_display = to_display.transform((x, items[order[0]][0]))[0]
    offset = dx if ha == 'left' else -dx
    for y_display, height, i in zip(ys, heights, order):
        text, colour = items[i][1], items[i][2]
        lines = text.count('\n')+1
        top = y_display+height/2
        y = to_data.transform((x_display, top-lines*line*scale/2))[1]
        axis.annotate(text, (x, y), xytext=(offset, 0), textcoords='offset points',
                      ha=ha, va='center', color=colour, annotation_clip=False)
        if len(items[i]) > 3:
            y = to_data.transform((x_display, top-(lines+.42)*line*scale))[1]
            axis.annotate(items[i][3], (x, y), xytext=(offset, 0), textcoords='offset points', ha=ha,
                          va='center', color=MUTED, fontsize=6.5, annotation_clip=False)


def _method_line(axis, x, y, family, **kwargs):
    style = METHOD[FAMILY[family]]
    return axis.plot(x, y, color=style['color'], marker=style['marker'], **kwargs)


def _pair_line(axis, *args, **kwargs):
    return axis.plot(*args, color=CONTROL['pair']['color'], linestyle=CONTROL['pair']['linestyle'],
                     lw=kwargs.pop('lw', .9), **kwargs)


def _hollow(**kwargs):
    return dict(markerfacecolor='white', markeredgewidth=.9, **kwargs)


def _q(name):
    """'logarithmic_256_r15' -> 'Taylor, q = 256' (q: selected coordinates)."""
    return f'Taylor, $q = {name.split("_")[1]}$'


# ----------------------------------------------------------------------------- main figures

def draw_storage(data):
    """Learned storage needed to match dense-vs-dense, against dense width."""
    widths = data['widths']
    n = np.asarray(widths, float)
    toy = {}
    for row in data['toy_individuals']:
        toy.setdefault(row['family'], {}).setdefault(row['width'], []).append(row['selected']['learned'])
    digits = {family: {group['width']: group['learned_values'] for group in groups}
              for family, groups in data['digits_groups'].items()}
    panels = [('a', 'Circle, $d = 2$', 2, data['toy_groups'], toy, data['fits']['Toy circle (d = 2)']),
              ('b', 'Digits 1 vs 7, $d = 64$', 64, data['digits_groups'], digits,
               data['fits']['Digits 1 vs 7 (d = 64)'])]
    figure, axes = _panels(sharey=True, wspace=.1, right=.96)
    grid = np.geomspace(widths[0], widths[-1], 200)
    for axis, (letter, title, d, groups, individual, fits) in zip(axes, panels):
        dense = n**2+n*(d+1)  # (L-1)n^2 + n(d+1) learned scalars, L = 2
        axis.plot(n, dense, color=CONTROL['dense']['color'], lw=1.1)
        labels = [(dense[-1], 'dense', INK)]
        for family in ('legendre', 'harmonic', 'logarithmic'):
            if family not in groups:
                continue
            style = METHOD[FAMILY[family]]
            mean = np.array([group['mean'] for group in groups[family]])
            for width in widths:
                values = individual[family][width]
                axis.scatter([width]*len(values), values, s=4, color=style['color'], alpha=.35, lw=0, zorder=2)
            _method_line(axis, n, mean, family, zorder=3)
            label = (mean[-1], style['label'], INK)
            if family in fits:
                fit = fits[family]
                axis.plot(grid, fit['coefficient']*np.log(grid)**fit['exponent'], color=style['color'],
                          lw=.8, linestyle=(0, (3, 2)), zorder=2)
                label += (rf'$\propto(\log n)^{{{fit["exponent"]:.1f}}}$',)
            labels.append(label)
        _width_ticks(axis, widths)
        axis.set_xlim(widths[0]/1.25, widths[-1]*3.4)
        axis.spines['bottom'].set_bounds(widths[0], widths[-1])
        axis.set_yscale('log')
        _log_ticks(axis.yaxis)
        axis.set_xlabel('Dense width $n$')
        _panel(axis, letter, title)
        axis.labels_ = labels
    axes[0].set_ylabel('Learned scalars')
    axes[0].set_ylim(1.2e4, 6e8)
    for axis in axes:
        _direct_labels(axis, axis.labels_, widths[-1]*1.12)
    return figure


def draw_accuracy(data):
    """Endpoint error against learned storage at dense width 4096."""
    figure, axes = _panels(height=2.6, wspace=.22)
    limits = data['shared_learned_limits']
    for axis, (letter, key, title) in zip(axes, (('a', 'sphere', 'Sphere, $d = 3$'),
                                                  ('b', 'digits', 'Digits 1 vs 7, $d = 64$'))):
        result = data['panels'][key]
        summaries = result['summaries']
        pair = summaries['dense_pair']['endpoint_rms']
        axis.axhspan(pair['mean']-pair['sd'], pair['mean']+pair['sd'], color=LIGHT, lw=0, zorder=0)
        _pair_line(axis, [limits[0], limits[1]], [pair['mean']]*2)
        frozen = summaries['frozen_features']['endpoint_rms']['mean']
        axis.axhline(frozen, color=CONTROL['frozen']['color'], linestyle=CONTROL['frozen']['linestyle'], lw=.9)

        # Small dense networks trained directly; the full-width member is the benchmark itself.
        controls = result['fixed_original_reference_controls']
        dense = sorted((c for c in controls if c['family'] == 'dense' and c['moving'] < 1e7),
                       key=lambda c: c['moving'])
        x, y = [c['moving'] for c in dense], [c['endpoint_rms'] for c in dense]
        spread = []
        for c in dense:
            summary = result['fixed_original_reference_dense_summaries'].get(c['name'])
            if summary is None:
                spread.append((0, 0))
            elif key == 'sphere':
                spread.append((summary['median']-summary['minimum'], summary['maximum']-summary['median']))
            else:
                spread.append((summary['endpoint_rms']['sd'],)*2)
        style = CONTROL['dense']
        axis.errorbar(x, y, yerr=np.array(spread).T, fmt='none', ecolor=style['color'], elinewidth=.6, alpha=.6)
        axis.plot(x, y, color=style['color'], marker=style['marker'], lw=1.1, ms=3.6)
        low = sorted((c for c in controls if c['family'] == 'low_rank'), key=lambda c: c['moving'])
        style = CONTROL['low_rank']
        axis.plot([c['moving'] for c in low], [c['endpoint_rms'] for c in low], color=style['color'],
                  marker=style['marker'], linestyle=style['linestyle'], lw=1, ms=3.4)

        ends = {}
        for family in ('legendre', 'harmonic', 'logarithmic'):
            # An incomplete budget has no three-repetition mean and is left out, never averaged partially.
            groups = sorted((g for g in summaries.values() if g['family'] == family and g['status'] == 'complete'
                             and 'endpoint_rms' in g), key=lambda g: g['moving'])
            if not groups:
                continue
            colour = METHOD[FAMILY[family]]['color']
            x = [g['moving'] for g in groups]
            for metric, hollow in (('endpoint_rms', False), ('extra_endpoint_rms', True)):
                if metric not in groups[0] or (hollow and family != 'logarithmic'):
                    continue
                mean = np.array([g[metric]['mean'] for g in groups])
                sd = np.array([g[metric]['sd'] for g in groups])
                axis.errorbar(x, mean, yerr=[np.where(mean-sd > 0, sd, mean*.5), sd], fmt='none',
                              ecolor=colour, elinewidth=.6, alpha=.6)
                if hollow:
                    axis.plot(x, mean, color=colour, marker='o', linestyle=(0, (1, 1.5)), lw=1, ms=3.4,
                              zorder=4, **_hollow())
                else:
                    _method_line(axis, x, mean, family, zorder=5)
                ends[family+('_unseen' if hollow else '')] = (x[-1], mean[-1])

        axis.set(xscale='log', yscale='log', xlim=limits, ylim=(2.5e-5, .6), xlabel='Learned scalars')
        _log_ticks(axis.xaxis)
        _log_ticks(axis.yaxis)
        _panel(axis, letter, title)
        for family, (x, y) in ends.items():
            unseen = family.endswith('_unseen')
            _label(axis, x, y, 'unseen inputs' if unseen else METHOD[FAMILY[family]]['label'],
                   color=MUTED if unseen else INK)
        _label(axis, dense[0]['moving'], dense[0]['endpoint_rms'], 'small dense', dx=-2, dy=5, va='bottom')
        _label(axis, low[-1]['moving'], low[-1]['endpoint_rms'], 'low rank')
        _label(axis, limits[1], frozen, 'frozen features', dx=0, dy=2.5, ha='right', va='bottom', color=MUTED)
        _label(axis, limits[1], pair['mean'], 'dense vs.\ndense', dx=0, dy=2, ha='right', va='bottom',
               color=MUTED)
    axes[0].set_ylabel('Endpoint test RMS')
    return figure


def draw_trajectory(data):
    """Test RMS to the dense run over training, compressions against dense vs. dense."""
    times = np.asarray(data['times'], float)
    figure, axes = _panels(sharey=True, wspace=.1)
    for axis, (letter, key, title) in zip(axes, (('a', 'circle', 'Circle, $d = 2$'),
                                                  ('b', 'digits', 'Digits 1 vs 7, $d = 64$'))):
        summaries = data['panels'][key]['summaries']
        pair = np.asarray(summaries['dense_pair']['mean'])
        _pair_line(axis, times, pair, lw=1)
        labels = [(pair[-1], 'dense vs.\ndense', MUTED)]
        for family in ('legendre', 'harmonic', 'logarithmic'):
            if family in summaries:
                mean = np.asarray(summaries[family]['mean'])
                axis.plot(times, mean, color=METHOD[FAMILY[family]]['color'], lw=1.5)
                labels.append((mean[-1], METHOD[FAMILY[family]]['label'], INK))
        axis.set_yscale('log')
        _log_ticks(axis.yaxis)
        axis.set_xlim(0, 40.5)
        axis.spines['bottom'].set_bounds(0, 32)
        axis.set_xticks([0, 8, 16, 24, 32])
        axis.set_xlabel('Training time $t$', x=16/40.5)
        _panel(axis, letter, title)
        axis.labels_ = labels
    axes[0].set_ylabel('Test RMS to dense')
    lowest = min(np.min(line.get_ydata()) for axis in axes for line in axis.lines)
    axes[0].set_ylim(lowest/2, .06)
    for axis in axes:
        _direct_labels(axis, axis.labels_, 32.6)
    return figure


def _polar(axis, angles, curves, train=None, offset=3., rings=(-1, 0, 1), limit=5.6):
    """Radius = offset + prediction; faint rings at offset + rings, zero dashed."""
    circle = np.linspace(0, 2*np.pi, 361)
    for value in rings:
        radius = offset+value
        axis.plot(radius*np.cos(circle), radius*np.sin(circle), color=LIGHT if value else '#c9c8c2',
                  lw=.5, linestyle=(0, (2, 2)) if value == 0 else '-', zorder=0)
    loop = np.r_[angles, angles[:1]]
    for values, style in curves:
        radius = offset+np.r_[values, values[:1]]
        axis.plot(radius*np.cos(loop), radius*np.sin(loop), **{'solid_joinstyle': 'round', **style})
    if train is not None:
        train_angles, labels = train
        radius = offset+np.asarray(labels)
        axis.scatter(radius*np.cos(train_angles), radius*np.sin(train_angles), s=7, color=INK,
                     edgecolors='white', linewidths=.5, zorder=6)
    axis.set(xlim=(-limit, limit), ylim=(-limit, limit), aspect='equal')
    axis.axis('off')


def _order_style(order, dense=False):
    if dense:
        return dict(color=INK, lw=1.6, zorder=2)
    return dict(color=LEGENDRE_ORDERS[order], lw=1, zorder=3+order,
                linestyle=(0, (3, 1.5)) if order == max(LEGENDRE_ORDERS) else '-')


def _legend_row(figure, entries, y=.04):
    """One centred row of line/dot keys in figure coordinates."""
    handles = []
    for label, style in entries:
        if style == 'dot':
            handles.append(mpl.lines.Line2D([], [], color=INK, marker='o', linestyle='none', ms=3.2, label=label))
        else:
            handles.append(mpl.lines.Line2D([], [], label=label, **{k: v for k, v in style.items() if k != 'zorder'}))
    figure.legend(handles=handles, loc='lower center', bbox_to_anchor=(.5, y), ncol=len(handles),
                  handlelength=2.2, columnspacing=2.2)


def draw_radial_trajectory(data):
    """The function on the circle at four common times: dense and Legendre orders."""
    times = data['common_times']
    angles = data['history_angles']
    train = (np.arctan2(data['train_inputs'][:, 1], data['train_inputs'][:, 0]), data['train_labels'])
    figure, axes = plt.subplots(1, 4, figsize=(TEXT_WIDTH, 1.95))
    figure.subplots_adjust(left=.01, right=.99, bottom=.16, top=.9, wspace=.04)
    for axis, t in zip(axes, (0, 5, 20, 80)):
        i = int(np.flatnonzero(times == t)[0])
        curves = [(data['common_dense'][i], _order_style(0, dense=True))]
        curves += [(data[f'common_memory_{p}'][i], _order_style(p)) for p in (1, 3, 7)]
        _polar(axis, angles, curves, train)
        axis.set_title(f'$t = {t}$', pad=1)
    _legend_row(figure, [('dense', _order_style(0, dense=True))]
                + [(f'Legendre, $q = {p}$', _order_style(p)) for p in (1, 3, 7)]
                + [('training labels', 'dot')], y=.0)
    return figure


def draw_same_rank(data):
    """Same rank bound, same training fit: trained factors versus Legendre memory."""
    meta = json.loads(str(data['metadata_json']))
    angles, dense = data['factor_angles'], data['factor_dense']
    memory = data['memory_endpoint_3']
    factors = [data[f'factor_seed_{seed}'] for seed in (20260924, 20260925)]
    measured = [float(np.sqrt(np.mean((v-dense)**2))) for v in (memory, *factors)]
    recorded = [meta['factor_radial_rms'][key] for key in ('P3', '20260924', '20260925')]
    if not np.allclose(measured, recorded, rtol=1e-12, atol=1e-14):
        raise ValueError('Radial factor metrics differ from the saved records')
    train = (np.arctan2(data['train_inputs'][:, 1], data['train_inputs'][:, 0]), data['train_labels'])
    figure, axes = plt.subplots(1, 3, figsize=(TEXT_WIDTH, 2.35))
    figure.subplots_adjust(left=.01, right=.99, bottom=.13, top=.86, wspace=.05)
    reference = dict(color='#cfcec8', lw=2.6, zorder=1)
    low = CONTROL['low_rank']['color']
    loop = np.r_[angles, angles[:1]]

    def gap(axis, prediction, colour):
        outer, inner = 3+np.r_[prediction, prediction[:1]], 3+np.r_[dense, dense[:1]]
        x = np.r_[outer*np.cos(loop), (inner*np.cos(loop))[::-1]]
        y = np.r_[outer*np.sin(loop), (inner*np.sin(loop))[::-1]]
        axis.fill(x, y, color=colour, alpha=.18, lw=0, zorder=1)

    panels = [('Trained factors $W_0 + AB$', [(dense, reference), (factors[0], dict(color=low, lw=1.1)),
               (factors[1], dict(color=low, lw=1, linestyle=(0, (3, 1.6))))],
               f'RMS {measured[1]:.3f} and {measured[2]:.3f}'),
              ('Dense network', [(dense, dict(color=INK, lw=1.4))], 'reference'),
              ('Legendre, $q = 3$', [(dense, reference), (memory, dict(color=METHOD['legendre']['color'], lw=1.2))],
               f'RMS {measured[0]:.5f}')]
    for axis, (title, curves, note) in zip(axes, panels):
        if title.startswith('Trained'):
            for factor in factors:
                gap(axis, factor, low)
        _polar(axis, angles, curves, train)
        axis.set_title(title, pad=2)
        axis.text(.5, -.02, note, transform=axis.transAxes, ha='center', va='top', color=MUTED)
    return figure


def draw_moments(data):
    """A few Legendre moments already reconstruct a neuron's history."""
    history, fits = data['histories'], data['fits']
    figure, axes = plt.subplots(2, 3, figsize=(TEXT_WIDTH, 2.7), gridspec_kw={'height_ratios': [2, 1]})
    figure.subplots_adjust(left=.07, right=.99, bottom=.12, top=.9, wspace=.12, hspace=.55)
    shades = ['#3b3b38', '#77766f', '#adaca6']
    time = np.linspace(0, 1, len(history))
    blue = METHOD['legendre']['color']
    for order in range(3):
        axis = axes[0, order]
        for neuron, shade in enumerate(shades):
            values = np.r_[history[:, neuron], fits[:, :, neuron].ravel()]
            lower, upper = values.min(), values.max()
            scale = lambda v: 2-neuron+.8*(v-lower)/max(upper-lower, 1e-12)
            axis.plot(time, scale(history[:, neuron]), color=shade, lw=1.3)
            axis.plot(time, scale(fits[order, :, neuron]), color=blue, lw=1, linestyle=(0, (3, 1.6)))
        _panel(axis, 'abc'[order], f'$q = {order+1}$')
        axis.set_title(f'median error {100*data["median_errors"][order]:.0f}%', loc='right', pad=6, color=MUTED,
                       fontsize=7)
        axis.set(xticks=[0, 1], xticklabels=['start', 'now'], yticks=[], ylim=(-.1, 3.0))
        axis.spines['left'].set_visible(False)
        now, halfway = data['coefficients'][order], data['halfway_coefficients'][order]
        lower, upper = np.percentile(np.r_[now, halfway], [1, 99])
        grid = np.linspace(lower-.12*(upper-lower), upper+.12*(upper-lower), 200)
        density = axes[1, order]
        for values, style, colour in ((now, '-', INK), (halfway, (0, (3, 1.6)), MUTED)):
            bandwidth = max(1.06*values.std()*len(values)**(-.2), 1e-12)
            curve = np.exp(-.5*((grid[:, None]-values[None, :])/bandwidth)**2).sum(axis=1)
            density.plot(grid, curve, color=colour, linestyle=style, lw=1)
        density.set(xticks=[], yticks=[])
        density.spines['left'].set_visible(False)
        density.set_xlabel(f'moment {order} across 512 neurons', labelpad=2)
    axes[0, 0].set_ylabel('three neurons')
    _label(axes[1, 2], 1, .9, 'now', dx=0, ha='right', xycoords='axes fraction')
    _label(axes[1, 2], 1, .62, 'halfway', dx=0, ha='right', xycoords='axes fraction', color=MUTED)
    return figure


# ----------------------------------------------------------------------------- appendix figures

def draw_spectra(data):
    """Singular values of dense feature histories collapse across widths."""
    rows = sorted(data['history_spectra'], key=lambda row: row['width'])
    widths = [row['width'] for row in rows]
    shades = plt.get_cmap('Greys')(np.linspace(.35, .95, len(rows)))
    figure, axes = _panels(wspace=.32)
    axis = axes[0]
    for row, shade in zip(rows, shades):
        values = np.asarray(row['normalized_singular_values'][:300], float)
        width = row['width']
        axis.plot(np.arange(1, len(values)+1), values, color=shade, lw=1.1,
                  label=str(width) if width < 1000 else f'{width // 1024}k')
    fixed = [row['fixed_tolerance_ranks']['0.01'] for row in rows]
    shrinking = [row['shrinking_tolerance_rank'] for row in rows]
    axis.axvline(np.mean(fixed), color=MUTED, lw=.6, linestyle=(0, (1, 1.8)))
    _label(axis, np.mean(fixed), 1.5e-6, '1% tail', dx=3, color=MUTED)
    axis.set(xscale='log', yscale='log', xlim=(1, 300), ylim=(1e-6, 1.5), xlabel='Singular value index $j$',
             ylabel=r'$\sigma_j\,/\,\|\sigma\|$')
    _log_ticks(axis.yaxis)
    axis.legend(title='width $n$', loc='lower left', handlelength=1.2, labelspacing=.25, title_fontsize=7)
    _panel(axis, 'a', 'Feature-history spectrum')
    axis = axes[1]
    axis.plot(widths, fixed, color=INK, marker='o', lw=1.2)
    axis.plot(widths, shrinking, color=MUTED, marker='o', linestyle=(0, (3, 1.6)), lw=1.2, **_hollow())
    _width_ticks(axis, widths)
    axis.set_xlim(widths[0]/1.2, widths[-1]*3.2)
    axis.spines['bottom'].set_bounds(widths[0], widths[-1])
    axis.set(ylim=(0, 100), xlabel='Dense width $n$', ylabel='Rank needed')
    _panel(axis, 'b', 'Rank for a given tail')
    _direct_labels(axis, [(fixed[-1], 'fixed 1%', INK), (shrinking[-1], r'$1\%\cdot\sqrt{512/n}$', MUTED)],
                   widths[-1]*1.12)
    return figure


def draw_query_distance(data):
    """Endpoint error along controlled paths away from declared inputs."""
    angles = np.asarray(data['plan']['paths']['angles'], float)
    figure, axis = _single()
    labels = []
    for name, row in data['controlled_paths'].items():
        values = np.asarray(row['endpoint_rms_by_angle'], float)
        if name.startswith('dense_'):
            _pair_line(axis, angles, values, lw=1)
            labels.append((values[-1], 'dense vs.\ndense', MUTED))
            continue
        hollow = name.split('_')[1] == '256'
        axis.plot(angles, values, color=METHOD['taylor']['color'], marker='o', lw=1.3, ms=3.2,
                  linestyle=(0, (3, 1.6)) if hollow else '-', **(_hollow() if hollow else {}))
        labels.append((values[-1], _q(name), INK))
    axis.set(xlim=(0, angles[-1]*1.75), xlabel='Distance from declared input (rad)', ylabel='Endpoint test RMS')
    axis.set_xlabel('Distance from declared input (rad)', x=1/1.75/2)
    axis.spines['bottom'].set_bounds(0, angles[-1])
    axis.set_xticks(np.arange(0, angles[-1]+1e-9, .1))
    axis.set_ylim(0, axis.get_ylim()[1]*1.08)
    _direct_labels(axis, labels, angles[-1]*1.06)
    return figure


def draw_robustness(data):
    """Storage across input dimension and error ratio across architectures."""
    figure, axes = _panels(wspace=.3)
    axis = axes[0]
    dims = ['2', '3', '10', '64', '784']
    selected = data['selected']
    for j, d in enumerate(dims):
        chosen = selected.get(d, {})
        for family, best in chosen.items():
            style = METHOD[FAMILY[family]]
            x = j+((-.13 if family == 'harmonic' else .13) if len(chosen) > 1 else 0)
            axis.plot([x, x], [best['learned'], best['total']], color=style['color'], lw=.8, alpha=.6)
            axis.plot(x, best['learned'], marker=style['marker'], color=style['color'], ms=4.2)
            axis.plot(x, best['total'], marker=style['marker'], color=style['color'], ms=4.2, **_hollow())
    axis.set_xticks(range(len(dims)), dims)
    axis.set(xlim=(-.5, len(dims)-.4), yscale='log', ylim=(3e4, 2e6), xlabel='Input dimension $d$',
             ylabel='Stored scalars')
    _log_ticks(axis.yaxis)
    _panel(axis, 'a', 'Smallest passing model')
    harmonic, taylor = selected['2']['harmonic'], selected['784']['logarithmic']
    _label(axis, -.13, harmonic['total'], 'Harmonic', dx=0, dy=6, ha='center', va='bottom')
    _label(axis, 4, taylor['learned'], 'Taylor', dx=0, dy=-6, ha='center', va='top')
    _label(axis, 4, taylor['total'], 'total', dx=6, color=MUTED)
    _label(axis, 4, taylor['learned'], 'learned', dx=6, color=MUTED)

    axis = axes[1]
    cases = [('baseline', 'baseline'), ('depth3', '$L = 3$'), ('depth4', '$L = 4$'),
             ('silu', 'SiLU'), ('m16', '$m = 16$')]
    colour = METHOD['taylor']['color']
    for j, (case, _) in enumerate(cases):
        row = data['architecture'][case][0]
        if 'maximum_ratio' not in row:
            _label(axis, j, .5, 'inconclusive', dx=0, ha='center', color=MUTED,
                   xycoords=('data', 'axes fraction'))
            continue
        unresolved = row['status'] == 'numerically_unresolved'
        axis.plot(j-.1, row['endpoint_ratio'], marker='o', color=colour, ms=4.2,
                  **(_hollow() if unresolved else {}))
        axis.plot(j+.1, row['maximum_ratio'], marker='o', color=colour, ms=4.2, **_hollow())
    _pair_line(axis, [-.5, len(cases)-.5], [1, 1])
    axis.set_xticks(range(len(cases)), [label for _, label in cases])
    axis.set(xlim=(-.5, len(cases)-.5), yscale='log', ylim=(5e-3, 2), ylabel='Error / dense vs. dense')
    _log_ticks(axis.yaxis)
    _panel(axis, 'b', 'Taylor across architectures')
    _label(axis, len(cases)-.5, 1, 'dense vs. dense', dx=0, dy=2.5, ha='right', va='bottom', color=MUTED)
    first = data['architecture']['baseline'][0]
    _label(axis, -.1, first['endpoint_ratio'], 'end of\ntraining', dx=0, dy=6, ha='center', va='bottom',
           color=MUTED)
    _label(axis, .1, first['maximum_ratio'], 'worst\ntime', dx=0, dy=-6, ha='center', va='top', color=MUTED)
    return figure


def draw_panel_size(data):
    """Endpoint error on eight common queries as the declared panel grows, at fixed storage."""
    records = data['panel_size']['records']
    sizes = [row['source_panel_size'] for row in records]
    figure, axis = _single()
    colour = METHOD['taylor']['color']
    names = sorted(records[0]['common_panel_models'],
                   key=lambda name: records[0]['common_panel_models'][name]['learned'])
    labels = []
    for name, hollow in zip(names, (True, False)):
        y = [row['common_panel_models'][name]['endpoint_rms'] for row in records]
        axis.plot(sizes, y, color=colour, marker='o', lw=1.3, linestyle=(0, (3, 1.6)) if hollow else '-',
                  **(_hollow() if hollow else {}))
        labels.append((y[-1], _q(name), INK))
    pair = [row['common_dense_pair']['endpoint_rms'] for row in records]
    _pair_line(axis, sizes, pair, lw=1)
    labels.append((pair[-1], 'dense vs.\ndense', MUTED))
    axis.set_xscale('log')
    axis.set_xticks(sizes, [str(s) for s in sizes])
    axis.xaxis.set_minor_locator(mpl.ticker.NullLocator())
    axis.set(xlim=(sizes[0]/1.15, sizes[-1]*4.2), yscale='log', ylim=(8e-4, .1), ylabel='Endpoint test RMS')
    axis.set_xlabel('Declared panel size', x=np.log(sizes[-1]*1.15/sizes[0])/np.log(4.2*1.15*sizes[-1]/sizes[0])/2)
    axis.spines['bottom'].set_bounds(sizes[0], sizes[-1])
    _log_ticks(axis.yaxis)
    _direct_labels(axis, labels, sizes[-1]*1.2)
    return figure


def draw_transfer(data):
    """Sources rebuilt for a new target, reused from the old one, or pooled."""
    transfer = data['transfer']
    times = np.asarray(data['times'], float)
    keep = times > 0
    figure, axis = _single()
    pair = np.asarray(transfer['baseline_curve'])
    _pair_line(axis, times[keep], pair[keep], lw=1)
    labels = [(pair[-1], 'dense vs.\ndense', MUTED)]
    for name, colour, style in (('rebuilt', METHOD['taylor']['color'], '-'),
                                ('transferred', CONTROL['dense']['color'], '-'),
                                ('pooled', CONTROL['low_rank']['color'], (0, (4, 2)))):
        curve = np.asarray(transfer['metrics'][name]['curve'])
        axis.plot(times[keep], curve[keep], color=colour, linestyle=style, lw=1.4)
        labels.append((curve[-1], name, INK))
    axis.set_yscale('log')
    _log_ticks(axis.yaxis)
    axis.set(xlim=(0, 45), ylim=(8e-5, .4), xticks=[0, 8, 16, 24, 32], ylabel='Test RMS to dense')
    axis.spines['bottom'].set_bounds(0, 32)
    axis.set_xlabel('Training time $t$', x=16/45)
    _direct_labels(axis, labels, 32.6)
    return figure


def draw_fixed_budget(data):
    """Error ratio of fixed-width compressions as the dense width grows."""
    widths = data['widths']
    figure, axes = _panels(sharey=True, wspace=.1)
    left, right = widths[0]/1.25, widths[-1]*3.4
    for axis, (letter, key, title) in zip(axes, (('a', 'circle', 'Circle, $d = 2$'),
                                                  ('b', 'digits', 'Digits 1 vs 7, $d = 64$'))):
        labels = []
        for family in ('harmonic', 'logarithmic'):
            rows = sorted((r for r in data['summaries'] if r['panel'] == key and r['family'] == family),
                          key=lambda r: r['dense_width'])
            if not rows:
                continue
            style = METHOD[FAMILY[family]]
            for row in rows:
                values = row['worst_recorded_ratio']['values']
                axis.scatter([row['dense_width']]*len(values), values, s=5, color=style['color'], alpha=.4, lw=0)
            mean = [r['worst_recorded_ratio']['mean'] for r in rows]
            _method_line(axis, [r['dense_width'] for r in rows], mean, family)
            labels.append((mean[-1], style['label'], INK))
        _pair_line(axis, [left, widths[-1]*1.08], [1, 1])
        labels.append((1, 'dense vs.\ndense', MUTED))
        _width_ticks(axis, widths)
        axis.set_xlim(left, right)
        axis.spines['bottom'].set_bounds(widths[0], widths[-1])
        axis.set_yscale('log')
        _log_ticks(axis.yaxis)
        axis.set_xlabel('Dense width $n$')
        _panel(axis, letter, title)
        axis.labels_ = labels
    axes[0].set_ylabel('Worst-time error / dense vs. dense')
    axes[0].set_ylim(.1, 4)
    for axis in axes:
        _direct_labels(axis, axis.labels_, widths[-1]*1.15)
    return figure


def draw_dense_pairs(data):
    """Discrepancy between independent dense networks, against width."""
    rows = [row for row in data['summary'] if row['count']]
    widths = [row['width'] for row in rows]
    figure, axes = _panels(sharey=True, wspace=.1)
    for axis, (letter, metric, title) in zip(axes, (('a', 'endpoint_rms', 'End of training'),
                                                     ('b', 'max_time_rms', 'Worst time'))):
        for row in rows:
            axis.scatter([row['width']]*len(row[metric]['values']), row[metric]['values'], s=6,
                         color=MUTED, alpha=.5, lw=0)
        mean = [row[metric]['mean'] for row in rows]
        axis.plot(widths, mean, color=INK, marker='o', lw=1.3)
        grid = np.geomspace(widths[0], widths[-1], 50)
        coefficient = data['descriptive_sqrt_fits'][metric]
        axis.plot(grid, coefficient/np.sqrt(grid), color=MUTED, lw=.9, linestyle=(0, (3, 2)))
        _width_ticks(axis, widths)
        axis.set_xlim(widths[0]/1.2, widths[-1]*2.2)
        axis.spines['bottom'].set_bounds(widths[0], widths[-1])
        axis.set_yscale('log')
        _log_ticks(axis.yaxis, narrow=True)
        axis.set_xlabel('Dense width $n$')
        _panel(axis, letter, title)
        axis.labels_ = [(mean[-1], 'mean', INK), (coefficient/np.sqrt(widths[-1]), r'$c/\sqrt{n}$', MUTED)]
    axes[0].set_ylabel('Dense vs. dense RMS')
    for axis in axes:
        _direct_labels(axis, axis.labels_, widths[-1]*1.12)
    return figure


def draw_costs(data):
    """Recorded costs as a minimal ruled table (also written as LaTeX)."""
    times = [('source_seconds', 'Source'), ('build_seconds', 'Build'), ('training_seconds', 'Training'),
             ('query_seconds', 'Queries')]
    storage = [('learned_mib', 'Learned'), ('fixed_mib', 'Fixed'), ('total_mib', 'Total')]
    blocks = [('circle', 'Circle, $d = 2$'), ('digits', 'Digits 1 vs 7, $d = 64$')]

    def model(label):
        name, _, config = label.partition(' ')
        config = config.replace('k=', 'q=').replace(', ', ',\\ ')
        return name + (f', ${config}$' if config else '')

    def cell(value, sd):
        if abs(value) < 5e-3:
            return '–'
        return f'{value:.2f}' if sd < 5e-3 else f'{value:.2f} ± {sd:.2f}'

    table = []
    for key, title in blocks:
        rows = [row for row in data['rows'] if row['panel'] == key]
        if rows:
            table.append((title, None))
            for row in rows:
                summary = row['summary']
                table.append((model(row['label']),
                              [cell(summary[f]['mean'], summary[f]['sample_sd']) for f, _ in times]
                              + [f'{summary[f]["mean"]:.1f}' for f, _ in storage]))
    columns = [.0, .38, .51, .64, .745, .845, .92, 1.0]  # right edges except the first (left)
    height = .19*(len(table)+3)
    figure, axis = plt.subplots(figsize=(TEXT_WIDTH, height))
    figure.subplots_adjust(left=.01, right=.99, top=.97, bottom=.03)
    axis.axis('off')
    step = 1/(len(table)+2.6)
    y = 1-.5*step

    def rule(y, width=.8, start=0., stop=1.):
        axis.plot([start, stop], [y, y], color=INK, lw=width, transform=axis.transAxes, clip_on=False)

    rule(1, .9)
    put = lambda x, y, text, **kw: axis.text(x, y, text, transform=axis.transAxes, va='center', **kw)
    put(.505, y, 'Recorded time (s)', ha='center')
    put(.9, y, 'Storage (MiB)', ha='center')
    rule(y-.45*step, .4, .26, .75)
    rule(y-.45*step, .4, .78, 1.)
    y -= step
    for j, (_, name) in enumerate(times+storage):
        put(columns[j+1], y, name, ha='right')
    put(0, y, 'Model', ha='left')
    rule(y-.5*step, .5)
    for label, cells in table:
        y -= step
        if cells is None:
            put(0, y, label, ha='left', style='italic', color=MUTED)
            continue
        put(.015, y, label, ha='left')
        for j, text in enumerate(cells):
            put(columns[j+1], y, text, ha='right')
    rule(y-.55*step, .9)
    lines = [r'\begin{tabular}{@{}lrrrrrrr@{}}', r'\toprule',
             r' & \multicolumn{4}{c}{Recorded time (s)} & \multicolumn{3}{c}{Storage (MiB)}\\',
             r'\cmidrule(lr){2-5}\cmidrule(l){6-8}',
             'Model & ' + ' & '.join(name for _, name in times+storage) + r'\\', r'\midrule']
    for label, cells in table:
        if cells is None:
            lines.append(rf'\multicolumn{{8}}{{@{{}}l}}{{\emph{{{label}}}}}\\')
        else:
            lines.append(' & '.join([label]+[c.replace('±', r'$\pm$').replace('–', '--') for c in cells]) + r'\\')
    lines += [r'\bottomrule', r'\end{tabular}']
    figure.latex_table = '\n'.join(lines)+'\n'
    return figure


# ----------------------------------------------------------------------------- earlier radial and sphere data

def _radial_panels(data, depth):
    description = json.loads(str(data['description_json']))[depth]
    panels = []
    for i, info in enumerate(description):
        prefix = f'{depth}_{i}_'
        predictions = {p: data[prefix+f'P{p}'] for p in info['orders']}
        for p, expected in info['rms'].items():
            actual = np.sqrt(np.mean((predictions[int(p)]-predictions[0])**2))
            if not np.isclose(actual, expected, rtol=2e-11, atol=2e-13):
                raise ValueError('Radial bundle metric mismatch')
        panels.append((info['title'], data[prefix+'angles'], data[prefix+'train_angles'],
                       data[prefix+'labels'], predictions, {int(p): v for p, v in info['rms'].items()}))
    return panels


def _radial_gallery(data, depth):
    panels = _radial_panels(data, depth)
    orders = sorted(panels[0][4])[1:]
    palette = dict(zip(orders, ['#9bbfea', '#3f84d8', '#1d5ba6'] if len(orders) == 3 else LEGENDRE_ORDERS.values()))

    def style(order):
        if order == 0:
            return dict(color=INK, lw=1.5, zorder=2)
        return dict(color=palette[order], lw=1, zorder=3+order,
                    linestyle=(0, (3, 1.5)) if order == orders[-1] else '-')

    figure = plt.figure(figsize=(TEXT_WIDTH, 4.1))
    grid = figure.add_gridspec(2, 6, left=.01, right=.99, bottom=.11, top=.94, wspace=.1, hspace=.34)
    slots = [grid[0, 0:2], grid[0, 2:4], grid[0, 4:6], grid[1, 1:3], grid[1, 3:5]]
    for slot, (title, angles, train_angles, labels, predictions, rms) in zip(slots, panels):
        axis = figure.add_subplot(slot)
        curves = [(predictions[0], style(0))]+[(predictions[p], style(p)) for p in orders]
        _polar(axis, angles, curves, (train_angles, labels))
        axis.set_title(title.replace(' · ', ', '), pad=0)
        text = '   '.join(f'$q={p}$: {rms[p]:.2g}' for p in orders)
        axis.text(.5, -.01, 'RMS  '+text, transform=axis.transAxes, ha='center', va='top', color=MUTED,
                  fontsize=6.5)
    _legend_row(figure, [('dense', style(0))]+[(f'Legendre, $q = {p}$', style(p)) for p in orders]
                + [('training labels', 'dot')], y=-.005)
    return figure


def draw_radial_gallery(data):
    """Five circle tasks at their own fitted endpoints, three hidden layers."""
    return _radial_gallery(data, 'deep')


def draw_radial_shallow(data):
    """Five circle tasks at their own fitted endpoints, two hidden layers."""
    return _radial_gallery(data, 'shallow')


def _sphere_views(data, resolution=360):
    import scipy.spatial
    legacy = _module('scripts/figures.py')  # its surface interpolation, without its PDF writer
    legacy.ConvexHull, legacy.cKDTree = scipy.spatial.ConvexHull, scipy.spatial.cKDTree
    surface = legacy.SphereSurface(data['test_inputs'])
    return legacy, {back: surface.texture_coordinates(resolution, back) for back in (False, True)}


def _sphere_figure(data, kind):
    meta = json.loads(str(data['metadata_json']))
    for order in (1, 2, 3):
        measured = np.sqrt(np.mean((data[f'P{order}']-data['dense'])**2))
        if not np.isclose(measured, meta['rms'][f'P{order}'], rtol=1e-12, atol=1e-14):
            raise ValueError('Sphere bundle RMS mismatch')
    legacy, views = _sphere_views(data)
    dense = data['dense']
    if kind == 'comparison':
        fields = [(dense, 'dense', None, True), (data['P3'], 'Legendre, $q = 3$', None, True),
                  (data['P3']-dense, 'difference', 3, False)]
    else:
        fields = [(dense, 'dense', None, True)]+[(data[f'P{p}']-dense, f'Legendre, $q = {p}$', p, False)
                                                  for p in (1, 2, 3)]
    output_limit, error_limit = legacy.OUTPUT_LIMIT, legacy.ERROR_LIMIT
    cmap = mpl.colors.LinearSegmentedColormap.from_list('signed', DIVERGING)
    columns = len(fields)
    figure = plt.figure(figsize=(TEXT_WIDTH, 3.5 if columns == 4 else 3.3))
    grid = figure.add_gridspec(3, columns, left=.05, right=.99, top=.9, bottom=.02, wspace=.06, hspace=.06,
                               height_ratios=[1, 1, .28])
    lat, lon = np.linspace(-np.pi/2, np.pi/2, 300), np.linspace(0, 2*np.pi, 600)
    graticule = [np.column_stack([np.cos(a)*np.cos(lon), np.cos(a)*np.sin(lon), np.full_like(lon, np.sin(a))])
                 for a in np.deg2rad([-60, -30, 0, 30, 60])]
    graticule += [np.column_stack([np.cos(lat)*np.cos(b), np.cos(lat)*np.sin(b), np.sin(lat)])
                  for b in np.deg2rad(range(0, 360, 60))]
    for column, (values, title, order, is_output) in enumerate(fields):
        limit = output_limit if is_output else error_limit
        if np.max(np.abs(values)) > limit+1e-10:
            raise ValueError('Colour limits would clip data')
        for row, back in enumerate((False, True)):
            axis = figure.add_subplot(grid[row, column])
            inside, indices, weights = views[back]
            field = np.full(inside.shape, np.nan)
            field[inside] = np.sum(values[indices]*weights, axis=1)
            axis.imshow(field, cmap=cmap, vmin=-limit, vmax=limit, extent=(-1, 1, -1, 1), interpolation='bilinear')
            basis = legacy.sphere_camera(back)
            for line in graticule:
                for piece in legacy.visible_segments(line, basis):
                    axis.plot(piece[:, 0], piece[:, 1], color=INK, lw=.25, alpha=.25)
            ring = np.linspace(0, 2*np.pi, 300)
            axis.plot(np.cos(ring), np.sin(ring), color='#c9c8c2', lw=.6)
            projected = data['inputs'] @ basis.T
            front = projected[:, 2] > 0
            axis.scatter(projected[front, 0], projected[front, 1], s=4, color=INK, edgecolors='white',
                         linewidths=.4, zorder=5)
            axis.set(xlim=(-1.04, 1.04), ylim=(-1.04, 1.04), aspect='equal')
            axis.axis('off')
            if row == 0:
                axis.set_title(title, pad=11)
                if order:
                    axis.text(.5, 1.01, f'RMS {meta["rms"][f"P{order}"]:.4f}', transform=axis.transAxes,
                              ha='center', va='bottom', color=MUTED, fontsize=6.5)
            if column == 0:
                axis.text(-.02, .5, 'back' if back else 'front', transform=axis.transAxes, rotation=90,
                          ha='right', va='center', color=MUTED)
    bars = [(0, 1, output_limit, 'prediction')] if kind != 'comparison' else [(0, 2, output_limit, 'prediction')]
    bars.append((1, columns, error_limit, 'minus dense') if kind != 'comparison' else (2, 3, error_limit, 'minus dense'))
    for start, stop, limit, label in bars:
        slot = grid[2, start:stop].get_position(figure)
        width = min(slot.width*.8, .3)
        axis = figure.add_axes([slot.x0+(slot.width-width)/2, slot.y0+slot.height*.55, width, slot.height*.18])
        bar = figure.colorbar(mpl.cm.ScalarMappable(mpl.colors.Normalize(-limit, limit), cmap), cax=axis,
                              orientation='horizontal', ticks=[-limit, 0, limit])
        bar.outline.set_visible(False)
        axis.tick_params(length=2, pad=1.5)
        axis.set_xticklabels([f'{-limit:g}'.replace('-', '−'), '0', f'{limit:g}'])
        axis.set_title(label, pad=2, color=MUTED, fontsize=7)
    return figure


def draw_sphere_orders(data):
    """Dense output and the three Legendre differences on both hemispheres."""
    return _sphere_figure(data, 'orders')


def draw_sphere_comparison(data):
    """Dense output, Legendre order 3 and their difference on both hemispheres."""
    return _sphere_figure(data, 'comparison')


def draw_paired_projection(_):
    """Schematic: pairing two projected histories multiplies their errors."""
    figure, axis = plt.subplots(figsize=(TEXT_WIDTH, 1.9))
    figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
    axis.set(xlim=(0, 10), ylim=(0, 3.1))
    axis.axis('off')
    blue = METHOD['legendre']['color']
    cells = [(1.9, 1.55, r'$\int b_P h_P^\top$', 'kept', '#dfeafa'),
             (3.7, 1.55, r'$\int b_P h_\perp^\top = 0$', '', '#f3f2ee'),
             (1.9, .25, r'$\int b_\perp h_P^\top = 0$', '', '#f3f2ee'),
             (3.7, .25, r'$\int b_\perp h_\perp^\top$', 'the whole error', '#fbe7dd')]
    for x, y, formula, note, colour in cells:
        axis.add_patch(mpl.patches.FancyBboxPatch((x, y), 1.7, 1.15, boxstyle='round,pad=0,rounding_size=.08',
                                                  facecolor=colour, edgecolor='none'))
        axis.text(x+.85, y+.62, formula, ha='center', va='center', fontsize=9, math_fontfamily='dejavusans')
        if note:
            axis.text(x+.85, y+.2, note, ha='center', va='center', color=MUTED, fontsize=7)
    for x, text in ((2.75, r'retained $h_P$'), (4.55, r'omitted $h_\perp$')):
        axis.text(x, 2.9, text, ha='center', va='center', color=blue)
    for y, text in ((2.12, r'retained $b_P$'), (.82, r'omitted $b_\perp$')):
        axis.text(1.75, y, text, ha='right', va='center', color=blue)
    axis.text(5.9, 2.15, 'Orthogonal projection removes both mixed terms,', va='center')
    axis.text(5.9, 1.8, 'so only omitted × omitted remains:', va='center')
    axis.text(5.9, 1.05, r'$\left\Vert\int b h^\top-\int b_P h_P^\top\right\Vert_F'
              r'\;\leq\;\Vert b-b_P\Vert_{L^2}\,\Vert h-h_P\Vert_{L^2}$', va='center', fontsize=9,
              math_fontfamily='dejavusans')
    return figure


if __name__ == '__main__':
    raise SystemExit(main())
