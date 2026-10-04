"""Independent frozen-middle oracle and predetermined dense replay checks."""
import argparse
import hashlib
from pathlib import Path
import sys
import torch
import json
from hypergradient import FunctionalFlow, circle, write, utc
from hypergradient_controls import FrozenMiddle

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'data/generated/response_memory_use_cases_20261001'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    names=['hypergradient_controls_check.py','hypergradient_controls.py','hypergradient.py',
           'baseline_compact_flow.py','HYPERGRADIENT_CONTROL_PROTOCOL.md']
    write(args.out/'manifest.json',{'command':sys.argv,'started_utc':utc(),
          'python':sys.executable,'torch':torch.__version__,'threads':torch.get_num_threads(),
          'device':'cpu','source_hashes':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in names}})
    for name in names:(args.out/name).write_bytes((HERE/name).read_bytes())
    x,y=circle(8,.13,'cpu',torch.float64);query,truth=circle(32,.37,'cpu',x.dtype)
    model=FrozenMiddle(x,32,101,'dense')
    with torch.no_grad():state=model.solve(y,1/32,1)
    w,W,c=[v.detach().requires_grad_() for v in state]
    h=torch.tanh(w@x.T);g=torch.tanh(W@h);loss=(c@g/32-y).square().mean()
    dw,dW,dc=torch.autograd.grad(loss,(w,W,c))
    expected=(-32*dw,torch.zeros_like(dW),-32*dc)
    actual=model.rhs(state,y)
    oracle_error=max(float((a-b).abs().max()) for a,b in zip(actual,expected))
    fixed_middle_error=float((state[1]-model.W0).abs().max())
    def objective(labels):return (model.predict(model.solve(labels,1/32,1),query)-truth).square().mean()
    direction=torch.arange(1,9,dtype=x.dtype);direction/=direction.norm()
    yy=y.clone().requires_grad_()
    ad=float(torch.autograd.grad(objective(yy),yy)[0]@direction)
    eps=1e-4
    fd=float((objective(y+eps*direction)-objective(y-eps*direction))/(2*eps))
    relative=abs(ad-fd)/max(abs(ad),1e-12)
    assert oracle_error<1e-12 and fixed_middle_error==0 and relative<1e-6
    rows=[];input_hashes={}
    for folder in ['hypergradient_strong_regular01','hypergradient_irregular01']:
        path=BASE/folder/'results.json';input_hashes[str(path.relative_to(BASE))]=hashlib.sha256(path.read_bytes()).hexdigest()
        originals={}
        for row in json.loads(path.read_text()):
            seed=row['seed'];xx=torch.tensor(row['inputs'],dtype=torch.float32)
            labels=torch.tensor(row['labels'],dtype=xx.dtype)
            orig=torch.tensor(row['original_labels'],dtype=xx.dtype)
            test,target=circle(256,.71,'cpu',xx.dtype)
            dense=FunctionalFlow(xx,512,seed,'dense')
            with torch.no_grad():
                if seed not in originals:
                    originals[seed]=float((dense.predict(dense.solve(orig,1/64,8),test)-target).square().mean())
                refined=float((dense.predict(dense.solve(labels,1/64,8),test)-target).square().mean())
            improvement=row['original_dense_mse']-row['dense_test_mse']
            refined_improvement=originals[seed]-refined
            rows.append({'panel':row['panel'],'seed':seed,'kind':row['kind'],
                         'coarse_mse':row['dense_test_mse'],'refined_mse':refined,
                         'refined_original_mse':originals[seed],
                         'relative_improvement_drift':abs(refined_improvement-improvement)/abs(improvement)})
    refinement_pass=max(r['relative_improvement_drift'] for r in rows)<.1
    result={'rhs_autograd_max_error':oracle_error,'fixed_middle_error':fixed_middle_error,
            'label_autograd':ad,'label_finite_difference':fd,'label_fd_relative_error':relative,
            'refinement':rows,'refinement_pass':refinement_pass,
            'input_hashes':input_hashes,'inner_solves':16,'ended_utc':utc(),'exit_status':0}
    write(args.out/'checks.json',result);print(json.dumps(result,indent=2))


if __name__=='__main__':main()
