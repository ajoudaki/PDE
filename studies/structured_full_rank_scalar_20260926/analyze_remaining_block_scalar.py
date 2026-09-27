"""Audit remaining-task checkpoints and combine all twelve tasks without new fits."""
import block_scalar_closure as scalar
import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, Rect, Circle
from reportlab.lib.colors import HexColor
from circle_tasks import BY_NAME
from plot_block_continuation import text, line, axis_top, INK, GRID
from run_block_scalar_closure import digest, write, rms, COUNTS

TASKS = ('pair_cos1', 'pair_cos3', 'near_pair_sin9', 'triple_cos3', 'triple_mixed',
         'cluster_triple_cos9', 'broad_ridge6', 'sharp_ridge8', 'alternating3',
         'alternating5', 'alternating9', 'multiscale12')
BLUE = HexColor('#2563eb')
ORANGE = HexColor('#d95f02')


def audit(directory):
    manifest = json.loads((directory/'manifest.json').read_text())
    source = Path(__file__).resolve().parent
    for name, h in manifest['sources'].items():
        assert digest(source/name) == h == digest(directory/'source_snapshot'/name)
    rows = json.loads((directory/'results.json').read_text())
    comparisons = json.loads((directory/'comparisons.json').read_text())
    selection = json.loads((directory/'selection.json').read_text())
    pool = scalar.initial_pool(2048, 16, 1)
    predictions = {}
    maximum_forward = maximum_mse = maximum_metric = 0.
    for row in rows:
        path = directory/row['data_file']
        assert digest(path) == row['data_sha256']
        assert row['min_clock'] >= 1 and row['total_seconds'] < 60
        if row['fitted']:
            assert row['train_mse'] <= .01*(1+1e-7)
        u, labels = BY_NAME[row['task']].data()
        with np.load(path) as data:
            layout, G, initial = scalar.initialize(pool, data['indices'], u, row['order'])
            assert np.array_equal(initial, data['initial_vector']) and np.array_equal(G, data['G'])
            assert np.all(np.isfinite(data['vector']))
            assert row['dynamic_scalars'] == layout.size and row['static_G_scalars'] == G.size
            predicted = scalar.predict(layout, data['G'], data['vector'], data['angles'])
            train = scalar.forward(layout, data['G'], data['vector'], u)[0]
            maximum_forward = max(maximum_forward, float(np.max(np.abs(predicted-data['prediction']))))
            maximum_mse = max(maximum_mse, abs(float(np.mean((train-labels)**2))-row['train_mse']))
            assert np.max(np.abs(train-data['train_prediction'])) < 1e-12
            if row['kind'] == 'representative':
                expected = np.random.default_rng(np.random.SeedSequence([1,row['subset_stream']])).permutation(128)[:row['q']]
                assert np.array_equal(expected, data['indices'])
            predictions[row['tag']] = data['prediction']
    assert maximum_forward < 1e-12 and maximum_mse < 1e-12
    baseline = Path(manifest['baseline'])
    dense = {}
    for name, h in manifest['baseline_data_hashes'].items():
        assert digest(baseline/name) == h
        with np.load(baseline/name) as data:
            dense[name] = data['prediction']
    row_by_tag = {r['tag']:r for r in rows}
    for comp in comparisons:
        row = row_by_tag[comp['tag']]
        reference = row_by_tag[selection['references'][comp['task']]]
        fitted_pair = row['fitted'] and reference['fitted']
        assert comp['fitted_pair'] == fitted_pair
        if fitted_pair:
            value = rms(predictions[row['tag']], predictions[reference['tag']])
            maximum_metric = max(maximum_metric, abs(value-comp['rms_vs_full_closure']))
        else:
            assert comp['rms_vs_full_closure'] is None
        for method in ('block16', 'gaussian'):
            key = 'rms_vs_dense_'+method
            if comp[key] is not None:
                value = rms(predictions[row['tag']], dense[f"{row['task']}__{method}.npz"])
                maximum_metric = max(maximum_metric, abs(value-comp[key]))
        error = predictions[row['tag']]-predictions[reference['tag']]
        change = abs(float(np.sqrt(np.mean(error**2)))-float(np.sqrt(np.mean(error[::2]**2))))
        assert abs(change-comp['quadrature_change']) < 1e-12
    assert maximum_metric < 1e-12
    assert max(r['quadrature_change'] for r in comparisons) <= 1e-4
    return {'directory':str(directory), 'saved_states_verified':len(rows),
        'fitted_runs':sum(r['fitted'] for r in rows), 'source_and_data_hashes_verified':True,
        'exact_initial_subsets_verified':True, 'restored_circle_max_difference':maximum_forward,
        'training_mse_max_difference':maximum_mse, 'metric_max_difference':maximum_metric,
        'max_quadrature_change':max(r['quadrature_change'] for r in comparisons)}


def plot(out, summaries, references, metric, stem):
    drawing = Drawing(1220, 1120)
    drawing.add(Rect(0,0,1220,1120,fillColor=HexColor('#ffffff'),strokeColor=None))
    title = ('Population compression: circle prediction error' if metric=='rms_vs_full_closure'
             else 'Total circle prediction error versus dense Gaussian')
    text(drawing,610,1086,title,size=22,anchor='middle')
    text(drawing,610,1062,'k = 16 | P = 8 | Reference width = 2048 | Stop MSE = 0.01 | Three subset draws',size=12,anchor='middle')
    for index, task in enumerate(TASKS):
        row, col = divmod(index,3)
        left, bottom, width, height = 66+col*402, 820-row*235, 309, 156
        text(drawing,left+width/2,bottom+height+31,task,size=13,anchor='middle')
        group = {r['q']:r[metric] for r in summaries if r['task']==task}
        if not any(group.values()):
            text(drawing,left+width/2,bottom+height/2,'No fitted reference available',size=12,anchor='middle')
            continue
        maximum = max(r['max'] for r in group.values() if r)
        ref = references[task]['rms_vs_dense_gaussian'] if metric=='rms_vs_dense_gaussian' else None
        if ref is not None:
            maximum = max(maximum, ref)
        step, count = axis_top(maximum)
        top = step*count
        xp = lambda q:left+width*(math.log2(q)-3)/3
        yp = lambda y:bottom+height*y/top
        for j in range(count+1):
            yy = yp(j*step)
            line(drawing,left,yy,left+width,yy,GRID,.7)
            text(drawing,left-8,yy-3,f'{j*step:.3g}',size=9,anchor='end')
        line(drawing,left,bottom,left,bottom+height,INK,.8)
        line(drawing,left,bottom,left+width,bottom,INK,.8)
        text(drawing,left,bottom+height+9,'Absolute RMS',size=9)
        points=[]
        for q in COUNTS:
            x=xp(q)
            text(drawing,x,bottom-17,str(q),size=10,anchor='middle')
            if group[q] is None:
                continue
            value=group[q]
            line(drawing,x,yp(value['min']),x,yp(value['max']),BLUE,1.1)
            for bound in ('min','max'):
                line(drawing,x-4,yp(value[bound]),x+4,yp(value[bound]),BLUE,1.1)
            points.append((x,yp(value['mean'])))
            drawing.add(Circle(x,yp(value['mean']),3.5,fillColor=BLUE,strokeColor=None))
        for a,b in zip(points,points[1:]):
            line(drawing,*a,*b,BLUE,2)
        if ref is not None:
            line(drawing,left,yp(ref),left+width,yp(ref),ORANGE,1.3,[4,4])
        text(drawing,left+width/2,bottom-35,'Representative blocks q (log2)',size=9,anchor='middle')
    text(drawing,610,61,'Dots: mean; bars: min-max over three subsets. Each panel has its own linear RMS scale.',size=11,anchor='middle')
    text(drawing,610,40,('All 12 tasks fitted by the block closure; dense Gaussian unavailable for alternating9.'
        if all(references[t]['fitted'] for t in TASKS) else 'Unfitted endpoints are excluded; see report for training losses.'),size=11,anchor='middle')
    if metric=='rms_vs_dense_gaussian':
        text(drawing,610,19,'Orange dashed line: full 128-block closure versus dense Gaussian.',size=11,anchor='middle')
    renderPDF.drawToFile(drawing,str(out/(stem+'.pdf')))
    renderPM.drawToFile(drawing,str(out/(stem+'.png')),fmt='PNG',dpi=72)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    out=args.output.resolve()
    manifest=json.loads((out/'manifest.json').read_text())
    previous=Path(manifest['previous'])
    assert digest(previous/'results.json')==manifest['previous_results_sha256']
    assert digest(previous/'refinement.json')==manifest['previous_refinement_sha256']
    assert json.loads((previous/'refinement.json').read_text())['passed']
    audits=[audit(path) for path in (previous,out)]
    rows=[]; summaries=[]; references={}
    for directory in (previous,out):
        batch=json.loads((directory/'results.json').read_text())
        rows += [{**r,'source_directory':str(directory)} for r in batch]
        summaries += json.loads((directory/'summary.json').read_text())
        refs=json.loads((directory/'selection.json').read_text())['references']
        references.update({t:next(r for r in batch if r['tag']==tag) for t,tag in refs.items()})
    assert len([r for r in rows if r['kind']=='representative'])==108
    write(out/'all_tasks_summary.json',summaries)
    write(out/'all_tasks_results.json',rows)
    plot(out,summaries,references,'rms_vs_full_closure','all_tasks_compression')
    plot(out,summaries,references,'rms_vs_dense_gaussian','all_tasks_gaussian')
    lines=['# Moving-block scalar closure: all twelve circle tasks','',
        'Nine remaining tasks tested at fixed k16, P8 and q8/32/64, with three nested subset draws.',
        'The original three tasks are reused unchanged. Full reference:128 blocks (width2048).',
        'Primary error is absolute RMS of the prediction difference on2048 circle points.',
        'Every fitted endpoint is its own first training-MSE0.01 crossing; no test points enter training.',
        '', '| Task | q8 vs full | q32 vs full | q64 vs full | q64 vs dense Gaussian | Fitted representative/reference pairs |',
        '|---|---:|---:|---:|---:|---|']
    csv_rows=[]
    increasing=[]; improving=[]; unresolved=[]; monotonic=[]
    for task in TASKS:
        group={r['q']:r for r in summaries if r['task']==task}
        fmt=lambda value:f"{value['mean']:.6f}" if value else 'unavailable'
        vals=[group[q]['rms_vs_full_closure'] for q in COUNTS]
        gauss=group[64]['rms_vs_dense_gaussian']
        counts='/'.join(str(group[q]['fitted_pairs']) for q in COUNTS)
        lines.append(f"| {task} | {' | '.join(fmt(v) for v in vals)} | {fmt(gauss)} | {counts} (each out of3) |")
        if all(vals) and all(group[q]['fitted_pairs']==3 for q in COUNTS):
            reduction=vals[0]['mean']-vals[-1]['mean']
            (improving if reduction>.001 else increasing if reduction<-.001 else unresolved).append(task)
            if vals[0]['mean']>=vals[1]['mean']>=vals[2]['mean']:
                monotonic.append(task)
        for q in COUNTS:
            r=group[q]
            csv_rows.append({'task':task,'q':q,'fitted_pairs':r['fitted_pairs'],
                **{metric+'_'+stat:(r[metric][stat] if r[metric] else '')
                   for metric in ('rms_vs_full_closure','rms_vs_dense_block16','rms_vs_dense_gaussian')
                   for stat in ('mean','min','max')}})
    lines += ['', 'Values are means over fitted subset draws; CSV gives all ranges.',
        f'q8-to-q64 improvement>0.001: {improving}.',f'q8-to-q64 increase>0.001: {increasing}.',
        f'Changes below0.001: {unresolved}.',f'Monotone mean compression curves: {len(monotonic)}/12 ({monotonic}).',
        '', '| Task | Reference MSE | Full closure vs dense block16 | Full closure vs Gaussian |',
        '|---|---:|---:|---:|']
    for task in TASKS:
        r=references[task]
        fmt=lambda x:f'{x:.8g}' if x is not None else 'unavailable'
        lines.append(f"| {task} | {r['train_mse']:.8g} | {fmt(r['rms_vs_dense_block16'])} | {fmt(r['rms_vs_dense_gaussian'])} |")
    partial=[r for r in rows if not r['fitted']]
    lines+=['','Unfitted new endpoints (excluded from matched-loss comparisons):']
    lines += [f"- {r['tag']}: MSE={r['train_mse']:.8g}, stop={r['stop_reason']}, seconds={r['total_seconds']:.3f}." for r in partial] or ['None.']
    completion=json.loads((out/'completion.json').read_text())
    lines+=['',f'New campaign: `{json.dumps(completion)}`',
        '', 'The saved dense Gaussian and dense block16 alternating9 runs were unfinished, so their fitted-function metrics are unavailable.',
        'q8/q32/q64 reduce population state and block storage by approximately16x/4x/2x. '
        'The finite reference has128 blocks, so these tests do not establish an infinite-population rate. '
        'Three subset draws share one initial population and are not three independent network initializations.',
        'No new solver refinement was run; the unchanged solver/core retain the previous clustered-task refinement check '
        '(circle RMS1.49e-7 at10x tighter tolerances). New-task saved predictions, initialization and errors are independently recomputed.',
        'No training trajectory guarantee follows from comparing separately stopped fitted endpoints.',
        '', '![Population compression](all_tasks_compression.png)',
        '', '![Total Gaussian discrepancy](all_tasks_gaussian.png)']
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    with (out/'all_tasks_summary.csv').open('w') as file:
        writer=csv.DictWriter(file,fieldnames=list(csv_rows[0]))
        writer.writeheader();writer.writerows(csv_rows)
    write(out/'audit.json', {'campaigns':audits, 'analysis_source_sha256':digest(__file__),
        'figure_hashes':{name:digest(out/name) for name in ('all_tasks_compression.png','all_tasks_gaussian.png')},
        'monotone_mean_tasks':monotonic, 'improvement_over_001_tasks':improving,
        'increase_over_001_tasks':increasing, 'below_001_tasks':unresolved})
    print((out/'report.md').read_text())


if __name__=='__main__':
    main()
