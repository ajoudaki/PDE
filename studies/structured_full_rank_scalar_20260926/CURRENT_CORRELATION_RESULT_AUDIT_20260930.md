# Current-correlation candidate result audit

2026-09-30. Scoped internal audit; no promotion review or scientific
independence claim. The auditor previously evaluated the assigned dense
saved endpoints. This audit may read the supervisor's frozen current-
correlation protocol, candidate implementations, route reports, check files,
and the saved result files they designate. No incomplete candidate source,
other study, training, repeat fit, parameter tuning, or dataset expansion
is permitted. Candidate-source access begins only after the supervisor
provides a freeze notice with hashes.

## Prompt-only requirements recorded before candidate access

These requirements precede inspection of either candidate and do not assume
that either passes. Additional model-specific conditions may be necessary
once the actual definitions are available. Any such additions will be
identified separately from this initial checklist.

1. **Typed state and coefficient provenance.** Identify the autonomous
   training state, its initialization, mobilities and loss normalization,
   fixed training-dependent coefficients, and decoder. Distinguish an exact
   identity of the declared finite model from its approximation to dense
   dynamics. No endpoint-derived coefficients may enter the fitted model.

2. **Training loss.** With `L=mean(r^2)`, `f=y+r`, `alpha=2/m` and
   `rdot=-alpha T r`, exact differentiation requires
   `Ldot=-(4/m^2) r^T T r`. Determine whether `T` is symmetric positive
   semidefinite by construction, only observed numerically, or unsupported.
   If state coordinates instead represent features/readouts directly,
   derive `fdot` and its corresponding tangent before making a loss claim.
   Accepted-step monotonicity does not by itself prove the continuous
   identity, and a PSD tangent does not certify a numerical solver.

3. **Readout energy.** For an actual canonical readout `f=<c h>` with
   `cdot=-alpha sum_a r_a h_a`, `q=<c^2>` satisfies
   `qdot=-2 alpha r^T f`. This is an identity of an actual shared readout;
   merely defining an independent scalar by the same ODE establishes an
   energy bookkeeping identity, not the existence of that readout.
   Track nonnegativity, initial readout energy, any clipping or reset,
   and consistency between physical and bookkeeping energies.

4. **Energy decoder feasibility.** For `K_ab=<h_a h_b>`, Cauchy–Schwarz
   requires `f(x)^2 <= q K_xx`; bounded tanh features additionally give
   `K_xx <= 1` and `abs(f(x)) <= sqrt(q)`. If an actual shared readout is
   claimed, the joint Gram `[[q,f^T],[f,K]]` must be PSD on every evaluated
   finite set. These are necessary consistency tests, not approximation
   guarantees. A violation must not be hidden by an output-only clipping
   rule that changes training consistency or the declared dynamics.

5. **Alias and train/query consistency.** Evaluate the same decoder on
   training and passive inputs. Check whether training predictions equal
   the state used to form residuals. Identify every interpolation,
   completion, alias, output rescaling, or correction; derive its dynamics
   or mark it as an additional decoder hypothesis. An exact training
   interpolation identity alone does not establish a shared bounded-feature
   realization or an accurate passive function.

6. **Query independence.** Passive evaluation may depend on a frozen
   training solution and the requested query, but training coefficients,
   initial state, solver path, stopping rule and fitted state must not
   depend on the passive grid. Verify whether query batching/order/count
   changes random or quadrature nodes, matrix factorization, normalization,
   or cache construction that feeds back into training. Any numerical
   check must reuse saved state without refitting. If a construction only
   defines a separate extension for each query set, distinguish that from
   one consistent passive function.

7. **Current correlations and response limitations.** Identify what `q`,
   current `K`, joint gates, mixed readout–gate moments and first-layer
   response the candidate retains or drops. A correction can be exact for
   its declared approximation without matching the dense current tangent.
   Success on one contraction does not establish the full kernel, and
   state-matrix fidelity does not establish derivative fidelity.

8. **Saved result replay and fair comparison.** Use only the frozen tasks
   and reference files. Recompute reported metrics from saved outputs,
   compare endpoint times and MSEs, and state whether comparisons use a
   common physical time or each method's own threshold. Keep absolute and
   relative errors and denominator sizes distinct. Preserve all tasks and
   failures; do not replace a failed run or select a favorable checkpoint.

9. **Version and budget provenance.** Hash every read source/input; compare
   supervisor freeze hashes, campaign hashes, saved source snapshots and
   result hashes. Report which source produced which result. Verify run
   count and declared time/width/seed/task settings from the designated
   records. Do not claim budget compliance from a single runtime field if
   failed or preliminary attempts are omitted. Missing records are a
   limitation, not evidence that no additional run occurred.

10. **Calibrated conclusion.** Separate exact model identities, checks at
    saved states, tested predictive fidelity and unresolved convergence.
    This audit may identify concrete implementation defects and empirical
    limits; it cannot certify arbitrary-accuracy closure, trajectory
    causality, asymptotic concentration or repository promotion.

## Frozen inputs and implementation-specific audit

### Route A: frozen source and constructor-only audit

The supervisor authorized Route A before any candidate fit. Observed hashes
match the supplied freeze exactly:

| File | SHA256 |
|---|---|
| `CURRENT_CORRELATION_ROUTE_A_20260930.md` | `a6ae2b5b876c13f116c0e4eef8142cb86a1d8ae9a4e766b4c8f4be75c7c6fc21` |
| `current_projected_correlation.py` | `cd7ead9070a2ecce2f9728143666f79381a146fb7ec968656c89673a1a22d2e1` |
| `check_current_projected_correlation.py` | `9f56f02d9cd5ec6275ac0b3d2216b91cf90dfd5c2b49bfde8f82d18fba5c6de8` |

The frozen algebra is internally consistent. Expanding
`hdot_a=-alpha sum_b r_b beta_ab D_a D_b c` with
`D_a=s_a(I-lambda_a h_a tensor h_a)` produces the declared `A,u`,
weighted gate Gram and scalar RHS. The matrix orientation in code agrees
with `Hdot=H A+c u^T`. Self-adjointness of each `D_a` makes the lower
tangent a Schur product of PSD Grams even though the operators are not
positive. This distinction is necessary: PSD tangent is supported while
physical tanh-gate bounds need not hold.

The augmented Gram congruence gives the exact canonical energy identity,
the stated monotone-loss identity, and per-query Cauchy–Schwarz bounds.
The global finite-time existence argument closes: positivity and invariant
diagonal slack bound the feature Gram; bounded residual/output then bounds
the energy derivative on every finite interval. The query argument is
consistent with the training alias equations and one-way query coupling.
Neither this argument nor a norm-bounded Gram establishes a literal dense
tanh-neuron realization.

The candidate report discloses its material scientific limitations:
initial response operators are frozen and isotropized; projected gate
multiplication discards Gaussian cubic components; saturation rescaling is
imposed; the `D_a` operators can violate physical gate contractivity;
the zero-readout Gram flow stays in the initial training span; and a
single-input radial barrier is introduced. The prior exact cubic-response
theorem is explicitly not inherited. These are changes of model, not bugs
in the scalar implementation. Fidelity therefore remains an empirical
question after the algebra passes.

The neural initializer supplies a realizable initial augmented geometry.
The generic constructor/`from_coefficients` interface validates only parts
of this domain: it does not reject every negative passive diagonal or
inconsistent passive cross Gram. Exact positivity claims should therefore
retain the stated valid-initialized-coefficient hypothesis. No inconsistency
was found in the designated frozen coefficients.

The author's finite-dimensional operator check was rerun once, without
integration: PASS, maximum discrepancy 2.22e-16, explicit RHS discrepancy
4.94e-17. The zero-readout, query alias, beta trace, restart, energy,
saturation-boundary and Gram checks all passed. This is a rerun of an
instantaneous check, not a repeat fit or a new dataset.

The separate saved constructor-only campaign `preflight_projected` was
replayed using its own frozen source snapshots. Its three source/input
hash sets match; the copied dense predictions equal the original canonical
saved predictions exactly; predicted outputs, MSE, alias values and state
counts replay exactly. Augmented eigenvalues are no lower than -1.02e-16.
Finite-difference loss identity discrepancies are at most 2.64e-11.
The audit took 0.1032 seconds, performed no integration, and is retained in
`current_correlation_20260930/audit/preflight_projected.json`.

Training/total scalar counts are 6/1038 for the pair and 10/1305 for each
cluster. The latter totals include all 256 passive circle queries and
training aliases. No claim of a query-count-independent full state applies
to Route A. Width-dependent neural construction is disclosed and the
autonomous model does not retain width arrays.

### Shared integration semantics checked before candidate fits

With explicit supervisor authorization, the audit read the preflight's
frozen `small_scalar_integrator.py` and `_ScalarRK45` dependency. RK45 uses
the maximum over blockwise RMS normalized local errors. Route A includes
its passive-query coordinates in an error block, so those coordinates can
affect finite-tolerance adaptive steps despite exact mathematical query
independence. The protocol's promising-result branch separately checks a
training-only solve; the constructor-level RHS test does not replace it.

The wall limit is checked before each RHS evaluation, and interruption
retains the previous accepted state and records a numerical-gate stop.
This is a cooperative budget, not process termination at an exact
wall-clock instant. A threshold-crossing accepted step is located by
Brent root finding on the RK45 dense interpolant. The continuous loss
monotonicity result supports a first crossing; neither the saved history
nor the root finder certifies all floating-point interpolation error.
The physical cap is passed to RK45 as its terminal time.

This prefit stage found no mathematical or implementation blocker to the
precommitted Route A fit. It was not a favorable accuracy verdict. The
following sections record the subsequently authorized frozen B and result
audits; they do not alter either candidate.

### Route B: exact transport and explicit approximation limits

The supervisor's B freeze also matches all observed hashes:

| File | SHA256 |
|---|---|
| `CURRENT_CORRELATION_ROUTE_B_20260930.md` | `4d696ab574d3dea3ed42a80403105d3bd8afa0347a1b0a6c5aff50675498f205` |
| `current_gaussian_correlation.py` | `7b37942a3b0a6eaae2d0e52ec4cd0e42e6d82fe08c0cdf17bff69f7965362b90` |
| `check_current_gaussian_correlation.py` | `1708437f28690ff08584d59280fee403fb6aeef990641a59b15e6bb0f4894086` |

The covariance-gradient and transport equations are consistent. With
training abstract vectors `H=F R`, readout `b=F beta`, and `F^T F=V0`,
the matrix product in `Rdot` has the correct right-mobility orientation.
For a query, `ell=A^{-1} A_x` and `v_x=v_x0+F(R-I)ell` differentiate to
the stated passive equation. This is an exact representation improvement
of the declared Gaussian closure, not an endpoint interpolation alias or
a fitted correction. Every query uses the same `R,beta` state and no
trajectory history. At training aliases, `ell=e_a`; both prediction and
its derivative agree with the training formula.

The gradients of `f_a=u_a s(V_aa)` give the stated positive tangent and
canonical energy identity. The backward Gram is the Gram of projected
gradients `p_a=s_a b+u_a t_a v_a`, not the exact Gaussian weighted gate
moment. Keeping that distinction prevents an unsupported identification
with the `D` matrix in the saved dense diagnostic. Positive quadrature
weights and their normalized second moment support the bounded decoder
and contraction bounds of the ideal finite-link formula. The code uses
short scalar series at removable singularities; its claimed exact
derivative is understood up to that numerical special-function evaluation
and floating-point error, not a literal symbolic identity of the truncated
branches. The deterministic gradient and scalar-reference checks resolve
this at the relevant numerical precision.

The transport uses a fixed positive-definite mobility solve, with no
discarded positive eigenvalues or ridge. Its condition numbers are 23.21
for the pair and 276.43 for the clustered inputs. It retains only the
initial feature span, assumes a centered Gaussian law despite finite
empirical means, and freezes/isotropizes the initial hidden mobility.
The initial tangent is also changed: full relative Frobenius changes are
0.02847 and 0.02721, while the weakest initial-kernel Rayleigh ratios are
0.93283 and 0.71219. Thus the clustered weak direction loses about 28.8%
of its initial kernel strength even though the global change is only 2.7%.
This is a disclosed approximation, not a numerical defect or a proved
cause of its later passive error.

B's deterministic check was rerun once without integration. It passed:
moment/query derivative discrepancies were at most 1.67e-16, output-gradient
central-difference error was 1.27e-10, and direct scalar quadrature errors
were at most 3.47e-14 for `s` and 2.19e-13 for `t` over the declared grid.
The constructor-only saved campaign replayed exactly. At every subsequently
audited saved B endpoint, deleting all query coefficients produces a model
with bitwise-identical training RHS, initial state and solver blocks. B
therefore has no query contribution even to the adaptive error norm.
No training-only solve was needed or performed for this algebraic check.
This differs from A's query-augmented adaptive error control.

### Eight saved fit endpoints: replay and decision

The audit inspected exactly the six primary fits in `focus_projected` and
`focus_gaussian`, plus the two authorized near-pair fits in
`refinement_projected` and `refinement_gaussian`. It performed **no training
or integration**. Both candidates and their reports match the prefit freeze
in every source snapshot. Every snapshot matches its manifest. The same
runner, integrator and final protocol snapshots occur in all four fitted
campaigns; the runner correctly converts B's block dictionary to slices
before integration. The constructor-only A snapshot predates that harmless
runner-interface change. No candidate source changed between fits.

All primary/refinement numerical coefficients exactly match their upstream
constructor-only arrays. Refinement coefficient arrays also match primary
arrays, including metadata. The stored dense comparison functions equal
the original saved canonical references exactly. Saved model predictions,
training MSEs, circle errors and nested-panel errors replay exactly.

| Candidate | Task | Raw circle RMS | Endpoint time | Dynamic scalars, training / total |
|---|---|---:|---:|---:|
| A | near_pair_sin9 | 0.1511612051 | 13.530493 | 6 / 1038 |
| A | cluster_triple_cos9 | 0.7081889556 | 49.415691 | 10 / 1305 |
| A | cluster_triple_cos1 | 0.0147639776 | 5.595303 | 10 / 1305 |
| B | near_pair_sin9 | 0.3428953555 | 13.233368 | 6 / 6 |
| B | cluster_triple_cos9 | 0.8319302866 | 53.189525 | 12 / 12 |
| B | cluster_triple_cos1 | 0.0088194245 | 4.432443 | 12 / 12 |

**Both tested witnesses fail the frozen accuracy decision.** Neither has
both hard errors at most 0.05. Neither reaches the promising-partial
threshold, which requires both hard errors at most half their stated
bounded-Gram baselines, even though both pass the smooth-control limit.
A improves the near pair from the protocol's 0.24026 baseline but worsens
the hard cluster from 0.25268 to 0.70819. B worsens both hard comparisons.
No extension or scientific retuning is justified by the precommitted tree.

Across all eight fit records, fitted MSE error is at most 1.38e-16; alias
error is at most 1.57e-14; the smallest augmented Gram/covariance eigenvalue
is -1.06e-14; and the smallest tangent eigenvalue is 0.003189. There are
no saved accepted loss increases, nonfinite outputs, saturation violations,
or tanh/readout-energy bound violations. The largest 128/256-circle metric
change is 7.12e-8, well below 1e-4. Zero-residual RHS and the appropriate
query-independence RHS checks are exactly zero. The loss derivative's
additional central-difference discrepancy is at most 4.52e-10.

The exact algebraic energy checks pass at floating-point scale. An optional
central difference of B's quadratic readout energy at the hard-cluster
endpoint has absolute error 1.44e-7 at the single chosen small perturbation;
the independently contracted exact energy derivative error is 7.78e-16.
The less accurate finite difference is retained in raw audit output, not
silently discarded or rerun with a tuned perturbation. It is a numerical
derivative-evaluation qualification, not an energy-identity violation.
B's endpoint scalar-link 128/256 discrepancies are at most 2.23e-15 for
`s` and 9.95e-14 for `t`; all observed variances are below 3.285, within
the deterministic scalar-reference grid's range.

The tighter **near-pair only** fits change the actual 256-point prediction
by RMS 1.54e-11 for A and 1.15e-10 for B. These changes are far below the
large near-pair accuracy errors and the frozen 1e-4 gate. The cluster and
smooth tasks each have one new fit plus saved-state replay; their complete
trajectories were not independently reproduced or tolerance-refined in
this round. A query-free integration was not run. Those branches were
conditional on promising accuracy, and neither candidate triggered them.
No claim of independent all-task trajectory reproduction is warranted.

All eight recorded fits stop at the target. Their fitting times total
1.434726 seconds; the largest is 0.516794 seconds, below the per-fit
20-second cooperative limit. All use one BLAS thread, the prescribed
primary or refinement tolerances, and the physical time cap 3000. The
audited records contain six primary and two authorized refinement fits;
constructor checks are separately labeled nonintegrating. This accounting
concerns the designated saved campaigns, not a filesystem-wide claim about
unrelated activity.

### Storage accounting and reproducibility

The runner's `coefficient_scalars` counts B's serialized Unicode metadata
array as one scalar. The runner's `coefficient_bytes` includes that text's
uncompressed array bytes. Neither quantity should be presented as pure
numeric model size. Correct numeric counts and in-memory array accounting
are:

| Candidate / design | Numeric coefficient scalars / bytes | Serialized metadata-array bytes | Static model NumPy-array bytes including nested arrays | Dynamic state bytes |
|---|---:|---:|---:|---:|
| A / pair | 1300 / 10400 | 0 | 14608 | 8304 |
| A / cluster | 1834 / 14672 | 0 | 18960 | 10440 |
| B / pair | 1560 / 12480 | 13948 | 16608 | 48 |
| B / cluster | 2099 / 16792 | 14000 | 23008 | 96 |

For A, nested triangle-index arrays contribute 48/96 bytes omitted by the
runner's top-level `model_array_bytes`. For B, nested quadrature nodes and
weights contribute 2048 omitted bytes. Static counts include query
coefficients and cached solves; they exclude Python object overhead,
solver work arrays, temporary RHS/decoder allocations and width-dependent
initializer transients. No peak-memory measurement was recorded, so these
counts are not represented as a measured process-memory maximum. B's
quadrature nodes are fixed scalar special-function data, not evolving
neurons or particles.

The audit source is `audit_current_correlation.py`. Fresh outputs are
`current_correlation_20260930/audit/preflight_projected.json`,
`preflight_gaussian.json`, `focus_projected.json`, `focus_gaussian.json`,
`refinement_projected.json`, `refinement_gaussian.json` and `completion.json`.
They retain snapshot/input hashes, exact coefficient-reuse checks, all
replayed metrics, invariant checks, the less accurate central difference,
and refinement prediction comparisons. Audit-script hashes identify the
incremental preflight and full-audit versions; no candidate fit was rerun
by the auditor.

## Internal audit conclusion

The declared finite-model identities, implementation checks, saved-state
replay and designated provenance checks pass. Both candidates fail their
precommitted practical accuracy test. The failure is not evidence that
every finite current-correlation closure fails, and the tested exact
energy/positivity identities do not certify dense fidelity. Near-pair
tolerance checks substantially constrain an integration-error explanation
there; unperformed all-task refinement, dense width limits, full trajectory
causality and arbitrary-accuracy approximation remain outside this audit.
No promotion or independent-review status is implied.
