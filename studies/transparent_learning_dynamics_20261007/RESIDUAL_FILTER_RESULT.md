# Stable steps are not yet accurate trajectories

2026-10-07. Numerical continuation of the same causal feature–response system
on the previously unresolved 16-input panel. Global proofs and two-input
approximation work remain paused.

Current status: all 16 dense and eight causal runs are complete, including
the prescribed refinements and a fresh repeated causal run. The independent
saved-array audit confirms the arithmetic. The outcome is **stable but still
numerically unresolved**: the lower-layer accuracy target is missed, and
particle and time-step uncertainties remain substantial.

Subsequent [fresh-quadrature diagnostic](FROZEN_QUADRATURE_RESULT.md): re-evaluating
these coefficient histories with independent particles shifts lower similarities
toward dense, but does not meet every fresh-resolution gate. Because those
histories remain frozen, it does not replace this coupled-model accuracy table.

## What has changed

The dense continuous-flow reference is now well resolved on the checked draw:
halving the normalized RK4 step from 0.025 to 0.0125 changes the two hidden
feature Grams by at most \(4.33\times10^{-9}\) and
\(9.27\times10^{-9}\), and predictions by at most
\(2.57\times10^{-8}\). This repairs the previous reference's failed
full-horizon refinement check, for the tested width and seed.

A residual-filtered time integrator also removes the large loss oscillations
in all eight tested causal runs. But stability has not completed the accuracy
task. Their lower-layer mean similarity changes still differ from the dense
comparison on the **same filtered mesh** by 27–31%, missing the predeclared
20% target. The upper layer is closer on that mesh, at 12–17%.
The entire candidate is retained; no memory channel is
discarded and no result is recast as a global theorem.

## 1. Same system, different numerical step

The finite-step population program changes. Its intended continuous flow
does not, but convergence to that flow is not established by consistency alone.
This matters because the candidate's currently rigorous construction is discrete.

Keep exactly the previous two-hidden-layer tanh model, Gaussian initialization,
zero readout, mean squared loss, 16 nonorthogonal training inputs in dimension
8, varied mixed-sign labels of magnitudes 0.25–0.70, and four unlabeled passive
inputs. These exploratory labels are not certified against the original
conservative theorem's small-label cap. The normalized
input Gram is \(S_{ab}=v_a^\top v_b\). At each current state, write
\(C^\ell_{ab}=h_{\ell,a}^\top h_{\ell,b}/n\) and
\(D^\ell_{ab}=\delta_{\ell,a}^\top\delta_{\ell,b}/n\), using population
expectations for the causal model. The raw training deficit is
\(c_a=y_a-f_a\). Only training indices appear in the following solve.

For normalized time step \(h=2\Delta t/m\), form the current training kernel
and filtered write coefficient:

\[
K=(C^2+C^1\odot D^2+S\odot D^1)_{1:m,1:m},
\qquad
\widetilde c=(I+hK)^{-1}c.
\]

Here \(\odot\) denotes entrywise multiplication. Use \(\widetilde c\),
instead of \(c\), in **every** new parameter or learned-history write.
Recompute features, the kernel and reciprocal responses at every step.
The filter does not freeze a kernel or supply future dense information.
All prior writes retain the filtered coefficients from their own write time.
Raw \(c\) remains the residual used to measure loss. Passive inputs never
enter the solve or a forcing sum.

For the finite dense model, this step exactly contracts the current
*linearized* residual: a kernel eigenmode of eigenvalue \(\lambda\ge0\)
is multiplied by \(1/(1+h\lambda)\), instead of Euler's
\(1-h\lambda\). It is first-order consistent with the same canonical
gradient flow because \(\widetilde c-c=-hK\widetilde c\).
Nonlinear Taylor terms remain: this is not unconditional actual-loss descent,
second-order integration, or a path-accuracy theorem.

For the population program, all formal local derivatives freeze the global
write coefficients \(\widetilde c\). They do not differentiate the
self-consistent population kernel through an individual primitive probe.
The current backward field is computed before the filter, so its
\(D^1\) contribution is available without an algebraic loop.
The full derivation, independent finite-Jacobian check and edge cases are in
[the integrator audit](RESIDUAL_FILTER_INTEGRATOR_CHECK.md).

The finite-particle kernel expression is not asserted to equal the Jacobian
of the entire adaptive Gaussian-sampling algorithm. Local consistency of
the population write formula also does not prove convergence of growing
response histories. These are separate unresolved matters.

## 2. Fixed comparison and the primary result

The horizon remains \(2t/m\in[0,19.2]\), equivalently physical time
\([0,153.6]\). Primary filtered step is 0.2, giving 96 updates and 97 saved
states. Dense width-1024 means use seeds 101/202/303; causal 256-particle
means use seeds 1701/1702/1703. A causal particle is a quadrature sample,
not a neuron of a dense network of the same stated width.

For each realization subtract its own initial Gram, then average. Each
table error is the maximum over saved times of the RMS of the **difference
matrix** in the stated block. Divide by the corresponding dense mean
movement's maximum-time block RMS for the relative column. Maxima need not
occur at the same time. Training–training includes diagonals here; the
analysis also reports the off-diagonal block separately.

| Hidden layer | Block | Same-filtered-mesh error, RMS | Relative error | Against dense RK4, RMS | Relative error |
|---:|:---|---:|---:|---:|---:|
| 1 | training–training | 0.011911 | 27.33% | 0.012574 | 28.99% |
| 1 | training–passive | 0.011727 | 31.41% | 0.011773 | 31.66% |
| 2 | training–training | 0.009157 | 17.39% | 0.010411 | 19.49% |
| 2 | training–passive | 0.008168 | 12.37% | 0.010191 | 15.23% |

The RK4 comparison uses the means of width-1024 step-0.025 reference runs,
sampled at the filtered times. Its step-halving control is width 512,
seed 101; numerical accuracy has not been individually certified for every
ensemble draw. These are finite numerical references, not exact solutions.

The previous ordinary-Euler means had 57–67% relative errors. The new
comparison is substantially better but not a pass in every block. Its
particle count and step differ from that previous ensemble, so this contrast
is not a convergence-rate estimate or a perfectly matched single-variable
ablation. The same-initialization dense integrator comparisons below isolate
the numerical change more directly.

The [time-resolved figure](../../data/generated/transparent_learning_dynamics_20261007/residual_filter_v1/analysis/integration_repair.png)
shows the full saved horizon. Its upper row plots Gram-change magnitudes;
its lower row plots actual matrix-discrepancy RMS, which can be appreciable
even when the upper curves look close. The analysis also saves all-time
blockwise curves in CSV and NPZ, and reports absolute-Gram errors separately
from initialization-subtracted errors.

## 3. Time accuracy: damping the instability does not remove bias

At width 512 and seed 101, compare filtered dense paths with the RK4
step-0.0125 reference, at equal normalized physical times:

| Filtered step | Layer 1 TT RMS | Layer 1 TP RMS | Layer 2 TT RMS | Layer 2 TP RMS | Largest prediction difference |
|---:|---:|---:|---:|---:|---:|
| 0.4 | 0.009164 | 0.007816 | 0.011131 | 0.014774 | 0.15950 |
| 0.2 | 0.005190 | 0.004429 | 0.006270 | 0.008331 | 0.08926 |
| 0.1 | 0.002779 | 0.002374 | 0.003357 | 0.004458 | 0.04757 |
| 0.05 | 0.001441 | 0.001231 | 0.001742 | 0.002312 | 0.02462 |

TT denotes training–training and TP training–passive. These errors decrease
under the predeclared refinements, consistent with first-order accuracy.
Nevertheless, **even step 0.05 does not pass the existing 1%-of-feature-change
entrywise numerical gate**: its four block errors exceed those thresholds by
factors 3.66–3.95. The primary filtered step's block-RMS bias is about 12–13%
of the dense feature movement. Stable loss is insufficient to claim a
numerically resolved continuous trajectory at that step.

All 24 runs have finite saved arrays and nonincreasing saved raw loss.
The three primary causal runs finish at relative losses between
\(6.25\times10^{-10}\) and \(1.26\times10^{-9}\). These are observed
properties of this cohort, not consequences of a nonlinear-stability theorem.

## 4. Timing versus a changed representation path

The [source-only mechanism diagnostic](RESIDUAL_FILTER_MECHANISM_DIAGNOSTICS.md)
requires comparison both at equal physical time and at matched **raw** loss.
Kernel eigenmodes are filtered differently, so the new step cannot generally
be treated as a single scalar clock change. Its numerical sample mixing is
not an additional feature-learning mechanism.

For dense width 512, seed 101, at 99% loss reduction the refined RK4 path
crosses normalized time 5.5851; the filtered step-0.2 path crosses 6.1250.
For a like-for-like stage diagnostic, take the reference's loss-crossing time
and compare the filtered path first at that same time, then at its own crossing
of the same raw loss. With fixed linear interpolation, the training–passive
Gram RMS differences are:

| Loss reduction | Layer 1: equal time / matched loss | Layer 2: equal time / matched loss |
|---:|:---|:---|
| 50% | 0.003429 / 0.001361 | 0.008354 / 0.003044 |
| 80% | 0.004377 / 0.001144 | 0.006888 / 0.002910 |
| 99% | 0.002130 / 0.000645 | 0.003320 / 0.001593 |

At 99% reduction, the matched-stage errors are 1.94% and 2.41% of the
reference's passive-block movement; training off-diagonal errors are 1.73%
and 3.13%. The comparisons support substantial timing bias for these observables,
not equality of all states under a time reparameterization. Matching a scalar
loss does not match the residual vector. Remaining matched-stage discrepancies
include time-integration and interpolation effects, and the interpolation error
has not been separately bounded.
These stage diagnostics do not quantify what fraction of the whole-trajectory
error timing explains.

The actual individual-feature displacement is a different observable from
Gram-change RMS. At this same matched-loss stage, the dense RK4 / filtered
step-0.2 RMS displacements are:

| Panel | Layer 1 | Layer 2 |
|:---|:---|:---|
| Training | 0.30924 / 0.30696 | 0.32354 / 0.32109 |
| Passive | 0.28112 / 0.27949 | 0.31365 / 0.31127 |

Thus this numerical step slightly suppresses both layers' displacement at
this stage; it does not manufacture the strong downward redistribution seen
when learned middle memory is physically removed. This conclusion is
stage- and draw-specific. It neither resolves the previous reciprocal/affine
ablations nor replaces their dedicated refinement needs.

The causal discrepancy has a different pattern. Matching the three-run mean
raw loss to 99% reduction still leaves lower-layer errors of 28.75% on
training off-diagonals and 31.30% on training–passive pairs against the dense
RK4 means. Upper-layer matched-stage errors are 15.72% and 11.18%.
The lower discrepancy therefore does not disappear after this timing
diagnostic. At the same stage, causal/dense-RK4 RMS individual-feature
displacements are 0.3221/0.3179 and 0.3278/0.3281 on training inputs, and
0.2982/0.2862 and 0.3106/0.3114 on passive inputs, for layers 1 and 2.
Similar amounts of movement do not establish the correct sample associations.
This validates the decision to test full pairwise similarities, rather than
using loss or feature-motion size as a proxy for accuracy. It does not yet
identify a defective term in the population equations: particle uncertainty
and unresolved discretization remain competing explanations.

These ensemble-stage comparisons first average the raw losses and observables,
then interpolate the first mean-loss crossing. They are not averages of
per-seed matched-loss comparisons.

## 5. Exact memory accounting and limits

With zero initial readout, the filtered program obeys

\[
f_a^k=h\sum_{j<k,b\le m}\widetilde c_b^{\,j} C^2_{ab}(k,j).
\]

This retains the old mechanism: a historical training write is evaluated
against the current query feature, including passive queries. Using raw
\(c\) instead would describe a different numerical write history, not reveal
a missing physical memory term. Roundoff-level reconstruction checks verify
accounting, not the accuracy of the trajectory that was reconstructed.

For the primary seed-1701 causal run, reconstruction with the filtered
write history differs from its saved output by at most
\(2.00\times10^{-15}\). Incorrectly using the raw residual history produces
an error of 0.17148. This is a consequential numerical-accounting distinction,
not evidence for a new physical memory channel.

## 6. Remaining uncertainty and reproducibility

The prescribed 128-particle step refinement gives the following maximum-entry
differences at common saved times. The numerical gate is the larger of
\(10^{-5}\) and 1% of the finer run's observed maximum-entry Gram change.

| Block | Steps 0.2 versus 0.1 | Numerical gate | Result |
|:---|---:|---:|:---|
| Layer 1 TT | 0.007307 | 0.001146 | fails |
| Layer 1 TP | 0.007134 | 0.000954 | fails |
| Layer 2 TT | 0.026477 | 0.001783 | fails |
| Layer 2 TP | 0.016085 | 0.002087 | fails |

These are measured finite-particle mesh changes, not a pure deterministic
truncation-error estimate: changing the chronological Gaussian query basis
also changes the finite-sample representation, even at the same random seed.
They do not numerically resolve the causal continuum trajectory.

At fixed step 0.2, changing 256 to 512 causal particles on seed 1701 changes
the four initialization-subtracted blocks by maximum-time RMS
0.013962, 0.013684, 0.017924 and 0.019136, respectively. Each exceeds the
corresponding primary causal-versus-dense mean discrepancy. The width-512 to
width-1024 dense mean changes are 0.007348, 0.006932, 0.007372 and 0.006691.
These single particle/width comparisons diagnose unresolved sampling and
width effects; they are not certified error bounds or convergence rates.

The descriptive uncertainty envelope combines three estimated standard
errors with these particle and width changes. No block meets the predeclared
criterion for sustained excess beyond it, although some have pointwise
excess. The envelope is not a simultaneous confidence band and contains no
time-bias allowance. A wide envelope is **not** counted as an accuracy pass.
The observed lower-layer 20% target failure is retained; its source is not
yet isolated between the population equations and numerical approximations.

The fresh repeated 256-particle run reproduces all 19 saved arrays exactly,
including both-time similarities and reciprocal-response arrays. This is
one-run reproducibility, not an independent reproduction of the full campaign.
The independent reviewer instead recomputed the complete summary from the
saved arrays, agreeing to roundoff.

Across the cohort the largest recorded Gaussian covariance-factor defect
is \(2.53\times10^{-8}\), the largest discarded variance is
\(2.56\times10^{-12}\), and the largest linear-solve defect is
\(5.56\times10^{-16}\). These arithmetic diagnostics do not bound
finite-particle integration error. All 24 runs used a total of 1277.38 seconds
of numerical execution and at most 10790.6 MiB process RSS, within the
predeclared 30-minute and 12-GiB budgets. No additional scientific seed or
mesh was chosen after viewing the outcomes.

The integrator audit also identifies an off-campaign API guard issue:
non-Python Boolean false values can bypass its full-model-only check before
being normalized. Every campaign run uses the full-model default, so this
does not affect these results. The frozen implementation must not be treated
as a validated arbitrary-ablation interface.

## 7. Scientific conclusion

This phase repairs a failed dense reference and demonstrates a stable,
consistent numerical stepping rule. It does **not** close the full-system
similarity-accuracy claim. It also makes one explanatory distinction sharper:
similar total feature motion, successful fitting and near-identical scalar
Gram-change magnitudes can coexist with appreciable pairwise discrepancies,
including associations with passive inputs. Loss and movement size alone are
inadequate validation proxies for the requested similarity accuracy. These
experiments do not prove that every valid reduction must explicitly retain
all pairwise relations rather than reconstructing them.

The earlier middle-memory and reciprocal-return observations remain qualified
by their own ablation controls. This phase does not revalidate them on refined
meshes or resolve the late activation-sensitivity control. No memory or gate
is removed from the system. The next useful numerical decision would separate
particle integration error from time bias at fixed geometry; global proofs
and two-input cubic refinements remain paused. No further scientific cohort
is part of this completed bounded phase.

Sources: [new causal integrator](causal_filtered_integrator.py),
[driver](residual_filter_experiment.py),
[predeclared cohort](run_residual_filter_cohort.py),
[analysis](analyze_residual_filter.py), and
[independent evidence check](RESIDUAL_FILTER_EVIDENCE_CHECK.md).
Generated evidence is under
`data/generated/transparent_learning_dynamics_20261007/residual_filter_v1/`.
