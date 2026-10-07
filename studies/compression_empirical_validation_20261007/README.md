# Empirical validation of response compression

## Scope and claim level

Current continuation: the raw-image two-update run below is only a short-program
sanity check, not validation of a trained compressed model. The replacement
experiment requires matched, step-refined Euler training to MSE below 0.01.
Its protocol and any infeasible comparisons are recorded at the end of this file;
neither a different integrator nor an early resource stop counts as success.

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

## Requested raw-image, 100-training-image continuation

The user explicitly requested Logarithmic versus dense and total-state-matched
small dense versus dense on raw images with 100 training examples. This
continues the same empirical investigation; it does not reopen the earlier
hyperparameter search or change its conclusions. Use digits 3 versus 8,
all 64 pixels (no PCA or fitted feature reduction), per-image norm scaling,
100 stratified training images and all remaining 257 validation images.
The split seed remains 47, labels are -1/+1, and the reference has two tanh
hidden layers of width 4096. No evaluation image chooses parameters.

Primary quantity is whole-validation prediction RMS at physical time five;
also report the maximum over common saved times. Dense and matched MLP use
RK4 steps 0.125/0.0625. Numerical checks include both dense references and
the matched model; the decoder is compared as its declared Euler program,
not relabeled as a converged gradient-flow discretization. Its source is
independent of the dense target. A useful compression must have smaller total
retained payload; a large-state decoder does not qualify merely by fitting.

Static feasibility check: with m=100,d=64, the source program names
64+2+H*(13*100+64+1)+6*100 fields after H panels. At H=10/20 this is
14,316/27,966 fields, beyond the existing 24-million-value source cache cap
at n=4096. Independently, all Gaussian roots enter full-span selection;
their generic ranks already prevent a small payload at those orders.
These are implementation/witness limitations, not a lower bound on every
Logarithmic construction. Do not silently replace the full-rank selector.

Precommitted resource-feasible attempt: H=2 panels of length 2.5 through the
same time five, noise 0.01, one member, all 257 validation queries, seed201.
This very coarse order is selected for storage/cost, not validation fidelity.
If it completes below the 300-second decoder cap with smaller-than-dense
payload, run H=3 (step 5/3) at the same seed for a disclosed order comparison,
provided static cache and measured resource estimates allow it. Neither
result is chosen by its validation error: both are reported. At most two
such primary configurations plus one numerical implementation retry are
allowed; each model at most 300 seconds, with at most 2 GB CPU source payload
and 20 GB allocated GPU memory. A failed/capped decoder yields no invented
RMS or fictitious matched-small control. Ordinary unit tests are separate.

### Raw-image result (one seed; no claim of useful resolved-flow compression)

`raw_digits_m100_h2_s201` completed. All 257 validation images retain their
64 original pixel coordinates, with independent per-image unit-norm scaling
only. Training has 51 threes and 49 eights. A scoped independent check
reconstructed the split and tensors directly from `load_digits`, checked
disjoint/exhaustive indices and identical inputs across every model, and
recomputed the saved RMS curves and inventories exactly.

At recorded times 0, 2.5 and 5, the results against refined dense dynamics are:

| Model | RMS at t=2.5 | RMS at t=5 (also the recorded maximum) |
|---|---:|---:|
| Independent dense | 0.0071171269 | 0.0169756746 |
| Logarithmic, two Euler panels | 0.0611283200 | 0.2964844318 |
| Total-payload-matched dense, width 3701 | 0.0058247144 | 0.0161433175 |

The selected rank is 1865. The decoder retains 13,951,649 numerical/index
words, including 6,500 common data words. Its matched MLP has 13,937,966
parameters; width 3702 would exceed the model-only budget. Dense has
17,043,456 parameters, so the persistent reduction is only 18.14 percent.
Retained-plus-query workspace is 25,176,147 words, larger than dense parameters.
These payload figures exclude Python/LAPACK overhead and are not process RAM.

The decoder's source, metric, replay and queries took 61.65, 35.31, 60.23 and
47.87 seconds, respectively (205.24 seconds total). Replay error is
1.831e-11; source reconstruction error is 2.620e-13. Dense coarse/fine changes
are 8.003e-7 and 7.812e-7, independently recomputed from arrays. The matched
dense change is reported as 7.522e-7; that run did not save its coarse array,
so the independent archive check cannot reconstruct this last diagnostic.
Future captures now retain both matched-control resolutions.

No H=3 run was launched: scaling the measured source/replay costs predicts
more than the 300-second cap, and its expected full-span payload is larger
than dense. More strongly, at H=10/H=20, scalar-pair history plus immutable
coefficients/instructions alone require 19,972,316/75,903,216 words, already
larger than dense before adding any selected fields or metric. This is a
limitation of the current retained representation at these parameters,
not an impossibility theorem for the compression idea.

The large RMS above is substantially a temporal-discretization effect.
A separate diagnostic used the existing `Dense` and `dense_rhs`, the same
raw tensors, and exactly two Euler steps of length 2.5. At time five:

| Common two-step Euler comparison | Whole-validation RMS |
|---|---:|
| Logarithmic versus dense | 0.0165968613 |
| Matched small dense versus dense | 0.0284335378 |
| Independent dense pair | 0.0191227462 |

The coarse dense model itself differs from the refined trajectory with the
same initialization by 0.3102444868. Thus the decoder tracks this coarse
finite program much better than it tracks resolved gradient flow. The
matched-integrator result is a single-seed diagnostic, not a recovered
resolved-training or useful working-memory compression claim. Both tables
must remain visible together; neither supersedes the other by changing the
reference integrator. Classification is not the RMS observable.

Reproduction of the primary run (use a fresh output name):

```bash
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py validate \
  --device cuda:0 --task digits --raw-images --dimension 64 --samples 100 \
  --tuning-samples 0 --width 4096 --seed 201 --horizon 5 --refine \
  --log-probe --log-steps 2 --log-step 2.5 --log-queries 512 --log-all-times \
  --per-run-seconds 300 --out PATH/TO/FRESH/RUN
```

The numerical control initializes `Dense(4096,64,201,device)`, its independent
copy with seed 10201, and `Dense(3701,64,60201,device)`. Starting from each
`initial_state`, apply `state = [v + 2.5*dv for v,dv in
zip(state, model.rhs(state, train_inputs, train_labels))]` twice, evaluating
`model.predict` on the saved `query_inputs` before and after each step.
Compare those arrays with each other and with `trajectories.npz`'s
`logarithmic` and dense arrays at indices for times 0, 2.5, 5. This diagnostic
uses no alternative implementation of the network or gradient.

An exact implementation cleanup now omits the Gaussian action's duplicate
moment-request prepass for nonstreaming execution; streaming queries retain
it. A scoped before/after test was bit-identical for all source/selected
fields, coefficients, pair values/order, losses and queries. Full algebra
checks pass in `raw_checks_01` and `raw_checks_02`. The recorded 205.24-second
scientific run predates this cleanup; no improved timing is claimed from it.
The paper and its earlier figure bundle were not rewritten by this follow-up.

## Corrected full-training Euler experiment (preregistered)

The user now requires actual substantial training, not a fixed short horizon:
the same small-step Euler rule for the compressed model and dense controls,
training MSE below 0.01, and prediction RMS on all unseen validation images.
Retain the raw digits 3-versus-8 split (seed 47), 100 training images, 257
validation images, all 64 pixels with per-image normalization and no PCA,
two tanh hidden layers, zero readout, and the existing physical mobilities.
Large width remains 4096. No validation labels enter training or setup.

Primary question: can the current Logarithmic construction remain smaller
than dense while matching its trained predictions at dense-pair variability,
and how does a total-retained-state-matched ordinary network compare?
The contrary outcome is that the current construction cannot support this
training schedule in compressed storage; that yields no invented compressed
RMS and no substitute method relabeled Logarithmic.

Root owns this README, experiment driver and Git transaction. A scoped helper
may add only the reusable Euler integrator/check functions before
`validation_main` in the single existing capture script. Another read-only
helper checks feasibility against that script and the paper's finite decoder
construction. No other study supplies scientific inputs.

Before any full Logarithmic run, audit state growth for the required update
count. An exact cache/linear-algebra optimization is allowed; changing the
mathematical compression, truncating its historical dependencies or substituting
Harmonic/a smaller Gaussian network requires an explicit new method disclosure
and user direction. Do not reduce the update count to make storage fit.

Numerical protocol: seed 201 for the large reference and seed 10201 for its
independent copy. A training-only pilot starts at Euler step 0.05 and stops at
training MSE 0.005 (margin below the requested 0.01), subject to physical-time
cap 200 and 300 seconds per model run. Round the final common horizon upward
to a multiple of 0.5; extend it if either reference/control has not reached
0.01. This fixes fitting time from training loss, never from validation RMS.
At that horizon, compare Euler steps 0.05 and 0.025 on the same initialization;
halve further, no smaller than 0.003125 in this bounded pass, when needed.
The empirical resolution gate is maximum recorded validation RMS change at
most 0.001 and at most ten percent of the independent dense-pair discrepancy.
This is a numerical refinement check, not a rigorous global error bound.
Observations are at physical intervals of 0.5 plus the exact endpoint.

Float64 is the reference precision. Float32 with TF32 disabled is allowed only
after a same-initialization full-horizon comparison against float64 has maximum
recorded prediction RMS difference below 0.00005. Record both results and
precision provenance. A failed precision gate keeps float64; a resource cap
is failure/inconclusive, never a license to shorten fitting.

Once a legitimate compressed run supplies its total retained state, choose
the largest ordinary dense width within that model-only budget, using the
same data and physical Euler schedule. Match across refinement runs at a
common physical horizon. All methods' training losses and step counts must
be reported, even if the compressed or matched model fails to fit. Primary
measurement is final whole-validation prediction RMS against the same large
reference; also retain maximum recorded-time RMS and dense-pair variability.
No classification accuracy may substitute for this observable.

This bounded continuation permits at most 16 model/precision/refinement runs,
each at most 300 seconds, at most 20 GB GPU memory, at most 2 GB numerical CPU
payload, and 30 minutes of numerical execution in total. Use both available
GPUs without oversubscription. Numerical unit tests are separate. If the
existing Logarithmic representation fails a static storage/feasibility gate,
complete the dense numerical protocol and record the precise blocked comparison;
do not launch a predictably oversized transcript. Preserve all historical
records and do not overwrite prior run folders or silently edit paper figures.

### Authorized bounded-state replacement (before its numerical results)

The user explicitly chose "Develop a bounded-state Logarithmic approximation"
after the history obstruction was explained. The new experimental model is
called **bounded Gaussian-action packets**, not the certified Logarithmic
decoder. It replaces the adaptive history by a fixed nonlinear network with
data-conditioned, covariance-balanced initialization. Its subsequent transpose
law and dynamics are not those of the full Gaussian-history decoder, and the
Logarithmic theorem does not automatically apply. This is a new empirical
approximation, not a repaired proof or a validated logarithmic scaling law.

Construction uses only an independent width-4096 first-layer initialization
and the 100 training inputs. Compute its initial feature Gram. At packet
width q, initialize a q-by-q operator conditioned on prescribed initial
training actions with that Gram. Balance those action packets with a thin
Gaussian QR factor so their empirical covariance equals the source Gram.
Keep the Gaussian complement on the orthogonal complement of the initial
training features. Both propagation directions use this same operator and
its transpose; every weight then follows the ordinary physical Euler rule.
The full source Gram/table and all factorizations are discarded after setup.
No target dense trajectory, validation input, or validation label enters setup.

The retained state is exactly q*64+q*q+q numerical scalars, with no history
growth and no separate fixed matrix. Match the ordinary Gaussian control at
exactly width q, the same first-layer/base initialization seed, same step and
same final physical time. Source seed is 40201, small/packet base seed is
60201, independent of reference seeds 201 and 10201. Freeze q=256 and q=512
as two reported budgets, not a winner selected by validation error. They are
practical budgets only; this one-width experiment tests no n-asymptotic claim.

All six models (two large references and both packet/small-control budgets)
must reach training MSE below 0.01 on one common horizon. Their training-only
fitting pilots use the stricter 0.005 target; the shared horizon is the largest
pilot stopping time rounded up to 0.5. Refine every final model at the same
two step sizes and report final and maximum recorded unseen prediction RMS.
The pass/comparability criterion remains factor three of dense-pair RMS;
beating the matched small network is a separate observation, never presumed.
Unit checks require the initializer's action/covariance identities, inherited
physical gradients, fixed-state restart, and absence of retained source arrays.

This explicit new-method authorization increases the bounded allowance to
at most 28 model/precision/refinement runs, retaining the 300-second per-model,
30-minute cumulative execution and memory caps. This covers two packet
budgets, matched controls, the two dense references and their numerical
checks. No extra hyperparameter search is permitted after observing results.
If the approximation performs poorly, report it; do not modify its initializer
or budget rule using validation performance.

Training-only pilot outcome: the two large networks first reach MSE 0.005
at times 79.0 and 78.9; ordinary q=256/512 controls at 80.2/80.7; bounded
q=256/512 models at 80.2/79.7. Therefore freeze common final time **81**.
The dense 0.05-versus-0.025 comparison has maximum recorded prediction change
0.003153, failing the 0.001 gate. The final common Euler pair is consequently
0.0125 and 0.00625 (6,480/12,960 updates); if this pair still fails, apply the
already declared final halving to 0.003125 to every affected comparison.
The initial dense float32-vs-float64 check differs by at most 6.165e-8 RMS.
Final-horizon precision checks remain required. No validation performance
comparison between packet and small-network models was inspected to choose
these budgets, the common horizon, or the initializer.

### Bounded packet construction and approximation boundary

Let V have the m unit-normalized training inputs as rows. The deployable state
is A in R^(q by d), W in R^(q by q), and w in R^q, with prediction
`f(v) = w.T @ tanh(W @ tanh(A @ v)) / q`. Its architecture and subsequent
physical gradient flow are exactly those of the ordinary q-width control;
the only difference is a data-conditioned initial hidden matrix. In particular
this experiment does not establish anything beyond smaller networks with a
different initialization, nor does it validate the original decoder's dynamics.

At setup, draw independent source A_n and compute
`H_n = tanh(A_n @ V.T)`, `K = H_n.T @ H_n / n`. The small model's A and base
Gaussian G are identical to the ordinary control's initial first/hidden
matrices. Write `H = tanh(A @ V.T) = Q @ R`, using thin QR. Draw a separate
Gaussian q-by-m array and take its sign-corrected thin QR factor Q_z, so
`Q_z.T @ Q_z = I`. The sign correction multiplies columns by the signs of the
QR triangular diagonal; it removes the library's deterministic QR sign bias.
Use `Z = sqrt(q) * Q_z @ chol(K).T` and initialize

```
W = G + (Z - G @ H) @ inverse(R) @ Q.T,   w = 0.
```

The code uses a triangular solve, never an explicit inverse. Since
`inverse(R) @ Q.T @ H = I`, it follows exactly that `W @ H = Z` and
`Z.T @ Z / q = K`. For a vector orthogonal to the columns of H, the correction
vanishes, so its action remains that of G. Forward and backward propagation
reuse W and W.T. These are algebraic identities, not a trained-trajectory
approximation theorem. Covariance balancing makes packet rows dependent and
not exactly Gaussian; the later adaptive Gaussian history and wide transpose
law are not preserved. No claim here transfers the Logarithmic theorem.

The source first weights/features, Gram, packet table and QR/Cholesky factors
are all temporary. Only the three weight arrays are needed for inference and
restart; `weights.npz` stores exactly those arrays. Ordinary common training
data add 6,500 scalars to either model if retained. Scalar diagnostics and
provenance in the report are external experiment metadata. Training peak CUDA
allocation includes the initial-state copy, current state, derivatives, data
and diagnostic buffers, and is reported separately from deployable model size.
No history of responses is an operand of a subsequent update or query.

For q >= m, initialization arithmetic is
`O(n*d*m + n*m^2 + q*m^2 + q^2*m)`, plus Gaussian generation; temporary numerical
arrays are `O(n*d + n*m + q^2 + q*m + m^2)`. Subsequent Euler work per step is
`O(q^2*m + q*d*m)`, with `O(q^2 + q*d + q*m)` model/training workspace (besides
common data). One new query costs `O(q^2 + q*d)` work and `O(q+d)` extra
workspace beyond the loaded weights. These costs are for this new empirical
model, not for the theorem's decoder. The experiment chooses two fixed q
values and does not infer logarithmic width scaling.

### Corrected full-training outcome

All models use **12,960 full-batch Euler steps of size 0.00625 through time
81**, with a matched run at 6,480 steps of size 0.0125. Every final training
MSE is below 0.005. All 257 validation images are evaluated; RMS is prediction
discrepancy against the same width-4096 reference, not classification error.
This is one data split and one independent reference pair, not a replicated
superiority or asymptotic claim.

| Model | Deployable weight scalars | Training MSE | Final validation RMS | Maximum recorded-time RMS |
|---|---:|---:|---:|---:|
| Dense reference, n=4096 | 17,043,456 | 0.00475360881 | 0 | 0 |
| Independent dense, n=4096 | 17,043,456 | 0.00471663009 | 0.00841495569 | 0.01700302784 |
| Ordinary q=256 | 82,176 | 0.00488593267 | 0.02740924335 | 0.04540505464 |
| Bounded packets q=256 | 82,176 | 0.00489077176 | 0.01424297188 | 0.05144772833 |
| Ordinary q=512 | 295,424 | 0.00495973016 | 0.01489553437 | 0.04392802620 |
| Bounded packets q=512 | 295,424 | 0.00482226606 | 0.00974181286 | 0.02307065355 |

The new initializer improves the endpoint error in both tested budgets. At
q=256 it performs worse over the recorded trajectory: the maximum-error ratio
is 3.0258 dense-pair units, narrowly failing the frozen factor-three rule.
At q=512 the ratio is 1.3569 and both endpoint and trajectory metrics improve
over the matched control. This does not imply the q=256 failure is robustly
separated from the numerical/seed uncertainty around that cutoff.

The maximum step-halving RMS for the six models lies between 0.0007483 and
0.0008853: every model passes the 0.001 absolute and 10-percent dense-pair
relative resolution gates. These are empirical refinement checks, not a
rigorous continuum-GF error certificate. Full-horizon precision checks use
float64 versus float32, with TF32 disabled, on identical initializations;
the two large models are checked at step 0.0125 and the four small models at
step 0.00625. The final summary must record complete six-model coverage.

Measured fine-run integration plus recorded diagnostics takes 14.57/14.70
seconds for the large pair, 10.96/11.16 seconds for the ordinary q=256/512
controls, and 10.79/11.06 seconds for the bounded counterparts. Packet setup
takes 0.261/0.265 seconds. Its peak CUDA allocation is 47.41/50.14 million
bytes during setup and 35.15/38.22 million bytes during the run; large-reference
run peak is 287.44 million bytes. These are PyTorch allocated tensor peaks,
not total process RSS or GPU driver reservation; Python/data-loader/import
overhead is not included. Small models are launch/diagnostic-overhead limited,
so the parameter reduction is not a comparable measured runtime speedup.

The scoped audit independently reconstructed the raw data split, recomputed
all twelve runs' MSE/RMS/refinement metrics, checked the matched budgets,
and reloaded all four fine small-model checkpoints. Re-evaluated predictions
agree with their GPU records within 1.5e-7. The algebra/gradient/restart checks
are retained in `euler_bounded_checks_01`. No prior scientific record is
overwritten, and the paper/theorem/earlier figures are not changed by this
new-method experiment. The two-update result remains only a sanity check.

Final aggregate: `data/generated/compression_empirical_validation_20261007/
euler_comparison_02/report.json` and `rms.npz`. All six model initializations
have full-horizon precision coverage; the largest float32/float64 discrepancy
is 7.4463e-7 RMS. This supersedes provisional `euler_comparison_01`, whose
precision flag did not check coverage of the independent dense initialization.
The summary code now requires actual float64/float32 dtypes and coverage of
every compared initialization, and reports the tested steps explicitly.
The continuation executed 26 model runs, approximately 600.23 seconds total
setup-plus-run work, with maximum individual combined time 186.33 seconds.
It remained within its amended 28-run, 30-minute and 300-second caps. Counts
include fitting pilots, reference precision checks and all model refinements;
unit tests and CPU-only metric recomputation are separate.

### Reproduction of the corrected experiment

Run from the repository root with `/home/amir/miniconda3/bin/python -B`.
GPU access requires host execution in this environment. Use a fresh output
directory for each invocation. `euler-fit` fixes the raw 100/257 split and
canonical two-hidden-layer model; `--horizon 81` disables early loss stopping.
The six configurations are:

| Label | CLI width | Seed | Extra model arguments |
|---|---:|---:|---|
| dense | 4096 | 201 | none |
| iid | 4096 | 10201 | none |
| small256 | 256 | 60201 | none |
| small512 | 512 | 60201 | none |
| packets256 | 4096 | 60201 | `--model bounded-packets --packet-width 256 --source-seed 40201` |
| packets512 | 4096 | 60201 | `--model bounded-packets --packet-width 512 --source-seed 40201` |

For every row run both `--step 0.0125` and `--step 0.00625`, with
`--dtype float32 --horizon 81 --device cuda:0` (or a free second GPU).
The width argument is the source width only for bounded packets; their
actual deployable width is `--packet-width`. For example:

```bash
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py euler-fit \
  --model bounded-packets --width 4096 --packet-width 512 --seed 60201 \
  --source-seed 40201 --horizon 81 --step 0.00625 --dtype float32 \
  --device cuda:0 --out PATH/TO/FRESH/PACKET512_FINE
```

Repeat the two large configurations in float64 at step 0.0125, and all four
small configurations in float64 at step 0.00625. The construction always uses
float64 before conversion, so the pre-conversion initialization hashes must
match. Run `euler-summary` with one `--pair LABEL COARSE_DIR FINE_DIR` per
table row and one `--precision FLOAT64_DIR FLOAT32_DIR` per precision check,
plus `--out PATH/TO/FRESH/SUMMARY`. It checks common data, times, seeds through
initialization hashes, step halving and complete precision coverage, then
recomputes every RMS and training MSE from saved arrays. Its six-case primary
labels are `dense`, `iid`, `small256`, `small512`, `packets256`, `packets512`.
Full environment, commands, source hashes, losses, times, CUDA allocated
peaks and arrays are retained in each run directory. Small-model checkpoints
contain only `first`, `readout` and `hidden` arrays.

For unit checks:

```bash
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py euler-fit \
  --check-only --model bounded-packets --device cpu --out PATH/TO/FRESH/CHECKS
```
