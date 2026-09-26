"""Update the eleven scientific panels and nearest-size table with new p7."""
import argparse
import json
import math
import numpy as np
import suite_plots as previous
from matplotlib.lines import Line2D

ORDERS = {'new':(1,3,5,7), 'old':(1,3,5), 'gaussian':(1,3,5), 'orthogonal':(1,3,5)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--analysis', type=previous.Path, required=True)
    parser.add_argument('--manifest', type=previous.Path, required=True)
    parser.add_argument('--out', type=previous.Path, required=True)
    args = parser.parse_args()
    rows = json.loads((args.analysis/'metrics.json').read_text())
    cases = list(json.loads(args.manifest.read_text())['cases'])
    lookup = {(r['case'],r['method']):r for r in rows}
    expected = {(c,f'{f}_p{p}') for c in cases for f in ORDERS for p in ORDERS[f]}
    assert len(rows)==143 and set(lookup)==expected
    out = previous.owned(args.out)
    assert not out.exists()
    out.mkdir(parents=True)
    plt = previous.plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes = plt.subplots(4,3,figsize=(15.2,12.6),sharex=True,sharey=True)
    positive = [r[level+'_rms'] for r in rows for level in ('primary','refined') if r.get(level+'_rms') is not None and r[level+'_rms']>0]
    displayed = []
    for ax,case in zip(axes.flat,cases):
        for family in ORDERS:
            selected = [lookup[case,f'{family}_p{p}'] for p in ORDERS[family]]
            x = [r['vectors'] for r in selected]
            for level,style,alpha,width in (('primary',':',.42,1.),('refined','-',1.,1.7)):
                y = [r.get(level+'_rms') if r['valid'] else np.nan for r in selected]
                line = ax.plot(x,y,color=previous.COLORS[family],ls=style,alpha=alpha,lw=width,
                    marker=previous.MARKERS[family] if level=='refined' else None,ms=5)[0]
                assert np.array_equal(line.get_xdata(),x)
                assert np.array_equal(line.get_ydata(),y,equal_nan=True)
            for r in selected:
                value=r.get('refined_rms')
                displayed.append(dict(case=case,method=r['method'],vectors=r['vectors'],
                    primary_rms=r.get('primary_rms'),refined_rms=value,valid=r['valid']))
                if not r['valid'] and value is not None and value>0:
                    ax.scatter([r['vectors']],[value],marker='x',s=65,lw=1.7,color=previous.COLORS[family],zorder=5)
        ax.set_title(previous.title(case),loc='left',fontsize=11,fontweight='medium')
        invalid = [f"{r['family']} p{r['p']}" for r in rows if r['case']==case and not r['valid']]
        if invalid:
            ax.text(.02,.035,'Unvalidated: '+', '.join(invalid),transform=ax.transAxes,fontsize=8,color='#7a3434')
        ax.set_yscale('log')
        ax.set_ylim(min(positive)/1.5,max(positive)*1.5)
        ax.set_xlim(0,157)
        ax.set_xticks([0,38,72,112,149])
        ax.grid(which='major',alpha=.2)
    ax=axes.flat[-1]
    ax.axis('off')
    ax.text(.04,.94,'Retained dictionary vectors',transform=ax.transAxes,fontweight='bold',va='top')
    ax.text(.04,.78,'Derivative: 6, 18, 38, 72\nOld / Gaussian / orthogonal: 8, 45, 149',transform=ax.transAxes,linespacing=1.7,va='top')
    ax.text(.04,.48,'Solid: finer endpoint pair\nDotted: primary endpoint pair\n×: terminal diagnostic failing a validity gate',transform=ax.transAxes,linespacing=1.7,fontsize=9,va='top')
    fig.legend(handles=[Line2D([0],[0],color=previous.COLORS[f],marker=previous.MARKERS[f],label=previous.LABELS[f],lw=1.7) for f in ORDERS],
               loc='upper center',ncol=4,bbox_to_anchor=(.5,.965),frameon=False)
    fig.suptitle('Circle RMS discrepancy versus retained dictionary vectors',fontsize=17,y=.993)
    fig.supxlabel('Total retained vectors K₁ + K₂ (linear scale)',y=.031)
    fig.supylabel('RMS versus the common dense learned function (log scale)',x=.008)
    fig.text(.5,.002,'Width 2048 · Own first detected training MSE 0.001 crossing · 8192 circle angles · Fixed archived controls and common references',ha='center',fontsize=9)
    fig.tight_layout(rect=(.022,.049,1,.937),h_pad=2.4,w_pad=1.7)
    for suffix in ('png','pdf','svg'):
        fig.savefig(out/('suite_rms_vs_vectors.'+suffix),dpi=180,bbox_inches='tight')
    plt.close(fig)
    table_methods = ('new_p5','new_p7','old_p3','gaussian_p3','orthogonal_p3')
    labels = ['Task','Derivative p5\n38 vectors','Derivative p7\n72 vectors','Old p3\n45 vectors','Gaussian p3\n45 vectors','Orthogonal p3\n45 vectors']
    body=[]
    tabledata=[]
    for case in cases:
        values=[]
        for method in table_methods:
            r=lookup[case,method]
            v=r.get('refined_rms')
            values.append(('Unavailable' if v is None else f'{v:.5f}')+(' †' if not r['valid'] else ''))
            tabledata.append(dict(case=case,method=method,value=v,valid=r['valid']))
        body.append([previous.title(case),*values])
    fig,ax=plt.subplots(figsize=(15,.43*len(cases)+1.5))
    ax.axis('off')
    table=ax.table(cellText=body,colLabels=labels,colWidths=[.325]+[.135]*5,cellLoc='right',bbox=[0,0,1,1])
    table.auto_set_font_size(False);table.set_fontsize(10.5)
    for (r,c),cell in table.get_celld().items():
        cell.set_edgecolor('#d8dce2')
        if r==0:
            cell.set_facecolor('#e8eef5');cell.set_text_props(weight='bold')
        elif r%2==0:
            cell.set_facecolor('#f7f9fc')
        if c==0:
            cell.set_text_props(ha='left')
        if r>0 and c>0 and not lookup[cases[r-1],table_methods[c-1]]['valid']:
            cell.set_text_props(color='#9d3734')
    fig.suptitle('Derivative p7, preceding p5, and nearest available archived size',fontsize=16,y=.985)
    fig.text(.5,.022,'Finer endpoint pair; common dense reference per task. Lower is better.\n72 versus 45 vectors is the nearest available comparison, not an exact size match. † Unvalidated terminal diagnostic.',ha='center',fontsize=10)
    fig.subplots_adjust(left=.018,right=.982,bottom=.135,top=.9)
    for i,values in enumerate(body,1):
        for j,value in enumerate(values):
            assert table.get_celld()[i,j].get_text().get_text()==value
    for suffix in ('png','pdf','svg'):
        fig.savefig(out/('suite_nearest_size_table.'+suffix),dpi=180,bbox_inches='tight')
    plt.close(fig)
    assert len(displayed)==143 and len(tabledata)==55
    previous.save_json(out/'plot_data.json',dict(curves=displayed,table=tabledata))
    previous.save_json(out/'plot_validation.json',dict(passed=True,displayed_refined_points=143,case_panels=11,
        table_metric_cells=55,artist_coordinates_equal_source_metrics=True,table_artist_text_equal_source_values=True,
        x_axis='linear total dictionary vectors',y_axis='log circle RMS',
        metrics_path=str(args.analysis/'metrics.json'),metrics_sha256=previous.sha(args.analysis/'metrics.json'),
        plotter_sha256=previous.sha(__file__),style_source_sha256=previous.sha(previous.__file__)))
    print(json.dumps(dict(out=str(out),valid_rows=sum(r['valid'] for r in rows),rows=len(rows))))


if __name__ == '__main__':
    main()
