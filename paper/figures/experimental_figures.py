#!/usr/bin/env python3
"""Render the experimental manuscript figures into paper/figures by default.

The adjacent response_memory_source.npz supplies the complete plotting data;
no training archives or model execution are needed. Use --overwrite to replace
only this script's named outputs. See paper/FIGURE_EXPERIMENT.md.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import platform
import subprocess

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, ConnectionPatch
from matplotlib.transforms import Bbox

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BASE = ROOT / 'data/generated/neural_response_memory_20260922'
INK, GRAY, LIGHT = '#233442', '#70808d', '#e4eaf0'
BLUE, TEAL, ORANGE, PURPLE, RED = '#337eb8', '#198779', '#d88632', '#8564ad', '#bf5460'
COLORS = {1: ORANGE, 2: BLUE, 3: TEAL, 7: PURPLE}
CASES = ['two_outliers_alternating', 'quadrant_alternating', 'quadrant_pairs',
         'quadrant_center_edges', 'equal_mixed_odd']
NAMES = ['Outliers / alternating', 'Quadrant / alternating', 'Paired labels',
         'Center / edges', 'Mixed odd labels']
plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 10, 'text.color': INK,
    'axes.labelcolor': INK, 'axes.edgecolor': LIGHT, 'xtick.color': GRAY,
    'ytick.color': GRAY, 'axes.titleweight': 'semibold', 'axes.titlesize': 11,
    'axes.spines.top': False, 'axes.spines.right': False,
    'grid.color': LIGHT, 'grid.linewidth': .65, 'axes.axisbelow': True,
    'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none',
    'savefig.facecolor': 'white', 'figure.facecolor': 'white',
})


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def rms(a):
    return float(np.sqrt(np.mean(np.asarray(a) ** 2)))


def source_data():
    arrays, meta, sources = {}, {}, {}

    def record(path):
        p = Path(path)
        if not p.is_absolute():
            p = ROOT / p
        # No cross-study retrieval: this gallery uses this study's evidence only.
        p.resolve().relative_to(BASE.resolve())
        key = str(p.relative_to(ROOT))
        if key not in sources:
            sources[key] = sha(p)
        return p

    def read_json(path):
        return json.loads(record(path).read_text())

    def take(path, mapping):
        with np.load(record(path), allow_pickle=False) as z:
            for old, new in mapping.items():
                arrays[new] = z[old]

    factor = read_json(BASE / 'factor_analysis01/metrics.json')
    keep = ['case', 'P', 'rank', 'factor_seed', 'circle_rms', 'valid',
            'endpoint_refinement_rms', 'precision_limited', 'status']
    meta['factor_memory'] = [{k: r.get(k) for k in keep} for r in factor['closure_selected']]
    meta['factor_direct'] = [{k: r.get(k) for k in keep} for r in factor['factor_selected']]
    comparisons = [c for r in factor['paired_comparisons'] for c in r['comparisons']]
    meta['factor_resolved_wins'] = sum(c['status'].startswith('closure lower') and
                                      c['directional_difference_resolved'] for c in comparisons)
    meta['factor_excluded'] = sum(not r['valid'] for r in factor['factor_selected'])
    assert meta['factor_resolved_wins'] == 29 and meta['factor_excluded'] == 1
    case = 'quadrant_pairs'
    dense_path = ROOT / factor['dense_references'][case]['arrays_source']
    take(dense_path, {'endpoint_angles': 'factor_angles',
                     'endpoint_prediction': 'factor_dense',
                     'training_inputs': 'train_inputs', 'labels': 'train_labels',
                     'snapshot_times': 'dense_times', 'circle_predictions': 'dense_history',
                     'circle_angles': 'history_angles'})
    previous = factor['dense_references'][case]['previous_arrays_source']
    take(previous, {'snapshot_times': 'dense_previous_times',
                    'circle_predictions': 'dense_previous_history'})
    meta['factor_radial_rms'] = {}
    for p in [1, 3, 7]:
        row = next(r for r in factor['closure_selected'] if r['case'] == case and r['P'] == p)
        take(row['arrays_source'], {'endpoint_prediction': f'memory_endpoint_{p}',
             'snapshot_times': f'memory_times_{p}', 'circle_predictions': f'memory_history_{p}',
             'matched_time_rms': f'archived_time_rms_{p}'})
        take(row['previous_arrays_source'], {'snapshot_times': f'memory_previous_times_{p}',
             'circle_predictions': f'memory_previous_history_{p}'})
        value = rms(arrays[f'memory_endpoint_{p}'] - arrays['factor_dense'])
        assert np.isclose(value, row['circle_rms'], rtol=1e-10, atol=1e-13)
        meta['factor_radial_rms'][f'P{p}'] = value
    for seed in [20260924, 20260925]:
        row = next(r for r in factor['factor_selected'] if
                   r['case'] == case and r['P'] == 3 and r['factor_seed'] == seed)
        take(row['arrays_source'], {'endpoint_prediction': f'factor_seed_{seed}'})
        if seed == 20260924:
            take(row['arrays_source'], {'reference_snapshot_times': 'legacy_dense_times',
                 'reference_circle_predictions': 'legacy_dense_history', 'circle_angles': 'legacy_angles'})
        value = rms(arrays[f'factor_seed_{seed}'] - arrays['factor_dense'])
        assert np.isclose(value, row['circle_rms'], rtol=1e-10, atol=1e-13)
        meta['factor_radial_rms'][str(seed)] = value

    # Use intersections, never nearest-time matching or interpolation of predictions.
    common = arrays['dense_times']
    for p in [1, 3, 7]:
        common = np.intersect1d(common, arrays[f'memory_times_{p}'])
    assert np.array_equal(common, np.array([0., 1., 2., 5., 10., 20., 40., 80.]))
    arrays['common_times'] = common
    assert np.array_equal(arrays['history_angles'], arrays['legacy_angles'])

    def at(times, values, t):
        hits = np.flatnonzero(times == t)
        assert len(hits) == 1
        return values[hits[0]]

    dense = np.stack([at(arrays['dense_times'], arrays['dense_history'], t) for t in common])
    arrays['common_dense'] = dense
    previous_dense = np.stack([at(arrays['dense_previous_times'],
                                 arrays['dense_previous_history'], t) for t in common])
    meta['saved_matched_time_check'] = {}
    for p in [1, 3, 7]:
        legacy = np.stack([at(arrays['legacy_dense_times'], arrays['legacy_dense_history'], t)
                           for t in arrays[f'memory_times_{p}']])
        check = np.sqrt(np.mean((arrays[f'memory_history_{p}'] - legacy) ** 2, axis=1))
        delta = float(np.max(np.abs(check - arrays[f'archived_time_rms_{p}'])))
        assert delta < 1e-13
        meta['saved_matched_time_check'][str(p)] = delta
        prediction = np.stack([at(arrays[f'memory_times_{p}'],
                                  arrays[f'memory_history_{p}'], t) for t in common])
        old = np.stack([at(arrays[f'memory_previous_times_{p}'],
                           arrays[f'memory_previous_history_{p}'], t) for t in common])
        arrays[f'common_memory_{p}'] = prediction
        arrays[f'common_rms_{p}'] = np.sqrt(np.mean((prediction - dense) ** 2, axis=1))
        arrays[f'common_sensitivity_{p}'] = (np.sqrt(np.mean((old - prediction) ** 2, axis=1))
                                             + np.sqrt(np.mean((dense - previous_dense) ** 2, axis=1)))
    meta['trajectory'] = {
        'case': case, 'width': 2048, 'hidden_layers': 2, 'query_count': 2048,
        'common_times': common.tolist(), 'displayed_times': [0, 5, 20, 80],
        'metric': 'RMS versus finest fresh dense reference at identical physical times',
        'sensitivity': 'Sum of separate coarse/fine prediction RMS changes at each saved time',
        'note': 'Recomputed from saved predictions; archived matched_time_rms used an older dense reference.'}

    mnist = read_json(BASE / 'mnist100_analysis01/metrics_summary.json')
    meta['mnist'] = [r for r in mnist['comparisons'] if r['level'] == .001]
    mapping = {'prediction_dense_loss_0p001': 'mnist_dense', 'validation_digits': 'mnist_digits'}
    for p in [1, 2, 3]:
        mapping[f'prediction_P{p}_loss_0p001'] = f'mnist_{p}'
    take(BASE / 'mnist100_analysis01/validation_predictions_and_errors.npz', mapping)
    for row in meta['mnist']:
        assert np.isclose(rms(arrays[f"mnist_{row['order']}"] - arrays['mnist_dense']),
                          row['rms_difference'], rtol=1e-11, atol=1e-14)

    deep = read_json(BASE / 'deep_circle_analysis01/metrics_summary.json')
    meta['deep_orders'] = [{k: r[k] for k in ['case', 'P', 'rms_8192',
                           'combined_sensitivity']} for r in deep['endpoint_comparisons']]
    # These are published-in-study ranges, not newly reconstructed feature states.
    record(ROOT / 'data/generated/neural_response_memory_20260922/deep_circle_analysis01/summary.md')
    meta['feature_ranges'] = [[.345441, .648572], [.382720, .736775], [.460717, .677563]]
    meta['feature_range_source'] = 'studies/neural_response_memory_20260922/DEEP_CIRCLE_RESULTS.md'
    sources[meta['feature_range_source']] = sha(ROOT / meta['feature_range_source'])
    meta['sources'] = sources
    return arrays, meta


def canvas(title, subtitle, size=(12, 7)):
    fig = plt.figure(figsize=size)
    fig.text(.045, .952, title, fontsize=20, weight='bold', va='top')
    fig.text(.045, .902, subtitle, fontsize=10.5, color=GRAY, va='top')
    return fig


def footer(fig, line1, line2=''):
    fig.text(.045, .044, line1, fontsize=9, color=GRAY, va='bottom')
    if line2:
        fig.text(.045, .018, line2, fontsize=9, color=GRAY, va='bottom')


def panel_label(ax, text):
    ax.text(0, 1.055, text, transform=ax.transAxes, weight='bold', va='bottom', fontsize=11)


def arrow(ax, a, b, color=GRAY, connectionstyle='arc3,rad=0', lw=1.6):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=12,
                 lw=lw, color=color, connectionstyle=connectionstyle))


def box(ax, x, y, w, h, text='', color=LIGHT, fontsize=10, edge='none'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=.012,rounding_size=.015',
                              facecolor=color, edgecolor=edge, lw=1))
    if text:
        ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=fontsize)


def mechanism(a, meta):
    fig = canvas('A learned connection is a paired memory',
                 'SCHEMATIC  /  One training sample; three history modes illustrated, not three fixed neuron features.')
    ax = fig.add_axes([.045, .20, .91, .65]); ax.set(xlim=(0, 1), ylim=(0, 1)); ax.axis('off')
    for x, label in [(.045, '1  Responses'), (.37, '2  History coordinates'), (.735, '3  Interaction')]:
        ax.text(x, .96, label, weight='bold', fontsize=12)
    for x, color, label in [(.10, BLUE, r'$i$'), (.225, TEAL, r'$j$')]:
        ax.add_patch(Circle((x, .82), .035, facecolor=color, edgecolor='none'))
        ax.text(x, .82, label, color='white', ha='center', va='center', fontsize=12)
    arrow(ax, (.14, .82), (.185, .82))
    ax.text(.162, .75, 'adjacent layers', ha='center', color=GRAY, fontsize=9)
    x = np.linspace(0, 1, 180)
    for y, f, color, label in [(.55, .075*np.tanh(7*(x-.5))+.025*np.sin(7*x), BLUE,
                               r'forward history $h_i$'),
                              (.31, .09*np.sin(4*x)+.03*x, TEAL,
                               r'backward history $b_j=r\delta_j/\rho$')]:
        ax.plot(.035+.255*x, y+f, color=color, lw=2.4)
        ax.plot([.035, .29], [y-.13, y-.13], color=LIGHT)
        ax.text(.035, y+(.13 if color == BLUE else .105), label, fontsize=10, color=color)
        arrow(ax, (.305, y), (.36, y), color)
        for k in range(3):
            box(ax, .38+k*.088, y-.058, .073, .116, f'$m_{{{1 if color == BLUE else 2}}}^{{({k})}}$',
                '#e5f0f8' if color == BLUE else '#e0f1ed', fontsize=12)
        arrow(ax, (.657, y), (.723, .47), color)
    ax.text(.49, .675, 'same three polynomial modes', ha='center', color=GRAY, fontsize=9)
    ax.text(.495, .17, 'One entry per neuron, per mode.\nThe moment vectors evolve.',
            ha='center', fontsize=10, linespacing=1.6)
    box(ax, .73, .39, .255, .18, 'paired outer products\n' +
        r'$\Delta\widehat W=-\frac{2}{n\tau}\sum_{k<3}(2k+1)m_2^{(k)}(m_1^{(k)})^\top$',
        '#edf5f2', fontsize=10)
    box(ax, .74, .70, .095, .12, r'$W_0$', '#e4e7e9', fontsize=18)
    ax.text(.85, .76, '+', ha='center', va='center', fontsize=20, color=GRAY)
    ax.text(.924, .76, r'$\Delta\widehat W$', ha='center', va='center', fontsize=16, color=TEAL)
    arrow(ax, (.86, .59), (.86, .68), TEAL)
    ax.text(.787, .87, 'fixed, retained', ha='center', fontsize=9, color=GRAY)
    arrow(ax, (.87, .36), (.87, .06), TEAL)
    arrow(ax, (.87, .06), (.16, .06), TEAL)
    arrow(ax, (.16, .06), (.16, .135), TEAL)
    ax.text(.51, .025, 'Current interaction changes the responses entering the next memory update',
            ha='center', va='top', color=TEAL, fontsize=10)
    # Explicit separation between fixed coordinates in history and moving directions in neuron space.
    inset = fig.add_axes([.06, .092, .25, .09]); inset.set(xlim=(0, 1), ylim=(-1.25, 1.35)); inset.axis('off')
    for k, c in enumerate([GRAY, BLUE, TEAL]):
        inset.plot(x, np.polynomial.legendre.legval(2*x-1, [0]*k+[1]), color=c, lw=1.25)
    inset.text(1.08, .1, 'Fixed basis in history coordinate', va='center', fontsize=10)
    inset2 = fig.add_axes([.66, .075, .105, .11]); inset2.set(xlim=(-.1, 1.1), ylim=(-.1, 1.1)); inset2.axis('off')
    for end, c in [((.94, .18), LIGHT), ((.77, .51), BLUE), ((.38, .94), TEAL)]:
        arrow(inset2, (0, 0), end, c)
    fig.text(.78, .125, 'Moving directions\nin neuron space', va='center', fontsize=10)
    footer(fig, 'History modes are fixed coordinate functions; their vector-valued coefficients are dynamical states.')
    return fig


def polar(ax, theta, curves, train_inputs=None, labels=None, maxrad=5.5):
    ax.set_theta_zero_location('E'); ax.set_theta_direction(1)
    ax.set_ylim(0, maxrad); ax.set_yticks([2, 3, 4]); ax.set_yticklabels(['−1', '0', '+1'], fontsize=8)
    ax.set_xticks(np.deg2rad([0, 90, 180, 270])); ax.set_xticklabels(['0°', '90°', '180°', '270°'], fontsize=8)
    ax.grid(color=LIGHT); ax.spines['polar'].set_visible(False)
    fulltheta = np.r_[theta, theta[0]+2*np.pi]
    ax.plot(fulltheta, np.full_like(fulltheta, 3), color=GRAY, lw=.75, ls='--')
    for y, c, lw, ls in curves:
        assert np.min(3+y) > 0 and np.max(3+y) < maxrad
        ax.plot(fulltheta, np.r_[3+y, 3+y[0]], color=c, lw=lw, ls=ls)
    if train_inputs is not None:
        angles = np.arctan2(train_inputs[:, 1], train_inputs[:, 0])
        ax.scatter(angles, 3+labels, s=18, color=INK, zorder=10, edgecolor='white', linewidth=.35)


def trajectory(a, meta):
    fig = canvas('Learning in motion, at the same physical times',
                 'SAVED TRAJECTORIES  /  Paired-label circle task · two tanh hidden layers · width 2,048')
    times = a['common_times']
    for j, t in enumerate([0, 5, 20, 80]):
        i = int(np.flatnonzero(times == t)[0])
        ax = fig.add_axes([.055+.235*j, .50, .205, .285], projection='polar')
        curves = [(a['common_dense'][i], INK, 2.5, '-')]
        curves += [(a[f'common_memory_{p}'][i], COLORS[p], 1.35, '--' if p == 7 else '-') for p in [1, 3, 7]]
        polar(ax, a['history_angles'], curves, a['train_inputs'], a['train_labels'])
        fig.text(.1575+.235*j, .838, f'$t={t}$', ha='center', weight='bold', fontsize=12)
    handles = [Line2D([0], [0], color=INK, lw=2, label='Dense')]+[
        Line2D([0], [0], color=COLORS[p], lw=2, label=f'Memory P={p}') for p in [1, 3, 7]]
    fig.legend(handles=handles, loc='center', bbox_to_anchor=(.50, .438), ncol=4, frameon=False, fontsize=10)
    ax = fig.add_axes([.08, .14, .59, .255])
    for p in [1, 3, 7]:
        ax.plot(times[1:], a[f'common_rms_{p}'][1:], 'o-', color=COLORS[p], lw=1.5, ms=5)
        ax.plot(times[1:], a[f'common_sensitivity_{p}'][1:], ':', color=COLORS[p], lw=1.0, alpha=.8)
    ax.set(xlabel='Physical training time', ylabel='Circle RMS difference', yscale='log', xlim=(0, 82))
    ax.grid(True, which='major')
    fig.text(.72, .37, 'Eight genuine shared times', weight='bold', fontsize=12, va='top')
    fig.text(.72, .317, 'Dots: measured discrepancy\nSolid joins: visual guides only\nDotted: numerical sensitivity',
             linespacing=1.65, fontsize=10, va='top')
    fig.text(.72, .172, 'At initialization the functions agree\nto numerical roundoff (not on log axis).',
             linespacing=1.5, fontsize=9.5, color=GRAY, va='top')
    footer(fig, 'Radius = 3 + prediction; dashed ring = zero; dots on circles = training labels. RMS uses 2,048 angles.',
           'Sensitivity = sum of dense and closure coarse/fine RMS changes; an empirical diagnostic, not an error certificate.')
    return fig


def factor_control(a, meta):
    fig = canvas('Same correction rank. Different learned functions.',
        'SAVED ENDPOINTS  /  Same initialized W₀ and outer weights · two tanh hidden layers · width 2,048')
    panels = [('Dense reference', [(a['factor_dense'], INK, 2., '-')], 'Paired-label task'),
              ('Response memory · P=3', [(a['factor_dense'], INK, 2., '-'),
                 (a['memory_endpoint_3'], TEAL, 1.7, '--')],
                 f"RMS {meta['factor_radial_rms']['P3']:.5f}"),
              ('Directly trained factors', [(a['factor_dense'], INK, 1.4, '-'),
                 (a['factor_seed_20260924'], ORANGE, 1.7, '-'),
                 (a['factor_seed_20260925'], RED, 1.7, '--')], 'RMS 0.37546 / 0.20358')]
    for i, (title, curves, detail) in enumerate(panels):
        ax = fig.add_axes([.075+.315*i, .505, .235, .28], projection='polar')
        polar(ax, a['factor_angles'], curves, a['train_inputs'], a['train_labels'])
        fig.text(.1925+.315*i, .835, title, ha='center', fontsize=11, weight='bold')
        fig.text(.1925+.315*i, .455, detail, ha='center', fontsize=10)
    fig.text(.50, .43, 'Learned-correction rank bound 24 for both compressed models', ha='center', weight='bold', fontsize=11)
    for i, case in enumerate(CASES):
        ax = fig.add_axes([.065+.185*i, .14, .157, .19])
        series = [(meta['factor_memory'], None, TEAL, 'o', '-'),
                  (meta['factor_direct'], 20260924, ORANGE, '^', '-'),
                  (meta['factor_direct'], 20260925, RED, 's', '--')]
        for rows, seed, color, marker, style in series:
            selected = sorted([r for r in rows if r['case'] == case and
                              (seed is None or r['factor_seed'] == seed)], key=lambda r:r['rank'])
            x = [r['rank'] for r in selected]
            y = [r['circle_rms'] if r['valid'] else np.nan for r in selected]
            ax.plot(x, y, marker=marker, color=color, ls=style, lw=1.25, ms=4)
            for r in selected:
                if r['valid'] and r['precision_limited']:
                    ax.plot(r['rank'], r['circle_rms'], marker=marker, ms=5, mfc='white', mec=color)
        ax.set(yscale='log', ylim=(1e-7, 3), yticks=[1e-6, 1e-3, 1],
               xticks=[4, 12, 28] if i==4 else [8, 24, 56], xlabel='Rank bound')
        ax.set_title(NAMES[i], fontsize=9); ax.grid(True, axis='y')
        if i==0:
            ax.set_ylabel('Circle RMS vs dense', fontsize=9)
            ax.text(.04, .04, '1 capped run omitted', transform=ax.transAxes, va='bottom', fontsize=7.5, color=GRAY)
        else:
            ax.set_yticklabels([])
    handles=[Line2D([0],[0],color=c,marker=m,label=l,ls=s) for c,m,l,s in
             [(TEAL,'o','Response memory','-'),(ORANGE,'^','Factor seed 20260924','-'),(RED,'s','Factor seed 20260925','--')]]
    fig.legend(handles=handles, loc='center', bbox_to_anchor=(.52,.377), ncol=3, frameon=False, fontsize=9)
    footer(fig, 'Each model is shown at its own MSE 0.001 endpoint. RMS uses 8,192 angles. Hollow points have limited numerical precision.',
           'Memory wins all 29 resolved comparisons with this factor-flow baseline; this is not a claim against every low-rank method.')
    return fig


def clock_figure(a, meta):
    fig = canvas('A clock changes the spacing of a response history',
                 'SCHEMATIC  /  An illustrative smooth path, not a measured network trajectory.')
    t = np.linspace(0, 1, 1601)
    speed = .035+1.4*np.exp(-((t-.31)/.057)**2)+.85*np.exp(-((t-.77)/.085)**2)
    s = np.r_[0, np.cumsum((speed[1:]+speed[:-1])*np.diff(t)/2)]
    s = s / s[-1]
    path = np.stack([1.5*s, .46*np.sin(2*np.pi*s-.6)],axis=1)
    velocity = np.gradient(path,t,axis=0)
    rho = .12+.18*(1-t)
    g = rho+np.linalg.norm(velocity,axis=1)
    tau = 1+np.r_[0,np.cumsum((g[1:]+g[:-1])*np.diff(t)/2)]
    axes=[]
    for rect,x,label in [([.075,.58,.49,.235],t,'Physical time  t'),
                         ([.075,.24,.49,.235],tau,'Joint clock  τ')]:
        ax=fig.add_axes(rect); axes.append(ax)
        ax.plot(x,path[:,0],color=BLUE,lw=2.3)
        ax.set(xlabel=label,ylabel='One response',ylim=(-.1,1.65));ax.grid(True)
    events=[.24,.34,.65,.83]
    for ev,c in zip(events,[BLUE,TEAL,ORANGE,PURPLE]):
        j=int(np.argmin(abs(t-ev)))
        for ax,x in zip(axes,[t,tau]):
            ax.scatter(x[j],path[j,0],s=26,color=c,zorder=5)
        fig.add_artist(ConnectionPatch((t[j],-.1),(tau[j],1.65),coordsA=axes[0].transData,
                       coordsB=axes[1].transData,color=c,alpha=.23,lw=1))
    fig.text(.075,.858,'The same events; a different horizontal coordinate',fontsize=11,weight='bold')
    for ypos,clock,label,color in [(.57,t,'Uniform physical-time markers',GRAY),
                                 (.25,tau,'Uniform joint-clock markers',TEAL)]:
        ax=fig.add_axes([.66,ypos,.265,.245]);ax.axis('off')
        ax.plot(path[:,0],path[:,1],color=LIGHT,lw=3)
        marks=np.linspace(clock[0],clock[-1],16)
        px=np.interp(marks,clock,path[:,0]);py=np.interp(marks,clock,path[:,1])
        ax.scatter(px,py,color=color,s=22,edgecolors='white',linewidth=.4,zorder=3)
        ax.set_title(label,fontsize=10,pad=2)
    fig.text(.08,.142,r'Simple:  $\dot\tau=\rho=\mathrm{RMS}(r)$',fontsize=14)
    fig.text(.50,.142,r'Joint:  $\dot\tau=\rho+\|\dot\Psi\|_2$     $\Rightarrow$     $\|d\Psi/d\tau\|_2\leq 1$',fontsize=14)
    footer(fig, 'Ψ collects the forward and residual-weighted backward responses. Residual RMS is not the rate at which loss falls.',
           'The joint clock bounds speed; it guarantees neither constant speed nor low-order accuracy. Weighting still uses ρ dt (a shared Gram matrix).')
    return fig


def pairing(a, meta):
    fig=canvas('Why pairing two memories multiplies their errors',
               'PROJECTION IDENTITY  /  Both histories use the same orthogonal projection and the same integration measure.')
    fig.text(.095,.79,r'$h=h_P+h_\perp$',fontsize=24,color=BLUE)
    fig.text(.545,.79,r'$b=b_P+b_\perp$',fontsize=24,color=TEAL)
    ax=fig.add_axes([.10,.27,.61,.44]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.44,.97,r'Retained $h_P$',ha='center',color=BLUE,fontsize=13)
    ax.text(.80,.97,r'Omitted $h_\perp$',ha='center',color=BLUE,fontsize=13)
    ax.text(.015,.65,r'Retained $b_P$',va='center',color=TEAL,fontsize=12)
    ax.text(.015,.24,r'Omitted $b_\perp$',va='center',color=TEAL,fontsize=12)
    cells=[(.28,.47,'kept interaction',r'$\int b_P h_P^\top$', '#e1f1ec'),
           (.64,.47,'mixed term = 0',r'$\int b_P h_\perp^\top=0$', '#f1f3f6'),
           (.28,.06,'mixed term = 0',r'$\int b_\perp h_P^\top=0$', '#f1f3f6'),
           (.64,.06,'entire pairing error',r'$\int b_\perp h_\perp^\top$', '#faebd8')]
    for x,y,title,eq,c in cells:
        box(ax,x,y,.32,.35,color=c)
        ax.text(x+.16,y+.255,title,ha='center',fontsize=10)
        ax.text(x+.16,y+.115,eq,ha='center',fontsize=15)
    fig.text(.765,.61,'Orthogonality',weight='bold',fontsize=13)
    fig.text(.765,.54,'kills both mixed terms.\nOnly omitted × omitted remains.',fontsize=10,linespacing=1.6)
    fig.text(.11,.204,r'$\left\|\int bh^\top-\int b_Ph_P^\top\right\|_F'
             r'\leq\|b-b_P\|_{L^2}\,\|h-h_P\|_{L^2}$',fontsize=20)
    bottom=fig.add_axes([.1,.092,.82,.065]);bottom.axis('off')
    box(bottom,.0,.1,.30,.70,'History reconstruction error','#faebd8')
    arrow(bottom,(.32,.45),(.69,.45),TEAL)
    bottom.text(.505,.72,'feedback stability',ha='center',fontsize=10,color=TEAL)
    box(bottom,.71,.1,.28,.70,'Trajectory error','#e1f1ec')
    footer(fig,'The algebraic cancellation alone is not a tracking theorem. Regularity controls the projection tails; stability controls feedback.')
    return fig


def mnist_figure(a, meta):
    fig=canvas('Prediction agreement, with the discrepancies made visible',
               'MNIST 3 vs 8  /  100 training images · 1,984 held-out images · two tanh hidden layers · width 4,096')
    x=a['mnist_dense']; ax=fig.add_axes([.08,.23,.32,.57])
    for digit,c in [(3,BLUE),(8,TEAL)]:
        sel=a['mnist_digits']==digit
        ax.scatter(x[sel],a['mnist_3'][sel],s=7,color=c,alpha=.38,edgecolors='none',label=f'Digit {digit}',rasterized=True)
    lo,hi=min(x.min(),a['mnist_3'].min())-.1,max(x.max(),a['mnist_3'].max())+.1
    ax.plot([lo,hi],[lo,hi],color=GRAY,lw=1,ls='--');ax.set(xlim=(lo,hi),ylim=(lo,hi),
        xlabel='Dense prediction',ylabel='Memory P=3 prediction',aspect='equal')
    ax.set_title('One agreement plot');ax.legend(frameon=False,loc='upper left');ax.grid(True)
    limit=max(np.max(np.abs(a[f'mnist_{p}']-x)) for p in [1,2,3])*1.12
    for i,p in enumerate([1,2,3]):
        ax=fig.add_axes([.52,.63-.205*i,.40,.16])
        delta=a[f'mnist_{p}']-x
        ax.scatter(x,delta*1000,s=6,color=COLORS[p],alpha=.4,edgecolors='none',rasterized=True)
        ax.axhline(0,color=GRAY,lw=.8);ax.set(xlim=(lo,hi),ylim=(-limit*1000,limit*1000));ax.grid(True,axis='y')
        ax.text(.02,.87,f'P={p}',transform=ax.transAxes,color=COLORS[p],weight='bold',fontsize=11)
        ax.text(.98,.87,f'RMS {rms(delta):.6f}',transform=ax.transAxes,ha='right',fontsize=10)
        ax.set_ylabel('Δf × 10³')
        if i<2:ax.set_xticklabels([])
        else:ax.set_xlabel('Dense prediction')
    fig.text(.52,.855,'Signed residuals, one shared vertical scale',fontsize=11,weight='bold')
    fig.text(.08,.145,'P=2 is slightly closer than P=3 at this endpoint.',fontsize=12,weight='bold')
    footer(fig,'Each model reaches its own training-MSE 0.001 endpoint. Residual = memory prediction − dense prediction.',
           'All 1,984 held-out points are shown. RMS measures function agreement, not label RMSE; no new training was run.')
    return fig


def order_figure(a, meta):
    fig=canvas('Measured order trends, with their numerical scale',
               'DEEP CIRCLE TASKS  /  Three tanh hidden layers · width 4,096 · each model at its own MSE 0.001 endpoint')
    taskcolors=[RED,ORANGE,TEAL,BLUE,PURPLE]
    for j,(left,title,field) in enumerate([(.075,'Prediction discrepancy','rms_8192'),
                                          (.405,'Numerical sensitivity','combined_sensitivity')]):
        ax=fig.add_axes([left,.34,.25,.44])
        for case,name,color in zip(CASES,NAMES,taskcolors):
            rows=sorted([r for r in meta['deep_orders'] if r['case']==case],key=lambda r:r['P'])
            ax.plot([r['P'] for r in rows],[r[field] for r in rows], 'o-' if j==0 else 'D:',
                    color=color,lw=1.4,ms=5,label=name)
        ax.set(xlabel='History order P',yscale='log',xticks=[1,2,3]);ax.set_title(title)
        ax.set_ylabel('Circle RMS' if j==0 else 'Sum of coarse/fine RMS changes');ax.grid(True)
    ax=fig.add_axes([.755,.34,.20,.44]); ranges=meta['feature_ranges']
    for layer,(lo,hi) in enumerate(ranges,1):
        ax.plot([layer,layer],[lo,hi],color=TEAL,lw=9,solid_capstyle='round')
        ax.plot([layer,layer],[lo,hi],'o',color=TEAL,ms=5)
        ax.text(layer,hi+.035,f'{lo:.2f}–{hi:.2f}',ha='center',fontsize=8.5)
    ax.set(xlim=(.5,3.5),ylim=(0,.9),xticks=[1,2,3],xlabel='Hidden layer',ylabel='Activation RMS change')
    ax.set_title('Representations move');ax.grid(True,axis='y')
    ax.text(.5,-.28,'Range over 20 fitted runs\n(dense and P=1,2,3)',transform=ax.transAxes,
            ha='center',fontsize=9,color=GRAY,linespacing=1.5)
    handles=[Line2D([0],[0],color=c,marker='o',label=n) for c,n in zip(taskcolors,NAMES)]
    fig.legend(handles=handles,loc='center',bbox_to_anchor=(.36,.20),ncol=2,frameon=False,fontsize=9)
    fig.text(.075,.107,'No fitted power-law slope. P=2 outperforms P=3 on both alternating-label tasks.',fontsize=11,weight='bold')
    footer(fig,'Left: measured errors on 8,192 circle angles. Middle: empirical sensitivity diagnostics, not certified bounds or confidence intervals.',
           'Right: absolute training-activation RMS movement from initialization, using the ranges recorded in the deep-circle report.')
    return fig


FIGURES=[('memory_mechanism',mechanism,'Schematic'),('learning_in_motion',trajectory,'Saved measurements'),
         ('same_rank_dynamics',factor_control,'Saved measurements'),
         ('learning_clocks',clock_figure,'Schematic'),('paired_projection',pairing,'Mathematical diagram'),
         ('mnist_residuals',mnist_figure,'Saved measurements'),('order_sensitivity',order_figure,'Saved measurements')]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=HERE)
    parser.add_argument('--bundle',type=Path,default=HERE/'response_memory_source.npz')
    parser.add_argument('--from-archives',action='store_true',help='Re-extract the original saved data instead of using the portable bundle.')
    parser.add_argument('--overwrite',action='store_true',help='Replace only the named figure outputs from this renderer.')
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    output_names=[f'{name}.{ext}' for name,_,_ in FIGURES for ext in ['pdf','svg','png']]
    output_names+=['experimental_gallery.pdf','experimental_manifest.json','experimental_gallery.html']
    collisions=[name for name in output_names if (args.out/name).exists()]
    if collisions and not args.overwrite:
        parser.error('Outputs exist; use --overwrite or a fresh --out directory: '+', '.join(collisions))
    if not args.from_archives:
        with np.load(args.bundle,allow_pickle=False) as z:
            meta=json.loads(str(z['metadata_json']));a={k:z[k] for k in z.files if k!='metadata_json'}
    else:
        a,meta=source_data()
        bundle=args.out/'response_memory_source.npz'
        if bundle.exists() and not args.overwrite:
            parser.error('Source bundle exists; use --overwrite or a fresh output directory.')
        np.savez_compressed(bundle,**a,metadata_json=json.dumps(meta))
    entries=[]
    with PdfPages(args.out/'experimental_gallery.pdf') as book:
        for name,draw,kind in FIGURES:
            fig=draw(a,meta)
            book.savefig(fig)
            # The manuscript supplies the title, experimental setup and caption.
            # Remove gallery headers/footnotes from the individual paper exports.
            for text in fig.texts:
                if text.get_position()[1] > .88 or text.get_position()[1] < .065:
                    text.set_visible(False)
            width,height=fig.get_size_inches()
            crop=Bbox.from_extents(.025*width,.075*height,.98*width,.88*height)
            for ext in ['pdf','svg','png']:
                fig.savefig(args.out/f'{name}.{ext}',dpi=170,bbox_inches=crop)
            plt.close(fig)
            entries.append({'name':name,'kind':kind})
            print('Rendered',name,flush=True)
    meta['render']={'script':str(Path(__file__).relative_to(ROOT)),'script_sha256':sha(__file__),
                    'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__,
                    'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                    'figures':entries,'training_performed':False,'paper_exports':'Cropped headers and footnotes; captions supplied in main.tex.'}
    meta['output_sha256']={name:sha(args.out/name) for name in output_names if name.endswith(('.pdf','.svg','.png'))}
    meta['bundle_sha256']=sha(args.out/'response_memory_source.npz' if args.from_archives else args.bundle)
    (args.out/'experimental_manifest.json').write_text(json.dumps(meta,indent=2)+'\n')
    body='\n'.join(f'<section><p class="kind">{html.escape(e["kind"])}</p><a href="{e["name"]}.pdf">PDF</a> · '
        f'<a href="{e["name"]}.svg">SVG</a><img src="{e["name"]}.png" alt="{e["name"]}"></section>' for e in entries)
    (args.out/'experimental_gallery.html').write_text('<!doctype html><meta charset="utf-8"><title>Response memory — experimental figures</title>'
        '<style>body{font:16px system-ui;background:#eef2f5;color:#233442;max-width:1200px;margin:40px auto;padding:0 20px}'
        'section{background:white;margin:28px 0;padding:20px;border-radius:12px}img{width:100%;display:block}.kind{color:#70808d}'
        'a{color:#337eb8}h1{font-weight:650}</style><h1>Response memory: seven figure prototypes</h1>'
        '<p>Existing saved evidence and labeled schematics. No new training.</p>'
        '<p><a href="experimental_gallery.pdf">Download the full seven-page PDF gallery with captions</a></p>'+body)
    print('Gallery:',args.out/'experimental_gallery.pdf')


if __name__=='__main__':
    main()
