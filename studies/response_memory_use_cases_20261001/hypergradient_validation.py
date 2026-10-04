"""Independent functional-adapter checks; no fitting or method selection."""
import argparse,hashlib,json,sys,time
from pathlib import Path
import numpy as np
import torch
from hypergradient import FunctionalFlow,circle,utc,write,SOURCE,BASE

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);a=parser.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    (a.out/'hypergradient_validation_source.py').write_bytes(Path(__file__).read_bytes())
    result=dict(start_utc=utc(),source_sha256=SOURCE,baseline_sha256=BASE,validation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),python=sys.version,torch=torch.__version__,gpu=torch.cuda.get_device_name(0))
    device='cuda:0';dtype=torch.float64;x,y=circle(8,.13,device,dtype);v,target=circle(32,.37,device,dtype)
    xx=x.clone().requires_grad_();direction=torch.arange(1,1+x.numel(),device=device,dtype=dtype).reshape_as(x);direction=direction/direction.norm()
    def loss(z):
        flow=FunctionalFlow(z,32,101,'q4')
        return (flow.predict(flow.solve(y,1/32,1),v)-target).square().mean()
    exact=float((torch.autograd.grad(loss(xx),xx)[0]*direction).sum());rows=[]
    for eps in [1e-4,5e-5]:
        fd=float((loss(x+eps*direction)-loss(x-eps*direction))/(2*eps))
        rows.append(dict(epsilon=eps,autograd=exact,finite_difference=fd,relative_error=abs(fd-exact)/max(abs(exact),1e-12)))
    result['input_prefix_fd']=rows
    # Readout-only direct Euler vs spectral linear map, including antipodal nullspace.
    flow=FunctionalFlow(x,32,101,'dense');h=torch.tanh(flow.W0@torch.tanh(flow.w0@x.T));hq=torch.tanh(flow.W0@torch.tanh(flow.w0@v.T));c=flow.c0.clone()
    for _ in range(256):c=c-(2/len(x))/32*h@(c@h/32-y)
    direct=c@hq/32;spectral=flow.frozen_map(v,1/32,8)@y
    result['frozen_euler_spectral_error']=float((direct-spectral).abs().max());result['end_utc']=utc();result['pass']=result['frozen_euler_spectral_error']<1e-10 and all(r['relative_error']<1e-4 for r in rows)
    write(a.out/'validation.json',result);print(json.dumps(result))
if __name__=='__main__':main()
