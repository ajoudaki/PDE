# Fixed-order population closure: Lyapunov geometry, p=1

Started 2026-09-16. Research only; nothing promoted to established material.

## Question and fixed contract

Find a current-state geometric or Lyapunov principle explaining hidden
organization in the canonical bias-free two-hidden-layer tanh population
closure on the normalized circle. State is (Gamma_1,Gamma_2,M). Preserve
full initialization correlations, eta=1/4096 inverse-Cholesky dictionary
normalization, physical unhalved probability-weighted square-loss metric,
and the actual M transpose. No closure-order or neural-width conclusion
is part of this investigation.

Scientific inputs are established docs/, code/, and this study's own
artifacts and generated data. No other study, network substitution or
frozen-feature approximation was used. Existing unrelated working-tree changes are
preserved; no shared book/code or Git-index changes were made.

## Current continuation: constructing the missing flow corrections

The user clarified that input perturbations should GUIDE THE DESIGN of a
potential through its training-time decay defect. Computing the old
potential's Hessian alone did not answer that request. The current account
is [correction_synthesis.md](correction_synthesis.md), under
[correction_contract.md](correction_contract.md).

Two actual constructions now replace a derivative-only answer. Neither
has established the desired broader unit-label initialized convergence
theorem; the all-rho claim remains OPEN.

First, the matrix extension is

    Phi_mat=L+mu0(1+q) xi^T(Gamma0+p p^T)^(-1)xi,
    p=(f(v_i))_i/sqrt(3), n=(1,1,1)^T/sqrt(3), xi=p-n,
    Gamma0_ij=E2[H_i(0)H_j(0)]/3,
    mu0=(n^T Gamma0^(-1)n)^(-1), q=E2[c^2].

It uses the initialized interpolation geometry and current predictions,
is regular even at current tangent rank losses, dominates L, starts at
two and agrees exactly with the old potential on symmetry. Its completed
square adds disagreement and mean/disagreement cross terms. The full
physical derivative and first/second TRAINED DEFECT are derived. A
quadratic initial defect is repaired with a geometry-dependent
normalization AND a changed trial rate; this does not preserve the old
rate 4C0 off symmetry and does not prove that 4mu0 works for all time.

This corrected potential has an all-time exponential theorem near every
unit-label symmetric seed with a regular fitting endpoint. That condition
has not been certified on a new rho range. Separately, its formula is
well defined for every distinct, non-antipodal three-input configuration:
the initialized feature Gram has rank three. The larger definition domain
is not a larger decay theorem.

Second, [correction_normal_form.md](correction_normal_form.md) constructs
cubic and quartic CURRENT-STATE corrections to the physical linear
correction cost xi^T K^(-1)xi. Finite algebraic equations choose the cubic
term to cancel its moving-metric flow defect, then choose the quartic
term to cancel the new defect. The exact remainder is quintic in current
error. The resulting loss-controlling potential has a proved local decay
inequality and an all-time certificate from a sufficiently accurate
current state with nonsingular K. This is a residual expansion, not an
all-path input expansion; coercivity already implies loss decay, and
the construction has not enlarged the initialized capture basin.

Two independent routes also locate a genuine limit to regular corrections.
At an assumed collapsed fitted state, explicit bounded state paths have
quartic loss and cubic gradient speed. Smooth positive residual-quadratic
potentials cannot have a uniform positive exponential rate on its whole
ambient neighborhood. This is not a reached-trajectory counterexample.
For an actual symmetric seed ending there, the first two trained input
responses are bounded and converge; the first prediction response vanishes,
while a possible second prediction disagreement produces fourth-order
loss. The decisive missing estimate concerns that source on initialized
reached states, not merely invertibility of an auxiliary metric.

| Artifact | Result and check scope |
|---|---|
| [correction_matrix.md](correction_matrix.md) | Explicit matrix extension, actual flow defect and quadratic corrections, regular-endpoint all-time theorem. |
| [correction_initial_rank.md](correction_initial_rank.md) | Generic three-input definition domain via initialized-field independence; no decay extension. |
| [correction_matrix_review.md](correction_matrix_review.md) | Fresh isolated complete review: PASS for both frozen inputs; rate-change and scope qualifications explicit. |
| [correction_normal_form.md](correction_normal_form.md) | Actual cubic/quartic defect cancellation, exact quintic remainder, local comparison and all-time current-state certificate. |
| [correction_normal_form_review.md](correction_normal_form_review.md) | Fresh isolated complete review: PASS, including physical-space bounds; two minor clarifications applied and verified in its addendum. |
| [correction_flow.md](correction_flow.md) | Correct state-function correction equations; gradient-square ansatz, explicit ambient obstruction, first/second response limits and possible third-order secular source. |
| [correction_design.md](correction_design.md) | Independent regular curvature metric and coupling correction, full derivative, current-coefficient fitting readout and independent first/second response argument. |
| [correction_singular_review.md](correction_singular_review.md) | Fresh isolated review of the singular-state obstruction and actual response claims in the two preceding reports. |
| [correction_validation.md](correction_validation.md), [correction_manifest.sha256](correction_manifest.sha256) | Author checks, exact review scopes, source integrity and current versions. |

The three analytical routes froze before comparison. Root owns the
normal-form and generic-rank constructions, this README and synthesis;
route authors and fresh reviewers wrote their assigned separate files.
No computation was run or numerical campaign reopened. Nothing is
promoted. Remaining authorized work is a reached-state mechanism that
controls the full corrected defect beyond the known regular endpoints;
the presence of explicit extra terms is not itself that mechanism.

## Previous continuation: broad rho family and full sphere Hessians

The user asks to extend the open-neighborhood result across the earlier
rho=2ab+b^2 family, and to capture independent second-order perturbations
of all three inputs. The authoritative account is now
[rho_hessian_synthesis.md](rho_hessian_synthesis.md), under the explicit
[continuation contract](rho_hessian_contract.md). The full unit-label
all-rho perturbation theorem remains OPEN; the preceding near-rho=1
unconditional theorem is retained below and has not been broadened by
assuming the missing condition.

For every rho in [-1/2,1), on each fixed-dictionary orientation branch,
we prove that positive transverse tangent geometry at the symmetric
FITTING ENDPOINT suffices for a free all-time input neighborhood with
the same exponentially decaying mixed potential. The tangent Gram may
lose rank earlier without invalidating this theorem. The only possible
symmetric transverse rank loss is simultaneous coincidence of all upper
preactivation coefficients M a_i and vanishing common backward vector d_i.
Every such loss is an isolated quadratic contact. What remains unresolved
is whether a contact can occur exactly at F=1 under the prescribed
initialization. Genericity in a varying label amplitude does not answer
that fixed-unit-label question.

The second-order request IS resolved at every fixed finite horizon: the
complete population flow is C2 in all six sphere tangent coordinates,
with a cubic remainder. All six first and 21 mixed second response
equations retain w,c,M, sphere curvature, the transpose and the data
dependence of C0. At a symmetric reference, five input directions have
vanishing scalar first variations. Their potential Hessian combines a
positive disagreement square with the second responses of mean output,
readout size and initialization geometry, whose signs are not fixed.

At a possible singular fitting endpoint, the first-order input response
vanishes. Quadratic predictor errors may then generate quartic loss,
while two weak tangent directions may open quadratically. We prove the
exact coefficients, including the projection removing the common gradient.
This is local geometry, not a selection rule for the trained endpoint or
an all-time decay proof. Global input convexity is also ruled out for the
trained potential at small positive times; that does not rule out decay
in training time. No compatible initialized convergence counterexample
has been constructed.

| Artifact | Result and check scope |
|---|---|
| [rho_endpoint_extension.md](rho_endpoint_extension.md) | Broad-family collapse criterion, isolated quadratic zeros, endpoint-only perturbation theorem, and precise exceptional-amplitude scope. |
| [rho_endpoint_extension_review.md](rho_endpoint_extension_review.md) | Fresh isolated complete review: PASS for that candidate and its declared dependencies. |
| [sphere_second_variation.md](sphere_second_variation.md) | Complete finite-time sphere response/Hessian theorem, Gaussian-weighted remainder proof, symmetry and global curvature constraints. |
| [sphere_second_variation_review.md](sphere_second_variation_review.md) | Fresh isolated review: PASS for the finite-horizon theorem and structural conclusions; no mathematical repairs required. |
| [rho_hessian_geometry.md](rho_hessian_geometry.md) | Independent derivation of the broad-family obstruction and endpoint theorem; full inverse-correction second variation, normal endpoint geometry and valid data-dependent gluing. Root checked completely. |
| [rho_singular_hessian.md](rho_singular_hessian.md) | Explicit quadratic predictor, quartic loss and projected second-order metric-opening coefficients at an assumed singular fitting state. |
| [rho_singular_hessian_review.md](rho_singular_hessian_review.md) | Fresh isolated review: PASS; two minor notation/scope repairs applied and verified in its versioned addendum. |
| [rho_global_rate_boundary.md](rho_global_rate_boundary.md) | Continuity proves loss of any geometry-independent rate near contradictory data, including through nondegenerate triples. Author checked; no fixed compatible failure example. |
| [rho_hessian_validation.md](rho_hessian_validation.md), [rho_hessian_manifest.sha256](rho_hessian_manifest.sha256) | Complete root checks, review scopes, source integrity and current artifact versions. |

The analytical routes froze before comparison. Assigned authors used only
the specified established inputs and this study's artifacts. Root owns this
README and synthesis; the independent authors and reviewers wrote separate
flat reports. No experiment was run, the old diagnostic campaign stays
closed, and nothing was promoted. The next authorized mathematical task
is exclusion of the simultaneous collapse at F=1, or a nonlinear tail
estimate at that event using the derived quadratic coefficients. The
finite-time Hessian itself is no substitute for that estimate.

## Previous unconditional result: an open family with unequal angles

The perturbation route now gives a complete local theorem for the exact
canonical **d=3** population closure, with labels exactly (+1,+1,-1).
The main proof is [resolution_open_family.md](resolution_open_family.md),
and [resolution_synthesis.md](resolution_synthesis.md) states its meaning
and remaining boundaries. The continuation contract is
[resolution_contract.md](resolution_contract.md).

For every sufficiently small positive e, take the distinct signed reference
directions v_i=(1+e e_i)/sqrt(3+2e+e^2). There is a positive neighborhood of
this triple such that EVERY unit input triple in that neighborhood, after
absorbing the fixed label signs, has a positive full tangent-Gram lower bound
for all physical time from prescribed initialization. This is an open family
with no required equality of angles or data symmetry. The full state converges
to a fitting state, with remaining physical length at most sqrt(L/k).

The same explicit mixed potential survives the perturbation:

    U=(H1+H2-H3)/3, F=E[cU], q=E[c^2], C0=E[U0^2],
    Phi=L [1+C0(1+q)/(C0+F^2)].

For a geometry-dependent positive lambda, it satisfies
L<=Phi, Phi(0)=2 and Phi_dot<=-lambda Phi at every time. Every derivative
of the changing multiplier is included. Loss itself also decays exponentially.
The new proof uses the first-layer reverse response to control the two
prediction-difference directions that the old scalar proof did not control.
It proves all-time trapping after a finite-time comparison, rather than
assuming that finite-horizon perturbation control extends indefinitely.

This supersedes the previous absence of an unconditional nonsymmetric open
family. It does not settle all angular configurations, the unit-label
orthogonal reference, or arbitrary three-input configurations for the
original canonical **d=2 circle** dictionary. The neighborhood is proved
positive but has no numerical radius. A quantitative addendum proves that
the symmetric seeds' full tangent conditioning is bounded above and below
by positive constants times e^2; the nonsymmetric potential rate may be
chosen at least a constant times e^2. No experiment was run or result promoted.

| Artifact | Result and check scope |
|---|---|
| [resolution_open_family.md](resolution_open_family.md) | Complete unit-label open-family theorem, full tangent coercivity, mixed potential and complete-state convergence. |
| [resolution_open_family_review.md](resolution_open_family_review.md) | Fresh isolated complete analytical review: PASS for the unchanged frozen theorem and all its required canonical/symmetric dependencies. |
| [resolution_root_check.md](resolution_root_check.md) | Complete author-side reconstruction and checks of the independent routes. |
| [resolution_rate.md](resolution_rate.md) | Complete quantitative refinement: sharp e^2 full-tangent conditioning for the nearby symmetric seeds and an e^2 lower potential rate for their open neighborhoods. |
| [resolution_rate_review.md](resolution_rate_review.md) | Separate complete follow-up analytical review of the quantitative addendum: PASS, with no repairs. |
| [resolution_endpoint.md](resolution_endpoint.md) | Orthogonal transverse rank-loss events are isolated and quadratic; the unit endpoint remains undecided. |
| [resolution_positive.md](resolution_positive.md) | Independent derivation of the same orthogonal obstruction and isolated rank loss. |
| [resolution_metric.md](resolution_metric.md) | Secondary theorem for all but locally finitely many common label amplitudes; not a unit-label substitute. |
| [resolution_synthesis.md](resolution_synthesis.md) | Current theorem, mechanism, supersession and explicit remaining gaps. |
| [resolution_validation.md](resolution_validation.md), [resolution_manifest.sha256](resolution_manifest.sha256) | Review scopes, unchanged frozen candidates, source integrity and final artifact versions. |

## Previous follow-up: perturbation identifies missing potential terms

At the preceding stage, the user proposed perturbing a solved configuration to identify
the missing potential terms, especially interactions involving the first
hidden layer. This continues the same investigation. The current account
was [perturbation_synthesis.md](perturbation_synthesis.md), under the
[bounded analytical contract](perturbation_contract.md).

The method has produced exact new information. Away from symmetry the
signed predictions split into a mean F and two disagreement directions.
Their coupling is sign-indefinite and involves all three gradient blocks
w,M,c. On a fixed horizon, an epsilon input perturbation creates
O(epsilon) disagreement and O(epsilon^2) disagreement energy/coupling;
the mean quantities can still change at first order. These are not
all-time stability estimates.

There is a concrete current-state candidate geometry: the minimum squared
physical parameter correction that removes the current residual in the
linearized predictor. It is r^T K^(-1)r for the probability-normalized
signed residual and full tangent Gram. Its expansion contains disagreement
energy, a mean/disagreement cross term and the term completing their square.
Its derivative includes the full moving-Gram correction. A specified
matrix-evolution inequality would make L+lambda r^T K^(-1)r an exponential
potential directly bounding loss. That inequality remains UNPROVED for
generic initialized trajectories; this is a conditional template.

A new exact first-layer/middle-layer balance is also proved: for orthogonal
unit inputs, ||M||F^2-E1 sum_i sinh^2(w.u_i) is conserved. For other input
angles its derivative is an explicit residual-weighted forward/backward
cross term. This is an invariant/defect identity, not a positive potential.
At the orthogonal three-input reference, first-layer sensitivity can
protect transverse tangent directions even when upper activations coincide.
An exact endpoint-degeneracy criterion was derived, but exclusion of that
event along the initialized trajectory remains open.

| Artifact | Actual result and check |
|---|---|
| [perturbation_modes.md](perturbation_modes.md) | Independent full Gram, mean/disagreement equations, old potential defect, and inverse-transverse correction with all metric derivatives; root checked completely. |
| [perturbation_lower_balance.md](perturbation_lower_balance.md) | New exact orthogonal balance, angular defect, finite-horizon bound, narrow primitive obstruction and coordinate metric. |
| [perturbation_lower_balance_audit.md](perturbation_lower_balance_audit.md) | Fresh complete audit: formulas pass; three scope clarifications applied without changing equations. |
| [perturbation_orthogonal.md](perturbation_orthogonal.md) | Independent exact transverse criterion and preserved middle-matrix component; complete root check, endpoint exclusion still open. |
| [perturbation_metric_template.md](perturbation_metric_template.md) | Root's minimum-correction geometry, explicit Schur expansion and full evolving-metric derivative. |
| [perturbation_metric_check.md](perturbation_metric_check.md) | Complete post-freeze check, plus the stronger conditional potential L+lambda E that needs no uniform upper Gram bound. |
| [perturbation_synthesis.md](perturbation_synthesis.md) | Current interpretation, claim boundaries, corrections and exact remaining estimate. |
| [perturbation_manifest.sha256](perturbation_manifest.sha256) | Current artifact/dependency versions; earlier manifests retain historical README versions. |

The geometry restriction remains a restriction of the proved mechanism;
necessity for learning has not been shown. The first layer was fully
trained in the earlier theorem but its specific transverse geometry was
not used. This follow-up exposes that unused information. No experiment
was run, and the earlier numerical campaign stays closed. Nothing is
promoted. At that stage the generic circle theorem and an unconditional
perturbed-family extension remained open. The current result above resolves
the latter for a specific d=3 open family, while preserving the former gap.

## Earlier exponential-potential continuation

The primary target remains three generic equal-mass circle inputs with
labels (+1,+1,-1), now seeking an exponentially decaying current-state
potential with any increasing loss comparison. **The unconditional
generic circle theorem remains open. No initialized convergence
counterexample has been constructed.** The current authoritative account
is [three_exp_synthesis.md](three_exp_synthesis.md); its primary contract
is [three_exp_contract.md](three_exp_contract.md).

A complete restricted theorem is now available for three correlated
inputs in **three dimensions**, preserving the exact canonical general-d
p=1 initialization and full dynamics. For

    u1=(a,b,b), u2=(b,a,b), u3=-(b,b,a),
    a^2+2b^2=1, a!=b, labels=(+1,+1,-1),

define U=(H1+H2-H3)/3, F=E[cU], and C0=E[U0^2]>0. The potential

    Phi = L [1 + C0 (1+E[c^2])/(C0+F^2)]

satisfies L<=Phi<=2L and Phi_dot<=-4 C0 Phi from initialization, with
Phi(0)=2. Also L<=exp(-4 C0 t), ||U||^2>=C0, and the complete state
converges to a fitting endpoint with remaining physical length at most
sqrt(L/C0). The initialized three-feature Gram has rank three. The
proof uses coordinate-permutation symmetry, which restricts the realized
residual to one direction; it is not a generic multiresidual theorem.
The admitted choice a=-2/sqrt(6), b=1/sqrt(6) has u3=u1+u2 with
labels (+1,+1,-1), so a bias-free linear predictor cannot even classify
it correctly. The nonlinear closure is proved to fit it.

[three_coordinate_many_inputs.md](three_coordinate_many_inputs.md) gives
the same restricted-family theorem for every fixed m=d>=3 and arbitrary
label signs. Root checked the complete corollary, including its new
rank exception and dimension-dependent bounds; the fresh three-input
audit does not cover that later artifact.

This dimensional extension remains separate from the original
two-dimensional dictionary problem. The user welcomed the result and now
asks to use it or an orthogonal reference to identify a more general
potential's form. This does not identify the d=3 dictionary with d=2.
The earlier scope decision is recorded in
[three_exp_scope_update.md](three_exp_scope_update.md).

| Artifact | Result and check scope |
|---|---|
| [three_coordinate_candidate.md](three_coordinate_candidate.md) | Complete frozen d=3 restricted-family theorem, including direct population existence, exact symmetry, initialization, potential and endpoint. |
| [three_coordinate_root_check.md](three_coordinate_root_check.md) | Root's complete author-side reconstruction: PASS at the stated d=3 scope. |
| [three_coordinate_audit.md](three_coordinate_audit.md) | Fresh isolated complete analytical review: PASS for the frozen d=3 candidate, including all canonical dependencies and initial-time/degenerate-rank cases. |
| [three_exp_root.md](three_exp_root.md), [three_exp_reparam_check.md](three_exp_reparam_check.md) | Explicit conditional exponential potential and complete bounded check, on a declared bounded-readout sublevel below L=1/3. |
| [three_exp_escape.md](three_exp_escape.md), [three_exp_escape_audit.md](three_exp_escape_audit.md) | Lower coefficient submersion, positive-loss strict saddles in the stated chart, and ambient stationary examples; fresh review PASS. |
| [three_exp_escape_second_pass.md](three_exp_escape_second_pass.md) | Bounded readout returns suffice below L=1/3; positive limiting loss forces geometric degeneration and, below that threshold, diverging readout. |
| [three_exp_openfamily.md](three_exp_openfamily.md) | Conditional capture and openness, plus an exact initialized obstruction to global monotonicity of L(1+||c||^2). No initialized capture seed proved. |
| [three_exp_invariant.md](three_exp_invariant.md) | Nonlinear balance defect and fixed-positive-loss ambient states with arbitrarily small full gradient. Not a trajectory counterexample. |
| [three_exp_product_check.md](three_exp_product_check.md) | Explicit countersequence to a readout-speed/readout-norm product bound; hidden gradient remains uncontrolled. Root checked the complete construction. |
| [three_exp_diagnostic_report.md](three_exp_diagnostic_report.md) | Seven predeclared finite-rule runs completed; primary population-monotonicity test inconclusive because its refinement gate failed. |
| [three_exp_synthesis.md](three_exp_synthesis.md) | Current claim ledger, exact gaps, proof interpretation and provenance. |
| [three_exp_validation.md](three_exp_validation.md), [three_exp_manifest.sha256](three_exp_manifest.sha256) | Final proof-scope, provenance, link and source/array identity checks for this continuation. |

One modest diagnostic was run and closed, using 3.7003 CPU seconds and
111372 KiB peak resident memory. Its source, command, deterministic
initialization, source/array hashes and validity thresholds are retained
in [three_exp_diagnostic.py](three_exp_diagnostic.py), its report and
`data/generated/closure_lyapunov_p1_20260916/three_exp_diagnostic_01/`.
No numerical observation is used to complete a proof. These are internal
research results, not established or promoted material.

## Earlier generic three-input continuation

The user's latest target is a mixed current-state potential for three
generic equal-mass circle inputs with labels (+1,+1,-1), permitting
individual class distances to move either way. **Unconditional fitting
and such a potential remain unresolved. No convergence counterexample
has been constructed.** See [generic3_synthesis.md](generic3_synthesis.md)
for that stage's conclusions and [generic3_contract.md](generic3_contract.md)
for the exact target and scoped route assignments.

The strongest new theorem is conditional: if the actual trajectory ever
reaches L<1/3 and its readout c stays bounded in L2 thereafter, then L tends
to zero. It needs neither bounded w or M nor a uniformly positive full
hidden Gram. The proof compactifies the exact upper tanh feature family
by adding sign fields, proves independence after grouping equal/opposite
fields, and uses readout stationarity to force fitting. Both hypotheses
remain unproved for arbitrary generic initialized unit-label triples.

| Artifact | Result and actual check |
|---|---|
| [generic3_stationary_geometry.md](generic3_stationary_geometry.md) | Root's complete stationary characterization, feature compactness and conditional convergence proof. |
| [generic3_compactness_check.md](generic3_compactness_check.md) | Complete bounded post-freeze analytical check of that proof: PASS; not an isolated whole-study review. |
| [generic3_metric_route.md](generic3_metric_route.md) | Exact residual defect and a conditional reached-state capture theorem; root checked the algebra and limitations. |
| [generic3_metric_second_pass.md](generic3_metric_second_pass.md) | Mixed feature/readout barriers, nonlinear balance defects, and explicit correction that the capture comparison is history-dependent, not a saved-state potential. |
| [generic3_geometry_route.md](generic3_geometry_route.md) | Exact distance evolution and open-set same-class expansion in both hidden layers; a stress test only for the requested mixed potential. |
| [generic3_geometry_audit.md](generic3_geometry_audit.md) | Fresh isolated complete analytical audit of the unchanged geometry candidate and its canonical dependencies: PASS. |
| [generic3_synthesis.md](generic3_synthesis.md) | Current claim ledger, precise remaining estimates, provenance and scope. |
| [generic3_manifest.sha256](generic3_manifest.sha256) | Final continuation artifacts and canonical source versions. |

No experiments were run at that stage. These results are internal research, with exact
or conditional status as stated; nothing is promoted. Root and the two
fresh scoped routes compared candidates only after freezing them. The
later second-pass checks are identified separately. The user's mixed
potential proposal is not disproved by nonmonotone pairwise distances.

## Earlier arbitrary-arrangement extension

Read [all_angles_result.md](all_angles_result.md) for the current combined
argument and exact remaining gap. The earlier [synthesis.md](synthesis.md)
and [proof.md](proof.md) are retained as historical, narrower results.

For balanced opposite labels +/-A, the following are proved in the exact
initialized p=1 closure:

| Input family | Label scope | Conclusion |
|---|---|---|
| Distinct pairs related by a coordinate or diagonal reflection of the actual dictionary | Every A>0, including A=1 | Full-state fitting and convergence; protected hidden contrast and strictly larger endpoint contrast. Every separation angle in (0,pi] occurs. |
| Antipodal pairs in any orientation | Every A>0 | The same conclusions, by architectural oddness. |
| Any distinct non-antipodal pair, with arbitrary orientation | 0<A<=lambda(u,v)/(8 sqrt(5)) | Full-state fitting and convergence; a codimension-two local fitting set with neutral directions. |

Here lambda(u,v)>0 is the exact least eigenvalue of the initialized
probability-weighted upper-feature Gram, proved positive for every
non-antipodal distinct pair. The small-label hypothesis is substantive;
it does not prove the arbitrary-orientation unit-label target.

The new current-state potential on the scalar-residual families is

    P = ||c||^2/F^2,        P(0+) = 1/C_0,
    Phi = (1+||c||^2)/(C_0+F^2),

where U=(H_+-H_-)/2, F=<c,U>, and C_0=||U_0||^2>0. Both are nonincreasing
along the initialized trajectory; Phi is regular at initialization.
The exact normalized-readout inequality proves

    ||U_t||^2 >= C_0,
    L(t) <= A^2 exp(-4 C_0 t),
    remaining physical length <= sqrt(L(t)/C_0),
    ||U_infty||^2 > C_0.

Thus training preserves a useful distinction between the opposite-label
inputs, increases their upper hidden separation at the endpoint, and
converges in the full physical state metric and joint-law W2 topology.
Neither potential must tend to zero, and intermediate hidden separation
need not be monotone. Neutral fitting directions remain.

The old near-antipodal angle restriction and lower cross-sign bottleneck
are superseded for reflection-pair convergence. The cross-sign question
remains open only as a separate coefficient-level mechanism. The precise
remaining primary gap is **arbitrary orientation with unit labels**: the
common prediction need not vanish, so a second residual direction enters
the flow. Initial full Gram positivity alone does not control that direction
through large nonlinear motion. The fixed finite dictionary has no
arbitrary rotational symmetry.

Coincident contradictory labels and same-label antipodes remain exact
obstructions. Ambient M=c=0 remains a positive-loss stationary state, so
the initialized-trajectory hypotheses cannot be discarded.

## Follow-up: three or four unit-labelled inputs

[three_four_input_extension.md](three_four_input_extension.md) records the
bounded analytical follow-up requested by the user. Its exact conclusions are:

- Four equally weighted rectangle vertices (a,b),(a,-b),(-a,b),(-a,-b),
  with a,b>0, a^2+b^2=1 and labels +1,-1,+1,-1, inherit the same potential,
  full-state convergence and strict endpoint class-mean contrast gain.
  This is an exact ambient loss/gradient reduction by architectural oddness.
  The antipodal constraints are redundant, so this result does not introduce
  an additional independent residual mode.
- For ANY three or four distinct unit directions with no antipodal pair,
  the initialized upper hidden functions are linearly independent. A cubic
  Taylor identity and a Vandermonde determinant prove this from the checked
  initialized map. Every assignment of unit labels is therefore representable
  with a bounded readout and the initialized hidden state. This is an existence
  certificate, not a claim that training freezes features or converges.
- A concrete next problem is the equally weighted dataset (e1,+1),(e2,+1),
  ((e1+e2)/sqrt(2),-1). Its actual coordinate-swap symmetry leaves two
  independent residual modes. Global unit-label fitting and a geometric
  potential controlling both remain OPEN.

Root checked the complete new derivation analytically, including probability
factors, gradient identities, rank exceptions, and the distinction between
representability and training. This is an author-side internal check; no new
independent review, experiment, or promotion took place. The added artifact
and current README are versioned by
[three_four_input_manifest.sha256](three_four_input_manifest.sha256).
Earlier manifests are preserved as historical versions of the current notes.

## Extension evidence and internal checks

| Artifact | Scope and check role |
|---|---|
| [continuation_contract.md](continuation_contract.md) | Exact user-requested target, source versions, scoped assignments, and no-experiment decision. |
| [scalar_margin_extension.md](scalar_margin_extension.md) | Frozen normalized-readout argument, finite feature-time existence, noncollapse, rate and complete-state convergence. |
| [scalar_margin_audit.md](scalar_margin_audit.md) | Complete analytical audit of that scalar argument: PASS. |
| [all_angles_cone_attempt.md](all_angles_cone_attempt.md) | Independent all-angle initialized positivity proof. Its later cone gap is retained but no longer needed for convergence. |
| [scalar_strict_gain.md](scalar_strict_gain.md) | Nonzero initial hidden gradient implies strict endpoint contrast gain. |
| [all_angle_ingredients_audit.md](all_angle_ingredients_audit.md) | Complete assigned checks of all-angle initialization and strict-gain ingredient: PASS. |
| [all_angle_combination_check.md](all_angle_combination_check.md) | Post-freeze author-side check of the combined all-angle reflected result: PASS. |
| [arbitrary_pair_local.md](arbitrary_pair_local.md) | Exact initialized map, strict scalar monotonicity, arbitrary-pair Gram rank, and full local small-label proof. |
| [arbitrary_initialization_audit.md](arbitrary_initialization_audit.md) | Detailed independent internal audit of its complete initialization Sections 1–4, including every constant: PASS. |
| [check_arbitrary_local_root.md](check_arbitrary_local_root.md) | Root's complete analytical check of Sections 1–7, including basin and topology: PASS. |
| [antipodal_upgrade_check.md](antipodal_upgrade_check.md) | Checks every-orientation antipodes, actual signed-permutation reflections, and the absence of arbitrary dictionary rotations. |
| [regular_potential_check.md](regular_potential_check.md) | Checks the full regular-potential derivative and strict contrast gain for all four reflection involutions. |
| [all_angles_result.md](all_angles_result.md) | Root's current combined proof, with the dependency chain and unresolved generic unit-label case explicit. |
| [continuation_validation.md](continuation_validation.md) | Final combined-scope, algebra, link and source-version checks. |
| [continuation_manifest.sha256](continuation_manifest.sha256) | Exact identities for this continuation and its final current notes. |

The displayed extension results are **proved and internally checked at
the stated scopes**. Checks are analytical, with their actual coverage
recorded in the reports; they are not formal verification or promotion
reviews. Generic unit-label convergence remains open, not disproved.

## Earlier evidence, provenance and checks (retained history)

| Artifact | Claim and check role |
|---|---|
| [route_global.md](route_global.md) | Fresh scoped independent axis-cone derivation; complete proof and direct all-angle-route obstruction. Frozen before comparison. |
| [route_local.md](route_local.md) | Fresh scoped independent small-label theorem near orthogonal inputs; codimension-two fitting geometry and finite state length. Frozen before comparison. |
| [route_extension.md](route_extension.md) and [proof.md](proof.md) | Root's axis calculation and explicit unit-label angular extension; frozen input and edition with the four audited presentation corrections. |
| [extension_check_global.md](extension_check_global.md) | Post-freeze full analytical cross-check of extension by the axis-route author; no substantive gap found. |
| [check_local_root.md](check_local_root.md) | Root's complete analytical check of the local route, including exact constants, topology and manifold proof; passed for stated small-label scope. |
| [audit_extension.md](audit_extension.md) | Fresh isolated complete mathematical audit of the main frozen proof: PASS, four nonblocking presentation corrections applied in proof.md. |
| [audit_final_edition.md](audit_final_edition.md) | Direct diff verifies all four presentation fixes and unchanged mathematical content/constants in proof.md. |
| [geometric_corollary_check.md](geometric_corollary_check.md) | Post-freeze check of current-state correction, its full evolving derivative, neutral directions and distinction between physical and joint-law distances. |
| [cross_sign_note.md](cross_sign_note.md) | Corrects the frozen global route: one open cross-sign estimate would control both signal and common modes; all-angle initial positivity must also be checked. Conditional route, not an all-angle proof. |
| [source_hashes_initial.txt](source_hashes_initial.txt) | Initial HEAD and hashes of all relevant instructions and established scientific inputs. |

The main theorem is **proved and internally checked** at its exact scope.
The fresh audit read every scientific line of its frozen candidate and
complete relevant canonical inputs; it found no blocking mathematical gap.
The four corrections concern naming, deterministic positivity wording and
clarifying active equations versus symmetry-frozen coordinates. The corrected
edition retains every mathematical constant and conclusion. The local theorem
and geometric corollary also pass their stated internal checks. These checks
are not the separate promotion procedure or formal machine verification.

Canonical sources: docs/global_nonlinear.md C.4.7.9 state/dynamics/existence,
C.4.7.10 B/C.1 dictionary and complete initialization, and D.3. Shared
AGENTS.md, RESEARCH_WORKFLOW.md Part 1, docs/README.md, docs/NOTATION.md,
and the research and rigorous-mathematics skills were read. Relevant source
hashes were rechecked unchanged during the investigation.

## Claim classification and limitations

The main and complementary claims are analytical proofs for their exact
restricted data families. They are not empirical claims or conditional
inferences from numerics. Internal check status is distinct from promotion;
no promotion process has been started. Broader coefficient-level sign control is
open, not disproved; it is unnecessary for the new reflection theorem. The ambient nonstall extension is disproved by the
explicit stationary state. No claim about generalization or agreement of
p=1 with the full network at long times is made.

The earlier pair and first three-input results required no numerical
experiments. Their reproduction consists of following the complete
displayed algebra and constant definitions against the hashed canonical
source. The later exponential-search diagnostic is recorded above with
its separate reproducibility obligations and inconclusive primary result.
No external scientific theorem is used to fill a missing estimate.

## Contributors and ownership

Root owns README, current combination, provenance, normalized-readout
proof and complete local-route check. pair_global owns the cone/sign
route, initialized positivity, and its assigned post-freeze checks.
local_geometry owns the arbitrary-pair initialized map and local theorem,
and its assigned symmetry/corollary checks. audit_extension owns its
assigned internal audit reports. Independent route candidates were frozen
before cross-comparison; later combination checks are identified as such.
All artifacts remain flat in this study. No Git transaction or shared-path
edit was made by this investigation.

For the generic-three-input continuation, generic3_metric owns its two
metric-route artifacts; generic3_geometry owns its independent geometry
route and the later compactness check; generic3_audit owns the fresh
geometry audit. Root owns the contract, stationary/compactness argument,
synthesis, README and manifest. The second-pass agents' exposure to root
arguments is disclosed in their reports.

## Remaining authorized research and close status

The generic-three-input exponential search has produced the exact and
conditional results listed above. Its primary circle theorem is unresolved.
A sufficient next route is to prove entry below loss 1/3 and bounded
readout returns, or a combined hidden/readout estimate that excludes
positive-loss escape; obtaining an exponential potential also requires
the stated quantitative or bounded-region bridge. A second route is
initialized entry into the exact capture region. Initial representability
is proved and is not the missing estimate. The d=3 permutation theorem
does not discharge these circle obligations.

The analytical routes and assigned checks for this continuation are
complete, including the fresh d=3 review. No computation or agent is
running. The computation is closed; no extra run is implied by its unused budget.
No promotion is requested. All earlier frozen proofs, reports and historical
manifests remain intact. The new routes were frozen before comparison;
post-freeze root-supplied arguments are explicitly identified in their files.
The separate escape second pass preserves the original audit target's
exact hash; the reviewer records the temporary append/restore incident.

For this continuation, three_exp_invariant owns its original invariant,
reparametrization check and product-countersequence files; three_exp_escape
owns its original and second-pass analyses; three_exp_openfamily owns its
capture analysis and the identified post-freeze check. three_exp_audit
owns the isolated escape review. three_coordinate_candidate owns the
dimensional alternative, and three_coordinate_audit its fresh isolated
review. Root owns the conditional construction, diagnostic, synthesis,
current notes, scope record, author reconstruction and final validation.

For the perturbation follow-up, perturbation_modes owns its frozen mode
derivation and later metric check; perturbation_orthogonal owns the frozen
orthogonal criterion; perturbation_balance_audit owns the fresh lower-balance
review. Root owns the balance, full correction-metric template, synthesis,
README and manifest. These analytical routes and checks are complete, with
the open estimates explicitly retained. No computation or agent is running.
