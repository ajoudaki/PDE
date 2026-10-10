#!/usr/bin/env python3
"""Render the selected paper inventory from saved inputs, never from training.

No arguments renders all figures into a fresh, study-owned output directory.
Use --list, --check, --only NAME..., or --out DIR. --export-data DIR packages
the plotting inputs; --data-dir DIR subsequently renders from that package.
Legacy vector artwork uses the existing safe renderers and needs pdflatex,
pdftoppm, ReportLab, SciPy and Pillow. No PyTorch or GPU is used.
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
import subprocess
import sys
import tempfile

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
    'radial_trajectory': ('response', 'legacy', 'main',
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
        'raw query RMS, mean +/- sample SD and dashed dense-pair error. Only '
        'declared inputs and recorded positive times are shown. Sources use '
        'full-horizon rollout. Nonpositive SD lower bounds use a display floor.'),
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
        'Fixed compact width 512: mean/sample SD of per-pair ratios of maximum-recorded '
        'compression RMS to maximum-recorded dense-pair RMS; crosses show all three '
        'pairs. All complete candidates are included regardless of passing. Source '
        'settings can vary with dense width. Nonpositive lower SD bounds are omitted. '
        'Saved finite-grid observations, with no smoothing or new training.'),
    'robustness': ('robustness', 'draw_robustness', 'appendix',
        'Corrected dimension candidates and five single-seed architecture cases. '
        'Dimension selection uses max(error)/max(dense pair) <= 1; endpoint '
        'agreement is not an additional selection filter. Different targets and '
        'panel projection variants are marked. Architecture uses one shared '
        'regularized empirical configuration, not a new theorem certificate.'),
    'sphere_orders': ('sphere', 'legacy', 'appendix',
        'Earlier population response-memory endpoint experiment: four ReLU layers, '
        'width 2048, 64 training points, 8192 equal-area queries, one seed and '
        'Euler step 1/128. Models stop individually at training RMS <= 0.01, '
        'not common times. Both hemispheres and shared error scales are shown. '
        'ReLU is outside the analytic-activation theorem; saved-data replotting '
        'does not reproduce the unavailable historical training producer.'),
    'radial_gallery': ('radial', 'legacy', 'appendix',
        'Five earlier Legendre tasks, three tanh hidden layers, width 4096, '
        'orders 1/2/3. Each model is at its own training-MSE 0.001 endpoint, '
        'not a shared time. RMS uses all 8192 angles; radius is 3 + prediction.'),
    'same_rank': ('response', 'legacy', 'appendix',
        'Older paired-label endpoint comparison: Legendre order 3 and two '
        'trained-factor seeds, both with correction rank bound 24. Equal rank '
        'does not mean equal total storage. Each fits training MSE 0.001 at its '
        'own time; RMS compares predictions against dense on 8192 circle queries.'),
    'paired_projection': (None, 'legacy', 'proof appendix',
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
        'sample SD; fitted inverse-square-root curves are descriptive.'),
    'dense_pairs_mnist': ('dense_pairs_mnist', 'draw_dense_pairs', 'appendix',
        'Three independent dense pairs per width on MNIST. Mean and sample SD; '
        'fitted inverse-square-root curves are descriptive.'),
    'radial_shallow': ('radial', 'legacy', 'alternative',
        'Earlier two-hidden-layer tanh circle gallery, width 2048, orders 1/3/7. '
        'Individually fitted training-MSE 0.001 endpoints; not common-time errors.'),
    'sphere_comparison': ('sphere', 'legacy', 'alternative',
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


def _pdf_preview(prefix, dpi):
    subprocess.run(['pdftoppm', '-f', '1', '-singlefile', '-r', str(dpi), '-png',
                    str(prefix.with_suffix('.pdf')), str(prefix)], check=True, timeout=60,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def _legacy(name, source, prefix, dpi):
    """Call only saved-data render functions; never legacy command-line defaults."""
    if name in ('radial_trajectory', 'same_rank'):
        module = _module('scripts/tikz_figures.py')
        module.RESPONSE_BUNDLE = source
        builder = module.trajectory if name == 'radial_trajectory' else module.same_rank_radial_preview
        tex = builder()
        with tempfile.TemporaryDirectory(prefix='paper-tikz-') as temp:
            path = Path(temp) / 'figure.tex'
            path.write_text(tex)
            result = subprocess.run(['pdflatex', '-no-shell-escape', '-interaction=nonstopmode',
                                     '-halt-on-error', path.name], cwd=temp,
                                    capture_output=True, text=True, timeout=60)
            if result.returncode:
                raise RuntimeError(result.stdout[-3000:])
            shutil.copyfile(Path(temp)/'figure.pdf', prefix.with_suffix('.pdf'))
        prefix.with_suffix('.tex').write_text(tex)
    elif name == 'paired_projection':
        with plt.rc_context():
            module = _module('figures/experimental_figures.py')
            figure = module.pairing({}, {})
            for label in figure.texts:
                if label.get_position()[1] > .88 or label.get_position()[1] < .065:
                    label.set_visible(False)
            _save(figure, prefix, dpi)
        return [PAPER/'figures/experimental_figures.py']
    else:
        module = _module('scripts/figures.py')
        sphere = name.startswith('sphere_')
        module.load_plotting(sphere=sphere)
        if not sphere:
            depth = 'shallow' if name == 'radial_shallow' else 'deep'
            module.draw_circle_figure(module.load_circle_bundle(source)[depth], prefix, depth)
        else:
            with np.load(source, allow_pickle=False) as archive:
                data = {key: archive[key].copy() for key in archive.files if key != 'metadata_json'}
                metadata = json.loads(str(archive['metadata_json']))
            for order in (1, 2, 3):
                measured = np.sqrt(np.mean((data[f'P{order}']-data['dense'])**2))
                if not np.isclose(measured, metadata['rms'][f'P{order}'], rtol=1e-12, atol=1e-14):
                    raise ValueError('Sphere bundle RMS mismatch')
            surface = module.SphereSurface(data['test_inputs'])
            coordinates = {back: surface.texture_coordinates(500, back) for back in (False, True)}
            module.draw_sphere_figure(prefix, data, metadata, coordinates,
                                     'orders' if name == 'sphere_orders' else 'comparison')
    _pdf_preview(prefix, dpi)
    return [PAPER/('scripts/tikz_figures.py' if name in ('radial_trajectory', 'same_rank')
                  else 'scripts/figures.py')]


def draw_moments(data):
    """Redraw the cached illustration; this function never trains a network."""
    history, fits = data['histories'], data['fits']
    figure, axes = plt.subplots(2, 3, figsize=(11.5, 3.6),
                                gridspec_kw={'height_ratios': [2, 1]})
    colors = ['#2F6DB5', '#C8553D', '#3A8A6B']
    time = np.linspace(0, 1, len(history))
    for order, title in enumerate(['Mean', '+ linear trend', '+ quadratic shape']):
        axis = axes[0, order]
        for neuron, color in enumerate(colors):
            values = np.r_[history[:, neuron], fits[:, :, neuron].ravel()]
            lower, upper = values.min(), values.max()
            scale = lambda v: 2-neuron + .8*(v-lower)/max(upper-lower, 1e-12)
            axis.plot(time, scale(history[:, neuron]), color=color, linewidth=1.4)
            axis.plot(time, scale(fits[order, :, neuron]), color='.2', linestyle='--', linewidth=1)
        axis.set(title=f'q = {order+1}: {title}', xticks=[0, 1], xticklabels=['Start', 'Now'], yticks=[])
        axis.text(.5, .97, f'Median error {100*data["median_errors"][order]:.0f}% of range',
                  transform=axis.transAxes, ha='center', va='top', fontsize=8, color='.4')
        axis.set_ylim(-.1, 3.4)
        now, halfway = data['coefficients'][order], data['halfway_coefficients'][order]
        lower, upper = np.percentile(np.r_[now, halfway], [1, 99])
        grid = np.linspace(lower-.12*(upper-lower), upper+.12*(upper-lower), 200)
        for values, style, label in [(now, '-', 'Now'), (halfway, '--', 'Halfway in learning clock')]:
            bandwidth = max(1.06*values.std()*len(values)**(-.2), 1e-12)
            density = np.exp(-.5*((grid[:, None]-values[None, :])/bandwidth)**2).sum(axis=1)
            axes[1, order].plot(grid, density, style, color='.45', linewidth=1, label=label)
        axes[1, order].set(title=f'Coefficient {order}', xticks=[], yticks=[])
        for row in axes:
            row[order].spines[['top', 'right', 'left']].set_visible(False)
    axes[0, 0].set_ylabel('Three neuron histories')
    axes[1, 0].set_ylabel('512 neurons')
    handles, labels = axes[1, 0].get_legend_handles_labels()
    figure.legend(handles, labels, loc='lower center', ncol=2, frameon=False)
    figure.tight_layout(rect=(0, .09, 1, 1))
    return figure


def _save(figure, prefix, dpi):
    for extension in ('pdf', 'png'):
        figure.savefig(prefix.with_suffix('.'+extension), dpi=dpi, bbox_inches='tight')
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
    parser.add_argument('--dpi', type=int, default=180)
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
    global np, plt
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from threadpoolctl import threadpool_limits
    plt.rcParams.update({'font.size': 10, 'pdf.fonttype': 42, 'savefig.facecolor': 'white'})
    record = dict(command=[sys.executable, str(Path(__file__).resolve()), *(argv or sys.argv[1:])],
                  python=platform.python_version(), numpy=np.__version__, matplotlib=matplotlib.__version__,
                  plotting_source_sha256=_sha(__file__), training_performed=False, gpu_used=False,
                  inputs={key: dict(path=str(path), sha256=_sha(path)) for key, path in inputs.items()},
                  figures={}, errors={})
    cache = {}
    with threadpool_limits(limits=1):
        for name in names:
            key, renderer, placement, caption = FIGURES[name]
            prefix = output/name
            try:
                dependencies = []
                if renderer == 'legacy':
                    dependencies = _legacy(name, inputs.get(key), prefix, args.dpi)
                else:
                    if key not in cache:
                        if inputs[key].suffix == '.json':
                            cache[key] = json.loads(inputs[key].read_text())
                        else:
                            with np.load(inputs[key], allow_pickle=False) as archive:
                                cache[key] = {field: archive[field].copy() for field in archive.files}
                    with plt.rc_context():
                        _save(globals()[renderer](cache[key]), prefix, args.dpi)
                prefix.with_suffix('.caption.txt').write_text(caption+'\n')
                record['figures'][name] = dict(placement=placement, caption=caption,
                    outputs={path.name: _sha(path) for path in output.glob(name+'.*')},
                    renderer_sources={str(path.relative_to(ROOT)): _sha(path) for path in dependencies})
                print(f'[{len(record["figures"])}/{len(names)}] {name}', flush=True)
            except Exception as error:
                record['errors'][name] = f'{type(error).__name__}: {error}'
                print(f'FAILED {name}: {error}', file=sys.stderr, flush=True)
            (output/'manifest.json').write_text(json.dumps(record, indent=2)+'\n')
    print(f'Figures and captions: {output}')
    return int(bool(record['errors']))


# Saved-result renderers are defined below; they perform no file IO or training.
def _main_style():
    return {'font.size': 10, 'axes.spines.top': False,
            'axes.spines.right': False, 'pdf.fonttype': 42,
            'savefig.facecolor': 'white'}


def draw_storage(data):
    """Render saved width/group means and saved fit coefficients."""
    from matplotlib.ticker import NullFormatter

    widths = np.asarray(data['widths'])
    panels = [('Toy circle (d = 2)', data['toy_groups']),
              ('Digits 1 vs 7 (d = 64)', data['digits_groups'])]
    styles = {'legendre': ('Legendre', '#185b84', 's'),
              'harmonic': ('Harmonic', '#dd8822', '^'),
              'logarithmic': ('Taylor', '#228833', 'o')}
    with plt.rc_context(_main_style()):
        figure, axes = plt.subplots(1, 2, figsize=(11.5, 4.5), sharex=True, sharey=True)
        for axis, (title, groups) in zip(axes, panels):
            for family, (label, color, marker) in styles.items():
                if family not in groups:
                    continue
                values = [group['mean'] for group in groups[family]]
                axis.plot(widths, values, color=color, marker=marker, linewidth=2,
                          markersize=5, label=label)
                fit = data['fits'][title].get(family)
                if fit is not None:
                    grid = np.geomspace(widths[0], widths[-1], 250)
                    values = fit['coefficient'] * np.log(grid)**fit['exponent']
                    axis.plot(grid, values,
                              color=color if family == 'harmonic' else '#333333',
                              linestyle='--', linewidth=1.5,
                              label=rf'{label} fit: $(\log n)^{{{fit["exponent"]:.2f}}}$')
            axis.set(xscale='log', yscale='log', xlabel='Dense width n', title=title)
            axis.set_xticks(widths, [str(n) for n in widths])
            axis.xaxis.set_minor_formatter(NullFormatter())
            axis.tick_params(axis='x', labelsize=8)
            axis.grid(alpha=.2)
            axis.legend(fontsize=8, frameon=False)
        axes[0].set_ylabel('Mean learned scalars')
        figure.text(.02, .02,
                    'Three seeds; trajectory RMS ≤ dense–dense. Fixed storage excluded.',
                    fontsize=9)
        figure.tight_layout(rect=(0, .06, 1, 1))
    return figure


def draw_accuracy(data):
    """Render saved paired summaries, original controls, and incomplete budgets."""
    styles = {'legendre': ('Legendre', '#4477AA', 's'),
              'harmonic': ('Harmonic', '#EE7733', '^'),
              'logarithmic': ('Taylor', '#228833', 'o'),
              'dense': ('Dense', '#666666', 'D'),
              'low_rank': ('Low rank', '#CC6677', 'v')}
    families = ('legendre', 'harmonic', 'logarithmic')

    def metric_values(groups, metric, statistic):
        return [group[metric][statistic] if group['status'] == 'complete' else np.nan
                for group in groups]

    with plt.rc_context(_main_style()):
        figure, axes = plt.subplots(1, 2, figsize=(11.8, 4.8), sharex=True)
        for axis, panel, title in zip(axes, ('sphere', 'digits'),
                                      ('3D sphere', 'Digits 1 vs 7')):
            result = data['panels'][panel]
            for family, (label, color, marker) in styles.items():
                if family in families:
                    selected = sorted((group for group in result['summaries'].values()
                                       if group['family'] == family),
                                      key=lambda group: group['moving'])
                    if not selected:
                        continue
                    x = [group['moving'] for group in selected]
                    # A missing repetition produces a gap, never a partial mean.
                    axis.errorbar(x, metric_values(selected, 'endpoint_rms', 'mean'),
                                  yerr=metric_values(selected, 'endpoint_rms', 'sd'),
                                  color=color, marker=marker, markersize=4.5,
                                  linewidth=1.2, capsize=3, elinewidth=1, label=label)
                    if panel == 'digits' and family == 'logarithmic':
                        axis.errorbar(
                            x, metric_values(selected, 'extra_endpoint_rms', 'mean'),
                            yerr=metric_values(selected, 'extra_endpoint_rms', 'sd'),
                            linestyle=':', marker=marker, markerfacecolor='white',
                            color=color, markersize=5, linewidth=1, capsize=3,
                            elinewidth=1, label='Taylor, undeclared')
                else:
                    selected = sorted(
                        (point for point in result['fixed_original_reference_controls']
                         if point['family'] == family), key=lambda point: point['moving'])
                    if not selected:
                        continue
                    axis.plot([point['moving'] for point in selected],
                              [point['endpoint_rms'] for point in selected],
                              color=color, marker=marker, markersize=4.5,
                              linewidth=1.2, label=label)
                    for point in selected:
                        summary = result['fixed_original_reference_dense_summaries'].get(point['name'])
                        if summary:
                            deviation = ([[summary['median']-summary['minimum']],
                                          [summary['maximum']-summary['median']]]
                                         if panel == 'sphere' else summary['endpoint_rms']['sd'])
                            axis.errorbar(point['moving'], point['endpoint_rms'],
                                          yerr=deviation, fmt='none', color=color,
                                          capsize=3, linewidth=1)
            for name, metric, label, color, linestyle in (
                    ('frozen_features', 'endpoint_rms', 'Frozen features', '#AA4499', '--'),
                    ('dense_pair', 'endpoint_rms', 'Dense benchmark', '#333333', ':'),
                    ('dense_pair', 'extra_endpoint_rms', 'Dense benchmark, undeclared', '#999999', '-.')):
                group = result['summaries'][name]
                if group['status'] != 'complete' or metric not in group:
                    continue
                mean, deviation = group[metric]['mean'], group[metric]['sd']
                if mean is None or deviation is None:
                    continue
                axis.axhline(mean, color=color, linestyle=linestyle, linewidth=1, label=label)
                axis.axhspan(mean-deviation, mean+deviation, color=color, alpha=.09, linewidth=0)
            incomplete = [group for group in result['summaries'].values()
                          if group['status'] != 'complete']
            if incomplete:
                missing = ', '.join(sorted({styles[group['family']][0] for group in incomplete
                                           if group['family'] in styles}))
                axis.text(.02, .03, f'{missing}: {len(incomplete)} incomplete budget'
                          + ('s' if len(incomplete) > 1 else ''),
                          transform=axis.transAxes, fontsize=8, color='#AA3333',
                          bbox=dict(facecolor='white', edgecolor='none', alpha=.9))
            axis.set(xscale='log', yscale='log', xlabel='Learned scalars', title=title,
                     xlim=data['shared_learned_limits'])
            axis.grid(alpha=.15)
        axes[0].set_ylabel('Endpoint query RMS')
        legend = {}
        for axis in axes:
            handles, labels = axis.get_legend_handles_labels()
            legend.update(zip(labels, handles))
        figure.legend(legend.values(), legend.keys(), loc='upper center', ncol=4,
                      frameon=False, fontsize=8.5)
        figure.tight_layout(rect=(0, 0, 1, .81))
    return figure


def draw_trajectory(data):
    """Render the selected raw-RMS snapshot with compression and dense-pair curves."""
    styles = {'legendre': ('Legendre', '#4477AA'),
              'harmonic': ('Harmonic', '#EE7733'),
              'logarithmic': ('Taylor', '#228833'),
              'dense_pair': ('Dense–dense', '#333333')}
    times = np.asarray(data['times'])
    with plt.rc_context(_main_style()):
        figure, axes = plt.subplots(1, 2, figsize=(11.8, 4.8), sharex=True, sharey=True)
        for axis, panel, title in zip(axes, ('circle', 'digits'), ('Circle', 'Digits 1 vs 7')):
            for family, summary in data['panels'][panel]['summaries'].items():
                if family not in styles:
                    continue
                mean, sd = np.asarray(summary['mean']), np.asarray(summary['sd'])
                label, color = styles[family]
                floor = float(mean.min())*1e-3
                axis.plot(times, mean, color=color, label=label, linewidth=1.5,
                          linestyle='--' if family == 'dense_pair' else '-')
                axis.fill_between(times, np.where(mean-sd > 0, mean-sd, floor), mean+sd,
                                  color=color, alpha=.12, linewidth=0)
            axis.set(yscale='log', xlabel='Training time', title=title, xlim=(0, 32))
            axis.grid(alpha=.15)
        axes[0].set_ylabel('Test RMS')
        display_floor = .5*min(np.min(line.get_ydata()) for axis in axes for line in axis.lines)
        axes[0].set_ylim(bottom=display_floor)
        handles, labels = axes[0].get_legend_handles_labels()
        figure.legend(handles, labels, loc='upper center', ncol=4, frameon=False, fontsize=8.5)
        figure.tight_layout(rect=(0, 0, 1, .91))
    return figure


def _app_finish(figure, axes, note=""):
    for axis in np.asarray(axes, dtype=object).ravel():
        axis.spines[["top", "right"]].set_visible(False)
        axis.grid(alpha=.15)
    figure.tight_layout(rect=(0, .12 if note else 0, 1, 1))
    if note:
        figure.text(.02, .015, note, fontsize=8, va="bottom")
    return figure


def _app_taylor_label(name):
    _, width, rank = name.split("_")
    return f"Taylor width {width}, rank {rank.removeprefix('r')}"


def draw_spectra(data):
    """Use appendix_saved_metrics.json: history_spectra, spectral_inconclusive."""
    rows = sorted(data["history_spectra"], key=lambda row: row["width"])
    figure, axes = plt.subplots(1, 3, figsize=(11.8, 3.8))
    colors = ["#2563eb", "#d97706", "#16856c", "#8b5bb7", "#c44848"]
    for index, row in enumerate(rows):
        values = row["normalized_singular_values"]
        axes[0].loglog(np.arange(1, len(values) + 1), values,
                       color=colors[index % len(colors)], linewidth=1.2,
                       label=f"n={row['width']}")
    axes[0].set(xlabel="Singular-value index", ylabel=r"$\sigma_j/\|H_\perp\|_F$",
                title="Saved dense activation histories", ylim=(1e-10, 1.5))
    widths = [row["width"] for row in rows]
    for tolerance, marker, label in (("0.01", "o", "1% tail"),
                                      ("0.001", "s", "0.1% tail")):
        axes[1].plot(widths, [row["fixed_tolerance_ranks"][tolerance] for row in rows],
                     marker=marker, label=label)
    axes[1].plot(widths, [row["shrinking_tolerance_rank"] for row in rows],
                 "^--", color="#ad3b70", label=r"$0.01\sqrt{512/n}$ tail")
    axes[1].set(xlabel="Dense width n", ylabel="Required history rank",
                title="Relative Frobenius-tail tolerance", xscale="log")
    for field, label, marker in (("original_history_rms", "Before projection", "s"),
                                 ("projected_history_rms", "After projection", "o")):
        axes[2].plot(widths, [row[field] for row in rows], marker=marker, label=label)
    axes[2].set(xlabel="Dense width n", ylabel="History RMS",
                title="Measured history size", xscale="log")
    for axis in axes[1:]:
        axis.set_xticks(widths, [str(width) for width in widths])
    for axis in axes:
        axis.legend(frameon=False, fontsize=7)
    note = "Circle pilot; empirical history ranks, one seed. No prediction-error guarantee."
    missing = data.get("spectral_inconclusive", [])
    if missing:
        note += "\nInconclusive widths: " + ", ".join(str(row["width"]) for row in missing)
    return _app_finish(figure, axes, note)


def draw_query_distance(data):
    """Use feedback/scope/report.json: plan.paths, controlled_paths."""
    paths = data["plan"]["paths"]
    figure, axis = plt.subplots(figsize=(6.4, 4.0))
    for name, row in data["controlled_paths"].items():
        dense = name.startswith("dense_")
        label = "Independent dense pair" if dense else _app_taylor_label(name)
        axis.plot(paths["angles"], row["endpoint_rms_by_angle"], marker="o", ms=3,
                  linestyle="--" if dense else "-", label=label)
    axis.set(xlabel="Angular distance from declared anchor (radians)",
             ylabel=f"Endpoint RMS across {paths['path_count']} fixed paths",
             title="Controlled query paths · d=10, n=2048")
    axis.legend(frameon=False, fontsize=8)
    return _app_finish(figure, [axis],
        "One seed; extra path inputs withheld from source setup.\n"
        "Zero distance includes the actual anchor error; no anchor-error subtraction.")


def draw_robustness(data):
    """Use robustness/metrics.json: dimensions, selected, architecture."""
    from matplotlib.lines import Line2D
    dimensions, selected = data["dimensions"], data["selected"]
    architecture = data["architecture"]
    figure, axes = plt.subplots(1, 2, figsize=(12.5, 4.8))
    colors = {"harmonic": "#EE7733", "logarithmic": "#228833"}
    labels = {"harmonic": "Harmonic", "logarithmic": "Taylor"}
    ds = [2, 3, 10, 64, 784]
    for family in colors:
        for index, dimension in enumerate(ds):
            candidates = [row for row in dimensions[str(dimension)] if row["family"] == family]
            best = selected.get(str(dimension), {}).get(family)
            if best is None:
                if candidates:
                    axes[0].text(index, .035 + (.08 if family == "harmonic" else 0),
                        labels[family] + ": no pass", transform=axes[0].get_xaxis_transform(),
                        ha="center", fontsize=7, rotation=25, color=colors[family])
                continue
            offset = -.05 if family == "harmonic" else .05
            projected = dimension == 784
            axes[0].scatter(index + offset, best["learned"],
                marker="D" if family == "harmonic" else "o", s=45,
                facecolors="none" if projected else colors[family], edgecolors=colors[family])
            axes[0].scatter(index + offset, best["total"], marker="s", s=35,
                            facecolors="none", edgecolors=colors[family])
            if projected:
                axes[0].annotate("panel projection", (index + offset, best["learned"]),
                    xytext=(-5, -18), textcoords="offset points", ha="right",
                    fontsize=8, color=colors[family])
    for row in dimensions["2"]:
        if (row.get("variant") == "spatial-resolution repair"
                and row["family"] == "harmonic" and row["status"] == "fail"):
            axes[0].scatter(-.12, row["learned"], marker="x", color=colors["harmonic"], s=55)
            axes[0].scatter(-.12, row["total"], marker="x", color=".55", s=35)
            axes[0].annotate(f"probe {row['maximum_ratio']:.3f}×", (-.12, row["learned"]),
                xytext=(5, 8), textcoords="offset points", fontsize=8, color=colors["harmonic"])
    handles = [Line2D([], [], color=colors[family], marker="o", linestyle="none",
                      label=labels[family]) for family in colors]
    handles += [Line2D([], [], color="black", marker="o", linestyle="none", label="Learned"),
                Line2D([], [], color="black", marker="s", markerfacecolor="none",
                       linestyle="none", label="Total"),
                Line2D([], [], color=colors["harmonic"], marker="x", linestyle="none",
                       label="Failed small probe")]
    axes[0].legend(handles=handles, fontsize=8, frameon=False, ncol=2)
    axes[0].set(xticks=range(5), xticklabels=ds, yscale="log", xlabel="Input dimension d",
                ylabel="Retained scalars", title="Smallest TESTED passing learned state")
    axes[0].margins(y=.23)
    axes[0].text(.02, .98,
        "Selection: max(error) / max(dense pair) ≤ 1\nDifferent targets/variants; no scaling curve fitted",
        transform=axes[0].transAxes, va="top", fontsize=8)
    cases = ["baseline", "depth3", "depth4", "silu", "m16"]
    for index, case in enumerate(cases):
        row = architecture[case][0]
        if "maximum_ratio" not in row:
            axes[1].text(index, .06, "inconclusive", transform=axes[1].get_xaxis_transform(),
                         ha="center", fontsize=8, rotation=25)
            continue
        unresolved = row["status"] == "numerically_unresolved"
        for offset, field, marker in ((-.06, "endpoint_ratio", "o"),
                                       (.06, "maximum_ratio", "s")):
            axes[1].scatter(index + offset, row[field], marker=marker, s=45,
                facecolors="none" if unresolved else colors["logarithmic"],
                edgecolors=colors["logarithmic"])
        if unresolved:
            axes[1].annotate("numerically unresolved", (index, row["maximum_ratio"]),
                xytext=(0, 10), textcoords="offset points", ha="center", fontsize=7, color="#AA3344")
    axes[1].axhline(1, color=".4", linestyle="--", linewidth=1)
    axes[1].set(xticks=range(5), xticklabels=["Baseline\nL=2, tanh, m=8", "L=3", "L=4", "SiLU", "m=16"],
                yscale="log", ylabel="RMS / paired dense RMS", title="One shared Taylor configuration")
    axes[1].legend(handles=[Line2D([], [], color=colors["logarithmic"], marker=marker,
        linestyle="none", label=label) for marker, label in (("o", "Endpoint"), ("s", "Max / max recorded"))],
        frameon=False, fontsize=8)
    return _app_finish(figure, axes,
        "Single seed; full-horizon source compilation. Finite Euler measurements.\n"
        "Dimension variants are separate comparisons; no minimum-size or continuum guarantee.")


def draw_panel_size(data):
    """Use refresh scope/metrics.json: panel_size.records."""
    rows = data["panel_size"]["records"]
    sizes = [row["source_panel_size"] for row in rows]
    figure, axis = plt.subplots(figsize=(6.7, 4.1))
    for name, color in (("logarithmic_256_r15", "#009E73"), ("logarithmic_512_r37", "#0072B2")):
        axis.plot(sizes, [row["common_panel_models"][name]["endpoint_rms"] for row in rows],
                  "o-", label=_app_taylor_label(name), color=color)
    axis.plot(sizes, [row["common_dense_pair"]["endpoint_rms"] for row in rows], "--",
              color="#333333", label="Independent dense pair, common 8")
    axis.set(xlabel="Declared source query-panel size", ylabel="Endpoint prediction RMS on common 8 queries",
             title="Fixed compact budgets, fixed evaluation queries", xticks=sizes)
    axis.legend(frameon=False, fontsize=8)
    return _app_finish(figure, [axis],
        "Single seed, d=10, n=2048; the same eight evaluation queries at every size.\n"
        "Both compact budgets are fixed; this does not test a panel-dependent sufficient budget.")


def draw_transfer(data):
    """Use refresh scope/metrics.json: times, transfer.metrics, baseline_curve."""
    times = np.asarray(data["times"])
    transfer = data["transfer"]
    figure, axis = plt.subplots(figsize=(6.7, 4.1))
    for name, label, color in (("rebuilt", "Rebuilt for changed target", "#0072B2"),
                               ("transferred", "Original target sources", "#009E73"),
                               ("pooled", "Pooled non-target sources", "#D55E00")):
        curve = np.asarray(transfer["metrics"][name]["curve"])
        valid = (times > 0) & (curve > 0)
        axis.plot(times[valid], curve[valid], color=color, label=label)
    baseline = np.asarray(transfer["baseline_curve"])
    valid = (times > 0) & (baseline > 0)
    axis.plot(times[valid], baseline[valid], "--", color="#333333", label="Independent dense pair")
    axis.set(xlabel="Training time", ylabel="Declared-query prediction RMS", yscale="log",
             title="Changed-label source transfer at one fixed budget")
    axis.legend(frameon=False, fontsize=8)
    return _app_finish(figure, [axis],
        "One seed; full-horizon empirical sources; width 256, source rank 15.\n"
        "Changed training labels are outside the fixed-task theorem; source dilution is not a unique cause.")


def draw_costs(data):
    """Use costs_final/metrics.json: rows[*].panel, label, summary."""
    fields = ["source_seconds", "build_seconds", "training_seconds", "query_seconds",
              "learned_mib", "fixed_mib", "total_mib"]
    figure, axes = plt.subplots(2, 1, figsize=(12.4, 5.3))
    for axis, panel, title in zip(axes, ["circle", "digits"], ["Circle", "8×8 digits 1 vs 7"]):
        axis.axis("off")
        axis.set_title(title + " · selected Figure 4 configurations · three paired seeds", fontsize=11, pad=8)
        cells = []
        for row in data["rows"]:
            if row["panel"] != panel:
                continue
            formatted = []
            for field in fields:
                value = row["summary"][field]
                precision = 3 if field.endswith("_mib") or field in ("build_seconds", "query_seconds") else 2
                text = f"{value['mean']:.{precision}f}"
                if not field.endswith("_mib"):
                    text += f" ± {value['sample_sd']:.{precision}f}"
                formatted.append(text)
            cells.append([row["label"], *formatted])
        table = axis.table(cellText=cells, cellLoc="center", loc="center",
            colLabels=["Model", "Source (s)", "Build (s)", "Updates (s)", "Queries (s)",
                       "Learned (MiB)", "Fixed (MiB)", "Total (MiB)"],
            colWidths=[.21, .105, .105, .12, .12, .115, .115, .115])
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.9)
        for (row_index, _), cell in table.get_celld().items():
            cell.set_edgecolor("#dddddd")
            cell.set_linewidth(.5)
            if row_index == 0:
                cell.set_facecolor("#edf1f5")
                cell.set_text_props(weight="bold")
            elif row_index % 2 == 0:
                cell.set_facecolor("#f8f9fb")
    figure.suptitle("Recorded runtime and retained storage · mean ± sample SD", fontsize=13, y=.99)
    figure.text(.02, .015,
        "Saved offline setup and Euler runtimes; no new benchmark runs or demonstrated training-time speedup.\n"
        "Retained storage excludes workspace and source temporaries. Process GPU peaks are not model memory.",
        fontsize=8, va="bottom")
    figure.tight_layout(rect=(0, .12, 1, .94), h_pad=2)
    return figure


def draw_fixed_budget(data):
    """Render saved fixed-width candidates, retaining failed pairs and full upper SD."""
    from matplotlib.ticker import NullFormatter

    styles = {'harmonic': ('Harmonic', '#EE7733'),
              'logarithmic': ('Taylor', '#228833')}
    omitted_lower_sd = False
    with plt.rc_context(_main_style()):
        figure, axes = plt.subplots(1, 2, figsize=(10.3, 4.1), sharey=True)
        for axis, panel, title in zip(axes, ('circle', 'digits'),
                                      ('Circle', '8×8 digits 1 vs 7')):
            for family, (label, color) in styles.items():
                rows = [row for row in data['summaries']
                        if row['panel'] == panel and row['family'] == family]
                if not rows:
                    continue
                widths = np.asarray([row['dense_width'] for row in rows])
                means = np.asarray([row['worst_recorded_ratio']['mean'] for row in rows])
                deviations = np.asarray([row['worst_recorded_ratio']['sample_sd'] for row in rows])
                lower = np.where(means > deviations, deviations, 0.)
                omitted_lower_sd |= bool(np.any(means <= deviations))
                axis.errorbar(widths, means, yerr=[lower, deviations], fmt='o-', color=color,
                              capsize=3, markersize=5, linewidth=1.6, label=label)
                for row in rows:
                    values = row['worst_recorded_ratio']['values']
                    axis.scatter([row['dense_width']]*len(values), values, color=color,
                                 s=23, marker='x', alpha=.58, zorder=4)
            axis.axhline(1, color='#555555', linestyle=':', linewidth=1.2)
            axis.set(xscale='log', yscale='log', xlabel='Dense width', title=title)
            axis.set_xticks(data['widths'], [str(width) for width in data['widths']])
            axis.xaxis.set_minor_formatter(NullFormatter())
            axis.grid(alpha=.16)
            axis.legend(frameon=False, loc='upper left')
        axes[0].set_ylabel('Relative test RMS')
        figure.suptitle(f'Fixed compact width {data["compact_width"]}', fontsize=13)
        footer = 'Mean ± sample SD; × individual pairs. Lines connect saved observations.'
        if omitted_lower_sd:
            footer += ' Nonpositive lower SD bounds are not drawn.'
        figure.text(.5, .01, footer, ha='center', fontsize=8.5)
        figure.tight_layout(rect=(0, .055, 1, .92))
    return figure


def draw_dense_pairs(data):
    """Use either dense-pair report.json: config, summary, descriptive_sqrt_fits."""
    rows = [row for row in data["summary"] if row["count"]]
    widths = np.asarray([row["width"] for row in rows])
    figure, axes = plt.subplots(1, 2, figsize=(8.4, 3.8))
    for axis, metric, title in zip(axes, ["endpoint_rms", "max_time_rms"], ["Endpoint", "Worst recorded"]):
        means = np.asarray([row[metric]["mean"] for row in rows])
        deviations = np.asarray([row[metric]["sd"] or 0 for row in rows])
        axis.errorbar(widths, means, yerr=[np.minimum(deviations, .95 * means), deviations],
                      fmt="o-", capsize=3, label="Mean ± SD")
        for row in rows:
            axis.scatter(np.full(row["count"], row["width"]), row[metric]["values"],
                         color="#0072B2", alpha=.4, s=14)
        coefficient = data["descriptive_sqrt_fits"][metric]
        axis.plot(widths, coefficient / np.sqrt(widths), "--", color="grey", label="Fitted c/√n")
        axis.set(xscale="log", yscale="log", xlabel="Dense width", ylabel="Dense-pair RMS", title=title)
        axis.set_xticks(widths, [str(width) for width in widths])
        axis.legend(frameon=False, fontsize=8)
    dataset = data["config"]["dataset"]
    title = "MNIST 1 vs 7" if dataset["name"] == "mnist" else f"Sphere, d={dataset['dimension']}"
    figure.suptitle(title + " · independent dense pairs", fontsize=11)
    note = "Three independent pairs per width; the same seed lists across widths.\nDescriptive c/√n fit, not a pass threshold."
    missing = [row["width"] for row in data["summary"] if not row["count"]]
    if missing:
        note += " Inconclusive widths: " + ", ".join(map(str, missing))
    return _app_finish(figure, axes, note)


if __name__ == '__main__':
    raise SystemExit(main())
