"""One-time cache for the existing moments illustration, never a plotting default.

Runs the unchanged deterministic toy producer once on CPU, retaining only
the arrays needed to redraw its figure. This is not a new compression test.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np
from numpy.polynomial import legendre
from threadpoolctl import threadpool_limits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    root = Path(__file__).resolve().parents[2]
    source = root / 'paper/scripts/tikz_figures.py'
    spec = importlib.util.spec_from_file_location('paper_moments_source', source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    captured = {}

    def capture(frame, event, result):
        if event == 'return' and frame.f_code is module.moments.__code__:
            captured.update(frame.f_locals)

    started = time.monotonic()
    with threadpool_limits(limits=1):
        sys.setprofile(capture)
        try:
            module.moments()
        finally:
            sys.setprofile(None)
    _, history, halfway = captured['rows'][0]
    selected = np.asarray(captured['picks'][0])
    x = np.linspace(-1, 1, len(history))
    fits, errors = [], []
    for order in (1, 2, 3):
        fitted = legendre.legval(x, legendre.legfit(x, history, order-1)).T
        fits.append(fitted[:, selected])
        errors.append(np.median(np.sqrt(np.mean((fitted-history)**2, axis=0)) /
                                np.maximum(np.ptp(history, axis=0), 1e-12)))
    metadata = dict(source=str(source.relative_to(root)),
                    source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                    seed=3, width=512, training_samples=8, dimension=2,
                    euler_step=0.05, steps=8000, nonzero_random_readout=True,
                    seconds=time.monotonic()-started,
                    scope='Existing illustrative reconstruction, not canonical theorem validation')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.output, histories=history[:, selected], fits=np.asarray(fits),
                        median_errors=np.asarray(errors), selected_neurons=selected,
                        coefficients=legendre.legfit(x, history, 2),
                        halfway_coefficients=legendre.legfit(x, halfway, 2),
                        metadata_json=np.asarray(json.dumps(metadata)))
    print(json.dumps(dict(output=str(args.output), **metadata)), flush=True)


if __name__ == '__main__':
    main()
