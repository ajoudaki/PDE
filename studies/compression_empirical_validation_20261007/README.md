# Empirical validation of response compression

## Scope and claim level

New empirical investigation requested on 2026-10-07. The scientific inputs are
the current `paper/` manuscript, its self-contained integrated appendix, and its
capture/plotting scripts. No other study supplies scientific inputs. The single
implementation is `paper/figures/capture_trajectory.py`; generated records go in
fresh `data/generated/compression_empirical_validation_20261007/<run>/` folders.
This is not a promotion to the established book.

The question is whether practical versions of the stated Harmonic and
Logarithmic mechanisms have small retained state while matching unseen-input
dense trajectories at the scale of independently measured dense variability.
No finite experiment proves a width asymptotic, a supremum over the sphere,
an infinite-time statement, or a theorem outside its assumptions. Empirical
orders do not need to satisfy conservative sufficient constants. An algorithm
that changes the closure mechanism must be named and distinguished explicitly.

## Preregistered protocol (before new numerical results)

- Dense reference: two hidden tanh layers initially; unit input directions;
  Gaussian first weights of variance one, Gaussian hidden entries of variance
  `1/n`, zero stored readout, prediction `w.T @ h / n`, mean squared loss and
  block mobilities `(n, 1, n)`. Label RMS is order one, not reduced using the
  theorem's small-label sufficient condition. Additional depth is a separate
  recorded configuration.
- Toy directions: circle and spheres in dimensions 3, 5 and 10. Training
  inputs and passive setup quadrature inputs are separate from test inputs.
  No test labels or test prediction errors enter source construction.
- Primary metric: maximum, over a common finite list of physical times, of
  unseen-input prediction RMS against the dense reference. Also retain the
  entire RMS curve, endpoint error, training loss and predictive test error.
  Normalize by the same metric for an independent pair of dense runs, not by
  a theorem upper bound. Report individual denominators, not only ratios.
- A practical comparability pass means ratio at most 3, with numerical
  sensitivity at most 10 percent of the dense-pair denominator. A near-zero
  denominator or failed integration makes the comparison inconclusive.
  This factor is an empirical decision threshold, not a probability theorem.
- Harmonic uses its coupled dense source. Also report independent-reference
  fidelity where feasible. Logarithmic must use an independent target dense
  initialization. Never use stored target predictions as a decoder.
- Pilot seeds are 101 and 102; held-out seeds are 201, 202 and 203. Tune sizes,
  spectral orders and solver settings only on pilots. Freeze their rule before
  reporting a held-out scaling experiment. Width candidates are 256, 512, 1024,
  2048 and 4096; run the affordable prefix, report that prefix exactly, and do
  not infer an asymptotic exponent from a narrow or saturated size range.
- Initial common horizons are 0, 0.5, 1, 2, 5, 10 and 20. Longer horizons and
  nonlinear targets may be selected on pilots if initial feature motion is
  negligible; record and freeze that decision before held-out evaluation.
- Controls: frozen initial NTK (at zero readout this is the frozen-feature
  kernel), ordinary smaller Gaussian dense networks, and explicit LoRA
  increments with trained outer layers. Count LoRA's fixed dense mixer
  separately. Match total retained scalars for small-network comparisons and
  moving scalars for the specifically labeled LoRA comparison. Report any
  unavoidable budget mismatch, not an interpolated fictional model.
- Diagnostics: feature displacement, initial-versus-trained kernel change,
  frozen-NTK discrepancy, initialization Gram/isometry defects, readout
  interpolation identity, state inventory, setup time/peak device memory,
  training time and query time/additional memory. These diagnose mechanisms;
  moving weights alone are not evidence against lazy behavior.
- Numerical checks precede scientific runs: dense RHS versus automatic
  differentiation, Harmonic full-retention limit, source-metric identities,
  finite replay consistency, and step/tolerance refinement. Retain failed
  checks and unsuccessful configurations. Float64 is the initial reference;
  a faster precision is admitted only after a recorded comparison.
- Real-data gate: use a small local standard benchmark (initial candidate:
  sklearn handwritten digits, 64 inputs), with a fixed train/test split and
  explicit scalar task. Width 2048 or 4096 is desirable but subject to timing.
  Run only after the toy method and numerical-validity checks pass. Do not
  claim classification superiority merely from teacher fidelity.
- Resource limits: toy model run at most 120 seconds, real-data model run at
  most 300 seconds. Initial campaign at most 120 toy model runs and 12 real
  model runs; profile before scaling and stop an unpromising method after two
  failed numerical/mechanism checks until its cause is understood. Use both
  GPUs for independent configurations; no oversubscription. Wall-time caps
  include synchronization and record failures/partial progress. Setup must be
  charged separately and must not be silently excluded from efficiency.
- Each fresh run records configuration, source hash, package/device versions,
  seeds, actual orders, timings and failures. Generated arrays are not Git
  source. Paper figures are selected only after results, favoring scaling with
  matched controls; unsuccessful or missing tests remain documented.

## Environment and progress

The ordinary sandbox cannot access CUDA. Host execution has two RTX 3090 GPUs
and `/home/amir/miniconda3/bin/python` with PyTorch 2.9.0+cu130. No package
installation was needed. Both GPUs have executed independent pilots.

The single script now contains the exact Harmonic metric/deficit runtime and
an explicitly empirical finite-program Logarithmic backend. Harmonic setup uses
an offline dense RK4 rollout through the whole reported horizon, passive-node
Chebyshev/spherical-polynomial fitting, and optional per-family SVD truncation
before paired initialized-mixer images are formed. Mandatory initialization
directions, the BSS selector and its full positive metrics are retained. This
does not demonstrate the certified initializer's practical setup speedup.

Logarithmic uses float64, an ordinary counter PRNG, Euler panels, one ensemble
member and full numerical-rank selection. It preserves both Gaussian
orientations, covariance corrections, immutable field definitions, causal
selected-metric replay and full empirical passive-query reductions. It does
not instantiate the theorem's bit precision, space-PRG or probability
certificate. Its width is measured, never prescribed as a small network.

`checks_complete_01` records reproducible checks: dense and LoRA gradients,
Harmonic source isometry/initialization/paired actions, the corrected-readout
constraint and full-width dense limit, plus Logarithmic Gaussian posterior,
source/replay, row regeneration and passive-query identities. Errors are below
2e-15 for the Harmonic geometric identities and below 1e-14 for the Gaussian
posterior check. The full-width Harmonic trajectory discrepancy decreases by
about sixteen under RK4 step halving.

Initial pilots show substantial dense-versus-frozen-feature discrepancies.
The first LoRA step of 0.125 was numerically unresolved; those runs are retained
but must not support a control claim. The circle rerun at step 0.005 versus
0.0025 resolves the LoRA comparison (sensitivity below 5e-9).

The Harmonic circle pilot at width 4096 and per-family source rank eight misses
the factor-three threshold (ratio 3.47). Increasing to rank sixteen, temporal
degree five and circle degree nine gives ratio 1.32 with about 1.07 million
retained scalars versus 16.79 million dense parameters. This is pilot evidence,
not a held-out result. Matched-size ordinary networks also pass several pilots;
superiority over them is not presumed. Higher-dimensional pilots d=5 and d=10
also pass the practical threshold at their tested budgets.

### Frozen confirmation rule, after pilots and before held-out runs

For the circle, use per-family rank `ceil(2*log(e*n))`, temporal degree five,
circle degree nine, nine time nodes and 64 passive spatial nodes. For d=3,5,10,
use per-family rank `ceil(log(e*n))`, temporal degree three, spatial degree
three, nine time nodes and 128 passive spatial nodes. BSS determines actual
selected widths; a cap below n prevents silently calling full retention
compression. The fit horizon is 20, labels have RMS one, RK4 steps are 0.125
and 0.0625, and test inputs are not setup nodes. These are practical rules, not
optimized or certified asymptotic exponents.

Confirmation plan: circle widths 1024, 2048, 4096 with seeds 201,202,203; d=3,5,10
at width 2048 with seed 201; the latter are explicitly single-seed dimension
checks. Every run includes its dense pair, frozen NTK and total-state-matched
ordinary network. This raises the capped campaign allowance to 200 toy model
runs (including refinements), justified by measured sub-ten-second dense runs;
per-model time caps are unchanged. No held-out seed has yet informed this rule.

Real digits has a separate fixed 64-image tuning-query partition; all remaining
held-out images are reserved for confirmation. PCA is fitted on training data
only. No raw-pixel or classification-superiority claim follows automatically.

Existing archived Legendre capture remains unchanged and the new validation
path does not import other-study code.

### Campaign accounting update

The first implementation checkpoint is `fefd944`. Both methods' algebra and
mechanism were independently checked against the paper's explicit equations.
Subsequent changes add causal Logarithmic trajectory observations, remove unused
Harmonic caches, separate inference readout refresh, and improve accounting.

At the next accounting pass there were 222 recorded model executions including
source construction, with approximately 606 seconds of recorded solver work.
The earlier 200-execution allowance underestimated refinements and source
rollouts; this overrun is recorded rather than retroactively hidden. The final
campaign is now capped at 320 executions including those items, to complete
matched LoRA, real-data confirmation and dimensional Logarithmic checks. All
per-model time caps remain unchanged. No additional tuning grid is authorized
by this bookkeeping update; the already frozen Harmonic rules stay frozen.

Circle confirmation passed all nine width/seed configurations. At width 4096,
the three runs use roughly 11.7--11.8 times fewer model-tensor scalars than the
dense reference, with variability ratios 0.159, 1.617 and 0.505. The matched
ordinary networks have ratios 0.506, 2.640 and 3.232. This is not a uniform
ordering: Harmonic loses to the matched network in two lower-width runs.

Single-seed d=3,5,10 Harmonic checks also pass. The first real digits pilot
passes but does not improve classification accuracy over the controls. The
first d=5 Logarithmic trajectory pilot passes fidelity, but its 2.63 million
retained words exceed the width-1024 dense model's 1.05 million parameters.
Fidelity alone is therefore not a compression success. Wider runs must count
the full state and query workspace before a compression claim is made.

Digits confirmation is frozen at width 4096, 32 training images, training-only
PCA dimension eight, source rank 19 per family, time degree five, spatial
degree three, nine temporal nodes and 256 passive sphere nodes; horizon 20 and
the same RK4 refinement. Seeds 201,202,203 use only the held-out query partition.
The pilot's rank-19 model passes fidelity but does not beat the matched ordinary
network or improve classification accuracy; confirmation will retain that
comparison whether favorable or unfavorable.

Logarithmic query evaluation has been algebraically batched: each unseen input
keeps its own conditional coefficients, while all inputs reuse the same two
or three row-regeneration passes. Tests agree with independent single-query
execution below 2e-16. Batching does not condition queries on one another or
change training. Reported workspace now includes the batch, and total query
work is not a single-input latency measurement.

Logarithmic confirmation now freezes ten Euler panels of length 0.5 through
time five, observation noise 0.01, one source member, and 32 passive queries.
This follows the d=10 pilot: twenty panels exceeded the 120-second cap, while
ten panels passed with ratio 1.62 and roughly 6.2-fold persistent-payload
savings at width 4096. This failed 20-panel run remains in the ledger. Orders
are not selected on confirmation seeds. Dimension checks use m=max(d,3),
d=2,3,5,10 at width4096 and seed201. Dimension five additionally uses widths
1024 and2048 at seed201 and width4096 at seeds202,203. These limited finite
widths cannot identify an asymptotic exponent. Each successful decoder run
also gets a total-payload-matched dense-network control, with common training
data removed from both model budgets. This final planned batch raises the
execution allowance to 400, including all references, refinements and setup
programs; it adds no theorem search or open-ended tuning.

### Final controls and real-data decoder check

The moving-state-matched LoRA pilot compared mobility multipliers 0.25, 1 and
4 at width 2048. Multiplier 0.25 had the best pilot fidelity and was frozen
before confirmation seed 201. That confirmation has 313,344 moving LoRA
scalars versus Harmonic's 315,481, with a further 4,194,304 fixed LoRA scalars.
Its trajectory discrepancy is 7.51 dense-pair units versus Harmonic's 0.479.
RK4 steps 0.01 and 0.005 resolve the comparison. This is one controlled
factorization/optimizer comparison, not a lower bound for every low-rank model.

A separate Logarithmic digits pilot uses eight training images, training-only
PCA dimension five and horizon five. Ten panels fail the practical threshold
(ratio 3.929); twenty panels of length 0.25 pass on the 64-image tuning split
(ratio 1.989), but use 6,608,623 words versus 16,801,792 dense parameters.
Freeze the latter setting, noise 0.01 and one member for one confirmation at
seed 201 on all 285 held-out images. This is a separate small-data check, not
the 32-training-image Harmonic task. No more tuning follows this confirmation.

The initial twelve-real-execution allowance was exceeded: the accounting
before the last confirmation already included 57 real-data executions
(references, source programs and refinements included). This planning overrun
is recorded explicitly; the later total campaign allowances superseded the
initial split, and no individual real-data model is allowed over 300 seconds.

## Final outcomes and publication selection

No further tuning follows the final confirmation. The scientific campaign contains 399
recorded model/source executions under the accounting convention above,
including 69 real-data executions and separate refinements. Recorded dense,
Harmonic, small-network and LoRA solver work totals about 1,254 seconds;
source assembly and Logarithmic work are additional and recorded separately.
At campaign close there were 52 report files, including check-only and failed/partial records;
driver completion is distinct from every requested method completing.
The failed d=10 twenty-panel decoder stopped at 120.08 seconds: the
deadline is checked between numerical operations, not a hard process kill.

| Frozen confirmation | State result | Fidelity result |
|---|---|---|
| Harmonic circle, three widths and three seeds | 11.7--11.8-fold model-tensor savings at n=4096 | All nine pass; ratios 0.159--1.617 |
| Harmonic d=3,5,10, n=2048, one seed each | 0.63--0.76 million tensor scalars | Ratios 0.751, 0.937, 0.997 |
| Harmonic digits, 32 training images, three seeds | About 4.6-fold tensor savings | Ratios 1.85--2.44; smaller MLP is better in all three |
| Logarithmic d=5, three widths, five cases total | 688,220 persistent words; 24.4-fold saving at n=4096 | All five pass; ratios 0.909--1.781 |
| Logarithmic d=3 and d=10, n=4096, one seed each | About 67-fold and 6.2-fold persistent savings | Ratios 1.84 and 1.26 |
| Logarithmic circle, n=4096 | About 68-fold persistent saving | Fails: ratio 6.95 |
| Logarithmic digits, eight training images, one seed | 6,608,623 words; 2.54-fold saving | Fails: ratio 4.94; matched MLP 3.02 |

The real-data decoder's query envelope raises its numerical payload to
11,052,846 words, with 67.9 seconds for source, metric, replay and all queries.
Its favorable pilot did not carry over to held-out fidelity. That outcome is
not hidden behind its 94.39% classification accuracy. The Harmonic digits
task is separate (32 training images and PCA dimension eight): Harmonic and
dense reach 97.32%, and one matched smaller MLP reaches 97.70%.

The main figure pairs state and fidelity width curves for both methods. The
appendix figure retains the dimension checks, real-data Harmonic curves and
the failed circle decoder. The text reports the LoRA confirmation and real
decoder failure. All pilot/confirmation/failed records, not just plotted
successes, are exported to `paper/figures/compression_validation_source.json`.
Its plots can be regenerated without the generated run folders using the
single script's `plot-validation --bundle` mode.

The evidence supports useful finite-width representations, not a verified
logarithmic asymptotic or universal advantage over small MLPs. Frozen-NTK
discrepancies and the resolved matched-moving-state LoRA failure distinguish
the tested dynamics from those particular controls. Harmonic setup is
teacher-informed and uses a full finite-horizon rollout; no cheap-warmup or
end-to-end speedup is inferred from the smaller retained state. Numerical
payload accounting is not Python/LAPACK process memory.

Final algebra checks in `checks_final_01` pass: dense/LoRA RHS versus autograd,
Harmonic paired metric and full-retention identities, isolated restart and
query permutation, Logarithmic both-orientation Gaussian posterior, explicit
fixed-matrix Euler update, row regeneration, causal replay and batched query
equivalence. A separate scoped audit recomputed all 23 originally plotted
confirmation metrics and accuracies from saved predictions with no mismatch;
its plot-eligibility finding was fixed without dropping failed accuracy cases.
These are internal implementation and measurement audits, not independent
validation of the theoretical proof chain.

Publication figures are in `figures_final_01`. Rerendering solely from the
versioned JSON bundle in `portable_replot_01` produces byte-identical PNGs.
The manuscript build in `paper_build_ByuJlC` has 199 pages and no final LaTeX
warnings, unresolved references or overfull boxes. Main-text figure page 13,
supplementary figure page 18 and the new empirical prose were visually checked;
the checked PDF is copied to `paper/main.pdf`. The theorem modules and static
proof appendix were not changed by this empirical integration.

The closing independent audit also verified the final LoRA and real-decoder
records. Its numerical-gate hardening was applied: both dense references must
be numerically resolved, and decoder refinement uses exactly its sampled
times and queries. Recomputing these stricter checks from all 25 confirmation
arrays changes no outcome; the largest full-grid dense-pair sensitivity is
0.000578 dense-pair units. `checks_driver_final_01` is a separate width-32
functional regression (not a scientific scaling run) covering both gates and
the smaller decoder query subset. The final portable ledger in
`figures_final_02` includes this check, for 53 reports in total. Historical
run reports retain their original gate fields rather than being rewritten.
