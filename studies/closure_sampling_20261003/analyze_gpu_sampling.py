"""Recompute bounded GPU sampling metrics and resolution checks from archives."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np


def validity(coarse_dir,fine_dir,output):
    coarse_dir,fine_dir=Path(coarse_dir),Path(fine_dir)
    c=np.load(coarse_dir/'observations.npz');f=np.load(fine_dir/'observations.npz')
    rc=json.loads((coarse_dir/'record.json').read_text())
    rf=json.loads((fine_dir/'record.json').read_text())
    tc=np.searchsorted(f['times'],c['times'])
    assert np.allclose(f['times'][tc],c['times'],atol=1e-12)
    # Coordinate matching, not interpolation between query functions.
    distances=np.max(np.abs(c['panel'][:,None,:]-f['panel'][None,:,:]),axis=2)
    pc=np.argmin(distances,axis=1)
    assert float(distances[np.arange(len(pc)),pc].max())<1e-12
    fine_shared=f['predictions'][tc][:,:,pc]
    gaps=np.max(np.abs(c['predictions']-fine_shared),axis=(0,2))
    ce=np.max(np.abs(c['predictions']-c['predictions'][:,0:1,:]),axis=(0,2))
    fe=np.max(np.abs(f['predictions']-f['predictions'][:,0:1,:]),axis=(0,2))
    threshold=min(1e-4,.05*ce[1])
    record={'coarse':str(coarse_dir),'fine':str(fine_dir),'models':rc['model_names'],
       'same_point_dt_errors':gaps.tolist(),'threshold':float(threshold),
       'dt_pass':bool(gaps.max()<=threshold),'coarse_sup':ce.tolist(),'fine_sup':fe.tolist(),
       'max_metric_change':float(np.max(abs(ce-fe))),
       'panel_time_pass':bool(np.max(abs(ce-fe))<=threshold),
       'coarse_dt':rc['dt'],'fine_dt':rf['dt']}
    Path(output).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return record


def analyze(input_dirs,output):
    out=Path(output);out.mkdir(parents=True,exist_ok=False)
    rows=[]; controls=[]; inventory=[]; problems=[]
    for dirname in input_dirs:
        for record_path in sorted(Path(dirname).glob('*/record.json')):
            r=json.loads(record_path.read_text()); folder=record_path.parent
            for file in ('observations.npz','reduced_restart.npz'):
                actual=hashlib.sha256((folder/file).read_bytes()).hexdigest()
                if actual!=r[file+'_sha256']: raise ValueError('archive hash mismatch '+str(folder/file))
            data=np.load(folder/'observations.npz')
            pred=data['predictions'];residual=data['residual_rms']; motion=data['feature_motion']
            error=pred-pred[:,0:1,:]
            sup=np.abs(error).max(axis=(0,2))
            rms=np.sqrt(np.mean(np.max(np.abs(error),axis=0)**2,axis=1))
            endpoint=np.abs(error[-1]).max(axis=1)
            endpoint_rms=np.sqrt(np.mean(error[-1]**2,axis=1))
            assert np.allclose(sup,[x['sup_panel_time'] for x in r['metrics']],rtol=1e-12,atol=1e-14)
            base={k:r[k] for k in ('n','seed','angle','sign')}
            for j in (1,len(sup)-1):
                controls.append(dict(base,model=r['model_names'][j],error=float(sup[j]),
                    scaled_error=float(np.sqrt(r['n'])*sup[j]),endpoint_error=float(endpoint[j]),
                    rms_time_sup=float(rms[j]),scaled_rms_time_sup=float(np.sqrt(r['n'])*rms[j]),
                    scaled_endpoint_error=float(np.sqrt(r['n'])*endpoint[j]),
                    ratio_to_dense=float(sup[j]/sup[1]),settled=r['settled'][j]))
            for s in r['schedule']:
                j=s['model_index']; d=r['sampler_diagnostics'][j-2]
                row=dict(base,p=s['p'],anchor=s['anchor'],selected_width=s['width'],
                    moving=s['moving'],fixed=s['fixed'],total=s['total'],error=float(sup[j]),
                    scaled_error=float(np.sqrt(r['n'])*sup[j]),dense_error=float(sup[1]),
                    ratio_to_dense=float(sup[j]/sup[1]),rms_time_sup=float(rms[j]),
                    scaled_rms_time_sup=float(np.sqrt(r['n'])*rms[j]),
                    endpoint_error=float(endpoint[j]),endpoint_rms=float(endpoint_rms[j]),
                    scaled_endpoint_error=float(np.sqrt(r['n'])*endpoint[j]),
                    scaled_endpoint_rms=float(np.sqrt(r['n'])*endpoint_rms[j]),
                    fit_rms=float(residual[-1,j]),settled=r['settled'][j],
                    feature1=float(motion[-1,j,0]),feature2=float(motion[-1,j,1]),
                    dense_feature1=float(motion[-1,0,0]),dense_feature2=float(motion[-1,0,1]),
                    initial_gram_error=d['training_gram_frobenius_error'],
                    initial_forward_error=d['forward_initial']['mean_weighted_rms'],
                    initial_reverse_error=d['reverse_initial_jet']['mean_weighted_rms'])
                rows.append(row)
                if any(not f['success'] for layer in ('cubature1','cubature2') for f in d[layer]['fits']):
                    problems.append({'case':str(folder),'width':s['width'],'reason':'cubature optimizer non-success'})
                if d['frame1']['discarded_directions'] or d['frame2']['discarded_directions']:
                    problems.append({'case':str(folder),'width':s['width'],'reason':'selected Gram numerical mode discarded'})
            inventory.append({'case':str(folder),**base,'last_time':r['last_time'],
                'setup_seconds':r['setup_seconds'],'evolution_seconds':r['evolution_seconds'],
                'total_seconds':r['total_seconds'],'all_settled':all(r['settled']),
                'max_residual':max(r['last_residual_rms']),
                'max_tail_change':max(r['last_ten_time_change'])})
    def write_csv(name,records):
        with (out/name).open('w',newline='') as handle:
            writer=csv.DictWriter(handle,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
    write_csv('all_comparisons.csv',rows);write_csv('controls.csv',controls);write_csv('cases.csv',inventory)
    groups=[]
    for angle in (60.,90.):
      for sign in (-1,1):
       for n in (512,1024,2048):
        for anchor in (128,256,512):
         for p in (1,2):
            selected=[r for r in rows if (r['angle'],r['sign'],r['n'],r['anchor'],r['p'])==(angle,sign,n,anchor,p)]
            if not selected: continue
            group={'angle':angle,'sign':sign,'n':n,'anchor':anchor,'p':p,'count':len(selected),
                   'selected_width':selected[0]['selected_width'],'total':selected[0]['total'],
                   'all_settled':all(r['settled'] for r in selected)}
            for metric in ('error','scaled_error','ratio_to_dense','endpoint_error','rms_time_sup','feature1','feature2'):
                values=[r[metric] for r in selected]
                group[metric+'_median']=float(np.median(values));group[metric+'_min']=min(values);group[metric+'_max']=max(values)
            groups.append(group)
    write_csv('cell_summary.csv',groups)
    decisions=[]
    for anchor in (128,256,512):
      for p in (1,2):
        selected=[g for g in groups if g['anchor']==anchor and g['p']==p]
        growth=[]
        for angle in (60.,90.):
         for sign in (-1,1):
            low=next((g for g in selected if (g['angle'],g['sign'],g['n'])==(angle,sign,512)),None)
            high=next((g for g in selected if (g['angle'],g['sign'],g['n'])==(angle,sign,2048)),None)
            if low and high: growth.append({'angle':angle,'sign':sign,'factor':high['scaled_error_median']/low['scaled_error_median']})
        complete=len(selected)==12 and all(g['count']==3 for g in selected)
        worst=max(g['ratio_to_dense_median'] for g in selected)
        growthmax=max(g['factor'] for g in growth)
        settled=all(g['all_settled'] for g in selected)
        verdict=('incomplete' if not complete else 'unsettled' if not settled else
                 'competitive' if worst<=1.5 and growthmax<=1.5 else
                 'disfavored_witness' if worst>3 or growthmax>2 else 'inconclusive')
        decisions.append({'anchor':anchor,'p':p,'max_cell_median_ratio':worst,
            'growth':growth,'max_scaled_growth':growthmax,'complete':complete,
            'all_settled':settled,'verdict':verdict})
    report={'case_count':len(inventory),'comparison_count':len(rows),'decisions':decisions,
       'optimizer_or_conditioning_flags':problems,'all_settled':all(r['all_settled'] for r in inventory),
       'max_fit_residual':max(r['max_residual'] for r in inventory),
       'max_last_ten_change':max(r['max_tail_change'] for r in inventory),
       'summed_case_seconds':sum(r['total_seconds'] for r in inventory),
       'summed_setup_seconds':sum(r['setup_seconds'] for r in inventory),
       'summed_evolution_seconds':sum(r['evolution_seconds'] for r in inventory)}
    (out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    plot(groups,controls,out)
    print(json.dumps(report,indent=2))


def plot(groups,controls,out):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axs=plt.subplots(2,2,figsize=(10.5,7.2),sharex=True,layout='constrained')
    ns=np.array([512,1024,2048])
    for ax,(angle,sign) in zip(axs.flat,[(90.,1),(90.,-1),(60.,1),(60.,-1)]):
        for name,color,style in [('dense_independent','#222222','-'),('frozen_dense_hidden','#999999',':')]:
            v=[[r['scaled_error'] for r in controls if (r['angle'],r['sign'],r['n'],r['model'])==(angle,sign,n,name)] for n in ns]
            ax.plot(ns,[np.median(x) for x in v],style,color=color,marker='o',label='Dense vs dense' if name=='dense_independent' else 'Frozen hidden control')
            if name=='dense_independent':ax.fill_between(ns,[min(x) for x in v],[max(x) for x in v],color=color,alpha=.1)
        for p,color,marker in [(1,'#0072B2','s'),(2,'#D55E00','^')]:
            g=[next(r for r in groups if (r['angle'],r['sign'],r['n'],r['anchor'],r['p'])==(angle,sign,n,512,p)) for n in ns]
            ax.plot(ns,[r['scaled_error_median'] for r in g],color=color,marker=marker,label=f'State ∝ log(n)^{p}, anchor 512')
            ax.fill_between(ns,[r['scaled_error_min'] for r in g],[r['scaled_error_max'] for r in g],color=color,alpha=.10)
        ax.set_title(f'{angle:.0f}° inputs · '+('same-sign labels' if sign==1 else 'opposite-sign labels'))
        ax.set_xscale('log',base=2);ax.set_yscale('log');ax.set_xticks(ns,labels=[str(n) for n in ns]);ax.grid(alpha=.2)
        ax.set_ylabel('√n × maximum sampled prediction error')
        ax.set_xlabel('Original width n')
    handles,labels=axs[0,0].get_legend_handles_labels()
    fig.legend(handles,labels,loc='outside lower center',ncol=2,frameon=False)
    fig.suptitle('Initialized coordinated sampling: medians and ranges over 3 seed pairs\nAll saved physical times and 257 unseen circle directions',fontsize=12)
    fig.savefig(out/'width_scaling.png',dpi=180)
    fig.savefig(out/'width_scaling.pdf')
    plt.close(fig)


def main():
    parser=argparse.ArgumentParser();sub=parser.add_subparsers(dest='mode',required=True)
    v=sub.add_parser('validity');v.add_argument('--coarse',required=True);v.add_argument('--fine',required=True);v.add_argument('--output',required=True)
    a=sub.add_parser('analyze');a.add_argument('--inputs',nargs='+',required=True);a.add_argument('--output',required=True)
    args=parser.parse_args()
    if args.mode=='validity':
        r=validity(args.coarse,args.fine,args.output)
        if not(r['dt_pass'] and r['panel_time_pass']):raise SystemExit(2)
    else:analyze(args.inputs,args.output)


if __name__=='__main__':main()
