# Unique predictor selection in fixed-order population closure

2026-09-19. Study of uniqueness of the fitted predictor across optimization
noise realizations. Previous optimizer studies and their unpromoted findings
are not scientific inputs. The proofs below are derived from the established
book and independent attempts within this study. They are research results,
not promoted established material.

## Current result

Resumed by explicit user direction, 2026-09-20:
[RESUMPTION_20260920.md](RESUMPTION_20260920.md) recovers the precise
projected-selector theorem, all sufficient parameter bounds, its selected
function, and the three proof roles of the large coefficient rho. Current
proof/dependency and review hashes match the recorded final versions.
The hidden/readout loss learning-rate ratio is 1/rho; readout/hidden is rho.
The recovery uses theta for parameter coordinates and preserves reviewed proof
files. This is state recovery, not a new result or promotion. Relaxing the
mobility restriction remains open; no experiment or older GF limiting-rate
campaign was launched. The lead owns the recovery note and this checkpoint.

Task pause, 2026-09-20: the user requested a cross-account/task handoff to conserve
tokens. [HANDOFF.md](HANDOFF.md) records the research vision, exact continuation
point, source/code map, restrictions and resume message. The complete prior
39-result accounting is preserved in
[RESULTS_INVENTORY_HANDOFF_20260920.md](RESULTS_INVENTORY_HANDOFF_20260920.md).
That cross-study inventory is historical navigation, not a scientific dependency
or a waiver of study boundaries. No new proof, experiment, promotion or Git
transaction was performed for the pause. The completed theorem below is unchanged.

Continuation, 2026-09-19: the user requests simplification of the same
selected-optimizer theorem, retaining every compatible finite dataset,
exponential loss convergence and a noise-independent limiting function.
This continues the study's optimizer/uniqueness investigation. The strongest
new construction is ordinary loss descent with fixed layer learning rates,
plus projected quadratic selection and projected noise. The earlier exact
readout-transport construction remains valid; it is not used as an assumption
about any previous optimization trajectory.

## Simpler optimizer: full-Jacobian projected selection

[PROJECTED_SELECTOR_LEAD.md](PROJECTED_SELECTOR_LEAD.md) contains the new
complete proof. It retains the canonical population representation,
initialization, correlations and unhalved loss, but changes relative layer
learning rates. In the fixed coordinates z=(sqrt(rho)(h-h0),c), write e for
weighted training residual and T_z for the full prediction Jacobian. Let

\[
 P_z=I-T_z^*(T_zT_z^*)^{-1}T_z.
\]

The rule is

\[
 \dot z=-\nabla_z L-\epsilon P_z z+\eta\sqrt L\,P_z U_t,
 \qquad \|U_t\|\le1.
\]

The first term is the ordinary unhalved loss gradient in these coordinates.
The added drift is the quadratic state preference projected onto directions
that leave all current training predictions unchanged to first order. The
noise is projected onto the same directions and vanishes with sqrt(L).
Unlike the earlier update, this rule evaluates no grad J, no current fitting
readout and no derivatives of an inverse or projector. It requires a current
full-Jacobian Gram inverse; that computational operation remains substantive.

For sigma=lambda_min K_h0>0, the proof gives explicit rho, epsilon=sigma/8,
and 0<eta<=sqrt(epsilon/4), all fixed before training, such that

\[
 L(t)\le L(0)e^{-2\sigma t},\qquad
 \|z(t)-z_*\|\le\|z_*\|e^{-\epsilon t/2}.
\]

The target z_* is the unique nearby minimum of ||z||²/2 subject to fitting.
It is the same variational selection principle as the earlier construction
(and the same endpoint if rho is the same). Its existence and uniqueness are
proved independently of the noisy trajectory. The potential
Psi=||z-z_*||²/2 obeys dot Psi<=-epsilon Psi and controls both the original
physical distance and training loss. Thus every permitted noise sequence has
the same fitted predictor limit, uniformly on the circle and locally uniformly
on R². All-time boundedness and the Gram gap follow from explicit inequalities;
they are not assumed. The chosen m+1 independent mark-field noise directions
guarantee different state trajectories with positive probability for every
merged sample count m; random intermediate passive predictions are not needed
or asserted universally.

The remaining restriction is explicit: the loss term in physical coordinates
has hidden learning rate 1/rho and readout rate 1. The proof may require very
large rho for poorly conditioned data. Equivalently, after consistently
rescaling both the clock and forcing schedule, one can retain hidden rate 1
and use readout rate rho. Neither formulation is a small perturbation of the
canonical equal-rate physical flow. No layer is frozen, and the target permits
learned hidden geometry, but motion remains in a certified neighborhood.

Independent derivation [NATURAL_CONSTRAINED_ROUTE.md](NATURAL_CONSTRAINED_ROUTE.md)
reaches the same projected-selection mechanism with skew tangent noise and a
centered-Lagrangian Lyapunov proof. It uses half-loss time normalization and
permits the secondary strength to decrease at fixed metric, with a weakening
selection rate. It does not establish random state motion for every dataset;
the lead's explicit noise construction does. This route was frozen before
comparison and is not conflated with the primary unhalved-clock theorem.

## Other simplifications and a noise obstruction

[NATURAL_PENALTY_ROUTE.md](NATURAL_PENALTY_ROUTE.md) gives two complete
ordinary-physical-gradient constructions:

- Adding only rho||h-h0||²/2 and ||P0 c||² to L, with P0 the fixed initialized
  readout-nullspace projection, gives exponential fitting and a unique common
  predictor with no current inverse or layer-metric change. Its hidden endpoint
  is h0, so it deliberately selects the initial-feature kernel predictor.
- Adding epsilon J(h) as well gives a learned hidden endpoint and the same
  guarantees, but retains evaluation of grad J and selects the readout in the
  initial feature span. There is no feature-transport equation. Its objective
  decreases; monotonicity of L alone is not proved.

Both use a strong hidden quadratic penalty and noise tangent to their complete
objective. Neither is claimed to establish nearly unmodified gradient flow.
The first is algebraically simplest but does not retain learned final hidden
geometry; this is why the projected learned selector is the primary answer.

[NATURAL_NOISE_OBSTRUCTIONS.md](NATURAL_NOISE_OBSTRUCTIONS.md) also proves an
exact canonical-start obstruction: train the first coordinate input, and add
arbitrarily small readout noise in a specifically constructed second-coordinate
field orthogonal to 1 and Z2. The original coupled hidden and readout gradient
flow still fits exponentially; the noise vanishes after time one and the full
state converges. Nevertheless an unseen orthogonal input retains a nonzero
Gaussian output variance. A compatible antipodal opposite-label pair is the
same one-representative training problem after merging. This refutes uniqueness
inferences based only on the smallness or disappearance of added noise. It is
not a theorem that every designed noise or ordinary SGD has random endpoints.
The added bounded-random-ODE corollary establishes the same obstruction with a
uniformly small, compactly supported velocity perturbation; it also works when
that perturbation is multiplied by the current positive training residual.
Thus the obstruction is not dependent on unbounded Brownian displacements.

A separate elementary calculation in that report proves that isotropic
nonnegative weight decay cannot both erase arbitrary readout-nullspace memory
and retain an exponential zero-loss tail even in a two-coordinate linear
model. Projecting the selection drift avoids that conflict by separating
fitting directions from the directions that select a predictor.

## Earlier construction

For the exact canonical p=1 closure and every finite positively weighted
compatible binary dataset on the normalized circle, an explicitly constructed
noisy optimizer converges exponentially, for every allowed noise realization,
to the same fitted population state and the same predictor. Convergence of
predictions is uniform on the circle and locally uniform on R².

This is a **selection theorem for a new optimizer**. It adds a strong penalty
on physical hidden displacement from initialization, keeps hidden variables
inside an explicitly certified neighborhood, and transports the readout as
features move. It does not prove uniqueness for the original loss gradient
flow, an arbitrarily small perturbation of it, or the previously discussed
noisy optimizers. Neither hidden block is frozen by the rule.

There is also an exact obstruction to uniqueness from labels alone: even with
the canonical hidden state fixed, bounded readouts fitting a finite dataset
can prescribe any real value at a new circle input outside its antipodal
classes. This is representability, not a reachability claim.

## Contract

Target the canonical p=1 population closure of the bias-free two-hidden
tanh model, on finite positively weighted compatible binary circle data.
Preserve full initialized joint mark laws, ridge/Cholesky normalization,
the actual M transpose, physical population L2/Frobenius norms, and
unhalved square loss. Hidden gradients of the new objective use those
physical norms; the new readout transport is a changed optimization rule,
not the original product-metric gradient of loss. Higher p are not claimed.

Separate: well-posedness given a noise path; convergence to a predictor
along one run; agreement across noise realizations; uniqueness among all
interpolants; and uniqueness of states versus uniqueness of functions.
The user permits new optimization variants. Any additional selection
criterion, restricted state region, or changed hidden/readout dynamics
must be explicit. Do not infer agreement from a passive-input mesh alone.

The target is a process from canonical initialization with
zero-loss limit and a deterministic limiting function on the whole
circle, independent of its optimization noise. A state potential with a
uniquely selected zero may prove this, but its definition may use only
the current state and explicit fixed information. A variational target
must have a proved existence/uniqueness theorem and cannot be supplied
by an unknown training endpoint.

## Selection and proof map

Write h=(w,M), h0=(g,D), and let A_h map the population readout to the
probability-weighted vector of training predictions. Let Y be the weighted
label vector and K_h=A_h A_h*. Define

\[
J(h)=\tfrac12Y^T K_h^{-1}Y,
\qquad F(h)=J(h)+\tfrac\rho2\|h-h_0\|^2.
\]

J is half the squared norm of the minimum-norm readout that exactly fits
the training labels with the current hidden features. The selection principle
is equivalently to minimize

\[
\tfrac\rho2\|h-h_0\|^2+\tfrac12\|c\|^2
\quad\text{subject to }A_hc=Y,\quad\|h-h_0\|\le r.
\]

The positive radius r and finite coefficient rho are explicitly calculated
from canonical marks and the input Gram eigenvalue. Strong convexity of F
in this neighborhood proves existence of a unique interior minimizer h_*.
No future trajectory or supplied endpoint enters the optimizer.

If P_h is the orthogonal projection onto ker A_h and q=P_hc, the potential is

\[
\Phi(S)=F(h)-\min_{\|k-h_0\|\le r}F(k)+L(S)+\|q\|^2.
\]

It has exactly one zero in the declared domain: h=h_* and
c=A_h* K_h^{-1}Y. The new rule uses negative gradient of F with random
directions tangent to its level sets, exponentially damps the training
residual with tangent random directions, and includes the full moving-feature
transport in the readout. The complete formulas are in
[UNIQUE_NOISY_SELECTOR.md](UNIQUE_NOISY_SELECTOR.md). They give

\[
\dot\Phi\le-2\min(\omega,\gamma)\Phi,
\qquad L(t)=L(0)e^{-2\gamma t},\qquad
\|S_t-S_*\|\le C\sqrt{\Phi(S_t)}.
\]

Here omega=rho-C_J>0, C_J is an explicit local Lipschitz bound for grad J,
and gamma>0 is a chosen residual rate. The state norm is the physical
L²/Frobenius product norm on the fixed canonical mark carrier. All bounds
hold for every bounded direction sequence in the specified random ODE;
there is no Itô noise or missing quadratic-variation term. Noise parameters
and their realizations do not change the uniquely selected endpoint once
the selection parameters are fixed.

The proof dependencies are:

1. [CANONICAL_FEATURES.md](CANONICAL_FEATURES.md): reconstruct the exact
   correlated Gaussian/ridge p=1 initialization. Its upper activation fields
   are linearly independent for every finite set of distinct circle inputs
   modulo antipodes. Thus K_h0 is positive definite without an assumed
   all-time kernel gap. The same proof supplies the passive-query freedom.
2. [MODEL_AND_GEOMETRY.md](MODEL_AND_GEOMETRY.md): exact model, physical
   derivatives, local C1,1 constants, positive-Gram neighborhood, and inverse
   operator bounds. No false twice-differentiable L² Nemytskii premise.
3. [UNIQUE_NOISY_SELECTOR.md](UNIQUE_NOISY_SELECTOR.md): unique variational
   target, exact transport, all-time confinement/existence, physical
   coercivity, exponential decay and deterministic common predictor.
4. [PASSIVE_LIMITS.md](PASSIVE_LIMITS.md): strong-state and finite-travel
   estimates for uniform passive predictions; why convergence of each run
   or a query mesh alone cannot establish agreement between different runs.
5. [HIDDEN_MOVEMENT.md](HIDDEN_MOVEMENT.md): both hidden-block gradients are
   nonzero at the canonical coordinate-input pair, for every binary label pair
   and positive mass pair, and remain nonzero on an open neighborhood of those
   configurations. Thus the rule permits actual learning in both hidden blocks.

The independently developed abstract route
[SELECTION_ROUTE.md](SELECTION_ROUTE.md) uses the same variational idea
with bounded, exponentially vanishing additive random forcing. It gives
an alternative convergence proof under stated feature-map hypotheses,
but not monotone loss. It is a secondary, separately scoped construction;
the primary result uses tangent noise and the exact potential above.

## Claims and remaining boundaries

| Statement | Status and exact scope |
|---|---|
| Positive canonical training Gram for every finite compatible circle dataset after merging duplicate/antipodal constraints | Proved at p=1; internally checked against the full assigned book derivation |
| Same finite training labels allow different passive predictions | Proved for represented canonical-hidden readouts; no reachability inference |
| Unique minimum of the selected fitted-state objective | Proved in the certified hidden neighborhood; strong anchoring is essential to this proof |
| Canonically initialized noisy selector reaches the same fitted state for every allowed noise path | Proved by the persisted potential and transport argument; internally checked |
| Uniform passive predictor convergence and finite physical travel | Proved; no assumed state endpoint or collapsing metric |
| Nonzero hidden movement is possible | Explicit canonical witness in HIDDEN_MOVEMENT.md |
| Original GF or previous noisy procedures select a noise-independent predictor | Open; not assessed through prior studies |
| All zero-loss states have the same predictor | Falsified by the augmented-query readout construction |
| Unrestricted hidden learning, anchor removal, a vanishing deviation from original GF, p>=2, finite-width or time-discrete guarantees | Not established |

Compatibility means equal labels at repeated inputs and opposite labels at
antipodal inputs, as forced by the bias-free odd architecture. Combine these
equivalent constraints with their masses. Remaining representatives may be
arbitrarily close. The positive Gram gap is data dependent and need not have
a uniform lower bound. Near collisions the certified radius can be very
small, and inverse operators, the anchor and physical-state prefactors can
be very large. A freely chosen residual rate does not imply uniformly cheap
computation or an equally fast original gradient flow.

The selected predictor depends on the declared anchoring rule, physical norms,
dictionary/initialization, and training data. It is independent of the allowed
optimization noise once those choices are fixed. The result is mathematical
optimizer design, not a generalization-error guarantee or an efficient
discretization claim. No untouched query or its label is used by the optimizer.

## Sources and process

Startup HEAD: bcee9782651c34ae1204d37186e5c57e9282b273. Index empty;
unrelated tracked changes preserved. No Git mutation, experiment,
implementation, established edit, or promotion has been performed.

Read AGENTS.md and RESEARCH_WORKFLOW.md Part 1; apply the rigorous-math
and conjecture-investigation skills. Established scientific inputs:
docs/README.md, docs/NOTATION.md, and complete relevant blocks in
docs/global_nonlinear.md C.4.7.9 state/well-posedness, C.4.7.10.B/C.1,
and D.3. The precise p=1 dictionaries and Gaussian contraction formula
are taken from B/C.1, with the maintained ridge eta_1=1/4096. Including
constants, the established dictionaries have sizes 5 and 3.

Established source hashes read by the lead:

- docs/global_nonlinear.md: `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
  Complete relevant spans: 12084–12425, 13161–13786, 15146–15528.
- docs/NOTATION.md: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- docs/README.md: `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad`.

## Checks and reproduction

Continuation check: the complete projected-selector proof was checked by the
lead and, after both independent candidates froze, by natural_constrained_route.
[PROJECTED_SELECTOR_REVIEW.md](PROJECTED_SELECTOR_REVIEW.md) reports mathematical
PASS with no remaining proof objection for candidate SHA
`96df35354d2b54f111db6d60bba3b5ebc01b8211d0ab61530cba1ec6118a827d`.
The full report, SHA
`257f4736c7ff447a4c83cc08bb714e951d4b71fef71804a9717d277bacf59dd7`,
was read by the lead. It checks constants, full-Jacobian chain rule, noise,
physical coercivity, target definition, global existence, and common passive
predictor. Its clock clarification was incorporated: optional acceleration
requires the same reparameterization of the forcing schedule. These are
informed internal checks, not isolated promotion reviews.

The lead also read both complete alternative route reports and the entire
noise-obstruction report, checking their proofs against the same model inputs.
The projected route's independent argument uses different constants/noise and
is retained as corroborating mathematics; the displayed primary rates come
from PROJECTED_SELECTOR_LEAD.md alone. No claim about ordinary SGD or unmodified
GF is imported from them. Additional informed checks were read completely by
the lead:

- [NATURAL_PENALTY_REVIEW.md](NATURAL_PENALTY_REVIEW.md), mathematical PASS for
  the two ordinary-gradient variants at source SHA
  `1c2a1d2a9dc217ba61af75fc66768e48044f7686ce7725bd4ed81d9c7ef17416`.
  Report SHA: `068f5b03ff32054e72e5bcd5d21659d30c384234fdd526a6c3db998bfd21e1eb`.
- [NATURAL_OBSTRUCTION_REVIEW.md](NATURAL_OBSTRUCTION_REVIEW.md), scoped support
  for the exact canonical-start counterexample and scalar isotropic-decay
  obstruction, with the Brownian-coefficient versus bounded-velocity distinction
  stated explicitly. Its version closure checks the added bounded-ODE variant.
  The complete closure was read by the lead; final report SHA:
  `87a914558eb0bd6263aa5f08c69b451875f10b76190670f2b93bcd5256443ba9`.

Continuation source versions are PROJECTED_SELECTOR_LEAD.md at the reviewed
hash above, NATURAL_PENALTY_ROUTE.md at the hash above,
NATURAL_NOISE_OBSTRUCTIONS.md at
`890de9f524fe6777ce9e54e97245f9b8be80a14bc892d88d7f31fd3be01dd010`, and
NATURAL_CONSTRAINED_ROUTE.md at
`7b00aec87bfe6b905badc0df113e9bbce026757f57d37a3151bc0a4df2796a31`.
The last differs from its independently frozen hash
`91102471b84ac737a65b934cb7cff844467cad3c609fb030f48a271b31b6b681`
only by 27 missing math-command backslashes. No mathematical content changed.
The lead independently reversed those insertions and recovered the frozen hash.
Final scoped Markdown-link and whitespace checks passed; the index remains
empty and established scientific source hashes remain unchanged. No numerical
experiment, source promotion or commit was performed in this continuation.

This is an analytical study; reproduction means checking the displayed
identities and bounds against the named canonical source blocks. No empirical
claim or numerical training campaign is included.

The lead read all three independently frozen routes before comparison,
checked the complete source/dependency arguments, and audited the final
model/transport proof. The within-study informed checks are retained in full:

- [CANONICAL_REVIEW.md](CANONICAL_REVIEW.md): exact Gaussian contraction,
  the delicate scalar monotonicity estimate, finite-family independence,
  and augmented-query readouts. Mathematical PASS; formatting-only correction
  is tracked with its original and amended hash.
- [SELECTOR_REVIEW.md](SELECTOR_REVIEW.md): explicit local constants,
  Hilbert minimizer existence without compactness, projection transport,
  coercivity, confinement, continuation, passive predictions and scope.
  Analytic PASS; its one-constraint genuine-noise completion was added to
  the main proof and is tracked in the review closure.

These are informed internal checks, not fresh isolated promotion reviews.
The README records the integrated theorem; the reports identify their exact
frozen input versions and any followup coverage. The alternative route remains
separate from the primary theorem and has a lead analytic check only.
The lead also read HIDDEN_MOVEMENT.md completely and independently verified
both scaling derivatives, probability-weight cancellation (two constraints give
J=1/a, one gives J=1/(2a)), and the continuity argument. This is a lead internal
check, not a separate reviewer claim about that followup.

Final proof versions:

| Artifact | SHA-256 |
|---|---|
| MODEL_AND_GEOMETRY.md | `d3ed7af3baadbb55e190e2423f0751b11da5ba24ef0c8fcc5c47f627ef57ff89` |
| UNIQUE_NOISY_SELECTOR.md, including the one-constraint noise completion | `d7a7b23f41688d652145d0eb19f407d4a8c974139b904291ffcede82c421eecf` |
| CANONICAL_FEATURES.md, after insertion-only math-delimiter repair | `5eab1371afaca04719bcd78a88c586f33042a008a28bbf1f3a07f0a0f6075b91` |
| PASSIVE_LIMITS.md | `957af4f8276a3a597c97d4fef63eaef749bb1cd55251490198e91a327b9619a9` |
| SELECTION_ROUTE.md | `f806191257eab74436c5ab5da17e0e3c3cc10a2000d6aee8cb0872649f24120b` |
| HIDDEN_MOVEMENT.md | `a166159835ee76fb54e0330b159cbc413ad73a1337680380d028d04839ea1710` |

The canonical delimiter repair adds exactly 167 missing opening escapes and
changes no mathematical content. Its original reviewed hash is
`b202a5344b2ba5bb845e2a907e3347467a7dc65115c68a155af9d367090b53f3`;
the historical dependency recorded in HIDDEN_MOVEMENT.md identifies that
scientifically identical pre-formatting version. The selector's pre-completion
hash is recorded in SELECTOR_REVIEW.md. Established scientific source hashes
were rechecked unchanged at close; the index and unrelated changes were preserved.
Both version closures were read completely by the lead. Final report hashes are
`de9d5d806c2a93361672ad797b1769721a3b7e067e854dc1cd78c1def37ccea1`
(canonical review) and
`a6ab07662863fc5ad92cb32cd3719c62871428a6cade0aa5651b17e5f54c60ba`
(selector review). Scoped document checks found no missing repository Markdown
file links or trailing whitespace. No mathematical issue remains within the
stated selected-optimizer theorem; the open original-GF questions above remain.

## Work and ownership

Lead owns this README, the full model/selection proof, and synthesis.
Scoped agents receive only self-contained prompts or named established
book spans, without prior study or conversation inputs. Independent
routes are frozen before comparison and reviewed before final claims.

Contributors:

- Lead: README.md, MODEL_AND_GEOMETRY.md, UNIQUE_NOISY_SELECTOR.md;
  comparison, source checks and synthesis.
- unique_p1_features: CANONICAL_FEATURES.md and HIDDEN_MOVEMENT.md;
  initially scoped to book lines 13161–13786 and NOTATION only.
- unique_passive_limits: PASSIVE_LIMITS.md from a self-contained prompt;
  after freezing, the informed canonical review with complete named sources.
- unique_selection_geometry: SELECTION_ROUTE.md from a self-contained abstract
  prompt; after freezing, the informed model/selector/passive cross-check.
- natural_penalty_route: NATURAL_PENALTY_ROUTE.md from model/canonical notes;
  after freezing, scoped check of the exact obstruction and scalar decay bound.
- natural_constrained_route: NATURAL_CONSTRAINED_ROUTE.md from model/canonical
  notes; after freezing, PROJECTED_SELECTOR_REVIEW.md with complete dependencies.
- natural_noise_obstructions: NATURAL_NOISE_OBSTRUCTIONS.md from model/canonical
  notes; after freezing, informed check of the ordinary-gradient penalty route.

The three continuation routes received fresh scoped contexts and did not see
one another's candidates before freezing. The obstruction author disclosed a
metadata query that unexpectedly exposed unrelated completed-agent summaries
after its principal derivation; it retrieved no linked material and reports
using none of that scientific content. This route is marked not fully isolated.
The lead received the exposure metadata only and did not retrieve the unrelated
summaries. All accepted mathematics is checked from the permitted model inputs.

No route saw another route in this study before freezing. Followups and reviews
are explicitly informed within-study work, with the accidental external metadata
exposure distinguished above. The present investigation is complete at the
selected-optimizer scope. The continuation simplifies the rule substantially,
but removing the required layer-mobility restriction while retaining learned
terminal geometry and avoiding grad J remains open. No claim about the original
GF implicit bias follows from these constructions.
