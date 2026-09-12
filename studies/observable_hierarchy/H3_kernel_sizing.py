"""Uncertified finite-cost preflight for a reference circle-kernel compiler.

This script performs no trajectory integration and supplies no certificate.
Its only purpose is to select a plausible fixed polynomial degree for a later
rigorous Gaussian-Hermite coefficient calculation.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import time


def main(output):
    start = time.perf_counter()
    import numpy as np
    from scipy.special import roots_hermitenorm
    x, weight = roots_hermitenorm(512)
    weight /= math.sqrt(2*math.pi)
    lower = np.tanh(x)
    q = float(weight @ (lower*lower))
    upper = np.tanh(math.sqrt(q)*x)
    v = float(weight @ (upper*upper))
    prev = np.zeros_like(x)
    current = np.ones_like(x)
    alpha, beta = [], []
    for n in range(64):
        alpha.append(float(weight @ (lower*current))**2)
        beta.append(float(weight @ (upper*current))**2)
        prev, current = current, (x*current-math.sqrt(n)*prev)/math.sqrt(n+1)
    result = dict(status='UNCERTIFIED sizing only; no GF certificate',
                  quadrature='512-node floating Gauss-Hermite',
                  q=q, v=v,
                  degrees=[dict(degree=n,
                      lower_tail_estimate=q-sum(alpha[:n+1]),
                      upper_tail_estimate=v-sum(beta[:n+1]),
                      uniform_prediction_tail_estimate_at_T=
                          .01*(q+v-sum(alpha[:n+1])-sum(beta[:n+1])))
                      for n in [7, 15, 31, 63]],
                  runtime_seconds=time.perf_counter()-start,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  python=platform.python_version(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    destination = Path(output)
    destination.mkdir(parents=True, exist_ok=False)
    (destination/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    main(parser.parse_args().output)
