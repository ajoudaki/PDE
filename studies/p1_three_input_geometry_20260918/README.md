# Three-input learning and singular states of the canonical p=1 closure

## Research contract

New study, 2026-09-18. The user requests a return to the original p=1
population closure: determine whether a rotated equilateral triple can remain
at positive loss, characterize singular states as far as possible, and prove
an exponential loss-controlling potential on a genuine three-input family.
This changes the model from the preceding scalar discussion and is therefore
a separate study. No unpromoted findings or artifacts from other studies are
scientific inputs. The motivating data are specified here independently.

Use the bias-free two-hidden-layer tanh closure on x in sqrt(2) S1, the exact
joint Gaussian initialization, eta=1/4096 Cholesky dictionary normalization,
physical population-L2/Frobenius gradient metric, full evolving M and actual
transpose, and unhalved probability-weighted square loss. The inactive
constant coordinates may only be removed by the proved parity invariant.
The active mark dimensions are four and two; w and c remain population fields.
There is no finite-width or increasing-order claim in this study.

Initial data family: x_i(theta)=sqrt(2)(cos(theta+2 pi(i-1)/3),
sin(theta+2 pi(i-1)/3)), labels (+1,+1,-1), masses (3/8,1/8,1/2).
Other explicit genuine triples may be used for the positive theorem. Avoid
assuming a future Gram bound or trajectory compactness. Separate initial
stalls, arbitrary critical states, and failures reachable from initialization.

## Inputs and ownership

Established inputs: docs/README.md, docs/NOTATION.md,
docs/observable_p1.md, and docs/global_nonlinear.md C.4.7.9,
C.4.7.10.B--C and D.3 as needed for the exact dictionary and population flow.
Shared AGENTS.md and workflow Part 1 apply. Research and rigorous-mathematics
skills are in use. Maintained code will only be used after its guide is read.

Primary agent owns this README, synthesis, validation and any diagnostics.
Fresh scoped analytical agents will own separate flat files and start from
specified established sources or self-contained equations, without study
history or each other's candidates. Input scope and actual checks will be
recorded in their reports. Generated products, if needed, belong only in
data/generated/p1_three_input_geometry_20260918/.

HEAD at startup: 019e3630237e33f58b9636c0aa67a039bebf0182. Index empty.
Unrelated concurrent changes are preserved. No promotion, Git write or
shared-source edit is authorized by this research pass.

## Current status

The synthesis is [result.md](result.md). The following exact statements are
**internally checked**, with complete proofs and independent reviews:

- The initialized upper code is (F(v1),F(v2)), where F is odd and strictly
  increasing. Every finite distinct, nonantipodal circle set has a strictly
  positive initial upper Gram. Initial stalls are exactly signed label-mass
  cancellation within every antipodal input class; in that case zero is
  already optimal among all odd predictors on the finite data.
- Every rotation of the equilateral triple is initially nondegenerate and
  starts with strictly decreasing loss. The initial Gram gap is uniform over
  this fixed rotation family. Arbitrary rotation covariance of the fixed
  p=1 dictionary is false and was not used.
- For three nonparallel inputs, the lower feature differential is onto at
  every bounded-displacement canonical state. This gives a complete finite
  current-state singularity and stationarity test for all matrix ranks.
  At rank two, forward collisions cause full tangent singularity only when
  the corresponding backward vector also vanishes.
- Every positive-loss stationary point in the canonical parity/bounded-
  displacement class is a saddle. Nonzero M gives negative second variation;
  one M=0 stratum has zero second variation but cubic descent. All local
  minima in this class therefore have zero loss. Positive stationary losses
  have a gap at least the smallest sample mass, here 1/8.
- Explicit finite fitting states can collapse both positive upper codes to
  one vector and the negative code to its opposite while preserving full
  three-sample tangent rank through the first layer. Upper-Gram rank alone
  does not characterize the learning geometry.

Proof and review ownership:

| Scope | Author report | Independent internal review |
|---|---|---|
| Initialized geometry, finite-data initial stalls and symmetry scope | [initial_geometry.md](initial_geometry.md) | [audit_initial.md](audit_initial.md) |
| Current-state singularity, stationary strata and saddle theorem | [stationary_geometry.md](stationary_geometry.md) | [audit_stationary.md](audit_stationary.md) |
| Constructive initialized theorem search | [positive_potential.md](positive_potential.md) | Primary-agent check of its conditional trapping lemma; unconditional entrance remains unproved. |

The analytical routes started in fresh contexts with the established source
scope stated above and did not see each other's findings before candidate
freeze. The isolated reviewers received only their complete frozen report
and named established dependencies. Scope corrections and complete hashes
are in [validation.md](validation.md). The primary agent owns the synthesis,
derived representation/odd-risk corollaries, diagnostics, README and manifest.

## Positive-theorem continuation

The subsequent positive-theorem search is recorded in
[positive_continuation.md](positive_continuation.md). It preserves the
canonical circle model and unit labels. Three independent routes were
developed, frozen, and then compared. No new numerical campaign was run.

New **internally checked** results:

- For any proved single-residual reduction with a trainable linear readout
  initialized at zero, convexity of the readout radius in the residual clock
  gives an unconditional exponential loss bound and finite state endpoint.
  This applies to arbitrary rotated single signed directions in full p=1,
  and to exact reflected equal-weight pairs. All hidden blocks keep training.
- Near the reflected antipodal pair, the endpoint transverse derivative is
  strictly positive. This yields a regular two-output endpoint and an open
  family allowing independent perturbations of both directions and masses.
  The potential is the ordinary current loss; the finite prefix and infinite
  tail both satisfy a proved exponential dissipation inequality. This is
  still a two-input theorem, not a genuine-three-input solution.
- For at most three current signed upper codes in a fixed compact annulus,
  separated from incompatible antipodal collisions, a uniformly bounded odd
  interpolating readout exists even through compatible collisions at arbitrary
  relative scales. First and second divided differences prove this result;
  no uniform upper-Gram gap is assumed. The all-time geometric protection
  needed to turn it into a fitting theorem remains open.
- The exact bound ||c(t)||_2^2 <= t holds unconditionally. The multi-residual
  readout-radius identity includes a residual-direction rotation term whose
  sign/control remains unresolved.

| Route | Persisted argument | Check and remaining limit |
|---|---|---|
| Linear readout and residual direction | [global_positive_route.md](global_positive_route.md) | Fresh isolated [audit](audit_global_positive.md): PASS for scalar theorem, endpoint and exact identities. No triple result. |
| Regular reference and open data families | [open_family_route.md](open_family_route.md) | Complete primary-agent reconstruction, including the prefix-to-tail completion in the synthesis. Open two-input family only. |
| Norm/entropy geometry and compatible collisions | [energy_geometry_route.md](energy_geometry_route.md) | Section 8 received a fresh isolated [audit](audit_collision_interpolation.md): PASS. Earlier route diagnostics remain author checked. |

The reviewed candidates stay frozen; the minor regularity conventions in
the scalar audit are stated in the validation record. These checks are not
promotion. No unconditional exponential potential for a genuine triple has
been proved, and no counterexample to such a potential has been established.

## Previous empirical evidence and remaining question

One precommitted [diagnostic](diagnostic_plan.md) was executed by
[diagnostic.py](diagnostic.py): tensor Gaussian rules 8/12/16, three equilateral
rotations, T=120, and one tighter time-solver repeat. All ten solves completed
in 18.83 seconds under the 120-second single-thread cap. The finest losses
were about 0.000308,0.000331,0.000490, but population refinement failed the
declared agreement threshold and no angle met the resolved-fitting criterion.
Time and coefficient refinement passed. The complete
[outcome](diagnostic_result.md) is empirical and unresolved; the mathematical
theorems do not depend on it. Products are under
`data/generated/p1_three_input_geometry_20260918/equilateral_01/`.

**Still open:** whether every initialized equilateral rotation tends to zero
loss, and an unconditional exponential loss-controlling potential for a
general unit-label triple. The missing estimate must exclude positive-loss
saddle approach or asymptotic escape/degeneration, or prove entry into the
regular fitting basin from data alone. Qualitative finite-time surjectivity
and no bad local minima do not imply that estimate. The exact singularity
classification does not cover arbitrary full p=1 states outside canonical
parity or states at infinity. There is no claim that all stationary partitions
listed in the proof are dynamically reachable.

The first bounded pass is complete. The user's subsequent request explicitly
reopens the same initialized convergence question for a strong positive result.
The continuation preserves the exact unit-label model and permits an open
family of genuine triples as a substantive intermediate target. It does not
accept future coercivity/compactness as hypotheses or change the initialization.
Three fresh independent routes were completed: global readout/residual control
(`global_positive_route.md`), a solvable reference and open-family extension
(`open_family_route.md`), and a forward/backward energy invariant
(`energy_geometry_route.md`). Each has only the established equations and the
two complete checked proof files as scientific inputs, and owns its named file.
The primary agent checked quantitative compactness/progress arguments and
owns synthesis. The current continuation ends with the exact unresolved
obligations above, after developing, comparing and checking these mechanisms.
An optional input-dimension scope question has not been answered; the work
therefore remains on the circle and makes no R3 claim.
No promotion, shared-source edit, staging or commit is authorized.
Current source and generated-evidence versions can be checked with
`sha256sum -c studies/p1_three_input_geometry_20260918/manifest.sha256`.
