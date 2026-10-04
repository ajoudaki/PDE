"""Bounded IEEE float32 kernel verification before reference-only trajectories."""
import os
os.environ['OMP_NUM_THREADS']='1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import torch
import fast_training as original
import fast_training_split_reference as split
import reuse_check


def torch_hadamard(x):
    v=x.clone()
    n=v.shape[-1]
    width=1
    while width<n:
        block=v.reshape(*v.shape[:-1],-1,2,width)
        a,b=block[...,0,:].clone(),block[...,1,:].clone()
        block[...,0,:]=a+b
        block[...,1,:]=a-b
        width*=2
    return v*(n**-.5)


def relative(a,b):
    return float(np.linalg.norm(a-b)/np.linalg.norm(b))


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    torch.set_num_threads(1);torch.set_grad_enabled(False)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    torch.manual_seed(810001)
    n=32768
    x=torch.randn(5,n,device='cuda:0')
    y=split.hadamard(x)
    expected=torch_hadamard(x)
    xn=x.cpu().numpy()
    yn=y.cpu().numpy()
    metrics={'torch_bitwise_equal':torch.equal(y,expected),
        'torch_relative_error':relative(yn,expected.cpu().numpy()),
        'numpy_float64_relative_error':relative(yn,reuse_check.hadamard(xn)),
        'involution_relative_error':relative(split.hadamard(y).cpu().numpy(),xn)}
    selected=[0,1,16383,16384,32767]
    basis=torch.zeros(len(selected),n,device='cuda:0')
    for row,column in enumerate(selected): basis[row,column]=1
    explicit=np.asarray([[(-1 if (i&j).bit_count()%2 else 1)*np.float32(n**-.5)
                          for j in range(n)] for i in selected],dtype=np.float32)
    metrics['basis_signs_exact']=np.array_equal(split.hadamard(basis).cpu().numpy(),explicit)
    small=x[:,:16384]
    metrics['lower_width_bitwise_equal']=torch.equal(split.hadamard(small),original.hadamard(small))
    mixer=split.Mixer(n,'quarter_circle',8001,'cuda:0')
    arr={name:getattr(mixer,name).cpu().numpy() for name in ['lp','rp','li','ri','perm','inverse','left','right','middle']}
    forward_ref=reuse_check.hadamard(reuse_check.hadamard(xn[...,arr['rp']]*arr['right'])[...,arr['perm']]*arr['middle'])*arr['left']
    forward_ref=forward_ref[...,arr['lp']]
    transpose_ref=reuse_check.hadamard((reuse_check.hadamard(xn[...,arr['li']]*arr['left'])*arr['middle'])[...,arr['inverse']])*arr['right']
    transpose_ref=transpose_ref[...,arr['ri']]
    forward=mixer.forward(x);transpose=mixer.transpose(x)
    metrics['mixer_forward_float64_relative_error']=relative(forward.cpu().numpy(),forward_ref)
    metrics['mixer_transpose_float64_relative_error']=relative(transpose.cpu().numpy(),transpose_ref)
    z=x.roll(1,0)
    metrics['adjoint_error']=float(((forward*z).sum()-(x*mixer.transpose(z)).sum()).abs()/(x.norm()*z.norm()))
    torch.cuda.synchronize()
    checks=[v<3e-6 for k,v in metrics.items() if 'error' in k]
    checks += [metrics[k] for k in ('torch_bitwise_equal','basis_signs_exact','lower_width_bitwise_equal')]
    sources=[Path(__file__),Path(split.__file__),Path(original.__file__),Path(reuse_check.__file__),Path(__file__).with_name('POPULATION_COST_SPLIT_REFERENCE_AMENDMENT.md')]
    result={'passed':all(checks),'width':n,'batch':5,'seed':810001,'mixer_seed':8001,
        'precision':'float32 IEEE; independent NumPy float64 oracle','metrics':metrics,
        'elapsed_seconds':time.monotonic()-started,'gpu':torch.cuda.get_device_name(),
        'visible_gpu':os.environ.get('CUDA_VISIBLE_DEVICES'),
        'source_hashes':{str(s.resolve()):hashlib.sha256(s.read_bytes()).hexdigest() for s in sources}}
    (args.out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    np.savez(args.out/'verification_arrays.npz',input=xn,split_output=yn,numpy_output=reuse_check.hadamard(xn))
    print(json.dumps(result,indent=2),flush=True)
    if not result['passed']: raise RuntimeError('split reference kernel verification failed')


if __name__=='__main__':main()
