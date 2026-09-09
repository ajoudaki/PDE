# Reproduction details

## Reference environment

- Python 3.12
- NumPy 2.3.5
- Matplotlib 3.10.8
- IEEE float64
- one BLAS thread

The exact environment and BLAS build are written to
`metadata/environment.json` under the selected generated run directory at run time.

## Commands

```bash
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MPLCONFIGDIR="${TMPDIR:-/tmp}/dense_mup_mpl"

python -m unittest discover -s tests -v
python run_all.py --config config/protocol.json
python make_manifest.py
python make_manifest.py --verify
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

The default run directory is repository
`data/generated/resnet_dense_long_horizon/`. The example below is run from this
study directory. If using `--output-root`, select that same root here and in
both manifest commands.

```python
import json
import numpy as np
from pathlib import Path

run_root = Path("../../data/generated/resnet_dense_long_horizon").resolve()
with np.load(run_root / "results/raw/<run>.npz", allow_pickle=False) as z:
    metadata = json.loads(str(z["metadata_json"]))
    times = z["times"]
    grams = z["grams"]
```

## Verification

After reproduction, from the study root, verify the newly generated manifest:

```bash
python make_manifest.py --verify
```

For a selected run, add the same `--output-root /absolute/path/to/run` used by
the producer. Verification is read-only and resolves schema-2 `source` and
`run` roots from the selected `metadata/manifest.json`, checking the companion
`SHA256SUMS` too. Its virtual prefixes are not physical paths relative to the
source directory. The retained source-side historical seal is not modified or
used to certify a new run. These checks verify recorded bytes, not scientific
correctness or cross-environment equality of newly generated arrays.
