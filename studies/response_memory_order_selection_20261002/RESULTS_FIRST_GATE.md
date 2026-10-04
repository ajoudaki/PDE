# First feature-competition gate: inconclusive witness

The preregistered first seed failed the feature-competition gate. Training learned a shortcut and moved the hidden features, but did not acquire useful invariant prediction on the zero-shortcut probe. The producer stopped before any ordering intervention, ordinary-rival forecast, response-memory computation or additional seed. This is not a negative result about data-order effects or response memory.

## What was run

The paper's bias-free network with two tanh hidden layers, width512, canonical mobilities(n,1,n), Gaussian initialization and zero readout was trained by2560 actual SGD steps of size0.01 with batches of64. This is the fixed128-epoch mixed prefix on1280 examples, at physical step time25.6. Exactly1152 majority and128 minority examples gave an accessible shortcut s=e*y+0.1*epsilon. The invariant label was y=tanh(z1*z2*z3), with independent Gaussian signal coordinates; its population linear Hermite component vanishes. The16 input coordinates also included12 independent nuisance coordinates.

The shifted test distribution preserved the shortcut marginal and broke only its association with the label. The separate zero-shortcut diagnostic set s=0 and retained the signal and nuisance coordinates. The label second moment V_y=E[y^2] estimated on8192 held-out examples was0.195001989603.

| Measured quantity | Absolute value | Divided by V_y |
|---|---:|---:|
| Training MSE |0.116575613618|0.597817560|
| Shifted test MSE |0.219975173473|1.128066303|
| Zero-shortcut MSE |0.195424407721|1.002166225|
| Shortcut replacement sensitivity E[(f(x)-f(x with s replaced))^2] |0.046881794930|0.240417008|

Hidden activation changes from initialization had RMS0.06318564 and0.10158651 in the two layers, exceeding the required0.05 in at least one layer. Shortcut sensitivity exceeded the required0.1 V_y. The invariant-prediction gate required zero-shortcut MSE below0.95 V_y; its observed1.00217 V_y failed. The zero predictor's risk is exactly V_y for this squared-error metric, so the diagnostic was essentially at that baseline.

All recorded values and parameters were finite. Final parameter RMS values were1.0033060,0.0443017 and1.1218176 for the first matrix, hidden matrix and readout, below the validity cap100. Maximum observed per-coordinate update RMS at epoch endpoints was0.00051363,0.0000025211 and0.00179205 respectively. These are sampled update diagnostics, not a bound over every update.

## Numerical and provenance checks

Manual canonical-mobility gradients agreed with float64 automatic differentiation to relative error1.49468e-16. Analytic directional derivatives of the batch field agreed with centered finite differences to4.37069e-11. Both passed the preregistered tolerances. Scientific execution used float32 and disabled TF32; its reference process is raw SGD, so there is no claim of gradient-flow discretization accuracy.

The exact command was:

```bash
CUDA_VISIBLE_DEVICES=0 /home/amir/miniconda3/bin/python studies/response_memory_order_selection_20261002/run_order_gate.py --seed 101 > data/generated/response_memory_order_selection_20261002/seed_101_stdout.log 2>&1
```

Environment: PyTorch2.9.0+cu130 onGPU0, NVIDIA GeForce RTX3090. The producer's measured elapsed time at stopping was1.7221seconds; this excludes interpreter startup and is not a GPU-utilization measurement. There was one scientific GPU process and it finished within one minute of launch, well within the20-minute process and30-minute wall caps. The CPU derivative-check invocation preceded scientific execution.

Producer SHA256:
`52ac8ced99bf4dc093f229859d93ee930443ed768ddd04538e01e7fd455e7eed`

Protocol SHA256:
`85ac816374eee5609ce1b0ddf5aa21adc32961da6c8b08eb065421d87f8c10f1`

Raw products under `/home/amir/Codes/PDE/data/generated/response_memory_order_selection_20261002/` include `derivative_checks.json`, `seed_101_stdout.log`, and, in `seed_101/`, the complete fixed data and schedules, initialized-exposure environment record, every-prefix-epoch metrics, final prefix weights and `summary.json`. The environment record preserves both source hashes. The producer and protocol are study-owned; no shared code, book, paper or Git index was modified.

## Scientific consequence and stop

The result shows why hidden movement alone is an inadequate feature-competition gate: here it accompanied shortcut acquisition without measurable useful invariant prediction. This particular state is unsuitable for the proposed test of which of two useful representations survives ordering. The order effect, matched-loss persistence, narrower-network forecast, moving first-order forecast, readout-refit rival and fixed-middle-matrix rival all remain untested.

The original question stays open. This trial does not distinguish whether the invariant feature is learned later, whether the shortcut suppresses it throughout this run, or whether the chosen teacher/network/sample configuration is a poor witness. No post-outcome change to prefix length, task, step, width or gate was made, and no additional calculation was launched. A different authorized investigation would need to establish a viable competition regime before investing in history compression.
