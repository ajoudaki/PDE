"""Summarize frozen runs, compare to networks, and create standalone figures."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'data/generated/first_order_dimension_mnist'

def load_run(path):
    return json.loads((path/'summary.json').read_text()),np.load(path/'observations.npz',allow_pickle=False)

def analyze(output,run_group='main',control_group='main_controls',width=2048):
    dest=BASE/output;dest.mkdir(parents=True,exist_ok=False)
    runs={}
    for model in ('network','closure'):
        runs[model]=[load_run(BASE/f'{run_group}/{model}_{seed}') for seed in (1729,2718,3141)]
        assert all(r['configuration']['width']==width for r,a in runs[model])
    report={'main':{},'comparisons':[],'controls':{},'wider':{},'toy':{},'run_group':run_group,'control_group':control_group,'width':width}
    for model,items in runs.items():
        rows=[]
        for r,a in items:
            p=a['test_predictions'];y=a['test_y'];pred=p>=0;true=y>=0
            confusion=[[int(np.sum((true==i)&(pred==j))) for j in (False,True)] for i in (False,True)]
            rows.append({'seed':r['configuration']['seed'],'selected_time':r['selected_time'],'final_time':r['final_time'],
                         'test_accuracy':float(np.mean(pred==true)),'test_mse':float(np.mean((p-y)**2)),
                         'negative_recall':float(np.mean(pred[~true]==False)),'positive_recall':float(np.mean(pred[true])),
                         'confusion_rows_negative_positive':confusion,
                         'moving_state_bytes':r.get('moving_state_bytes'),'retained_model_bytes':r['retained_model_bytes'],
                         'peak_allocated_bytes':r['peak_allocated_bytes'],'integration_seconds':r['integration_seconds'],
                         'training_wall_seconds':r['training_wall_seconds'],'precision_probe':r['precision_probe']})
        values=np.array([r['test_accuracy'] for r in rows])
        report['main'][model]={'rows':rows,'mean_test_accuracy':float(values.mean()),'seed_sd_test_accuracy':float(values.std(ddof=1)),
                               'range_test_accuracy':[float(values.min()),float(values.max())]}
    for (nr,na),(cr,ca) in zip(runs['network'],runs['closure']):
        n=na['test_predictions'];c=ca['test_predictions'];y=na['test_y']
        report['comparisons'].append({'seed':nr['configuration']['seed'],
             'accuracy_difference_pp':100*float(np.mean((c>=0)==(y>=0))-np.mean((n>=0)==(y>=0))),
             'prediction_disagreement':float(np.mean((n>=0)!=(c>=0))),
             'relative_output_rms':float(np.linalg.norm(c-n)/np.linalg.norm(n)),
             'absolute_output_rms':float(np.sqrt(np.mean((c-n)**2))),
             'network_selected_time':nr['selected_time'],'closure_selected_time':cr['selected_time']})
    for model in ('network','closure'):
        p=BASE/f'{control_group}/{model}_halfstep'
        if p.exists() and (p/'summary.json').exists():
            r,a=load_run(p);mr,ma=runs[model][0];mask=np.flatnonzero(np.isclose(ma['times'],r['final_time']))
            if len(mask):
                ref=ma['val_predictions'][mask[0]];test=a['val_predictions'][-1];y=a['val_y']
                rms=float(np.sqrt(np.mean((test-ref)**2)))
                accuracy_difference=float(abs(np.mean((test>=0)==(y>=0))-np.mean((ref>=0)==(y>=0))))
                report['controls'][model]={'half_step_validation_rms':rms,'half_step_accuracy_difference_pp':100*accuracy_difference,
                                           'passed':rms<=.002 and accuracy_difference<=.002,'actual_horizon':r['final_time']}
                common=np.intersect1d(ma['times'],a['times'])
                gaps=np.asarray([np.asarray(a['val_predictions'][np.flatnonzero(a['times']==t)[0]],dtype=np.float64)-ma['val_predictions'][np.flatnonzero(ma['times']==t)[0]] for t in common])
                report['controls'][model]['max_over_recorded_times_validation_rms']=float(np.sqrt(np.mean(gaps*gaps,axis=1)).max())
                report['controls'][model]['max_over_recorded_times_absolute_error']=float(np.abs(gaps).max())
        p=BASE/f'width4096/{model}_1729'
        if (p/'summary.json').exists():
            r,a=load_run(p);report['wider'][model]={'selected_time':r['selected_time'],'final_time':r['final_time'],
                      'test':r['test'],'integration_seconds':r['integration_seconds'],'peak_allocated_bytes':r['peak_allocated_bytes']}
        toy=[]
        for seed in (1729,2718):
            r,a=load_run(BASE/f'toy/{model}_{seed}');toy.append({'seed':seed,'selected_time':r['selected_time'],'test':r['test']})
        report['toy'][model]=toy
    (dest/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white'})
    colors={'network':'#242424','closure':'#2863b0'}
    labels={'network':'Actual network','closure':'First-order closure'}
    fig,axs=plt.subplots(2,2,figsize=(12,8),layout='constrained')
    for model,items in runs.items():
        for i,(r,a) in enumerate(items):
            times=a['times'];tr=[o['train']['mse'] for o in r['observations']];va=[o['validation']['accuracy']*100 for o in r['observations']]
            axs[0,0].semilogy(times,tr,color=colors[model],alpha=.65,label=labels[model] if i==0 else None)
            axs[0,1].plot(times,va,color=colors[model],alpha=.65,label=labels[model] if i==0 else None)
            axs[0,1].scatter([r['selected_time']],[next(o['validation']['accuracy']*100 for o in r['observations'] if o['time']==r['selected_time'])],color=colors[model],s=25)
        rows=report['main'][model]['rows'];x=0 if model=='network' else 1
        accuracy=np.array([r['test_accuracy']*100 for r in rows]);axs[1,0].scatter(x+np.array([-.1,0,.1]),accuracy,color=colors[model],s=45)
        axs[1,0].plot([x-.2,x+.2],[accuracy.mean()]*2,color=colors[model],linewidth=3)
    axs[0,0].set(title='Training loss',xlabel='Physical training time',ylabel='Mean squared error');axs[0,0].legend()
    axs[0,1].set(title='Validation accuracy · dots mark selected checkpoints',xlabel='Physical training time',ylabel='Accuracy (%)');axs[0,1].set_ylim(85,100.1)
    axs[1,0].set(title='Official test set · three seeds',ylabel='Accuracy (%)',xticks=[0,1],xticklabels=['Network','p = 1 closure'])
    allacc=[v['test_accuracy']*100 for x in report['main'].values() for v in x['rows']]
    axs[1,0].set_ylim(min(allacc)-.7,100.)
    na=runs['network'][0][1];ca=runs['closure'][0][1];y=na['test_y']
    axs[1,1].scatter(na['test_predictions'],ca['test_predictions'],c=np.where(y>0,'#ce644c','#3c7897'),s=7,alpha=.45,rasterized=True)
    lim=max(np.max(np.abs(na['test_predictions'])),np.max(np.abs(ca['test_predictions'])))
    axs[1,1].plot([-lim,lim],[-lim,lim],'--',color='#777777',linewidth=1)
    axs[1,1].set(title='Test predictions · seed 1729',xlabel='Actual network output',ylabel='p = 1 closure output')
    fig.suptitle(f'MNIST 3 versus 5 · all 784 pixels · n = P = {width:,}',fontsize=15)
    fig.savefig(dest/'mnist_comparison.png',dpi=180);fig.savefig(dest/'mnist_comparison.pdf');plt.close(fig)
    fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained')
    for model,items in runs.items():
        for i,(r,a) in enumerate(items):
            for ell,ax in enumerate(axs,1):
                grams=a[f'gram{ell}'];movement=np.linalg.norm(grams-grams[0],axis=(1,2))/np.linalg.norm(grams[0])
                ax.plot(a['times'],movement,color=colors[model],alpha=.6,label=labels[model] if i==0 else None)
                ax.set(title=f'Hidden layer {ell}',xlabel='Physical training time',ylabel='Relative Gram change from initialization')
    axs[0].legend();fig.suptitle('Feature movement on a fixed training/validation panel')
    fig.savefig(dest/'gram_movement.png',dpi=160);plt.close(fig)
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='analysis_001')
    p.add_argument('--run-group',default='main');p.add_argument('--control-group',default='main_controls');p.add_argument('--width',type=int,default=2048)
    args=p.parse_args();analyze(args.output,args.run_group,args.control_group,args.width)
