# Structured fixed-data population continuation

2026-09-30. The user now authorizes choosing a fixed dataset of three, four,
or a few structured points to advance the same q=1 population-learning study.
Latent-factor acquisition, sustained feature evolution and the selected fitted
function are the targets. This remains the explicitly designated study, not
a new compression direction. The current manuscript, authorized appendices,
this study and maintained book inputs remain the scientific boundary.

## Object and distinctions

Keep the exact two-hidden-layer tanh q=1 population equations, fixed initialized
Gaussian T and its true adjoint, zero initial readout/value, Gaussian read-in,
and residual-speed key clock. No learned dense matrix, finite-neuron trajectory,
fresh independent reverse mixer, frozen-feature substitute, or alternate
optimizer may replace it. Population fields represent joint laws; separate
marginal densities do not determine repeated source actions. A finite list of
named densities is not claimed to be an autonomous Markov closure without
showing that its fixed-source correlations suffice.

The previous paper/study source hashes remain unchanged. The complete manuscript
and includes were already read in this task; root reread current instructions,
README, docs/index.qmd and docs/notation.qmd. Skills used remain
investigate-conjectures and solve-math-rigorously. Local regular unique
equivariant population-flow existence remains an explicit hypothesis where
not constructed. A finite-source initialized Gaussian theorem does not prove
all-time fitting. Past two-sample results are not extended by analogy.

## Initial mathematical portfolio

| Route | Scientific scope | Owned file | Mechanism sought |
|---|---|---|---|
| latent_orbit_route | Self-contained canonical model prompt | LATENT_ORBIT_ROUTE.md | Four-point latent factors and representation of their interaction |
| simplex_mechanism_route | Self-contained canonical model prompt | SIMPLEX_MECHANISM_ROUTE.md | Three/four-point simplex geometry, interaction signs beyond a pair |
| global_memory_route | Self-contained model/source prompt | GLOBAL_MEMORY_ROUTE.md | Sustained compensation, invariant or endpoint theorem |
| root | Current authorized sources and this study | STRUCTURED_POPULATION_ANALYSIS.md; initial-integral code; shared README/SYNTHESIS | Choose a nonvacuous dataset, integrate and audit |

Fresh scoped agents do not see each other's results until candidates freeze.
Initial deliverable is one complete lemma/counterexample or an exact blocked
implication per route. Root will select one substantive mechanism, pursue its
remaining proof obligations, and obtain a fresh candidate check. An outcome is
not called profound or globally novel merely because the user requests it.

## Bounded deterministic calculation: initial population integrals

Purpose: distinguish whether the same-label common/contrast effect from two
points survives a nontrivial orbit, and whether individual latent modes grow
under a label depending only on their product. This evaluates initialized
Gaussian expectations, not a width approximation or a training experiment.

Candidates, fixed before the calculation:

1. Three equilateral unit circle points, all labels +1.
2. Four tetrahedron vertices (sigma,tau,sigma*tau)/sqrt(3), all +1;
   equivalently signed inputs of a rotated lifted-XOR task.
3. The same four-point orbit with coordinate squared scales (.8,.1,.1).
4. The same orbit with squared scales (.98,.01,.01).

Compute first reverse response coefficients M, first-layer mode energy
accelerations, and, if inexpensive, full second-layer mode energy accelerations
including the actual joint innovation covariance. Product Gaussian-Hermite
quadrature uses two predetermined resolutions, initial-root orders 31 and 45,
second-population orders 21 and 31. Gaussian inputs and covariance are derived
from the exact initialization; no sources are independently redrawn after
reuse. All derivatives are in feature time s=2 integral(1-f)dt for these
transitive all-positive signed datasets.

Limits: these four configurations and two resolutions, no trajectory integration;
at most ten minutes wall time and one process with bounded chunking. Stop on
an implementation/normalization disagreement rather than interpreting it.
Signs stable at both resolutions with a margin at least ten times their
discrepancy select a proof target; other signs are inconclusive. Quadrature
agreement is diagnostic evidence only, never a rigorous sign certificate.
No fitting/end behavior is inferred from these calculations.

Use NumPy 1.26.4 and SciPy 1.13.0, float64, deterministic quadrature (no random
seed), thread count one. Code/configuration lives here; exact outputs and run
metadata go under data/generated/q1_population_mechanism_20260930/ in a fresh
structured-initial-integrals run directory. Retain source/input/output hashes
and executed command. No manuscript or maintained-code edit, staging or commit.

## Selected second round: weak latent factors in a lifted XOR task

The initial quadrature completed with exit 0. Tetrahedral and moderately
anisotropic orbits have positive initial primitive-factor energy accelerations
in both layers, despite zero factor-label correlations. The small-factor
configuration does not meet the prescribed quadrature-discrepancy criterion
for its smallest coefficients and is marked numerically inconclusive.
No sign proof is inferred. The complete code and results are retained.

Choose the fixed four-point family u_(sigma,tau)=(sqrt(1-2epsilon²),
epsilon*sigma, epsilon*tau), labels sigma*tau, with small but fixed positive
epsilon. An arbitrary fixed orthogonal input rotation may hide these axes;
the latent bits are analyst-specified generative variables, not extra targets.
This is a perturbative proof family, not an input or time limit replacing the
actual closure. The goal is a rigorous strict sign at every sufficiently small
fixed epsilon, together with all-time restrictions on any fitted representation.

After first-route freezes and complete root reads, latent_orbit_route owns
WEAK_FACTOR_ROUTE.md (first-layer factor acquisition and decoder consequences),
simplex_mechanism_route owns WEAK_FACTOR_SECOND_LAYER.md (full second-layer
factor response with joint adjoint innovations). These targeted follow-ups
receive the new task and exact initialized-source formulas, not each other's
new proofs. Root derives/checks limiting constants and all-time selection limits.

Additional bounded calculation: one-dimensional Gaussian integrals in the
analytically derived weak-factor coefficients, Gaussian-Hermite orders
61, 101, 201. These are diagnostics only. If strict signs need numerical
certification, use explicit compact-domain quadrature error, Gaussian tail
and rounding enclosures; an uncertified floating result cannot establish
the theorem. No further dataset search or trajectory integration is authorized
by this second-round record.

## Outcome, bounded evidence and continuation checkpoint

The selected result is strict local primitive-factor acquisition in both
hidden layers of the weak-factor XOR task, with simultaneous context
suppression, first-layer hierarchy improvement and an exact all-time
constituent-versus-product accessibility constraint. The full assembled
proof is STRUCTURED_POPULATION_ANALYSIS.md. It explicitly leaves regular
population-flow construction, global fitting, endpoint existence and full
query-amplitude selection open. No priority claim is made.

Root completed and read all frozen first-round routes before integration.
LATENT_ORBIT_ROUTE.md and SIMPLEX_MECHANISM_ROUTE.md remain alternative
author-checked candidates; their simpler structural statements are not
advertised as the new acquisition theorem. GLOBAL_MEMORY_ROUTE.md is a
complete author-checked attempt with a named remaining memory-defect bound,
not a positive fitting result or an actual nonfitting trajectory.

Executed diagnostic commands, repository root, exit 0:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python studies/q1_population_mechanism_20260930/structured_initial_integrals.py --output data/generated/q1_population_mechanism_20260930/structured_initial_integrals_20260930_01/results.json
python studies/q1_population_mechanism_20260930/weak_factor_constants.py --output data/generated/q1_population_mechanism_20260930/weak_factor_constants_20260930_01/results.json
```

The four configurations and two resolutions were exactly those above; no
adaptive trajectory search was added. Python 3.10.12, NumPy 1.26.4, SciPy
1.13.0, deterministic quadrature with no random seed. The selected limiting
constants are initialization integrals. The diagnostic key
`context_energy_weight_dd_coefficient` in weak_factor_constants.py concerns
the context **readin-coordinate squared norm**, not context activation
energy; it must not be substituted for the latter. The later proof and
certificate compute and label the actual context activation coefficients.

| Diagnostic artifact | SHA256 |
|---|---|
| structured_initial_integrals.py | d49eb9449091c7a41ce62599ee35a99c0db3daa2736a57713bd5a217e8856ff0 |
| structured_initial_integrals_20260930_01/results.json | 432704d499017c2cf95d7866ad0bab7c7c6ad3deb2d844f592c3ca5365e65d76 |
| weak_factor_constants.py | ad026e67578dbc07bdc307230041398a029f73bace1b9e0192bd9e22a787b3e0 |
| weak_factor_constants_20260930_01/results.json | 9034055abb010672f312792d7dde7bf24afcd9b2f9101ee8acd4d549b759c796 |

The direct small-factor quadrature failed the predeclared sign-agreement
threshold for its smallest terms and remains inconclusive. It was not used
to justify a theorem. The targeted exact weak-factor expansion reduced the
sign question to one-dimensional moments. That finite obligation was closed
with directed Decimal interval arithmetic, exact polynomial fourth-derivative
bounds, composite Simpson error and Gaussian tail bounds. See Section 8 of
the main note for the full argument and executed reproduction commands.

| Proof-support artifact | SHA256 |
|---|---|
| weak_factor_interval_certificate.py | 51c7570b1f34a066287f286295868c87283ac45f16d0895d4b4d716c7010be54 |
| weak_factor_interval_certificate_20260930_01/results.json | 316a83c28ccba4415d47d54f6bdb7ad2cd1a307150e86e0b9694ce4feded62cf |
| weak_factor_coefficient_certificate.py | 9d0b0322bcc59a88c6ca5bef1b6ac69911bd035c2cd92006b08e4e511605bba5 |
| weak_factor_coefficient_certificate_20260930_01/results.json | 586699805890bb62ee02dee03a2a091fafcfe63f4fb07f68e8cc3dae92349f1a |

All output paths in these tables are beneath
data/generated/q1_population_mechanism_20260930/; sources remain in this
study. The scripts refuse overwriting and include source/input hashes in
their output. Checker reproductions use separate generated directories.

The fresh first-layer checker read only its complete frozen route, explicit
canonical model excerpt and certificate; its scoped child inspected only
certificate primitives. The fresh second-layer checker read only its own
complete frozen route, explicit model and certificates. Both independently
reproduced and audited the rigorous signs and returned conditional PASS.
The separate assembled-candidate checker receives the complete main note,
both complete route derivations, certificate scripts and exact outputs;
it receives no prior verdicts or other route findings. README records final
hashes and the assembled check outcome. These are internal mathematical
checks, not promotion reviews. No numerical training simulation, manuscript
edit, maintained-code change, staging, commit or push was performed.
