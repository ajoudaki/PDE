# Code and saved-data audit

## Scope and safety

All four supplied Python files were read statically. No submitted training or figure-generation entry point was run. The plotting script's default list includes `moments()`, which trains a network; it was deliberately not invoked. A reviewer-written NumPy script reads only frozen NPZ arrays with `allow_pickle=False` and performs bounded arithmetic. No outside study paths were accessed. Exact command: `python check_saved_evidence.py`, cwd `/home/amir/Codes/PDE/paper/reviews/20260927_current_draft/visionary`, Python 3.10.12/NumPy 1.26.4, exit 0. Output: `saved_evidence_checks.json`.

## Static mapping and consistency

- `figures/frozen_ntk.py:33–55`: initializes the same two-layer tanh network and evaluates its three mobility-weighted kernel blocks. The factors `1/n`, `1/n²`, `1/n` are consistent with mobilities `(n,1,n)` and readout `wᵀh/n`. `formula_check()` contains an independent autograd comparison, but that check was not rerun here because Torch is unavailable.
- `figures/frozen_ntk.py:111–185`: solves the frozen flow spectrally, bisects the threshold time, includes all resolved modes, and computes 8,192-query predictions in chunks. No ridge tuning or test-label selection is present in the inspected path. Saved results permit direct reconstruction without executing the full-width kernel build.
- `figures/capture_trajectory.py:33,57–69,240`: the actual closure implementation is loaded from two hash-checked modules in an external archived ZIP. The wrapper's dense gradient formula is consistent with the paper. Its error controllers, accepted/rejected steps, shared checkpoint schedule, and coarse/fine sensitivity computation are explicit. The method uses lifted activation state; the source records report a small activation drift, but equivalence to the paper's raw memory ODE cannot be audited without the underlying engines.
- `figures/learning_controls.py:26,91–118`: uses supplied endpoint predictions plus external factor-analysis records and arrays, computes the canonical kernel, and checks the exact antipodal quotient. Factor optimizers themselves are absent from this packet.
- `scripts/tikz_figures.py:188–235,313`: the explanatory moments panel fits normalized polynomial coefficients; it is not a closure rollout. This matches the caption's post-hoc qualification but calls for a coefficient/moment notation clarification (L6).
- `scripts/tikz_figures.py:493–550`: the trajectory panel uses saved common times and separates coarse/fine sensitivity from measured error.
- `scripts/tikz_figures.py:732–791`: controls check saved metrics and explicitly rescale the NTK output, preserving signed original units and avoiding negative radial folding. Visual inspection confirms scale annotations.
- The factor summary includes a valid-run filter and marks limited numerical precision. Its fixed TikZ numbers are consistent with supplied records for displayed cases. There is no basis here for a claim of broad hyperparameter fairness against all low-rank methods; the paper correctly limits the control to one Euclidean factor-flow family and two factor seeds.

## Executed observations

| Check | Observed result | Interpretation |
|---|---|---|
| File integrity | All 31 declared hashes match | Packet is internally consistent |
| Circle RMS, all ten task/depth cases | Reproduces Table 2 rounding | Reported endpoint metrics supported |
| MNIST, 100 images | 0.00324756, 0.00108443, 0.00119922 | Supports reported prediction fidelity; P=3 is slightly worse than P=2 |
| Sphere | 0.0219342, 0.0127961, 0.00454013 | Supports the single saved ReLU endpoint example |
| Trajectory arrays | 39 shared times; RMS and sensitivity recompute | Genuine shared-time array structure; no between-checkpoint certificate |
| Max shared-time RMS for P=1,3,7 | 0.0709651, 0.00587917, 0.000175201 | Strong order-dependent tracking illustration on this task |
| P=7 above sensitivity | 6 of 38 positive times | Many tiny discrepancies are numerically unresolved; paper acknowledges this |
| Five control tasks | All RMS values reproduce | Strong matched-target fidelity differences in saved predictions |
| Frozen prediction reconstruction | Max absolute difference 3.73e-9 | Saved kernels, coefficients and predictions are mutually consistent |
| Factor summary metadata | 29/29 wins; 28 ratios above two | Verifies summary aggregation, not original factor training |

## Issues and limitations

**L3 — Minor Point, static plus executed evidence.** `main.tex:315` says only that the stored readout is small, whereas `frozen_ntk.py:33–37` uses component standard deviation `1/n`. This makes the initial frozen kernel overwhelmingly readout-driven. Existing control metadata also shows very long frozen fit times; the quadrant-alternating time is approximately 70.9 million against memory 244.2. The comparison is legitimate for its declared fidelity target and fitted-endpoint protocol. Giving these values would make its meaning clearer and prevent readers from confusing it with a generic kernel-method comparison.

**L6 — Minor Point, static and visual evidence.** `tikz_figures.py:225,313` plots `c_k=(2k+1)\bar h_k/tau`, not the raw stored `\bar h_k`. The figure's population interpretation is sound, but the plotted objects should be named precisely.

**Packet coverage limit, no adverse repository finding.** Missing underlying trainers, full sweep records, and the 1,000-image MNIST source prevent independent reproduction of those claims in this review. The intentionally paper-only packet does not establish that the repository or eventual release lacks them. For a distributable reproducibility package, include a portable engine/configuration manifest and distinguish rendering saved predictions from replaying training.

No fatal empirical concern or demonstrated metric error was found. Training-label leakage into query predictions is the intended supervised flow; the reported metric is discrepancy from the dense predictor, not unseen-label accuracy. Multiple tasks sharing one network initialization do not establish across-initialization statistical robustness, but the paper does not claim a population empirical confidence interval.
