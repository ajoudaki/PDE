"""Publication files for the fixed eleven-case suite; no model computation."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT/'data/generated/gradient_flow_probe_dictionary_20260921'
FAMILIES = ('new','old','gaussian','orthogonal')
LABELS = {'new':'Derivative dictionary','old':'Old dictionary','gaussian':'Gaussian control','orthogonal':'Orthogonal control'}
COLORS = {'new':'#1165a3','old':'#2b8c59','gaussian':'#db7b19','orthogonal':'#8b4daf'}
MARKERS = {'new':'o','old':'s','gaussian':'^','orthogonal':'D'}
ORDERS = (1,3,5)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def owned(path):
    path = path.resolve()
    if not path.is_relative_to(DATA) or path == DATA:
        raise ValueError('output must be in current study generated directory')
    return path


def title(case):
    return case.replace('_', ' ').capitalize()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--analysis', type=Path, nargs='+', required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    out = owned(args.out)
    if out.exists():
        raise FileExistsError(out)
    manifest = json.loads(args.manifest.read_text())
    cases = list(manifest['cases'])
    rows, provenance = [], []
    for directory in args.analysis:
        directory = owned(directory)
        data = json.loads((directory/'metrics.json').read_text())
        rows.extend(data)
        provenance.append(dict(path=str(directory), metrics_sha256=sha(directory/'metrics.json'),
                               completion=json.loads((directory/'completion.json').read_text())))
    lookup = {}
    for row in rows:
        key = row['case'], row['method']
        if key in lookup:
            raise ValueError('duplicate analysis cell '+str(key)+'; pass exactly one final result per case')
        lookup[key] = row
    expected = {(case, f'{family}_p{p}') for case in cases for family in FAMILIES for p in ORDERS}
    if set(lookup) != expected:
        raise ValueError(f'analysis coverage mismatch, missing={sorted(expected-set(lookup))}, extra={sorted(set(lookup)-expected)}')
    out.mkdir(parents=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    ncols, nrows = 3, math.ceil(len(cases)/3)
    fig, axes = plt.subplots(nrows,ncols,figsize=(15.2,3.15*nrows),sharex=True,sharey=True)
    displayed_points=[]
    positive = [r.get(level+'_rms') for r in rows for level in ('primary','refined') if r.get(level+'_rms') is not None and r[level+'_rms'] > 0]
    ymin, ymax = min(positive)/1.5, max(positive)*1.5
    for ax, case in zip(axes.flat,cases):
        for family in FAMILIES:
            selected = [lookup[case,f'{family}_p{p}'] for p in ORDERS]
            x = [r['vectors'] for r in selected]
            for level, style, alpha, width in (('primary',':',.42,1.),('refined','-',1.,1.7)):
                y = [r.get(level+'_rms') if r['valid'] else np.nan for r in selected]
                line=ax.plot(x,y,color=COLORS[family],ls=style,alpha=alpha,lw=width,
                        marker=MARKERS[family] if level=='refined' else None,ms=5)[0]
                assert np.array_equal(line.get_xdata(),x)
                assert np.array_equal(line.get_ydata(),y,equal_nan=True)
            for r in selected:
                value = r.get('refined_rms')
                displayed_points.append(dict(case=case,method=r['method'],vectors=r['vectors'],
                    primary_rms=r.get('primary_rms'),refined_rms=value,valid=r['valid'],
                    marker='family' if r['valid'] else 'invalid_cross'))
                if not r['valid'] and value is not None and value > 0:
                    scatter=ax.scatter([r['vectors']],[value],marker='x',s=65,lw=1.7,color=COLORS[family],zorder=5)
                    assert np.array_equal(scatter.get_offsets(),[[r['vectors'],value]])
        invalid = [f"{r['family']} p{r['p']}" for r in rows if r['case']==case and not r['valid']]
        ax.set_title(title(case),loc='left',fontsize=11,fontweight='medium')
        if invalid:
            ax.text(.02,.035,'Unvalidated: '+', '.join(invalid),transform=ax.transAxes,fontsize=8,color='#7a3434',wrap=True)
        ax.set_yscale('log')
        ax.set_ylim(ymin,ymax)
        ax.set_xlim(0,157)
        ax.set_xticks([0,38,75,112,149])
        ax.grid(which='major',alpha=.2)
    for ax in list(axes.flat)[len(cases):]:
        ax.axis('off')
        ax.text(.04,.94,'Retained vectors at p = 1, 3, 5',transform=ax.transAxes,fontweight='bold',va='top')
        ax.text(.04,.78,'Derivative: 6, 18, 38\nOld / Gaussian / orthogonal: 8, 45, 149',transform=ax.transAxes,linespacing=1.7,va='top')
        ax.text(.04,.48,'Solid: finer endpoint pair\nDotted: primary endpoint pair\n×: terminal diagnostic failing a validity gate',transform=ax.transAxes,linespacing=1.7,fontsize=9,va='top')
    handles = [Line2D([0],[0],color=COLORS[f],marker=MARKERS[f],label=LABELS[f],lw=1.7) for f in FAMILIES]
    fig.legend(handles=handles,loc='upper center',ncol=4,bbox_to_anchor=(.5,.965),frameon=False)
    fig.suptitle('Circle RMS discrepancy versus retained dictionary vectors',fontsize=17,y=.993)
    fig.supxlabel('Total retained vectors K₁ + K₂ (linear scale)',y=.031)
    fig.supylabel('RMS versus the common dense learned function (log scale)',x=.008)
    fig.text(.5,.002,'Width 2048 · Own first detected training MSE 0.001 crossing · 8192 circle angles · Fixed archived controls and common references',ha='center',fontsize=9)
    fig.tight_layout(rect=(.022,.049,1,.937),h_pad=2.4,w_pad=1.7)
    for suffix in ('png','pdf','svg'):
        fig.savefig(out/('suite_rms_vs_vectors.'+suffix),dpi=180,bbox_inches='tight')
    plt.close(fig)
    # A readable p5 table retains invalid controls with an explicit marker.
    labels = ['Task','Derivative p5\n38 vectors','Old p3\n45 vectors','Gaussian p3\n45 vectors','Orthogonal p3\n45 vectors']
    body=[]
    invalid_notes=[]
    markdown=['| Task | Derivative p5 (38) | Old p3 (45) | Gaussian p3 (45) | Orthogonal p3 (45) |', '|---|---:|---:|---:|---:|']
    for case in cases:
        values=[]
        for family in FAMILIES:
            baseline_p = 5 if family == 'new' else 3
            row=lookup[case,f'{family}_p{baseline_p}']
            value=row.get('refined_rms')
            cell='Unavailable' if value is None else f'{value:.5f}'
            if not row['valid']:
                cell+=' †'
                invalid_notes.append(dict(case=case,method=row['method'],reasons=row['reasons']))
            values.append(cell)
        body.append([title(case),*values])
        markdown.append('| '+case+' | '+' | '.join(values)+' |')
    fig,ax=plt.subplots(figsize=(13, .43*len(cases)+1.3))
    ax.axis('off')
    table=ax.table(cellText=body,colLabels=labels,colWidths=[.38,.155,.155,.155,.155],cellLoc='right',bbox=[0,0,1,1])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (r,c),cell in table.get_celld().items():
        cell.set_edgecolor('#d8dce2')
        if r==0:
            cell.set_facecolor('#e8eef5')
            cell.set_text_props(weight='bold')
        elif r%2==0:
            cell.set_facecolor('#f7f9fc')
        if c==0:
            cell.set_text_props(ha='left')
        if r>0 and c>0 and not lookup[cases[r-1],f"{FAMILIES[c-1]}_p{5 if FAMILIES[c-1] == 'new' else 3}"]['valid']:
            cell.set_text_props(color='#9d3734')
    fig.suptitle('38-vector derivative vs 45-vector baselines',fontsize=17,y=.985)
    note=('† Numerical validity gate failed; value retained as a terminal diagnostic.' if invalid_notes
          else 'All 44 displayed cells pass the numerical validity checks.')
    fig.text(.5,.022,'Circle RMS at the finer endpoint pair; common dense reference per task. Lower is better.\n'+note,ha='center',fontsize=10)
    fig.subplots_adjust(left=.018,right=.982,bottom=.115,top=.91)
    for i, values in enumerate(body,1):
        for j,value in enumerate(values):
            assert table.get_celld()[i,j].get_text().get_text() == value
    for suffix in ('png','pdf','svg'):
        fig.savefig(out/('suite_nearest_size_table.'+suffix),dpi=180,bbox_inches='tight')
    plt.close(fig)
    (out/'suite_nearest_size_table.md').write_text('\n'.join(markdown)+'\n\nFiner endpoint pair. '+note+'\n')
    assert len(displayed_points)==132 and len({(p['case'],p['method']) for p in displayed_points})==132
    save_json(out/'plot_data.json',dict(refined_curve_points=displayed_points,nearest_size_table=body))
    save_json(out/'plot_validation.json',dict(passed=True,source_metric_rows=len(rows),
        displayed_refined_points=len(displayed_points),validated_points=sum(p['valid'] for p in displayed_points),
        invalid_crosses=sum(not p['valid'] for p in displayed_points),
        case_panels=len(cases),nearest_size_table_rows=len(body),nearest_size_metric_cells=4*len(body),
        nearest_size_invalid_metric_cells=len(invalid_notes),
        artist_coordinates_equal_source_metrics=True,table_artist_text_equal_source_values=True,
        x_axis='linear total dictionary vectors',y_axis='log circle RMS',
        sources=[dict(path=str(directory/'metrics.json'),sha256=sha(directory/'metrics.json')) for directory in args.analysis]))
    save_json(out/'invalid_cells.json',[dict(case=r['case'],method=r['method'],reasons=r['reasons']) for r in rows if not r['valid']])
    # Matched case set is declared without silently replacing failed controls.
    common=[case for case in cases if all(lookup[case,f'{f}_p{p}']['valid'] for f in FAMILIES for p in ORDERS)]
    save_json(out/'coverage.json',dict(declared_cases=cases,rows=len(rows),valid_rows=sum(r['valid'] for r in rows),
        common_all_method_cases=common,excluded_from_all_method_intersection=[c for c in cases if c not in common],
        counts={f:{str(p):lookup[cases[0],f'{f}_p{p}']['vectors'] for p in ORDERS} for f in FAMILIES},
        aggregation='No aggregate scores plotted; each panel retains its full fixed method list.'))
    save_json(out/'plot_provenance.json',dict(sources=provenance,plotter_sha256=sha(__file__),manifest_sha256=sha(args.manifest),
        outputs={str(p):sha(p) for p in sorted(out.iterdir()) if p.is_file()}))
    print(json.dumps(dict(out=str(out),valid_rows=sum(r['valid'] for r in rows),total_rows=len(rows),common_cases=common)),flush=True)


if __name__=='__main__':
    main()
