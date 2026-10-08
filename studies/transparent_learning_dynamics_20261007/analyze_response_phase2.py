"""Predeclared unequal-residual cohorts; descriptive diagnostics, not CIs."""
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT=Path('data/generated/transparent_learning_dynamics_20261007/unequal_residuals_v1')


def load(name):
    with np.load(ROOT/name/'trajectory.npz') as data:
        return {k:data[k] for k in data.files}


def mean_sem(runs,key):
    values=np.array([r[key] for r in runs])
    return values.mean(0),values.std(0,ddof=1)/np.sqrt(len(values))


def endpoint(runs,key):
    avg,sem=mean_sem(runs,key)
    return dict(mean=avg[-1].tolist(),sem=sem[-1].tolist())


def compare_curve(a,b,key):
    stride=round((a['time'][1]-a['time'][0])/(b['time'][1]-b['time'][0]))
    return float(np.max(abs(a[key]-b[key][::stride])))


def observables(r):
    return np.column_stack([r['f'],(r['c1']-r['c1'][0]).reshape(len(r['time']),-1),
                            (r['c2']-r['c2'][0]).reshape(len(r['time']),-1),r['area']])


def plot(curves,dest):
    from PIL import Image,ImageDraw,ImageFont
    img=Image.new('RGB',(1500,1030),'white');draw=ImageDraw.Draw(img)
    fp='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    normal=ImageFont.truetype(fp,20);small=ImageFont.truetype(fp,17)
    title=ImageFont.truetype(fp,27)
    draw.text((45,15),'Unequal residuals: dense comparison and passive mechanisms',fill='black',font=title)
    panels=[(55,100,725,495),(815,100,1480,495),(55,595,725,990),(815,595,1480,990)]
    for (x0,y0,x1,y1),panel in zip(panels,curves):
        draw.text((x0,y0-40),panel['title'],fill='black',font=normal)
        allvalues=np.concatenate([np.asarray(a[2]) for a in panel['series']])
        lo,hi=min(0.,float(allvalues.min())),float(allvalues.max())
        margin=.06*(hi-lo or 1);lo-=margin;hi+=margin
        left,right,top,bottom=x0+65,x1-15,y0+10,y1-75
        def point(t,z):return (left+t/24*(right-left),bottom-(z-lo)/(hi-lo)*(bottom-top))
        for t in (0,6,12,18,24):
            x,_=point(t,0);draw.line((x,top,x,bottom),fill='#eeeeee')
            draw.text((x-10,bottom+6),str(t),font=small,fill='black')
        for z in np.linspace(lo,hi,5):
            _,y=point(0,z);draw.line((left,y,right,y),fill='#eeeeee')
            draw.text((x0,y-8),f'{z:.2f}',font=small,fill='black')
        draw.line((left,top,left,bottom,right,bottom),fill='black',width=1)
        for k,(label,t,values,color) in enumerate(panel['series']):
            draw.line([point(float(tt),float(z)) for tt,z in zip(t,values)],fill=color,width=3)
            xx=x0+10+(k%2)*320;yy=y1-42+(k//2)*24
            draw.line((xx,yy+10,xx+25,yy+10),fill=color,width=3)
            draw.text((xx+32,yy),label,fill='black',font=small)
    img.save(dest/'mechanism_phase2.png')


def main():
    dest=ROOT/'analysis';dest.mkdir(exist_ok=False)
    summary={};curves=[];source_curves=None
    for case in ('A','B'):
        dense=[load(f'dense_{case}_n1024_s{s}_dt0.1_rk4_full') for s in (101,202,303)]
        low=[load(f'dense_{case}_n512_s{s}_dt0.1_rk4_full') for s in (101,202,303)]
        euler=[load(f'dense_{case}_n1024_s{s}_dt0.4_euler_full') for s in (101,202,303)]
        causal=[load(f'causal_{case}_N4096_s{s}_dt0.4_full') for s in (1701,1702,1703)]
        small=[load(f'causal_{case}_N1024_s{s}_dt0.4_full') for s in (1701,1702)]
        fine=[load(f'causal_{case}_N1024_s{s}_dt0.2_full') for s in (1701,1702)]
        refined=load(f'dense_{case}_n1024_s101_dt0.05_rk4_full')
        dm=np.mean([observables(r) for r in euler],0)
        pm=np.mean([observables(r) for r in causal],0)
        ds=np.std([observables(r) for r in euler],0,ddof=1)/np.sqrt(3)
        ps=np.std([observables(r) for r in causal],0,ddof=1)/np.sqrt(3)
        sm=np.mean([observables(r) for r in small],0)
        fm=np.mean([observables(r)[::2] for r in fine],0)
        # Width change uses the RK4 cohorts at the comparison grid; not an
        # Euler width extrapolation, nor a certified bound on population bias.
        width=abs(np.mean([observables(r)[::4] for r in dense],0)-
                  np.mean([observables(r)[::4] for r in low],0))
        envelope=3*np.sqrt(ds*ds+ps*ps)+abs(sm-pm)+width
        pairwise=[float(np.max(abs(euler[a]['f']-euler[b]['f'])))
                  for a in range(3) for b in range(a)]
        result=dict(dense_rk4={k:endpoint(dense,k) for k in
                              ('f','area','source_integrals','gate_drift_integrals',
                               'initial_readout_integral','passive_defect','passive_split')},
                    dense_euler={k:endpoint(euler,k) for k in ('f','area')},
                    causal={k:endpoint(causal,k) for k in ('f','area')},
                    dense_refinement={k:compare_curve(dense[0],refined,k)
                                      for k in ('f','c1','c2','area','source_integrals')},
                    fixed_euler_max_output_mean_discrepancy=float(np.max(abs(dm[:,:3]-pm[:,:3]))),
                    dense_pairwise_max_output_discrepancies=pairwise,
                    dense_pairwise_mean=float(np.mean(pairwise)),
                    mean_discrepancy_max_per_observable=abs(dm-pm).max(0).tolist(),
                    envelope_excess_max_per_observable=np.maximum(abs(dm-pm)-envelope,0).max(0).tolist(),
                    particle_refinement_max_per_observable=abs(sm-pm).max(0).tolist(),
                    euler_step_refinement_max_per_observable=abs(fm-sm).max(0).tolist(),
                    width_change_rk4_max_per_observable=width.max(0).tolist(),
                    dense_area_snapshots=np.mean([r['area'][[0,20,40,80,240]] for r in dense],0).tolist(),
                    snapshot_times=[0,2,4,8,24],
                    dense_delta_c1_endpoint=float(np.mean([r['c1'][-1,0,1]-r['c1'][0,0,1] for r in dense])),
                    dense_delta_c2_endpoint=float(np.mean([r['c2'][-1,0,1]-r['c2'][0,0,1] for r in dense])),
                    causal_delta_c1_endpoint=float(np.mean([r['c1'][-1,0,1]-r['c1'][0,0,1] for r in causal])),
                    causal_delta_c2_endpoint=float(np.mean([r['c2'][-1,0,1]-r['c2'][0,0,1] for r in causal])))
        if case=='A':
            result['approximations']={}
            dmean=np.mean([r['f'] for r in dense],0)
            for model in ('potential','ordered'):
                with np.load(ROOT/'approximation'/f'{model}.npz') as data:
                    ap={k:data[k] for k in data.files}
                result['approximations'][model]=dict(
                    final_f=ap['f'][-1].tolist(),
                    max_training_output_error=float(np.max(abs(ap['f'][:,:2]-dmean[:,:2]))),
                    max_passive_output_error=float(np.max(abs(ap['f'][:,2]-dmean[:,2]))),
                    max_gram_change_error={key:float(np.max(abs((ap[key]-ap[key][0])-
                        np.mean([r[key]-r[key][0] for r in dense],0)))) for key in ('c1','c2')})
            pot=np.load(ROOT/'approximation'/'potential.npz');ordered=np.load(ROOT/'approximation'/'ordered.npz')
            curves.append(dict(title='A: passive prediction (orthogonal training)',series=[
                ('dense RK4 mean',dense[0]['time'],dmean[:,2],'#111111'),
                ('causal Euler mean',causal[0]['time'],pm[:,2],'#167ac6'),
                ('cubic potential',pot['time'],pot['f'][:,2],'#dd7e14'),
                ('ordered cubic',ordered['time'],ordered['f'][:,2],'#b135aa')]))
            source_curves=dict(title='A: sources of passive nonadditivity',series=[
                (label,dense[0]['time'],np.mean([r['source_integrals'][:,k] for r in dense],0),color)
                for k,label,color in ((0,'readout','#111111'),(1,'middle writes','#167ac6'),(2,'lower feature motion','#dd7e14'))])
            area_curve_A=(dense[0]['time'],np.mean([r['area'] for r in dense],0))
        else:
            no_r=[load(f'causal_B_N4096_s{s}_dt0.4_no_reciprocal') for s in (1701,1702)]
            result['no_reciprocal']={k:endpoint(no_r,k) for k in ('f','area')}
            result['no_reciprocal'].update(
                delta_c1_endpoint=float(np.mean([r['c1'][-1,0,1]-r['c1'][0,0,1] for r in no_r])),
                delta_c2_endpoint=float(np.mean([r['c2'][-1,0,1]-r['c2'][0,0,1] for r in no_r])))
            curves.append(dict(title='B: passive prediction (correlated training)',series=[
                ('dense RK4 mean',dense[0]['time'],np.mean([r['f'][:,2] for r in dense],0),'#111111'),
                ('causal Euler mean',causal[0]['time'],pm[:,2],'#167ac6'),
                ('no reciprocal return',no_r[0]['time'],np.mean([r['f'][:,2] for r in no_r],0),'#dd7e14')]))
            area_curve_B=(dense[0]['time'],np.mean([r['area'] for r in dense],0))
        summary[case]=result
    sym={}
    for mode in ('full','frozen_middle','affine_gates'):
        runs=[load(f'dense_symmetric_n512_s{s}_dt0.1_rk4_{mode}') for s in (101,202)]
        sym[mode]={k:endpoint(runs,k) for k in ('f','source_integrals','gate_drift_integrals',
                                              'initial_readout_integral','passive_defect','passive_split')}
    summary['symmetric_controls']=sym
    records=[(p,json.loads(p.read_text())) for p in ROOT.glob('*/record.json')]
    dense_records=[r for p,r in records if p.parent.name.startswith('dense_')]
    causal_records=[r for p,r in records if p.parent.name.startswith('causal_')]
    numerical_runs=[load(p.parent.name) for p,r in records if p.parent.name.startswith('dense_')]
    rk4=[r for (p,rec),r in zip([z for z in records if z[0].parent.name.startswith('dense_')],numerical_runs)
         if rec['config']['method']=='rk4']
    summary['execution']=dict(dense_runs=len(dense_records),causal_runs=len(causal_records),
        wall_seconds=sum(r['wall_seconds'] for p,r in records),
        maximum_peak_rss_kib=max(r['peak_rss_kib'] for p,r in records),
        dense_identity_max=max(float(r['identities'].max()) for r in numerical_runs),
        rk4_source_integration_error=max(float(max(abs(r['integrated_source_defect']))) for r in rk4),
        rk4_ordered_identity_error=max(float(max(r['ordered_identity_error'])) for r in rk4),
        gaussian_factor_covariance_error=max(r['diagnostics'][family]['maximum_covariance_error']
                                             for r in causal_records for family in ('eta','xi')),
        gaussian_factor_discarded_variance=max(r['diagnostics'][family]['maximum_discarded_variance']
                                              for r in causal_records for family in ('eta','xi')))
    summary['qualifications']=[
        'Means and run standard errors are descriptive; 2 or 3 seeds do not establish confidence coverage.',
        'Envelope: three combined run SE plus particle-size and RK4 dense-width changes; not a CI or rate certificate.',
        'Comparison is fixed-mesh Euler; dense RK4 and causal Euler curves are not equally accurate continuum solvers.',
        'Euler source integrals do not obey the continuous product rule exactly; only RK4 used for source attribution.',
        'Maximum RSS is a process/cohort high-water mark, hence a conservative per-run upper envelope.',
        'Quadrature source and coefficients use initialization only; no completed dense trajectory is fitted.',
        'Labels are exploratory, not certified by the original conservative label cap.'
    ]
    (dest/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    curves.extend([dict(title='Signed order memory along dense learning',series=[
        ('A: orthogonal',*area_curve_A,'#167ac6'),('B: correlated',*area_curve_B,'#dd7e14')]),source_curves])
    plot(curves,dest)
    source=Path(__file__)
    manifest={str(p):hashlib.sha256(p.read_bytes()).hexdigest()
              for p in ROOT.rglob('*') if p.is_file()}
    manifest[str(source)]=hashlib.sha256(source.read_bytes()).hexdigest()
    (dest/'sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
