"""Primary sample-by-sample validation comparison at shared physical times."""
import argparse
import json
from pathlib import Path
import itertools
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from DATA import read_idx

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'data/generated/first_order_dimension_mnist'
SEEDS=(1729,2718,3141)

def error_metrics(pred,reference):
    pred=np.asarray(pred,dtype=np.float64);reference=np.asarray(reference,dtype=np.float64)
    error=pred-reference;absolute=np.abs(error);scale=float(np.sqrt(np.mean(reference**2)))
    return {'rms':float(np.sqrt(np.mean(error**2))),'relative_rms':float(np.sqrt(np.mean(error**2))/max(scale,1e-30)),
            'mae':float(absolute.mean()),'median_absolute':float(np.median(absolute)),
            'p90_absolute':float(np.quantile(absolute,.9)),'p95_absolute':float(np.quantile(absolute,.95)),
            'p99_absolute':float(np.quantile(absolute,.99)),'max_absolute':float(absolute.max()),
            'bias':float(error.mean()),'sign_disagreements':int(np.sum((pred>=0)!=(reference>=0))),
            'sign_agreement':float(np.mean((pred>=0)==(reference>=0))),
            'within_0_05':float(np.mean(absolute<=.05)),'within_0_1':float(np.mean(absolute<=.1)),
            'within_0_2':float(np.mean(absolute<=.2)),
            'correlation':float(np.corrcoef(pred,reference)[0,1]) if scale>1e-15 and np.std(pred)>1e-15 else None}

def analyze(output,run_group='main',width=2048):
    dest=BASE/output;dest.mkdir(parents=True,exist_ok=False)
    runs={model:[np.load(BASE/f'{run_group}/{model}_{s}/observations.npz',allow_pickle=False) for s in SEEDS] for model in ('network','closure')}
    meta={model:[json.loads((BASE/f'{run_group}/{model}_{s}/summary.json').read_text()) for s in SEEDS] for model in ('network','closure')}
    shared=set(runs['network'][0]['times'].tolist())
    for model in runs:
        for run in runs[model]:shared.intersection_update(run['times'].tolist())
    times=np.asarray(sorted(shared));final=float(times[-1])
    data=np.load(BASE/'data_3_5/dataset.npz',allow_pickle=False);labels=data['val_y'];ids=data['val_ids']
    digest=hashlib.sha256((BASE/'data_3_5/dataset.npz').read_bytes()).hexdigest()
    assert len(ids)==1000 and len(np.unique(ids))==1000
    for model in runs:
        for run,metadata in zip(runs[model],meta[model]):
            assert np.array_equal(labels,run['val_y'])
            assert metadata['data']['metadata']['dataset_sha256']==digest
            assert metadata['configuration']['width']==width
    predictions={model:np.asarray([[run['val_predictions'][np.flatnonzero(run['times']==t)[0]] for t in times] for run in runs[model]],dtype=np.float64) for model in runs}
    net=predictions['network'];closure=predictions['closure'];netmean=net.mean(axis=0);closuremean=closure.mean(axis=0)
    trajectory=[]
    for i,t in enumerate(times):
        individual=[error_metrics(closure[j,i],netmean[i]) for j in range(3)]
        pairs=[error_metrics(net[j,i],net[k,i]) for j,k in itertools.combinations(range(3),2)]
        trajectory.append({'time':float(t),'individual_closure_vs_network_mean':individual,
                           'closure_mean_vs_network_mean':error_metrics(closuremean[i],netmean[i]),
                           'network_pairwise_rms':[x['rms'] for x in pairs]})
    chosen=-1;reference=netmean[chosen];average=closuremean[chosen]
    all_pairs=[{'closure_seed':s,'network_seed':n,**error_metrics(closure[i,chosen],net[j,chosen])} for i,s in enumerate(SEEDS) for j,n in enumerate(SEEDS)]
    worst=np.argsort(np.abs(average-reference))[::-1]
    examples=[{'validation_row':int(i),'official_train_id':int(ids[i]),'digit':3 if labels[i]>0 else 5,
               'network_outputs':[float(x) for x in net[:,chosen,i]],'closure_outputs':[float(x) for x in closure[:,chosen,i]],
               'network_mean':float(reference[i]),'closure_mean':float(average[i]),'absolute_mean_error':float(abs(average[i]-reference[i]))} for i in worst[:20]]
    within_class={}
    for digit,sign in ((3,1),(5,-1)):
        mask=labels==sign
        within_class[str(digit)]={'count':int(mask.sum()),'network_mean_output_sd':float(np.std(reference[mask])),
             'individual_closure_vs_network_mean':[error_metrics(p[mask],reference[mask]) for p in closure[:,chosen]]}
    selected={}
    for model in runs:
        selected[model]=np.asarray([run['val_predictions'][np.flatnonzero(run['times']==r['selected_time'])[0]] for run,r in zip(runs[model],meta[model])],dtype=np.float64)
    report={'primary_question':'sample-by-sample raw validation prediction approximation; no rescaling or fitted calibration',
            'validation_count':len(labels),'common_final_time':final,'seeds':SEEDS,'run_group':run_group,'width':width,
            'seed_pairing_is_not_initialization_coupling':True,
            'within_class':within_class,
            'label_only_diagnostic':{'description':'Oracle diagnostic returning the true validation label, not a deployable model or training baseline',
                                     **error_metrics(labels,reference)},
            'provenance':{'analysis_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                          'dataset_sha256':digest,'run_summary_sha256':{f'{model}_{seed}':hashlib.sha256((BASE/f'{run_group}/{model}_{seed}/summary.json').read_bytes()).hexdigest() for model in runs for seed in SEEDS}},
            'final':trajectory[-1],'all_individual_seed_pairs':all_pairs,'worst_examples':examples,
            'secondary_independently_selected':{'network_times':[r['selected_time'] for r in meta['network']],
                  'closure_times':[r['selected_time'] for r in meta['closure']],
                  'individual_closure_vs_network_mean':[error_metrics(p,selected['network'].mean(axis=0)) for p in selected['closure']]},
            'trajectory':trajectory}
    (dest/'summary.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    np.savez_compressed(dest/'sample_predictions.npz',times=times,network=net,closure=closure,labels=labels,official_train_ids=ids)
    csv=np.column_stack([ids,labels,net[:,chosen].T,closure[:,chosen].T,reference,average,average-reference])
    np.savetxt(dest/'validation_samples.csv',csv,delimiter=',',header='official_train_id,label,network_1729,network_2718,network_3141,closure_1729,closure_2718,closure_3141,network_mean,closure_mean,mean_error',comments='')
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white'})
    fig,ax=plt.subplots(2,2,figsize=(12,9),layout='constrained')
    colors=np.where(labels>0,'#ce654a','#3377a1')
    for j in range(3):ax[0,0].scatter(reference,closure[j,chosen],s=7,c=colors,alpha=.23)
    limit=max(float(np.max(abs(reference))),float(np.max(abs(closure[:,chosen]))))
    ax[0,0].plot([-limit,limit],[-limit,limit],color='#333333',linestyle='--',linewidth=1)
    ax[0,0].set(title='Each closure seed · orange: 3, blue: 5',xlabel='Actual network mean output',ylabel='p = 1 closure output')
    for j in range(3):ax[0,1].scatter(reference,closure[j,chosen]-reference,s=7,c=colors,alpha=.23)
    ax[0,1].axhline(0,color='#555555',linewidth=1)
    ax[0,1].set(title='Raw prediction error · no calibration',xlabel='Actual network mean output',ylabel='Closure minus network')
    for j,s in enumerate(SEEDS):
        rms=[r['individual_closure_vs_network_mean'][j]['rms'] for r in trajectory]
        ax[1,0].plot(times,rms,label=f'Closure seed {s}',linewidth=1.5)
        errors=np.sort(np.abs(closure[j,chosen]-reference))
        ax[1,1].plot(errors,np.arange(1,len(errors)+1)/len(errors),label=f'Closure {s}')
    network_spread=np.array([r['network_pairwise_rms'] for r in trajectory])
    ax[1,0].plot(times,network_spread.mean(axis=1),'--',color='#222222',label='Network–network seed difference')
    ax[1,0].set(title='Comparison at identical physical times',xlabel='Physical training time',ylabel='Validation output RMS difference');ax[1,0].legend(fontsize=8)
    ax[1,1].set(title=f'Per-image absolute errors at T = {final:g}',xlabel='Absolute output error',ylabel='Fraction of validation images',xlim=(0,float(np.max(np.abs(closure[:,chosen]-reference)))*1.03));ax[1,1].grid(alpha=.2)
    fig.suptitle(f'MNIST 3 versus 5 · prediction fidelity at T = {final:g} · n = P = {width:,}',fontsize=14)
    fig.savefig(dest/'validation_prediction_comparison.png',dpi=180);fig.savefig(dest/'validation_prediction_comparison.pdf');plt.close(fig)
    images=read_idx(BASE/'mnist_raw/train-images-idx3-ubyte.gz')
    fig,axs=plt.subplots(3,4,figsize=(11,9),layout='constrained')
    for a,e in zip(axs.flat,examples):
        a.imshow(images[e['official_train_id']],cmap='gray');a.axis('off')
        a.set_title(f"digit {e['digit']} · validation row {e['validation_row']}\nnet {e['network_mean']:+.3f} · p1 {e['closure_mean']:+.3f}\n|difference| {e['absolute_mean_error']:.3f}",fontsize=9)
    fig.suptitle('Largest mean-prediction discrepancies · validation images only',fontsize=14)
    fig.savefig(dest/'worst_validation_images.png',dpi=170);plt.close(fig)
    print(json.dumps({'common_final_time':final,'final':report['final'],'secondary':report['secondary_independently_selected']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='validation_analysis_001')
    p.add_argument('--run-group',default='main');p.add_argument('--width',type=int,default=2048)
    args=p.parse_args();analyze(args.output,args.run_group,args.width)
