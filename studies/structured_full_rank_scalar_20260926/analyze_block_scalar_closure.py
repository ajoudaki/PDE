"""Check saved moving-block states and plot the two distinct approximation errors."""
import block_scalar_closure as scalar
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from reportlab.graphics import renderPDF,renderPM
from reportlab.graphics.shapes import Drawing,Rect,Circle
from reportlab.lib.colors import HexColor
from plot_block_continuation import text,line,axis_top,INK,GRID
from circle_tasks import BY_NAME

TASKS=('near_pair_sin9','cluster_triple_cos9','alternating5')
LABELS=('Close-input pair','Clustered cosine-9','Alternating-5')
COUNTS=(8,32,64)
BLUE=HexColor('#2563eb');ORANGE=HexColor('#d95f02')


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def audit(out):
    manifest=json.loads((out/'manifest.json').read_text())
    source=Path(__file__).resolve().parent
    for name,h in manifest['sources'].items():
        assert digest(source/name)==h and digest(out/'source_snapshot'/name)==h
    rows=json.loads((out/'results.json').read_text())
    comparisons=json.loads((out/'comparisons.json').read_text())
    selection=json.loads((out/'selection.json').read_text())
    pool=scalar.initial_pool(2048,16,1)
    predictions={};max_forward=0.;max_mse=0.
    for row in rows:
        path=out/row['data_file']
        assert digest(path)==row['data_sha256']
        assert row['fitted'] and row['train_mse']<=.01*(1+1e-7)
        assert row['min_clock']>=1 and row['total_seconds']<60
        u,y=BY_NAME[row['task']].data()
        with np.load(path) as data:
            layout,G,initial=scalar.initialize(pool,data['indices'],u,row['order'])
            assert np.array_equal(data['initial_vector'],initial)
            assert np.array_equal(data['G'],G)
            assert row['dynamic_scalars']==layout.size and row['static_G_scalars']==G.size
            assert np.all(np.isfinite(data['vector']))
            # Restore only the retained model; neither pool nor reference is used by predict.
            pred=scalar.predict(layout,data['G'],data['vector'],data['angles'])
            train=scalar.forward(layout,data['G'],data['vector'],u)[0]
            max_forward=max(max_forward,float(np.max(np.abs(pred-data['prediction']))))
            mse=float(np.mean((train-y)**2))
            max_mse=max(max_mse,abs(mse-row['train_mse']))
            assert np.max(np.abs(train-data['train_prediction']))<1e-12
            predictions[row['tag']]=data['prediction']
            if row['kind']=='representative':
                expected=np.random.default_rng(np.random.SeedSequence([1,row['subset_stream']])).permutation(128)[:row['q']]
                assert np.array_equal(expected,data['indices'])
    assert max_forward<1e-12 and max_mse<1e-12
    baseline=Path(manifest['baseline']);dense={}
    for name,h in manifest['baseline_data_hashes'].items():
        assert digest(baseline/name)==h
        with np.load(baseline/name) as data:dense[name]=data['prediction']
    max_metric=0.
    for row in comparisons:
        p=predictions[row['tag']];ref=predictions[selection['references'][row['task']]]
        expected=float(np.sqrt(np.mean((p-ref)**2)))
        max_metric=max(max_metric,abs(expected-row['rms_vs_full_closure']))
        assert abs(expected-row['rms_vs_full_closure'])<1e-12
        for method,key in (('block16','rms_vs_dense_block16'),('gaussian','rms_vs_dense_gaussian')):
            expected=float(np.sqrt(np.mean((p-dense[f"{row['task']}__{method}.npz"])**2)))
            assert abs(expected-row[key])<1e-12
    assert len([r for r in rows if r['kind']=='representative'])==27
    refinement=json.loads((out/'refinement.json').read_text())
    assert refinement['passed']
    report={'source_hashes_verified':True,'saved_states_verified':len(rows),
        'exact_initial_subsets_verified':True,'restored_circle_forward_max_difference':max_forward,
        'training_mse_max_difference':max_mse,'metric_max_difference':max_metric,
        'all_fitted':True,'solver_refinement':refinement,
        'max_loss_rise':max(r['max_loss_rise'] for r in rows),
        'min_representative_seconds':min(r['total_seconds'] for r in rows if r['kind']=='representative'),
        'max_representative_seconds':max(r['total_seconds'] for r in rows if r['kind']=='representative')}
    (out/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
    with (out/'summary.csv').open('w') as file:
        writer=csv.writer(file)
        writer.writerow(['task','q','kind','subset_stream','rms_vs_full_closure','rms_vs_dense_block16','rms_vs_dense_gaussian'])
        for r in comparisons:writer.writerow([r[k] for k in ('task','q','kind','subset_stream','rms_vs_full_closure','rms_vs_dense_block16','rms_vs_dense_gaussian')])
    return report


def plot(out):
    summaries=json.loads((out/'summary.json').read_text())
    rows=json.loads((out/'results.json').read_text())
    selection=json.loads((out/'selection.json').read_text())
    refs={task:next(r for r in rows if r['tag']==selection['references'][task]) for task in TASKS}
    drawing=Drawing(1210,820)
    drawing.add(Rect(0,0,1210,820,fillColor=HexColor('#ffffff'),strokeColor=None))
    text(drawing,605,787,'Moving-block scalar closure: circle prediction error',size=21,anchor='middle')
    text(drawing,605,761,'Block size k = 16 | History P = 8 | Stop MSE = 0.01 | Three nested subset draws',size=12,anchor='middle')
    text(drawing,605,728,'Population compression only: RMS versus all 128 blocks at the same history order',size=13,anchor='middle')
    text(drawing,605,407,'Total discrepancy: RMS versus the original width-2048 dense Gaussian',size=13,anchor='middle')
    for row_index,metric in enumerate(('rms_vs_full_closure','rms_vs_dense_gaussian')):
        for column,(task,label) in enumerate(zip(TASKS,LABELS)):
            left=65+column*400;bottom=480-row_index*320;width=310;height=190
            group={r['q']:r[metric] for r in summaries if r['task']==task}
            maximum=max(r['max'] for r in group.values())
            baseline=refs[task]['rms_vs_dense_gaussian'] if row_index else None
            if baseline is not None:maximum=max(maximum,baseline)
            step,count=axis_top(maximum);top=step*count
            xs=[left+width*(math.log2(q)-3)/3 for q in COUNTS]
            yp=lambda y:bottom+height*y/top
            text(drawing,left+width/2,bottom+height+20,label,size=14,anchor='middle')
            text(drawing,left,bottom+height+4,'Absolute RMS',size=9)
            for j in range(count+1):
                value=j*step;yy=yp(value)
                line(drawing,left,yy,left+width,yy,GRID,.7)
                text(drawing,left-8,yy-3,f'{value:.3g}',size=9,anchor='end')
            line(drawing,left,bottom,left,bottom+height,INK,.8)
            line(drawing,left,bottom,left+width,bottom,INK,.8)
            ys=[]
            for q,xx in zip(COUNTS,xs):
                r=group[q];yy=yp(r['mean']);ys.append(yy)
                line(drawing,xx,yp(r['min']),xx,yp(r['max']),BLUE,1.2)
                for edge in ('min','max'):line(drawing,xx-4,yp(r[edge]),xx+4,yp(r[edge]),BLUE,1.2)
                drawing.add(Circle(xx,yy,4,fillColor=BLUE,strokeColor=None))
                text(drawing,xx,bottom-20,str(q),size=11,anchor='middle')
            for j in range(2):line(drawing,xs[j],ys[j],xs[j+1],ys[j+1],BLUE,2)
            if baseline is not None:line(drawing,left,yp(baseline),left+width,yp(baseline),ORANGE,1.4,[4,4])
            text(drawing,left+width/2,bottom-43,'Representative blocks q (log2)',size=10,anchor='middle')
    line(drawing,175,81,210,81,BLUE,2)
    text(drawing,220,77,'Mean RMS; bars show min-max over three subsets',size=11)
    line(drawing,665,81,700,81,ORANGE,1.4,[4,4])
    text(drawing,710,77,'Full 128-block closure versus dense Gaussian',size=11)
    text(drawing,605,44,'All models fitted. Each panel uses its own linear RMS scale. Reference population width is finite: 2048.',size=11,anchor='middle')
    text(drawing,605,24,'q = 8 / 32 / 64 retains 1/16 / 1/4 / 1/2 of the original blocks. Test inputs are evaluated after training.',size=11,anchor='middle')
    stem=out/'moving_block_errors'
    renderPDF.drawToFile(drawing,str(stem.with_suffix('.pdf')))
    renderPM.drawToFile(drawing,str(stem.with_suffix('.png')),fmt='PNG',dpi=72)
    return stem


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve()
    print(json.dumps(audit(out),indent=2));print(plot(out))
