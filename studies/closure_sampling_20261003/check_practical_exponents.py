"""Independent Gaussian parameterization check; no network training."""
from pathlib import Path
import argparse
import hashlib
import json
import sys
import numpy as np
from scipy.special import roots_hermitenorm
from assess_practical_exponents import covariance, rank_needed


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    out=Path(args.output);out.mkdir(parents=True,exist_ok=False)
    x,w=roots_hermitenorm(256);w=w/np.sqrt(2*np.pi)
    def conditional(q):
        result=np.zeros_like(q)
        for a in range(len(q)):
            for b in range(len(q)):
                variance=q[a,a]
                correlation=np.clip(q[a,b]/variance,-1.,1.)
                za=np.sqrt(variance)*x[:,None]
                zb=np.sqrt(variance)*(correlation*x[:,None]
                    +np.sqrt(max(0.,1-correlation*correlation))*x[None,:])
                result[a,b]=np.sum(w[:,None]*w[None,:]*np.tanh(za)*np.tanh(zb))
        return result
    q=np.array([[1.,1.,0.,-1.],[1.,1.,0.,-1.],
                [0.,0.,1.,0.],[-1.,-1.,0.,1.]])
    reference=covariance(q,256)
    assert np.max(np.abs(reference-conditional(q)))<1e-12
    assert abs(reference[0,2])<1e-14
    assert abs(reference[0,0]+reference[0,3])<1e-14
    here=Path(__file__).resolve().parent
    config_path=here/'gpu_multidata_baseline_0.json'
    config=json.loads(config_path.read_text())
    u=np.array(config['datasets']['circle8_smooth']['U'])
    qa=covariance(covariance(u@u.T,256),256)
    qb=conditional(conditional(u@u.T))
    error=float(np.max(np.abs(qa-qb)));assert error<1e-11
    # Direct brute-force tail sums rather than reverse cumulative sums.
    singular=np.array([5.,3.,2.,1.,0.])
    for tolerance in (0.,.1,.3,.6,1.):
        candidates=[k for k in range(len(singular)+1)
                    if np.sum(singular[k:]**2)<=tolerance**2*np.sum(singular**2)]
        assert rank_needed(singular,3,1,float(np.sum(singular**2)),tolerance)==3+min(candidates)
    paths=[Path(__file__),here/'assess_practical_exponents.py',config_path]
    result=dict(independent_parameterization_max_error=error,
        degenerate_correlation_checks=True,tail_selector_brute_force=True,
        argv=sys.argv,input_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        warning='Converged quadrature and numerical tail checks, not certified trajectory bounds.')
    (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'check_source.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(result))


if __name__=='__main__':main()
