# Sampler-rank audit for circle-RMS calibration

2026-10-03. Scoped numerical continuation. This audit reads only
`neuron_sampling_setup.py`, `gpu_sampling_experiment.py`,
`GPU_SAMPLING_PROTOCOL.md`, `GPU_SAMPLING_RESULTS.md`, and
`GPU_NUMERICAL_CODE_CHECK.md`, plus the required mathematical-presentation
skill. It launches no training and changes no implementation. Prior numerical
results quoted below are taken from the supplied report; their raw archives
are outside this audit's initial input scope.

The proposed width/rank sweep can distinguish some practical sampler errors,
provided selected width and basis rank are reported separately. Increasing
rank alone does not systematically improve the sampler: it improves source
representation while making positive moment matching more demanding.
Local whitening controls the mixer norm but generally changes sampled source
responses when the selected Grams differ from identity.

## Existing parameters and the minimal runner change

`build_sampler` already accepts `n_selected`, `basis_rank`, `probe_count`,
`mass_floor`, and `singular_tolerance`. No sampler change is needed to expose
rank. The existing runner hardcodes 16 probes and leaves `basis_rank` unset,
which selects `min(N-1,8)` for selected width `N`.

For the requested continuation, the runner should accept selected widths and
requested ranks, enumerate valid pairs `1 <= rank <= N <= n`, and pass the rank
explicitly. Fixing probes, floor, and tolerance at their existing values
isolates the width/rank experiment. Archive those values and both actual
retained ranks, since numerical source rank may be below the request.
Model names, schedule rows, and restart keys must identify both `N` and rank;
the old names and restart keys identify only `N` and would collide in a rank
sweep. An identical initialization witness can be reused within a case.

For two input coordinates and two examples, actual reduced storage is
`N^2+3N` moving scalars plus `2N+6` fixed scalars. Rank changes setup but adds
no retained runtime coordinates to this implementation.

| Selected width N | Moving | Fixed | Total |
| ---: | ---: | ---: | ---: |
| 24 | 648 | 54 | 702 |
| 32 | 1120 | 70 | 1190 |
| 48 | 2448 | 102 | 2550 |
| 64 | 4288 | 134 | 4422 |
| 96 | 9504 | 198 | 9702 |
| 128 | 16768 | 262 | 17030 |

Deleting the setup witness before evolution would reduce unused process
memory; autonomy of the existing reduced equations does not depend on that
deletion. Dense comparison storage is separate from the declared model count.

## Why rank and cubature accuracy are confounded

For actual retained rank `r`, `_positive_cubature` fits a constant and all
upper-triangular source products. There are `1+r(r+1)/2` listed moments. The
constant is already imposed by unit mass, so `N` positive masses have `N-1`
continuous degrees of freedom against up to `r(r+1)/2` nonconstant conditions.
Moment dependencies can reduce the effective number of conditions; this
count alone is not an impossibility proof for a particular source matrix.

| Rank r | Listed constant/product moments |
| ---: | ---: |
| 8 | 37 |
| 12 | 79 |
| 16 | 137 |
| 24 | 301 |

At rank 24 every proposed width is below the listed moment count. At rank 16
even width 128 is below it. At ranks 8 and 12, widths beyond approximately 37
and 79 respectively at least remove this elementary parameter-count obstacle;
neither exact feasibility nor success of this greedy optimizer follows.
The positive floor adds another approximation: every selected mass must be
at least `.05/N`, even when exact matching might prefer a smaller mass.

The optimizer minimizes standardized moment residuals. Its objective is not
the unweighted Frobenius norm of the Gram defect because each product row is
divided by its dense RMS. A successful optimizer status certifies neither
exact moments nor accurate prediction. The existing diagnostics correctly
retain actual Gram operator/Frobenius defects and spectra separately.

The selected sets need not be nested as `N` changes. Their lower mass bound
changes already in the initial QR-seeded solve, which can change subsequent
greedy additions. Rank changes also change selection and the fitting target.
Nonmonotone final errors should therefore be retained rather than smoothed
away or treated as failed experiments.

## Exact source distortion from local whitening

Let `n` be dense width; let `V` and `U` be the first- and second-population
source bases returned by `_basis`, with shapes `n by r1` and `n by r2` and
`V.T V/n = I`, `U.T U/n = I`. Let `I,J` be selected indices and `mu,nu` their
positive unit-sum masses. Write `V_I=V[I]`, `U_J=U[J]`, and define

\[
G_1=V_I^\top\operatorname{diag}(\mu)V_I,\qquad
G_2=U_J^\top\operatorname{diag}(\nu)U_J,\qquad
C=U^\top W_0V/n.
\]

Here `W0` is the dense initialized mixer. Suppose no selected-Gram directions
are discarded, so both `G1` and `G2` are positive definite. Expanding the
implemented square-root-mass frames gives

\[
B=U_JG_2^{-1/2}C G_1^{-1/2}V_I^\top\operatorname{diag}(\mu).
\]

The weighted reverse mixer is
`B*=diag(mu)^(-1) B.T diag(nu)`. Multiplication therefore yields the exact
identities

\[
\begin{aligned}
BV_I&=U_JG_2^{-1/2}C G_1^{1/2},\\
B^*U_J&=V_IG_1^{-1/2}C^\top G_2^{1/2}.
\end{aligned}
\]

Even in the ideal source-space case `W0 V=U C`, the desired sampled forward
response is `U_J C`, so local whitening introduces the source coefficient
defect `G2^(-1/2) C G1^(1/2)-C`. The reverse defect has the corresponding
transposed formula. If either source inclusion is approximate, its projection
residual contributes as well. Exact cubature `G1=I,G2=I` removes this particular
distortion. A bounded weighted mixer norm or absence of deleted modes does
not remove it. This is structural source distortion, not an allegation that
the numerical whitening itself fails to produce orthonormal frames.

The supplied prior audit reports no discarded selected-Gram modes but Gram
operator defects ranging from approximately `.0300` to `.9347`. Those values
therefore do not establish small whitening distortion. As rank grows, record
minimum/maximum Gram eigenvalues and condition numbers alongside the existing
forward, reverse, feature, and second-jet errors. The source residuals and
`selected_target_training_gram` versus `compressed_initial_training_gram`
help distinguish quadrature mismatch from additional projection/nonlinearity
mismatch without pretending to provide an additive prediction-error budget.

A setup-only synthetic algebra check used `numpy.default_rng(29417)`,
`n=96,r=8,N=24`, QR-normalized independent Gaussian `V,U`, and
`C=.1*rng.normal(size=(8,8))`. It called the existing cubature and frame
functions with floor `.05` and tolerance `1e-10`; the ideal dense mixer can
be defined by `W0=U C V.T/n`, which has both exact source inclusions. Results:

| Quantity | Value |
| --- | ---: |
| Forward identity maximum absolute discrepancy | `1.11e-15` |
| Reverse identity maximum absolute discrepancy | `8.88e-16` |
| Weighted forward sampled-source defect, Frobenius | `.0260564` |
| Weighted reverse sampled-source defect, Frobenius | `.0260564` |
| Gram-1 operator defect | `.0635606` |
| Gram-2 operator defect | `.0990090` |
| Weighted mixer norm and core norm | `.5371781` |

Every optimizer step reported success. SciPy emitted its ordinary warning
that a trial iterate outside bounds was clipped. Returned masses passed the
sampler's checks. This small test verifies the displayed identities and
exhibits distortion despite exact source inclusions; it supplies no trained
prediction evidence or estimate for the proposed scientific configurations.

## Metric and validity checks for the continuation

For circle panel angles `theta_k`, saved physical times `t_j`, and prediction
error `e_jk=f_reduced(t_j,theta_k)-f_dense(t_j,theta_k)`, the natural circle-RMS
error uniformly over saved training times is

\[
E_{\rm RMS}=\max_j\sqrt{\frac1M\sum_{k=1}^M e_{jk}^2}.
\]

This differs from the old `rms_of_time_sup`, which computes
`sqrt(mean_k max_j |e_jk|^2)` and is an upper bound on `E_RMS`. Archive both,
the RMS time trace, its maximizing time, endpoint RMS, and `sqrt(n)*E_RMS`.
Compute the paired dense-copy RMS by the same formula on the same grid.
Reuse the old maximum-error metric as a diagnostic, not as a silent substitute
for the new target.

The smallest tested state count attaining `sqrt(n)*E_RMS <= C` is only a
tested sufficient count for that configuration. If rank is selected using
the same prediction data, describe the result as an empirical search envelope,
not a predetermined deployable rank rule. Retain every rank/width outcome,
failures, and nonmonotonicity. Across configurations, a maximum, a cellwise
median, and a fitted trend answer different questions and must be named.

Targeted checks needed before interpreting the new sweep are:

1. Preserve the existing RHS, Heun, weighted-gradient, restart, and float64
   checks. Confirm every pair maps to the intended model and restart keys;
   repeated widths at different ranks are the important new coverage case.
2. Inspect every sampler's optimizer statuses, finite masses, mass sum/floor,
   retained modes, selected-Gram spectra, source residuals, and forward/reverse
   jet errors. A higher-rank failure is a reported result, not permission to
   silently reduce the rank or omit the model.
3. Repeat a half-step check including the largest selected width and rank.
   The old small-width check does not establish numerical resolution of these
   new models. Compare matched predictions and the new RMS metric with the
   target error scale and paired dense-copy RMS; preserve the existing absolute
   tolerance as well. A changing or exceptionally small paired denominator
   must not be hidden by pooling.
4. Double the angular and observation panels on an agreed representative case.
   Nested original points test solver parity; comparing RMS on the full coarse
   and full fine panels tests the changed angular quadrature. Compare time maxima
   on matched and on all fine times separately, since narrow transient peaks
   need not occur at the old observation times.
5. Report both a common physical horizon and any settlement-driven extensions.
   The entire batch shares an extension trigger; adding many models can change
   the comparison horizon for all of them. Training fit is not unseen-angle
   fidelity, and empirical endpoint settlement is not an infinite-time bound.

No rank, moment, or numerical-conditioning diagnostic establishes the
asymptotic minimal state growth. They make the bounded empirical sufficient
counts and the construction's approximation limitations interpretable.

## Inspected snapshots

| File | SHA-256 |
| --- | --- |
| `neuron_sampling_setup.py` | `f3199851e30e267bab005b06ccf16f68f05b0307695d9d4cbca64aa2ddc28f02` |
| `gpu_sampling_experiment.py` | `2721dc8fb8f569ff6296267c4426c9ba153c49b0697734acf889867cce263bfc` |
| `GPU_SAMPLING_PROTOCOL.md` | `8dc345251e17eb35892e554d244c1b7bae26e1b287df66647f4c55bcaabbb8bb` |
| `GPU_SAMPLING_RESULTS.md` | `3d4f166fe41856190ce17dfa9991eb387eef54806fb2f0447274a588dc54cd26` |
| `GPU_NUMERICAL_CODE_CHECK.md` | `9ad27878949f5d27cc020b61cb224d572f8bf82913e2371c7d3a3c02a5cd2873` |

## New runner audit before calibration

The supervisor expanded this audit's input scope to the complete
`gpu_rms_growth_experiment.py` and `GPU_RMS_GROWTH_PROTOCOL.md`. The final
inspected runner hash is
`83be73776a1c3f2da778ecd7da770fea987a519dc6cdc0f064ade82234a0fc3e`;
the new protocol hash is
`71befafaec79f2f4d8e15118f0b79b7f987eb6ec5f2815074b13654a00cef81d`.
No blocking scientific implementation defect was found in this snapshot.
This reviewer launched no training on either GPU or CPU.

The new protocol explicitly fixes **RMS of pointwise time suprema** as its
primary observable, reflecting the intervening clarification. This supersedes
the proposed primary ordering in the earlier metric discussion above.
Both orderings remain reported. It also deliberately increases setup probes
from 16 to 32 and uses a bounded calibration grid followed, conditionally, by
fresh-seed validation; it is not the provisional six-width grid discussed
earlier in this audit.

The runner imports `fields`, `heun`, initialization, weighted packing, and
feature-motion functions unchanged from the prior runner. Dense and reduced
models each call their own Heun update with their own current state and
predictions. There is no dense residual, trained snapshot, or future prediction
in sampler setup or reduced evolution. Explicit `basis_rank`, configured
probe count and mass floor, and `singular_tolerance=1e-10` reach `build_sampler`.
The initialization witness is discarded before training. Padding remains
consistent with the already-reviewed weighted implementation.

`comparison_metrics` computes the declared primary error, the other RMS/time
ordering, endpoint RMS, and the maximum absolute error directly from raw
prediction arrays. Every ratio uses the same case's independent dense model
and the corresponding metric. Undefined zero-baseline ratios are null.
Signed training predictions, circle predictions, residuals, motion, times,
query coordinates, labels, and training directions are archived. Endpoint
settlement uses the final prediction minus the prediction ten units earlier
under the protocol's unit or half-unit observation cadence. It remains an
endpoint comparison, not the maximum excursion over that interval.

Schedule rows enumerate model indices starting at two, exactly matching the
prediction axis and `model_<index>_` restart keys. Counts are
`moving=N^2+3N`, `fixed=2N+6`, `total=N^2+5N+6`. Repeated selected widths at
different ranks retain different keys. The generic runner allows duplicate
width/rank aliases and records their distinct count; it does not automatically
deduplicate them or expand a list of exponent aliases. The configuration
producer therefore must deduplicate the intended models and preserve every
growth-schedule-to-model mapping.

The final restart contains only each reduced `A,K,w,mu,nu`, shared training
directions and labels, a restart clock, and diagnostic model indices. It has
no dense state. `validate_archive` checks array dimensions, finite observations,
zero initial predictions, residual recomputation, positive normalized masses,
and reconstructs final training/query predictions using NumPy contractions.
Its stored-metric check calls the same metric function again, so that part is
an archival consistency check rather than an independent formula oracle.
The separate explicit-loop checks below supply an independent formula check.

The repaired initialization archive no longer repeatedly compresses the full
reference mixer and two dense mixers. `dense_initialization.json` records the
initialization factory, dense width, both seeds, setup/runtime dtypes, source
provenance pointer, and shape/dtype/raw-byte SHA-256 fingerprints of both
dense initializations and reference setup arrays. Reproduction can regenerate
these arrays with the archived sources and environment and verify their
fingerprints. Small setup arrays, selected indices, probes, and exact reduced
initial runtime arrays are still stored. This change does not alter training.

The reviewer ran only deterministic training-free checks. A NumPy random
fixture with seed 49411 and shape `(5 times,4 models,7 queries)` was evaluated
with explicit Python loops independent of the runner's reduction expressions.
All four metrics, their root-width scaling at width 512, and their paired
ratios agreed exactly in that execution. The runner's noncommuting-metric and
zero-baseline fixtures also passed. A synthetic CPU tensor packing check with
samplers `(N,rank)=(4,2),(6,2),(6,3)` verified distinct keys, removal of padded
coordinates, and counts `42,72,72`; it evaluated no training step. Configuration
checks retained all three pairs and rejected rank greater than selected width
and selected width greater than dense width. These helper functions were
unchanged by the final archival/metadata repair, which was read separately.

Several scientific decisions are appropriately external to this generic
runner: selecting a candidate only after the final cubature statuses and
frame-mode gates pass, freezing the selected rank/anchor before holdout,
enforcing the distinct calibration/validation/extrapolation seed sets,
implementing the protocol's global campaign clock, checking refined panels
and time steps, and applying the held-out decision rule. The runner archives
the required optimizer/frame information but does not itself exclude invalid
candidates from later selection. No actual calibration/holdout configuration
or new scientific archive was in this audit's input scope, so their compliance
is not certified by this code review.

## Calibration recovery and independent selection check

The supervisor subsequently authorized the three calibration output roots
`gpu_rms_growth_20261003_calibration_90`, `_60`, and `_60_resume` under
`data/generated/closure_sampling_20261003/`, together with their frozen
`gpu_rms_growth_calibration_*.json` configurations and the protocol. The checks
below read their raw data directly and neither import the analysis code nor
launch training.

The calibration's archived protocol hash is
`b603672426f6d5c5a95ebb0a71c87194a45939659802a030ed5cd102b8c4fbc3`.
All three runs contain this same protocol snapshot, including the clarified
selection rule: smallest qualifying selected width, then smallest worst-case
calibration error at that width, then smaller rank only for exact ties.
The runner hash remains `83be73776a1c3f2da778ecd7da770fea987a519dc6cdc0f064ade82234a0fc3e`.
Every archived source snapshot matched its recorded hash, and no source hash
differed across the three runs. Thus the earlier protocol hash in this audit
is superseded for the actual campaign by the common pre-run snapshot above.

The initial 60-degree worker completed both width-512 cases and failed during
construction of `N96_r24` for width 1024, seed 8411, positive second label.
The failure is `cubature optimizer returned invalid positive masses` in the
second population. Its record has step zero, state time zero, and zero
observations. The archive retains this failure and empty partial trajectory.

The resume configuration contains exactly the remaining four original cases
and exactly the first ten original sampler specifications. Other numerical
settings are identical. All three local frozen configuration files match the
archived input bytes. The failed and resumed case have identical dense
initialization JSON and all 87 arrays from the failed attempt's completed
setup archive agree exactly with the resumed setup. There was no trained
trajectory to replace and no seed search or modification of the sampler.

This is a valid completion of the unaffected calibration candidates if
`N96_r24` is treated as globally ineligible. Its eight successful cases must
remain visible but cannot qualify an incomplete candidate. There are twelve
unique completed scientific cases, plus one preserved failed construction
attempt; this is not thirteen independent calibration trajectories.

All twelve prescribed combinations of width, angle and label sign are now
present exactly once, all with reference seed 8411. The auditor independently
recomputed both RMS/time orderings, endpoint RMS, maximum error, and residuals
from the raw arrays. Metric differences from the records were zero. All 72
recorded artifact hashes matched. The 128 completed reduced restart states
have the declared scalar counts and reconstruct final training and circle
predictions with maximum absolute discrepancy `1.6653345369377348e-16`.
Every moving model met the recorded settlement criterion and all completed
cases ended at physical time 120.

| Candidate | Completed cases | Largest sqrt(n) times primary error | Eligibility at ceiling .10 |
| --- | ---: | ---: | --- |
| N24, rank 8 | 12 | .3510409649 | Error above ceiling |
| N24, rank 12 | 12 | .2282305669 | Error above ceiling |
| N24, rank 16 | 12 | .7161240411 | Error above ceiling |
| N48, rank 8 | 12 | .3511227198 | Error above ceiling |
| N48, rank 12 | 12 | .0776433579 | Qualifies |
| N48, rank 16 | 12 | .0751640871 | Qualifies; selected by frozen rule |
| N48, rank 24 | 12 | .3190758153 | Error above ceiling and final optimizer failure |
| N96, rank 8 | 12 | .3278039241 | Error above ceiling |
| N96, rank 12 | 12 | .0490882586 | Qualifies; larger state |
| N96, rank 16 | 12 | .0176412788 | Qualifies; larger state |
| N96, rank 24 | 8 | .0352476559 on completed cases | Incomplete after construction failure |

The separate `N48_r24` optimizer failure occurs in first-population cubature
at width 2048, 60 degrees, opposite labels: final status 8, 59 iterations,
objective `.060535819430883674`. Its output remains finite and trained, but
the protocol excludes it from positive selection. It must not be described
as an optimizer-successful candidate. All other complete candidates pass
their final optimizer and selected-frame-mode checks.

The independently selected anchor is therefore `N0=48`, rank 16, with
`P0=2550` total retained scalars. Both actual source bases retain rank 16 in
all twelve selected-candidate cases. Its largest scaled primary error is
`.07516408706344334`, at width 1024, 90 degrees, same-sign labels. This is a
calibration choice, not held-out evidence or a validated growth law. The
specified expansion to width 192 is unnecessary because qualifying complete
candidates already exist.

## Frozen selection and validation configuration check

The supervisor authorized `GPU_RMS_GROWTH_SELECTION.md`, both
`gpu_rms_growth_validation_90.json` and `_60.json`, and their generated output
roots for the next audit stage. The selection artifact records the independently
confirmed anchor `N0=48`, rank 16, and `P0=2550`. Its SHA-256 is
`ef1fd7c943a3120c4ed1acadd8d4905cc3a0e8df024337efcb55fea64e3622ba`.
Both validation workers archived that same artifact before their case loops,
with the reviewed runner hash and common frozen protocol.

The two configurations contain exactly the 80 prescribed combinations of
widths 512, 1024, 2048, 4096; reference seeds 8511 through 8515; angles 60 and
90 degrees; and both second-label signs. These reference seeds are disjoint
from calibration seed 8411. All sampler ranks are 16. Each budget equals
`2550*(log(n)/log(512))**p`, and every configured width is the largest integer
whose complete scalar count fits that budget. Both local configuration files
match the archived input bytes.

There is one operational deviation from the instruction to deduplicate:
the four width-512 sampler entries have identical width 48 and rank 16,
and this runner computes all four. They are four schedule aliases of one
deterministic construction, not four distinct models or independent replicates.
The selection artifact and runner explicitly flag that interpretation.
If all cases complete, there would be 320 schedule rows representing 260
distinct reduced models. Counting the aliases as extra evidence would be
incorrect; duplicate computation itself does not change the error criterion.

During this audit, the 60-degree worker stopped after 23 completed cases.
At width 2048, seed 8512, opposite-sign labels, `p1` requires width 53 and
its second-population cubature failed with invalid positive masses. The setup
archive records exactly one completed sampler, `p0` at width 48. Failure step,
time, and observation count are all zero. The failure was reported promptly.
It excludes `p1` from the strict all-cases positive criterion; it is not
evidence about an asymptotic exponent or a proof that other constructors fail.
The unaffected schedules require a documented continuation before the full
held-out comparison can be assessed.

## Completed held-out archive audit

The supervisor authorized the additional frozen resume configurations and
output roots `_validation_60_resume`, `_validation_90_resume`, and
`_validation_60_resume2`. The final audit reads all five validation roots
directly, without using the campaign analysis functions or launching training.

Two further constructor failures occurred before any training in their cases:

| Original case | Failing schedule | Selected width | Completed samplers before failure |
| --- | ---: | ---: | ---: |
| n2048, seed8512, 60 degrees, opposite labels | p1 | 53 | 1 |
| n2048, seed8514, 90 degrees, same labels | p2 | 59 | 2 |
| n4096, seed8514, 60 degrees, same labels | p0 | 48 | 0 |

All three fail the second-population positive-mass check, with state time,
completed step, and observation count zero. They remain in the archived
failure/status files. The first 60-degree resume contains exactly the 17
remaining original cases with p0,p2,p4; the 90-degree resume contains exactly
the 14 remaining cases with p0,p4; and the final 60-degree resume contains
exactly its last four cases with p4. Their retained sampler specifications
match the originals. The first two resume configurations preserve all
numerical settings apart from the allowed worker budget/description fields.

For each failed-to-resumed case, the dense-initialization JSON and every
already-built unaffected model's initial arrays match exactly after mapping
model names to their possibly changed archive indices. The three comparisons
checked 15, 15, and 7 matching setup arrays respectively. Every archived source
has a valid recorded hash, with identical source hashes across all five
validation invocations. No failed trajectory was replaced by a favorable seed
or changed sampler.

There are exactly 80 unique completed cases on the prescribed grid, all ending
at physical time 120. Every one contains p4; some invalidated schedules are
absent in later cases. The auditor checked all 480 record-linked artifact
hashes, recomputed the four prediction metrics and settlement flags from raw
arrays, and independently reconstructed all 267 completed reduced restart
states. Recorded metrics agree exactly; the maximum restart prediction error
is `1.6653345369377348e-16`. All completed moving models are settled and have
successful final cubature fits with no removed selected-frame modes. All 20
width-512 cases have exactly identical predictions across their four schedule
aliases. The 267 schedule rows represent 207 distinct reduced models.

The primary scaled error means `sqrt(n)` times RMS over query directions of
each direction's maximum absolute error over saved times. The complete p4
results are:

| Dense width n | Cases | Selected width N | Total retained scalars | Largest scaled primary error |
| ---: | ---: | ---: | ---: | ---: |
| 512 | 20 | 48 | 2550 | .0565966534 |
| 1024 | 20 | 59 | 3782 | .0428927691 |
| 2048 | 20 | 72 | 5550 | .0300796922 |
| 4096 | 20 | 87 | 8010 | .0426995023 |

The largest p4 error is `.05659665342145616`, at width 512, seed 8515,
60 degrees and opposite labels. It is below the frozen `.15` ceiling in every
held-out case. The exact protocol's cellwise median-growth checks also pass:

| Angle | Second-label sign | Median scaled error, n512 | Median scaled error, n4096 | Ratio |
| ---: | ---: | ---: | ---: | ---: |
| 60 | -1 | .0422233519 | .0333546285 | .7899569076 |
| 60 | +1 | .0254341783 | .0234563338 | .9222367445 |
| 90 | -1 | .0262800437 | .0259702452 | .9882116437 |
| 90 | +1 | .0227949679 | .0209745646 | .9201401242 |

The construction, error-ceiling, settlement, and cellwise-growth gates thus
pass for p4 on these eighty cases. The prescribed refined time-step/panel
checks are a separate gate and are not covered by this completed-archive
section. The extrapolation stress is also separate.

For the other schedules, the completed-case maxima are informative but cannot
erase the constructor failures or fill missing cases:

| Schedule | Completed cases | Largest scaled primary error on completed cases | Strict positive criterion |
| ---: | ---: | ---: | --- |
| p0 | 76 | .1169809630 | Fails construction; also fails growth in both complete 90-degree cells |
| p1 | 49 | .0886311011 | Fails construction; incomplete grid |
| p2 | 62 | .0571769938 | Fails construction; incomplete grid |

All completed cases remain below `.15`, including those of invalidated
schedules. For p0 the two fully observed 90-degree cells have 512-to-4096
median-growth ratios `2.5977872089` for opposite labels and `3.0791361822`
for same-sign labels, exceeding the protocol's factor 1.5. The numerical
constructor failures of p1 and p2 are separate from prediction scaling.
Neither they nor p0's finite-grid growth discriminator establish an asymptotic
lower bound or optimality of p4. The verified result is one sufficient tested
schedule, subject to the remaining numerical-resolution gates.

## Resolution gates and final validation tables

The supervisor authorized both refinement roots/configurations and the final
`gpu_rms_growth_20261003_validation_analysis` outputs. This audit independently
compared the coarse and fine raw trajectories in the fixed width-4096 case
and the actual worst p4 held-out case at width 512. Both use the original
samplers and the same physical horizon 120. The fine time step is `.1`,
observation interval `.5`, and circle panel size 514 with offset 1. The actual
coarse times and circle coordinates agree exactly with the fine arrays at
their even indices. Thus the same-point comparison is a solver comparison;
the full fine metric also includes the new times and angles.

| Resolution case | Largest same-point prediction change | Largest full primary-metric change | p4 primary-metric change | Threshold |
| --- | ---: | ---: | ---: | ---: |
| n4096, seed8511, 60 degrees, opposite labels | `2.402339138923848e-5` | `1.3351983081048846e-5` | `1.0784957103272298e-7` | `1e-4` |
| n512, seed8515, 60 degrees, opposite labels | `2.3869034412621337e-5` | `1.375393349213605e-5` | `3.0901539943293047e-6` | `1e-4` |

The coarse paired dense primary errors are `.0022742543539014015` and
`.003375382734272755`; the applied minimum of `1e-4` and five percent of
these errors is `1e-4` in both cases. Both checks pass without another
time-step halving. All fine-run record-linked artifact hashes match and all
fine moving models are settled. These are the prescribed finite sampled
resolution checks, not a uniform numerical-error theorem for every case.

The final validation analysis summary SHA-256 is
`ee087cb63bfb64c041fd01417294fde755878b31c2ab388da8cb644012f4c394`.
Its 267 comparison rows, 58 cell-summary rows, four schedule counts/maxima/
medians, and missing-case counts agree with the independent raw-array audit.
Its recorded ceiling is `.15`, numerical validity is `pass`, and its only
empirically sufficient schedule is p4. The seed-bootstrap uncertainty output
was not independently recomputed in this audit; the checks here concern the
point estimates, coverage, and deterministic acceptance gates. Missing-cell
growth summaries for disqualified schedules must remain descriptive and
cannot substitute for complete five-seed cells.

This completes the protocol's eighty-case positive criterion for p4. It does
not establish an optimal exponent or an all-width/all-time error guarantee.

## Completed width-8192 stress and execution budget

The final authorized inputs add the extrapolation configurations and four
worker roots `_extrapolation_90`, `_60`, `_90_resume`, and `_60_resume`.
They contain exactly four scientific cases: width 8192, fresh reference seed
8611, both angles and both label signs. The p4 budget is
`11100.52583447645`, and width 102 is its largest admissible integer: the
retained count is `P(102)=10920`, whereas `P(103)=11130` exceeds the budget.
Requested and actual source ranks are 16 throughout.

Each initial extrapolation worker completed its same-sign case and then hit
its 210-second worker timer during the opposite-sign case. Those partial
traces and timeout failures remain archived. With execution time still
available under the global campaign cap, the supervisor authorized completing
the same two cases in separate unchanged one-case invocations. No new seed,
data geometry, sampler, or numerical setting was introduced.

The completed opposite-sign reruns have identical dense-initialization
fingerprints to their interrupted attempts. Every saved time, circle
prediction, signed training prediction, residual, and feature-motion value
matches the retained original prefix **exactly**: 93 saved times through
physical time 92 for 90 degrees, and 97 saved times through time 96 for
60 degrees. Thus the interrupted and completed attempts count as one
scientific case each; the timeouts are resource-history entries, distinct
from the earlier invalid-positive-mass construction failures.

| Angle | Second-label sign | sqrt(n) times primary error | sqrt(n) times endpoint RMS | Final time |
| ---: | ---: | ---: | ---: | ---: |
| 90 | +1 | .0329318105677 | .0324330749312 | 120 |
| 60 | +1 | .0317250268003 | .0258941819423 | 120 |
| 90 | -1 | .0179222726206 | .0116078083484 | 120 |
| 60 | -1 | .0227732641356 | .0133365558495 | 120 |

All four cases satisfy the `.15` ceiling and settlement checks. Their final
cubature solves succeed and no selected-frame mode is removed. The auditor
independently recomputed all four prediction metrics and residual/settlement
checks, verified 24 record-linked artifact hashes, and reconstructed the four
reduced restarts with maximum prediction discrepancy
`1.3877787807814457e-16`. All extrapolation source snapshots match their hashes
and each other. This is one additional-seed, four-case stress, not four extra
independent replicates of every held-out width or a new asymptotic rate fit.

The final execution-budget file is
`gpu_rms_growth_20261003_validation_analysis/execution_budget_complete.json`.
Using the same explicit metadata method independently, the auditor formed
each of the fourteen worker intervals from final `status.json` modification
time minus its recorded `wall_seconds`, then took the union of those
intervals. The union is `1330.025727033615` seconds, or
`22.16709545056025` minutes, below the 25-minute execution cap. At most two
recorded worker intervals overlap. Peak recorded GPU allocation is
`6.018158435821533` GiB per worker, below 8 GiB. This is an audit of the
recorded worker-activity intervals, including initialization and evolution;
it excludes gaps and postprocessing as specified by the campaign's execution
accounting. The preserved failure and timeout attempts are included.

No scientific or numerical blocker remains for the stated bounded empirical
finding: p4 passes the prescribed eighty-case validation and the additional
four-case width-8192 stress. This audit performs no promotion and makes no
claim that fourth-power logarithmic state growth is necessary or optimal.
