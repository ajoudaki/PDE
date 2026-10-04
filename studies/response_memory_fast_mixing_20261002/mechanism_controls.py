"""Two frozen adversarial matrix controls for the initialized-learning study."""
import sys,hashlib,json
from pathlib import Path
import numpy as np
import torch
import fast_training as run
from reuse_check import FastMixer

BaseMixer=run.Mixer


class ControlMixer(BaseMixer):
    def __init__(self,n,kind,seed,device):
        if kind not in ('two_point','bad_right'):
            super().__init__(n,kind,seed,device);return
        super().__init__(n,'quarter_circle',seed,device)
        self.kind=kind
        if kind=='two_point':
            singular=np.concatenate([np.zeros(n//2),np.full(n//2,np.sqrt(2))])
            reference=FastMixer(singular,seed+20000)
            self.middle=torch.as_tensor(reference.middle,device=device,dtype=torch.float32)

    def forward(self,x):
        if self.kind!='bad_right':return super().forward(x)
        z=x[...,self.rp]*self.right
        return (run.hadamard(z[...,self.perm]*self.middle)*self.left)[...,self.lp]

    def transpose(self,x):
        if self.kind!='bad_right':return super().transpose(x)
        z=run.hadamard(x[...,self.li]*self.left)*self.middle
        return (z[...,self.inverse]*self.right)[...,self.ri]


if __name__=='__main__':
    torch.backends.cuda.matmul.allow_tf32=False
    for kind in ('two_point','bad_right'):
        mixer=ControlMixer(128,kind,7501,'cuda:0')
        x=torch.as_tensor(np.random.default_rng(7901).standard_normal((5,128)),device='cuda:0',dtype=torch.float32)
        W=mixer.forward(torch.eye(128,device='cuda:0')).T
        errors=[((mixer.forward(x)-x@W.T).norm()/(x@W.T).norm()).item(),
                ((mixer.transpose(x)-x@W).norm()/(x@W).norm()).item()]
        if max(errors)>3e-6:raise RuntimeError((kind,errors))
        print('explicit matrix checks',kind,errors,flush=True)
    run.Mixer=ControlMixer
    run.main()
    out=Path(sys.argv[sys.argv.index('--out')+1])
    conf=json.loads((out/'config.json').read_text())
    conf['sources'][str(Path(__file__))]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (out/'config.json').write_text(json.dumps(conf,indent=2)+'\n')
