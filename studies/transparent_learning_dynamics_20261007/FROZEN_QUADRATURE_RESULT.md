# Independent population averages expose a numerical self-consistency defect

2026-10-07. Bounded continuation of the 16-input causal feature–response
investigation. The causal mechanisms, dataset and horizon are unchanged.
Global proofs and two-input cubic work remain paused.

## Bottom line

Fresh Gaussian integration of the **recorded, frozen coefficient histories**
substantially changes the lower-layer similarities toward dense training.
The measured lower-layer dense discrepancies fall from 27–31% to 12–15%.
This supports finite-particle integration as a contributor to the previous
mismatch, but **does not establish an improved causal solver**. The new
calculation never updates those coefficient histories, so it is a diagnostic
of their necessary moment consistency, not a new autonomous trajectory.

The predeclared experiment is **inconclusive as a confirmation**: lower-layer
fresh-integration uncertainty misses the fixed resolution gate. Upper-layer
integration clears that gate, but its effects are mixed and lie between the
predeclared negligible/material thresholds. No scientific run was added after
those results. The coupled model's previously reported accuracy remains
unchanged.

## 1. What was predicted and held fixed

The [README contract](README.md#fresh-quadrature-self-consistency-audit-2026-10-07)
was recorded before scientific execution. The question was whether the
remaining mismatch mainly reflects inaccurate population integration, or
persists when the recorded local circuits are evaluated independently.

The fixed setting is the preceding two-hidden-layer tanh model: 16
nonorthogonal training inputs in dimension 8, mixed-sign labels with
magnitudes 0.25–0.70, and four passive inputs. Normalized time is
\(2t/m\in[0,19.2]\), with step 0.2 and 97 saved states. These exploratory
labels are not certified against the original conservative small-label cap.
Passive inputs have no forcing weights or labels in any update.

The sources are the three full filtered causal runs with 256 integration
particles and seeds 1701/1702/1703. The comparison retains the previous
three width-1024 dense filtered runs, seeds 101/202/303, on the same mesh.
No dense values are used to construct the fresh population calculation.

Before the test:

- A necessary-moment defect below 5% of dense similarity movement in every
  primary block would support a negligible measured defect.
- A defect above 20%, also exceeding three estimated fresh-integration
  standard errors at its maximum time, would be materially large.
- Explaining at least half the old discrepancy additionally required a
  reduction of at least 50% in maximum-time dense-comparison error **and**
  passing the fresh-quadrature resolution gate.
- Resolution required both the maximum block-RMS three-standard-error scale
  and the independent-half difference to be below 5% of dense movement.

These are descriptive criteria, not simultaneous confidence guarantees.
The registered explanation decision uses the three-source ensemble; the
retained single-source comparisons are diagnostics, not additional successes.

## 2. The exact diagnostic and its limitations

Keep the existing notation: \(c=y-f\); \(C^\ell,D^\ell\) are the two-time
feature and backward-signal Grams at hidden layer \(\ell\); and
\(R^h,R^\delta\) are the directed local responses. The residual-filtered
step stores the effective training force \(\widetilde c=(I+hK)^{-1}c\),
where \(h=2\Delta t/m\). For normalized input directions \(v_a\), its
current training kernel at step \(k\) is explicitly

\[
K_{ab}=C^2_{ab}(k,k)+C^1_{ab}(k,k)D^2_{ab}(k,k)
       +(v_a^\top v_b)D^1_{ab}(k,k),\qquad a,b\le m.
\]

Freeze the recorded arrays
\(C^1,D^2,R^h,R^\delta,\widetilde c\). Draw fresh lower initial Gaussian
weights, a lower Gaussian history \(\xi\) of covariance \(D^2\), and an
upper Gaussian history \(\eta\) of covariance \(C^1\). These three families
are independent; within each history, all prescribed temporal and input
correlations remain. Evaluate the original local equations with those fixed
arrays. In particular, **neither the raw residual nor the residual filter is
recomputed to drive the fresh particles**.

If a recorded coefficient history were an exact population solution at this
step, its local circuits would reproduce its own moments when integrated over
these Gaussian laws. Failure of this necessary condition is therefore an
informative numerical diagnostic. Success would not be sufficient: this
phase tests current feature/backward moments, predictions and displacement,
not every two-time moment or every response derivative.

The primitive covariance target is the saved raw empirical Gram, factored
once before sampling. It differs slightly from the old sampler's retained
factor covariance, whose small reconstruction defects remain documented in
the source records. More fresh particles integrate this frozen law better;
they do not restore directions missing from the original finite-particle
Gram, recompute the reciprocal responses, or close a new population solution.
This is also not an independent test of time discretization.

Each source received 32,768 fresh samples in 32 independent batches of 1024,
using seeds 8101/8102/8103. A fourth run exactly repeated the first in a fresh
process. Batch averages supply conditional standard errors, independent-half
comparisons, and nested 8192/16384/32768-sample diagnostics. Conditional means
and variances here treat the original coefficient paths as fixed. They do
not quantify source-path randomness or dense-width error.

## 3. Similarity changes over the whole saved horizon

For every source or fresh batch, subtract its own initial Gram before
averaging. Error means maximum over the 97 saved times of block-RMS matrix
discrepancy; relative error divides by maximum block-RMS dense mean change.
Temporal maxima can occur at different times. Training–training includes
diagonals; off-diagonal results are retained separately in the analysis.

| Layer and block | Original versus dense | Frozen replay versus dense | Fresh-minus-original defect |
|:---|---:|---:|---:|
| Layer 1, training–training | 27.33% | 12.32% | 23.34% |
| Layer 1, training–passive | 31.41% | 15.19% | 27.47% |
| Layer 2, training–training | 17.39% | 15.94% | 14.18% |
| Layer 2, training–passive | 12.37% | 12.90% | 12.09% |

For the lower training block, the absolute RMS dense discrepancy changes
from 0.011911 to 0.005372; for lower training–passive pairs, from 0.011727
to 0.005673. Those are measured reductions of 54.90% and 51.63%, respectively.
The lower off-diagonal training result is similar: 29.29% becomes 13.34%.
Thus the observation is not just a change in individual feature norms.

The upper training discrepancy improves only modestly, from 0.009157 to
0.008394. The upper passive discrepancy increases from 0.008168 to 0.008519,
a 4.30% worsening in this metric. A partial lower-layer improvement must not
be reported as a uniform improvement of the system.

Absolute-Gram comparisons, all single-source results, nested sample-count
changes and full time curves are saved in `analysis/summary.json`,
`analysis/curves.csv`, and `analysis/curves.npz` under the generated directory
below. The [trajectory figure](../../data/generated/transparent_learning_dynamics_20261007/frozen_quadrature_v1/analysis/self_consistency.png)
plots actual matrix discrepancies, not differences of scalar Gram norms.

## 4. The resolution gate remains binding

All quantities below are in the same unnormalized block-RMS units as the
preceding errors. The threshold is 5% of the dense mean Gram-change scale.

| Layer and block | Three conditional SE | Independent-half difference | Threshold | Resolution |
|:---|---:|---:|---:|:---|
| Layer 1, training–training | 0.002790 | 0.001947 | 0.002179 | fails |
| Layer 1, training–passive | 0.002714 | 0.001888 | 0.001867 | fails |
| Layer 2, training–training | 0.002190 | 0.001552 | 0.002634 | passes |
| Layer 2, training–passive | 0.002200 | 0.001257 | 0.003301 | passes |

The measured lower defects exceed the material-size threshold and the
three-SE scale, and the nominal error reductions exceed 50%. Nevertheless,
the stricter resolution criterion fails, so the registered explanation flag
is **false**, not a confirmed success. Every single-source block also fails
its resolution criterion. Pooling the three source paths reduces conditional
fresh-sampling uncertainty; it does not eliminate their variability.

Across those three paths, the estimated standard-error scale of the correction
is about 0.0086–0.0098, larger than its fresh-integration-only SE. This
cross-source quantity mixes source-path variation with fresh-sampling error
and has only three sources. It is neither a pure coefficient-uncertainty
estimate nor a calibrated confidence interval.

## 5. What changes the explanation, and what does not

The results provide a direct test of finite-particle consistency as a
possible explanation of the dense discrepancy. However, they do not
identify an incorrect physical memory term. All learned writes, reciprocal
returns and activation gates were retained with their recorded coefficients.

One post-test directional diagnostic helps interpret the mixed table. Stack
all saved times and entries of one block, call the original error vector
\(E=C_{\rm source}-C_{\rm dense}\), and the fresh correction
\(U=C_{\rm fresh}-C_{\rm source}\), using initialization-subtracted Grams.
The scalar \(E^\top U/\|E\|^2\) measures correction along the old error,
not reduction of its maximum-time norm. For lower training and passive
blocks it is respectively -0.765 and -0.762, with conditional fresh-sampling
SEs 0.0214 and 0.0235. Thus the observed correction points substantially
against the previous error. This exploratory diagnostic does not replace
the preregistered gates.

For the upper blocks the corresponding coefficients are about -0.408 and
-0.420, yet the error norm improves little or worsens. The exact identity
\(\|E+U\|^2=\|E\|^2+2E^\top U+\|U\|^2\) explains why favorable movement
along one error direction is insufficient: the correction has other
components too. This is an interpretation of numerical error geometry,
**not a newly discovered physical feature-learning interaction**.
The identity uses the stacked Euclidean norm; the table instead takes a
maximum over time of block RMS. Their different temporal aggregation is
another reason favorable stacked alignment need not reduce the table's error.

Actual RMS individual-feature displacements at the final saved time are:

| Panel and layer | Original | Frozen replay |
|:---|---:|---:|
| Training, layer 1 | 0.33502 | 0.33266 |
| Passive, layer 1 | 0.31079 | 0.30157 |
| Training, layer 2 | 0.33968 | 0.34020 |
| Passive, layer 2 | 0.32013 | 0.32517 |

These are square roots of ensemble-mean squared individual displacements,
not Gram-change magnitudes. Relatively small changes in movement size coexist
with larger changes in sample associations. The old conclusion that movement
size alone is an inadequate validation proxy survives this independent
sampling diagnostic.

The final loss of the ensemble-mean prediction also changes: from
\(9.32\times10^{-10}\) to 0.003153 times its initial loss. The largest mean
prediction difference is 0.05454. The original finite-quadrature fit therefore
does not transfer unchanged to the independently integrated frozen circuit.
This is not failure of a freshly retrained population model: no fresh
residual feedback or training was performed. Loss of the mean prediction is
not mean loss across runs.

## 6. Numerical checks and reproduction

Before scientific execution, supplied-primitive replay matched every tested
local field and prediction exactly on the tiny nonzero- and zero-label
programs. Full-Gram and individual-displacement identities, singular and
zero covariance cases, and rejection of materially indefinite covariance
also passed. The independent source review found no incorrect population
pairing, omitted current passive response, or adaptive update hidden in the
frozen evaluation.

In the scientific records, Gaussian factors reconstruct saved raw covariance
entries to at most \(2.99\times10^{-10}\), below the \(10^{-8}\) gate.
Retained ranks are 244–248 for the upper primitive and 233–241 for the lower
primitive, out of 1940 time/input coordinates. Small discarded positive
eigenvalue sums and roundoff-negative eigenvalues are reported per source.
These factor diagnostics do not bound finite-particle or time-step error.

The recorded exact filtered-write reconstruction errors are at most
\(1.34\times10^{-14}\) for individual readout coefficients and
\(1.34\times10^{-15}\) for averaged predictions. These are producer-checked
identities; the fresh local fields and full two-time Grams are not saved in
this current-moment campaign, so the saved-array reviewer does not claim to
reconstruct that identity independently from the outputs alone.

The repeated source-1701 replay reproduces all 91 saved non-timing arrays
exactly. Timing arrays are excluded for the stated reason. The complete
four-run campaign used 78.44 seconds recorded wall time and at most 429.7 MiB
process RSS, within its 20-minute/12-GiB budget. The initial plotting attempt
found no installed matplotlib; the saved-array figure was regenerated with
the available Pillow renderer, without rerunning any scientific calculation.

An [independent check](FROZEN_QUADRATURE_CHECK.md) recomputes the statistics
from saved batches and records its exact coverage and limitations. It is not
an independent rerun of the whole campaign.

## 7. Decision and next bottleneck

The phase leaves the global and full-trajectory accuracy claims open. It
adds targeted evidence that the small quadrature calculation has
a consequential necessary-moment consistency defect, particularly in the
lower-layer sample associations. The evidence is suggestive of a substantial
sampling contribution, not a completed attribution or a new validated solver.

An exact [Gaussian score identity](STEIN_RESPONSE_IDENTITY_CHECK.md) was also
checked as a possible lower-memory representation of reciprocal contractions.
It was not substituted into the solver: finite score-estimation noise can
scale with covariance rank divided by sample count, and rank is comparable
to the current adaptive population size. Avoiding tangent storage by adding
that uncontrolled error would not resolve this experiment.

The next useful implementation question is how to compute the **coupled**
population averages and their responses with separately controlled sampling
and time errors, retaining the same causal interactions. No new scientific
cohort, global proof or two-input approximation is part of this completed
phase.

Sources: [frozen replay](frozen_population_replay.py),
[fixed cohort](run_frozen_quadrature_cohort.py), and
[analysis](analyze_frozen_quadrature.py).
Generated evidence:
`data/generated/transparent_learning_dynamics_20261007/frozen_quadrature_v1/`.
