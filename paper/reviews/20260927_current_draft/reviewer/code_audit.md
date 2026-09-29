# Code and stored-evidence audit

This is an audit of the frozen **paper-only packet**. It is not a claim that unprovided dependencies are absent from the repository or a prospective release. No training was run and no study path referenced by the code was followed.

## Static map and safety

| File | Function | Coverage |
|---|---|---|
| `figures/frozen_ntk.py` | Reconstruct seeded two-hidden-layer tanh initialization; derive all mobility-weighted kernel blocks; solve frozen flow analytically; write predictions/manifest | Entire file read. Only safe pure helpers imported for an independent tiny finite-difference check. Main not executed. |
| `figures/learning_controls.py` | Assemble five dense/P3/factor endpoints and construct matched NTKs | Entire file read. Its study-owned metric and factor-array dependencies are outside the packet; main not executed. |
| `figures/capture_trajectory.py` | Replay dense and lifted response-memory models at 39 physical times with two Heun tolerances | Entire file read. `load_legacy` reads/executes two hash-checked modules from an unprovided archive. No import/execution of this file or those modules. |
| `scripts/tikz_figures.py` | Render figures from bundles; fixed same-rank values; toy clocks; small training run for the moments illustration | Entire file read. No builder executed, because the default entry point includes training and writes figure outputs. Inspected scaling/metrics statically. |
| Five `.npz` files | Frozen raw predictions, kernels, test cross-kernels, metadata | Loaded with `allow_pickle=False`; metric and spectral checks described below. |

No malicious network or credential access was seen in these scripts. The trajectory main function queries Git metadata and a CUDA device and invokes training; these actions were not run. No global package installation or shell escalation was attempted. Scientific data and outputs stayed within the assignment boundary.

## Agreement with equations and experimental protocol

**Frozen NTK.** `frozen_ntk.py:44–59` implements tanh forward/backward responses and the three kernel terms. The first-layer, internal-matrix and readout factors are respectively `1/n`, `1/n^2` and `1/n`, exactly as obtained from output `w^T h/n` and mobilities `(n,1,n)`. Inputs in these circle arrays are the normalized directions used by the forward pass; there is no missing input square-root factor when comparing the code's input convention to the manuscript. All blocks are included, including the very small hidden contributions from the small initialized readout. The spectral flow uses the correct `2/m` for unhalved mean squared loss. There is no ridge regularization or eigenmode truncation; a precision screen fails a run rather than silently changing its model.

**Trajectory.** `capture_trajectory.py:90–101` has dense gradients consistent with the same flow. Lines 142–220 use per-model adaptive explicit Heun controllers and preserve common physical checkpoints; lines 292–306 compute differences to the fine dense reference and sum coarse/fine changes for the sensitivity scale. This measures saved-time prediction discrepancies, not the supremum between checkpoints and not parameter error. The renderer presents exactly that distinction. The lifted solver's complete equivalence to the displayed closure cannot be independently checked without the omitted engines.

**Factors.** The endpoint state, seeds, matched loss and rank are present in metadata, and five-task P3 predictions are present. The factor producer is not in this packet. The stated initialization `A=0`, random `B` gives a common physical network. Direct Euclidean factor flow changes the matrix mobility; equal factor-array size therefore does not imply equal training law. The paper makes that limitation explicit and does not claim a comparison to an optimized or universal low-rank method.

**Rendering.** Circle RMS uses original uniform-angle arrays, not the subsampled polylines. `learning_controls_preview` checks metrics and marks any wider NTK radial unit; the rendered p. 14/p. 40 scales are visibly labeled. `trajectory` shades from the plot floor to the sensitivity diagnostic, not around the error as a confidence band. MNIST panels use signed differences in units of `10^-3` and a shared vertical scale. Sphere RMS uses original equal-area arrays and is not computed from interpolation. The same-rank compact chart has manually embedded rounded values consistent with the checked P3 data and metadata.

## Executed checks

Exact command, in the reviewer directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python /home/amir/Codes/PDE/paper/reviews/20260927_current_draft/reviewer/scratch/check_frozen_evidence.py
```

Exit 0; Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0. The script and full JSON output are retained under `scratch/`. No training is hidden in this check. Torch is unavailable, so the source autograd check was replaced by a finite-difference calculation on width 5, four training inputs and three query inputs.

| Check | Observation | Interpretation |
|---|---|---|
| Manifest | Every one of 31 entries matches | Frozen packet integrity confirmed |
| Independent NTK block finite differences | Max absolute error `2.824e-11` | Correct analytic block formula on tested tiny network |
| Five frozen spectral endpoints | MSE `0.001` to rounding; max cross-formula discrepancy `1.756e-8` | Very large output discrepancies are present in the supplied analytic calculation, not an obvious formula bug |
| Five control RMS rows | All reproduced from raw arrays | Main P3 versus factor/NTK endpoint claims supported |
| All shallow/deep circle RMS values | All 30 reproduced | Table 2 values and nonmonotonic small-order behavior supported |
| MNIST | RMS `0.0032475604`, `0.0010844347`, `0.0011992242`; all memory/dense signs coincide | Function agreement supported; no independent data/preprocessing audit |
| Sphere | RMS `0.02193417`, `0.01279610`, `0.00454013` | Supplementary reported trend reproduced from saved outputs |
| 29 factor wins | 29 wins, 28 ratios above 2, 1 excluded | Matches saved aggregate records; raw arrays do not independently establish every one of the 29 comparisons |
| Common-time diagnostics | Recomputed every error and sensitivity array | Correct use of paired checkpoint predictions and refinement differences |
| Joint-clock algebra | Derivative identity max error `2.442e-15` | Confirms cancellation on arbitrary test raw state; not a solver test |

The largest observed RMS at the saved times is `0.0709651`, `0.00587917`, `0.000175201` for P=1,3,7. At 2,16,32 of 38 positive times, respectively, the discrepancy is no larger than the saved coarse/fine sensitivity. The paper acknowledges limited numerical resolution; these observations should not be used to fit an asymptotic rate.

## Findings and limitations

**L4, Minor Point — coefficient/moment convention in Figure 2.** `tikz_figures.py:205–245` starts its illustrative clock at zero, resamples dense histories, and calls `legfit`; lines 315 onward plot distributions of the resulting normalized polynomial coefficients. They are proportional to, but different from, the raw unnormalized moment variables in the theorem, and have no unit-prefix contribution. Caption/axis clarification is sufficient. No effect on the central theorem or endpoint evidence.

**L5, Minor Point — initialization and physical endpoint times should be reported in the text.** `frozen_ntk.py:37–41` initializes readout entries as normal divided by width; Section 3 only calls the readout small. Five frozen fitted times are approximately `5.234e6`, `7.086e7`, `8.857e5`, `3.329e9`, and `553.7`. Their corresponding condition numbers are `5.433e5`, `8.543e6`, `8.543e6`, `2.285e9`, `39.32`. These stored quantities would make the scope of endpoint comparisons clearer without any new computation. They do not make the comparison unfair for its stated endpoint-predictor question.

**Verification limit, not assigned a flaw severity.** Complete response-memory engines, factor producers, data selection/preprocessing for MNIST, the joint-clock 82-configuration sweep, the 1,000-image MNIST run, and frozen-dictionary experiments were not supplied here. There is no independent full training reproduction, seed distribution analysis, or leakage audit of missing pipelines. No leakage was discovered in the supplied evaluation scripts, but the absent data pipeline cannot be certified. Full reproducibility requires those dependencies in whatever eventual release is intended; the current restricted review packet alone does not establish their availability.

No major implementation error or fatal empirical concern was established in the code/data that was available.
