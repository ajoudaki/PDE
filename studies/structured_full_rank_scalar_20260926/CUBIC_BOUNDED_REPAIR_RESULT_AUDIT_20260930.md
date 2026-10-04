# Audit of the bounded-Gram circle repair results

2026-09-30. Scope: the bounded and ungated methods in saved `round2` and
the bounded method in `round2_transfer`, under
`data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/`.
Only deterministic saved-data, initialization, and algebra checks were run;
no ODE or dense training was performed. The numerical refinement run is a
separate task and is not credited in this report.

This is an author-associated implementation/results audit with independent
coefficient and equation recomputation. This agent developed the bounded
route; this report is **not** an independent scientific promotion review.
No other study was inspected and no README was changed.

**Finding:** the stored metrics, training fits, state counts, coefficient
provenance, and endpoint geometry checks are internally consistent. No
implementation or data-leakage defect was found that explains the measured
improvement. The bounded method improves eight of nine saved circle RMS
comparisons, but worsens the mixed quartet and leaves errors around 0.24
and 0.25 on the difficult pair and cluster. It is a useful tested repair,
not a general accuracy guarantee or a fixed-state whole-function decoder.

## Recomputed results

The primary metric was recomputed directly as
`sqrt(mean((saved_prediction[:256] - saved_dense)^2))`, with no centering,
rescaling, normalization by target magnitude, or fitted alignment.

| Task | Original cubic RMS | Bounded RMS | Training states | All evolving states |
|---|---:|---:|---:|---:|
| near_pair_sin9 | 1.205628177 | 0.240263740 | 5 | 779 |
| cluster_triple_cos9 | 1.337774075 | 0.252676355 | 9 | 1045 |
| cluster_triple_cos1 | 0.042560839 | 0.010078917 | 9 | 1045 |
| pair_cos3 | 0.121253367 | 0.057492900 | 5 | 779 |
| pair_orthogonal_cos1 | 0.045205307 | 0.009671733 | 5 | 779 |
| triple_wide_mixed | 0.007534824 | 0.003085362 | 9 | 1045 |
| quartet_mixed | 0.039916377 | 0.050156663 | 14 | 1314 |
| broad_ridge6 | 0.043183463 | 0.019215755 | 27 | 1861 |
| alternating3 | 0.089800456 | 0.052032835 | 9 | 1057 |

The three corresponding ungated RMS values are 0.304872655,
0.450843248, and 0.025668166. Thus the matched gate comparison improves
all three tested cases. The gated/ungated comparison isolates this gate
within their shared closure; it does not isolate every difference from
the original cubic model.

All 12 inspected endpoints have stop reason `target` and recomputed
training MSE 0.001 to floating-point precision. The saved training residual
MSE equals each JSON value exactly. Recomputing MSE from **all original
training aliases**, including the six original points of `alternating3`,
differs from the effective residual MSE by at most `4.22e-15`. All saved
dense training outputs also give MSE 0.001, with discrepancy below
`1.04e-12`; these are matched training-threshold comparisons, not matched
physical-time comparisons.

Every inspected loss history has increasing times and no positive accepted
loss increment. Its final time and MSE match the saved endpoint metadata.
This verifies the stored histories, not every internal RK stage or the
entire continuous interpolant.

## State accounting and query scope

For `m` effective training points and `Q` initialized queries, the actual
implemented count is

\[
D_{\rm train}=m+\frac{m(m+1)}2,\qquad
D_{\rm total}=D_{\rm train}+Q(m+1).
\]

This includes every cross-Gram query coordinate and every query diagonal.
The runner uses `Q=256 + number_of_original_training_points`, so the alias
queries are also counted. `alternating3` has three effective training
representatives but 262 query points, producing 1057 total states.

The training count equals the previous cubic model's training count
`2m+m(m-1)/2`. The complete circle diagnostic uses substantially more
evolving coordinates than the previous shared cubic-integral decoder.
Claims of 5--27 scalars must therefore say **training states**, not all
states. Passive queries can be initialized independently and have no
mathematical feedback into the training vector field; they are not a
constant-state representation of the full input function.

## Initialization provenance and source integrity

The frozen runner obtains `K0`, `S`, labels, and initial query cross Grams
from the original coefficient archives; it obtains the query response
slice `B` from the geometric coefficient archives. The query initial
diagonal is recomputed from seed 1, width 1024 Gaussian initialization.
Only the bounded model's scalar coefficient arrays enter its vector field.
Dense fitted predictions enter the RMS calculation and saved comparison
arrays, not the model constructor, derivative, gate, or decoder.

An independent deterministic reconstruction drew first weights from
`SeedSequence([1,1])` and the Gaussian middle matrix from
`SeedSequence([1,101])`, with middle scaling `1/sqrt(1024)`. For all nine
tasks it then directly contracted the initial tanh features and first
response fields. Reconstructed `K0`, `S`, query cross Grams, and
`B[q,e,c,f]=S0[(query_q,e),(train_c,f)]` agree **bit for bit** with the
stored arrays. This also checks the query tensor's index roles and shows
that these coefficients contain no dense-trained values.

The following checks passed:

- All 12 frozen source hash entries across the two manifests match their
  saved source copies. The current bounded model and small integrator also
  match their saved versions. The current runner has since gained other
  branches, so the audit used the frozen round2 runner for executed logic.
- All 12 result archive hashes and 24 referenced input archive hashes match
  the JSON metadata: 36 checks in total.
- Every per-result JSON equals its summary entry.
- Saved dense and old cubic prediction arrays exactly equal the referenced
  original archive arrays. All 256 circle angles and the appended original
  training angles match the recorded ordering.

There are two reporting qualifications. First, the runner retains its
dense initialization and temporary initial feature array in outer Python
locals while the ODE runs. The model RHS and decoder never consult them,
but the experimental process does not have width-independent resident
memory. Second, the frozen integrator imports `_ScalarRK45` from
`cubic_scalar_ode.py`, and the runner imports `directions` from
`circle_tasks.py`; those transitive sources are not included in these two
run manifests or frozen source directories. This is a reproducibility
provenance gap, not an observed numerical or leakage defect.

## Independent equation and geometry checks

At every inspected saved endpoint, direct nested-loop contractions of
`T` and `N`, followed by the explicit augmented-Gram congruence equation
for each query, reproduce the implemented full RHS to at most `5.00e-12`
absolute error. This recomputation did not reuse the implementation's
einsum expressions for those contractions. Independently differentiating
`q=f^T K^-1 f` gives

\[
\dot q=2(K^{-1}f)^T\dot f
-(K^{-1}f)^T\dot K(K^{-1}f)
=-\frac4m r^Tf
\]

to at most `9.18e-13` absolute error across the endpoints. This verifies
the vector-field identity. A numerical trajectory-wide energy balance
cannot be reconstructed from the saved loss-only histories.

Reconstructing predictions directly as `k_x^T solve(K,f)` reproduces every
saved query output exactly. Recomputed RMS, residual MSE, and reported
geometry diagnostics also reproduce exactly. The maximum bounded training
alias error is `2.04e-13`; including ungated endpoints it is `2.75e-13`.
Zeroing all passive query coordinates leaves the entire training RHS
bitwise unchanged at every inspected state.

For all nine bounded endpoints:

- The training Gram and training kernel are positive definite numerically.
  The smallest endpoint Gram eigenvalue is `6.62e-5` on `broad_ridge6`.
- Every training and query diagonal is below one. The largest query
  diagonal is `0.997863551` on the difficult cluster.
- The maximum query Schur excess is `2.00e-15`, consistent with rounding.
  The independently reconstructed initial Schur excess is at most
  `2.39e-14`, also a small floating-point residual.
- Every query satisfies the readout-energy output bound at the saved
  endpoint. The least negative value of `max_x(f_x^2-q)` is `-0.0997478`;
  the energy cap is therefore not merely an equality at the sampled peak.

The ungated endpoints preserve the positive Gram and Schur checks, but
their largest query diagonals are 4.8533, 7.4493, and 1.0109. Their outputs
also exceed `sqrt(q)` at some queries. This is the expected consequence
of removing the gate, not a hidden constraint failure of the ablation.

## Numerical and scientific limits

The integrator brackets the first accepted target crossing and locates
the MSE threshold on its dense interpolant. It reports the resulting
threshold state, not the overshooting accepted endpoint. Its error norm
separates residual, packed training Gram, and passive query coordinates,
so many query states do not dilute the residual or training-Gram error
test. The passive queries share one RMS error block, however; that is not
a maximum error bound at every query. Their errors can also affect the
adaptive step schedule even though they never enter the mathematical
training RHS. A tighter-tolerance replicate is therefore useful and is
being handled separately.

Endpoint geometry passes do not verify every intermediate numerical state.
The largest endpoint training-Gram condition number is about `6.77e4`
on `broad_ridge6`; its prediction solve is not exact arithmetic. No
conditioning-induced discrepancy was detected in this audit. The maximum
128-versus-256 RMS change is about `1.00e-5` on the difficult cluster,
far below its RMS error but nonzero. Saved mesh agreement is not a
continuum quadrature theorem.

Finally, the model still has the arbitrary-query cubic projection defect
identified in `CUBIC_ENERGY_REPAIR_ROUTE_20260930.md`. The observed large
gain does not eliminate that defect or prove that the surrogate feature
geometry equals the dense network's geometry. The tasks belong to the
existing panel used to develop the research direction; the transfer runs
are not a new external dataset or a blinded benchmark. These limitations
affect the scope of the conclusion, not the recomputed numerical gains.
