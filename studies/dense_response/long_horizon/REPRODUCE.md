# Reproduction details

## Reference environment

- Python 3.12
- NumPy 2.3.5
- Matplotlib 3.10.8
- IEEE float64
- one BLAS thread

The exact environment and BLAS build are written to
`metadata/environment.json` at run time.

## Commands

```bash
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MPLCONFIGDIR="${TMPDIR:-/tmp}/dense_mup_mpl"

python -m unittest discover -s tests -v
python run_all.py --config config/protocol.json
python make_manifest.py
```

## Determinism

Every run uses NumPy's `default_rng` with a stored integer seed. Initial
draw order is \(B\), then the full \(W\) stack, then \(a\), matching the
corrected original audit. Fixed-step RK4 and a fixed sample grid avoid
adaptive-solver event-order differences. BLAS reductions can differ in the
last bits across hardware; the included refinement traces quantify timestep
sensitivity in the recorded reference environment, not cross-hardware
variability.

## Raw trace schema

Each compressed NPZ contains:

- `times`, `method_labels`, and response `orders`;
- output, loss, residual norm, and analytic output/loss speeds;
- every \(3\times3\) Gram at every depth node and its analytic derivative;
- reconstructed tangent kernels and minimum eigenvalues;
- the defect in \(\dot f+\widehat\Theta e\);
- forward, adjoint, and terminal constraint defects;
- instantaneous exact-snapshot \(q/r\) derivative errors;
- a JSON metadata scalar with model class, surrogate class, config/source
  hashes, solver, parameters, seed, and the explicit flag
  `actual_compiled_liouville_pde_run=false`.

Load without pickle:

```python
import json
import numpy as np

with np.load("results/raw/<run>.npz", allow_pickle=False) as z:
    metadata = json.loads(str(z["metadata_json"]))
    times = z["times"]
    grams = z["grams"]
```

## Verification

After reproduction, from the bundle root:

```bash
sha256sum -c metadata/SHA256SUMS
```
