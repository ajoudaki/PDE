# Basins and escape in fixed-order population closure

2026-09-19. New study for the materially different dynamical question of
reachability, attracting basins, and escape from bad equilibria.

## Consolidated current results

The latest optimizer results are in [RATE_RESULTS.md](RATE_RESULTS.md),
[NATURAL_NEAR_GF_RESULTS.md](NATURAL_NEAR_GF_RESULTS.md), and
[NONVANISHING_RATE_RESULTS.md](NONVANISHING_RATE_RESULTS.md): explicit
rates for accepted-noise schemes, a continuously evolving conditioning
correction with exponential loss decay, and precisely scoped limits
approaching original GF. The earlier basin/escape synthesis below
predates these quantitative continuations.

[CONSOLIDATED_RESULTS.md](CONSOLIDATED_RESULTS.md) gives the six main
surviving results in logical order, with exact scopes and proof/review
links: compatible-data interpolation; canonical strict initial descent;
thin basins for specified bad families; saturation obstructions at
infinity; the original-noise fitting-or-norm-escape dichotomy; and
unconditional fitting for the modified fractional-progress acceptance
rule. It removes superseded weaker conclusions from the main narrative
without deleting their original records. This is a synthesis of this
study only; earlier unpromoted landscape/potential studies are not inputs.

The earlier time clarification was eventual finite hitting time and
geometric decay in completed stages. The quantitative continuations
below supersede its lack of elapsed-time bounds for specified modified
algorithms. The original autonomous gradient-flow fitting question
remains open.

Consolidation check: the lead rechecked the noise statements against their
proofs and isolated reviews and verified unchanged source hashes for the
earlier deterministic proofs. A fresh read-only scoped agent,
consolidate_deterministic, read the assigned deterministic proof/review
files and confirmed the p=1,2 initialization scope and the distinction
between local conditional nullity and global meagreness. No new theorem,
experiment, established edit, or Git write accompanied this synthesis.

## Contract and scope

The user asks whether positive-loss equilibria of the canonical population
closure have null basins, whether any have substantial basins, and what
deterministic or stochastic mechanisms permit escape. Begin with the exact
circle closure at p=2 and p=3, retaining full dictionaries, initialized joint
laws, actual transpose, physical population L2/Frobenius gradient metric,
and unhalved probability-weighted square loss. Finite positive data weights
and compatible binary labels are the primary family. Every use of a
different scalar comparison model or perturbed algorithm must be explicit.

This is a new scientific direction under AGENTS.md. Scientific repository
inputs are established docs/ and code/ only, followed by this study's own
artifacts. No earlier study's unpromoted proof is imported. The user's
proposed nearby-lower-loss property can be considered as an explicit
hypothesis in abstract escape statements; any actual closure claim needing
it will supply its own derivation from established equations. Prior
conversation is not used as proof authority.

There is no infinite-dimensional Lebesgue measure. Every basin-size claim
must name its probability law, finite-dimensional slice, or topological
meaning. The canonical infinite-population initial law is deterministic;
randomness of its marks is not a random draw of a population state.
Finite-time avoidance, asymptotic convergence, local departure, global
escape, stochastic recurrence, loss fitting, and finite-particle behavior
are separate claims.

## Work and ownership

Lead owns this README and assembled results. Independent agents receive
self-contained prompt models or explicitly designated complete established
source sections, write separate flat files, and freeze before comparison.
This is theoretical work and proof checking. No experiment, established
material edit, Git write, or promotion is planned.

Startup read AGENTS.md and RESEARCH_WORKFLOW.md Part 1; use the rigorous
mathematics and conjecture-investigation skills. HEAD at startup:
07e627a7b5e6254c2a033b7273bb3649473b50e1; index empty; concurrent changes
preserved. Read docs/README.md and docs/NOTATION.md; exact equations and
dictionary source are global_nonlinear.md C.4.7.10.B, C.1, D.3.

## Initial proof obligations

1. Determine what nearby descent proves about attraction, without
   confusing non-minimality with a null basin. Seek an actual closure
   positive-basin example or identify the precise obstruction.
2. Derive current-state criteria for transverse instability from exact
   readout/hidden coupling. Verify the topology and regularity needed to
   turn negative curvature into a basin statement.
3. Define a natural noise law and prove only the escape conclusions its
   support and persistence justify. Distinguish fresh state perturbations
   from minibatch sampling of per-sample gradients.
4. Address the deterministic canonical initial state separately; nullity
   under an unrelated random perturbation law does not settle it.

## Results and claim levels

The deterministic question is partly resolved, not universally resolved.
There are rigorous local conditional-measure and global topological basin
theorems for explicit families of actual closure equilibria, including a
genuine partially fitted three-input equilibrium. No positive-measure
bad basin in the actual closure has been constructed, and no universal
bad-basin-nullity or canonical convergence theorem is claimed.

| Claim | Status and exact scope | Proof |
|---|---|---|
| Nearby lower loss alone implies a null basin | False, even for analytic nonnegative squared loss; scalar semistability supplies an open basin | ESCAPE_AND_LIMITS.md, Section 2 |
| Full physical Hilbert dynamics is well posed through every finite time | Proved directly for bounded fixed dictionaries and finite bounded-label data; preserves exact metric and transpose | ESCAPE_AND_LIMITS.md, Section 1; CLOSURE_ROUTE.md, Section 1 |
| Certain bad families have thin deterministic basins | Proved: local forward-trapped sets lie in positive finite codimension Lipschitz graphs, hence are null for conditional densities on unstable fibers; global basins of strong point convergence to the families are meagre | CLOSURE_ROUTE.md |
| A nonparallel three-input bad equilibrium with partial fitting exists | Proved: equal weights, labels (+,-,+), predictions (0,0,1), loss 2/3; inside canonical parity subsystem; coupled negative curvature and the same graph/meagre basin conclusion | PARTIALLY_FITTED_SADDLE.md |
| Canonical p=1 and p=2 immediately leave the zero-predictor loss level | Proved for every compatible finite circle dataset, with full correlations and each prescribed ridge; all later loss-one prediction limits are excluded | INITIAL_EXCLUSION.md; INITIAL_REVIEW.md verifies the same argument at p=1 |
| Minibatch noise automatically escapes every bad equilibrium | False in the actual closure: every individual sample gradient vanishes at (w,0,0), including many strict saddles | ESCAPE_AND_LIMITS.md, Section 4 |
| Persistent accepted small perturbations exclude bad point convergence | Proved for an explicitly changed algorithm: almost surely no non-local-minimum accumulation point at proposal times; no countability of equilibria required | ESCAPE_AND_LIMITS.md, Section 5 |
| Original full-support accepted-Gaussian rule reaches zero loss | Proved on bounded-recurrence paths; otherwise any positive-loss limit forces physical norm to tend to infinity. Recurrence from canonical initialization remains open. The bounded-step variant retains the older conditional precompactness result. | NOISE_GLOBAL_PROGRESS.md; ESCAPE_AND_LIMITS.md, Section 5 |
| Harmonic higher-order descent forces null basins | False as an abstract implication, even with odd polynomial predictions and a squared-loss remainder; no actual tanh open-basin construction follows | HARMONIC_ROUTE.md |
| All actual bad equilibria have null basins, or canonical loss tends to zero | Open | Missing estimates below |

Here compatible binary data means equal labels at repeated inputs and
opposite labels at antipodal inputs. There is no sample-count bound or
linear-independence assumption in the initial-descent theorem.

The actual deterministic families with proved basin thinness are:

1. (w,c,M)=(0,0,M0), M0 nonzero, when the signed input centroid is nonzero.
   The unstable dimension is rank(M0).
2. (w*,0,0) when sum_i mu_i y_i E[b1 phi(w* dot x_i/sqrt(2))] is nonzero.
   The unstable dimension is d2=3,6,10 at p=1,2,3.
3. More generally, stationary states whose individual backward fields
   q_i vanish and that have a negative loss second variation. Their
   gradient linearization is finite rank with an expanding eigenspace;
   the genuine partially fitted example belongs to this class.

The graph theorem is proved by comparing two exact trajectories and
showing their difference expands if its unstable component exceeds
its complementary component. It does not rely on an unverified C1
stable-manifold theorem in L2. Finite-time flow openness and a countable
cover give global meagreness; nonlinear infinite-dimensional flow maps
are not asserted to preserve Gaussian null sets.

At every stationary state, readout stationarity gives
L=1-sum_i mu_i f_i^2 for binary labels. Thus the canonical initial-descent
result excludes all zero-predictor stationary limits, not just a selected
collection of collapsed examples. Remaining positive-loss equilibria
relevant to that trajectory must have nonzero predictions and loss in
(0,1). The explicit loss-2/3 example demonstrates why this remaining
class cannot be dismissed by the loss-one exclusion alone. No canonical
reachability of that example is proved.

## Independent routes and validation

The closure cone route, Gaussian initialization route, and harmonic
Taylor route were assigned independently with explicit prompt-only or
established-book scopes. Their files were frozen before comparison.
The lead supplied the exact transverse-coupling test, the three-input
partially fitted construction, and the accepted-noise proof.

Separate isolated reviewers were assigned frozen scientific inputs:
INITIAL_REVIEW.md for the Gaussian initialization result, and
ESCAPE_REVIEW.md for the full-H dynamics, cone result, explicit saddle,
and noise theorem. Both reviews record PASS within the stated scopes.
INITIAL_REVIEW.md also verifies the order-one extension with its own
prescribed ridge. The escape review's wording correction, that a point
basin is contained in rather than equal to a countable union of trapped-set
pullbacks, was made and independently rechecked. The
harmonic route is retained as an internally checked route exploration;
its more detailed Taylor classifications are not needed by the main
basin or initial-descent theorems.

No numerical simulation was run. No established material was changed,
no Git write was performed, and nothing is promoted.

Source hashes at this investigation:

- global_nonlinear.md:
  81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c
- NOTATION.md:
  199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
- docs/README.md:
  60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad

## Exact unresolved obligations

The strongest outstanding deterministic question concerns positive-loss
stationary states with nonzero predictions, loss below one, and no
quadratic expanding direction. Nearby descent, an odd leading term,
and harmonic signed Taylor terms do not settle their basins. One needs
either a model-specific coupled escape estimate through the degenerate
directions, or an actual invariant attracting region in this closure.
The auxiliary squared-loss example shows that stabilizing motion in
extra flat directions cannot be ruled out by the leading descent term
alone.

Even a theorem making every point-convergent bad basin null would need
a separate argument for the deterministic canonical initial state.
It would also leave trajectories without a strong limiting state
uncontrolled; the finite-time bounds do not give all-time precompactness.
There is no claim here that positive-loss asymptotic behavior must
converge to a finite equilibrium.

For a stochastic conclusion one must specify support and persistence
of the noise. The proved accepted-proposal mechanism is a modification
of training, not an identification of SGD sampling noise. Vanishing
noise can have summable escape probabilities, and raw noisy steps
need not preserve loss monotonicity.

## Continuation: does the same noise eventually fit?

The next user request explicitly continues the accepted-noise question:
can the same process be shown to reach its zero global loss? This remains
in the current study, with unchanged scientific inputs and no import of
the earlier landscape study. HEAD at continuation startup was
5d88ee2f34c82da750b97c76507a07cffea3f5d9; index empty. Shared instructions
were reread and source hashes remained the ones above.

The original algorithm draws fresh fixed-scale centered Gaussian increments
in the full physical Hilbert state, accepts every strict loss decrease,
and optionally runs exact gradient flow between attempts. Its noise can
be unconditioned (full support) or conditioned to a fixed norm ball; the
new conclusions distinguish these.

| New claim | Status and scope | Artifact |
|---|---|---|
| No spurious local minima plus fixed Gaussian noise forces zero loss | Falsified as an abstract implication: an analytic scalar square loss has positive-probability drift to infinity with loss tending to one, even with intervening GF | NOISE_OBSTRUCTION.md |
| The closure has positive-loss approximate critical states at infinity | Proved at p=1,2,3 for a compatible three-input law even in V_rho: L=3/4+1/R, all gradient blocks tend to zero, M,c bounded, row norm R diverges | NOISE_CLOSURE_ROUTE.md |
| A fixed additive proposal has uniform useful gain over that positive-loss sublevel | Falsified in the actual closure: expected accepted gain tends to zero along the constructed sequence; this is not a stochastic trajectory counterexample | NOISE_CLOSURE_ROUTE.md |
| Every finite compatible circle dataset has an attained zero-loss state | Proved at p=1,2,3 by sign-pattern lower fields and independent scalar upper tanh features; no future trajectory or special initialization is used | NOISE_GLOBAL_PROGRESS.md, Section 2 |
| Bounded population-state balls have a uniformly positive chance to propose loss below any fixed positive threshold | Proved for unconditioned full-support proposals via a compact set of successful controls, without treating Hilbert balls as compact | NOISE_GLOBAL_PROGRESS.md, Section 3 |
| Under the original unconditioned rule, positive limiting loss forces physical norm to tend to infinity | Proved; bounded recurrence or norm-tight laws along an infinite deterministic subsequence therefore imply zero loss | NOISE_GLOBAL_PROGRESS.md, Section 4 |
| Same Gaussian law, but requiring a fractional reduction at each completed stage, reaches zero loss unconditionally | Proved for the explicitly changed acceptance rule: hold state fixed during rejected trials, every stage completes almost surely, L_J<=theta^J L_0. No uniform proposal-count or physical-time rate | NOISE_GLOBAL_PROGRESS.md, Section 5 |
| Uniform positive readout Gram and bounded M,c imply fitting for the original rule | Proved conditionally, including the bounded-proposal variant; no row compactness is needed | NOISE_CLOSURE_ROUTE.md, Section 4 |
| Original accepted process fits from canonical initialization on all compatible data | Still open; neither actual stochastic access to the saturation sequence nor its avoidance is proved | All new files |

The strict fractional-progress rule is kept separate from the original
accept-any-improvement rule. It preserves the Gaussian law and accepts
no uphill move, but rejects inadequate improvements and pauses GF while
waiting. Its proof can rely on very rare large Gaussian draws. It is an
eventual global-search theorem, not a practical-rate theorem or a theorem
for uniformly bounded infinitesimal noise or SGD.

Three routes were independently assigned and frozen before comparison:
NOISE_OBSTRUCTION.md (prompt-only abstract counterexample),
NOISE_CLOSURE_ROUTE.md (exact book equations and this study's earlier
escape proof), and NOISE_RECURRENCE.md (prompt-only probability criteria).
The lead wrote NOISE_GLOBAL_PROGRESS.md. The recurrence note supplies
additional internally checked abstract tools, including cumulative
conditional probability, tight-distribution criteria and quantitative
Gaussian shift bounds; its general-Hilbert boundedness question is distinct
from the closure-specific bounded-ball theorem now proved by the lead.

Independent isolated reviews are NOISE_GLOBAL_REVIEW.md for the global
progress and abstract counterexample, and NOISE_SATURATION_REVIEW.md for
the actual closure obstruction and Gram criterion. Both record PASS for
their complete frozen inputs, with no substantive correction required.
The lead read both reviews completely and rechecked the unchanged author
hashes. Their verdicts and reviewed hashes are recorded in those files.
No experiment, Git write,
established edit, or promotion was performed.

The remaining original-rule bottleneck is now a precise dynamical question:
can accepted noise from the canonical population initialization approach
increasingly saturated states with positive loss, fast enough that the
total probability of a useful proposal is finite? A local escape theorem
does not decide that. The constructed saturation sequence rules out a
uniform state-independent gain bound; the bounded-ball rescue theorem
shows that any such failure must involve escape of the physical norm.

## Continuation: quantitative speed and perturbation variants

The user now requests explicit speed guarantees for the same fractional
acceptance mechanism and alternative perturbations. This is continuation
of the present stochastic-fitting investigation. Only this study's own
proofs and established docs/code are scientific inputs; the intervening
retrospective inventory of other studies is not imported into this work.
Startup HEAD: ccd783d8d461bfed9a77a35d21831565cf48b314; index empty.
The established source hashes above are unchanged.

The contract is the exact p=1,2,3 finite compatible circle closure, with
canonical marks, metric, full matrix and initialization. Count proposal
time and specified exact-GF intervals explicitly; distinguish expected,
high-probability, almost-sure and successful-stage rates. No numerical
experiment is planned. Bounds may depend on data geometry and Gaussian
covariance. Optimizer changes are authorized but must be explicit; no
unknown fitted endpoint is an algorithmic input.

Active routes: noise_rate_existing owns RATE_EXISTING_RULE.md (finite
Gaussian lower bounds and recursive high-probability times for the same
rule); noise_rate_restart owns RATE_RESTART_ROUTE.md (quantitative
anchored/finite-dimensional proposal alternatives). Lead owns the
current-feature readout-noise route and synthesis. Routes receive only
their assigned existing inputs and freeze before comparison. A third
fresh route could not be started because the agent thread limit was
reached; the lead handles its question locally. No extra permission or
experiment is required. Scope-exposure disclosure from noise_rate_existing:
an agent-list response unexpectedly displayed unrelated old summaries;
the author reports these were not used. Its candidate will receive a
separate check and is not described as a blind independent attempt.

### Quantitative continuation results

The complete synthesis is RATE_RESULTS.md. The prior fractional-rule
statement “no proposal-count rate” is superseded by a finite explicit
high-probability budget; the prior absence of a uniform or unconditional
expected-time bound for that fixed Gaussian rule remains accurate.

| Result | Status and exact scope | Proof |
|---|---|---|
| Same held-state fractional Gaussian rule has a finite explicit confidence-time bound | Proved for canonical p=1,2,3 compatible finite circle data, arbitrary full-support trace-class covariance; includes fixed-duration full GF, with effective-input qualifications for numerical evaluation | RATE_EXISTING_RULE.md |
| Absolute finite-dimensional Gaussian refresh gives polynomial expected loss and hitting-time bounds | Proved at p=1,2,3; global replacement optimizer, with input-only candidate family and no supplied fit | RATE_RESTART_ROUTE.md Sections 2–3 |
| Auxiliary adaptive Gaussian readout search gives exponential expected incumbent loss | Proved at p=1,2,3; separate fixed-feature candidate chain, explicit condition-number dependence, global candidate replacement | RATE_RESTART_ROUTE.md Section 4 |
| Current-feature prediction-isotropic readout noise gives exponential expected loss and elapsed hybrid-time bounds | Proved from canonical p=1,2 on every compatible finite circle dataset; current Gram inverse, fractional acceptance, explicit positive full-GF interval preserving the Gram | RATE_ADAPTED_READOUT.md |
| Small inverse-free current-feature readout noise gives exponential expected loss with geometry-dependent rate | Proved from the same canonical starts; E L_k<=L0 exp[-q_* kappa^2 k/(4m)] with no Gram inverse and physical mean-square noise at most kappa^2 L/(16m^2) | RATE_SMALL_READOUT_NOISE.md |
| Both current-feature variants have a finite strong zero-loss state limit | Proved almost surely by summable accepted jumps and full-flow travel; infinite cumulative GF time is retained | Both readout rate proofs |
| Canonical p=3 automatically satisfies the initial Gram premise for every compatible dataset | Not proved here; an explicit optional input-only, loss-neutral hidden refresh provides it, changing the starting hidden state | RATE_ADAPTED_READOUT.md Section 6 |

The readout variants preserve the complete original closure and run all
three original gradient blocks on every GF interval. They impose a
small enough fixed interval to control total hidden travel. Their rate
proofs maintain readout expressivity; they are not unrestricted global
saddle-escape results, ordinary additive-noise results, or SGD results.
The prediction-isotropic variant can make large physical steps when
the Gram is ill conditioned. The inverse-free variant keeps physical
noise small but pays for poor geometry through its rate.

RATE_OTHER_REVIEW.md is a fresh isolated internal review of the
existing-rule and restart candidates. RATE_READOUT_REVIEW.md is a fresh
internal review of the prediction-isotropic candidate and its explicitly
supplied initialization proof dependencies. RATE_SMALL_NOISE_REVIEW.md
is an informed followup check of the inverse-free extension, not a
fresh promotion review. Minor corrections concern explicit binary-label
scope, target-accuracy ranges, and effective-input wording; the displayed
scientific estimates did not require substantive changes. Final hashes
and read coverage are recorded in the reviews.

All three review reports now record PASS on their final corrected
versions, with no outstanding mathematical objection in the stated
scope. The lead read every candidate and complete review, including
the amendment-closure sections. These are internal checks only.

All work stayed in this flat study. No experiment, established-book
edit, Git mutation, or promotion was performed. The general fitting
problem for small noise with unrestricted hidden flow, and the original
accept-every-strict-decrease fixed Gaussian rule, remain open.

## Continuation: natural perturbations approaching full gradient flow

The user explicitly continues the noisy-optimizer investigation, requesting
full continuously running GF with a more natural perturbation, or a
parameter family approaching GF while retaining quantitative fitting.
This reuses the current study as a continuation of the same optimizer
question. Startup HEAD bcee9782651c34ae1204d37186e5c57e9282b273;
index empty; this study untracked. Shared instructions were reread.
Established and in-study dependency hashes are unchanged from the
complete prior reads; the README and notation guide remain unchanged.

Contract: exact finite compatible binary circle closure, canonical
initialization and physical Hilbert metric, initially p=1 (p=2 only where
the same proved initialization fact applies). Preserve full correlations
and actual transpose. Define actual physical time, rate, and topology of
closeness to original GF. Distinguish infinitesimal-amplitude perturbations,
rare large jumps, deterministic regularization, multiplicative random
mobilities, loss monotonicity versus a different decaying potential, and
finite-horizon approximation versus all-time convergence. No future
trajectory or fitted endpoint may be an algorithmic input. New process
design is authorized, but its differences must be explicit.

Independent routes receive only assigned complete sources in this study
and canonical book sections, without inherited chat or other routes.
natural_noise_continuous owns NATURAL_CONTINUOUS_ROUTE.md (continuous
SDE/Poisson readout noise while all GF blocks run).
natural_noise_rare owns NATURAL_RARE_ROUTE.md (rare proposals with full
GF, physical-time rates and a precise rare-event limit).
Lead explores continuous current-state corrections and writes synthesis.
No experiment or code implementation is planned. Every completed new
candidate needs a full internal check; unchanged earlier reviews do not
certify a new stochastic or near-GF claim.

### Continuous and near-GF results

NATURAL_NEAR_GF_RESULTS.md gives the combined argument and exact
interpretation of each small-parameter limit. The key new continuous
potential is Phi_epsilon=L(1+epsilon tr(K^{-1})), with K the current
weighted readout Gram after compatible duplicate/antipodal aggregation.
Gradient flow of this potential, plus an explicit nonnegative readout
descent safeguard, has pathwise exponential actual-loss decay and a
finite fitted state endpoint. No neighborhood of initial hidden fields
is prescribed. The conditioning force can become large near singular
Gram, which is a substantive optimizer change.

| Claim | Status and exact scope | Proof |
|---|---|---|
| Continuous conditioning-corrected flow has L(t)<=L0 exp(-4 epsilon t), monotone potential and finite strong fitted endpoint | Proved for canonical p=1,2 and every finite compatible binary circle dataset; current-state conditioning correction and explicit absorption at a fitted singular endpoint | NATURAL_CONDITIONING_FLOW.md |
| A uniformly small colored readout noise can be included with the same pathwise rate | Proved along initialized loss-decreasing paths by projecting the bounded force tangent to the readout loss gradient; the deterministic conditioning correction remains essential | NATURAL_TANGENT_NOISE.md |
| The immediate corrected process approaches original GF as correction/noise vanish | Proved uniformly on each finite reference horizon with positive Gram throughout; does not prove closeness beyond a possible reference Gram zero | Both continuous notes |
| Gram determinant along original canonical GF has only isolated finite-time zeros | Proved by holomorphic shifted-L-infinity dynamics and initial positive Gram, p=1,2; no uniform eigenvalue lower bound follows | NATURAL_CONTINUOUS_ROUTE.md Section 3 |
| Rare activation of the continuous corrected process gives unconditional compact-time GF approximation and exponential expected physical-time loss | Proved: E L(t)<=(4/3)L0 exp(-epsilon t), probability of path deviation on [0,T] at most epsilon T, continuous states and finite strong fitted endpoint | NATURAL_NEAR_GF_RESULTS.md Sections 2–4 |
| Original full GF with rare global offers has polynomial or exponential physical-time fitting bounds | Proved at p=1,2,3; the exponential auxiliary-search version also has finite expected total state variation | NATURAL_RARE_ROUTE.md |
| Original hidden GF can run throughout accepted-readout noise with deadlines | Proved at p=1,2; rare activation plus singular ideal proposal intensity, continuous hidden paths, strong endpoint and exponential expected loss | NATURAL_CONTINUOUS_ROUTE.md |
| Full GF plus only ordinary uniformly small local noise fits unconditionally on all compatible data | Open; the continuous correction is not uniformly small near Gram singularity, and rare-intervention limits are not small-amplitude limits | NATURAL_NEAR_GF_RESULTS.md Sections 5–6 |

The new continuous loss rate is in actual continuously running ODE time.
There is no proposal-count-to-time conversion in that theorem. Removing
the conditioning correction removes its fitting proof, even when noise
is retained. The displayed geometry-independent exponent is paid for
by the Gram inverse and potentially large current-state forces.

NATURAL_CONDITIONING_REVIEW.md checks the full conditioning construction;
NATURAL_JUMP_REVIEW.md checks both independent rare/deadline routes.
The reviewers requested only precise mobility time regularity and
almost-everywhere wording for hidden derivatives at readout jumps;
these were repaired without changing an estimate. Informed followups
NATURAL_TANGENT_REVIEW.md and NATURAL_NEAR_GF_REVIEW.md check the
additive tangent-noise extension and the complete rare-activation
combination. Noise-size wording explicitly concerns the initialized
loss-decreasing paths, not ambient states of unbounded loss.

This continuation remains theoretical. No simulation, established edit,
Git mutation or promotion was performed. Finite-step numerical guarantees
and ordinary additive/SGD-noise global fitting remain outside the result.

All four natural-perturbation review reports now record PASS on their
final corrected inputs, with no outstanding mathematical objection in
the stated scopes. The lead read every complete candidate and review,
including both amendment-closure records, and verified the final hashes.
The conditioning and jump-route reviews were separate scoped checks;
the tangent and combined-theorem checks are explicitly informed
followups, not fresh promotion reviews. The principal final fingerprints
are conditioning `0cb163ae98d35a741fbcaee0cacd48ce6381f8746d0ed2f164f54d5eba82e3c0`,
tangent `12272146e901e97014a035ab2a9079d8161c55d0d838fe14c234396ae3ddd0b0`,
and synthesis `8b8c67b482a5a850284b0ac0013e3d25aa4c6534bd2556abafdc94a1a56f5742`.
These internal checks do not promote any result to established material.

## Continuation: nonvanishing rates in the GF approximation limit

The user asks whether a family approaching ordinary GF as epsilon tends
to zero can keep a nonzero physical-time decay exponent. This continues
the same optimizer investigation. HEAD remains
`bcee9782651c34ae1204d37186e5c57e9282b273`, the index is empty, and unrelated
working-tree edits are preserved. Shared instructions and the research
skills were reread; established and in-study source hashes are unchanged.

Contract: retain canonical p=1,2 finite compatible binary circle data,
the full physical state and clock, and compact-time state convergence to
ordinary GF. Distinguish an epsilon-uniform rate AND prefactor from a
fixed eventual exponent with an epsilon-dependent delay/prefactor.
Do not infer an impossibility theorem for canonical GF from an unresolved
fitting estimate. No simulation, implementation, or promotion is planned.

Independent prompt-only route `rate_limit_transfer` owns
NONVANISHING_LIMIT_ROUTE.md (limit transfer, quantitative obstruction,
and exact quantifiers). The lead owns NONVANISHING_RATE_RESULTS.md
(closure-specific consequences, constructive schedules, and synthesis).
A second route could not be started because the agent thread limit was
reached; it is handled locally. Frozen candidates will be compared and
checked before final claims. No other study is a scientific input.

### Rate-limit results and exact claim levels

The complete lead argument is NONVANISHING_RATE_RESULTS.md. The
independent prompt-only NONVANISHING_LIMIT_ROUTE.md supplies a sharper
abstract prefactor lower bound and accuracy/deviation implications.
The lead read that route completely, checked its derivations and scalar
examples, and verified its frozen hash
`96ddd60c46bf7806fcf2841a52c34b2bb3014106f8fb788bd5d7c7c02267f106`.

| Claim | Status and scope | Proof |
|---|---|---|
| An epsilon-uniform exponential envelope transfers to ordinary GF | Proved from fixed-time state convergence in probability and nonnegative continuous loss; no uniform integrability is needed | NONVANISHING_LIMIT_ROUTE.md; NONVANISHING_RATE_RESULTS.md Section 2 |
| Diverging prefactors can retain a fixed exponent while approaching GF | Proved constructively for canonical p=1,2: fixed-strength correction after a bounded random activation window beginning at log(1/epsilon)/lambda; continuous paths, strong fitted endpoint, logarithmic warmup | NONVANISHING_RATE_RESULTS.md Section 4 |
| The fixed-exponent variant has an explicit decaying potential | Proved on the extended state including the declared countdown a: Psi=exp(lambda a)L, Psi0=exp(V)L0/epsilon; E L(t)<=L0 min(1,(e-1) exp(-lambda t)/epsilon) | NONVANISHING_CLOCK_POTENTIAL.md |
| A uniformly small force must have a vanishing eventual exponent | False as an abstract assertion: a scalar smooth perturbation of quartic loss has force error at most epsilon, compact path error at most epsilon t, and late loss exponent four | NONVANISHING_SMALL_FORCE_EXAMPLE.md |
| The closure admits a bounded-prefactor, fixed-rate near-GF family on every compatible dataset | Open; it would prove ordinary canonical GF exponential fitting for those same datasets | NONVANISHING_RATE_RESULTS.md Sections 2–3 |

The clock potential records a scheduled future intervention; it is not a
hidden-geometry Lyapunov theorem for original S alone. After activation
the deterministic correction is fixed strength, although noise can remain
of size epsilon. The scalar small-force example is not a canonical
closure construction or counterexample. The exponent 4epsilon from the
earlier immediate optimizer is only a guaranteed floor; the exact stronger
bound retains the integral of the current smallest Gram eigenvalue.

The independent route was frozen before comparison. Its author then
received the complete frozen lead candidate, conditioning/tangent
dependencies, analytic-Gram section, and the two short extensions for an
explicitly informed internal cross-check in NONVANISHING_REVIEW.md.
The new reference checks do not promote any result. No numerical or
finite-step convergence claim, experiment, established edit, or Git
mutation accompanies this continuation.

The informed review now records PASS with no required correction. The
lead read the complete report and verified unchanged hashes of every
new frozen input. It checked the new limiting, activation, endpoint,
scalar and countdown arguments and reread their conditioning/tangent
proofs and analytic-Gram lemma. Canonical initialization, physical model
identification and original finite-time characteristic bounds remained
explicit previously checked source inputs; this was not a fresh audit
of those unchanged upstream proofs. Review SHA-256:
`40f99a1c1eafc4a2cbf8d31781cd27b3f6b01b869967c1b7b3da5ae8dcde9c5b`.
Lead synthesis SHA-256:
`9683068ab81102bf09c8bd3b23d357bc8e0011da80c0ddc6c2eb253231882008`.
These results are internally checked within the stated scopes, not
promoted. The original bounded-prefactor near-GF rate target stays open.

## Continuation: calibrated epsilon and slower startup growth

The user asks whether the startup time can grow like log log(1/epsilon)
or slower, expressly excluding gains from hidden blowups or misleading
parameter changes. This continues the same optimizer investigation.
Shared instructions were reread; current HEAD and upstream scientific
hashes remain unchanged, the shared index is empty, and unrelated edits
are preserved. The earlier complete skill/reference and book reads remain
applicable; no new external scientific dependency is planned.

The contract now separates three quantities: the label epsilon in a
qualitative compact-time limit, a quantitative intervention/approximation
budget, and an actual bound on the total physical perturbing force.
Hold physical time, data, marks, gradient metric, postactivation correction
strength and noise refresh frequency fixed when comparing epsilon laws.
Audit the full deterministic correction as well as the random term.
No experiment, numerical implementation, Git mutation, or promotion.

Two independent prompt-only routes receive the exact equations or
explicit already-proved continuation inputs, with no inherited discussion:
`honest_epsilon_stability` owns EPSILON_SMALL_FORCE_ROUTE.md (quantitative
population-flow comparison with genuinely bounded perturbing force);
`honest_delay_metric` owns EPSILON_DELAY_ROUTE.md (arbitrary-delay family
and a calibrated accounting of its approximation/intervention cost).
The lead owns EPSILON_CALIBRATION_RESULTS.md and the shared README.
Routes freeze before comparison; new claims require complete checks.

### User-requested graceful stop

The user requested stopping during the internal review. Research and the
active reviewer were stopped; no further derivation or experiment is
authorized by this checkpoint alone.

Saved work:

- EPSILON_DELAY_ROUTE.md: frozen independent route, SHA-256
  `bc6fbacf3bf70f2dcb87171adc97d5e7805ae62ed54b17f839c7dcba7d83d35c`.
  Any diverging delay gives qualitative GF approximation; calibrating
  its intervention certificate restores logarithmic startup dependence.
- EPSILON_SMALL_FORCE_ROUTE.md: frozen independent route, SHA-256
  `62d432dce28ecfd71b88ef91ca451f1c07b464210d5be58dfb9ca2b0438fbf21`.
  A total physical force bounded by epsilon preserves state/loss
  proximity to GF through c(log(1/epsilon))^(2/5). A positive reference
  plateau would exclude log-log fitting on that scale; no actual
  canonical plateau is asserted. Both route files were read completely
  and their arguments checked by the lead after freezing.
- EPSILON_CALIBRATION_RESULTS.md: complete lead synthesis and new
  finite-window lower bound on actual discounted physical-state error.
  Current SHA-256
  `24947a4bcfdcbb65106a935fd1d5dc440d87da193e12cce973b9c3f3b6d26ecd`.
  This remains a candidate awaiting completion of the fresh scoped
  internal review. The reviewer reported that the core gradient,
  Lipschitz, growing-horizon and distance estimates checked out so far,
  and requested one activation-event quantifier correction. That phrase
  was repaired; complete final review and repair closure were not read
  before stopping. No final PASS is claimed for this continuation.

The substantive unresolved question is a genuine sublogarithmic fitting
guarantee at a fixed quantitative proximity/force specification, without
large uncontrolled deterministic corrections. Merely replacing the
chosen delay by iterated logarithms changes the approximation certificate
and does not establish that improvement. The historical logarithmic
schedule remains valid but was not an intrinsic or optimized tradeoff.

No established files, shared Git index, or generated numerical data were
changed. Resume only upon a new user request; first finish the saved
review and recheck source hashes before extending the arguments.
