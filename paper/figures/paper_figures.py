#!/usr/bin/env python3
"""Render the paper's data figures from saved metrics, in one shared style.

No model is trained here. Each figure reads the metrics.json written by the
corresponding `capture_trajectory.py` plotting command and redraws the same
numbers with `paper_style`.

Usage:
    python paper/figures/paper_figures.py [--data DIR] [--out DIR] [--only NAME ...]
"""
import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from paper_style import (CONTROL, FAMILY, INK, LIGHT, METHOD, MUTED, TEXT_WIDTH,  # noqa: E402
                         direct_labels, log_ticks, panel, save, use, width_ticks)

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT/'data/generated/paper_appendix_pilots_20261009'
SOURCES = {
    'storage': 'mean_task_comparison/metrics.json',
    'accuracy': 'figure3_paired_seeds/figures_final/metrics.json',
    'training': 'figure4_resplit_repair/figures/metrics.json',
    'robustness': 'refresh_20261010/robustness/metrics.json',
    'scope': 'refresh_20261010/scope/metrics.json',
    'fixed_width': 'refresh_20261010/fixed_budget_final/metrics.json',
    'costs': 'refresh_20261010/costs_final/metrics.json',
    'spectra': ['spectral_history/n512/report.json', 'spectral_history/n1024/report.json',
                'spectral_history/n2048/report.json', 'feedback/spectral_n4096/report.json',
                'feedback/spectral_n8192/report.json'],
}
TWO_PANEL = dict(left=.085, right=.985, bottom=.17, top=.87, wspace=.28)


def load(path):
    return json.loads(Path(path).read_text())


def two_panels(height=2.45, sharey=False, **adjust):
    fig, axes = plt.subplots(1, 2, figsize=(TEXT_WIDTH, height), sharey=sharey)
    fig.subplots_adjust(**{**TWO_PANEL, **adjust})
    return fig, axes


def end_label(ax, x, y, text, dx=4, dy=0, ha='left', va='center', color=INK):
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va=va, color=color,
                annotation_clip=False)


def method_line(ax, x, y, family, **kwargs):
    style = METHOD[FAMILY[family]]
    return ax.plot(x, y, color=style['color'], marker=style['marker'], **kwargs)


# ----------------------------------------------------------------------------- main figures

def figure_storage(data, out):
    """Learned storage needed to match dense-vs-dense, against dense width."""
    metrics = load(data/SOURCES['storage'])
    widths = metrics['widths']
    seeds = {}
    for row in metrics['toy_individuals']:
        seeds.setdefault(row['family'], {}).setdefault(row['width'], []).append(row['selected']['learned'])
    digits_seeds = {family: {group['width']: group['learned_values'] for group in groups}
                    for family, groups in metrics['digits_groups'].items()}
    panels = [('a', 'Circle, $d = 2$', 2, metrics['toy_groups'], seeds, metrics['fits']['Toy circle (d = 2)']),
              ('b', 'Digits 1 vs 7, $d = 64$', 64, metrics['digits_groups'], digits_seeds,
               metrics['fits']['Digits 1 vs 7 (d = 64)'])]
    fig, axes = two_panels(sharey=True, wspace=.1, right=.96)
    grid = np.geomspace(widths[0], widths[-1], 200)
    n = np.asarray(widths, float)
    for ax, (letter, title, d, groups, individual, fits) in zip(axes, panels):
        dense = n**2+n*(d+1)  # (L-1)n^2 + n(d+1) learned scalars, L = 2
        ax.plot(n, dense, color=CONTROL['dense']['color'], lw=1.1)
        labels = [(dense[-1], 'dense', INK)]
        for family in ('legendre', 'harmonic', 'logarithmic'):
            if family not in groups:
                continue
            style = METHOD[FAMILY[family]]
            mean = np.array([group['mean'] for group in groups[family]])
            for width in widths:
                values = individual[family][width]
                ax.scatter([width]*len(values), values, s=4, color=style['color'], alpha=.35, lw=0, zorder=2)
            method_line(ax, n, mean, family, zorder=3)
            label = (mean[-1], style['label'], INK)
            if family in fits:
                fit = fits[family]
                ax.plot(grid, fit['coefficient']*np.log(grid)**fit['exponent'], color=style['color'],
                        lw=.8, linestyle=(0, (3, 2)), zorder=2)
                label += (rf'$\propto(\log n)^{{{fit["exponent"]:.1f}}}$',)
            labels.append(label)
        width_ticks(ax, widths)
        ax.set_xlim(widths[0]/1.25, widths[-1]*3.4)
        ax.spines['bottom'].set_bounds(widths[0], widths[-1])
        ax.set_yscale('log')
        log_ticks(ax.yaxis)
        ax.set_xlabel('Dense width $n$')
        panel(ax, letter, title)
        ax._labels = labels
    axes[0].set_ylabel('Learned scalars')
    axes[0].set_ylim(1.2e4, 6e8)
    for ax in axes:
        direct_labels(ax, ax._labels, widths[-1]*1.12, dx=0)
    save(fig, out, 'fig2_storage_scaling')


def figure_accuracy(data, out):
    """Endpoint error against learned storage at dense width 4096."""
    metrics = load(data/SOURCES['accuracy'])
    fig, axes = two_panels(height=2.6, wspace=.22)
    limits = metrics['shared_learned_limits']
    for ax, (letter, key, title) in zip(axes, (('a', 'sphere', 'Sphere, $d = 3$'),
                                                ('b', 'digits', 'Digits 1 vs 7, $d = 64$'))):
        result = metrics['panels'][key]
        summaries = result['summaries']
        pair = summaries['dense_pair']['endpoint_rms']
        ax.axhspan(pair['mean']-pair['sd'], pair['mean']+pair['sd'], color=LIGHT, lw=0, zorder=0)
        ax.axhline(pair['mean'], color=CONTROL['pair']['color'], linestyle=CONTROL['pair']['linestyle'], lw=.9)
        frozen = summaries['frozen_features']['endpoint_rms']['mean']
        ax.axhline(frozen, color=CONTROL['frozen']['color'], linestyle=CONTROL['frozen']['linestyle'], lw=.9)

        controls = result['fixed_original_reference_controls']
        dense = sorted((c for c in controls if c['family'] == 'dense' and c['moving'] < 1e7),
                       key=lambda c: c['moving'])
        x = [c['moving'] for c in dense]
        y = [c['endpoint_rms'] for c in dense]
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
        ax.errorbar(x, y, yerr=np.array(spread).T, fmt='none', ecolor=style['color'], elinewidth=.6, alpha=.6)
        ax.plot(x, y, color=style['color'], marker=style['marker'], lw=1.1, ms=3.6)
        low = sorted((c for c in controls if c['family'] == 'low_rank'), key=lambda c: c['moving'])
        style = CONTROL['low_rank']
        ax.plot([c['moving'] for c in low], [c['endpoint_rms'] for c in low], color=style['color'],
                marker=style['marker'], linestyle=style['linestyle'], lw=1, ms=3.4)
        low_end = (low[-1]['moving'], low[-1]['endpoint_rms'])

        ends = {}
        for family in ('legendre', 'harmonic', 'logarithmic'):
            groups = sorted((g for g in summaries.values() if g['family'] == family and g['status'] == 'complete'
                             and 'endpoint_rms' in g and g['moving'] < 1.5e7), key=lambda g: g['moving'])
            if not groups:
                continue
            colour = METHOD[FAMILY[family]]['color']
            x = [g['moving'] for g in groups]
            for metric, hollow in (('endpoint_rms', False), ('extra_endpoint_rms', True)):
                if metric not in groups[0] or (hollow and family != 'logarithmic'):
                    continue
                mean = np.array([g[metric]['mean'] for g in groups])
                sd = np.array([g[metric]['sd'] for g in groups])
                lower = np.where(mean-sd > 0, sd, mean*.5)
                ax.errorbar(x, mean, yerr=[lower, sd], fmt='none', ecolor=colour, elinewidth=.6, alpha=.6)
                if hollow:
                    ax.plot(x, mean, color=colour, marker='o', markerfacecolor='white', markeredgewidth=.9,
                            linestyle=(0, (1, 1.5)), lw=1, ms=3.4, zorder=4)
                else:
                    method_line(ax, x, mean, family, zorder=5)
                ends[family+('_unseen' if hollow else '')] = (x[-1], mean[-1])

        ax.set(xscale='log', yscale='log', xlim=limits, xlabel='Learned scalars')
        log_ticks(ax.xaxis)
        log_ticks(ax.yaxis)
        panel(ax, letter, title)
        ax._annotate = dict(ends=ends, dense=(dense[0]['moving'], dense[0]['endpoint_rms']), low=low_end,
                            pair=pair['mean'], frozen=frozen)
    axes[0].set_ylabel('Endpoint test RMS')
    axes[0].set_ylim(2.5e-5, .6)
    axes[1].set_ylim(2.5e-5, .6)
    for ax in axes:
        notes = ax._annotate
        for family, (x, y) in notes['ends'].items():
            text = 'unseen inputs' if family.endswith('_unseen') else METHOD[FAMILY[family]]['label']
            end_label(ax, x, y, text, color=MUTED if family.endswith('_unseen') else INK)
        end_label(ax, *notes['dense'], 'small dense', dx=-2, dy=5, ha='left', va='bottom')
        end_label(ax, *notes['low'], 'low rank')
        end_label(ax, limits[1], notes['frozen'], 'frozen features', dx=0, dy=2.5, ha='right', va='bottom',
                  color=MUTED)
        end_label(ax, limits[1], notes['pair'], 'dense vs.\ndense', dx=0, dy=2, ha='right', va='bottom',
                  color=MUTED)
    save(fig, out, 'fig3_accuracy_storage')


def figure_training(data, out):
    """Test RMS to the dense run over training, compressions against dense vs. dense."""
    metrics = load(data/SOURCES['training'])
    times = np.asarray(metrics['times'], float)
    fig, axes = two_panels(sharey=True, wspace=.1)
    for ax, (letter, key, title) in zip(axes, (('a', 'circle', 'Circle, $d = 2$'),
                                                ('b', 'digits', 'Digits 1 vs 7, $d = 64$'))):
        summaries = metrics['panels'][key]['summaries']
        labels = []
        pair = np.asarray(summaries['dense_pair']['mean'])
        ax.plot(times, pair, color=CONTROL['pair']['color'], linestyle=CONTROL['pair']['linestyle'], lw=1)
        labels.append((pair[-1], 'dense vs.\ndense', MUTED))
        for family in ('legendre', 'harmonic', 'logarithmic'):
            if family not in summaries:
                continue
            mean = np.asarray(summaries[family]['mean'])
            ax.plot(times, mean, color=METHOD[FAMILY[family]]['color'], lw=1.5)
            labels.append((mean[-1], METHOD[FAMILY[family]]['label'], INK))
        ax.set_yscale('log')
        log_ticks(ax.yaxis)
        ax.set_xlim(0, 40.5)
        ax.spines['bottom'].set_bounds(0, 32)
        ax.set_xticks([0, 8, 16, 24, 32])
        ax.set_xlabel('Training time $t$', x=32/40.5/2)
        panel(ax, letter, title)
        ax._labels = labels
    axes[0].set_ylabel('Test RMS to dense')
    axes[0].set_ylim(2e-7, .06)
    for ax in axes:
        direct_labels(ax, ax._labels, 32.6, dx=0)
    save(fig, out, 'fig4_training_error')


# ----------------------------------------------------------------------------- appendix figures

def figure_spectra(data, out):
    """Singular values of the dense feature histories collapse across widths."""
    reports = [load(data/path) for path in SOURCES['spectra']]
    widths = [report['width'] for report in reports]
    shades = plt.get_cmap('Greys')(np.linspace(.35, .95, len(widths)))
    fig, axes = two_panels(wspace=.32)
    ax = axes[0]
    fixed, shrinking = [], []
    for report, width, shade in zip(reports, widths, shades):
        sigma = np.asarray(report['history_spectra'][0]['singular_values'], float)
        energy = np.sqrt(np.cumsum((sigma**2)[::-1])[::-1])/np.linalg.norm(sigma)  # tail norm from index j on
        rank = lambda tolerance: int(np.argmax(energy <= tolerance))
        fixed.append(rank(.01))
        shrinking.append(rank(.01*np.sqrt(512/width)))
        j = np.arange(1, 301)
        ax.plot(j, sigma[:300]/np.linalg.norm(sigma), color=shade, lw=1.1,
                label=f'{width}' if width < 1000 else f'{width // 1024}k')
    ax.axvline(np.mean(fixed), color=MUTED, lw=.6, linestyle=(0, (1, 1.8)))
    ax.annotate('1% tail', (np.mean(fixed), 1.5e-6), xytext=(3, 0), textcoords='offset points',
                color=MUTED, va='center')
    ax.set(xscale='log', yscale='log', xlim=(1, 300), ylim=(1e-6, 1.5), xlabel='Singular value index $j$',
           ylabel=r'$\sigma_j\,/\,\|\sigma\|$')
    log_ticks(ax.yaxis)
    ax.legend(title='width $n$', loc='lower left', handlelength=1.2, labelspacing=.25, title_fontsize=7)
    panel(ax, 'a', 'Feature-history spectrum')
    ax = axes[1]
    ax.plot(widths, fixed, color=INK, marker='o', lw=1.2)
    ax.plot(widths, shrinking, color=MUTED, marker='o', markerfacecolor='white', markeredgewidth=.9,
            linestyle=(0, (3, 1.6)), lw=1.2)
    width_ticks(ax, widths)
    ax.set_xlim(widths[0]/1.2, widths[-1]*3.2)
    ax.spines['bottom'].set_bounds(widths[0], widths[-1])
    ax.set_ylim(0, 100)
    ax.set_xlabel('Dense width $n$')
    ax.set_ylabel('Rank needed')
    panel(ax, 'b', 'Rank for a given tail')
    direct_labels(ax, [(fixed[-1], 'fixed 1%', INK), (shrinking[-1], r'$1\%\cdot\sqrt{512/n}$', MUTED)],
                  widths[-1]*1.12, dx=0)
    save(fig, out, 'appendix_spectra')


def figure_robustness(data, out):
    """Storage across input dimension and error ratio across architectures."""
    metrics = load(data/SOURCES['robustness'])
    fig, axes = two_panels(height=2.45, wspace=.3)
    ax = axes[0]
    dims = ['2', '3', '10', '64', '784']
    for j, d in enumerate(dims):
        chosen = metrics['selected'].get(d, {})
        for family, best in chosen.items():
            style = METHOD[FAMILY[family]]
            x = j+(-.13 if family == 'harmonic' and len(chosen) > 1 else .13 if len(chosen) > 1 else 0)
            ax.plot([x, x], [best['learned'], best['total']], color=style['color'], lw=.8, alpha=.6)
            ax.plot(x, best['learned'], marker=style['marker'], color=style['color'], ms=4.2)
            ax.plot(x, best['total'], marker=style['marker'], color=style['color'], ms=4.2,
                    markerfacecolor='white', markeredgewidth=.9)
    ax.set_xticks(range(len(dims)), dims)
    ax.set_xlim(-.5, len(dims)-.4)
    ax.set_yscale('log')
    log_ticks(ax.yaxis)
    ax.set_ylim(3e4, 2e6)
    ax.set_xlabel('Input dimension $d$')
    ax.set_ylabel('Stored scalars')
    panel(ax, 'a', 'Smallest passing model')
    harmonic = metrics['selected']['2']['harmonic']
    end_label(ax, -.13, harmonic['total'], 'Harmonic', dx=0, dy=6, ha='center', va='bottom')
    taylor = metrics['selected']['784']['logarithmic']
    end_label(ax, 4, taylor['learned'], 'Taylor', dx=0, dy=-6, ha='center', va='top')
    end_label(ax, 4, taylor['total'], 'total', dx=6, color=MUTED)
    end_label(ax, 4, taylor['learned'], 'learned', dx=6, color=MUTED)

    ax = axes[1]
    cases = [('baseline', 'baseline'), ('depth3', '$L = 3$'), ('depth4', '$L = 4$'),
             ('silu', 'SiLU'), ('m16', '$m = 16$')]
    colour = METHOD['taylor']['color']
    for j, (case, _) in enumerate(cases):
        row = metrics['architecture'][case][0]
        ax.plot(j-.1, row['endpoint_ratio'], marker='o', color=colour, ms=4.2)
        ax.plot(j+.1, row['maximum_ratio'], marker='o', color=colour, ms=4.2, markerfacecolor='white',
                markeredgewidth=.9)
    ax.axhline(1, color=CONTROL['pair']['color'], linestyle=CONTROL['pair']['linestyle'], lw=.9)
    ax.set_xticks(range(len(cases)), [label for _, label in cases])
    ax.set_xlim(-.5, len(cases)-.5)
    ax.set_yscale('log')
    log_ticks(ax.yaxis)
    ax.set_ylim(5e-3, 2)
    ax.set_ylabel('Error / dense vs. dense')
    panel(ax, 'b', 'Taylor across architectures')
    end_label(ax, len(cases)-.5, 1, 'dense vs. dense', dx=0, dy=2.5, ha='right', va='bottom', color=MUTED)
    first = metrics['architecture']['baseline'][0]
    end_label(ax, -.1, first['endpoint_ratio'], 'end of\ntraining', dx=0, dy=6, ha='center', va='bottom',
              color=MUTED)
    end_label(ax, .1, first['maximum_ratio'], 'worst\ntime', dx=0, dy=-6, ha='center', va='top', color=MUTED)
    save(fig, out, 'appendix_robustness')


def figure_scope(data, out):
    """Taylor's dependence on the declared panel and on the training target."""
    metrics = load(data/SOURCES['scope'])
    fig, axes = two_panels(wspace=.3)
    ax = axes[0]
    records = metrics['panel_size']['records']
    sizes = [row['source_panel_size'] for row in records]
    colour = METHOD['taylor']['color']
    names = sorted(records[0]['common_panel_models'], key=lambda name: records[0]['common_panel_models'][name]['learned'])
    labels = []
    for name, hollow in zip(names, (True, False)):
        y = [row['common_panel_models'][name]['endpoint_rms'] for row in records]
        width = name.split('_')[1]
        ax.plot(sizes, y, color=colour, marker='o', lw=1.3, linestyle=(0, (3, 1.6)) if hollow else '-',
                markerfacecolor='white' if hollow else colour, markeredgewidth=.9 if hollow else 0)
        labels.append((y[-1], f'Taylor, $q = {width}$', INK))
    pair = [row['common_dense_pair']['endpoint_rms'] for row in records]
    ax.plot(sizes, pair, color=CONTROL['pair']['color'], linestyle=CONTROL['pair']['linestyle'], lw=1)
    labels.append((pair[-1], 'dense vs. dense', MUTED))
    ax.set_xscale('log')
    ax.set_xticks(sizes, [str(s) for s in sizes])
    ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
    ax.set_xlim(sizes[0]/1.3, sizes[-1]*3.2)
    ax.spines['bottom'].set_bounds(sizes[0], sizes[-1])
    ax.set_yscale('log')
    log_ticks(ax.yaxis)
    ax.set_ylim(8e-4, .06)
    ax.set_xlabel('Declared panel size')
    ax.set_ylabel('Endpoint test RMS')
    panel(ax, 'a', 'Panel size, fixed storage')
    direct_labels(ax, labels, sizes[-1]*1.12, dx=0)

    ax = axes[1]
    transfer = metrics['transfer']
    times = np.asarray(metrics['times'], float)
    keep = times > 0
    labels = []
    pair = np.asarray(transfer['baseline_curve'])
    ax.plot(times[keep], pair[keep], color=CONTROL['pair']['color'], linestyle=CONTROL['pair']['linestyle'], lw=1)
    labels.append((pair[-1], 'dense vs.\ndense', MUTED))
    for name, label, colour, style in (('rebuilt', 'rebuilt', METHOD['taylor']['color'], '-'),
                                       ('transferred', 'transferred', '#55554f', '-'),
                                       ('pooled', 'pooled', '#8f8e88', (0, (4, 2)))):
        curve = np.asarray(transfer['metrics'][name]['curve'])
        ax.plot(times[keep], curve[keep], color=colour, linestyle=style, lw=1.4)
        labels.append((curve[-1], label, INK))
    ax.set_yscale('log')
    log_ticks(ax.yaxis)
    ax.set_xlim(0, 44)
    ax.spines['bottom'].set_bounds(0, 32)
    ax.set_xticks([0, 8, 16, 24, 32])
    ax.set_ylim(8e-5, .4)
    ax.set_xlabel('Training time $t$', x=16/44)
    ax.set_ylabel('Test RMS to dense')
    panel(ax, 'b', 'Sources reused for a new target')
    direct_labels(ax, labels, 32.6, dx=0)
    save(fig, out, 'appendix_scope')


def figure_fixed_width(data, out):
    """Error ratio of fixed-width compressions as the dense width grows."""
    metrics = load(data/SOURCES['fixed_width'])
    widths = metrics['widths']
    fig, axes = two_panels(sharey=True, wspace=.1)
    for ax, (letter, key, title) in zip(axes, (('a', 'circle', 'Circle, $d = 2$'),
                                                ('b', 'digits', 'Digits 1 vs 7, $d = 64$'))):
        labels = []
        for family in ('harmonic', 'logarithmic'):
            rows = sorted((r for r in metrics['summaries'] if r['panel'] == key and r['family'] == family),
                          key=lambda r: r['dense_width'])
            if not rows:
                continue
            style = METHOD[FAMILY[family]]
            x = [r['dense_width'] for r in rows]
            for row in rows:
                values = row['worst_recorded_ratio']['values']
                ax.scatter([row['dense_width']]*len(values), values, s=5, color=style['color'], alpha=.4, lw=0)
            mean = [r['worst_recorded_ratio']['mean'] for r in rows]
            method_line(ax, x, mean, family)
            labels.append((mean[-1], style['label'], INK))
        left, right = widths[0]/1.25, widths[-1]*3.4
        ax.axhline(1, color=CONTROL['pair']['color'], linestyle=CONTROL['pair']['linestyle'], lw=.9,
                   xmax=np.log(widths[-1]*1.08/left)/np.log(right/left))
        labels.append((1, 'dense vs.\ndense', MUTED))
        width_ticks(ax, widths)
        ax.set_xlim(left, right)
        ax.spines['bottom'].set_bounds(widths[0], widths[-1])
        ax.set_yscale('log')
        log_ticks(ax.yaxis)
        ax.set_xlabel('Dense width $n$')
        panel(ax, letter, title)
        ax._labels = labels
    axes[0].set_ylabel('Worst-time error / dense vs. dense')
    axes[0].set_ylim(.1, 4)
    for ax in axes:
        direct_labels(ax, ax._labels, widths[-1]*1.15, dx=0)
    save(fig, out, 'appendix_fixed_width')


def table_costs(data, out):
    """Recorded costs as a booktabs table (mean and sample SD over three seeds)."""
    metrics = load(data/SOURCES['costs'])
    columns = [('source_seconds', 'Source (s)'), ('build_seconds', 'Build (s)'),
               ('training_seconds', 'Training (s)'), ('query_seconds', 'Queries (s)')]
    storage = [('learned_mib', 'Learned'), ('fixed_mib', 'Fixed'), ('total_mib', 'Total')]
    lines = [r'\begin{tabular}{@{}l' + 'r'*len(columns) + 'r'*len(storage) + r'@{}}', r'\toprule',
             r' & \multicolumn{4}{c}{Recorded time (s)} & \multicolumn{3}{c}{Storage (MiB)}\\',
             r'\cmidrule(lr){2-5}\cmidrule(l){6-8}',
             'Model & Source & Build & Training & Queries & Learned & Fixed & Total\\\\', r'\midrule']
    panels = {'circle': 'Circle, $d = 2$', 'digits': 'Digits 1 vs 7, $d = 64$'}
    for key, title in panels.items():
        rows = [row for row in metrics['rows'] if row['panel'] == key]
        if not rows:
            continue
        lines.append(rf'\multicolumn{{8}}{{@{{}}l}}{{\emph{{{title}}}}}\\')
        for row in rows:
            name, _, config = row['label'].partition(' ')
            config = config.replace('k=', 'q=').replace(', ', ',\\ ')
            cells = [name + (f', ${config}$' if config else '')]
            for name, _ in columns:
                values = np.array([member[name] for member in row['members']], float)
                cells.append('--' if not values.any() else
                             f'{values.mean():.2f}' if values.std() < 5e-3 else
                             f'{values.mean():.2f} $\\pm$ {values.std(ddof=1):.2f}')
            for name, _ in storage:
                cells.append(f"{np.mean([member[name] for member in row['members']]):.1f}")
            lines.append(' & '.join(cells) + r'\\')
        lines.append(r'\addlinespace')
    lines[-1] = r'\bottomrule'
    lines.append(r'\end{tabular}')
    out.mkdir(parents=True, exist_ok=True)
    (out/'appendix_costs_table.tex').write_text('\n'.join(lines)+'\n')
    print(out/'appendix_costs_table.tex')


FIGURES = dict(storage=figure_storage, accuracy=figure_accuracy, training=figure_training,
               spectra=figure_spectra, robustness=figure_robustness, scope=figure_scope,
               fixed_width=figure_fixed_width, costs=table_costs)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--data', type=Path, default=DATA)
    parser.add_argument('--out', type=Path, default=Path(__file__).resolve().parent/'paper_figures')
    parser.add_argument('--only', nargs='+', choices=sorted(FIGURES))
    args = parser.parse_args()
    use()
    for name in args.only or FIGURES:
        FIGURES[name](args.data, args.out)
        plt.close('all')


if __name__ == '__main__':
    main()
