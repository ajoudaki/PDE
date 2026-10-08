# Frozen fresh-quadrature check

## Scope and completed verdict

This bounded audit reads the registered “Fresh-quadrature self-consistency
audit” contract, `frozen_population_replay.py`, the existing filtered and
panel producers, the new cohort driver, and its analysis. No scientific
runs or main-source edits were performed by this reviewer. All four completed
replays and the saved analysis have now been checked using their raw arrays.

The registered result is inconclusive, not a self-consistency pass and not a
validated explanation. Fresh ensemble lower-layer corrections exceed 20% of
dense movement and nominally remove more than half the old mean discrepancy,
but fail the predeclared fresh-quadrature resolution gate. Upper-layer means
pass that resolution gate, but corrections are in the intermediate 5–20%
range; the upper training–passive change error increases slightly. No primary
block satisfies the full registered explanation criterion.

The frozen replay has no identified scientific-launch blocker. Its local
equations, temporal covariance construction, primitive independence, fixed
forcing, and passive-input treatment match the intended frozen full-model
diagnostic. This is a necessary current-moment consistency check, not an
autonomous solver, a test of every response coefficient, or a guarantee about
the original continuous population law.

The producer contains same-primitive, zero-label, singular-covariance,
materially-indefinite-covariance, individual-displacement, and exact
readout-history tests. The supervisor reports that its pre-execution tiny
test passed with zero local-field errors and singular-factor reconstruction
error about 2.7e-15. This reviewer inspected those assertions but did not
execute a new test or independently rerun the scientific source trajectories.

## What is fixed, and what is integrated afresh

There are 16 training and four passive input directions. The normalized
time step is \(h=2\Delta t/16=.2\). The replay fixes the recorded arrays
\(C^1,D^2,R^h,R^\delta\) and the effective training-write vectors
\(\widetilde c^k=\texttt{write_deficit[k]}\). In these arrays, evaluated
time/sample precede driving time/sample. Their sample and time dimensions
are retained; no response history is inferred from the new particles.

For each fresh particle, let \(z_a^{(1),k},z_a^{(2),k}\) denote its layer
preactivations, \(h_a^{(\ell),k}=\tanh z_a^{(\ell),k}\) its features, and
\(w^k\) its readout. Its upper backward field is
\(\delta_a^{(2),k}=w^k[1-(h_a^{(2),k})^2]\).
The upper circuit uses only strictly earlier backward fields:
\[
z_a^{(2),k}=\eta_a^k+
 \sum_{j<k}\sum_{b=1}^{16}
 \bigl[R^h_{ab}(k,j)+hC^1_{ab}(k,j)\widetilde c_b^j\bigr]
 \delta_b^{(2),j}.
\]
The lower backward pre-gate field includes current response contributions:
\[
\begin{aligned}
b_a^{(1),k}={}&\xi_a^k+
 \sum_{j\le k}\sum_{b=1}^{16}R^\delta_{ab}(k,j)h_b^{(1),j}
 +h\sum_{j<k}\sum_{b=1}^{16}
 D^2_{ab}(k,j)\widetilde c_b^j h_b^{(1),j}\\
&+\mathbf1_{a>16}R^\delta_{aa}(k,k)h_a^{(1),k}.
\end{aligned}
\]
Its lower backward field is
\(\delta_a^{(1),k}=[1-(h_a^{(1),k})^2]b_a^{(1),k}\).
Writing \(S_{ab}=v_a^\top v_b\) for the fixed input Gram, the updates are
\[
z_a^{(1),k+1}=z_a^{(1),k}
 +h\sum_{b=1}^{16}S_{ab}\widetilde c_b^k\delta_b^{(1),k},
\qquad
w^{k+1}=w^k+h\sum_{b=1}^{16}\widetilde c_b^k h_b^{(2),k}.
\]
The passive-current term is an evaluation response, not a passive forcing
term. Passive indices enter neither parameter forcing sum. The source and
replay computations implement the same ordering, including the zero initial
readout and the strictly past readout history at saved step \(k\).

No fresh raw residual, feature Gram, backward Gram, or prediction feeds back
into these equations. Labels are used for diagnostic loss; effective writes
remain their recorded values. Dense arrays are read only by the downstream
comparison analysis, not by the replay. Source \(C^2,D^1,f\) are used for
comparison or source-motion reconstruction, not for evolving fresh fields.

## Temporal Gaussian construction and covariance limits

The initial lower root is a standard Gaussian vector in the original
eight-dimensional input space, multiplied by the input-direction matrix.
The full temporal Gaussian families have target covariances
\[
\mathbb E[\eta_a^k\eta_b^j]=C^1_{ab}(k,j),
\qquad
\mathbb E[\xi_a^k\xi_b^j]=D^2_{ab}(k,j).
\]
The factorization flattens each covariance in `(time, sample)` order. Each
fresh row multiplies one factor spanning the full time grid, so time slices
are not incorrectly sampled independently. Root, eta, and xi use distinct
Gaussian child streams, as do all batches. The draws are unwhitened iid rows;
their finite-sample covariance is not forced to equal its target.

The factor routine symmetrizes only within a declared roundoff tolerance,
rejects materially negative eigenvalues, and retains eigenvalues strictly
above \(10^{-12}\lambda_{\max}\) for this cohort. It records negative
eigenvalues, discarded positive trace, retained rank, asymmetry, and maximum
entry/Frobenius reconstruction errors. The scientific runner rejects a factor
whose maximum-entry reconstruction error exceeds 1e-8.

Fresh factors target the saved raw empirical Grams, not the original
chronological sampler's slightly truncated innovation factors. Consequently
the fresh/source difference includes this disclosed covariance retargeting.
A small covariance-matrix discrepancy alone is not a propagated bound on
nonlinear output discrepancies. More fresh samples also cannot restore
covariance directions missing from the source's 256-particle Gram.

The new integration law treats source arrays as externally fixed. It should
not be identified with the conditional distribution of the original adaptive
particles given their fitted coefficient path: that selection can create
dependencies. Fresh-batch standard errors describe the new frozen-circuit
integration only, excluding source-path uncertainty and uncertainty of the
dense comparison.

## Current Grams, actual displacement, and history identity

The producer keeps current Gram matrices and each batch's changes from its
own initialization. It separately computes actual squared displacement,
\[
\texttt{motion}\ell_a(k)
 =\frac1N\sum_{i=1}^N
 [h_{i,a}^{(\ell),k}-h_{i,a}^{(\ell),0}]^2.
\]
The source version is reconstructed as
\(C^\ell_{aa}(k,k)+C^\ell_{aa}(0,0)-2C^\ell_{aa}(k,0)\).
For training or passive panel \(A\), actual RMS displacement is
\(\sqrt{|A|^{-1}\sum_{a\in A}\texttt{motion}\ell_a(k)}\), not a Gram-change
RMS and not an unsquared motion difference. Source and fresh circuits have
their own initial features.

The saved readout identity is checked particlewise first:
\[
w_i^k=h\sum_{j<k}\sum_{b=1}^{16}
 \widetilde c_b^j h_{i,b}^{(2),j}.
\]
Multiplication by the current query feature and averaging gives the matching
prediction-history identity. Both checks use filtered writes, never raw
diagnostic residuals. The runtime checks enforce maximum error below 1e-10.
This validates arithmetic accounting, not trajectory accuracy.

The registered run does not enable optional full fresh two-time Gram output
and does not recompute fresh responses. Therefore current-moment consistency
cannot be promoted to self-consistency of all frozen coefficients.

## Conditional uncertainty and registered gates

For a given layer and block, let \(X_{r,b}(k)\) be the batch Gram change for
source path \(r\) and batch \(b\), with 32 batches per source. If \(J\)
source paths are averaged, the entrywise conditional standard-error estimate
implemented by the analysis is
\[
\mathrm{SE}_{ab}(k)^2=
 \frac1{J^2}\sum_{r=1}^J\frac1{32\cdot31}
 \sum_{b'=1}^{32}
 [X_{r,b';ab}(k)-\overline X_{r;ab}(k)]^2.
\]
Batch changes are formed before estimating this variance, preserving
within-batch time-zero/current covariance. The block scale is the RMS of
entrywise SEs. It estimates RMS matrix-mean integration noise, not the
standard error of a nonlinear discrepancy norm.

The analysis correctly checks maximum-over-time three-SE block scale and
raw independent-half difference against 5% of the dense mean change scale.
Materiality compares the correction with 20% of that scale and with three
SEs at the correction's own peak time. The explanation criterion additionally
requires at least 50% reduction of the maximum-over-time dense-comparison
error; reducing only the old peak-time error would not suffice.

The first-8192/16384/32768 averages overlap, so their differences are correlated
sensitivity checks rather than independent replications. Half-population
differences use disjoint batches but are noisier than the full-mean error;
the registered gate intentionally uses their raw difference. The exact repeat
is not an additional independent integration sample.

For directional interpretation, the initial analysis defines old error as
source minus dense and correction as fresh minus source. Its cosine is over
the stacked time/block arrays; negative values indicate correction toward
dense. Alignment alone can still overshoot. Cross-source correction scatter
includes both source-path variability and fresh integration noise.

Before interpreting outputs, the initial analyzer needed the following
reporting corrections, identified during the initial analysis review, before
interpreting the completed cohort:

- Unresolved quadrature must override a negligible/material classification.
  A small measured magnitude alone cannot support negligible defect if
  either resolution gate fails. Overall negligible requires all four
  primary ensemble blocks.
- The registered explanation decision is ensemble-only; per-source error
  reductions are descriptive.
- Absolute current-Gram fresh/dense and source/dense comparisons must be
  reported alongside change comparisons and fresh/source differences.
- Squared-motion differences do not replace the requested RMS feature
  displacements for source/fresh and training/passive panels.

These analysis/reporting issues were corrected without additional scientific
runs or changes to the frozen producer. The final analyzer includes
`material_resolved_defect`, `negligible_resolved_defect`, absolute dense
comparisons, and RMS individual displacements. Magnitude-only flags remain
descriptive; interpretation must use the resolved flags and the ensemble-only
registered criterion. Every checked block's `explains_at_least_half` is false.

## Independent saved-batch arithmetic

All 24 rows (six layer/block combinations, each ensemble and three
single-source comparisons) and additional observables were reconstructed
without invoking the analyzer. The 774 checked numerical values/flags agreed
within 4.45e-16. Another 198 stored means, paired-change standard errors,
halves, prefixes, and raw-loss diagnostics reproduce exactly from the batches.
The later exploratory projection's 48 numerical values also reproduce exactly.

The dense reference here is the previous three-seed, width-1024 **filtered
step-.2 mean**, not RK4 or an exact continuous flow. Each current Gram has its
own initialization subtracted before forming the following change comparisons.

| Layer/block | Fresh correction RMS | Correction/dense movement | Old dense-error RMS | Fresh dense-error RMS | Error remaining |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 TT | .01017198 | 23.34% | .01191117 | .00537184 | 45.10% |
| 1 TT off-diagonal | .01005857 | 24.79% | .01188465 | .00541224 | 45.54% |
| 1 TP | .01025895 | 27.47% | .01172683 | .00567258 | 48.37% |
| 2 TT | .00747139 | 14.18% | .00915732 | .00839401 | 91.66% |
| 2 TT off-diagonal | .00749346 | 14.07% | .00910996 | .00843326 | 92.57% |
| 2 TP | .00798017 | 12.09% | .00816817 | .00851909 | 104.30% |

RMS values are maxima over the saved time grid; the ratio of maxima need not
describe error reduction at one common time. These are means of frozen
replays, not the observed accuracy of a recoupled trajectory.

The four primary ensemble resolution tests are:

| Layer/block | Maximum three-SE RMS | Maximum half-difference RMS | 5% threshold | Resolution |
| --- | ---: | ---: | ---: | --- |
| 1 TT | .00278987 | .00194662 | .00217928 | Fail: SE |
| 1 TP | .00271426 | .00188761 | .00186699 | Fail: SE and halves |
| 2 TT | .00219002 | .00155201 | .00263363 | Pass |
| 2 TP | .00219957 | .00125740 | .00330091 | Pass |

Layer-1 TT off-diagonal also fails its SE criterion; layer-2 TT off-diagonal
passes both criteria. All ensemble correction peaks occur at the endpoint
\(\tau=19.2\), where each correction exceeds its own three-SE scale. That
fact does not waive the stricter predeclared resolution test. No measured
ensemble correction is below the 5% negligible threshold.

All 18 single-source rows fail quadrature resolution. Their ratios of fresh
to old maximum dense-comparison error, using the same fixed dense ensemble
reference, are retained rather than selected for favorable direction:

| Source | Layer 1 TT | Layer 1 TP | Layer 2 TT | Layer 2 TP |
| --- | ---: | ---: | ---: | ---: |
| 1701 | .5794 | .5733 | .9104 | 1.0242 |
| 1702 | .6802 | .7222 | .6216 | .7625 |
| 1703 | .4994 | .5817 | 1.0051 | .9460 |

These single-source numbers are descriptive, not three independent passes
of an ensemble-only explanation criterion. Source-to-source correction
scatter is appreciable: the four primary ensemble correction standard-error
summaries are .00965661, .00872237, .00909756, and .00864317. They mix
coefficient-path variability with fresh integration noise and must not be
presented as pure source-coefficient uncertainty.

Absolute current-Gram errors are different from change errors. On the four
primary blocks, old/fresh maximum RMS discrepancies from the dense mean are
.01373922/.00700634, .01258848/.00653579, .01101984/.00875488, and
.00957676/.00749430. In particular, the upper TP absolute error improves even
though its initialization-subtracted error worsens. Neither metric should
be silently substituted for the other.

## Motion, prediction, and exploratory direction diagnostics

Endpoint individual-feature RMS displacements are:

| Layer/panel | Source | Fresh frozen replay |
| --- | ---: | ---: |
| 1 training | .33502047 | .33266122 |
| 1 passive | .31079188 | .30156880 |
| 2 training | .33968346 | .34020170 |
| 2 passive | .32012653 | .32516595 |

Thus the pairwise correction is not captured by a uniform rescaling of
individual displacement amounts. Maximum changes of mean predictions,
current lower backward Gram, and current upper backward Gram are .05454317,
.57093293, and .17475960, respectively. These additional observables have not
been assigned new pass/fail thresholds after observing them.

The loss of the ensemble-mean prediction at the endpoint changes from
9.3193e-10 to .00315289 relative to initial loss. This is not mean loss across
source paths and is not a fresh training objective: the forcing was never
updated to correct that diagnostic residual.

The final analyzer adds an explicitly post-test directional diagnostic. For
the stacked old error \(E=\Delta C_{\rm source}-\Delta C_{\rm dense}\) and
fresh correction \(Q=\Delta C_{\rm fresh}-\Delta C_{\rm source}\), it reports
\(\langle E,Q\rangle/\|E\|_F^2\) and its conditional batch standard error.
The old direction is fixed relative to the fresh draws. On the four primary
blocks these are -.764915±.021439, -.762210±.023478, -.407864±.017184, and
-.420107±.019907, where ± denotes **one estimated conditional SE**, not a
confidence interval. They indicate a coherent favorable projection, but the
upper TP maximum error can still worsen. Projection precision is not full
matrix precision, and these post-test quantities do not replace the failed
registered resolution/explanation gates.

## Reproduction, numerical factors, and provenance checks

Four successful runs used 32768 samples each in 32 batches of 1024. All 92
saved arrays per run are finite. The fresh repeat matches all 91 deterministic
arrays exactly; `batch_seconds` is excluded because runtime is not
deterministic. Archive/record hashes, embedded source arrays, configurations,
producer hashes, commands, seeds, and source sampler provenance agree.
Recorded total scientific wall time is 78.435998 seconds; peak RSS is
440012 KiB, or 429.699219 MiB. The fixed four-run budget was respected.

A delegated read-only check independently refactored the six saved covariance
targets, without simulating any local trajectories. Eigenvalue arrays and
reconstruction diagnostics agree exactly with the saved values:

| Source | Family | Rank | Maximum entry reconstruction error | Discarded positive trace |
| --- | --- | ---: | ---: | ---: |
| 1701 | eta | 248 | 1.05155e-11 | 1.43884e-9 |
| 1701 | xi | 241 | 2.07897e-10 | 2.88141e-8 |
| 1702 | eta | 244 | 8.11062e-12 | 1.51903e-9 |
| 1702 | xi | 233 | 2.98558e-10 | 3.29330e-8 |
| 1703 | eta | 244 | 9.48736e-12 | 1.75245e-9 |
| 1703 | xi | 233 | 2.83891e-10 | 3.61569e-8 |

All targets have dimension 1940. Their minimum eigenvalues lie between
-1.43622e-12 and -8.56471e-14, within the declared roundoff tolerance;
the absolute sums of negative eigenvalues lie between 3.87759e-12 and
3.55082e-11. Every reconstruction passes the 1e-8 gate. This numerical
factorization success is separate from the finite-integration resolution
failures above.

Maxima recomputed from saved per-batch identity-error arrays are
1.33227e-14 for readout-vector history and 1.33227e-15 for prediction history,
passing the 1e-10 gate. Full fresh local fields/two-time Grams were not saved,
so this audit validates those recorded diagnostics and their source formulas;
it does not independently reconstruct the fresh identities from unsaved
primitives. The source-level same-primitive test remains the supervisor's
pre-execution validation described above.

The numerical evidence supports a potentially important finite-integration
explanation for part of the lower-layer discrepancy, but the predeclared
resolution rule leaves that explanation unvalidated. Upper-layer corrections
are resolved only as this conditional frozen-circuit diagnostic and remain
intermediate in size. None of these findings establishes convergence of the
adaptive source program or a general theorem.

## Source provenance

Reviewed frozen replay SHA-256:
`b0b5e1f519f936c7286e7101ec33a09b68ac4127ab72015207df93b06ef7d4c0`.
The driver is
`b428d97f371b5bdd954f73e317fc65c7100441fdc871b5232762f5c5c03e0614`.
The final inspected analyzer and matching saved summary use
`086a10c9f76b9e2c3ad3fac23a3614965c1d70ca1f38e32ee40679dd8573314c`.
It supersedes the preliminary reporting logic discussed above; the scientific
producer was not changed.
The driver fixes the four registered runs, their seeds, 32768 samples in 32
batches of 1024, serial execution, no overwrite, and the 1200-second remaining
recorded-work timeout. The replay process imposes the 12-GiB address-space
limit and checks source-array/source-code hashes before saving its result.
