# Pause and cross-task handoff — 2026-09-20

## Read this first

The user paused because this account is running out of tokens. This is a
documentation-only handoff, not a new research result or promotion. No proof
search, numerical campaign, or long-running process was launched for this pause.
The small reference-checking helper completed. Other tasks in the shared checkout
are not being stopped or modified.

The latest completed direction is **unique predictor selection by a simpler
noisy optimizer for the canonical p=1 population closure**. The theorem is
complete within its stated restrictions. There is no unfinished calculation
that must be rescued before reading the result. Its main remaining restriction
is a potentially large, data-dependent ratio of readout to hidden learning rates.

The complete historical accounting is preserved verbatim in
[RESULTS_INVENTORY_HANDOFF_20260920.md](RESULTS_INVENTORY_HANDOFF_20260920.md):
the earlier 26-item list plus all 13 subsequently added items. It includes
precise scopes, caveats, proof links, empirical evidence and open questions.
Do not replace it with a short list that omits the landscape/strict-saddle results.

All 39 entries were reported as internally checked study results in this task.
The inventory is a locator, **not a new independent review of those proofs**.
Check the originating README, exact statement, full proof and relevant review
before relying on an entry. Nothing here promotes it into the established book.

Current task: `01a0bfa3-a35f-7352-b845-3d7063d02a73`.
The inventory comes from inherited completed turn
`01a0bb3a-fa48-7f01-baea-81fce828b51c`.
The older parent task is `01a0aa9c-908a-7ff1-92d5-76e03816c2f5`.
Do not read that parent's newer turns as continuation of this branch: it has
continued separately. A lookup during handoff unexpectedly exposed later parent
turn summaries; they were excluded from this handoff and all continuation claims.

## Workspace, permissions and study boundaries

Repository: `/home/amir/Codes/PDE`. PDE and PDE-2 share this checkout and Git index.
Do not clone it, create worktrees, reset it, or adopt another task's changes.
Read current [AGENTS.md](/home/amir/Codes/PDE/AGENTS.md) and Part 1 of
[RESEARCH_WORKFLOW.md](/home/amir/Codes/PDE/RESEARCH_WORKFLOW.md) first.
Use `investigate-conjectures` for research-state work and
`solve-math-rigorously` for proofs; use `teach-technical-math` for explanations.

This handoff and its cross-study inventory are administrative navigation.
They do **not** waive the repository rule against importing unpromoted findings
between studies. Continue one study in its own context. Use that study's artifacts
and established docs/code as scientific inputs. A materially different research
direction normally needs a new study and fresh scientific derivation from allowed
inputs. If a task coordinates several studies, keep their scientific contexts
separate. The user can explicitly direct another task to continue the current
study by pasting the resume message at the end of this document.

Do not reopen an old campaign merely because an old README lists a next step.
Promotion remains separate: workflow Part 2 requires complete fresh reviews,
integration checks, and approval of the concrete reviewed addition. Internal
PASS reports do not satisfy that gate.

At pause, HEAD was `22d2ed040258f5927de5367e815e80527f097743` and the index
was empty. An unrelated tracked modification existed at
`studies/random_dictionary_learned_circle_20260920/SCALING_RUN_RECORD.md`;
it was not read or modified. Recheck current status when resuming. No commit,
staging, book edit or maintained-code edit was performed for this handoff.

## Research vision and philosophical through-line

The central question is **what nonlinear training organizes in the complete
population state**, beyond merely decreasing output error. We want a useful
mathematical geometry of feature learning: which distinctions between inputs
remain accessible, which hidden directions become neutral, how forward and
backward interactions preserve or destroy progress, and what selects behavior
away from the finite training set.

The initial intuition was class separation: members of one class might come
together while different classes separate. The user explicitly accepted that
these movements need not be individually monotone. A successful potential may
mix expanding and contracting components. Its target must be justified by the
dynamics and symmetries, rather than imposing a single arbitrary representation.

The program developed along five connected thrusts:

1. **Exact state geometry and deterministic learning.** Derive everything from
   the actual fixed-order closure, retaining both hidden layers, the correlated
   Gaussian marks, the actual M transpose and the physical gradient metric.
   Find potentials and protected contrast mechanisms, first on understood pairs,
   then genuinely multidirectional examples and open families. Perturbations of
   inputs along the whole flow were intended to reveal missing geometric terms,
   not to substitute a local Taylor expansion for a global theorem.
2. **Extreme configurations as tests of a potential.** Distinguish slow onset,
   slow tails, architectural incompatibility, finite bad equilibria and saturation
   at infinity. Use near-degenerate families and hitting-time lower bounds to
   determine how constants or initial potential values must blow up. Failure of
   a uniform bound is not failure of learning for each fixed compatible dataset.
3. **Landscape versus actual dynamics.** No bad local minima is a major result,
   but it does not imply GF convergence or null bad basins. Analyze strict saddles,
   higher-order descent, state-space topology, population measures, reachability
   from canonical initialization and possible escape to infinity separately.
4. **Designed stochastic dynamics as a bridge toward natural training.** First
   guarantee escape/fitting, then quantify elapsed time, then reduce interventions
   toward GF. Distinguish noise from deterministic correction, physical movement
   from time rescaling, and sample-gradient noise from full-support proposals.
   Near-GF convergence was explored as a route to GF itself; the user then
   explicitly set that limiting-rate direction aside to focus on uniqueness.
5. **Selection of a whole function.** Interpolating finitely many labels leaves
   hidden and readout freedom. The latest goal is a natural enough optimizer that
   both fits exponentially and selects the same predictor across its noise paths.
   This requires controlling directions invisible to the training outputs, not
   just proving that passive outputs converge separately in each run.

The long-term ambition remains nonlinear deep feature learning, not replacing it
silently with a frozen-feature model. Restricted or anchored results are useful
when their costs are explicit. The user values complete unconditional theorems
for the declared process, rather than assuming future Gram gaps, boundedness,
parameter convergence or an oracle endpoint. Do not claim that an unresolved
proof obligation is progress merely because it has been restated more precisely.

## Model contract and canonical sources

The principal model is the bias-free two-hidden-layer tanh fixed-p population
closure. Most latest results use p=1 on the normalized circle, |x|=sqrt(2).
Some earlier p=1 theorems extend to normalized spheres in R^d; retain the stated
dimension, invariant state space and initialization of each theorem.

Read [docs/README.md](/home/amir/Codes/PDE/docs/README.md),
[docs/NOTATION.md](/home/amir/Codes/PDE/docs/NOTATION.md), and the complete relevant
sections of [docs/global_nonlinear.md](/home/amir/Codes/PDE/docs/global_nonlinear.md):

- C.4.7.9: complete closure state, autonomous dynamics, restart and well-posedness.
- C.4.7.10 B/C.1: precise dictionaries, Gaussian contractions and equations.
- C.4.7.10 D.3: physical gradient metric and loss dissipation.

Previously read line spans were 12084–12425, 13161–13786 and 15146–15528;
prefer section identifiers if lines have moved. The established starting facts
are unique existence through every finite time, autonomy/restart from the full
state, and the unhalved-loss identity

\[
\dot L=-\|\dot w\|_{L^2}^2-\|\dot c\|_{L^2}^2-\|\dot M\|_F^2.
\]

At canonical p=1 the full enriched dictionaries have b1 in R^5 and b2 in R^3,
including constant coordinates. The invariant active reduction discussed earlier
has four and two active coordinates and an active 2-by-4 matrix; do not mistake
that reduction for a different full dictionary. Initialization is w=g, M=D, c=0.
The ridge eta_1=1/4096, canonical Cholesky normalization and all joint mark
correlations must be preserved. The marks are frozen; w,c,M evolve.

The convenient functional description is

\[
a_h(x)=\mathbb E_1[b_1\phi(w\cdot x/\sqrt2)],\qquad
H_h(x)=\phi(b_2^\top M a_h(x)),\qquad
f_{h,c}(x)=\mathbb E_2[cH_h(x)],\quad \phi=\tanh,
\]

where h=(w,M). The w and c variables are population fields, not merely finite
vectors. The physical state norm uses population L2 and Frobenius norms.
For finite data,

\[
L=\sum_i\mu_i(f(x_i)-y_i)^2,\qquad \mu_i>0,\quad\sum_i\mu_i=1.
\]

Use x for inputs, phi for activation, and theta for parameter coordinates.
The user expressly rejected z as a name for the full parameter state because
it is usually a preactivation. In the latest theorem, theta is scaled displacement
from initialization, not raw parameters. Merge compatible duplicates/antipodes
before inverting the weighted training Gram. No positive geometry-independent
rate is claimed as inputs approach degeneracy.

## Complete study directory map

All paths below are under `/home/amir/Codes/PDE/studies/`. Every listed README
exists. A metadata-only scan of this branch's file-change records recovered
eleven study directories, including two earlier supporting studies not separately
enumerated in the 39-result list. This table is an index; enter only the study selected for continuation.
The numbered items refer to the accompanying complete 39-result inventory.

| Study | Research scope and important entry files | Inventory |
|---|---|---|
| `closure_lyapunov_p1_20260916` | Initial geometric potentials; reflected/general-separation pairs, structured triples, open families and input-response corrections. Start README.md, then all_angles_result.md, resolution_synthesis.md, correction_synthesis.md. | 10, 11, 13 |
| `closure_extremal_times_p1_20260917` | Earlier extremal configurations and hitting-time investigation, with a two-input anchor. Entry files: README.md, extremal_hitting_times.md, two_input_anchor.md, validation.md; check_algebra.py is a study-owned algebra diagnostic. Consult its recorded scope before comparing with the later sphere results. | Supporting history for 14; not an additional new claim |
| `closure_gaussian_reduction_p1_20260917` | Exact Gaussian/kernel framing, canonical M(0), active dictionary reduction and functional autonomous dynamics. Start README.md and exact_reduction.md. | 25 |
| `minimal_feature_closure_20260917` | Earlier compressed feature-closure design and density formulation. Entry files: README.md, minimal_closures.md, validation.md. Keep model choices separate from the full canonical p=1 model. | Supporting setup for 26 |
| `scalar_density_potential_20260917` | Deliberately smaller scalar-dictionary density model; a positive pair theorem and representable three-input trapping counterexamples. Start README.md, potential.md, rotation_obstruction.md. This is not the full p=1 model. | 26 |
| `p1_three_input_geometry_20260918` | Role of the first hidden layer and full output tangent map; upper-feature Gram collapse need not destroy trainability. Start README.md and result.md. | 12 |
| `p1_sphere_extremes_20260918` | Weighted slow-start classification, extreme families, actual incompatible plateau, stationary gaps, dependent-input strict saddles, null basins, higher-order counterexamples, input perturbations and a wide-network diagnostic. Start README.md, WEIGHTED_THREE_INPUT_RESULTS.md, DEPENDENT_BASIN_RESULTS.md, INPUT_CONDITION_RESULTS.md, FINITE_BASIN_EXTENSION.md, PLATEAU_CLASSIFICATION.md. | 3–8, 10, 14–17; numerical evidence |
| `p1_stochastic_escape_20260918` | No bad local minima on sphere data, subtle infinite-dimensional local geometry, higher-order descent, actual minibatch SGD and local fitting. Start README.md, no_bad_local_minima.md, cubic_and_higher_descent.md, straight_line_geometry_attempt.md, local_minibatch_fitting.md, sgd_geometry.md. | 1, 3, 17, 18, 20, 21 |
| `fixed_p_population_landscape_20260919` | General fixed-p finite-sample landscape theorem and unrestricted sample count at p=2,3 using dictionary structure. Start README.md, finite_sample_theorem.md, p2_p3_unrestricted_theorem.md. | 1, 2 |
| `fixed_p_population_basins_20260919` | Bad basins, saturation at infinity, accepted perturbations, unconditional noisy fitting, rates, continuously corrected flow and near-GF rate limits. Start README.md, CONSOLIDATED_RESULTS.md, NOISE_GLOBAL_PROGRESS.md, RATE_RESULTS.md, NATURAL_NEAR_GF_RESULTS.md, NONVANISHING_RATE_RESULTS.md. | 9, 19, 22–24, 27–31 |
| `fixed_p_predictor_uniqueness_20260919` | **Latest study.** Canonical feature independence, passive-query nonuniqueness, unique selected predictors, simplified projected optimizer, alternatives and exact vanishing-noise counterexample. Start this README.md and the reading order below. | 32–39; renewed proofs supporting 3, 9 |

Generated-data namespaces are `data/generated/<study-name>/`. Existing directories
were verified for closure_lyapunov_p1_20260916,
closure_gaussian_reduction_p1_20260917, scalar_density_potential_20260917,
p1_three_input_geometry_20260918 and p1_sphere_extremes_20260918. No matching
generated directory exists at pause for the other six listed studies. Absence
of a data directory is not a missing proof artifact. Do not manufacture run
paths or treat a numerical diagnostic as an infinite-time population theorem.

## Latest theorem: exact continuation point

The current study's [README.md](README.md) is authoritative for its present state.
Read the latest theorem through these permitted dependencies:

1. [CANONICAL_FEATURES.md](CANONICAL_FEATURES.md): exact initialized feature
   independence for arbitrary finite compatible circle data; positivity of K0;
   bounded fitting readouts with arbitrary extra passive-query value.
2. [MODEL_AND_GEOMETRY.md](MODEL_AND_GEOMETRY.md): exact model, physical derivatives,
   local regularity, explicit Gram neighborhood and operator bounds.
3. [UNIQUE_NOISY_SELECTOR.md](UNIQUE_NOISY_SELECTOR.md): independently defined
   variational target, its existence/uniqueness, and the original transported
   readout selector.
4. [PROJECTED_SELECTOR_LEAD.md](PROJECTED_SELECTOR_LEAD.md): the latest, simpler
   rule and all-time proof; [PROJECTED_SELECTOR_REVIEW.md](PROJECTED_SELECTOR_REVIEW.md)
   is its informed internal check, not a promotion review.
5. [PASSIVE_LIMITS.md](PASSIVE_LIMITS.md) and [HIDDEN_MOVEMENT.md](HIDDEN_MOVEMENT.md):
   uniform prediction convergence and explicit genuine hidden-learning examples.

With A_h c the weighted training-prediction vector, Y the weighted labels,
K_h=A_h A_h*, define

\[
J(h)=\tfrac12Y^\top K_h^{-1}Y,
\qquad F(h)=J(h)+\tfrac\rho2\|h-h_0\|^2.
\]

For explicit sufficiently large rho and a certified hidden neighborhood, F has
a unique interior minimizer h_*. The corresponding minimum-norm fitting readout
is c_*=A_h* K_h^{-1}Y at h=h_*. This defines a target independently of the flow;
the optimizer does not receive its endpoint from an oracle.

Set

\[
\theta=(\sqrt\rho(h-h_0),c),\qquad e=A_hc-Y,\qquad
T_\theta=De,\qquad
P_\theta=I-T_\theta^*(T_\theta T_\theta^*)^{-1}T_\theta.
\]

The full Jacobian includes both hidden blocks and the readout. For bounded
periodically refreshed directions U_t, use

\[
\dot\theta=-2T_\theta^*e-\epsilon P_\theta\theta
             +\eta\sqrt L\,P_\theta U_t.
\]

Writing sigma=lambda_min(K0)>0, the theorem supplies explicit finite rho,
epsilon=sigma/8 and 0<eta<=sqrt(epsilon/4). From canonical theta(0)=0 it proves

\[
L(t)\le L(0)e^{-2\sigma t},\qquad
\|\theta(t)-\theta_*\|\le\|\theta_*\|e^{-\epsilon t/2}.
\]

The current-state potential Psi=||theta-theta_*||²/2 satisfies
dot Psi<=-epsilon Psi-L and L<=C Psi. All-time confinement, persistent Gram
positivity, existence, finite physical travel and uniform whole-circle predictor
convergence are conclusions, not assumed trajectory properties. Every permitted
noise path has the **same deterministic population endpoint**, hence the same
function. Genuine random state paths can be supplied for every merged sample
count. This is stronger than almost-sure fitting to a potentially random endpoint.

Crucial costs: hidden loss-gradient learning rate 1/rho versus readout rate 1;
rho may be very large for poor geometry; only a certified neighborhood is used;
current full-Jacobian Gram inversion remains; noise is a deliberately projected
random ODE, not ordinary SGD or unaccounted-for Ito noise. No layer is frozen,
but the proof controls total hidden movement. This is not yet a nearly unchanged
canonical equal-rate flow. Noise amplitude tending to zero does not remove the
selection drift or change of metric. The chosen endpoint depends on the declared
selection principle, not merely the labels.

The alternative routes are preserved, not conflated:

- [NATURAL_CONSTRAINED_ROUTE.md](NATURAL_CONSTRAINED_ROUTE.md): independent
  projected-selection derivation with different noise and half-loss clock.
- [NATURAL_PENALTY_ROUTE.md](NATURAL_PENALTY_ROUTE.md): ordinary physical-gradient
  penalties; one returns hidden layers to initialization, another learns hidden
  geometry but evaluates grad J. Loss need not itself be monotone in the latter.
- [NATURAL_NOISE_OBSTRUCTIONS.md](NATURAL_NOISE_OBSTRUCTIONS.md): exact canonical
  full-GF example with exponentially vanishing training loss but noise-dependent
  unseen output, even for arbitrarily small bounded forcing that stops at time 1;
  also an isotropic-decay tradeoff in a specified linear model.
- Corresponding reviews: NATURAL_PENALTY_REVIEW.md and
  NATURAL_OBSTRUCTION_REVIEW.md. The README records precise versions/check scopes.

## Established code and simulation references

Read [code/README.md](/home/amir/Codes/PDE/code/README.md) before using APIs.
Its numerical closure section currently begins near line 754.

- [code/pde/observable_solver.py](/home/amir/Codes/PDE/code/pde/observable_solver.py):
  initialize, evolve, predict, rhs, loss, paired_observations, save_restart,
  load_restart. Simultaneous Heun integration of w,c,M with separate initialization
  and population quadratures.
- [observable_initialization.py](/home/amir/Codes/PDE/code/pde/observable_initialization.py),
  [observable_compiler.py](/home/amir/Codes/PDE/code/pde/observable_compiler.py),
  [observable_words.py](/home/amir/Codes/PDE/code/pde/observable_words.py): maintained
  Gaussian initialization, compiler and dictionary-word machinery. Preserve
  InitializationLimits/CompilerLimits, ridge conventions, retained redundancies
  and the reverse-to-forward response contribution.
- [observable_torch_circle.py](/home/amir/Codes/PDE/code/pde/observable_torch_circle.py):
  optional float64 CPU/CUDA counterpart. Public initialized/imported orders are
  1,3,5. A mathematical p=2 theorem does not imply this API supports order 2.
- [code/GENERAL_P1.md](/home/amir/Codes/PDE/code/GENERAL_P1.md): general-dimension
  p=1 guide; related files observable_p1_initialization.py, observable_torch_p1.py,
  closure_comparison.py and code/scripts/example_general_p1.py.
- The earlier [observable_closure.py](/home/amir/Codes/PDE/code/pde/observable_closure.py)
  is a static prototype with different dictionary/ridge conventions, not the
  trajectory solver used above. Do not substitute it silently.

The code references were checked against the maintained README and filename
metadata, not re-audited or run during this handoff. The recent optimizer theorems
have not been implemented, benchmarked, or given finite-step convergence proofs.
The historical wide-network diagnostic is in its own sphere-extremes study and
does not establish convergence of the fixed-order population closure.

## Important corrections that must survive the handoff

- The unrestricted local-minimum result is proved at p=1,2,3, not every fixed p.
  The higher-order sufficient sample bound is binomial(p+2,2), not binomial(p,2).
- The equal-weight r-wise-independence instability threshold is
  4r/[n(r+1)], not 4r/(n+r+1). The three-input stronger result covers 0<L<1;
  arbitrary weights have the stated regularity caveat for basin conclusions.
- General two-input unit-label fitting at arbitrary orientations was not proved.
  Reflection families cover all angular separations but not every orientation.
- No bad local minima does not imply all bad equilibria are strict saddles,
  have cubic descent, or have null basins. Nor does it imply GF converges.
- A full-support measure on population perturbations is not the same as the
  Gaussian marks defining one deterministic canonical population state.
- Positive-loss state sequences at infinity are not reached trajectories.
  Noncanonical trajectories reaching bad equilibria do not establish canonical
  failure or a non-null bad basin.
- Small-loss convergence, state convergence, per-run passive convergence,
  cross-noise predictor agreement and uniqueness among all interpolants differ.
- The universal learned-selector theorem is currently p=1 on circle data.
  The conditioning-corrected fitting theorem is p=1,2; general accepted-noise
  fitting covers p=1,2,3. Do not merge their scopes or optimization rules.
- Exponential successful-stage decay is not an elapsed-time rate. A declared
  proposal clock is not a wall-clock complexity bound. A fixed exponent with a
  diverging prefactor/startup delay is not a uniform from-start GF theorem.
- No proof here automatically transfers from exact population flow to finite
  quadrature, finite-width networks, Euler/Heun discretization or ordinary SGD.

## Open work and how to resume without changing the task accidentally

The immediate request is only to pause and preserve the work. No new experiment
or research branch is scheduled. When the user resumes this direction, the most
natural continuation is to simplify the selected optimizer further while keeping
all three obligations together: every compatible finite dataset, exponential
fitting in the declared clock, and one limiting function across allowed noise.
The concrete bottleneck is relaxing the large-rho hidden-mobility restriction
without hiding an all-time Gram assumption or reintroducing a more complicated
oracle/transport mechanism. This is an open target, not a claim that a solution
is close or an instruction to launch it before resumption.

Other unresolved directions remain: universal canonical GF fitting, universal
bad-basin nullity, norm escape under the original accept-every-improvement rule,
unrestricted no-bad-minimum results at higher p, and rigorous discretization.
The user explicitly paused the nonvanishing-rate-to-GF pursuit before choosing
uniqueness; do not resume that older pursuit automatically.

Before new proof work, select one study and reread its complete relevant proofs
and corrections. State any changed contract. For experiments, predeclare a
specific uncertainty, numerical controls, a modest resource cap and stopping
condition. For independent agents, provide explicit permitted inputs and separate
flat output files; start fresh without inherited scientific discussion when
independence matters. Keep proved, conditional, empirical and open conclusions
distinct, and be direct about failure.

## Short message the user can paste into the next task

> Resume the population-closure research in `/home/amir/Codes/PDE`. I explicitly
> direct you to continue the existing study
> `studies/fixed_p_predictor_uniqueness_20260919` for the latest
> optimizer/unique-predictor direction. First read current `AGENTS.md`,
> `RESEARCH_WORKFLOW.md` Part 1, that study's `HANDOFF.md`, `README.md`, and the
> linked `RESULTS_INVENTORY_HANDOFF_20260920.md`. The inventory preserves all
> 39 results and the study map; it is historical navigation, not permission to
> import unpromoted results between studies. Preserve the canonical model,
> physical metric and explicit limitations. The latest theorem gives exponential
> fitting and one noise-independent limiting function at p=1 using projected
> selection, but requires a possibly large hidden/readout learning-rate ratio.
> Recover that result accurately before proposing the next step. Do not reopen
> the older GF limiting-rate campaign or run experiments merely from old notes.
> Use x for inputs, phi for activation and theta for parameter coordinates.
