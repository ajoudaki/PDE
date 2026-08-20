# Final compactness round manifest

## Primary files

- `COMPACTNESS_REPORT.md`: theory/evidence synthesis.
- `coupled_cauchy_ledger.py`: one-run diagnostic wrapper.
- `results/compactness/coupled_cauchy_ledger_seed23.json`: complete numerical ledger.

## Exact command

```bash
OMP_NUM_THREADS=1 \
OPENBLAS_NUM_THREADS=1 \
MKL_NUM_THREADS=1 \
NUMEXPR_NUM_THREADS=1 \
python coupled_cauchy_ledger.py \
  --seed 20260723 \
  --N 1 \
  --R 512 \
  --base-order 8 \
  --dt 0.025 \
  --checkpoints 0.125,0.25 \
  --output results/compactness/coupled_cauchy_ledger_seed23.json
```

The wrapper imports the unchanged canonical operator PDE and the prior
parity-reduced quadrature/stepper through the two explicit compatibility
links at the convergence-program root. The immutable release in the archive
preserves the original bundled dependency copies.

## Integrity

- protocol:
  `8b3f6a9ce80575f675454a5ebff63c33e347b28d33a77e0442a4385209eda1fd`
- runner:
  `c62f48335e2309bbdf5056a41ca92bbb94e023e2049b35719662c33d1146c819`
- result:
  `fc5a88c0e65f6142ae202bc5d96f5049616fc8ecaf944c4ef5fee71d30dddc40`

The result embeds the original release-runner hash
`a12715d02987b0bbb7380e5f7ae35f1a673d58e01a930eefcdaeca8636f96085`.
The active runner differs only in its local import path after the directory
wrapper was removed; the exact original runner remains in the archived bundle.

The admissible run used 211.036 seconds of wall time. No degree-nine,
second-seed, refinement, or post-result scientific branch was run.
