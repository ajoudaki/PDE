"""Exact rational preflight for the C-H3 short-horizon source cap.

This module certifies explicit scalar inequalities. It is not a population
solver and does not certify a supplied trajectory or a closure residual.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import platform
import resource
import time


def _down(x, bits=256):
    scale = 1 << bits
    return F((x.numerator*scale)//x.denominator, scale)


def _up(x, bits=256):
    return -_down(-x, bits)


def exp_bounds(x, terms=80):
    """Rational enclosure of exp(x), for nonnegative rational x < terms+2."""
    x = F(x)
    if x < 0 or terms < 0 or x >= terms + 2:
        raise ValueError("require 0 <= x < terms+2 and nonnegative terms")
    term = total = F(1)
    for j in range(1, terms + 1):
        term *= x / j
        total += term
    remainder = term * x / (terms + 1) / (1 - x / (terms + 2))
    return _down(total), _up(total + remainder)


def source_cap():
    """Return exact proved overestimates at Y=1,T=1/200."""
    T, C, R, B = F(1, 200), F(101, 10000), F(10101, 10000), F(1, 32)
    exponential = exp_bounds(2*T)[1]
    assert exponential < R and exponential - 1 < C
    D = B + 2*R*C*C*T
    L1 = 4*R*exp_bounds(6*R*D*T + 8*R*R*T*T*C*C)[1]
    d = 2*R*T + 2*C
    psi = d*exp_bounds(d*T*(L1 + 2*R))[1]
    assert psi < B
    return dict(T=T, readout=C, residual=R, beta_cap=B,
                backward_shift=D, lower_pulse=L1, upper_row=psi,
                strict_cap_margin=B-psi)


def gaussian_tail_bound(cutoff):
    """Upper bound for ||Q 1_{|Q|>cutoff}||_2 from Gaussian+bounded form.

    Applies only to the canonical small-time path proved in the accompanying
    note, not to arbitrary numeric action outputs.
    """
    cap = source_cap()
    cutoff = F(cutoff)
    C, D = cap['readout'], cap['backward_shift']
    if cutoff < D:
        raise ValueError("cutoff below the bounded response envelope")
    exponent = (cutoff-D)**2/(8*C*C)
    # exp at large arguments is range-reduced, with exact rational arithmetic.
    halvings = 0
    while exponent > 1:
        exponent /= 2
        halvings += 1
    lower = exp_bounds(exponent)[0]
    for _ in range(halvings):
        lower = _down(lower*lower)
    return 4*(C+D)/lower


def comparison_constants(cutoff, action=F(201,100), readout=F(1,50)):
    """Exact common-carrier sum-norm Lipschitz/tail comparison constants.

    Both actions must have norm <= action, both readout L2 norms <= readout,
    and the reference readout must have that supremum bound. Labels <=1.
    Tail bearing endpoint is the exact canonical path.
    """
    s, A, C = F(cutoff), F(action), F(readout)
    if min(s, A, C) < 0:
        raise ValueError("nonnegative bounds required")
    r = 1+C
    x = 2*A*A*C*C + 4*r*C*A*A + 2*C*C*A + 2*r*C*(2*A+1) + 2*(C+r)*A + 4*r*s
    k = 2*A*C*C + 2*r*C*(2*A+1) + 2*C*C + 4*r*C + 2*(C+r)
    c = 2*A*C + 2*r*A + 2*C + 2*r + 2
    return dict(row_coefficient=x, middle_coefficient=k,
                readout_coefficient=c, lipschitz=max(x,k,c), tail_factor=4*r)


def uniform_defect_budget(defect, initial_error=0, cutoff=F(1,5)):
    """Conditional propagation bound; caller must separately prove the defect.

    If the represented path is in the stated common ball and its full canonical
    RHS defect is <= defect a.e., then the returned sum raw error bounds it.
    This function supplies no algorithm for evaluating that defect.
    """
    defect, initial_error = F(defect), F(initial_error)
    if min(defect, initial_error) < 0:
        raise ValueError("errors must be nonnegative")
    T = F(1,200)
    constants = comparison_constants(cutoff)
    L = constants['lipschitz']
    amp = exp_bounds(L*T)[1]
    source = defect + constants['tail_factor']*gaussian_tail_bound(cutoff)
    return amp*initial_error + (amp-1)*source/L


def report():
    cap = source_cap()
    constants = comparison_constants(F(1,5))
    tail = gaussian_tail_bound(F(1,5))
    assert tail < F(1,10**15)
    assert constants['lipschitz'] < F(83,10)
    budget = uniform_defect_budget(F(1,100000))
    assert budget < F(52,10**9)
    values = {**cap, **constants, 'cutoff':F(1,5), 'tail_bound':tail,
              'conditional_error_for_defect_1e_minus_5':budget}
    return dict(status='exact scalar preflight PASS; full C-H3 incomplete',
                arithmetic='Python arbitrary-precision integer/rational; no floating premise',
                values={key:dict(rational=str(value), display=float(value)) for key,value in values.items()})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    destination = Path(args.output)
    destination.mkdir(parents=True, exist_ok=False)
    start = time.perf_counter()
    result = report()
    result.update(runtime_seconds=time.perf_counter()-start,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  python=platform.python_version(), platform=platform.platform(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (destination/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key:value['display'] for key,value in result['values'].items()}, indent=2))
