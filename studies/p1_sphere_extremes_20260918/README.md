# Three-input p=1 sphere extremes

## Question and exact scope

Started 2026-09-18 in response to the user's request to investigate slow
initial learning, slow terminal convergence, and positive-loss failure using
three normalized inputs in dimension three. This is a new study because both
the input domain and the primary research direction changed. Its scientific
repository inputs are only established docs/code and its own artifacts. No
unpromoted proof or diagnostic from any other study is imported.

Use the exact general-dimensional p=1 initialized construction in
`docs/observable_p1.md`, with d=3, x in sqrt(3) S2, phi=tanh, ridge 1/4096,
zero population readout, full joint Gaussian lower marks, and the actual
transpose of the full moving M. After the proved odd-parity reduction,
b1 has dimension six, b2 dimension three, w dimension three, and M is 3x6.
All three parameter blocks evolve in the physical L2/L2/Frobenius gradient
metric for the unhalved probability-weighted square loss. Fixed-order
population dynamics, not approximation of a neural-width limit, is the target.
Binary unit labels and positive masses are retained; balance is preferred
when compatible with the mechanism being tested.

Separate: initial slope, fixed-threshold hitting time, eventual fitting,
terminal rate at each fixed nondegenerate configuration, and behavior as
configurations degenerate. Slow rates along a family do not by themselves
disprove an exponential rate for each fixed member. A positive conclusion
requires a proved protection mechanism, not merely failure to find a counterexample.

## Workflow, ownership and sources

Read AGENTS.md, workflow Part 1, research and rigorous-mathematics skills,
docs/README.md and docs/NOTATION.md. Scientific equation inputs are
`docs/observable_p1.md` completely and the saved-state, physical metric and
well-posedness proof of `docs/global_nonlinear.md` C.4.7.9.3--4 and
C.4.7.10.D.3, adapted explicitly to the fixed finite dimensions here.

The primary agent owns this README, synthesis, verification and manifests.
Fresh agents independently examine initial delays, asymptotic obstructions,
and protected three-input families, using only assigned established sources.
They own separate flat reports and do not see each other's candidates before
freeze. Only this study and its generated namespace may be written.

HEAD at startup: 019e3630237e33f58b9636c0aa67a039bebf0182. Index empty.
Unrelated concurrent changes are preserved. No shared-source edit, promotion,
stage or commit is part of this research request.

## Current status and authorized work

The input-perturbation continuation has two complementary results,
integrated in [INPUT_PERTURBATION_RESULTS.md](INPUT_PERTURBATION_RESULTS.md).
Almost every fixed tangent input direction removes PSD bad equilibria
from a physical-Hilbert neighborhood of the original fixed state, at
sufficiently small direction-dependent amplitudes. But every neighborhood
of the original data contains an open set admitting other exact PSD
equilibria of loss 48/49. The counterexample extends to an open family of
fixed perturbation directions at every sufficiently small positive
direction-dependent amplitude. A seed continuation and shrinking open
data neighborhoods have uniformly bounded states and one fixed matrix
and readout, converging to a different original equilibrium. Each new
finite-perturbation state has cubic descent, and the same data have an
explicit zero-loss fit. The complete proofs passed a fresh internal
review; the main counterexample also passed an informed analytical
cross-check. Thus generic input noise does not restore the global
strict-saddle premise. No nonparallel bad basin of positive probability
or canonical initialized failure has been proved.

The user's requested quick finite-network check is complete in
[WIDE_NETWORK_GF_RESULTS.md](WIDE_NETWORK_GF_RESULTS.md). Two canonical
width1024, two-hidden-layer tanh networks fitted the seven-input geometry
to loss below1e-6, rather than remaining at48/49. A tenfold tighter
same-seed integration replay passed the predeclared agreement checks.
The three runs took44.884 seconds and157.36MiB peak RSS. This is empirical
evidence for the actual finite networks; it does not settle fixed-p=1
canonical reachability or infinite-time basin probability.

The latest data-restriction continuation is summarized in
[INPUT_CONDITION_RESULTS.md](INPUT_CONDITION_RESULTS.md). An open,
dependent four-input family recovers the whole below-one bad point-basin
theorem. Explicit loss thresholds extend it to larger circuits and to
arbitrarily many nonparallel inputs in a fixed dimension. A proposed
stronger general data-rank certificate is proved too restrictive for
every dependent equal-weight family with five or more inputs. The new
results are internally checked by independent initial derivations, lead
reconstruction, and a documented informed check of the synthesis; they
have not received a fresh isolated review or promotion.

The preceding arbitrary-finite-input continuation is summarized in
[FINITE_BASIN_EXTENSION.md](FINITE_BASIN_EXTENSION.md). A seven-input
equal-weight construction disproves the universal strict-saddle premise,
even with an actual positive-semidefinite Hilbert Hessian and cubic descent.
Special descending positive-plateau trajectories exist, but the unrestricted
finite-input bad-basin probability remains open. New scoped basin extensions
and a deterministic finite-input stationary-loss gap are also proved.

The complete three-input basin theorem and its precise remaining gaps are in
[DEPENDENT_BASIN_RESULTS.md](DEPENDENT_BASIN_RESULTS.md). Linear independence
is removed entirely for equal-weight compatible triples, including every
nonaligned circle triple, and for generic arbitrary-weight triples. The
bad point-convergence basin is meagre and null under the same specified
population-field randomization. Arbitrarily many finite compatible inputs
also admit an explicit nonempty open exponential fitting basin.
[BASIN_RESULTS.md](BASIN_RESULTS.md) retains the preceding independent-input
theorem. These results do not settle canonical initialized fitting or
positive-loss behavior without a state limit.

The principal results have passed fresh isolated internal mathematical
review. These remain study results, not established book material. Read
`PLATEAU_CLASSIFICATION.md` for the current terminal question, new
landscape/escape theorems and the still-open configuration-only iff.
`WEIGHTED_THREE_INPUT_RESULTS.md` contains the complete weighted slow-onset
classification and architectural plateau, and `MAIN_RESULTS.md` contains
the earlier slow-family and protected-fitting results.

* `early_delay.md`: balanced genuine three-input family, initial slope of
  order epsilon^4 and fixed-threshold delay at least order epsilon^-2.
  The proof retains all trained blocks through an energy barrier.
* `necessary_potential_growth.md`: general close-pair delay and the precise
  implication of any delay for a uniformly exponentially decaying potential
  with declared power domination of loss.
* `terminal_geometry.md`: full finite fitting-state singularity criterion
  for three independent inputs; an initialized signed-axis class has a
  strictly exponential terminal asymptotic. Ambient singularity is not
  asserted to be reachable from initialization.
* `protected_family.md`: the scalar prediction/readout ratio protects a
  learning signal. The complete unconditional theorem covers an open
  family of independently perturbed inputs and weights, with all-time
  L'<=-lambda L and actual bounded fitted endpoints. Every initialization,
  endpoint-rank, entrance and trapping obligation is proved. Mixed labels
  have reference masses 2/3 and 1/3; balance is not asserted for this result.
* `initialization_positivity.md`: an elementary analytic proof that the
  full conditional initialized coefficient preserves sign, including the
  reverse response and actual ridge. No numerical constant is a premise.
* `cyclic_uniformity.md`: a subsequent compactness corollary extends the
  symmetric reference guarantee to all canonical cyclic three-input
  orbits, with one positive rate. It includes a zero signed-first-moment
  nonlinear classification example. Its independent review passed. It
  does not enlarge the separately proved independent-perturbation range.

Reviews and repair record:

* `review_delay.md`: every principal delay/size theorem verified; its
  superseding post-repair verdict is PASS. The one optional Dini-derivative
  clause now explicitly requires continuity along the trajectory and the
  upper-right derivative. The reviewer confirmed this exact repair.
* `review_positivity_terminal.md`: PASS for analytic positivity, full
  finite fitting-state differential classification, and the signed-axis
  terminal exponential asymptotic. Its scope clarification about nonfitting
  critical states was incorporated into `terminal_geometry.md`; its unit
  direction clarification was incorporated into `initialization_positivity.md`.
  The latter now also calls the diagnostic numerical evidence explicitly.
  These post-review wording changes do not alter a proof or inequality.
* `review_open_family.md`: PASS for the complete unconditional open-family
  theorem, including the exact coefficient, full-state continuation,
  actual endpoint rank, Hilbert regularity, entrance, trapping, and decay
  from time zero. No future-conditioning premise remains in that theorem.
* `review_cyclic_uniformity.md`: PASS for the uniform cyclic rate and
  bounded fitted endpoints over all cyclic directions, including the
  zero signed-first-moment endpoint and the stated scope distinctions.

The source proof files record the independent route freezes and later
authorized comparison within this study. Review hashes identify each
reviewed version. No source or result from another study was consulted.
The current checkpoint is complete for these stated theorems. The broader
terminal question for realizable arbitrary configurations remains open.
The subsequent continuation below proves a descending initialized positive
plateau that attains an architectural floor; it does not prove optimization
failure on realizable data.

The unresolved broad question is initialized optimization failure or
universal fitting for arbitrary compatible three-input configurations.
A slow family does not decide it, and failed counterexample attempts are
not positive theorems.

## Authorized continuation: weighted classification and descending plateaus

The user's next request continues this study's same two directions: classify
all asymptotic slow starts among weighted three-input laws, and construct or
exclude strict initial learning followed by a positive terminal loss. The
canonical scope and source boundary are unchanged. HEAD and the empty index
were rechecked; unrelated changes remain untouched.

The classification will distinguish vanishing initial slope, vanishing
progress on every fixed finite horizon, divergence of every fixed positive
loss-drop hitting time, and divergence of just one deeper threshold. These
are not identified without proofs. Actual laws have positive weights; zero
weights are allowed in their compactified limits.

Fresh independent routes developed `start_classification.md`,
`start_hitting_classification.md`, and `plateau_construction.md`, using only
their explicitly assigned established sources and the permitted completed
proofs in this study. Candidates are compared only after freeze. The lead
author owns the aggregate statement, architectural loss-floor analysis and
README. No numerical experiment is planned for this continuation.

The plateau investigation distinguishes contradictory coincident labels,
antipodal labels incompatible with oddness, and optimization failure on
data that the initialized hidden representation can fit. A negative example
in one category will not be presented as a theorem in another.

This continuation is now complete for the following precisely scoped
theorems, with fresh isolated internal reviews passing both routes:

* `start_classification.md`: explicit necessary-and-sufficient defect for
  vanishing initial slope, including arbitrary weights, inactive limiting
  slots and every geometry. Slow onset is equivalent to vanishing progress
  on each fixed finite horizon and divergence of every positive-drop
  hitting time. Balanced data simplify to weighted coalescence; equal
  thirds cannot have asymptotically vanishing initial progress.
* `start_hitting_classification.md`: independent full-flow classification,
  data continuity and a reciprocal-distance delay bound. Both onset
  reports distinguish delay to one selected threshold and give balanced
  independent-input families showing that its converse fails.
* `plateau_construction.md`: three distinct, exactly balanced sphere inputs
  with strict loss descent from 1 to 1/2, a bounded full-state endpoint,
  nonzero motion in both hidden blocks, and an exponential excess-loss
  tail. Same-label antipodes impose the attained architectural floor.
* `architectural_loss_floor.md`: exact attained architectural minimum for
  every weighted triple, using strict injectivity modulo sign of the
  canonical initialized coefficients and independence of their nonlinear
  features. There are no three-input expressivity obstructions beyond
  inconsistent labels at coincidences or antipodes. Initialization is
  stationary exactly when its loss 1 is already this architectural minimum.
* `WEIGHTED_THREE_INPUT_RESULTS.md`: authoritative combined statement,
  definitions, proof architecture, exact plateau and scope limitations.

Reviews:

* `review_weighted_start.md`: PASS for both complete onset candidates,
  their finite-time estimates, all boundary cases, and counterexamples.
  Its nonblocking clarification is incorporated in the synthesis: the
  explicit defect is a function of the listed three slots, not an intrinsic
  numerical metric after merging atoms. Its zero set and vanishing
  criterion are invariant. Frozen source hashes remain unchanged.
* `review_weighted_plateau.md`: PASS for the complete initialized plateau
  and architectural minimum, including clock continuation, physical
  factors, exact limit and tail, full hidden-block motion, initialized
  Gaussian sign certificate and feature independence. Frozen source
  hashes remain unchanged.

The complete review packets and hashes are recorded in those reports.
No numerical diagnostic was needed for this continuation. An initialized
positive plateau above the architectural minimum on compatible data is
still unresolved; these proofs do not hide that issue in a conditional
Gram or boundedness premise.

## Authorized continuation: necessity of the architectural plateau condition

The next user request asks for a necessary-and-sufficient condition on a
weighted three-input configuration for strict initialized descent followed
by positive limiting loss. This continues the same study's terminal
direction. The desired classification is in the data, not an oracle
condition involving an unknown limiting state or integrated future kernel.
The central open implication is whether every compatible triple has
L(t) tending to zero. The stronger statement that every law attains its
architectural minimum is investigated separately and is not assumed.

Fresh independent routes, with explicit source packets and no inherited
conversation, own `plateau_global_convergence.md`,
`plateau_finite_critical.md`, and `plateau_symmetry_counter.md`.
They investigate respectively global convergence, finite critical-state
geometry, and symmetry-based compatible failures. The lead author owns
comparison, synthesis and this README. Routes are compared only after
freeze. No numerical experiment is planned at this checkpoint. The
canonical initialized model, shared index and study boundary are unchanged.

This continuation reached the following internally checked results, not a
complete configuration-only plateau classification:

* `plateau_finite_critical.md`: for every compatible weighted triple,
  including dependent inputs, every finite positive-loss critical state
  with nonzero M is a strict saddle. The zero-M exception has either
  negative curvature or explicit cubic descent. Thus every finite local
  minimum fits. The proof uses Gaussian-tail lower separation and mixed
  lower/readout curvature. Every finite positive-loss initialized
  accumulation point is a strict saddle; no existence of such a point
  is assumed or asserted. Critical losses have a finite signed-partition
  list and a positive gap at least the smallest input mass.
* `plateau_global_convergence.md`: an independent strict-saddle proof for
  independent inputs using dual-vector lower perturbations and confluent
  Vandermonde separation. Also strict loss descent at every finite time
  for every nonstationary initialized law, and an explicit nonoptimal
  full-row-rank saddle. Its initial gap list was corrected: a finite
  initialized endpoint with M=0 is already excluded by loss below one.
* `plateau_ambient_counterexample.md`: an explicit same-mark, full-row-rank
  critical state with loss 8/9 for orthogonal inputs and mixed labels;
  its strictly negative second variation is computed. The canonical
  initialization on those same data fits, so this is not a reached
  counterexample. It rules out an ambient no-bad-critical-points route.
* `plateau_upper_escape.md`: without any full-state endpoint hypothesis,
  a bounded sequence of readout L2 and matrix norms forces the limiting
  loss into an explicit finite list determined by the weights. Outside
  that list their norm sum must tend to infinity. A positive plateau
  below the smallest mass therefore forces this upper-parameter escape.
* `plateau_symmetry_counter.md`: the inherited signed-coordinate symmetry
  sector always admits a fit on compatible data; transitive cases fit
  along the full scalar-clock flow. A weighted reflection candidate's
  necessary feature collapses were derived, but none is proved reached.
* `PLATEAU_CLASSIFICATION.md`: authoritative synthesis. The proved
  sufficient condition for a descending plateau is 0<L_odd<1. Necessity
  is equivalent to universal initialized fitting on compatible triples
  and remains open. A finite bad minimum is ruled out there; approach
  to a strict saddle or absence of finite accumulation remains unexcluded.

Internal checks are transparent within-study cross-audits after route
freeze, not fresh isolated promotion reviews. An attempted additional
fresh reviewer could not be created because the agent thread limit was
reached. The independent derivations and the lead author's complete
source/proof checks were retained. The finite-critical route also records
an earlier supervisor sketch of the ambient saddle, which it did not use.

* `review_plateau_finite_critical.md`: stronger saddle theorem and all
  dependencies pass. Post-review wording explicitly keeps the auxiliary
  nullspace criterion's independent-input hypothesis and restricts the
  accumulation statement to finite accumulation points. The reviewer
  verified both repairs and exact unchanged proof content by hash
  reconstruction.
* `review_plateau_global_ambient.md`: independent-input theorem, strict
  finite-time descent, both explicit saddles and same-data initialized
  fitting pass. Its M=0 scope correction was incorporated and rechecked.
* `review_plateau_upper_escape.md`: PASS for every constant, the bounded-
  sequence dissipation argument, collision limits, enumeration and escape
  quantifier. It separately records the symmetry route's self-audit. The
  lead author read and checked that route completely and fixed its sole
  display typo (missing backslash before quad) without mathematical edits.

All reviewed versions and post-repair hashes are in the reports. No
experiment was run, no new initialized compatible failure was found,
and neither missing necessity nor all-time boundedness is claimed proved.
The next decisive obligation is a canonical saddle-avoidance or escape
exclusion theorem, or an actual compatible initialized counterexample;
an ambient critical state or a future-kernel condition cannot substitute
for it. No promotion or shared-source change was performed.

## Authorized continuation: the three-rank-one cancellation proposal

The user's next proposal is to combine the rank-one structure of the three
middle-gradient terms with readout and first-layer stationarity, hoping to
derive the missing input-level necessity. This continues the same plateau
investigation. The physical model, prescribed initialized trajectory of
interest, and study boundary remain unchanged. No experiment is needed.

Fresh independent routes developed `rank_one_geometry.md` (prompt-only
linear algebra) and `rank_one_joint_stationarity.md` (exact canonical model
and selected earlier proofs from this study). The lead independently
developed `rank_one_nonlinear_obstruction.md`. The candidates were frozen
before their comparison. The lead owns this README and aggregate synthesis;
each route owns its separate flat report. A fresh isolated reviewer is
checking the frozen lead construction and its complete dependencies in
`review_rank_one_nonlinear_obstruction.md`.

The proved algebraic fact is exactly the user's nonzero-term assertion:
three nonzero rank-one matrices summing to zero share a left-factor line
or a right-factor line. Zero-factor cases require separate treatment.
For independent inputs, first-layer stationarity additionally gives
p_i r_i M^T d_i=0 separately. These constraints have a complete algebraic
classification and quantitative approximate versions in the algebra report.

The key new obstruction is stronger than the earlier zero-backward example.
For every independent input triple, every positive weighting and every
binary labeling, the lead construction gives an exact finite positive-loss
critical state with all three middle-gradient terms nonzero rank one.
All nonlinear population moments are realized by actual fields on the
unchanged canonical correlated marks. A convex Gaussian-expectation
argument realizes any sufficiently small triple of lower moments.
The backward vectors are nonzero but annihilated by M^T. With balanced
weights (1/4,1/4,1/2) and labels (+,+,-), this stationary state's loss is
3/4. The independent nonlinear route constructs the same mechanism with
rank-two M for orthogonal inputs.

These are ambient stationary states, not initialized trajectories. They
disprove the proposed inference from joint stationarity to architectural
input conflicts, while leaving universal initialized fitting unresolved.
A separate full-row-rank branch has zero backward response and the same
positive loss. Merely keeping M full row rank therefore cannot complete
the missing exclusion. No promotion is part of this work.

The lead read both complete independent route reports and checked their
linear algebra, nonlinear realization and all physical gradients. The
nonlinear route's display-only repairs are recorded in that report.
`review_rank_one_nonlinear_obstruction.md` is a fresh isolated PASS for the
complete frozen lead proof, SHA256
`07b481e396584ebbcfb30b155b157778179a6c11c929a85376e94e31d072784c`.
It also independently constructs an exact fit and a negative-curvature
direction, and checks the ancillary initialized-feature fitting chain.
The lead read that review completely. This is internal checking, not
promotion or initialized saddle avoidance.

A bounded algebra follow-up after the independent freezes supplies
`rank_one_algebra_extensions.md`. The lead integrates it with the exact
moment/readout construction in `rank_one_nonlinear_extensions.md`:
the nonzero-term obstruction can have rank-two M and rank-two lower
coefficient matrix, so its lower vectors need not all align; on the
zero-backward branch, both matrices can have full rank simultaneously.
The extra upper readout component may also be a bounded tanh feature.
The integration passed an explicitly separate follow-up check in the
same isolated review report, at SHA256
`e9c9c12a47f3a053e69216573b3d83165e393f300e510f5b6a480d722d2dc71c`.
The lead read the complete addendum and independently checked both rank
calculations and their exact nonlinear realization. The algebraic source
hash is `df35ce798e5488af31127192e338e786aca10192204d6ded2113b834aa0f1ee5`.
These refinements change none of the initialized reachability limitations.

This checkpoint is complete for the checked stationary-state obstruction.
The necessary direction of the initialized configuration-only plateau
classification remains unresolved: neither approach to a compatible saddle
nor positive-loss escape has been excluded or exhibited. Any subsequent
proof must establish a property of the prescribed trajectory, not assume
the absence of the exact critical states constructed here. No numerical
campaign, shared-source edit, stage, commit, or promotion was performed.

## Authorized continuation: basins of positive-loss stationary states

The next user request directly continues the unresolved dynamical plateau
question: reconstruct the states approaching compatible positive-loss
equilibria, prove thinness or measure-zero basins where justified, and
determine whether this excludes canonical initialized failure. This is
the same study and model. A theorem for a separately randomized initial
field will be distinguished from the deterministic population initialization
(w,c,M)=(g,0,D). Positive limiting loss without a finite endpoint remains
a separate alternative; a stable-manifold theorem cannot silently remove it.

The current theory-only search has three independent scoped routes:
`basin_spectral_route.md` checks exact derivative/spectral structure and
local trapping graphs; `basin_escape_route.md` investigates global bounds
and reached-state constraints; `basin_probability_route.md` develops the
globalization/probability claim from an explicitly supplied Banach-flow
setup. Their input packets and write ownership are in their assignments.
They freeze before comparison. The lead independently develops an exact
separable continuous-carrier realization, integrates the proofs, and owns
this README and the basin synthesis. There is no numerical campaign.

The proof contract keeps fixed the correlated canonical marks, full p=1
matrix/transpose, all trained blocks, physical time, and unhalved loss.
No finite-particle approximation, changed initialization, unproved
all-time compactness, or undefined infinite-dimensional Lebesgue measure
may replace the requested population claim. Scope distinctions will include
one equilibrium, all finite limiting equilibria, approach to an equilibrium
set without point convergence, and the entire positive-limit-loss basin.

The basin continuation reached the following checked results.

For every independent triple, arbitrary positive weights and binary labels,
all initial states with a physical-Hilbert endpoint of loss in (0,1)
lie in a countable union of Lipschitz hypersurfaces. This basin is meagre
and shy; an explicit full-support Gaussian randomization of the population
fields/matrix assigns it probability zero. The randomization can consist
of bounded fields almost surely. No boundedness or continuity of the
endpoint is assumed. This is a theorem about the full point-convergence
basin, not an assertion that every trajectory has a point limit.

Complete retained proofs:

* [basin_continuous_carrier.md](basin_continuous_carrier.md): exact
  separable compact-carrier realization containing canonical trajectories
  and constructed stationary states, with no Gaussian truncation; smooth
  flow and a critical Hessian of rank at most 48.
* [basin_spectral_route.md](basin_spectral_route.md): exact global physical
  Hilbert flow, small Lipschitz remainder at independent-input critical
  states, and a contained trapping-graph proof. It gives a countable
  backward cover and actual strong stable trajectories with strictly
  descending positive limiting loss from noncanonical starts.
* [basin_hilbert_landscape.md](basin_hilbert_landscape.md): dual-input
  variations extend strict-saddle geometry to every Hilbert equilibrium
  with 0<L<1, removing boundedness of the limiting fields.
* [basin_probability_route.md](basin_probability_route.md), Sections 1--5:
  hypersurface and explicit random-series probability arguments. Its
  optional activation-zero Section 6 is not used.
* [basin_hilbert_null_extension.md](basin_hilbert_null_extension.md):
  exact strong Gateaux time-map regularity and a one-transverse-direction
  pullback lemma. This closes the Hilbert probability proof without
  assuming false Frechet smoothness of the lower L2 gate.
* [basin_open_fitting.md](basin_open_fitting.md) and
  [basin_hilbert_fitting.md](basin_hilbert_fitting.md): explicit nonempty
  open fitting basins in both continuous-carrier and physical Hilbert
  topologies for every independent triple. Forward invariance, exponential
  loss decay, finite state length and fitted endpoints are proved.
* [basin_escape_route.md](basin_escape_route.md): global o(sqrt(t))
  physical displacement, time-average prediction identities, and a bounded
  noncompact stationary readout family. These do not prove compactness
  of a trained orbit.
* [BASIN_RESULTS.md](BASIN_RESULTS.md): integrated theorem, backward
  basin cover, probabilistic interpretation and unresolved implications.

[review_basin_framework.md](review_basin_framework.md) is a fresh isolated
internal review of the complete supplied chain and synthesis. All
component and integration checks passed, including the later Hilbert
landscape, strong Gateaux pullback, and Hilbert fitting extensions.
Exact hashes, packet additions, read coverage and unused source sections
are recorded there. The lead read the complete candidates and review,
and independently checked their derivations. The open-fitting report's
only repair renamed deterministic mark bounds to distinguish them from
random coordinates. The Hilbert-null report also received a single
display-only convergence-arrow repair after review; its record preserves
the original hash. No proof changed. No experiment was needed.

The entire positive-limit-loss basin is not proved null: escape or
nonconvergence remains unexcluded. Canonical population initialization
is deterministic, so nullity does not decide its membership. No universal
initialized fitting, configuration-only plateau iff, or dependent-input
basin thinness is claimed. These are the decisive remaining obligations,
not hidden hypotheses of the proved basin theorem. No shared-source edit,
stage, commit, or promotion was performed.

## Authorized continuation: dependent-input basin extension

The user asks to remove linear independence from the basin theorem,
particularly for three nonaligned circle inputs, and to assess extension
to larger finite or continuous training laws. This continues the same
basin investigation. The first target retains the exact physical Hilbert
topology and the specified randomization; a bounded-endpoint or stronger-
topology result must be labelled separately. Canonical initialized fitting
and convergence without an endpoint remain separate obligations.

Fresh scoped routes own `dependent_hilbert_geometry.md` and
`dependent_basin_functional.md`, respectively testing the equilibrium
geometry and the local/global trapping argument. They start without the
prior conversation and use explicitly assigned own-study proofs and
established sources. The lead owns synthesis, finite-sample extensions
and this README. No numerical experiment, shared-source edit, staging,
commit or promotion is planned. The shared HEAD and empty index were
rechecked; unrelated changes are preserved.

The lead has read and checked all three complete new candidates. A fresh
isolated review of their complete main proof chain and integration passed
in [review_dependent_extension.md](review_dependent_extension.md). Their
proofs establish the following extensions.

* [dependent_hilbert_geometry.md](dependent_hilbert_geometry.md): three
  projective circle directions determine the lower derivative-gate ratios
  up to sign. This proves negative bounded directional curvature at every
  nonaligned triple Hilbert equilibrium with loss in (0,1), and individual
  critical coefficient cancellation outside an explicit reflected-pair,
  oriented-label-conflict, unequal-mass case. Equal masses eliminate that
  exception for every geometry. The report also constructs an exact
  exceptional equilibrium without a second Frechet differential, so the
  stronger unrestricted smoothness premise is actually false.
* [dependent_basin_functional.md](dependent_basin_functional.md): an
  independent sign-rigidity/Gaussian-tail proof establishes cancellation
  and the entire Hilbert null-basin theorem for all nonaligned triples
  whose limiting lower displacement is bounded. Endpoint readouts may
  be L2. A separate finite-sample theorem allows any fixed dimension and
  at most one independent input relation; all graph, flow-regularity,
  countability and probability obligations are included.
* [dependent_finite_fitting.md](dependent_finite_fitting.md): initialized
  nonlinear features distinguish all finite distinct unoriented inputs,
  without a sample-count-versus-dimension restriction. Their Gram gives
  an explicit fit, the exact attained architectural floor, and a nonempty
  H-open full-flow fitting region with explicit exponential loss decay,
  finite state length and a fitted endpoint.
* [DEPENDENT_BASIN_RESULTS.md](DEPENDENT_BASIN_RESULTS.md): integrates the
  full-H equal-weight and generic-weight basin theorem. For every weighted
  triple, any remaining nonregular convergent endpoint has a specified
  reflected-pair loss. A known initial sublevel below all such values
  restores the fitting-on-convergence probability conclusion; balanced
  binary triples have the sufficient common sublevel L<1/2. This is not
  a claim that canonical initialization enters that sublevel.

The independent routes were developed without reading each other, with
the lead's exploratory followups explicitly disclosed in their reports.
Their hashes and the exact review packet are retained in the fresh review.
The lead additionally checked scalar factors, exceptional weight/label
cases, the ellipse convexity inequality, concentrated L2 perturbations,
and every readout-Gram/trapping estimate. Display delimiters and control
characters were checked in all four new proof files. No numerical
experiment was needed.

The final reviewed synthesis SHA256 is
`880a9dd5675060ad6c7b9fe97e485ed28c44f1e606af68a6b13fc86a16529117`.
The review records every component hash, complete read coverage, elementary
reconstructions and edge-case checks. The lead read the complete report.
Its single excluded secondary assertion is the functional route's optional
continuous-carrier topology extension, whose full construction was outside
this review packet; it is not used by the physical-Hilbert results reported
here. The final synthesis includes an explicitly checked clarification that
state convergence implies equilibrium by continuity of the vector field.
These are internally checked study results, not promoted book material.

The unqualified full-H basin theorem for unequal-weight reflected
exceptions remains open, as does its unrestricted many-sample analogue.
The explicit exceptional stationary states show failure of a Hessian
premise, not a positive-probability failure basin or canonical failure.
Infinite-support training laws require additional estimates and are not
obtained by a sample-count limit. Canonical-point membership and absence
of nonconvergent positive-loss behavior remain separate open obligations.
This continuation is complete for the stated extensions. No shared-source
edit, stage, commit or promotion was performed; unrelated work is untouched.

## Authorized continuation: arbitrary finite input basin theorem

The user asks whether the equal-weight three-input exceptional-basin theorem
extends to any finite number of normalized inputs in R^d, assuming only that
no two inputs coincide or are antipodal. This directly continues the same
basin investigation. The target retains physical Hilbert point convergence,
the same fixed canonical joint marks and odd sector, and the same explicit
full-support randomization of population fields. Full-state convergence and
canonical deterministic initialization are separate issues.

The theory-only round assigned independent fresh scoped attempts to
`finite_basin_geometry.md` and `finite_basin_tail.md`. Their initial inputs
are the established general-d p=1 chapter and explicitly assigned existing
proofs within this study. Each freezes before comparison. The lead checks
the exact equations, integrates results, and owns this README; a fresh
isolated review will check any new substantive construction. No numerical
experiment or established-source change is planned. HEAD remains
019e3630237e33f58b9636c0aa67a039bebf0182, the index is empty, and unrelated
changes are preserved.

The continuation is complete for these internally checked results:

* [finite_basin_geometry.md](finite_basin_geometry.md): seven distinct,
  non-antipodal, equally weighted inputs in R^3 admit an exact equilibrium
  of loss 48/49 with nonnegative second directional variation in every H
  direction. One readout gives nonzero individual critical coefficients,
  concentrated descent and no second Frechet differential. A post-freeze
  readout change instead gives an actual rank-one positive-semidefinite
  Hilbert Hessian. A complete strong-stable contraction then constructs
  special nonconstant trajectories decreasing to 48/49 from loss below one.
* [finite_basin_tail.md](finite_basin_tail.md): independently reconstructs
  the seven-input moment-matching obstruction and gives bounded cubic
  descent. Its post-comparison three-moment readout verifies cubic descent
  together with the actual positive-semidefinite Hessian. Separate null-basin
  extensions cover multiple direct-sum relation blocks with bounded limiting
  lower displacement, and arbitrary finite dependence under explicit
  full-support and conditional-mark endpoint hypotheses.
* [finite_critical_loss_gap.md](finite_critical_loss_gap.md): for any finite
  input list, every stationary loss is zero or at least the smallest sample
  mass. A finite signed-partition formula contains every critical value.
  Initial loss below that mass and physical state convergence imply exact
  fitting deterministically; for equal weights the threshold is 1/m.
* [FINITE_BASIN_EXTENSION.md](FINITE_BASIN_EXTENSION.md): integrates the
  obstruction, special trajectories, restricted positive results and exact
  unresolved unrestricted basin question.

The two initial routes were developed independently and frozen before their
comparison; the reports preserve the comparison boundary and attribute the
lead's readout and strong-stable suggestions. The lead read all complete
new reports and reconstructed the canonical gradients, every mixed second
variation, cubic coefficients, Frechet remainder, affine-chart contraction,
restricted basin arguments and the finite critical-loss formula. Display
delimiters and control characters were checked in the four new proof files.

A fresh isolated complete review passed in
[review_finite_basin_extension.md](review_finite_basin_extension.md), SHA256
`3e36f2e68346ab207b4a2df4009b8d12881319330dcd536a986612fabf68a757`.
It records exact hashes and full read coverage of the nine-file scientific
packet, checks all new and needed background proofs, and reports no required
repair or remaining missing dependency. The lead read that report in full.
The final synthesis SHA256 is
`3335dfcc23064a1deb02b46de6b347ec52e2b77b7968f63e3693492b16fca99f`.
Its only change during review was a recorded metadata sentence redirecting
status to this README; the reviewer reconstructed the previous hash.

The universal arbitrary-finite-input null-basin conclusion remains open.
The counterexample refutes the strict-saddle proof premise, not the basin
theorem itself. Cubic descent and a special stable curve do not establish
positive basin probability. The constructed endpoints have unbounded w-g
in L2 and do not refute bounded-displacement endpoint theorems. The missing
step is nonlinear control of degenerate center directions, or a genuine
positive-probability bad-basin construction. Canonical initialization,
all-time state convergence and positive-loss escape remain separate gaps.
No experiment, established-source edit, staging, commit or promotion was
performed; the empty shared index and unrelated changes were preserved.

## Authorized continuation: input conditions beyond pairwise nonalignment

The user next requested data restrictions weaker than input independence
that exclude the finite-input counterexample and restore the three-input
bad-basin argument. This is the same dynamical-basin investigation, with
the exact canonical p=1 model and physical Hilbert topology unchanged.
The current round is theory only. Two fresh independent scoped routes own
`input_condition_geometry.md` and `input_condition_regularity.md`; the lead
owns synthesis and this README. They use only assigned established material
and this study's complete proofs and freeze before comparison.

This round is complete for the following internally checked results:

* [INPUT_CONDITION_RESULTS.md](INPUT_CONDITION_RESULTS.md): complete
  synthesis and lead's universal sublevel theorem. The four-input
  equal-weight condition is rank three, every triple independent, and
  two positive/two negative entries in the unique relation after labeling.
  It recovers the full physical-H bad point-basin theorem below loss one
  on an open dependent family. Larger full circuits have explicit signed
  thresholds. Any n pairwise nonparallel equal-weight inputs have the same
  basin conclusion below loss 8/(3n); if every r inputs are independent,
  the threshold is 4r/[n(r+1)]. Strict labeled separation improves it to
  (5-4/r)/n, and separately supplies negative bounded directional curvature
  at every positive-loss endpoint below one for any finite sample count.
* [input_condition_geometry.md](input_condition_geometry.md): independent
  four-input proof, data-only signed-partition gate-rank certificate,
  finite linear-feasibility relaxation, and proved size limitation of
  that relaxation. Its first-candidate SHA256 is
  `7a4035acb28d23f38b07fff18f161c160bafb319ccc3440a12f22d1b19e0473d`.
* [input_condition_regularity.md](input_condition_regularity.md): independent
  four-input proof and an exact loss-3/4 equilibrium whose input second-
  moment matrices are independent but whose critical coefficients do not
  cancel and whose loss lacks a second Frechet differential in H. The
  lead's post-comparison arcosh construction is verified and strengthened
  to show that the exact nonlinear gate-rank certificate also fails for
  every dependent equal-weight family with n>=5. The lead's circuit
  thresholds and universal sublevel theorem receive complete informed
  checks. Initial Sections 1--7 were frozen before comparison; the file
  explicitly records that boundary and subsequent supplied ideas.

The lead read both full reports and their final addenda, reconstructed the
stationary partition formulas, sign rigidity, four-input cancellation,
negative mixed variation, actual Hilbert remainder and basin transfer,
four-input needle-perturbation obstruction, exact linked-gate arcosh
construction, and all group-cost threshold inequalities. The second
route read and checked the full synthesis and both final additions without
finding an error, recording exact version coverage in its Section 10.
This is an informed check, not a fresh isolated review; an attempted new
review context was unavailable because the agent tool reported its thread
limit. Internal checking does not require or substitute for promotion review.

Final synthesis SHA256:
`fa6670f4c8bbcd658d295e66db4517ebfdd42f7fabebdfaa86e5e7296b7a445b`.
Final regularity/report/check SHA256:
`94d65944520bb10d62953acea9960be7f68897f7af2b684eea9d0ebb87082871`.
The canonical chapter, functional basin proof and critical-loss-gap
source hashes were rechecked unchanged. Control-byte and display-delimiter
checks passed on the new reports. No numerical experiment was run.

The four-input family is open and nonempty, not dense for fixed labels.
No almost-everywhere geometric restriction restoring the whole (0,1)
basin result for arbitrary sample count has been proved. Failure of the
rank certificate or of Hilbert regularity is not a positive-probability
bad-basin example. All nullity results still require a physical state
limit and concern the specified population-field randomization. Canonical
initialized fitting, sublevel entry and positive-loss escape remain open.
The next mathematical bottleneck is stronger use of joint lower/upper
stationarity, or a trapping argument at nonregular/degenerate endpoints;
it is not merely independence of the pointwise residual vectors.
No established-source edit, staging, commit or promotion was performed;
HEAD, the empty index and unrelated changes were preserved.

## Authorized quick wide-network numerical follow-up

The user explicitly requested a quick wide actual-network GF simulation
of the same seven-input configuration from canonical initialization.
The scope was frozen before implementation in
[wide_network_gf_plan.md](wide_network_gf_plan.md), with numerical wall
cap240 seconds, two BLAS threads, main width1024 seed20260918, same-seed
tenfold tighter replay, and one conditional second seed20260919. This is
a finite-network validation follow-up within the same configuration
investigation, explicitly separated from fixed-p=1 population claims.
No other study's findings were used. The lead owns the plan, implementation,
report, outputs and this README. A fresh scoped read-only agent checked
the finite scaling and then the frozen implementation; it ran no experiment.

[wide_network_gf.py](wide_network_gf.py) uses canonical maintained
initialization, exact full dense GF equations, and a float64 embedded
RK3(2) integrator. All three planned runs completed; the optional seed
branch was triggered only after the reserved replay passed. The detailed
results, validation, reproduction command, source/output hashes and exact
limitations are in [WIDE_NETWORK_GF_RESULTS.md](WIDE_NETWORK_GF_RESULTS.md).
Raw data and final arrays are under
`data/generated/p1_sphere_extremes_20260918/wide_network_gf_20260918_01/`.
The main and second seed losses were9.4819222e-7 and9.3050268e-7 at times
59.46868 and61.51813. Main/replay maximum common-time prediction difference
was4.4053e-5 and final loss difference7.2597e-10. All seven labels fitted,
all saved accepted losses decreased, and both hidden populations moved.

The lead and scoped checker reconstructed the RHS and numerical stages;
the executed small-state gradient/energy/kernel checks and wide endpoint
reference checks passed. A separate read of saved trajectories verified
their reported losses, time ordering, finiteness and final label signs.
The second seed has no separate tolerance replay, as predeclared. No new
angle, width or seed search followed. This is not a promotion review or
a mathematical convergence certificate. The code and scientific plan
were unchanged during execution. HEAD and the empty index were preserved;
no established-source edit, staging, commit or promotion was performed.

## Authorized continuation: perturbing the seven-input flat equilibrium

The user proposes input noise on the sphere as a way to expose whether
the artificial flat positive-loss equilibrium is structurally exceptional.
This directly continues this study's input-geometry and bad-basin question.
The full canonical p=1 population model, correlated marks, physical
Hilbert metric, and all trainable matrix entries remain the target.
Frozen-state nonstationarity, nearby full-state instability, remote
equilibrium existence, and actual bad-basin probability are kept separate.
No numerical experiment is part of this theory round.

Two fresh independent agents, without inherited discussion, were assigned
the complete canonical chapter and selected complete proofs within this
study. They own `input_perturb_frozen.md` and `input_perturb_persist.md`.
The first froze its initial candidate before receiving the lead's separate
full-Hilbert local argument; its explicitly informed Section 10 then
verified that argument. The second route has not received either argument
before its freeze. The lead owns integration and this README. A fresh
isolated reviewer owns `review_input_perturb.md`, with only a neutral
assignment and a complete frozen scientific packet. No other study is an
input and no established source, index entry or Git history is changed.

The local theorem permits arbitrary L2
population and matrix adjustments near the reference equilibrium, rather
than only continuation in its construction ansatz. Readout stationarity
forces all seven effective vectors to coincide; flatness would force
the lower field to be supported on critical points of the known residual
function `sum_i rho_i tanh(s dot u_i)`. A transverse cubic-harmonic
expansion and a generic axial input drift remove those critical points
near the old two-point support. L2 closeness and lower stationarity then
give individual coefficient cancellation and an actual negative Hessian
eigenvalue. The amplitude conditions and direction-then-radius probability
quantifier are explicit in Section 10.

The completed continuation is integrated in
[INPUT_PERTURBATION_RESULTS.md](INPUT_PERTURBATION_RESULTS.md). Its proofs
and provenance are:

* [input_perturb_frozen.md](input_perturb_frozen.md): independent frozen
  stationarity and ansatz classifications, followed by the explicitly
  informed verification of the lead's full-Hilbert local theorem.
* [input_perturb_persist.md](input_perturb_persist.md): independent exact
  construction of seven nondegenerate residual critical points, invertible
  feature evaluations, canonical correlated-carrier interpolation and a
  rank-one PSD Hilbert Hessian at loss 48/49, valid on open sets of fully
  free input perturbations arbitrarily near the original data.
* [input_perturb_bounded_continuation.md](input_perturb_bounded_continuation.md):
  informed post-freeze verification of the lead's bounded continuation,
  open family of fixed perturbation directions, and direct exact fitting
  corollary. The seed states converge to a different bounded original
  equilibrium whose lower support uses the two exceptional axial amplitudes.
  Uniform bounds are not asserted over the whole direction family.
* [input_perturb_cubic.md](input_perturb_cubic.md): lead's explicit bounded
  cubic descent direction at every new finite-perturbation equilibrium,
  using the spare canonical Gaussian coordinate to cancel all first lower
  moment variations. The new states are not local minima.
* [input_perturb_crosscheck.md](input_perturb_crosscheck.md): separate
  informed complete analytical check of the independent persistence
  construction, after both initial candidates had been frozen.
* [review_input_perturb.md](review_input_perturb.md): fresh isolated
  complete review of the full local proof and its dependencies, followed
  by separately frozen supplemental reviews of the persistence proof,
  cubic corollary, bounded/directional/fitting addendum and final synthesis.

The lead read all complete reports and checked the canonical gradients,
population correlations, mixed Hessian terms, uniform residual expansions,
both critical-point blowups, all seven nondegeneracy conditions, both
feature determinant blocks, bounded interpolation on the actual target,
analytic directionwise continuation, and the cubic derivative. Both the
fresh reviewer and informed checker independently reconstructed the
decisive determinant coefficients. Every component passed for its stated
scope; these are internal checks, not promotion.

The fresh final review is 798 lines, SHA256
`e05ce336d4b5bfc9ee7a15763dc18f9d6546ab6106d4d140cc1712c47a1af936`;
it records complete read coverage of all 4486 scientific lines in its
final packet. The final synthesis SHA256 is
`6fd0ce34f10647dbf50ccf7fb8bbf35136fbfac360251efb612221c71ffb88eb`.
Two reference-state scope clarifications and an explicit positive-noise-
amplitude qualification for cubic descent were incorporated and rechecked.
After the review finished, the sole persistence-source change converted
the accidental comma in equation (30) into a LaTeX multiplication space.
Reversing that exact text replacement reconstructs its reviewed hash
`641204a025374966da3114bd153f10956d0d9d704d4e6420cd9659ea6cd30dae`;
the repaired source hash is
`790c5fafc28e07a9fcafa78bf555c75aab605dee1581c83e456f24a2cc26d9cd`.
No argument changed. The bounded/directional addendum and cubic proof
retain their reviewed hashes, respectively
`5450edff98391be754d75117c96cf039348dad6d7a5ea97710b9dc80f3a7ebda`
and `b050e2045487ebc1d5c1784ff6fa2cee7f348ba3207284f9bcb5a58805349020`.
The lead read the complete final review and cross-check. Control-byte and
display-delimiter checks passed on all new proof and synthesis files.

The global proposed strict-saddle premise is disproved, including its
almost-every-fixed-noise-direction interpretation: there is an open
family of directions with surviving PSD bad equilibria at all sufficiently
small positive amplitudes. The local theorem around the earlier fixed
single-amplitude state remains valid. Cubic descent rules out local
minimality and attraction of a whole neighborhood to one such point, but
does not prove or disprove a positive-measure proper basin. Canonical
initialized reachability, basin nullity at these degenerate endpoints,
and absence of positive loss without a state limit remain uncontrolled.
No numerical experiment, established-source change, staging, commit or
promotion was performed in this continuation. The shared HEAD and empty
index, and all unrelated changes, were preserved.

## Authorized continuation: breaking a given bad connection with input noise

The user clarified the target: **assume** canonical convergence to a bad
state at special data, and test whether generic arbitrarily small input
noise breaks that entire connection. Establishing which endpoints are
canonically reached is not the task. This continues the same input-noise
investigation, with all physical p=1 conventions unchanged. The previous
existence of remote PSD equilibria neither proves nor refutes the new
connection-fragility claim. No experiment is part of this continuation.

Fresh scoped agents started without inherited discussion. The independent
data-section route owns `input_basin_transverse.md`; the other route owns
`canonical_bad_reach.md` and was redirected from reachability to the given
connection when the user clarified. Only explicitly assigned complete
book and own-study sources were inputs. Their candidates were frozen
before cross-comparison. The lead independently derived
`input_connection_response.md` and then the elementary logical test
`input_connection_response_example.md`. The first agent's later check
of the lead theorem is explicitly informed and preserves its original
independent prefix. A fresh isolated reviewer owns
`review_connection_response.md`; its scientific packet contains the
complete canonical chapter and the complete lead/transport/example
candidates, without author history or earlier verdicts.

The current synthesis is
[INPUT_CONNECTION_RESULTS.md](INPUT_CONNECTION_RESULTS.md).
Under assumed strong canonical convergence to the original
single-amplitude loss-48/49 equilibrium, almost every tangent input
direction has an unbounded first-order trajectory response as time runs
over [0,infinity). The derivative exists at every finite time. The
proof retains the actual complete closure and uses a nonzero limiting
input force in a readout direction neutral for the endpoint Hessian.
This excludes a uniform all-time O(epsilon) perturbation bound. It has
no positive-amplitude exclusions and includes the two old exceptional
amplitudes, but concerns this specified endpoint class only.

This is not yet finite-noise escape. A separate exact analytic square-loss
example has unbounded first response, PSD bad equilibria, cubic descent
and exact zero-loss fits, but every small parameter perturbation still
converges badly at distance O(|epsilon|^(1/3)). It is explicitly not
p=1. The independent route also supplies a precise data-section
transversality theorem and exact p=1 sensitivity/joint trapping-graph
derivations, without claiming the missing transverse derivative has
been verified for canonical training.

The transport route shows that a bounded actual lower-field endpoint
with zero backward vectors cannot have integrable physical-state error
along a canonically initialized convergent trajectory; exponential
physical-state convergence is therefore impossible for these endpoints.
After a fixed sufficiently late entrance time, the first
perturbation-induced exit from a fixed endpoint ball has a logarithmically
diverging time lower bound as input noise tends to zero.
Neither statement proves generic escape. A secondary reflection check
on a particular seed carrier realization is not used in the main result.

Proof and evidence files:

* [input_connection_response.md](input_connection_response.md): complete
  lead proof of the generic unbounded first input response, including
  physical Hilbert differentiation and a zero-loss sanity check.
* [input_connection_response_example.md](input_connection_response_example.md):
  explicit nonlinear adjustment example separating derivative growth
  from escape, with full exact trajectories and curvature checks.
* [input_basin_transverse.md](input_basin_transverse.md): independent
  connection-transversality route, moving-basin terms, and separate
  rotating strict-saddle example; Section 9 is its informed check of
  the lead result. Independent Sections 1--8 preserve the exact original
  SHA256 `5660303f944fb0f637a3e2d3d5ca1f034e351252f32f711d536ed0c49a160ae6`.
* [canonical_bad_reach.md](canonical_bad_reach.md): assumed-connection
  transport, convergence-rate obstruction, exit-delay estimates, and
  explicitly secondary symmetry check.
* [review_connection_response.md](review_connection_response.md): fresh
  isolated check of the complete new response/transport/example packet;
  PASS for these results and the integrated synthesis, with the scope
  limitations recorded below.

The fresh isolated reviewer read all 1399 lines of its final scientific
packet, including the complete canonical chapter, revised response proof,
logical example, companion with its rate addendum, and final synthesis.
It verified the response's actual physical Hessian, finite-time input
derivative, operator-norm convergence, neutral forcing and genericity;
the companion's transport, nonintegrable-state-error corollary and
delayed-exit estimate; and every assertion of the elementary example.
The report's SHA256 is
`06203298beba2b18075bbe97e035bb21811241b927cdcc00b0aad233a46b43b6`.
The final response proof hash is
`39a3f5a854c34484132a3dde17f8be2c062c73c8a136fc2f5adbc82ac2096437`,
and the synthesis hash is
`3632c5c0b74c66d3cbe4f034123e22f43510f1e58bfa2c5101cd5d7b23a86982`.
The lead read the complete review and both complete route reports.
The separate informed check confirmed the main response theorem; its
sole requested regularity clarification was incorporated before final
independent review. The reviewer did not independently certify the
separate 960-line transversality route or the secondary reflection
continuation's branch-existence/scaling inputs; neither is needed for
the main new response theorem. Control-byte and display-delimiter checks
passed. These are internal checks, not promotion.

The generic p=1 escape conclusion, exclusion of nonlinear adjustment to
moving bad endpoints, and avoidance of all later bad convergence remain
open. No other study, maintained source/code, Git index, or shared history
was changed; no promotion was attempted.

## Earlier initialization-coefficient diagnostic and its limits

`initialization_diagnostic_plan.md` was frozen before its one execution.
The purpose was to test a simpler sign argument for one initialized
coefficient, not to test any trajectory or asymptotic rate. All three
precommitted Gauss--Hermite orders (64,128,256) completed in 0.06 seconds
under the 60-second cap, on Python 3.10.12 and NumPy 1.26.4. The validity
gate passed. The simpler coefficient A was about -0.00660666, whereas
the total diagonal coefficient was about 0.58518715. This numerical
evidence rejects that proposed shortcut; it is not a sign certificate.
The subsequent analytic proof controls the full conditional coefficient
and has no dependence on these approximations.

Reproduction command:

`timeout 60s env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python studies/p1_sphere_extremes_20260918/initialization_diagnostic.py`

Source SHA256:
`1e2962e224e309095551f75e591a70eca97b80f85ce5723bb46266b3eeb47e3f`.
Output `data/generated/p1_sphere_extremes_20260918/initialization_diagnostic.json`
SHA256:
`a1d8ab0f1af09e92e0e218023f55f0d5ff6d0a52af1c3a183ae54346675da49f`.
At that earlier analytical checkpoint no additional numerical experiment
was run. The later authorized wide-network diagnostic is recorded above.
No asymptotic theorem is based on numerical monotonicity.
