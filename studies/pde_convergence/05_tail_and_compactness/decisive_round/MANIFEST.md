# Final compactness round manifest

## Primary files

- `../PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`: theory/evidence synthesis.
- `coupled_cauchy_ledger.py`: one-run diagnostic wrapper.
- `coupled_cauchy_ledger_seed23.json`: complete numerical ledger.

## Exact command

```bash
OMP_NUM_THREADS=1 \
OPENBLAS_NUM_THREADS=1 \
MKL_NUM_THREADS=1 \
NUMEXPR_NUM_THREADS=1 \
python decisive_round/coupled_cauchy_ledger.py \
  --seed 20260723 \
  --N 1 \
  --R 512 \
  --base-order 8 \
  --dt 0.025 \
  --checkpoints 0.125,0.25 \
  --output decisive_round/coupled_cauchy_ledger_seed23.json
```

The wrapper imports the unchanged canonical operator PDE and the prior
parity-reduced quadrature/stepper. The final bundle includes those source
dependencies and the frozen protocol.

## Integrity

- protocol:
  `8b3f6a9ce80575f675454a5ebff63c33e347b28d33a77e0442a4385209eda1fd`
- runner:
  `a12715d02987b0bbb7380e5f7ae35f1a673d58e01a930eefcdaeca8636f96085`
- result:
  `fc5a88c0e65f6142ae202bc5d96f5049616fc8ecaf944c4ef5fee71d30dddc40`

The admissible run used 211.036 seconds of wall time. No degree-nine,
second-seed, refinement, or post-result scientific branch was run.
