"""Serial GPU1 campaign with retained logs and bounded process runtime."""
import argparse,json,time
from pathlib import Path
from types import SimpleNamespace
from write_buffer_experiment import run
p=argparse.ArgumentParser();p.add_argument('--phase',choices=['pilot','confirm','refine','width','switch'],default='pilot');p.add_argument('--seeds',default='101');p.add_argument('--out',required=True);p.add_argument('--selected',default='fixed1_32');p.add_argument('--selected-multiplier',type=float,default=1.);p.add_argument('--repeated',action='store_true');p.add_argument('--factor-seed',type=int,default=20260924);p.add_argument('--methods');p.add_argument('--max-campaign-seconds',type=float,default=600);a=p.parse_args();root=Path(a.out);root.mkdir(parents=True,exist_ok=True);started=time.perf_counter()
base=dict(check=False,width=256,dt=1/16,horizon=256,interval=32,threshold=.002,diagnostic_every=8,multiplier=1.,schedule=None,device='cuda:1',dtype='float32',max_seconds=90,factor_seed=a.factor_seed,support_switch=False,switch_interval=32.,switch_angle=3.141592653589793/16)
configs={
'dense':dict(method='dense',order=1),
'closure1':dict(method='closure',order=1),
'closure3':dict(method='closure',order=3),
'fixed1_8':dict(method='fixed',order=1,interval=8),
'fixed1_32':dict(method='fixed',order=1,interval=32),
'fixed3_32':dict(method='fixed',order=3,interval=32),
'defect1':dict(method='defect',order=1),
'delay8_lr1':dict(method='delayed',order=1,interval=8),
'delay8_lr025':dict(method='delayed',order=1,interval=8,multiplier=.25),
'delay32_lr1':dict(method='delayed',order=1,interval=32),
'delay32_lr025':dict(method='delayed',order=1,interval=32,multiplier=.25),
'delaydefect_lr1':dict(method='delayed',order=1),
'delaydefect_lr025':dict(method='delayed',order=1,multiplier=.25),
'factor3_a':dict(method='factor',order=3),
'factor3_b':dict(method='factor',order=3,factor_seed=7319)}
if a.phase!='pilot':
    selected=configs[a.selected].copy();delay=dict(method='delayed',order=1,interval=selected.get('interval',32),multiplier=a.selected_multiplier)
    configs={'dense':configs['dense'],a.selected:selected,'delay_selected':delay,'factor_selected':dict(method='factor',order=selected['order'])}
    if a.phase=='refine':base['dt']=1/32
    if a.phase=='width':base['width']=512
    if a.phase=='switch' or a.repeated:base['support_switch']=True
if a.methods:configs={name:config for name,config in configs.items() if name in a.methods.split(',')}
for seed in map(int,a.seeds.split(',')):
    for name,config in configs.items():
        out=root/f'{name}_s{seed}'
        if out.exists():
            assert (out/'summary.json').exists(),f'Incomplete existing run {out}'
            continue
        kw=dict(base,seed=seed,out=str(out));kw.update(config)
        if name.startswith('delaydefect'):kw['schedule']=str(root/f'defect1_s{seed}'/'summary.json')
        if name=='delay_selected' and a.selected=='defect1':kw['schedule']=str(root/f'defect1_s{seed}'/'summary.json')
        if time.perf_counter()-started>a.max_campaign_seconds:raise RuntimeError('Campaign time cap; remaining runs unstarted')
        run(SimpleNamespace(**kw))
print(json.dumps(dict(campaign_seconds=time.perf_counter()-started,phase=a.phase)))
