# Scoped verification of the PCA98 continuation

Complete inputs read: `P1_INITIALIZATION.py`, `P1_ENGINE.py`,
`NETWORK_ENGINE.py`, `INITIALIZATION_THEORY.md`, and `MODEL_SCOPE_CHECK.md`.
The scope is the existing fixed-p=1 experiment with a train-fitted centered
PCA representation, nominal P=n4096, and no whitening or row renormalization.
No GPU training is performed by this reviewer.

**Varying input lengths require no model or initializer change.** For any
finite input row u, both engines form tanh(w dot u); their displayed
gradients include the actual u and impose no unit-length identity. At
Gaussian initialization, Var(g dot u)=||u||², so varying PCA-score lengths
already induce the appropriate varying preactivation scale. The first-layer
physical metric remains the same when the new input row is interpreted as
U'=x'/sqrt(k), where k is the retained dimension.

Feed U'=(U-mean_train)V_k directly. Equivalently, declare x'=sqrt(k)U'.
There is no extra sqrt(784/k) factor. Whitening, per-row normalization, or
rescaling to force unit variance would define a different representation.
Centered scores are allowed to have length zero, below one, or above one;
the proof does not require a uniform unit-ball bound.

The dictionary's h_i=tanh(g dot e_i) and corresponding upper/reverse probes
are features anchored at the coordinate directions e_i. They are not
moments of the training inputs. The constants v,tau,alpha and the ridge
1/4096 therefore stay unchanged when the data law becomes anisotropic or
has varying norms. Initializing the same dictionary at dimension k is
legitimate; fitting its Gaussian constants to empirical PCA-coordinate
variances would change the construction. The dense evolving M remains
unrestricted. Sign folding holds for every input row and label, including
nonunit inputs, and requires no symmetry of the data law.

This establishes legality of the finite formulas. Centering, projection,
and the changed coordinate dictionary can change the learned function and
the approximation gap. Retaining 98% of centered training variance does
not certify preservation of individual predictions or fixed-p=1 closure
accuracy. The PCA closure should be compared with its own PCA network
reference, then the measured fidelity/time/memory can be compared with the
original 784-coordinate experiment at matching physical times.

Critical bounded checks are: one small arbitrary-norm physical-gradient,
blocking, and folding check; fresh seed1729 half-step controls through the
actual main horizon for both models; direct replay of saved endpoint
weights; and independent same-time metrics over the identical validation
IDs. Existing step sizes are candidates until the PCA controls pass. The
existing RMS<=0.002 and accuracy-difference<=0.2 percentage-point numerical
gate can be retained, with all recorded times and endpoint sign changes
reported. Late float64 probes diagnose local arithmetic only.

Timing should distinguish integration time, whole training time, and the
one-time CPU PCA fit/transformation. Compare equal physical horizons and
the same GPU/step/block/dtype settings, or retain the device caveat. Peak
allocated training memory keeps the existing definition; PCA preprocessing
memory and disk artifacts are separate costs. A smaller d reduces the
closure's d-by-2d moving matrix; the network's n-by-n middle matrix remains.

Runner/data integration and completed-run evidence are recorded below.
Generated evidence is retained under
`data/generated/first_order_dimension_mnist/pca_checks/`.

The bounded arbitrary-norm check passes in float64 on 13 rows with lengths
from zero to two, d5, network width16 and nominal closure P40. It compares
both engines' velocities with independently differentiated physical-metric
losses at nontrivial dense states, full versus blocked sums, the two closure
contraction orders, and folded/unfolded predictions and a Heun step. Maximum
discrepancy is 5.56e-17; inactive constant entries remain roundoff-zero.
Evidence: `nonunit_input_algebra.json`. This is a small formula check, not
a scientific training run or an accuracy result.

`RUN.py`, `PCA_BATCH.py`, and `PCA_PLAN.md` were read completely. The runner
loads the explicitly selected prepared dataset, infers d from its training
array, performs no rescaling, and loads test data from the same path only
after checkpoint selection. The engine/initializer files remain unchanged.
The new cumulative integration-time field records the already accumulated
step timer and introduces no additional GPU computation. The PCA dispatcher
uses the fixed T600 protocol and the crossed T100 benchmark, verifies
completed horizons, and requires the independent two-model half-step gate
before the remaining seeds. The PCA fit and data transformation remain the
separate data contributor's check.

The prepared PCA inputs have dimension240. All eight T100 benchmark
artifacts pass independent settings, actual checkpoint-shape, source-byte,
dataset-hash, GPU-crossover, and analytic memory-count checks. Every saved
observation array is bitwise identical between repetitions for each
representation/model. Evidence: `benchmark_inputs.json`. Measured training
peaks are 756.957/659.070 MiB for original/PCA networks and 278.419/130.520
MiB for original/PCA closures. These benchmark checks alone make no new
prediction-accuracy or time-step-accuracy claim.

`PCA_ANALYZE.py` was read completely. Its T600 and nearest-training-loss
comparisons use the correct same-ID references; all nine seed pairs and
within-class metrics are computed without calibration. A target outside
the saved training-loss range is marked unavailable rather than
extrapolated. The same-representation and total-preprocessing-effect
comparisons are distinct. The author added explicit benchmark settings,
GPU and provenance guards; the independent artifact checks above verify
actual source bytes and repeat equivalence for the completed runs.
Matched-loss rows currently carry no measured integration time, so timing
claims must retain their actual T100 or full-T600 workload definition.

**PCA numerical gate PASS.** `halfstep_gate.json` was published only after
both seed1729 controls completed T600. Every one of the 61 saved times
passes the stated RMS/accuracy thresholds. Exact full horizons, step counts,
float32/TF32-off settings, dataset hashes, labels, and frozen core source
bytes were verified before publishing the top-level `passed=true` flag.

| Half-step comparison | Network | Closure |
|---|---:|---:|
| T600 validation RMS | 8.46192369e-6 | 3.38937025e-6 |
| T600 maximum absolute difference | 5.29289246e-5 | 3.39150429e-5 |
| T600 prediction-sign changes | 0 | 0 |
| T600 accuracy change in percentage points | 0 | 0 |
| Largest RMS over all 61 saved times | 4.69212274e-4 | 1.10302571e-4 |

Both models also have zero sign and accuracy changes at every saved time.
Direct checkpoint replay passes all six PCA main runs and both half-step
controls, with maximum prediction discrepancy 1.13530e-6 and no sign
changes. All six main trajectories finish T600. The independent replay
evaluates selected and final train/validation/test outputs, hidden Grams,
and recorded movement from the saved finite weights, using each run's
recorded PCA dataset path and hash. `replay/complete_summary.json` collects
all eight results; no trajectory was retrained by this reviewer.

The added common-training-loss diagnostic was also read completely. It
sets one target equal to the largest individual terminal training MSE over
all twelve original/PCA network/closure runs, checks availability, and
selects each run's nearest recorded training-loss snapshot. Both candidate
and reference times move in this diagnostic. It is distinct from matching
to a fixed T600 reference and from equal-time comparison. No validation
output is used to select those times.

**Full scientific-analysis and export audit PASS.**
`pca_analysis_001` agrees with independent recomputation of 5,607 scalar
metrics; the largest discrepancy is 3.20e-14. This includes all four T600
and fixed-reference loss comparisons, all twelve common-loss choices,
four common-loss comparisons, every set of nine individual seed pairs,
within-class metrics, and post-selection validation metrics. All exported
NPZ arrays and the 38-column per-image CSV match the source observations
exactly. Dataset hashes, the same 1000 unique validation IDs/labels, and
retained analysis-source snapshots were checked.

The common target is 0.011080311898. Selected original-network times are
460/460/460; original-closure times are 300/290/290; PCA-network times are
600/600/600; PCA-closure times are 570/570/570. Targets outside a trajectory's
saved loss range are correctly reported unavailable in the separate
fixed-reference comparison. Evidence: `primary_analysis_audit.json`.

At equal T600, mean individual closure RMS against its own representation's
network mean is 0.0528773 for original inputs and 0.0405999 for PCA. At
the common training-loss diagnostic those values are 0.0431777 and
0.0416288. PCA closure and PCA network differ from the original network
mean by RMS 0.105314 and 0.0975023 respectively at the common-loss
snapshots. Thus the verified same-input approximation result should remain
distinct from preservation of the original network's predictions.

No unresolved implementation or arithmetic issue remains within this
scoped check. These are internally verified finite-p=1 results; the
half-step runs are numerical controls, not full-horizon same-step bitwise
reruns or a convergence guarantee. Timing-table aggregation and PCA
fit/data checks have their separate assigned reviews.
