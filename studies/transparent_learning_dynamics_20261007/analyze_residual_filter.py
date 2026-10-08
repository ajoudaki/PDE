"""Read-only analysis of the fixed 16-input integration-repair cohort."""
from pathlib import Path
from itertools import combinations
import csv
import hashlib
import json
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np

ROOT=Path('data/generated/transparent_learning_dynamics_20261007/residual_filter_v1')
OUT=ROOT/'analysis'


def path(kind,n,seed,h=.2,method='filtered',replicate=False):
    return ROOT/(f'{kind}_m16_n{n}_s{seed}_h{h}_{method}'+('_replicate' if replicate else ''))


def load(kind,n,seed,h=.2,method='filtered',replicate=False,keys=None):
    with np.load(path(kind,n,seed,h,method,replicate)/'trajectory.npz') as f:
        return {k:f[k] for k in (keys or ('f','loss','c1','c2','motion1','motion2','normalized_time'))}


def block(a,name):
    if name=='TT_offdiag':return a[...,:16,:16][...,~np.eye(16,dtype=bool)]
    a=a[...,:16,:16] if name=='TT' else a[...,:16,16:]
    return a.reshape(*a.shape[:-2],-1)


def rms(a):return np.sqrt(np.mean(np.asarray(a)**2,axis=-1))


def norms(a):return dict(max_entry=float(np.max(abs(a))),max_block_rms=float(np.max(rms(a))))


def first_stage(a,ratio):
    ix=np.flatnonzero(a['loss']/a['loss'][0]<=ratio)
    if not len(ix):return None
    k=int(ix[0]);previous=max(0,k-1)
    weight=1. if k==0 else float((a['loss'][previous]-ratio*a['loss'][0])/(a['loss'][previous]-a['loss'][k]))
    return {key:values[previous]*(1-weight)+values[k]*weight for key,values in a.items()}


def ensemble(runs,stride=1):
    return {k:np.mean([r[k][::stride] for r in runs],axis=0) for k in runs[0]}


def at_time(a,time):
    k=int(np.searchsorted(a['normalized_time'],time))
    previous=max(0,k-1)
    weight=1. if k==0 else float((time-a['normalized_time'][previous])/(a['normalized_time'][k]-a['normalized_time'][previous]))
    return {key:values[previous]*(1-weight)+values[k]*weight for key,values in a.items()}


def accuracy():
    dense=[load('dense',1024,s) for s in (101,202,303)]
    small=[load('dense',512,s) for s in (101,202,303)]
    flow=[load('dense',1024,s,.025,'rk4') for s in (101,202,303)]
    causal=[load('causal',256,s) for s in (1701,1702,1703)]
    large=load('causal',512,1701)
    rows=[];curves={'normalized_time':causal[0]['normalized_time']}
    for layer in (1,2):
        key=f'c{layer}'
        for name in ('TT','TT_offdiag','TP'):
            cc=np.array([block(r[key],name) for r in causal]);dd=np.array([block(r[key],name) for r in dense])
            ss=np.array([block(r[key],name) for r in small]);rr=np.array([block(r[key][::8],name) for r in flow])
            ll=block(large[key],name)
            row=dict(layer=layer,block=name)
            for kind in ('absolute','change'):
                c,d,s,r,l=(cc,dd,ss,rr,ll) if kind=='absolute' else (cc-cc[:,:1],dd-dd[:,:1],ss-ss[:,:1],rr-rr[:,:1],ll-ll[:1])
                diff=c.mean(0)-d.mean(0);flowdiff=c.mean(0)-r.mean(0)
                uncertainty=3*np.sqrt(c.var(0,ddof=1)/3+d.var(0,ddof=1)/3)+abs(l-c[0])+abs(s.mean(0)-d.mean(0))
                excess=abs(diff)-uncertainty
                threshold=min(.005,.2*np.max(abs(dd.mean(0)-dd.mean(0)[:1])))
                flags=excess[1:]>threshold
                sustained=bool(np.any(flags[:-2]&flags[1:-1]&flags[2:]))
                pair=[norms(d[a]-d[b]) for a,b in combinations(range(3),2)]
                row[kind]=dict(same_integrator=norms(diff),against_dense_flow=norms(flowdiff),
                    dense_time_bias=norms(d.mean(0)-r.mean(0)),
                    pairwise_dense_mean_max_rms=float(np.mean([x['max_block_rms'] for x in pair])),
                    particle_change=norms(l-c[0]),width_change=norms(s.mean(0)-d.mean(0)),
                    envelope_max=float(uncertainty.max()),envelope_excess_max=float(max(0,excess.max())),
                    sustained_envelope_excess=sustained)
                curves[f'l{layer}_{name}_{kind}_same_error_rms']=rms(diff)
                curves[f'l{layer}_{name}_{kind}_flow_error_rms']=rms(flowdiff)
            dc=dd.mean(0)-dd.mean(0)[:1];rc=rr.mean(0)-rr.mean(0)[:1]
            row['dense_filtered_change']=norms(dc);row['dense_flow_change']=norms(rc)
            row['relative_same_error']=row['change']['same_integrator']['max_block_rms']/norms(dc)['max_block_rms']
            row['relative_flow_error']=row['change']['against_dense_flow']['max_block_rms']/norms(rc)['max_block_rms']
            curves[f'l{layer}_{name}_causal_change_rms']=rms(cc.mean(0)-cc.mean(0)[:1])
            curves[f'l{layer}_{name}_dense_filtered_change_rms']=rms(dc)
            curves[f'l{layer}_{name}_dense_flow_change_rms']=rms(rc)
            rows.append(row)
    stages=[];motion=[]
    means={name:ensemble(runs) for name,runs in (('causal',causal),('dense_filtered',dense),('dense_flow',flow))}
    for ratio in (.8,.5,.2,.1,.01):
        values={name:first_stage(a,ratio) for name,a in means.items()}
        for method in means:
            for layer in (1,2):
                for panel,sl in (('training',slice(0,16)),('passive',slice(16,None))):
                    motion.append(dict(method=method,loss_ratio=ratio,layer=layer,panel=panel,
                        rms_displacement=float(np.sqrt(max(0,np.mean(values[method][f'motion{layer}'][sl]))))))
        for layer in (1,2):
            for name in ('TT_offdiag','TP'):
                target=block(values['dense_flow'][f'c{layer}']-means['dense_flow'][f'c{layer}'][0],name)
                item=dict(loss_ratio=ratio,layer=layer,block=name,dense_flow_change_rms=float(rms(target)),
                          reference_normalized_time=float(values['dense_flow']['normalized_time']))
                for method in ('causal','dense_filtered'):
                    observed=block(values[method][f'c{layer}']-means[method][f'c{layer}'][0],name)
                    item[method]=dict(error_rms=float(rms(observed-target)),
                        relative_error=float(np.linalg.norm(observed-target)/np.linalg.norm(target)),
                        cosine=float(observed@target/(np.linalg.norm(observed)*np.linalg.norm(target))),
                        normalized_time=float(values[method]['normalized_time']))
                stages.append(item)
    return rows,curves,stages,motion


def numerics():
    fine=load('dense',512,101,.0125,'rk4')
    coarse=load('dense',512,101,.025,'rk4')
    refinement={k:float(np.max(abs(coarse[k]-fine[k][::2]))) for k in ('f','c1','c2')}
    dense_rows=[]
    for h in (.4,.2,.1,.05):
        a=load('dense',512,101,h);stride=round(h/.0125)
        row=dict(step=h,output_bias=float(np.max(abs(a['f']-fine['f'][::stride]))),blocks=[],matched_loss=[])
        for layer in (1,2):
            key=f'c{layer}'
            for name in ('TT','TP'):
                ref=block(fine[key][::stride],name)
                bias=norms(block(a[key],name)-ref);change=norms(ref-ref[:1])
                row['blocks'].append(dict(layer=layer,block=name,bias=bias,
                    reference_change=change,
                    flow_accuracy_gate=bias['max_entry']<=max(1e-5,.01*change['max_entry'])))
        for ratio in (.5,.2,.01):
            x=first_stage(a,ratio);r=first_stage(fine,ratio)
            same_time=at_time(a,r['normalized_time'])
            for layer in (1,2):
                for name in ('TT_offdiag','TP'):
                    row['matched_loss'].append(dict(loss_ratio=ratio,layer=layer,block=name,
                        error_rms=float(rms(block(x[f'c{layer}']-r[f'c{layer}'],name))),
                        equal_time_at_reference_crossing_error_rms=float(rms(block(same_time[f'c{layer}']-r[f'c{layer}'],name))),
                        filtered_time=float(x['normalized_time']),reference_time=float(r['normalized_time'])))
        dense_rows.append(row)
    a=load('causal',128,1701,.2);b=load('causal',128,1701,.1)
    causal_rows=[]
    for layer in (1,2):
        for name in ('TT','TP'):
            ref=block(b[f'c{layer}'][::2],name)
            difference=norms(block(a[f'c{layer}'],name)-ref)
            causal_rows.append(dict(layer=layer,block=name,step_change=difference,
                refinement_gate=difference['max_entry']<=max(1e-5,.01*float(np.max(abs(ref-ref[:1]))))))
    reproduction={}
    with np.load(path('causal',256,1701)/'trajectory.npz') as original, np.load(path('causal',256,1701,replicate=True)/'trajectory.npz') as replica:
        assert original.files==replica.files
        for key in original.files:reproduction[key]=float(np.max(abs(original[key]-replica[key])))
    return dict(dense_rk4_refinement=refinement,dense_filtered=dense_rows,
                causal_step=causal_rows,reproduction=reproduction)


def memory_identity():
    a=load('causal',256,1701,keys=('f','C2','write_deficit','c'))
    rebuilt=np.zeros_like(a['f']);incorrect_raw=np.zeros_like(a['f'])
    for k in range(len(rebuilt)):
        rebuilt[k]=.2*np.einsum('jab,jb->a',a['C2'][k,:k,:,:16],a['write_deficit'][:k])
        incorrect_raw[k]=.2*np.einsum('jab,jb->a',a['C2'][k,:k,:,:16],a['c'][:k])
    return dict(reconstruction_error=float(np.max(abs(rebuilt-a['f']))),
                incorrect_raw_deficit_reconstruction_error=float(np.max(abs(incorrect_raw-a['f']))),
                maximum_raw_filtered_difference=float(np.max(abs(a['c']-a['write_deficit']))))


def figure(curves):
    from PIL import Image,ImageDraw,ImageFont
    im=Image.new('RGB',(1320,890),'white');draw=ImageDraw.Draw(im)
    fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    font=ImageFont.truetype(fontfile,18);small=ImageFont.truetype(fontfile,14)
    title=ImageFont.truetype(fontfile,24)
    draw.text((30,15),'16 interacting inputs: integration repair, same causal system',font=title,fill='black')
    draw.text((30,52),'Three-draw means; dense width 1024, causal particles 256. Four passive inputs. Normalized time 2t/m.',font=font,fill='black')
    colors={'TT':(27,105,176),'TP':(196,80,43)}
    for row in range(2):
        for column,layer in enumerate((1,2)):
            left=80+column*640;top=145+row*345;width=525;height=235
            if row==0:
                suffixes=('causal_change_rms','dense_filtered_change_rms','dense_flow_change_rms')
                heading=f'Layer {layer}: Gram-change magnitude'
            else:
                suffixes=('change_same_error_rms','change_flow_error_rms')
                heading=f'Layer {layer}: actual matrix-discrepancy RMS'
            maximum=max(float(curves[f'l{layer}_{block}_{suffix}'].max()) for block in ('TT','TP') for suffix in suffixes)*1.08
            draw.text((left,top-32),heading,font=font,fill='black')
            draw.line((left,top,left,top+height,left+width,top+height),fill='black')
            for j in range(5):
                y=top+height*(1-j/4)
                draw.line((left,y,left+width,y),fill=(225,225,225))
                draw.text((left-58,y-8),f'{maximum*j/4:.3f}',font=small,fill='black')
            for block in ('TT','TP'):
                for style,suffix in enumerate(suffixes):
                    values=curves[f'l{layer}_{block}_{suffix}']
                    points=[(left+i*width/(len(values)-1),top+height*(1-float(v)/maximum)) for i,v in enumerate(values)]
                    if style==0:draw.line(points,fill=colors[block],width=3)
                    elif style==1:
                        for i in range(0,len(points)-1,3):draw.line(points[i:i+2],fill=colors[block],width=2)
                    else:
                        for x,y in points[::3]:draw.ellipse((x-1.7,y-1.7,x+1.7,y+1.7),fill=colors[block])
            for value in (0,9.6,19.2):draw.text((left+value/19.2*width-12,top+height+8),str(value),font=small,fill='black')
    draw.text((40,798),'Blue: training-training. Orange: training-passive. Top: solid causal, dashed dense filtered, dotted dense RK4.',font=font,fill='black')
    draw.text((40,828),'Bottom: solid comparison on the same filtered mesh; dashed comparison against refined dense RK4.',font=font,fill='black')
    im.save(OUT/'integration_repair.png')


def main():
    records=[json.loads(p.read_text()) for p in sorted(ROOT.glob('*/record.json'))]
    assert len(records)==24 and all(r['exit_status']==0 for r in records)
    rows,curves,stages,motion=accuracy();OUT.mkdir(exist_ok=True)
    meta=dict(count=len(records),wall_seconds=sum(r['wall_seconds'] for r in records),
              peak_mib=max(r['peak_rss_kib'] for r in records)/1024,
              unstable_count=sum(r['numerically_unstable'] for r in records),
              maximum_relative_loss_increase=max(r['maximum_relative_loss_increase'] for r in records))
    sourcehash={}
    for r in records:
        for k,v in r['source_sha256'].items():
            assert sourcehash.get(k,v)==v;sourcehash[k]=v
    meta['source_sha256']=sourcehash
    summary=dict(metadata=meta,accuracy=rows,numerics=numerics(),matched_loss_diagnostic=stages,
        matched_loss_motion=motion,
        memory_identity=memory_identity(),analysis_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    np.savez_compressed(OUT/'curves.npz',**curves)
    with (OUT/'curves.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(curves);writer.writerows(zip(*curves.values()))
    figure(curves)
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
