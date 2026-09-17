"""Bounded full-batch toy/MNIST comparisons; validation selects checkpoints."""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time
import platform
import numpy as np
import torch
from NETWORK_ENGINE import NetworkEngine,NetworkState
from P1_ENGINE import ClosureEngine,TensorState

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
BASE=ROOT/'data/generated/first_order_dimension_mnist'

def cpu(t): return t.detach().cpu().numpy()
def clone(s): return type(s)(s.w.clone(),s.c.clone(),s.M.clone())
def metrics(pred,y):
    return {'mse':float(np.mean((pred-y)**2)),
            'accuracy':float(np.mean((pred>=0)==(y>=0)))}

def dataset(task,digits,data_name=None):
    if task=='toy':
        rng=np.random.default_rng(20260915);result={}
        for part,count in [('train',24),('val',128),('test',512)]:
            u=rng.normal(size=(count,8));u/=np.linalg.norm(u,axis=1,keepdims=True)
            result[part+'_u']=u
            result[part+'_y']=np.tanh(2*u[:,0]-1.5*u[:,1])+.35*np.sin(3*u[:,2])
        return result,{'dimension':8,'target':'tanh(2u1-1.5u2)+0.35sin(3u3)','seed':20260915}
    path=BASE/(data_name or ('data_%d_%d'%tuple(digits)))
    arrays=np.load(path/'dataset.npz',allow_pickle=False)
    # Do not retrieve test arrays until final checkpoint selection.
    result={k:arrays[k] for k in ('train_u','train_y','val_u','val_y')}
    if task=='pilot':
        val_ids=np.concatenate([np.flatnonzero(result['val_y']==s)[:64] for s in (1,-1)])
        result={k:(v[:256] if k.startswith('train') else v[val_ids]) for k,v in result.items()}
    return result,{'path':str(path),'metadata':json.loads((path/'metadata.json').read_text())}

def make_engine(model,d,n,seed,dtype,device,block):
    if model=='network':
        engine=NetworkEngine(d,n,seed,device=device,dtype=dtype,block_size=block)
        return engine,{'kind':'actual_dense_network','width':n,'seed':seed}
    from P1_INITIALIZATION import initialize
    init=initialize(d,n,seed,population_rule='antithetic',folded=True)
    engine=ClosureEngine(init.b1,init.g,init.b2,init.D,p1=init.p1,p2=init.p2,device=device,dtype=dtype,block_size=block)
    return engine,init.metadata

def save_state(path,engine,state):
    values={k:cpu(getattr(state,k)) for k in ('w','c','M')}
    if isinstance(engine,ClosureEngine):
        values.update({k:cpu(getattr(engine,k)) for k in ('b1','g','b2','D','p1','p2')})
    else:
        values.update({f'initial_{k}':cpu(getattr(engine.initial,k)) for k in ('w','c','M')})
    np.savez(path,**values)

def precision_probe(engine,state,train_u,train_y,val_u,step,steps):
    """Same late state, full-data continuation; never use test labels."""
    if isinstance(engine,ClosureEngine):
        e64=ClosureEngine(*(cpu(getattr(engine,k)) for k in ('b1','g','b2','D')),
                          p1=cpu(engine.p1),p2=cpu(engine.p2),device=engine.device,dtype=torch.float64,block_size=engine.block_size)
        s64=TensorState(*(getattr(state,k).double() for k in ('w','c','M')))
    else:
        e64=NetworkEngine(engine.d,engine.n,0,device=engine.device,dtype=torch.float64,block_size=engine.block_size)
        s64=NetworkState(*(getattr(state,k).double() for k in ('w','c','M')))
    s32=clone(state);data64=e64.prepare_data(train_u,train_y);data32=engine.prepare_data(train_u,train_y)
    for _ in range(steps):
        s32=engine.heun_step(s32,data32,step);s64=e64.heun_step(s64,data64,step)
    v64=e64.prepare_inputs(val_u) if isinstance(e64,ClosureEngine) else val_u
    v32=engine.prepare_inputs(val_u) if isinstance(engine,ClosureEngine) else val_u
    p64=cpu(e64.predict(s64,v64));p32=cpu(engine.predict(s32,v32))
    return {'steps':steps,'elapsed_physical_time':steps*step,'rms_prediction_difference':float(np.sqrt(np.mean((p64-p32)**2))),
            'max_prediction_difference':float(np.max(np.abs(p64-p32))),'pass':bool(np.sqrt(np.mean((p64-p32)**2))<=1e-4)}

def run(args):
    torch.set_num_threads(1);torch.set_num_interop_threads(1)
    torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    dtype=getattr(torch,args.dtype);device='cuda:'+str(args.gpu) if args.gpu>=0 else 'cpu'
    output=BASE/args.output
    output.mkdir(parents=True,exist_ok=False)
    source=output/'source';source.mkdir()
    hashes={}
    for p in HERE.iterdir():
        if p.suffix in ('.py','.md'):
            contents=p.read_bytes();(source/p.name).write_bytes(contents);hashes[p.name]=hashlib.sha256(contents).hexdigest()
    configuration=vars(args).copy();configuration['source_sha256']=hashes
    configuration['environment']={'torch':torch.__version__,'numpy':np.__version__,'python':platform.python_version(),
                                   'device':device,'gpu':torch.cuda.get_device_name(args.gpu) if args.gpu>=0 else None,'tf32':False}
    (output/'config.json').write_text(json.dumps(configuration,indent=2)+'\n')
    data,dmeta=dataset(args.task,args.digits,args.dataset);d=data['train_u'].shape[1]
    start=time.perf_counter();engine,imeta=make_engine(args.model,d,args.width,args.seed,dtype,device,args.block)
    state=engine.initial_state();train=engine.prepare_data(data['train_u'],data['train_y'])
    train_u=torch.as_tensor(data['train_u'],device=device,dtype=dtype)
    val_u=torch.as_tensor(data['val_u'],device=device,dtype=dtype)
    panel=np.concatenate([data['train_u'][:32],data['val_u'][:32]])
    panel_t=torch.as_tensor(panel,device=device,dtype=dtype)
    if args.gpu>=0: torch.cuda.synchronize(args.gpu);torch.cuda.reset_peak_memory_stats(args.gpu)
    init_seconds=time.perf_counter()-start
    observations=[];train_predictions=[];val_predictions=[];gram1=[];gram2=[]
    best_loss=float('inf');best_state=None;best_t=0.;time_now=0.
    training_start=time.perf_counter();integration_seconds=0.
    target=args.horizon;step_count=0;last_observed=-1.;stop_reason='horizon'
    def observe(t):
        nonlocal best_loss,best_state,best_t
        ptr=cpu(engine.predict(state,train_u));pval=cpu(engine.predict(state,val_u))
        obs=engine.observations(state,panel_t)
        gm1=obs['gram1_current'] if isinstance(engine,ClosureEngine) else obs['gram1']
        gm2=obs['gram2_current'] if isinstance(engine,ClosureEngine) else obs['gram2']
        rms1=obs['rms1'] if isinstance(engine,ClosureEngine) else obs['rms_motion1']
        rms2=obs['rms2'] if isinstance(engine,ClosureEngine) else obs['rms_motion2']
        tr=metrics(ptr,data['train_y']);va=metrics(pval,data['val_y'])
        record={'time':t,'train':tr,'validation':va,'rms_motion1':float(rms1),'rms_motion2':float(rms2),
                'cumulative_integration_seconds':integration_seconds}
        observations.append(record);train_predictions.append(ptr);val_predictions.append(pval)
        gram1.append(cpu(gm1));gram2.append(cpu(gm2))
        eligible=(args.task!='mnist' or t in (0.,10.,20.,50.,100.,150.,200.) or
                  (t>=300. and abs(t/100.-round(t/100.))<1e-8))
        if eligible and va['mse']<best_loss:
            best_loss=va['mse'];best_state=clone(state);best_t=t
        print(json.dumps({'model':args.model,'width':args.width,'seed':args.seed,**record}),flush=True)
    observe(0.)
    observation_every=10. if args.task!='pilot' else 5.
    while time_now<target-1e-10:
        dt=min(args.step,target-time_now)
        if args.gpu>=0: torch.cuda.synchronize(args.gpu)
        ts=time.perf_counter();state=engine.heun_step(state,train,dt)
        if args.gpu>=0: torch.cuda.synchronize(args.gpu)
        integration_seconds+=time.perf_counter()-ts
        time_now=round(time_now+dt,10);step_count+=1
        if abs(time_now/observation_every-round(time_now/observation_every))<1e-8 or time_now>=target-1e-10:
            if not all(bool(torch.isfinite(getattr(state,k)).all()) for k in ('w','c','M')):
                raise FloatingPointError('nonfinite training state')
            observe(time_now);last_observed=time_now
        if time.perf_counter()-training_start>args.max_seconds:
            stop_reason='runtime_cap';break
        if time_now>=target-1e-10 and args.continue_validation and target<args.maximum_horizon:
            before=[o for o in observations if abs(o['time']-(target-100.))<1e-6]
            if before and before[0]['validation']['mse']-observations[-1]['validation']['mse']>=.001:
                target=min(target+100.,args.maximum_horizon)
            else: stop_reason='validation_plateau'
    if last_observed!=time_now and time_now!=0: observe(time_now)
    if args.gpu>=0: torch.cuda.synchronize(args.gpu)
    wall_seconds=time.perf_counter()-training_start
    training_peak=torch.cuda.max_memory_allocated(args.gpu) if args.gpu>=0 else None
    probe=None
    if args.precision_probe and args.dtype=='float32':
        probe=precision_probe(engine,state,data['train_u'],data['train_y'],data['val_u'],args.step,20)
    save_state(output/'best_state.npz',engine,best_state);save_state(output/'final_state.npz',engine,state)
    arrays={'times':np.asarray([o['time'] for o in observations]),'train_predictions':np.asarray(train_predictions),
            'val_predictions':np.asarray(val_predictions),'gram1':np.asarray(gram1),'gram2':np.asarray(gram2),
            'train_y':data['train_y'],'val_y':data['val_y'],'panel_u':panel}
    test_record=None
    if args.task!='pilot':
        if args.task!='toy':
            with np.load(Path(dmeta['path'])/'dataset.npz',allow_pickle=False) as saved:
                data['test_u']=saved['test_u'];data['test_y']=saved['test_y']
        test_u=torch.as_tensor(data['test_u'],device=device,dtype=dtype)
        selected=cpu(engine.predict(best_state,test_u));terminal=cpu(engine.predict(state,test_u))
        arrays.update(test_predictions=selected,test_final_predictions=terminal,test_y=data['test_y'])
        test_record={'selected':metrics(selected,data['test_y']),'terminal':metrics(terminal,data['test_y'])}
    np.savez_compressed(output/'observations.npz',**arrays)
    moving_bytes=sum(a.numel()*a.element_size() for a in (state.w,state.c,state.M))
    memory=(engine.retained_bytes(state) if isinstance(engine,ClosureEngine) else 2*engine.state_bytes(state))
    report={'configuration':configuration,'data':dmeta,'initialization':imeta,'observations':observations,
            'selected_time':best_t,'final_time':time_now,'steps':step_count,'stop_reason':stop_reason,
            'initialization_seconds':init_seconds,'integration_seconds':integration_seconds,'training_wall_seconds':wall_seconds,
            'moving_state_bytes':moving_bytes,'retained_model_bytes':memory,
            'retained_model_and_best_checkpoint_bytes':memory+moving_bytes,
            'peak_allocated_bytes':training_peak,
            'peak_with_controls_and_test_bytes':torch.cuda.max_memory_allocated(args.gpu) if args.gpu>=0 else None,
            'precision_probe':probe,'test':test_record}
    (output/'summary.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'done':str(output),'selected_time':best_t,'test':test_record,'integration_seconds':integration_seconds,'probe':probe}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--task',choices=['toy','pilot','mnist'],required=True)
    p.add_argument('--model',choices=['network','closure'],required=True);p.add_argument('--width',type=int,default=2048)
    p.add_argument('--seed',type=int,default=1729);p.add_argument('--digits',type=int,nargs=2,default=[3,5])
    p.add_argument('--dataset',help='Prepared dataset directory within this study generated namespace')
    p.add_argument('--dtype',choices=['float32','float64'],default='float32');p.add_argument('--gpu',type=int,default=0)
    p.add_argument('--step',type=float,default=.5);p.add_argument('--horizon',type=float,default=200.)
    p.add_argument('--maximum-horizon',type=float,default=600.);p.add_argument('--continue-validation',action='store_true')
    p.add_argument('--precision-probe',action='store_true');p.add_argument('--block',type=int,default=1024)
    p.add_argument('--max-seconds',type=float,default=300.);p.add_argument('--output',required=True)
    run(p.parse_args())
