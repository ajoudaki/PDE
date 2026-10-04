"""One-dimensional Gaussian integrals for the weak-factor analytic jet."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.special import roots_hermitenorm


def constants(order):
    x, w = roots_hermitenorm(order)
    w = w/np.sqrt(2*np.pi)
    def E(f):
        return float(w @ f)
    t=np.tanh(x); p=1-t*t; q=-2*t*p; r=2*p*(3*t*t-1)
    v=E(t*t); a1=E(p*p); a2=E(q*q)
    z=np.sqrt(v)*x
    t2=np.tanh(z); p2=1-t2*t2; q2=-2*t2*p2; r2=2*p2*(3*t2*t2-1)
    d4=8*t2*p2*(2-3*t2*t2)
    B1=E(p2*p2); B2=E(q2*q2)
    B1p=E(q2*q2+p2*r2); B2p=E(r2*r2+q2*d4)
    C0=a2*B1p+a1*a1*B2p
    part_label=B1*(3*E(p*q*q*r)+E(p*p*q*q))
    part_latent=a1*B2*(4*E(p*p*q*q)+E(p**4))
    part_context=C0*E(t*p*p*q)
    latent=2*(part_label+part_latent+part_context)
    context=2*(B1*E(x*q*r)+2*a1*B2*E(x*p*q)+C0*E(x*t*p))
    return dict(order=order,v=v,a1=a1,a2=a2,B1=B1,B2=B2,B1p=B1p,B2p=B2p,C0=C0,
                latent_parts=[part_label,part_latent,part_context],latent_energy_dd_coefficient=latent,
                context_energy_weight_dd_coefficient=context,
                latent_weight_dd_coefficient=2*(B1*a2+B2*a1*a1))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    data=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),runs=[constants(n) for n in (61,101,201)])
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
