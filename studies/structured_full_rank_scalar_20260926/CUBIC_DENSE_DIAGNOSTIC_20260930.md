# Saved-endpoint diagnostic protocol

2026-09-30. Scope: `near_pair_sin9`, `cluster_triple_cos9`,
`cluster_triple_cos1`, `pair_cos3`, and `triple_wide_mixed` in the existing
cubic scalar circle study. Inputs are the assigned scalar/dense implementation
files, the existing cubic report, and the saved cubic and Gaussian reference
endpoints. No other study, fitting, training solve, or parameter selection.

Decision: determine whether the large passive-output errors arise alongside
large errors in the endpoint feature Gram, lower-layer tangent Gram, positive
completion, or decoder alias correction. Compare exact canonical dense tangent
kernels with the scalar `K0`, `M`, `N`, and quadratic completion on training
inputs and on the fixed 256-point passive circle. Endpoints retain their own
first MSE 0.001 crossing; endpoint differences are diagnostics, not a matched
physical-time causal decomposition.

The competing explanations are a small dense/scalar kernel discrepancy with
an amplified decoder error, versus substantial feature-response truncation
error already present in the kernel. Report numerical sizes without tuning a
threshold after observing them. Descriptive flags: relative Frobenius kernel
error below 0.1 is small, above 0.5 is large, and intermediate values are
unresolved. A large norm does not by itself establish the cause of trajectory
error.

Also evaluate exact dense readout energy `q = mean(c*c)` and the universal
tanh bound `max|f| <= sqrt(q)`. Scalar readout energy, if reconstructible from
the saved residual integrals and loss history, must be labeled a quadrature
diagnostic rather than an exact inference from final loss. A negative energy
estimate or a discrepancy in training replay invalidates that interpretation.

Validity: float64, one BLAS thread, finite output and kernel checks, saved
prediction replay at absolute error below 1e-10, training cubic-kernel identity
at relative error below 1e-10. Batched circle evaluation limits memory. No
replication or adaptive experiment is authorized; missing saved inputs are
reported and excluded. Hard budget: at most 15 seconds cumulative automated
data reads and numerical endpoint evaluation. Stop after one pass through the
five tasks or deadline, whichever occurs first.

Products: this protocol and appended results, the diagnostic source, and fresh
`data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/diagnostic/diagnostic.json`.

## Result

**The completion/alias decoder produces most of the final passive error in
the two difficult cases, but substantial feature and tangent-response errors
already exist upstream.** Dropping the alias after the fact would give up
training consistency and would leave those upstream errors in place. All
five saved endpoints were evaluated; no model was fitted or trained.

Let `alpha=2/m`, `K0` be the initial training Gram, and retain the code's
`M`, `N`, residual `r`, residual integral `z`, and iterated integrals `J,P`.
The exact algebra of this scalar model is

\[
Q=M^\top K_0^{-1}M,\qquad
K_{\rm cub}=K_0+M+M^\top+N,\qquad
K_{\rm sc}=K_{\rm cub}+Q.
\]

For a query `x`, its effective tangent cross-kernel is

\[
K_{\rm sc}(x,a)=K_0(x,a)
 +\alpha^2\sum_{b,c}C_{xabc}J_{bc}
 +[K_0(x,\cdot)K_0^{-1}Q]_a.
\]

Writing `Delta=y+r-f_cub(train)`, the consistency correction obeys
`Delta_dot=-alpha Q r`, and the alias prediction is
`K0(x,train) K0^{-1} Delta`. Thus the extra decoder is the time-integrated
effect of the positive kernel completion. These identities are exact for
the defined scalar ODE, separate from its accuracy for the dense network.

The dense canonical kernel was evaluated directly with
`D2(x)=c*tanh'(W h1(x))` and
`D1(x)=tanh'(w x)*(W^T D2(x))`:

\[
K_{\rm dense}(x,a)=\frac{h_2(x)\cdot h_2(a)}n
 +\frac{D_1(x)\cdot D_1(a)}n(x\cdot a)
 +\frac{D_2(x)\cdot D_2(a)}n
       \frac{h_1(x)\cdot h_1(a)}n.
\]

The mobilities are exactly `(n,1,n)`. All errors below compare each method's
own MSE 0.001 endpoint; they are not errors at a common physical time.

| Task | Completed training kernel relative Frobenius error | Circle cross-kernel relative Frobenius error | Raw cubic output RMS error | Alias circle RMS | Final output RMS error |
|---|---:|---:|---:|---:|---:|
| near_pair_sin9 | 0.5532 | 0.7571 | 0.1713 | 1.0994 | 1.2056 |
| cluster_triple_cos9 | 0.6858 | 0.7540 | 0.4968 | 1.2684 | 1.3378 |
| cluster_triple_cos1 | 0.4449 | 0.3515 | 0.0771 | 0.0427 | 0.0426 |
| pair_cos3 | 0.4355 | 0.4507 | 0.1235 | 0.1824 | 0.1213 |
| triple_wide_mixed | 0.3068 | 0.3037 | 0.0194 | 0.0247 | 0.0075 |

The two hard cases meet the preregistered large-kernel-error band. Their
error is therefore not explained by a small endpoint kernel discrepancy
alone. The controls also show why endpoint kernel norm is not a calibrated
predictor of final output error: the wide triple has 0.304 cross-kernel
error but only 0.0075 output RMS error.

### Readout energy and tanh feasibility

For the exact network let `q_c=mean(c*c)`. Cauchy–Schwarz and `|tanh|<=1`
give `|f(x)|<=sqrt(q_c)` for every query. Its canonical readout equation
also gives the exact identity

\[
\dot q_c=-2\alpha r^\top(y+r),\qquad
q_c(t)=q_c(0)-2\alpha y^\top z(t)
              -4\int_0^t\operatorname{MSE}(s)\,ds.
\]

Applying this identity to the scalar training trajectory with zero initial
readout defines its **compatible energy**. The scalar model itself has no
readout state; this is the energy a canonical readout realizing its training
trajectory would need. It is not an energy inferred from endpoint loss.
The saved accepted-step loss history supplies trapezoidal and Simpson
estimates. Monotonicity bounds the integral between its left and right
rectangular sums; the reported enclosure assumes the saved values represent
the exact monotone trajectory and does not certify ODE floating-point error.

| Task | Exact dense q_c | Scalar compatible q_c, Simpson | Scalar compatible q_c enclosure | Max scalar circle output | Max dense circle output |
|---|---:|---:|---:|---:|---:|
| near_pair_sin9 | 3.8837 | 5.4503 | [5.1905, 5.7081] | 2.9515 | 1.3552 |
| cluster_triple_cos9 | 8.8887 | 22.8089 | [22.1035, 23.5121] | 3.4135 | 1.2240 |
| cluster_triple_cos1 | 1.7480 | 1.4310 | [1.2925, 1.5662] | 0.9571 | 0.9512 |
| pair_cos3 | 2.4544 | 2.1906 | [2.0156, 2.3638] | 1.2632 | 1.1020 |
| triple_wide_mixed | 1.2294 | 1.0546 | [0.9790, 1.1288] | 0.7452 | 0.7387 |

For the near pair, `2.9515 > sqrt(5.7081)=2.3892`. The reported scalar
decoder cannot simultaneously be a tanh output and have the canonical
readout energy implied by its own training trajectory. This mismatch is
much larger than the loss-quadrature uncertainty. The cluster passes this
necessary bound, despite its large functional error; the bound is not an
accuracy guarantee. Dense endpoint outputs satisfy the exact bound in all
five cases.

### Where the feature approximation departs

The saved `J,P` also reconstruct the literal second-order feature correction
and cubic readout correction using only the initial realization. Write
`L[x,a,b]=D h2(x)[R_ab]`, where the initial response direction has
`dw=beta_ab*x_a` and `dW=gamma_ab*h1_a^T/n`. Then

\[
\delta h_2(x)=\alpha^2\sum_{a,b}J_{ab}L[x,a,b],\quad
c_1=-\alpha\sum_a z_a h_2^0(a),\quad
c_3=-\alpha^3\sum_{q,a,b}P_{qab}L[q,a,b].
\]

The raw cubic decoder is the truncation of
`mean((c1+c3)*(h2_initial+delta_h2))` through degree three, omitting the
degree-five `mean(c3*delta_h2)` term. Reconstructed `c1+c3` is a formal
readout approximation, distinct from the compatible energy above.

| Task | Dense feature motion RMS | Predicted second-order motion RMS | Feature prediction RMS error | Fraction of predicted features outside [-1,1] | mean((c1+c3)^2) |
|---|---:|---:|---:|---:|---:|
| near_pair_sin9 | 0.4671 | 0.8154 | 0.5232 | 34.72% | 6.6505 |
| cluster_triple_cos9 | 0.3715 | 1.0333 | 0.9324 | 39.86% | 65.7608 |
| cluster_triple_cos1 | 0.2879 | 0.3724 | 0.1484 | 15.13% | 1.5102 |
| pair_cos3 | 0.3973 | 0.5281 | 0.2664 | 23.92% | 2.3756 |
| triple_wide_mixed | 0.2135 | 0.2971 | 0.1150 | 8.52% | 1.0968 |

The hard-cluster readout correction has RMS 7.3177 versus linear readout
RMS 1.2889. Its full second-order feature Gram has Frobenius norm 5.7173,
the scalar projected/completed feature Gram has norm 1.4872, and the actual
dense feature Gram has norm 0.7767. Therefore merely restoring the feature
directions discarded by projection would greatly increase an already
overlarge unsaturated approximation; missing projection directions are
not a sufficient explanation or a justified standalone repair.

The weakest initial-kernel direction sharpens the strong-label contrast.
For cluster_cos9, the dense kernel in this direction is 0.63180 versus
scalar 0.20222. The dense lower-layer contribution is 0.33219 versus scalar
`N=0.02812`; the completion supplies `Q=0.14681`. With identical clustered
inputs but smooth cos1 labels, the corresponding full kernels are 0.00923
and 0.01122. This is a label-dependent response failure, rather than an
inevitable failure caused only by the initial Gram condition number.

Likewise `||K0^{-1}M||_2` is 4.0623 on the failing near pair and 4.0217 on
the successful smooth cluster. That norm flags departure from a sufficient
small-motion regime but cannot, by itself, classify functional failure.

### Ranked diagnosis and limits

1. **Largest immediate decoder discrepancy:** the integrated completion
   feeds a large initial-kernel interpolation correction into passive
   outputs on the hard tasks. For the near pair this also violates the
   necessary tanh/readout-energy constraint.
2. **Underlying response failure:** the unsaturated second-order features
   and cubic readout are no longer small corrections. The hard cluster's
   learned tangent response in its weak initial mode is substantially
   underestimated, despite an overlarge formal feature/readout expansion.
3. **Controls reject one-number diagnoses:** neither endpoint kernel
   relative error nor `||K0^{-1}M||` alone tracks functional fidelity. The
   alias, bounded-feature, energy, and label-direction diagnostics must
   be considered together.

These saved endpoints locate inconsistencies and rank their sizes. They
cannot identify the first physical time at which the trajectories separate,
prove which proposed repair will work, or establish hierarchy convergence.

### Numerical provenance

The completed pass took 1.061 seconds with one BLAS thread. A 0.544-second
implementation preflight stopped on an optional reconstruction check:
integrated shuffle identities were initially compared at absolute tolerance
1e-10, while the saved scalar ODE produces differences up to 3.07e-10.
That optional check was changed to 1e-8; the preregistered replay and kernel
identity gates stayed at 1e-10. No trajectory or coefficient was changed.
Including preflight and metadata reads stayed below the 15-second budget.
No further numerical experiment was run.

Direct dense prediction replay errors were at most 1.78e-15; training
cubic-kernel and second-feature contraction identities agreed within
2.65e-14. Source and input hashes, full matrices, weak-direction quantities,
quadrature estimates, and reconstruction checks are stored in
`diagnostic/diagnostic.json`. The implementation is
`cubic_dense_diagnostic_20260930.py`.
