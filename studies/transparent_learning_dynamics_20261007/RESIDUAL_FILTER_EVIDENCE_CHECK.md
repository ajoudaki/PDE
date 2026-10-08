# Residual-filtered integration: bounded evidence check

## Scope and current conclusion

This is an independent recomputation from saved arrays, not an independent
rerun of the scientific campaign. Inputs are the fixed contract in the study
README, `analyze_residual_filter.py`, the frozen producers, and records and
arrays under `data/generated/transparent_learning_dynamics_20261007/residual_filter_v1/`.
No scientific runs, source changes, other-study inputs, or global-proof claims
were used. The completed audit covers all 24 records: 16 dense and eight
causal runs, including the saved fresh-run reproduction. The completed
`RESIDUAL_FILTER_RESULT.md` is checked against these values and the source
definitions; this does not reproduce its prior-campaign comparisons.

The dense reference passes its prescribed refinement test decisively for the
tested width and seed. Residual filtering gives nonincreasing saved losses,
but the primary filtered step still has about 12–13% equal-time Gram bias.
Matched-loss discrepancies are appreciably smaller and decrease under mesh
refinement. This supports substantial timing bias, with a smaller remaining
matched-loss discrepancy; it does not identify an exact scalar clock
change or a new learning mechanism. Even the finest tested filtered step does
not meet the existing 1%-of-entrywise-change numerical gate.

For the completed causal cohort, lower-layer change errors on the same
filtered mesh are 27.33% TT and 31.41% TP, so the all-block 20% target is not
met. The 128-particle mesh-refinement check fails all four prescribed
entrywise gates, and the one particle-count change is substantial. All 19
saved reproduction arrays agree exactly, and filtered-write readout history
reconstructs to roundoff. These accounting and reproducibility successes do
not settle the unresolved trajectory accuracy.

## Observables and comparison conventions

There are 16 training and four passive inputs. For hidden layer
\(\ell\in\{1,2\}\),
\[
C^\ell_{ab}(\tau,\tau)
 =\frac1n h_a^{(\ell)}(\tau)^\top h_b^{(\ell)}(\tau),
\qquad
\Delta C^\ell(\tau)=C^\ell(\tau,\tau)-C^\ell(0,0),
\qquad \tau=2t/16.
\]
Here \(t\) is physical training time; saved normalized time is \(\tau\), and
the tabulated step \(h\) is its increment. TT contains all 256
training–training entries, TT off-diagonal contains 240 entries, and TP
contains 64 training–passive entries. For a difference matrix \(E\) and block
\(B\), the reported errors are
\[
\max_\tau\max_{(a,b)\in B}|E_{ab}(\tau)|,
\qquad
\max_\tau\sqrt{\frac1{|B|}\sum_{(a,b)\in B}E_{ab}(\tau)^2}.
\]
Relative trajectory errors divide the second quantity by the maximum block
RMS of reference \(\Delta C^\ell\). They are ratios of temporal maxima, not
the maximum of pointwise relative errors.

The raw loss is
\(\mathcal L(\tau)=16^{-1}\sum_{b=1}^{16}(y_b-f_b(\tau))^2\).
Matched-loss observations use linear interpolation between the saved samples
bracketing the first crossing of
\(\mathcal L(\tau)/\mathcal L(0)=r\). This is an interpolated diagnostic,
not a solver state evaluated at the exact crossing. For ensemble comparisons,
the analysis first averages losses and observables over seeds and then finds
the mean-loss crossing. This differs from averaging per-seed matched-loss
states. All reported dense crossings exist.

## Dense records and reference refinement

All 16 dense records have successful exit status, finite saved arrays, the
specified normalized horizon 19.2, and no saved loss increases. Losses
recomputed from labels and outputs agree to roundoff. The largest reported
linear-solve defect is \(5.55\times10^{-16}\). Recorded producer hashes agree
across runs and with the current frozen files. These checks concern the saved
trajectories, not an unconditional nonlinear-stability theorem.

At width 512, seed 101, RK4 steps .025 and .0125 differ as follows on their
common mesh:

| Observable | Maximum entry error | Maximum block-RMS error |
| --- | ---: | ---: |
| Layer 1 TT | 3.3163e-9 | 9.9597e-10 |
| Layer 1 TP | 4.3279e-9 | 1.4657e-9 |
| Layer 2 TT | 7.6139e-9 | 2.4843e-9 |
| Layer 2 TP | 9.2666e-9 | 3.1012e-9 |
| All 20 outputs | 2.5675e-8 | 1.2863e-8 |

Each passes the fixed maximum-entry gate
\(\max(10^{-5},.01\max|\Delta C^\ell|)\), with its analogous output
criterion. This is a check at one width and seed. The width-1024, three-seed
RK4 reference used for the principal ensemble comparison was not separately
step-halved for every draw. “Dense flow” below means the saved RK4 numerical
reference, not an exact continuous trajectory.

## Filtered dense bias at equal normalized physical time

The following maximum block-RMS errors compare width-512, seed-101 filtered
trajectories against RK4 step .0125 at common times. Their initial Grams are
identical, so absolute-Gram and initialization-subtracted errors coincide.

| Filtered step | Layer 1 TT | Layer 1 TP | Layer 2 TT | Layer 2 TP | Maximum output error |
| --- | ---: | ---: | ---: | ---: | ---: |
| .4 | .00916416 | .00781600 | .01113094 | .01477381 | .15950091 |
| .2 | .00518956 | .00442903 | .00626966 | .00833078 | .08925669 |
| .1 | .00277883 | .00237361 | .00335713 | .00445844 | .04757015 |
| .05 | .00144103 | .00123137 | .00174237 | .00231236 | .02461814 |

At step .2, these four errors are respectively 12.48%, 13.17%, 11.93%, and
12.55% of the reference block movement. Their maximum-entry errors are
.01375463, .01151598, .02709109, and .02503468. Removing TT diagonals does
not remove the discrepancy: layer-1 and layer-2 TT-off-diagonal RMS errors
are .00507249 and .00633119.

Errors decrease monotonically over the prescribed meshes. However, at step
.05 the four maximum-entry errors are .00384086, .00322934, .00752975, and
.00695863, whereas their 1% reference-change thresholds are .00097209,
.00081749, .00196282, and .00190296. They exceed the thresholds by factors
3.95, 3.95, 3.84, and 3.66. Stability and a favorable refinement trend therefore
do not make any of these filtered meshes a resolved 1%-accurate continuum
reference.

This is not peculiar to the single refinement draw. For width 1024, means of
seeds 101/202/303 at filtered step .2 versus means of the corresponding RK4
step-.025 draws give:

| Block | Maximum block-RMS bias | Relative bias |
| --- | ---: | ---: |
| Layer 1 TT | .00537410 | 12.39% |
| Layer 1 TP | .00474373 | 12.75% |
| Layer 2 TT | .00624890 | 11.70% |
| Layer 2 TP | .00831332 | 12.43% |

These are discrepancies of mean matrices, not average discrepancies of
individual runs. The corresponding maximum mean-output discrepancy is
.08918761.

## Matched-loss diagnostic: substantial lag, not an exact clock change

For width 512, seed 101, the RK4 interpolated time at 99% loss reduction is
\(\tau=5.58509109\). The table gives filtered times and block-RMS errors
relative to the RK4 movement at that same loss level. TT here excludes
diagonals, as specified by the mechanism diagnostic.

| Filtered step | Crossing time | Layer 1 TT off-diagonal | Layer 1 TP | Layer 2 TT off-diagonal | Layer 2 TP |
| --- | ---: | ---: | ---: | ---: | ---: |
| .4 | 6.624359 | 3.157% | 3.613% | 5.701% | 4.413% |
| .2 | 6.125001 | 1.731% | 1.944% | 3.127% | 2.409% |
| .1 | 5.861423 | .917% | 1.022% | 1.654% | 1.270% |
| .05 | 5.725061 | .474% | .526% | .853% | .654% |

At step .2 the corresponding absolute block-RMS errors are .00068368,
.00064464, .00163700, and .00159273. Their change-pattern cosines with RK4
are .999879, .999823, .999669, and .999798. A high cosine does not imply the
correct movement amplitude.

Earlier matched-loss differences are larger. At step .2, relative errors in
the same column order are 7.623%, 5.813%, 7.233%, and 6.141% at 50% loss
reduction; they are 4.194%, 4.068%, 5.240%, and 4.515% at 80% reduction.
The corresponding filtered/reference crossing times are
2.171447/1.943635 and 3.499021/3.158180.

Thus much of the equal-time discrepancy is consistent with delayed progress
in the filtered scheme. Nevertheless, a single matched scalar loss does not
match residual directions or the learned state. The remaining block errors
are far above RK4 refinement differences and decline with the filtered step.
They are consistent with smaller finite-mesh path bias, but also include
matched-loss interpolation error, which this check has not bounded separately.
They are not evidence that filtered sample mixing is a physical
feature-learning mechanism. The available arrays do not establish
that all other observables become identical under a scalar reparametrization
of time.

## Layerwise feature displacement

The saved `motion1` and `motion2` are squared individual-feature displacements,
not Gram-change magnitudes. For training or passive index set \(A\), define
\[
M_{\ell,A}(\tau)
 =\sqrt{\frac1{|A|}\sum_{a\in A}
 \frac1n\|h_a^{(\ell)}(\tau)-h_a^{(\ell)}(0)\|^2}.
\]
The causal equivalent is the square root of the mean of
\(C^\ell_{aa}(\tau,\tau)+C^\ell_{aa}(0,0)-2C^\ell_{aa}(\tau,0)\).
It requires a two-time Gram; a difference of equal-time Gram diagonals is
not this displacement.

At the interpolated 99%-loss-reduction stage, width 512 and seed 101 give:

| Method | Training layer 1 | Training layer 2 | Passive layer 1 | Passive layer 2 |
| --- | ---: | ---: | ---: | ---: |
| RK4 .0125 | .30924099 | .32353546 | .28111538 | .31364506 |
| Filtered .4 | .30525226 | .31916130 | .27844253 | .30944302 |
| Filtered .2 | .30696450 | .32108820 | .27949488 | .31126959 |
| Filtered .1 | .30800591 | .32222672 | .28020925 | .31237122 |
| Filtered .05 | .30859418 | .32285606 | .28063342 | .31298333 |

At this late matched-loss stage, the primary step suppresses both layers'
RMS motion slightly; it does not support a substantial qualitative
redistribution of motion between layers. This stage-specific finding does not
establish the same behavior at every time or for every draw. Layer motion is
not a conserved budget.

## Completed causal comparison

The principal comparison is between means of three 256-particle causal draws
(seeds 1701/1702/1703) and three width-1024 dense draws (101/202/303), at
normalized filtered step .2. The second dense reference is RK4 step .025
on those same dense seeds, sampled at the filtered times. In each realization
the initial Gram is subtracted before averaging. A particle count is not a
dense width.

I independently recomputed all six absolute/change accuracy rows, particle
and width differences, refinement gates, and envelope flags from raw arrays.
Checked summary quantities agree to at most \(2.22\times10^{-15}\), including
the alternative summation order used for the memory identity below.

| Layer/block | Same-filtered maximum RMS | Relative error | Against RK4 maximum RMS | Relative error |
| --- | ---: | ---: | ---: | ---: |
| 1 TT | .01191117 | 27.328% | .01257418 | 28.987% |
| 1 TT off-diagonal | .01188465 | 29.294% | .01269963 | 31.442% |
| 1 TP | .01172683 | 31.406% | .01177346 | 31.656% |
| 2 TT | .00915732 | 17.385% | .01041148 | 19.492% |
| 2 TT off-diagonal | .00910996 | 17.108% | .01058804 | 19.565% |
| 2 TP | .00816817 | 12.373% | .01019121 | 15.235% |

The four primary same-filtered maximum-entry errors are .03015929,
.02771580, .02178753, and .01757073 in layer-1 TT/TP, layer-2 TT/TP order.
Absolute-Gram errors are also nonzero: same-filtered maximum RMS values in
that order are .01373922, .01258848, .01101984, and .00957676. The lower-layer
discrepancy therefore is not solely a diagonal-norm effect or an artifact of
how initial differences are subtracted.

The lower layer misses the predeclared 20% target even on the same filtered
mesh. The upper layer meets that numerical target here, but the combined
all-block hypothesis is not an empirical pass. This is a finite-cohort
failure of the requested accuracy threshold, not a falsification of a
continuum population law.

The descriptive envelope has no sustained excess flags in any of the six
rows for either absolute Grams or changes. The largest positive change-error
excess before the extra sustained-excess threshold is .00242535; the
corresponding maximum for layer 1 is .00208517. These facts coexist with the
failed relative-error target: the envelope is broad and descriptive, not a
replacement accuracy criterion or a calibrated confidence bound.

## Causal mesh and particle changes

At 128 particles, seed 1701, compare filtered steps .2 and .1 on common times:

| Layer/block | Maximum entry change | Maximum RMS change | Entrywise gate threshold | Gate |
| --- | ---: | ---: | ---: | --- |
| 1 TT | .00730725 | .00266661 | .00114635 | Fail |
| 1 TP | .00713415 | .00284216 | .00095427 | Fail |
| 2 TT | .02647683 | .00609404 | .00178289 | Fail |
| 2 TP | .01608493 | .00558719 | .00208729 | Fail |

The output maximum-entry change is .04329570. Excluding training diagonals
still fails: maximum-entry changes are .00730725 and .01674590 in layers 1
and 2, with thresholds .00101228 and .00178289. This checks finite-particle
programs on different meshes; one adaptive-quadrature seed does not isolate
a pure deterministic truncation-error coefficient. In any event it does not
provide the required resolution evidence. The principal 256-particle
ensemble has no .1-mesh counterpart in this fixed cohort.

At step .2 and seed 1701, increasing particle count from 256 to 512 gives
the following changes of initialization-subtracted trajectories:

| Layer/block | Maximum entry change | Maximum RMS change |
| --- | ---: | ---: |
| 1 TT | .03996125 | .01396159 |
| 1 TP | .04259658 | .01368358 |
| 2 TT | .03944188 | .01792406 |
| 2 TP | .05868243 | .01913625 |

These are comparable to, or larger than, the principal mean discrepancies.
The off-diagonal TT maximum RMS changes are .01416890 and .01788029.
The corresponding dense width-512 versus width-1024 three-mean changes are
.00734765, .00693248, .00737238, and .00669099 on the four primary blocks.
These are distinct approximation axes; one change along either axis does
not estimate a limiting error or demonstrate convergence. They leave
sampling/quadrature and numerical-resolution explanations active.

## Causal matched-loss and individual-feature checks

All saved ensemble matched-loss diagnostics and displacement values were
independently reconstructed; their agreement with the analysis summary is
at roundoff. At 99% reduction of mean raw loss, the causal, filtered dense,
and RK4 mean crossings are 6.17393150, 6.13044552, and 5.57567139.

Against the RK4 mean at its own matching stage:

| Layer/block | Causal RMS error | Relative error | Change-pattern cosine |
| --- | ---: | ---: | ---: |
| 1 TT off-diagonal | .01110820 | 28.745% | .957813 |
| 1 TP | .01091927 | 31.302% | .950188 |
| 2 TT off-diagonal | .00829799 | 15.722% | .987632 |
| 2 TP | .00742737 | 11.175% | .994148 |

The lower-layer discrepancy does not disappear at matched mean loss.
Nevertheless, training RMS individual-feature displacements are
.32207749/.31793612 for causal/RK4 layer 1 and .32776336/.32810924 for
layer 2. Passive values are .29824354/.28619534 and .31062709/.31142768.
Similar displacement amounts therefore do not establish the correct
pairwise feature associations. This is a diagnostic distinction, not an
identification of a defective memory or reciprocal term: the mesh and
particle checks above remain unresolved.

## Reproduction, exact write accounting, and completed metadata

All 19 saved arrays in the fresh repetition of causal 256-particle seed 1701,
step .2, have exactly zero elementwise difference from the original. This
includes full two-time Grams, backward pairings, response arrays, raw and
filtered deficits, and motions, not only the headline observables. I checked
the two already-saved runs; I did not launch this reproduction.

For zero initial readout, the discrete filtered write identity is
\[
f_a^k=h\sum_{j<k}\sum_{b=1}^{16}
 \widetilde c_b^{\,j}C^2_{ab}(k,j).
\]
Here \(\widetilde c^{\,j}\) is the stored filtered training-write vector
`write_deficit[j]`, \(h=.2\), and \(C^2_{ab}(k,j)\) is the saved population
average of the current layer-2 feature for query \(a\) times the historical
layer-2 feature for training input \(b\). Reconstructing
the 256-particle seed-1701 output by direct historical matrix products gives
maximum error \(1.55\times10^{-15}\). The analyzer's contracted summation
agrees at roundoff. Substituting raw deficits instead gives .17147975 error;
the largest raw-versus-filtered deficit difference is .04766227. This checks
the actual numerical write history, not its accuracy relative to gradient
flow.

All 24 successful records have finite saved arrays, raw-loss consistency,
nonincreasing saved losses, and normalized horizon 19.2. Total recorded
numerical wall time is 1277.377619 seconds (21.2896 minutes); maximum
recorded peak resident memory is 10790.582 MiB (10.5377 GiB). There are zero
unstable flags and zero positive saved relative-loss increases. Frozen
producer hashes remain identical across records and match their source
files. These values respect the stated 24-run/30-minute/12-GiB campaign
limits; they are recorded numerical-run resources, not all analysis overhead.

The largest causal solve defect is \(5.55\times10^{-16}\). Across all causal
records, the two Gaussian-factor diagnostics report maximum covariance
errors \(2.5242\times10^{-8}\) (`eta`) and \(1.2287\times10^{-8}\) (`xi`),
and maximum discarded variances \(4.4891\times10^{-13}\) and
\(2.5530\times10^{-12}\). These small internal factorization diagnostics do
not bound finite-particle sampling error or the observed trajectory bias.

## Static analysis audit and claim limits

The block extraction, own-initialization subtraction, common-mesh strides,
and mean-matrix errors in `analyze_residual_filter.py` agree with the metric
definitions above. Several interpretation limits must remain explicit:

- The descriptive envelope combines three estimated standard errors with
  one particle-count change and one width change. It is not a calibrated
  simultaneous confidence bound. It applies to same-integrator comparisons
  and contains no time-bias allowance.
- Causal time refinement is at 128 particles, whereas the principal means
  use 256. The particle change is one 256-to-512 comparison at seed 1701.
  Neither independently establishes convergence of all principal draws.
- The causal refinement gate uses maximum-entry error; the principal
  relative trajectory errors use block RMS. Passing a 20% RMS comparison is
  not passing the 1% numerical-refinement criterion.
- The updated analysis now reports RMS displacement in `matched_loss_motion`,
  includes `reference_normalized_time`, and correctly calls the dense-only
  time field `filtered_time`. These repair the preliminary audit's reporting
  omissions without changing the frozen scientific producers. For an
  ensemble, square root of mean squared motion remains distinct from mean
  of per-seed RMS motions.
- The figure plots Gram-change RMS, not \(M_{\ell,A}\). Missing crossings
  and zero reference norms are not guarded in callers, but all checked
  stages exist and have nonzero reference movement.

The report's principal values and finite-program versus continuous-flow
distinction agree with this audit. Neither exact reproduction, roundoff
memory accounting, stable losses, nor absence of sustained descriptive-envelope
excess upgrades the failed lower-layer relative-accuracy or time-refinement
checks. The campaign is complete; its continuous-trajectory accuracy question
is not resolved, and no global guarantee follows.

Audit source snapshot: `analyze_residual_filter.py` SHA-256
`cab26469eb29fd46aeade5d022e852c50d10dff8c5722231633d1245983f23a0`.
The frozen base producer hash is
`eb58b62ca466649989067cd1287aa199b99b41899b59536cec02baa186c78b2d`;
the residual-filter experiment producer hash is
`1dceb072e71362eac0f1a5b8a96dddb45db826c4c1068ad99943e54b6e289e50`.
