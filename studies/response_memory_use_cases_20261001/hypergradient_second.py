"""Single preregistered second-teacher stress; network adapter is unchanged."""
import argparse,hashlib,sys,math
from pathlib import Path
import torch
import hypergradient as hg

def second_circle(count,shift,device,dtype):
    theta=(torch.arange(count,device=device,dtype=dtype)+shift)*(2*math.pi/count)
    return torch.stack((theta.cos(),theta.sin()),1),torch.sin(3*theta)+.4*torch.cos(theta)+.3*torch.cos(5*theta)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);a=parser.parse_args()
    a.out.mkdir(parents=True,exist_ok=False);out=a.out
    (out/'hypergradient_second_source.py').write_bytes(Path(__file__).read_bytes())
    (out/'hypergradient_source.py').write_bytes(Path(hg.__file__).read_bytes())
    a.out=str(a.out);a.device='cuda:0';a.width=512;a.dt=1/32;a.horizon=8.;a.seeds=[301];a.kinds=['dense','q1','frozen'];a.outer_steps=24;a.refine=True;a.teacher='sin3+.4cos1+.3cos5';a.wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    hg.circle=second_circle;hg.evaluate(a,out)
