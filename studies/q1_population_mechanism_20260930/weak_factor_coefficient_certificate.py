"""Certify the second-layer and hierarchy coefficients from enclosed moments.

No new quadrature and no training simulation. The input must be the recorded
outward Gaussian-moment certificate; all polynomial arithmetic remains outward.
"""
import argparse
import hashlib
import json
from pathlib import Path
from weak_factor_interval_certificate import I


def coefficients(data):
    inner = [I(0)] + [I(*v) for v in data['inner']]
    outer = [I(0)] + [I(*v) for v in data['outer']]
    kappa = 1-inner[1]
    a = inner[2]
    b = 4*(inner[2]-inner[3])
    T = outer[2]
    U = 4*(outer[2]-outer[3])
    S = 8*outer[2]-10*outer[3]
    V = 32*outer[2]-112*outer[3]+84*outer[4]
    B0 = b*S+a*a*V
    B1 = a*U
    C0 = a*S
    A0 = inner[2]-inner[3]
    A1 = -2*(inner[3]-inner[4])
    A2 = 4*(inner[4]-inner[5])
    A3 = -8*inner[3]+20*inner[4]-12*inner[5]
    A4 = 16*inner[4]-40*inner[5]+24*inner[6]
    A5 = inner[4]
    P = 4*(outer[4]-outer[5])
    Q = 16*outer[4]-40*outer[5]+24*outer[6]
    J0 = 3*outer[2]-2*outer[1]
    P0 = -2*(outer[3]-outer[4])
    Q0 = -8*outer[3]+20*outer[4]-12*outer[5]
    drift = B0*C0*A0+(B0*T+2*B1*C0)*A1+(4*B1*T+T*T)*A2+T*C0*A3+3*T*T*A4+B1*T*A5
    noise = a*a*(a+2*b)*P+3*a**4*Q
    memory = (kappa*a*b+a**3)*P+3*kappa*a**3*Q
    context_drift = J0*(B0*A0+2*B1*A1+T*A3)
    context_noise = a*(b*P0+a*a*Q0)
    context_memory = kappa*(b*P0+a*a*Q0)
    first = {k:I(*v) for k,v in data['first_coefficients'].items()}
    result = dict(
        second_latent=2*(drift+noise+memory),
        second_context=2*(context_drift+context_noise+context_memory),
        second_latent_drift=2*drift,
        second_latent_reverse_covariance=2*noise,
        second_latent_memory=2*memory,
        second_context_drift=2*context_drift,
        second_context_reverse_covariance=2*context_noise,
        second_context_memory=2*context_memory,
        first_latent_over_context=(kappa*first['latent']-a*first['context'])/(kappa*kappa),
        first_target_over_latent=(a*first['target']-b*first['latent'])/(a*a),
    )
    return {k:v.pair() for k,v in result.items()}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--moments',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    raw=args.moments.read_bytes()
    data=json.loads(raw)
    source=Path(__file__)
    interval_source=source.with_name('weak_factor_interval_certificate.py')
    assert data['source_sha256']==hashlib.sha256(interval_source.read_bytes()).hexdigest()
    result=dict(
        moment_file=str(args.moments),
        moment_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        interval_source_sha256=data['source_sha256'],
        coefficients=coefficients(data),
    )
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
