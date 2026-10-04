"""Independently analyze saved q=2/q=3 circle experiments; never train.

Usage: python analyze_higher_order_circle.py --run RUN --output FRESH_DIRECTORY
Stage-one runs without scalar trajectories are supported and clearly identified.
Metrics are recomputed from arrays; producer summaries supply metadata only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import shutil
import time

# Bound BLAS before importing NumPy, including standalone invocation.
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS'):
    os.environ[variable] = '2'
import numpy as np

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / 'data/generated/scalar_terminal_closure_20260930'
REFERENCE = GENERATED / 'circle_width1024_02'
CASES = ('two_outliers_alternating', 'quadrant_alternating')
ORDERS = (2, 3)
THRESHOLDS = (.1, .01, .001)
FIT = 1e-6
COLORS = {'dense': '#202020', 1: '#3975ae', 2: '#16836d', 3: '#7950aa',
          'scalar2': '#e58b21', 'scalar3': '#bd3c78'}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_digest(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def rms(value):
    return float(np.sqrt(np.mean(np.asarray(value, dtype=float)**2)))


def maximum(value):
    return float(np.max(np.abs(value)))


def basis(angles):
    phase = np.outer(angles, np.arange(1, 64, 2))
    return np.column_stack((np.cos(phase), np.sin(phase)))


def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, allow_nan=False) + '\n')


class Audit:
    def __init__(self):
        self.hashes = {}
        self.checks = []

    def file(self, path):
        path = Path(path)
        value = digest(path)
        self.hashes[str(path)] = value
        return value

    def json(self, path):
        before = self.file(path)
        value = json.loads(Path(path).read_text())
        if digest(path) != before:
            raise ValueError(f'Input changed while reading: {path}')
        return value

    def arrays(self, path, keys=None):
        before = self.file(path)
        with np.load(path, allow_pickle=False) as source:
            value = {k: source[k] for k in (source.files if keys is None else keys)}
        if digest(path) != before:
            raise ValueError(f'Input changed while reading: {path}')
        for key, a in value.items():
            if not np.issubdtype(a.dtype, np.number) or not np.isfinite(a).all():
                raise ValueError(f'Nonfinite or nonnumeric array: {path}:{key}')
        return value

    def compare(self, name, actual, expected, rtol=1e-9, atol=1e-11):
        if isinstance(actual, (str, bool)) or isinstance(expected, (str, bool)):
            ok, error = actual == expected, None
        else:
            a, b = np.asarray(actual), np.asarray(expected)
            ok = a.shape == b.shape and bool(np.allclose(a, b, rtol=rtol, atol=atol))
            error = maximum(a-b) if a.shape == b.shape and a.size else None
        self.checks.append({'name': name, 'passed': bool(ok), 'max_absolute_difference': error})

    @property
    def passed(self):
        return all(c['passed'] for c in self.checks)


def exact_common(left, right):
    common, il, ir = np.intersect1d(left, right, return_indices=True)
    if len(common) == 0:
        raise ValueError('No identical physical observation times')
    return common, il, ir


def loss_difference(at, av, bt, bv):
    common, ia, ib = exact_common(at, bt)
    return maximum(av[ia]-bv[ib]), len(common)


def fidelity(prediction, reference):
    away = np.abs(reference) >= .05
    disagreement = np.sign(prediction) != np.sign(reference)
    return {'rms': rms(prediction-reference), 'max': maximum(prediction-reference),
            'sign_disagreement': float(np.mean(disagreement)),
            'sign_disagreement_away': float(np.mean(disagreement[away])) if np.any(away) else None,
            'reference_away_fraction': float(np.mean(away))}


def prefixed(prefix, data):
    return {prefix+'_'+key: value for key, value in data.items()}


def resolution_data(directory, task, q, reference, initial_hashes, audit):
    name = f"{task['case']}/q{q}/{directory.name}"
    summary = audit.json(directory/'summary.json')
    data = audit.arrays(directory/'curves.npz')
    endpoint = audit.arrays(directory/'endpoint_states.npz')
    times, angles, labels = data['times'], data['angles'], data['labels']
    if times.ndim != 1 or not len(times) or np.any(np.diff(times) <= 0):
        raise ValueError(f'{name}: invalid time grid')
    m, n = len(labels), 1024
    if m != 8 or angles.shape != (8192,):
        raise ValueError(f'{name}: invalid sample/query count')
    audit.compare(name+':labels', labels, task['labels'], rtol=0, atol=0)
    audit.compare(name+':train_angles', data['train_angles'], task['train_angles_radians'], rtol=0, atol=0)
    audit.compare(name+':query_grid', angles, reference['angles'], rtol=0, atol=0)
    audit.compare(name+':endpoint_time', times[-1], reference['times'][-1], rtol=0, atol=0)
    audit.compare(name+':width', int(summary['width']), n)
    audit.compare(name+':seed', int(summary['seed']), 20260920)
    for key, expected in initial_hashes.items():
        audit.compare(name+':'+key, summary[key], expected)
    for key in ('closure_a', 'closure_readout', 'values', 'keys', 'clock'):
        if key not in endpoint:
            raise ValueError(f'{name}: missing endpoint {key}')
    if endpoint['values'].shape != (q, n, m) or endpoint['keys'].shape != (q, n, m):
        raise ValueError(f'{name}: unexpected mode state shape')
    expected_count = 3*n+2*q*n*m+1
    audit.compare(name+':moving_state_count', sum(v.size for v in endpoint.values()), expected_count)
    residual = data['closure_residual']
    if residual.shape != (len(times), m):
        raise ValueError(f'{name}: invalid residual shape')
    losses = np.mean(residual**2, axis=1)
    audit.compare(name+':loss_from_residual', losses, data['closure_loss'])
    audit.compare(name+':zero_initial_readout', residual[0], -labels, rtol=0, atol=1e-13)
    common, ic, ir = exact_common(times, reference['times'])
    if len(common) != min(len(times), len(reference['times'])):
        raise ValueError(f'{name}: full/reference grids are not nested')
    if 'dense_output' in data:
        audit.compare(name+':embedded_dense_endpoint', data['dense_output'], reference['dense_output'])
    if 'dense_loss' in data and data['dense_loss'].shape == times.shape:
        audit.compare(name+':embedded_dense_common_times', data['dense_loss'][ic], reference['dense_loss'][ir])
    if 'dense_reference_times' in data:
        audit.compare(name+':saved_dense_reference_times', data['dense_reference_times'], reference['times'], rtol=0, atol=0)
        audit.compare(name+':saved_dense_reference_loss', data['dense_reference_loss'], reference['dense_loss'])
    dense = reference['dense_output']
    metrics = dict(case=task['case'], order=q, resolution=directory.name,
                   final_time=float(times[-1]), closure_final_mse=float(losses[-1]),
                   dense_final_mse=float(reference['dense_loss'][-1]),
                   max_loss_error_vs_dense=maximum(losses[ic]-reference['dense_loss'][ir]),
                   loss_comparison_time_count=len(common), full_moving_scalars=expected_count,
                   full_fixed_mixer_scalars=n*n, scalar_moving_scalars=17,
                   scalar_fixed_scalars=712, scalar_total_scalars=729,
                   closure_fitted=bool(losses[-1] <= FIT), dense_fitted=bool(reference['dense_loss'][-1] <= FIT),
                   **prefixed('closure_vs_dense', fidelity(data['closure_output'], dense)))
    metrics['dense_fidelity_threshold_met'] = metrics['closure_vs_dense_rms'] <= .05 and metrics['closure_vs_dense_sign_disagreement'] <= .01
    for key in ('wall_seconds', 'peak_rss_bytes', 'high_water_rss_bytes'):
        if key in summary:
            metrics['recorded_'+key] = summary[key]
    handoffs, missing = [], []
    query_basis, train_basis = basis(angles), basis(data['train_angles'])
    for threshold in THRESHOLDS:
        tag = f'{threshold:g}'
        path = directory/f'handoff_{tag}.npz'
        if not path.exists():
            missing.append(threshold)
            continue
        h = audit.arrays(path)
        t = float(h['time'])
        where = np.flatnonzero(times == t)
        if len(where) != 1:
            raise ValueError(f'{name}/{tag}: handoff is not a saved full-model time')
        audit.compare(name+f'/{tag}:handoff_residual', h['residual'], residual[where[0]])
        if directory.name == 'coarse':
            first_cross = np.flatnonzero(losses <= threshold)
            audit.compare(name+f'/{tag}:first_coarse_crossing', int(where[0]), int(first_cross[0]) if len(first_cross) else -1)
        row = dict(case=task['case'], order=q, resolution=directory.name, threshold=threshold,
                   handoff_time=t, handoff_train_mse=float(np.mean(h['residual']**2)),
                   scalar_available=f'scalar_state_{tag}' in data)
        matrix, drift = h['matrix'], h['drift']
        if matrix.shape != (m,m) or drift.shape != (m,) or h['fourier'].shape != (64,m+2):
            raise ValueError(f'{name}/{tag}: invalid finite coefficient dimensions')
        row['contraction_margin'] = float(np.linalg.eigvalsh((matrix+matrix.T)/2)[0]-np.linalg.norm(drift))
        spatial = query_basis@h['fourier']-np.column_stack((h['query_f'], h['query_c'], h['query_b']))
        row['fourier_field_rms'] = np.sqrt(np.mean(spatial**2, axis=0)).tolist()
        row['fourier_field_max'] = np.max(np.abs(spatial), axis=0).tolist()
        if not row['scalar_available']:
            handoffs.append(row)
            continue
        st = data[f'scalar_state_{tag}']
        stimes = data[f'scalar_times_{tag}']
        mask = times >= t
        if st.shape != (len(stimes), 2*m+1):
            raise ValueError(f'{name}/{tag}: invalid scalar state')
        audit.compare(name+f'/{tag}:scalar_physical_times', stimes, times[mask], rtol=0, atol=0)
        audit.compare(name+f'/{tag}:scalar_initial_residual', st[0,:m], h['residual'])
        audit.compare(name+f'/{tag}:scalar_initial_integrals', st[0,m:], np.zeros(m+1))
        I, J = st[:,m:2*m], st[:,-1]
        scalar_losses = np.mean(st[:,:m]**2, axis=1)
        audit.compare(name+f'/{tag}:scalar_loss', scalar_losses, data[f'scalar_loss_{tag}'])
        train_observer = labels[None,:]+h['residual'][None,:]-I@matrix.T+J[:,None]*drift[None,:]
        observer_error = maximum(train_observer-labels[None,:]-st[:,:m])
        audit.compare(name+f'/{tag}:all_time_exact_train_observer', train_observer, labels[None,:]+st[:,:m], atol=1e-8)
        weights = np.r_[1.,-I[-1],J[-1]]
        coefficients = h['fourier']@weights
        scalar = query_basis@coefficients
        train_output = train_basis@coefficients
        direct = h['query_f']-h['query_c']@I[-1]+h['query_b']*J[-1]
        static = h['query_f']
        fourier_static = query_basis@h['fourier'][:,0]
        audit.compare(name+f'/{tag}:scalar_Fourier_readout', scalar, data[f'scalar_output_{tag}'])
        audit.compare(name+f'/{tag}:untruncated_readout', direct, data[f'scalar_direct_output_{tag}'])
        audit.compare(name+f'/{tag}:static_readout', static, data[f'static_output_{tag}'])
        full = data['closure_output']
        row.update(**prefixed('scalar_vs_dense', fidelity(scalar,dense)),
                   **prefixed('scalar_vs_closure', fidelity(scalar,full)),
                   direct_freezing_rms=rms(direct-full), direct_freezing_max=maximum(direct-full),
                   fourier_output_rms=rms(scalar-direct), fourier_output_max=maximum(scalar-direct),
                   static_vs_closure_rms=rms(static-full), static_vs_closure_max=maximum(static-full),
                   fourier_static_vs_closure_rms=rms(fourier_static-full),
                   scalar_residual_final_mse=float(scalar_losses[-1]),
                   scalar_fourier_train_mse=float(np.mean((train_output-labels)**2)),
                   scalar_fourier_train_consistency_max=maximum(train_output-labels-st[-1,:m]),
                   exact_train_observer_consistency_max=observer_error,
                   max_scalar_loss_error_vs_closure=maximum(scalar_losses-losses[mask]))
        err,count = loss_difference(stimes,scalar_losses,reference['times'],reference['dense_loss'])
        row.update(max_scalar_loss_error_vs_dense=err,dense_loss_comparison_time_count=count)
        row['dense_fidelity_threshold_met'] = row['scalar_vs_dense_rms'] <= .05 and row['scalar_vs_dense_sign_disagreement'] <= .01
        row['closure_fidelity_threshold_met'] = row['scalar_vs_closure_rms'] <= .01 and row['scalar_vs_closure_max'] <= .05
        row['scalar_residual_fitted'] = row['scalar_residual_final_mse'] <= FIT
        row['scalar_fourier_function_fitted'] = row['scalar_fourier_train_mse'] <= FIT
        row['improvement_over_static'] = row['static_vs_closure_rms']/row['scalar_vs_closure_rms'] if row['scalar_vs_closure_rms'] else None
        row['improvement_over_fourier_static'] = row['fourier_static_vs_closure_rms']/row['scalar_vs_closure_rms'] if row['scalar_vs_closure_rms'] else None
        data[f'analysis_scalar_{tag}'] = scalar
        data[f'analysis_fourier_static_{tag}'] = fourier_static
        handoffs.append(row)
    metrics.update(handoffs=handoffs,missing_handoffs=missing)
    return metrics,data


def refinement(left, right, audit, name):
    lm,la = left;rm,ra = right
    audit.compare(name+':refinement_query_grid', la['angles'],ra['angles'],rtol=0,atol=0)
    audit.compare(name+':refinement_final_time',la['times'][-1],ra['times'][-1],rtol=0,atol=0)
    value,count=loss_difference(la['times'],la['closure_loss'],ra['times'],ra['closure_loss'])
    result=dict(resolutions=[lm['resolution'],rm['resolution']],closure_endpoint_rms=rms(la['closure_output']-ra['closure_output']),closure_loss_max=value,common_time_count=count,handoffs={})
    result['full_gate_passed']=result['closure_endpoint_rms'] <= .002 and value <= .001
    left_h={h['threshold']:h for h in lm['handoffs']};right_h={h['threshold']:h for h in rm['handoffs']}
    for threshold in THRESHOLDS:
        tag=f'{threshold:g}'
        if threshold not in left_h or threshold not in right_h:continue
        audit.compare(name+f'/{tag}:shared_handoff_time',left_h[threshold]['handoff_time'],right_h[threshold]['handoff_time'],rtol=0,atol=0)
        if f'analysis_scalar_{tag}' not in la or f'analysis_scalar_{tag}' not in ra:continue
        value,count=loss_difference(la[f'scalar_times_{tag}'],la[f'scalar_loss_{tag}'],ra[f'scalar_times_{tag}'],ra[f'scalar_loss_{tag}'])
        result['handoffs'][tag]=dict(scalar_endpoint_rms=rms(la[f'analysis_scalar_{tag}']-ra[f'analysis_scalar_{tag}']),scalar_loss_max=value,
            static_endpoint_rms=rms(la[f'static_output_{tag}']-ra[f'static_output_{tag}']),fourier_static_endpoint_rms=rms(la[f'analysis_fourier_static_{tag}']-ra[f'analysis_fourier_static_{tag}']),common_time_count=count)
    primary=result['handoffs'].get('0.01')
    result['primary_scalar_gate_passed']=None if primary is None else primary['scalar_endpoint_rms'] <= .002
    result['primary_scalar_loss_sensitivity']=None if primary is None else primary['scalar_loss_max']
    result['prescribed_gates_passed']=bool(result['full_gate_passed'] and result['primary_scalar_gate_passed'])
    return result


def plot_all(output, analyses, selected_arrays, references, titles):
    os.environ['MPLCONFIGDIR']=str(output/'matplotlib-cache')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.bbox':'tight'})
    def finish(fig,name):
        fig.tight_layout(rect=(0,.025,1,.96))
        for ext in ('png','pdf'):fig.savefig(output/f'{name}.{ext}',dpi=180)
        plt.close(fig)
    fig,axes=plt.subplots(2,1,figsize=(13,8),sharex=True)
    fig.suptitle('Final signed circle predictions: full closures and primary scalar continuations',fontsize=14)
    for ax,case in zip(axes,CASES):
        ref=references[case]['fine'];degrees=np.degrees(ref['angles'])
        for key,label,color in [('dense_output','Dense',COLORS['dense']),('q1_output','q=1',COLORS[1])]:ax.plot(degrees,ref[key],label=label,color=color,lw=1.8)
        for q in ORDERS:
            if (case,q) not in selected_arrays:continue
            data=selected_arrays[case,q]
            ax.plot(degrees,data['closure_output'],color=COLORS[q],lw=1.6,label=f'q={q}')
            if 'analysis_scalar_0.01' in data:ax.plot(degrees,data['analysis_scalar_0.01'],color=COLORS[f'scalar{q}'],ls='--',lw=1.4,label=f'Scalar of q={q}, switch 0.01')
        ax.scatter(np.degrees(ref['train_angles']),ref['labels'],edgecolor='black',facecolor='white',s=28,zorder=6,label='Training labels')
        ax.axhline(0,color='#dddddd',lw=.6);ax.set_title(f"{titles[case]} | t={ref['times'][-1]:g}",loc='left')
        ax.set_ylabel('Signed prediction');ax.grid(alpha=.15);ax.legend(ncol=4,fontsize=8,loc='best')
        ax.set_xlim(0,360);ax.set_xticks(np.arange(0,361,60))
    axes[-1].set_xlabel('Circle angle (degrees)')
    fig.text(.01,.004,'One shared initialization; true output units. Dense is an imitation reference, not unseen ground truth.',fontsize=9)
    finish(fig,'final-predictions')
    fig,axes=plt.subplots(2,1,figsize=(13,8),sharex=False)
    fig.suptitle('Training losses at equal physical times',fontsize=14)
    for ax,case in zip(axes,CASES):
        ref=references[case]['fine']
        for key,label,color in [('dense_loss','Dense',COLORS['dense']),('q1_loss','q=1',COLORS[1])]:ax.semilogy(ref['times'],np.maximum(ref[key],1e-16),color=color,lw=1.7,label=label)
        for q in ORDERS:
            if (case,q) not in selected_arrays:continue
            data=selected_arrays[case,q];ax.semilogy(data['times'],np.maximum(data['closure_loss'],1e-16),color=COLORS[q],label=f'q={q}',lw=1.6)
            if 'analysis_scalar_0.01' in data:
                ax.semilogy(data['scalar_times_0.01'],np.maximum(data['scalar_loss_0.01'],1e-16),color=COLORS[f'scalar{q}'],ls='--',label=f'Scalar q={q} residual',lw=1.4)
                row=next(h for h in analyses[case,q]['handoffs'] if h['threshold']==.01)
                ax.scatter([data['times'][-1]],[max(row['scalar_fourier_train_mse'],1e-16)],marker='D',facecolors='none',edgecolors=COLORS[f'scalar{q}'],s=45,label=f'Scalar q={q} Fourier MSE')
        ax.axhline(FIT,color='#999999',ls=':',lw=.8);ax.set_xlim(0,float(ref['times'][-1])*1.02)
        ax.set_title(titles[case],loc='left');ax.set_ylabel('Training MSE');ax.grid(alpha=.15,which='both');ax.legend(ncol=4,fontsize=8)
    axes[-1].set_xlabel('Physical time')
    fig.text(.01,.004,'Scalar lines are residual-ODE loss; diamonds are the finite Fourier function loss. Display floor 1e-16.',fontsize=9)
    finish(fig,'losses')
    fig,axes=plt.subplots(2,2,figsize=(13,8),sharex=True)
    fig.suptitle('All prescribed switches: separate freezing and Fourier errors',fontsize=14)
    for i,case in enumerate(CASES):
        for j,q in enumerate(ORDERS):
            ax=axes[i,j];audit=analyses.get((case,q));rows=[] if audit is None else [h for h in audit['handoffs'] if h['scalar_available']]
            rows=sorted(rows,key=lambda h:h['handoff_train_mse'])
            if rows:
                x=[h['handoff_train_mse'] for h in rows]
                for key,label,color,style in [('scalar_vs_closure_rms','Scalar / closure','#e58b21','-'),('direct_freezing_rms','Untruncated freezing','#16836d','-'),('fourier_output_rms','Fourier contribution','#7950aa',':'),('static_vs_closure_rms','Static / closure','#888888','--'),('scalar_vs_dense_rms','Scalar / dense','#bd3c78','-')]:
                    ax.loglog(x,[max(h[key],1e-16) for h in rows],marker='o',color=color,ls=style,label=label)
                ax.axhline(audit['closure_vs_dense_rms'],color=COLORS['dense'],lw=.9,label='Closure / dense')
            else:ax.text(.5,.5,'Scalar stage not available',ha='center',transform=ax.transAxes)
            ax.set_title(f'{titles[case]} | q={q}',loc='left',fontsize=10);ax.grid(alpha=.15,which='both');ax.set_ylabel('Circle RMS error')
            if i==1:ax.set_xlabel('Actual closure MSE at switch (smaller is later)')
    axes[0,0].legend(ncol=2,fontsize=8)
    finish(fig,'errors-by-switch')
    return matplotlib.__version__


def csv_rows(path, rows):
    fields=sorted({k for row in rows for k,v in row.items() if not isinstance(v,(list,dict))})
    with Path(path).open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(rows)


def markdown_report(output, report):
    lines=['# Higher-order circle comparison','',
        'Metrics are independently reconstructed from saved arrays. Both tasks and both orders are included; q=1 and dense are the unchanged original common-time references.','',
        f"Artifact checks: **{'PASS' if report['all_checks_passed'] else 'FAIL'}**. Scalar stage: **{'complete' if report['scalar_stage_complete'] else 'incomplete or not yet evaluated'}**. Fitting and approximation thresholds are reported separately.",'',
        '| Task | q | Final closure MSE | Max trajectory MSE error vs dense | Final circle RMS vs dense | Max circle error | Sign disagreement | Full refinement |',
        '|---|---:|---:|---:|---:|---:|---:|---|']
    for a in sorted(report['q1_baselines']+report['cases'], key=lambda a:(a['case'],a['order'])):
        lines.append(f"| {a['case']} | {a['order']} | {a['closure_final_mse']:.4g} | {a['max_loss_error_vs_dense']:.5g} | {a['closure_vs_dense_rms']:.5g} | {a['closure_vs_dense_max']:.5g} | {100*a['closure_vs_dense_sign_disagreement']:.3f}% | {a['full_refinement_gate_passed']} |")
    lines+=['','Trajectory error is the maximum absolute difference of training MSE over every exactly shared saved physical time from initialization through the common endpoint. No interpolated reference points enter this metric. Circle errors refer to the endpoint on 8192 queries.','',
        'Primary scalar switch: closure MSE 0.01.','',
        '| Task | q | Scalar/closure RMS | Scalar/dense RMS | Dense sign disagreement | Residual MSE | Fourier training MSE | Scalar refinement |',
        '|---|---:|---:|---:|---:|---:|---:|---|']
    for a in report['cases']:
        for h in a['handoffs']:
            if h['threshold']==.01 and h['scalar_available']:
                lines.append(f"| {a['case']} | {a['order']} | {h['scalar_vs_closure_rms']:.5g} | {h['scalar_vs_dense_rms']:.5g} | {100*h['scalar_vs_dense_sign_disagreement']:.3f}% | {h['scalar_residual_final_mse']:.4g} | {h['scalar_fourier_train_mse']:.4g} | {a['refinement']['primary_scalar_gate_passed']} |")
    lines+=['','Every prescribed switch, including early/late failures:','',
        '| Task | q | Switch | Time | Scalar/closure RMS | Freezing RMS | Fourier RMS | Static/closure RMS |',
        '|---|---:|---:|---:|---:|---:|---:|---:|']
    for a in report['cases']:
        for h in a['handoffs']:
            if h['scalar_available']:
                lines.append(f"| {a['case']} | {a['order']} | {h['threshold']:g} | {h['handoff_time']:g} | {h['scalar_vs_closure_rms']:.5g} | {h['direct_freezing_rms']:.5g} | {h['fourier_output_rms']:.5g} | {h['static_vs_closure_rms']:.5g} |")
            else:lines.append(f"| {a['case']} | {a['order']} | {h['threshold']:g} | {h['handoff_time']:g} | pending | pending | pending | pending |")
    lines+=['','Dense fidelity requires RMS <=0.05 and sign disagreement <=1%. Scalar-to-closure fidelity requires RMS <=0.01 and maximum error <=0.05. These thresholds are not silently strengthened by the separate training-fit flags (MSE <=1e-6). All-time fitting, whole-circle accuracy, and terminal-tube hypotheses are not certified.','',
        'The 729-number scalar system includes 17 evolving numbers and 712 fixed coefficients, but obtaining them still requires full-width pre-switch training. Error components can cancel, so their RMS values need not add. Original dense refinement, higher-order refinement, initialization/reference hashes, observer identities, every maximum/sign/loss metric, and missing artifacts are in `analysis.json`; flat tables are in `closure_metrics.csv` and `scalar_metrics.csv`.','',
        'Plots: `final-predictions.png/pdf`, `losses.png/pdf`, and `errors-by-switch.png/pdf`. Their loss axes separate scalar residual loss from Fourier-function training MSE. Only finite saved states and finite observation grids are inspected; the analyzer neither trains nor verifies every intermediate RK stage.']
    (output/'REPORT.md').write_text('\n'.join(lines)+'\n')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();begin=time.perf_counter();run=args.run.resolve();output=args.output.resolve()
    if not run.is_relative_to(GENERATED) or not output.is_relative_to(GENERATED):
        parser.error('Run and output must remain inside this study generated namespace')
    output.mkdir(parents=True,exist_ok=False);shutil.copy2(__file__,output/Path(__file__).name)
    audit=Audit();audit.file(Path(__file__).resolve())
    provenance=audit.json(run/'provenance.json');task_data=audit.json(run/'circle_task_inputs.json')
    reference=Path(provenance.get('dense_reference_root',REFERENCE))
    if not reference.is_absolute():reference=(ROOT/reference).resolve()
    if reference.resolve()!=REFERENCE.resolve():raise ValueError('Unexpected dense reference; only the original same-study campaign is admitted')
    initial=audit.arrays(run/'initialization.npz');reference_initial=audit.arrays(reference/'initialization.npz')
    for key in ('a','w0','readout'):audit.compare('initialization:'+key,initial[key],reference_initial[key],rtol=0,atol=0)
    rng=np.random.default_rng(20260920)
    audit.compare('initial_A_generator',initial['a'],rng.standard_normal((1024,2)),rtol=0,atol=0)
    audit.compare('initial_W0_generator',initial['w0'],rng.standard_normal((1024,1024))/32,rtol=0,atol=0)
    audit.compare('initial_zero_readout',initial['readout'],np.zeros(1024),rtol=0,atol=0)
    initial_hashes={'a_initial_hash':array_digest(initial['a']),'w0_initial_hash':array_digest(initial['w0'])}
    audit.compare('task_input_file_hash',audit.file(run/'circle_task_inputs.json'),audit.file(reference/'circle_task_inputs.json'))
    for name in ('HIGHER_ORDER_EXPERIMENT_PLAN.md',):
        if (run/name).exists():audit.file(run/name)
    for source,expected in provenance.get('source_hashes',{}).items():
        copied=run/Path(source).name
        if not copied.is_file():raise ValueError(f'Missing frozen source copy: {copied}')
        audit.compare('frozen_source:'+copied.name,audit.file(copied),expected)
    recorded_reference_hashes=provenance.get('dense_reference_hashes',{})
    for source,expected in recorded_reference_hashes.items():
        p=Path(source)
        if not p.is_absolute():p=ROOT/p if (ROOT/p).is_file() else reference/p
        p=p.resolve()
        if not p.is_relative_to(reference.resolve()):raise ValueError('Reference hash points outside the admitted original campaign')
        audit.compare('recorded_reference:'+str(p),audit.file(p),expected)
    tasks={t['case']:t for t in task_data['tasks']};titles={c:tasks[c].get('title',c) for c in CASES}
    references={};dense_refinement={};baselines=[]
    for case in CASES:
        references[case]={r:audit.arrays(reference/case/r/'curves.npz') for r in ('coarse','fine')}
        a,b=references[case]['coarse'],references[case]['fine']
        v,k=loss_difference(a['times'],a['dense_loss'],b['times'],b['dense_loss'])
        dense_refinement[case]={'endpoint_rms':rms(a['dense_output']-b['dense_output']),'loss_max':v,'common_time_count':k}
        dense_refinement[case]['passed']=dense_refinement[case]['endpoint_rms']<=.002 and v<=.001
        q1_loss_error,q1_loss_count=loss_difference(b['times'],b['q1_loss'],b['times'],b['dense_loss'])
        q1_refine_loss,_=loss_difference(a['times'],a['q1_loss'],b['times'],b['q1_loss'])
        q1_refine_rms=rms(a['q1_output']-b['q1_output'])
        baselines.append(dict(case=case,order=1,resolution='fine',final_time=float(b['times'][-1]),
            q1_final_mse=float(b['q1_loss'][-1]),closure_final_mse=float(b['q1_loss'][-1]),
            max_loss_error_vs_dense=q1_loss_error,loss_comparison_time_count=q1_loss_count,
            refinement_endpoint_rms=q1_refine_rms,refinement_loss_max=q1_refine_loss,
            full_refinement_gate_passed=q1_refine_rms<=.002 and q1_refine_loss<=.001,
            **prefixed('closure_vs_dense',fidelity(b['q1_output'],b['dense_output'])),
            **prefixed('q1_vs_dense',fidelity(b['q1_output'],b['dense_output']))))
    analyses={};plot_arrays={};all_resolution_metrics=[];missing=[]
    for case in CASES:
        for q in ORDERS:
            done={}
            for res in ('coarse','fine','refined'):
                directory=run/case/f'q{q}'/res
                if (directory/'summary.json').exists():
                    dense=references[case]['coarse' if res=='coarse' else 'fine']
                    done[res]=resolution_data(directory,tasks[case],q,dense,initial_hashes,audit)
                    all_resolution_metrics.append(done[res][0])
            if 'coarse' not in done or 'fine' not in done:
                missing.append({'case':case,'order':q,'available_resolutions':list(done)});continue
            selected='refined' if 'refined' in done else 'fine';left='fine' if selected=='refined' else 'coarse'
            metrics,arrays=done[selected]
            metrics['refinement']=refinement(done[left],done[selected],audit,f'{case}/q{q}')
            metrics['original_coarse_fine_refinement']=refinement(done['coarse'],done['fine'],audit,f'{case}/q{q}/original')
            metrics['full_refinement_gate_passed']=metrics['refinement']['full_gate_passed']
            metrics['primary_scalar_refinement_gate_passed']=metrics['refinement']['primary_scalar_gate_passed']
            metrics['refinement_endpoint_rms']=metrics['refinement']['closure_endpoint_rms']
            metrics['refinement_loss_max']=metrics['refinement']['closure_loss_max']
            metrics['dense_reference_refinement_passed']=dense_refinement[case]['passed']
            for row in metrics['handoffs']:
                if not row['scalar_available']:continue
                sensitivity=metrics['refinement']['handoffs'].get(f"{row['threshold']:g}")
                row['refinement']=sensitivity
                if sensitivity:
                    tail=sensitivity['static_endpoint_rms']+metrics['refinement']['closure_endpoint_rms']
                    row['static_tail_sensitivity']=tail
                    row['static_tail_resolved']=row['static_vs_closure_rms']>10*tail
                    row['at_least_twofold_static_improvement']=2*row['scalar_vs_closure_rms']<=row['static_vs_closure_rms']
            analyses[case,q]=metrics;plot_arrays[case,q]=arrays
    scalar_complete=len(analyses)==4 and all(not a['missing_handoffs'] and len(a['handoffs'])==3 and all(h['scalar_available'] for h in a['handoffs']) for a in analyses.values())
    for case,q in analyses:
        prefix=f'{case}/q{q}/'
        analyses[case,q]['artifact_checks_passed']=all(c['passed'] for c in audit.checks if c['name'].startswith(prefix))
    mpl=plot_all(output,analyses,plot_arrays,references,titles)
    report=dict(run=str(run),reference_root=str(reference),cases=list(analyses.values()),q1_baselines=baselines,
                dense_reference_refinement=dense_refinement,all_resolution_metrics=all_resolution_metrics,
                missing_case_orders=missing,scalar_stage_complete=scalar_complete,
                all_checks_passed=audit.passed,checks=audit.checks,source_sha256=audit.hashes,
                recorded_reference_hashes_available=bool(recorded_reference_hashes),
                primary_threshold=.01,fit_threshold=FIT,scalar_count=729,
                runtime_seconds=time.perf_counter()-begin,numpy_version=np.__version__,matplotlib_version=mpl,
                scope='One seed, two tasks, saved finite times and 8192 circle queries; no training or uniform-circle certificate.')
    csv_rows(output/'closure_metrics.csv',[{k:v for k,v in a.items() if not isinstance(v,(dict,list))} for a in baselines+list(analyses.values())])
    csv_rows(output/'scalar_metrics.csv',[h for a in analyses.values() for h in a['handoffs']])
    write_json(output/'analysis.json',report);markdown_report(output,report)
    print(json.dumps({'case_orders':len(analyses),'scalar_stage_complete':scalar_complete,'checks_passed':audit.passed,'runtime_seconds':report['runtime_seconds'],'output':str(output)},indent=2))
    return 0 if audit.passed and not missing else 2


if __name__=='__main__':
    raise SystemExit(main())
