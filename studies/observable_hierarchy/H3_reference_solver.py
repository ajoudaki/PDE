"""Integrated bounded-reference certificate and reproducible observation API.

This fixed-order component has an analytical error floor. It is not the
arbitrary-accuracy, general-law C-H3 solver requested by the research contract.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import time

import H3_shorttime_solver as reference
import H3_circle_kernel as circle


def prediction(state, kernel, u1, u2):
    """Canonical-GF prediction enclosure for the represented reference state.

    state is an unmodified tuple produced by load_checkpoint/advance_checkpoint.
    Its intervals must descend from the certified reference initialization.
    Coordinates enclose the requested actual normalized unit direction.
    The cumulative analytical error is evaluated at the saved total time.
    """
    elapsed, b, beta, coefficients = state
    if not F(0) <= elapsed <= F(1, 200):
        raise ValueError('state outside the certified horizon')
    numerical = kernel.prediction_box(b, u1, u2)
    analytical = reference.sharpened_bounds(reference.rational(elapsed))['frozen_prediction']
    return numerical.widen(analytical)


def reproduce(destination):
    """One complete initialization/evolution/reload/whole-circle execution."""
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    start = time.perf_counter()
    config = circle.configuration_certificate()
    (destination/'circle_configuration.json').write_text(json.dumps(config, indent=2)+'\n')
    ref = reference.run(8192, destination/'midpoint_checkpoint.json')
    circle_start = time.perf_counter()
    kernel, lower, upper = circle.initialize(config)
    circle_seconds = time.perf_counter()-circle_start
    (destination/'kernel.json').write_text(json.dumps(kernel.record(), indent=2)+'\n')
    # Reload both saved ingredients. No initial integral or old trajectory is
    # used by continuation/observation after this point.
    saved = reference.load_checkpoint(destination/'midpoint_checkpoint.json')
    restored_kernel = circle.CircleKernel.from_record(json.loads((destination/'kernel.json').read_text()))
    state = reference.advance_checkpoint(saved, F(1, 400))
    k = state[3]['k']
    if not (F(k.lo) > F(23,100) and F(k.hi) < F(24,100)
            and F(k.hi)-F(k.lo) < F(3,10**10)):
        raise ArithmeticError('uniform-time coefficient-width gate failed')
    # Proof in H3_candidate_reference_v1.md: two closed-form steps, total T,
    # have this uniform width bound including a conservative arithmetic reserve.
    time_width = (F(6,1000)+2/F(23,100))*F(1,200)*(F(k.hi)-F(k.lo))+F(1,10**40)
    if time_width >= 2*circle.MAX_B_RADIUS:
        raise ArithmeticError('uniform-time readout error gate failed')
    error = restored_kernel.uniform_prediction_error()+circle.ANALYTIC_ENVELOPE
    if error >= F(1,100000):
        raise ArithmeticError('whole-circle numerical/analytical budget failed')
    e1 = prediction(state, restored_kernel, reference.I(1), reference.I(0))
    diagonal = 1/reference.I(2).sqrt()
    diagonal_result = prediction(state, restored_kernel, diagonal, diagonal)
    if not e1.lo > reference.D('1e-4'):
        raise ArithmeticError('prediction signal gate failed')
    if not diagonal_result.lo <= 0 <= diagonal_result.hi:
        raise ArithmeticError('whole-circle symmetry check failed')
    if not ref['pass']:
        raise ArithmeticError('paired motion/reference gate failed')
    sources = {}
    for module in (reference, circle):
        p = Path(module.__file__)
        sources[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result = dict(status='bounded reference component PASS; full C-H3 incomplete',
        reference=ref, kernel=restored_kernel.record(),
        uniform_prediction_error=str(error), uniform_prediction_error_display=float(error),
        uniform_time_readout_width_upper=str(time_width),
        final_e1_enclosure=e1.record(), diagonal_enclosure=diagonal_result.record(),
        circle_initialization_seconds=circle_seconds,
        elapsed_seconds=time.perf_counter()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        python=platform.python_version(), platform=platform.platform(),
        precision_decimal_digits=reference.getcontext().prec,
        sources=sources,
        checkpoint_sha256=hashlib.sha256((destination/'midpoint_checkpoint.json').read_bytes()).hexdigest(),
        kernel_sha256=hashlib.sha256((destination/'kernel.json').read_bytes()).hexdigest())
    (destination/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if hasattr(os, 'sched_getaffinity'):
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_AS, (8*1024**3, 8*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (890, 890))
    result = reproduce(args.output)
    print(json.dumps({key:result[key] for key in
          ('status','uniform_prediction_error_display','elapsed_seconds','peak_rss_kib')},indent=2))
