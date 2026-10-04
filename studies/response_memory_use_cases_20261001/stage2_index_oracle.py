"""Three parent-budget frozen-state float64 diagnostics, never an oracle learner."""
import argparse
import json
from pathlib import Path
import shutil
import sys
import time
import numpy as np
import torch
from stage2_index_experiment import make, pca, sha, write, HERE
from input_field import internal_matrix


@torch.no_grad()
def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True)
    p.add_argument('--pilot',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--selection',type=Path,required=True);args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    torch.cuda.set_device(0);device='cuda:0'
    selections=json.loads(args.selection.read_text())
    sources=['stage2_index_oracle.py','stage2_index_experiment.py','input_field.py','baseline_compact_flow.py','STAGE2_INDEX_THEORY.md']
    for name in sources:shutil.copy2(HERE/name,args.out/name)
    write(args.out/'manifest.json',dict(command=sys.argv,budget='root:3 diagnostic replays',dtype='float64',
          sources={n:sha(HERE/n) for n in sources},selection_sha256=sha(args.selection),
          torch=torch.__version__,numpy=np.__version__,device=torch.cuda.get_device_name(),threads=1,tf32=False))
    results=[]
    for domain in ['fashion','har','housing']:
        started=time.perf_counter();raw=dict(np.load(args.data/(domain+'.npz')))
        data={k:torch.tensor(raw[k],device=device,dtype=torch.float64)
              for k in ['X_train','y_train','X_val','y_val','X_test','y_test']}
        config=dict(selections[domain]['field'],seed=101)
        model=make(config,data,device,torch.float64)
        h=model._forward(model.inputs,model._factors())[0][0]
        oa=h.new_zeros((model.order,model.n,model.M));ob=torch.zeros_like(oa);ob[0]=h
        observers=[oa,ob];states=[*model.state,*observers];saved=[v.clone() for v in states]
        def step():
            hidden,backward,residual,_=model._loss_fields();rho=residual.square().mean().sqrt()
            velocities=[model._transport(oa,backward[1],rho),model._transport(ob,rho*hidden[0],rho)]
            model.step(1/32)
            for o,v in zip(observers,velocities):o.add_(v,alpha=1/32)
        stream=torch.cuda.Stream();stream.wait_stream(torch.cuda.current_stream())
        with torch.cuda.stream(stream):step()
        torch.cuda.current_stream().wait_stream(stream)
        for v,s in zip(states,saved):v.copy_(s)
        graph=torch.cuda.CUDAGraph()
        with torch.cuda.graph(graph,stream=stream):
            for _ in range(32):step()
        for v,s in zip(states,saved):v.copy_(s)
        for _ in range(64):graph.replay()
        torch.cuda.synchronize()
        h=model._forward(model.inputs,model._factors())[0][0]
        new,_,_,_=pca(h,model.C)
        overlap=model.basis.T@new/model.M;u,sv,vh=torch.linalg.svd(overlap)
        new=new@(vh.T@u.T);overlap=model.basis.T@new/model.M
        old=[v.clone() for v in model.moments]
        old_direct=[o@model.basis/model.M for o in observers]
        transported=[v@overlap for v in old]
        exact=[o@new/model.M for o in observers]
        records={};preds={};matrices={}
        for label,values in [('original',old),('overlap',transported),('oracle',exact)]:
            for v,s in zip(model.moments,values):v.copy_(s)
            preds[label]={split:model.predict(data['X_'+split]).cpu().numpy() for split in ['train','val','test']}
            matrices[label]=internal_matrix(model).cpu().numpy()
            records[label]={split:float(np.sqrt(np.mean((preds[label][split]-raw['y_'+split])**2)))
                            for split in ['train','val','test']}
        diffs={}
        for first,second in [('original','oracle'),('overlap','oracle'),('original','overlap')]:
            diffs[first+'_vs_'+second]={split:float(np.sqrt(np.mean((preds[first][split]-preds[second][split])**2)))
                                       for split in ['train','val','test']}
        pilot_result=None
        for file in args.pilot.glob('fit_*/result.json'):
            r=json.loads(file.read_text())
            if all(r['config'].get(k)==config.get(k) for k in ['domain','seed','kind','C','q']):
                pilot_result=(file,r);break
        file,r=pilot_result
        pilot_npz=np.load(file.parent/'predictions.npz')
        idx=[i for i,c in enumerate(r['checkpoints']) if c['time']==64][0]
        calibration=float(np.sqrt(np.mean((preds['original']['test']-pilot_npz['predictions'][idx])**2)))
        result=dict(domain=domain,config=config,seconds=time.perf_counter()-started,
                    dtype='float64',time=64.,dt=1/32,finite=all(bool(torch.isfinite(v).all()) for v in states),
                    source_data_sha256=sha(args.data/(domain+'.npz')),
                    old_observer_absolute_error=max(float((v-o).abs().max()) for v,o in zip(old,old_direct)),
                    old_observer_relative_error=max(float((v-o).norm()/o.norm()) for v,o in zip(old,old_direct)),
                    float32_float64_original_test_rms=calibration,
                    transport_moment_relative_error=[float((v-o).norm()/o.norm()) for v,o in zip(transported,exact)],
                    transport_matrix_relative_error=float(np.linalg.norm(matrices['overlap']-matrices['oracle'])/
                        np.linalg.norm(matrices['oracle']-model.matrices[0].cpu().numpy())),
                    target_rmse=records,prediction_rms=diffs)
        results.append(result);write(args.out/'results.json',results)
        np.savez_compressed(args.out/(domain+'.npz'),**{label+'_'+split:a for label,d in preds.items() for split,a in d.items()},
                            **{'matrix_'+label:a for label,a in matrices.items()})
        print(json.dumps(result),flush=True)
    write(args.out/'completion.json',dict(status='complete',fits=3,seconds=sum(r['seconds'] for r in results)))


if __name__=='__main__':main()
