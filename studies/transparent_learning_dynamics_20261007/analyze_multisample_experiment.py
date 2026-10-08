"""Predeclared blockwise analysis, no new trajectories or fitted predictors."""
from pathlib import Path
from itertools import combinations
import csv
import hashlib
import json
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np

ROOT = Path('data/generated/transparent_learning_dynamics_20261007/multisample_v1')
OUT = ROOT / 'analysis'


def path(kind, m, n, seed, h=.4, method='euler', mode='full'):
    return ROOT / f'{kind}_m{m}_n{n}_s{seed}_h{h}_{method}_{mode}'


def load(kind, m, n, seed, h=.4, method='euler', mode='full', keys=None):
    with np.load(path(kind, m, n, seed, h, method, mode) / 'trajectory.npz') as f:
        return {k: f[k] for k in (keys or ('time', 'normalized_time', 'f', 'loss', 'c1', 'c2', 'motion1', 'motion2'))}


def rms(a):
    return np.sqrt(np.mean(np.asarray(a)**2, axis=-1))


def block(a, m, name):
    if name == 'TT_offdiag':
        return a[..., :m, :m][..., ~np.eye(m, dtype=bool)]
    a = a[..., :m, :m] if name == 'TT' else a[..., :m, m:]
    return a.reshape(*a.shape[:-2], -1)


def norms(a):
    return dict(max_entry=float(np.max(abs(a))), max_block_rms=float(np.max(rms(a))))


def sustained(a):
    # Same individual entry must exceed the threshold at three consecutive
    # nonzero saved times; not three unrelated maxima or only one endpoint.
    a = a[1:]
    return bool(np.any(a[:-2] & a[1:-1] & a[2:]))


def accuracy():
    rows, curves = [], {}
    for m in (4, 8, 16):
        dense = [load('dense', m, 1024, s) for s in (101, 202, 303)]
        small = [load('dense', m, 512, s) for s in (101, 202, 303)]
        causal = [load('causal', m, 512, s) for s in (1701, 1702, 1703)]
        large = load('causal', m, 1024, 1701)
        c256 = load('causal', m, 256, 1701)
        c256fine = load('causal', m, 256, 1701, .2)
        for layer in (1, 2):
            for name in ('TT', 'TP'):
                key = f'c{layer}'
                db = np.array([block(d[key], m, name) for d in dense])
                sb = np.array([block(d[key], m, name) for d in small])
                cb = np.array([block(d[key], m, name) for d in causal])
                lb = block(large[key], m, name)
                timestep = block(c256fine[key][::2] - c256[key], m, name)
                row = dict(m=m, layer=layer, block=name)
                for kind in ('absolute', 'change'):
                    dd = db if kind == 'absolute' else db - db[:, :1]
                    ss = sb if kind == 'absolute' else sb - sb[:, :1]
                    cc = cb if kind == 'absolute' else cb - cb[:, :1]
                    ll = lb if kind == 'absolute' else lb - lb[:1]
                    diff = cc.mean(0) - dd.mean(0)
                    se = np.sqrt(dd.var(0, ddof=1)/3 + cc.var(0, ddof=1)/3)
                    particle = abs(ll - cc[0])
                    width = abs(ss.mean(0) - dd.mean(0))
                    envelope = 3*se + particle + width
                    excess = abs(diff) - envelope
                    drift = db.mean(0) - db.mean(0)[:1]
                    drift_max = np.max(abs(drift))
                    pair = [norms(dd[a]-dd[b]) for a, b in combinations(range(3), 2)]
                    row[kind] = dict(**norms(diff),
                        pairwise_dense_mean_max_entry=float(np.mean([v['max_entry'] for v in pair])),
                        pairwise_dense_mean_max_block_rms=float(np.mean([v['max_block_rms'] for v in pair])),
                        envelope_max=float(envelope.max()), excess_max=float(max(0, excess.max())),
                        excess_sustained_absolute=sustained(excess > .005),
                        excess_sustained_relative=sustained(excess > .2*drift_max),
                        particle_change=norms(particle), width_change=norms(width))
                    prefix = f'm{m}_l{layer}_{name}_{kind}'
                    curves[prefix+'_error_entry'] = np.max(abs(diff), axis=-1)
                    curves[prefix+'_error_rms'] = rms(diff)
                    curves[prefix+'_dense_variability_rms'] = np.mean([rms(dd[a]-dd[b]) for a,b in combinations(range(3),2)], axis=0)
                    curves[prefix+'_envelope_entry'] = envelope.max(-1)
                row['dense_change'] = norms(drift)
                row['causal_step_change'] = norms(timestep)
                row['relative_change_rms'] = row['change']['max_block_rms']/row['dense_change']['max_block_rms']
                row['relative_change_entry'] = row['change']['max_entry']/row['dense_change']['max_entry']
                curves[f'm{m}_l{layer}_{name}_dense_change_rms'] = rms(drift)
                curves[f'm{m}_l{layer}_{name}_causal_change_rms'] = rms(cb.mean(0)-cb.mean(0)[:1])
                rows.append(row)
    curves['normalized_time'] = dense[0]['normalized_time']
    return rows, curves


def numerics():
    rows = []
    for m in (4, 8, 16):
        fine = load('dense', m, 512, 101, .05, 'rk4', keys=('f','c1','c2','loss','kernel_blocks','normalized_time'))
        coarse = load('dense', m, 512, 101, .1, 'rk4')
        euler = load('dense', m, 512, 101)
        row = dict(m=m, rk4_refinement={}, euler_bias={}, blockwise=[])
        for k in ('f', 'c1', 'c2'):
            row['rk4_refinement'][k] = float(np.max(abs(fine[k][::2]-coarse[k])))
            row['euler_bias'][k] = float(np.max(abs(fine[k][::8]-euler[k])))
        for layer in (1,2):
            k=f'c{layer}'
            for name in ('TT','TP'):
                ref=block(fine[k],m,name)
                bias=block(euler[k]-fine[k][::8],m,name)
                difference=block(coarse[k]-fine[k][::2],m,name)
                drift=norms(ref-ref[:1])
                error=norms(difference)
                row['blockwise'].append(dict(layer=layer,block=name,refinement=error,euler_bias=norms(bias),
                    fine_change=drift,refinement_pass=error['max_entry']<=max(1e-5,.01*drift['max_entry'])))
        row['output_refinement_pass']=row['rk4_refinement']['f']<=max(1e-5,.01*float(np.max(abs(fine['f']))))
        row['all_refinement_pass']=row['output_refinement_pass'] and all(r['refinement_pass'] for r in row['blockwise'])
        eig=np.linalg.eigvalsh(fine['kernel_blocks'].sum(1)[:,:m,:m])[:,-1]
        row['kernel_max_eigen_initial']=float(eig[0]);row['kernel_max_eigen_max']=float(eig.max())
        row['fine_final_relative_loss']=float(fine['loss'][-1]/fine['loss'][0])
        row['coarse_final_relative_loss']=float(coarse['loss'][-1]/coarse['loss'][0])
        rows.append(row)
    return rows


def directional_predictions():
    rows=[]
    for m in (4,8,16):
        a=load('dense',m,512,101,.05,'rk4',keys=('time','loss','c1','c2','initial_curvature'))
        for ratio in (.8,.5,.2):
            k=int(np.flatnonzero(a['loss']/a['loss'][0]<=ratio)[0])
            for layer in (1,2):
                for name in ('TT','TT_offdiag','TP'):
                    observed=block(a[f'c{layer}'][k]-a[f'c{layer}'][0],m,name)
                    predicted=block(.5*a['time'][k]**2*a['initial_curvature'][layer-1],m,name)
                    rows.append(dict(m=m,layer=layer,block=name,target_loss_ratio=ratio,
                        time=float(a['time'][k]),actual_loss_ratio=float(a['loss'][k]/a['loss'][0]),
                        cosine=float(observed@predicted/(np.linalg.norm(observed)*np.linalg.norm(predicted))),
                        predicted_to_actual_norm=float(np.linalg.norm(predicted)/np.linalg.norm(observed)),
                        relative_prediction_error=float(np.linalg.norm(observed-predicted)/np.linalg.norm(observed))))
    return rows


def controls():
    rows=[]
    for kind,modes,seeds in (('dense',('frozen_middle','affine_gates'),(101,202)),
                             ('causal',('no_middle','no_reciprocal'),(1701,1702))):
        for mode in modes:
            for seed in seeds:
                full=load(kind,8,512,seed);control=load(kind,8,512,seed,mode=mode)
                row=dict(kind=kind,mode=mode,seed=seed,
                    full_final_relative_loss=float(full['loss'][-1]/full['loss'][0]),
                    control_final_relative_loss=float(control['loss'][-1]/control['loss'][0]),
                    passive_output_sup_per_input=np.max(abs(full['f'][:,8:]-control['f'][:,8:]),axis=0).tolist(),
                    passive_output_final_difference=(control['f'][-1,8:]-full['f'][-1,8:]).tolist(),blocks=[],motion=[])
                fine=load(kind,8,512,seed,.2,mode=mode) if kind=='dense' and seed==101 else None
                for layer in (1,2):
                    key=f'c{layer}'
                    for name in ('TT','TP'):
                        diff=block((control[key]-control[key][:1])-(full[key]-full[key][:1]),8,name)
                        item=dict(layer=layer,block=name,change_contrast=norms(diff))
                        if fine is not None:
                            item['control_refinement']=norms(block(fine[key][::2]-control[key],8,name))
                        row['blocks'].append(item)
                for ratio in (.1,.01,None):
                    indexes=[]
                    for a in (full,control):
                        if ratio is None:indexes.append(-1)
                        else:
                            ix=np.flatnonzero(a['loss']/a['loss'][0]<=ratio)
                            indexes.append(int(ix[0]) if len(ix) else None)
                    for layer in (1,2):
                        for name,sl in (('training',slice(0,8)),('passive',slice(8,None))):
                            values=[]
                            for a,i in zip((full,control),indexes):
                                values.append(None if i is None else float(np.sqrt(max(0,np.mean(a[f'motion{layer}'][i,sl])))))
                            row['motion'].append(dict(layer=layer,panel=name,loss_ratio=ratio,full=values[0],control=values[1]))
                if fine is not None:row['control_refinement_passive_output']=float(np.max(abs(fine['f'][::2,8:]-control['f'][:,8:])))
                rows.append(row)
    return rows


def readout_memory():
    rows=[]
    for m in (4,8,16):
        a=load('causal',m,512,1701,keys=('C2','c','f','loss','time'))
        history=a.pop('C2')
        rebuilt=np.zeros_like(a['f'])
        for k in range(1,len(rebuilt)):
            rebuilt[k]=.4*np.einsum('jab,jb->a',history[k,:k,:,:m],a['c'][:k])
        k=len(rebuilt)-1
        half=(k+1)//2
        old=.4*np.einsum('jab,jb->a',history[k,:half,:,:m],a['c'][:half])
        recent=rebuilt[-1]-old
        rows.append(dict(m=m,reconstruction_max=float(np.max(abs(rebuilt-a['f']))),
            final_passive=a['f'][-1,m:].tolist(),first_half_writes_at_final=old[m:].tolist(),
            second_half_writes_at_final=recent[m:].tolist()))
    return rows


def metadata():
    records=[json.loads(p.read_text()) for p in sorted(ROOT.glob('*/record.json'))]
    assert len(records)==52 and all(r['exit_status']==0 for r in records)
    allowed={'dense':{'full','frozen_middle','affine_gates'},'causal':{'full','no_middle','no_reciprocal'}}
    assert all(r['config']['mode'] in allowed[r['config']['kind']] for r in records)
    hashes={}
    for r in records:
        for key,value in r['source_sha256'].items():
            assert hashes.get(key,value)==value
            hashes[key]=value
    diag=[]
    for r in records:
        for key,value in r['diagnostics'].items():
            if isinstance(value,dict) and 'maximum_covariance_error' in value:
                diag.append(dict(config=r['config'],family=key,
                    covariance_error=value['maximum_covariance_error'],
                    discarded_variance=value['maximum_discarded_variance']))
    return dict(counts={kind:sum(r['config']['kind']==kind for r in records) for kind in allowed},
        wall_seconds=sum(r['wall_seconds'] for r in records),
        peak_mib=max(r['peak_rss_kib'] for r in records)/1024,
        source_sha256=hashes,covariance_diagnostics=diag)


def figure(curves, errors=False):
    # Static scientific figure, no interactive dependency or fitted data.
    from PIL import Image,ImageDraw,ImageFont
    im=Image.new('RGB',(1600,940),'white');draw=ImageDraw.Draw(im)
    fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    font=ImageFont.truetype(fontfile,17);small=ImageFont.truetype(fontfile,14)
    title=ImageFont.truetype(fontfile,23)
    heading='Feature-change errors versus dense variability' if errors else 'Feature-similarity changes throughout learning: same Euler mesh'
    draw.text((35,14),heading,fill='black',font=title)
    subtitle='Solid: error between ensemble means. Dashed: mean pairwise dense difference. These are different statistics.' if errors else 'Dense n=1024 (3 draws), causal N=512 (3 draws). Block RMS from initialization; uncentered Grams.'
    draw.text((35,47),subtitle,fill='black',font=font)
    colors={'TT':(23,103,175),'TP':(195,76,38)}
    for col,m in enumerate((4,8,16)):
        for row,layer in enumerate((1,2)):
            left=75+col*520;top=145+row*350;width=435;height=245
            keys=[f'm{m}_l{layer}_{block}_change_{kind}' for block in ('TT','TP') for kind in ('error_rms','dense_variability_rms')] if errors else [f'm{m}_l{layer}_{block}_{kind}_change_rms' for block in ('TT','TP') for kind in ('dense','causal')]
            ymax=max(float(curves[k].max()) for k in keys)*1.08
            draw.text((left,top-43),f'm={m}, hidden layer {layer}',font=font,fill='black')
            if m==16:draw.text((left,top-23),'NOT a controlled continuous-flow comparison',font=small,fill=(170,20,20))
            draw.line((left,top,left,top+height,left+width,top+height),fill='black',width=1)
            for j in range(5):
                y=top+height-j*height/4
                draw.line((left,y,left+width,y),fill=(225,225,225),width=1)
                draw.text((left-54,y-9),f'{j*ymax/4:.3f}',font=small,fill='black')
            for block in ('TT','TP'):
                for kind in ('dense','causal'):
                    if errors:
                        suffix='error_rms' if kind=='dense' else 'dense_variability_rms'
                        values=curves[f'm{m}_l{layer}_{block}_change_{suffix}']
                    else:values=curves[f'm{m}_l{layer}_{block}_{kind}_change_rms']
                    pts=[(left+i*width/(len(values)-1),top+height-height*float(v)/ymax) for i,v in enumerate(values)]
                    if kind=='dense':draw.line(pts,fill=colors[block],width=3)
                    else:
                        for i in range(0,len(pts)-1,2):draw.line(pts[i:i+2],fill=colors[block],width=3)
            for val in (0,9.6,19.2):draw.text((left+val/19.2*width-12,top+height+8),str(val),font=small,fill='black')
    legend='Blue: training-training. Orange: training-passive. Solid: mean error. Dashed: dense variability.' if errors else 'Blue: training-training. Orange: training-passive. Solid: dense. Dashed: causal.'
    draw.text((70,853),legend,font=font,fill='black')
    footer='Horizontal axis: normalized time 2t/m. Vertical axis: block RMS of Gram-change differences; same Euler mesh.' if errors else 'Horizontal axis: normalized time 2t/m. Curves show movement size, not entrywise accuracy; see blockwise table.'
    draw.text((70,883),footer,font=font,fill='black')
    im.save(OUT/('feature_trajectory_errors.png' if errors else 'feature_trajectory_changes.png'))


def main():
    OUT.mkdir(exist_ok=True)
    rows,curves=accuracy()
    summary=dict(metadata=metadata(),accuracy=rows,numerics=numerics(),
        initial_direction=directional_predictions(),controls=controls(),readout_memory=readout_memory(),
        analysis_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    np.savez_compressed(OUT/'accuracy_curves.npz',**curves)
    flat=[]
    for r in rows:
        flat.append(dict(m=r['m'],layer=r['layer'],block=r['block'],
            dense_drift_rms=r['dense_change']['max_block_rms'],
            change_error_rms=r['change']['max_block_rms'],
            relative_change_rms=r['relative_change_rms'],
            change_error_entry=r['change']['max_entry'],
            absolute_error_entry=r['absolute']['max_entry'],
            dense_pair_change_rms=r['change']['pairwise_dense_mean_max_block_rms'],
            dense_pair_absolute_entry=r['absolute']['pairwise_dense_mean_max_entry']))
    with (OUT/'blockwise_accuracy.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(flat[0]));writer.writeheader();writer.writerows(flat)
    with (OUT/'accuracy_curves.csv').open('w',newline='') as f:
        writer=csv.writer(f);keys=['normalized_time']+[k for k in curves if k!='normalized_time']
        writer.writerow(keys);writer.writerows(zip(*(curves[k] for k in keys)))
    figure(curves)
    figure(curves, errors=True)
    print(json.dumps(dict(metadata={k:v for k,v in summary['metadata'].items() if k!='covariance_diagnostics'},
                          accuracy=flat,numerics=summary['numerics'],readout_memory=summary['readout_memory']),indent=2))


if __name__=='__main__':main()
