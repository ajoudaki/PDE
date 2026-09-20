# A geometric potential for the scalar density closure

New research direction: establish a current-state Lyapunov quantity for the
scalar dictionary closure described by the user, including a consequence for
the full population state. This study does not identify that smaller closure
with the canonical p=1 trajectory or the full network.

**Latest result (2026-09-18, renewed unconditional search):**
[rotation_obstruction.md](rotation_obstruction.md) proves that every rotation
family of pairwise nonparallel triples with balanced unequal positive weights
contains a canonical trajectory with L_dot(0)<0 but L(t)>=1/2 for all time.
An equilateral, linearly separable family suffices; its raw class centers are
not antiparallel, and every member is finitely representable. Thus excluding
only initial stalls cannot yield an unconditional fitting potential. A theorem
on a further explicitly characterized successful class remains open. This
supersedes the earlier absence of an actual nonstationary failure example;
the earlier conditional and finite-time results retain their stated scopes.
See the final continuation below for checks, provenance, and limitations.

## Contract and scientific inputs

The model is two tanh hidden layers with scalar frozen marks b1,b2, evolving
w in R2, scalar c and scalar M. Inputs lie on sqrt(2) S1. The initialization
retains one matched normalized Gaussian forward probe from each population,
with eta=1/4096, w0=g and c0=0. Loss is the unhalved probability-weighted
square loss and time uses the original population-L2 / scalar Euclidean metric.

Scientific inputs are established docs/NOTATION.md, the exact coefficient
target of docs/observable_p1.md, and docs/global_nonlinear.md C.4.7.10.C.1/C.3.
The retained scalar coefficients and every new assertion are derived in this
study directly from those inputs. Other studies are not scientific inputs.
The full established reading guide, shared workflow Part 1 and required
research / rigorous-mathematics skills and applicable references were read.

The original 2026-09-17 pass was theoretical analysis and verification only.
The 2026-09-18 continuation below includes one bounded diagnostic under the
user's standing numerical authorization. All files remain flat in this study;
there are no shared-source edits, staging, commits, or promotion.

## Results and evidence

The complete argument is [potential.md](potential.md). It proves:

- For the equally weighted reflected opposite-label pair family, the explicit
  state potential Phi=L/K, with K the upper activation squared norm, is the
  exact minimum squared readout correction required to fit with present
  hidden features. Four K is the squared upper representation separation.
- K is positive and nondecreasing along the initialized nonlinear flow.
  Including its derivative gives Phi_dot<=-4K0 Phi and L<=Phi.
- Phi also bounds the square of the entire remaining physical path length.
  Both population fields and M therefore converge strongly to a fitting
  state; the corresponding fixed-mark transport distance is bounded by Phi.
  Both hidden layers actually move. The endpoint is a conclusion, not an
  input to the potential.
- A compatible opposite-label pair is an exact positive-loss equilibrium
  for a different orientation relative to a fixed scalar probe. This forbids
  an everywhere-finite, strictly decaying loss-controlling potential for
  every data law in this particular compressed model.
- For generic finite data the same geometric construction is the inverse-Gram
  residual norm. Its complete derivative and the exact missing directional
  inequality are derived. Initial positivity and initial decay are proved;
  no generic all-time fitting theorem is claimed.

Pair-pass status: **internally checked by the author**, with explicit analytic checks
and limitations in [validation.md](validation.md). This is not independent
review or promotion. That original pass used no numerical experiments.

## Reproduction and remaining scope

Read the self-contained proof and its established source sections. Exact
source and artifact versions are in [manifest.sha256](manifest.sha256);
from the repository root use
`sha256sum -c studies/scalar_density_potential_20260917/manifest.sha256`.

Open: continued conditioning and the derivative inequality (15) for generic
collision-free multiple inputs. The counterexample does not settle that
question. No contraction between arbitrary trajectories, unique preferred
hidden representation, scalar-to-p=1 comparison, or network limit is claimed.
Rates depend on geometry and can vanish near coincident inputs.

The original pair derivation and its stated restricted conclusions are complete.
The later user request explicitly authorized the continuation below. Owner
and checker: current primary agent. Only this study's files were edited.

## 2026-09-18 continuation: three inputs

The user explicitly requested a three-input extension. This reopens the same
potential investigation. The existing pair theorem remains unchanged. The
target is an actual extra fitting constraint, not a redundant antipodal atom,
with labels +1 and -1 and the same scalar initialization and physical metric.

Three fresh scoped routes were completed, each supplied the exact equations and
initialization plus selected established sources, without prior study arguments:

| Route / owned file | Mechanism and current status |
|---|---|
| [three_symmetry_route.md](three_symmetry_route.md) | Exact two-mode reduction; proved finite residual overshoot, finite interpolation, and limits of simple sign cones. |
| [three_generic_route.md](three_generic_route.md) | Lower derivative Gram, stationary gap, bounded-readout bridge, escape examples, and a finite-state exponential certificate. |
| [three_obstruction_route.md](three_obstruction_route.md) | Independent stationary-gap and strict-saddle analysis, plus a bounded-readout convergence proof. |

The primary agent owns synthesis, diagnostics and README. Route files were
read after their authors froze their candidates. The completed scoped
cross-audit is [three_generic_audit.md](three_generic_audit.md). The original
independent creative scopes and subsequent supplied-premise follow-ups are
distinguished in [three_validation.md](three_validation.md).

The current result is [three_input_result.md](three_input_result.md):

- **Conditional exponential theorem:** a test using loss, the full tangent
  Gram and an explicit local derivative bound at one finite time guarantees
  exponential decay of Phi=4L/kappa and bounds the entire remaining physical
  path length squared. Both hidden layers contribute. Reaching this test
  from the canonical initialization is not proved.
- **Global restriction:** after loss falls below the smallest sample mass,
  bounded readout norms along any unbounded time sequence imply L tends to
  zero. Thus a positive limiting loss below that threshold forces the readout
  norm to tend to infinity. No hidden-state compactness is assumed.
- **Exact initialization obstruction:** the balanced non-antipodal triple in
  [three_stalled_triple.md](three_stalled_triple.md) has loss identically one,
  although a finite fitting state exists with the same frozen marks. Small
  balanced weight perturbations give a logarithmic hitting-time lower bound
  and a necessary power-law growth bound on any common-rate initial potential.
  This does not rule out a generic-data theorem or prove a matching upper bound.
- **Finite-time positive result:** [three_entry_lemma.md](three_entry_lemma.md)
  proves entry below any fixed target loss for open sets of genuine triples
  sufficiently close to the successful pair. The allowed perturbation depends
  on the target loss, so this is not convergence for one fixed triple.
- **Obstructions retained:** the natural symmetric triple must overshoot one
  target in finite time. Ambient low-loss, small-gradient escape sequences
  invalidate a general compactness/PL shortcut, without being actual trajectories.

Status: the above precise scopes are **internally checked**, with complete
proofs and [three_validation.md](three_validation.md). No generic or genuinely
three-constraint initialized exponential theorem has been established. The
remaining estimate is a trajectory-specific readout bound after entry below
the gap, or attainment of the finite-state exponential certificate, or a
direct all-time directional bound for the changing inverse-Gram potential.

The only numerical diagnostic was precommitted in
[three_diagnostic_plan.md](three_diagnostic_plan.md) and executed by
[three_diagnostic.py](three_diagnostic.py). The exact command, environment,
outcomes and limitations are in [three_diagnostic_result.md](three_diagnostic_result.md).
It used 16/24/32 Gaussian nodes per coordinate, one thread and a 90-second
cap, finishing in 3.11 seconds. Products are in
`data/generated/scalar_density_potential_20260917/three_check_20260918_01/`.
The candidate decreased at sampled times, but late-time quadrature was not
resolved. No population monotonicity or asymptotic rate is inferred.

The manifest records the current source and generated evidence snapshot;
it does not replace the dated scope of either validation report. This bounded
three-route pass and its audit are complete. No further numerical campaign,
promotion or shared-source work is launched from this closing note.

## Further user-directed continuation: centers, scatter, and singularities

The user explicitly reopened the same three-input theorem and rejected a
future kernel/readout condition as its resolution. The new target is an
all-time fitting potential under assumptions on data and the specified
initialization alone, for genuinely three independent constraints. Explicit
singular data may be excluded; assigning an unknown bad trajectory to a
singular set after the fact is not an admissible theorem. The full scalar
feature-learning dynamics, physical metric and initialization stay fixed.

The research and rigorous-mathematics skills are applied. Three new fresh
prompt-only routes ran independently: centers_geometry.md (both-layer
class-center/scatter geometry), centers_nonescape.md (balance and reachable
state control), centers_counter.md (actual-flow obstructions and singular
growth). They do not import other studies or earlier route results; mature
equations may be compared after derivation. The primary agent owns synthesis,
candidate diagnostics, and README. Conditional all-time coercivity is recorded
as an unresolved obligation, never as completion of this new target.

The completed synthesis is [centers_result.md](centers_result.md). The
unconditional fitting/potential theorem remains **open**; the following
precise results are **internally checked**:

- The exact hidden-center/scatter decomposition keeps all three fitting
  constraints. The least-readout correction is the squared correction of
  common/within-class components plus the inverse squared remaining class
  contrast. It is a geometric candidate, not a proved Lyapunov function.
- The complete balanced initial-stall locus is classified by data alone.
  It means coincident initialized upper class centers relative to the fixed
  probe, and is not characterized by opposing raw input class centers.
- A genuine triple family has full initial feature rank and initial descent
  bounded away from zero, yet its loss stays at least 3/32 until
  t=(C epsilon)^(-2/3). This is a theorem on the exact initialized flow;
  each positive-epsilon instance is linearly separable and finitely representable.
- A common-rate potential with a fixed power-law loss comparison therefore
  needs initial value at least constant*exp(lambda(C epsilon)^(-2/3)).
  The initial least-readout correction grows only as epsilon^(-4), and the
  initial Gram eigenvalues have orders 1,epsilon^2,epsilon^4. Thus a fixed
  polynomial inverse-Gram normalization cannot supply that common-rate
  theorem. Geometry-dependent rates and more singular potentials remain possible.
- Every nonstalled initialized trajectory has a persistent hidden contrast
  lower bound derived from physical energy. It does not prove fitting:
  common-center/within-class cancellation and the changing full metric remain
  uncontrolled. Ambient small-dissipation and saddle constructions are
  preserved with explicit non-reachability qualifications.

Proof routes: [centers_geometry.md](centers_geometry.md),
[centers_counter.md](centers_counter.md), and
[centers_nonescape.md](centers_nonescape.md). The frozen actual-flow delay
and center-energy arguments were independently reconstructed in
[centers_audit.md](centers_audit.md); the primary agent separately checked
the appended initial-Gram asymptotics. Full check scopes and corrections
are in [centers_validation.md](centers_validation.md).

One new targeted diagnostic was authorized by the user's standing permission
and precommitted in [centers_diagnostic_plan.md](centers_diagnostic_plan.md).
Its [producer](centers_diagnostic.py) ran the genuine angles (60,126,99)
degrees at Gaussian grids 24/32/48 and the predeclared tighter-solver repeat,
finishing in 2.425 seconds under a 90-second cap. It found positive derivative
of the full inverse tangent-Gram potential, including the first layer, with
the declared empirical checks satisfied. This is evidence against that
candidate, not a rigorous population counterexample. The readout-only peak
comparison was inconclusive; late-time quadrature remains unresolved.
The exact command and evidence are [centers_diagnostic_result.md](centers_diagnostic_result.md),
with generated products under
`data/generated/scalar_density_potential_20260917/centers_check_20260918_01/`.

This pass is complete with the affirmative theorem unresolved. A next proof
must supply an actual current-state balance law controlling signed readout
cancellation and motion of the lower metric. Repeating a future coercivity
assumption does not close it. No further experiment, promotion, Git write,
or shared-source edit is launched from this record.

## Renewed user request: an unconditional potential

The user explicitly reopened the same investigation with “try harder and push
this potential; unconditional.” The contract remained the exact scalar
population dynamics, canonical initialization, three genuine fitting
constraints, data-only assumptions, and no future coercivity premise.
Additional singular data may be excluded only through a justified description.
The research and rigorous-mathematics skills continue to apply.

Three fresh, prompt-only routes were assigned the complete model and separate
owned files. No other study was a scientific input:

- [push_balance.md](push_balance.md) tested whether exact dilation balance
  yields a state invariant controlling the readout and M. Nonzero circulation
  on two tanh profiles rules out integrating that identity alone into a
  universal readout correction. Its finite-energy loop is explicitly not a
  training trajectory.
- [push_collision.md](push_collision.md) initially investigated lower-code
  collisions and escape. After its preliminary route had developed, the
  supervisor supplied a new rotation argument for independent reconstruction.
- [push_constructive.md](push_constructive.md) initially investigated entry
  into a fitting basin from a pair perturbation. It subsequently received the
  same rotation argument, and independently reconstructed and strengthened it.
  It also checked finite representability and uniform initial progress.

The resulting theorem is the complete self-contained
[rotation_obstruction.md](rotation_obstruction.md). Finite-time continuity
and exact antipodal covariance force a zero scalar hidden code for some
rotation at each time. Nested compact loss-superlevel sets give a single
fixed rotation with L(t)>=1/2 for every time. Unequal positive weights rule
out initial stalls at every rotation. Compactness also gives a uniform
positive initial descent across the whole family. The model can fit every
member at a finite state with unchanged marks.

Consequently **no finite exponentially decaying potential controlling loss
down to zero can cover all these nonstalled configurations**, even if its
positive rate is data-dependent. Allowing infinite potentials remains
consistent, but additional singular configurations are required. Every
rotation family above contains one, including the explicit equilateral
family with weights (3/8,1/8,1/2). Nearby hitting times for every loss target
below 1/2 diverge, in the extended sense. A common-rate, common-comparison
potential would have to diverge on approach to such a configuration.

This is an existence theorem for a bad angle, not a supplied numerical angle
or a positive-measure bad set. The proof does not establish positive initial
readout-Gram rank at that angle. It does not disprove an almost-everywhere
theorem or establish that all genuine triples fail. A positive unconditional
potential outside a fully data-defined larger singular set remains open.
The theorem is specific to a scalar hidden code with the fixed probe and
zero readout initialization; it is not a theorem against the full p=1 closure.

The primary agent owns synthesis, validation, manifest and this README.
The three route reports were read in full, and their mathematical arguments
were checked analytically. A fresh isolated reviewer was assigned only the
frozen synthesis, without route reports or prior verdicts. The final review
and version record are linked in [push_validation.md](push_validation.md).
The corrected main proof passed the [isolated internal audit](push_final_audit.md)
and is **internally checked**, with its exact limitations retained. The
affirmative potential theorem on a further successful data class remains open.
No numerical experiment was needed or run in this continuation. All current
work stays within this study; there is no promotion, shared-source edit,
staging, or commit.
