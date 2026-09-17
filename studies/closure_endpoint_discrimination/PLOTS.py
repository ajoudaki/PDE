"""Readable endpoint campaign figures from frozen saved outputs; never trains."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


def _analysis_module():
    spec=importlib.util.spec_from_file_location('endpoint_analysis',Path(__file__).with_name('ANALYZE.py'))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def target(theta,stage):
    a,b,c=theta-np.deg2rad(17),theta+np.deg2rad(11),theta-np.deg2rad(23)
    laws=[np.cos(a),np.cos(3*a),.60*np.cos(3*a)+.40*np.sin(5*a),
          .40*np.cos(3*a)+.35*np.sin(5*a)+.25*np.cos(7*b),
          .20*np.cos(3*a)+.25*np.sin(5*a)+.30*np.cos(7*b)+.25*np.sin(11*c)]
    return np.sign(laws[4]) if int(stage)==5 else laws[int(stage)]


def make_plots(manifest_or_path,out_directory,analysis=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    module=_analysis_module()
    manifest=(json.loads(Path(manifest_or_path).read_text())
              if isinstance(manifest_or_path,(str,Path)) else manifest_or_path)
    inputs=module.load_inputs(manifest['inputs_path'])
    jobs={name:module.load_job(path if isinstance(path,str) else path['path'],inputs)
          for name,path in manifest['jobs'].items()}
    out=Path(out_directory)
    out.mkdir(parents=True,exist_ok=True)
    theta=inputs['dense_theta']
    degrees=np.rad2deg(theta)
    stage=int(manifest.get('stage',next(iter(jobs.values()))['config'].get('stage',0)))
    main_names=[f'cl_N{n}_main' for n in (1,3,5) if f'cl_N{n}_main' in jobs]
    screen_mode=False
    if not main_names:
        screen_mode=True
        main_names=list(jobs)
    colors={1:'#1768AC',3:'#E07816',5:'#7C49A1'}
    curves={name:module._curve(jobs[name],inputs,dense=True) for name in main_names}
    seeds=[f'net_n8192_s{s}' for s in (11,29,47)]
    network=np.mean([module._curve(jobs[name],inputs,dense=True) for name in seeds],axis=0) if all(name in jobs for name in seeds) else None
    refined=[name for name in jobs if name.startswith('cl_') and name.endswith(('_fine','_finest'))]
    all_displayed=list(curves.values())+[module._curve(jobs[name],inputs,dense=True) for name in refined]
    if network is not None:
        all_displayed.append(network)
    all_displayed.append(target(theta,stage))
    offset=2. if min(float(np.min(f)) for f in all_displayed)>-2 else 1.+max(float(np.max(np.abs(f))) for f in all_displayed)
    times=[module._time(jobs[name]) for name in main_names]
    common=all(abs(t-times[0])<1e-7 for t in times)
    endpoint_label=f't={times[0]:g}' if common else ', '.join(
        f'N{jobs[name]["config"]["order"]}: t={module._time(jobs[name]):g}' for name in main_names)
    status='Screening curves; settling unconfirmed' if screen_mode else 'Finite-time endpoint diagnostics'
    focused=manifest.get('focused_result')
    if isinstance(focused,(str,Path)):
        focused=json.loads(Path(focused).read_text())
    if analysis and screen_mode:
        plateau=all(value.get('passed',False) for value in analysis.get('stopinfo',{}).values())
        status=('Screening curves; short plateau checks passed, confirmation not run'
                if plateau else 'Screening curves still moving; no settled endpoint claim')
    elif analysis:
        status=('Validated adjacent-order separation' if analysis.get('validated_separation')
                else 'Curves still moving; no settled endpoint claim' if not analysis.get('all_settled',False)
                else 'Settled finite-time comparison; see numerical gates')
    if focused:
        focused_text=('Adaptive N3–N5 pass' if focused['focused_separation'] else 'Adaptive N3–N5 unresolved')
        full_text='all-model pass' if focused['full_contract_pass'] else 'all-model unresolved'
        n1=focused.get('excluded_jobs',{}).get('cl_N1_main',{}).get('settling',{})
        n1_text='N1 still moving' if n1 and not n1.get('passed',False) else 'N1 shown at its saved time'
        pair_state=('pair/reference settling checks passed' if focused['all_compared_settled']
                    else 'pair/reference settling unresolved')
        status=f'{focused_text}; {full_text}\n{pair_state}; {n1_text}'
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,
                         'figure.facecolor':'white','savefig.facecolor':'white'})
    paths=[]

    def save(fig,name):
        path=out/name
        fig.savefig(path,dpi=170,bbox_inches='tight')
        pdf_path=path.with_suffix('.pdf')
        fig.savefig(pdf_path,bbox_inches='tight')
        plt.close(fig)
        paths.extend((str(path.resolve()),str(pdf_path.resolve())))

    def order(name):
        return int(jobs[name]['config'].get('order',str(name).split('N')[-1].split('_')[0]))

    def gap(ax,polar=False):
        for left,right in ((104,166),(284,346)):
            ax.axvspan(np.deg2rad(left) if polar else left,np.deg2rad(right) if polar else right,
                       color='#B5B0A6',alpha=.18,zorder=0)

    fig,ax=plt.subplots(figsize=(8,8),subplot_kw={'projection':'polar'})
    gap(ax,True)
    ax.plot(np.r_[theta,theta[0]+2*np.pi],np.full(len(theta)+1,offset),
            color='#52606D',ls='--',lw=1,label=f'Reference circle: radius R={offset:g}')
    for name,curve in curves.items():
        n=order(name)
        ax.plot(np.r_[theta,theta[0]+2*np.pi],offset+np.r_[curve,curve[0]],color=colors.get(n),lw=2,label=f'N={n}')
    if network is not None:
        ax.plot(np.r_[theta,theta[0]+2*np.pi],offset+np.r_[network,network[0]],color='#222222',lw=2.2,label='Network mean, n=8192')
    ax.plot(theta,offset+target(theta,stage),color='#777777',lw=1,ls=':',label='Declared target (unseen labels unused)')
    ax.scatter(inputs['train_theta'],np.full(len(inputs['train_theta']),offset),s=28,
               facecolors='white',edgecolors='#52606D',linewidths=1.2,zorder=5,
               label='Input locations at radius R')
    ax.scatter(inputs['train_theta'],offset+inputs['labels'],s=20,color='#222222',zorder=4,
               label='Target labels at radius R+y')
    ax.set_ylim(bottom=0)
    radial_title=manifest.get('radial_title',f'Stage {stage} · {endpoint_label}\n{status}')
    ax.set_title(f'{radial_title}\nRadius = {offset:g} + signed output; shaded arcs have no training data',pad=26)
    ax.legend(loc='upper left',bbox_to_anchor=(1.06,1.02),frameon=False)
    save(fig,'radial_overlay.png')

    fig,ax=plt.subplots(figsize=(12,5))
    gap(ax)
    ax.plot(degrees,target(theta,stage),color='#777777',ls=':',lw=1.5,label='Declared synthetic target')
    for name,curve in curves.items():
        n=order(name)
        ax.plot(degrees,curve,color=colors.get(n),lw=2,label=f'N={n}')
    if network is not None:
        seed_array=np.stack([module._curve(jobs[name],inputs,dense=True) for name in seeds])
        ax.fill_between(degrees,seed_array.min(axis=0),seed_array.max(axis=0),color='#333333',alpha=.15,label='Network seed range')
        ax.plot(degrees,network,color='#222222',lw=2,label='Network seed mean')
    ax.scatter(np.rad2deg(inputs['train_theta']),inputs['labels'],s=26,c='black',zorder=5,label='Training labels')
    ax.set(xlim=(0,360),xlabel='Angle (degrees)',ylabel='Signed output f(θ)',title=f'Stage {stage} · {endpoint_label} · training-free arcs shaded')
    ax.legend(ncol=3,loc='upper center',bbox_to_anchor=(.5,-.16),frameon=False)
    save(fig,'output_by_angle.png')

    fig,axes=plt.subplots(2,1,figsize=(12,7),sharex=True)
    for ax,(a,b) in zip(axes,((1,3),(3,5))):
        gap(ax)
        ax.axhline(0,color='#777777',lw=.8)
        an,bn=f'cl_N{a}_main',f'cl_N{b}_main'
        if screen_mode:
            matches={order(name):name for name in main_names}
            an,bn=matches.get(a),matches.get(b)
        if an in jobs and bn in jobs:
            delta=module._curve(jobs[bn],inputs,dense=True)-module._curve(jobs[an],inputs,dense=True)
            ax.plot(degrees,delta,color=colors[b],lw=2,label='Main resolution')
            for suffix,style in (('fine','--'),('finest',':')):
                na,nb=f'cl_N{a}_{suffix}',f'cl_N{b}_{suffix}'
                if na in jobs and nb in jobs:
                    ax.plot(degrees,module._curve(jobs[nb],inputs,dense=True)-module._curve(jobs[na],inputs,dense=True),
                            color='#222222',lw=1.5,ls=style,label=f'{suffix.capitalize()} quadrature')
            if not screen_mode:
                try:
                    t=module._time(jobs[an])-100
                    older=module._curve(jobs[bn],inputs,t)-module._curve(jobs[an],inputs,t)
                    ax.plot(np.rad2deg(inputs['circle_theta']),older,color='#888888',lw=1,ls='-.',label='100 time units earlier')
                except ValueError:
                    pass
            values=module._norms(delta,inputs['gap_dense_mask'].astype(bool))
            ax.set_title(f'N={b} minus N={a} · gap RMS {values["gap_rms"]:.4f} · gap max {values["gap_max"]:.4f}')
        ax.set(ylabel='Radial displacement Δf',xlim=(0,360))
        ax.legend(loc='upper right',frameon=False)
    axes[-1].set_xlabel('Angle (degrees)')
    fig.suptitle('Differences in common-offset radial functions; shaded arcs fixed before training'
                 + ('\nScreen comparison: '+endpoint_label if screen_mode else ''),y=1.01)
    fig.tight_layout()
    save(fig,'radial_differences.png')

    fig,axes=plt.subplots(2,2,figsize=(12,8))
    for name in main_names+([seeds[0]] if network is not None else []):
        job=jobs[name]
        array=job['arrays']
        t=array['times']
        is_net=name.startswith('net_')
        n=None if is_net else order(name)
        color='#222222' if is_net else colors.get(n)
        label='Network n=8192, seed11' if is_net else f'N={n}'
        if is_net and all(np.array_equal(jobs[seed]['arrays']['times'],t) for seed in seeds):
            seed_losses=np.stack([jobs[seed]['arrays']['loss'] for seed in seeds])
            axes[0,0].fill_between(t,np.maximum(seed_losses.min(axis=0),1e-15),
                                  np.maximum(seed_losses.max(axis=0),1e-15),color='#333333',alpha=.15)
            axes[0,0].semilogy(t,np.maximum(seed_losses.mean(axis=0),1e-15),color=color,label='Network three-seed mean loss')
        else:
            axes[0,0].semilogy(t,np.maximum(array['loss'],1e-15),color=color,label=label)
        drift_times,drift25,drift100=[],[],[]
        for now in t:
            if now<100:
                continue
            try:
                current=module._curve(job,inputs,now)
                d25=np.max(np.abs(current-module._curve(job,inputs,now-25)))
                d100=np.max(np.abs(current-module._curve(job,inputs,now-100)))
            except ValueError:
                continue
            drift_times.append(now);drift25.append(d25);drift100.append(d100)
        axes[0,1].semilogy(drift_times,np.maximum(drift25,1e-15),color=color,label=label)
        axes[1,0].semilogy(drift_times,np.maximum(drift100,1e-15),color=color,label=label)
        axes[1,1].plot(t,array['movement'][:,0],color=color,lw=1.5,label=f'{label}, layer1')
        axes[1,1].plot(t,array['movement'][:,1],color=color,lw=1.5,ls='--',label=f'{label}, layer2')
    axes[0,1].axhline(.005,color='#B44436',ls=':',label='Plateau threshold .005')
    axes[1,0].axhline(.01,color='#B44436',ls=':',label='Continuation threshold .01')
    axes[0,0].set(title='Unhalved training MSE',ylabel='MSE')
    axes[0,1].set(title='Whole-circle maximum change over 25 units',ylabel='Maximum output change')
    axes[1,0].set(title='Whole-circle maximum change over 100 units',ylabel='Maximum output change')
    axes[1,1].set(title='Paired hidden-activation movement',ylabel='RMS from initialization')
    for ax in axes.flat:
        ax.set_xlabel('Physical time')
        ax.grid(alpha=.15)
    axes[0,0].legend(frameon=False,fontsize=9)
    axes[0,1].legend(frameon=False,fontsize=8)
    axes[1,1].legend(frameon=False,fontsize=8,ncol=2)
    fig.suptitle(f'Stage {stage} · convergence and feature movement',y=1.01)
    fig.tight_layout()
    save(fig,'loss_and_settling.png')

    gram_summary=None
    if network is not None and manifest.get('gram_diagnostics',True):
        gram_names=main_names+seeds
        time_indices={name:{round(float(t),7):i for i,t in enumerate(jobs[name]['arrays']['times'])}
                      for name in gram_names}
        common_times=sorted(set.intersection(*(set(index) for index in time_indices.values())))
        if not common_times or abs(common_times[0])>1e-7:
            raise ValueError('Gram diagnostic requires shared history including initialization at t=0')
        if len(common_times)>1 and not np.allclose(np.diff(common_times),5.,rtol=0,atol=1e-7):
            raise ValueError('Gram diagnostic requires the shared five-time-unit observation grid')
        grams={name:np.asarray(jobs[name]['arrays']['grams'][[time_indices[name][t] for t in common_times]],dtype=np.float64)
               for name in gram_names}
        reference_gram=np.mean([grams[name] for name in seeds],axis=0)
        denominator=np.linalg.norm(reference_gram,axis=(-2,-1))
        if np.any(denominator<=0):
            raise ValueError('Relative Gram error has a zero reference denominator')
        errors={name:np.linalg.norm(grams[name]-reference_gram,axis=(-2,-1))/denominator for name in main_names}
        frozen_error=np.linalg.norm(reference_gram[0][None,:,:,:]-reference_gram,axis=(-2,-1))/denominator
        seed_spread=np.max([np.linalg.norm(grams[name]-reference_gram,axis=(-2,-1))/denominator for name in seeds],axis=0)
        fig,axes=plt.subplots(1,2,figsize=(12,5),sharex=True)
        for layer,ax in enumerate(axes):
            for name in main_names:
                n=order(name)
                ax.plot(common_times,errors[name][:,layer],color=colors.get(n),lw=2,label=f'N={n}')
            ax.plot(common_times,frozen_error[:,layer],color='#333333',ls='--',lw=1.6,
                    label='Frozen initial network Gram')
            ax.fill_between(common_times,0,seed_spread[:,layer],color='#777777',alpha=.15,
                            label='Network seed spread from mean')
            ax.set(title=f'Hidden layer {layer+1}',xlabel='Physical time',ylabel='Relative Frobenius error',
                   xlim=(common_times[0],common_times[-1]),ylim=(0,None))
            ax.grid(alpha=.15)
        axes[1].legend(frameon=False,fontsize=9)
        fig.suptitle('Training-input Gram matrices versus the three-seed network mean\n'
                     'Error = ‖G(t) − Ḡnetwork(t)‖F / ‖Ḡnetwork(t)‖F; frozen baseline uses Ḡnetwork(0)',y=1.06)
        fig.tight_layout()
        save(fig,'gram_relative_errors.png')
        gram_summary=dict(definition='Frobenius norm of G_closure(t)-mean_seed_G_network(t), divided by Frobenius norm of mean_seed_G_network(t)',
                          frozen_baseline='G=mean_seed_G_network(0), held constant; same current reference and denominator',
                          role='Descriptive hidden-feature diagnostic; not an endpoint separation or numerical-validation gate',
                          training_points=len(inputs['labels']),times=common_times,
                          errors={name:value.tolist() for name,value in errors.items()},
                          frozen_baseline_errors=frozen_error.tolist(),seed_spread=seed_spread.tolist(),
                          endpoint_errors={name:value[-1].tolist() for name,value in errors.items()},
                          endpoint_frozen_baseline=frozen_error[-1].tolist(),
                          endpoint_seed_spread=seed_spread[-1].tolist(),jobs={name:jobs[name]['directory'] for name in gram_names})
        (out/'gram_relative_errors.json').write_text(json.dumps(gram_summary,indent=2)+'\n')

    if refined:
        fig,axes=plt.subplots(1,2,figsize=(12,5),sharey=True)
        chosen=manifest.get('pair',[1,3])
        for ax,n in zip(axes,chosen):
            gap(ax)
            for suffix,style in (('main','-'),('fine','--'),('finest',':'),('half','-.')):
                name=f'cl_N{n}_{suffix}'
                if name in jobs:
                    ax.plot(degrees,module._curve(jobs[name],inputs,dense=True),ls=style,
                            color=colors[n] if suffix=='main' else '#333333',label=suffix)
            ax.set(title=f'N={n}: quadrature and step controls',xlabel='Angle (degrees)',xlim=(0,360))
            ax.legend(frameon=False)
        axes[0].set_ylabel('Signed output f(θ)')
        fig.tight_layout()
        save(fig,'numerical_control_curves.png')

    if focused:
        controls=focused['focused_numerical_controls']
        categories=[('quadrature','Quadrature'),('step','Time step'),('precision','Precision'),
                    ('width','Network width'),('seed_spread','Network seeds'),('remaining_drift','Remaining drift')]
        pair=focused['pair_raw_evidence']
        fig,axes=plt.subplots(1,2,figsize=(12,5.5))
        budget={}
        for ax,metric,letter in zip(axes,('gap_rms','gap_max'),('D','S')):
            values=[];witnesses=[]
            for category,label in categories:
                eligible={name:value for name,value in controls.items() if value['category']==category}
                witness=max(eligible,key=lambda name:eligible[name][metric],default=None)
                values.append(eligible[witness][metric] if witness else 0.)
                witnesses.append(witness)
            margin=min(pair['main'][metric],pair['refined'][metric])/5
            ax.bar(np.arange(len(categories)),values,color=['#466B8A']*5+['#B17A36'],alpha=.9)
            ax.axhline(margin,color='#A44134',ls='--',lw=1.5,label=f'Minimum main/refined {letter} ÷ 5')
            ax.set(xticks=np.arange(len(categories)),xticklabels=[label for category,label in categories],
                   ylabel='Gap RMS discrepancy' if metric=='gap_rms' else 'Maximum gap discrepancy',
                   title='RMS margin' if metric=='gap_rms' else 'Maximum-displacement margin',ylim=(0,None))
            ax.tick_params(axis='x',labelrotation=30)
            ax.grid(axis='y',alpha=.15);ax.legend(frameon=False,fontsize=9)
            budget[metric]=dict(categories=[c for c,l in categories],values=values,witnesses=witnesses,
                                pair_separation_divided_by_five=margin)
        gate=focused['gates']
        hard_failures=[f'{name}: {value["circle_max"]:.5f} > {value["circle_max_tolerance"]:g}'
                       for name,value in controls.items() if value['category'] in ('quadrature','step','precision')
                       and not value['passed'] and value.get('circle_max_tolerance') is not None
                       and value['circle_max']>value['circle_max_tolerance']]
        footer=('Five-times margin: '+('passed' if gate['focused_uncertainty_margin_passed'] else 'failed')+
                '; pair/reference settling: '+('passed' if gate['relevant_models_settled'] else 'unresolved')+'.')
        if hard_failures:
            footer+='\nAdditional maximum-norm control failures: '+'; '.join(hard_failures)
        fig.suptitle(f'Adaptive N3–N5 uncertainty accounting at {endpoint_label}\n'
                     'Every discrepancy must lie below its dashed margin; settling and hard numerical bounds remain separate gates',y=1.06)
        fig.text(.5,-.06,footer,ha='center',fontsize=10)
        fig.tight_layout()
        save(fig,'focused_uncertainty_budget.png')
        (out/'focused_uncertainty_budget.json').write_text(json.dumps(dict(budget=budget,gates=gate,
            original_all_model_verdict=focused['original_all_model_verdict'],interpretation=focused['interpretation']),indent=2)+'\n')

    ladder=manifest.get('ladder',[])
    if ladder:
        rows=[]
        for item in ladder:
            if isinstance(item,str):
                item=json.loads(Path(item).read_text())
            screen=item.get('screen',item)
            pair_values=screen.get('pairs',{})
            def cell(key):
                value=pair_values.get(key,{})
                return f'{value["gap_rms"]:.4f} / {value["gap_max"]:.4f}' if 'gap_rms' in value else '—'
            rows.append([str(item.get('stage',screen.get('stage','?'))),cell('1-3'),cell('3-5'),
                         str(item.get('outcome','provisional' if screen.get('provisional') else 'not separated in screen'))])
        fig,ax=plt.subplots(figsize=(12,max(2.5,.55*len(rows)+1.5)))
        ax.axis('off')
        table=ax.table(cellText=rows,colLabels=['Stage','N1–N3 gap RMS / max','N3–N5 gap RMS / max','Outcome'],
                       cellLoc='left',loc='center',colWidths=[.07,.25,.25,.43])
        table.auto_set_font_size(False);table.set_fontsize(10);table.scale(1,1.7)
        ax.set_title('Fixed complexity ladder · every attempted case retained\nScreen separation is provisional until the confirmation gates pass',pad=20)
        save(fig,'ladder_outcomes.png')
    summary=dict(stage=stage,radial_offset=offset,paths=paths,endpoint_label=endpoint_label,
                 status=status,reference='Three-seed width8192 mean' if network is not None else None)
    if gram_summary is not None:
        summary['gram_endpoint_errors']=gram_summary['endpoint_errors']
        summary['gram_frozen_baseline_endpoint']=gram_summary['endpoint_frozen_baseline']
    if focused:
        summary['focused_separation']=focused['focused_separation']
        summary['original_all_model_pass']=focused['full_contract_pass']
    (out/'plot_manifest.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary


def make_ladder_overview(campaign_directory,out_directory):
    """Combine all six frozen screen decisions without reanalyzing trajectories."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    campaign=Path(campaign_directory)
    out=Path(out_directory)
    results=[]
    for stage in range(6):
        path=campaign/f'stage_{stage:02d}'/'screen_analysis.json'
        if not path.exists():
            raise ValueError(f'All six completed screens required; missing {path}')
        results.append(json.loads(path.read_text()))
    out.mkdir(parents=True,exist_ok=True)
    fig=plt.figure(figsize=(14,10))
    grid=fig.add_gridspec(2,2,height_ratios=[1,1.25],hspace=.28)
    axes=[fig.add_subplot(grid[0,0]),fig.add_subplot(grid[0,1])]
    stages=np.arange(6)
    pair_colors={'1-3':'#1768AC','3-5':'#7C49A1'}
    for ax,metric,threshold,label in zip(axes,('gap_rms','gap_max'),(.075,.15),('Gap RMS difference D','Maximum gap difference S')):
        for pair,color in pair_colors.items():
            values=[r['pairs'][pair][metric] for r in results]
            ax.plot(stages,values,'o-',color=color,lw=2,label=f'N{pair.replace("-", " versus N")}')
        ax.axhline(threshold,color='#B44436',ls='--',lw=1.2,label=f'Required threshold {threshold:g}')
        ax.set(xticks=stages,xlabel='Target-law stage',ylabel=label,xlim=(-.2,5.2),ylim=(0,None))
        ax.grid(alpha=.15)
        ax.spines[['top','right']].set_visible(False)
        ax.legend(frameon=False,fontsize=10)
    ax=fig.add_subplot(grid[1,:]);ax.axis('off')
    law_names=['First harmonic','Third harmonic','Third + fifth','Third + fifth + seventh',
               'Third + fifth + seventh + eleventh','Sign of stage 4']
    rows=[]
    for stage,result in enumerate(results):
        stop=result['stopinfo']
        times=' / '.join(f'{stop[str(n)]["time"]:g}' for n in (1,3,5))
        unfinished=[f'N{n}' for n in (1,3,5) if not stop[str(n)]['passed']]
        plateau='Passed' if not unfinished else 'Still moving: '+', '.join(unfinished)
        visible=[key for key,value in result['pairs'].items() if value.get('provisional')]
        decision='Provisional '+', '.join(visible) if visible else 'No provisional separation'
        rows.append([str(stage),law_names[stage],times,plateau,decision])
    table=ax.table(cellText=rows,colLabels=['Stage','Fixed target law','Stop times N1 / N3 / N5',
                      'Short plateau check','Screen decision'],cellLoc='left',loc='center',
                      colWidths=[.05,.27,.21,.21,.26])
    table.auto_set_font_size(False);table.set_fontsize(10);table.scale(1,2.25)
    for (row,column),cell in table.get_celld().items():
        cell.set_edgecolor('#DDDDDD')
        if row==0:
            cell.set_facecolor('#EEEEEE');cell.set_text_props(weight='bold')
    fig.suptitle('Six predeclared target laws: screening outcomes\n'
                 'A pair must cross both thresholds; screen stop times may differ and do not establish a common settled endpoint',
                 fontsize=14,y=.98)
    fig.text(.5,.04,'Training inputs and unseen arcs are fixed across stages. The stage sequence does not imply monotone learning difficulty.\n'
                    'A provisional separation requires the full numerical and common-time confirmation before it can count as final success.',
                    ha='center',fontsize=10,color='#444444')
    paths=[]
    for suffix in ('png','pdf'):
        path=out/f'ladder_overview.{suffix}'
        fig.savefig(path,dpi=170,bbox_inches='tight')
        paths.append(str(path.resolve()))
    plt.close(fig)
    summary=dict(kind='six_stage_screen_overview',paths=paths,rows=rows,
                 scientific_interpretation='Screening evidence only; no confirmation inferred.')
    (out/'ladder_overview.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary


def main():
    parser=argparse.ArgumentParser()
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--manifest')
    mode.add_argument('--ladder-campaign')
    parser.add_argument('--analysis')
    parser.add_argument('--out',required=True)
    args=parser.parse_args()
    analysis=json.loads(Path(args.analysis).read_text()) if args.analysis else None
    result=(make_ladder_overview(args.ladder_campaign,args.out) if args.ladder_campaign
            else make_plots(args.manifest,args.out,analysis))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
