# Independent complete scientific review of R1

Reviewer: `/root/research_review_a`.

Decision: **ACCEPT the mathematical theorem in the frozen R1 packet.** I found
no mathematical error or missing necessary bridge requiring correction. This
is a scientific review of the specified frozen research result; it is not a
promotion decision or approval to change established repository material.

## Identity, isolation, and read coverage

I am distinct from the authors/assembler `/root`, `/root/transport`,
`/root/population`, `/root/nonlazy`, and from the relevance selector. I did
not author any candidate component. I did not read the live study README,
study history, prior verdicts, another reviewer's findings, or live book
sources. I did not delegate the review. No missing dependency was supplied
from memory as an assumed theorem.

The assignment and manifest were read completely. I personally read all
1,841 lines of `R1_PROOF.md` and all 1,310 lines of
`R1_DEPENDENCIES.md`, including proofs and boundary statements. The
nontruncated numbered read batches were:

- Proof: 1–360, 361–740, 741–1120, 1121–1500, 1501–1841.
- Dependencies: 1–350, 351–680, 681–1000, 1001–1310.

I read the complete required skill files
`/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter's complete
`references/research-contract.md` and `references/adversarial-audit.md`.
The packet includes the complete scientific dependencies needed for this
theorem. The introductory statement at proof lines 6–10 makes the C.1/C.3
references provenance only; the existence, oracle, and activity arguments
needed here are supplied within the frozen proof itself.

SHA-256 checks on the frozen scientific inputs gave exactly the manifest
values:

```text
R1_PROOF.md
b7f2a65252353d0e47af50da9895f7206d4e202dd591ac4342bf6a2696e036c1

R1_DEPENDENCIES.md
606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469
```

Additional provenance hashes:

```text
R1_ASSIGNMENT.md
520fd5064aeef156c025e501ffb7887a3423247b5db936f6e0ea23525dbe9d79

R1_MANIFEST.json
06ef4cf1ac0c43040b95f15722fc0f3564e8387a0919e168be128fbfa0ce3044
```

I also extracted the five included components from the frozen proof, removed
only its inter-component framing newlines, and verified every component
SHA-256 against the manifest. All five matched: `THEOREM.md`, `TRANSPORT.md`,
`POPULATION.md`, `ALGORITHM_AND_STATISTICS.md`, and `NONLAZY.md`. This did not
read the live component files. No Git operation or training experiment was
performed. Computation was limited to input and component integrity checks.

## Claim and research contract checked

The target is the actual two-hidden-layer tanh network with normalized input
`u=x/sqrt(2)`, mean unhalved squared loss, and stored-weight mobilities
`(n,1,n)`. The initial variances are `(1,1/n,1/n^2)`. The observation law is
an arbitrary probability law on `S^1 × [-Y,Y]`, with `Y>0` fixed and transport
cost `|u-u'|+|y-y'|`.

The theorem claims a positive interval depending only on this model and Y,
a strong state `(w,A,c)` in full-row L2/operator norm/readout L2, a quantitative
law modulus, an exactly ordered expected generalization gap, simultaneous
limits of actual GD, and positive finite-time activation displacement on an
open family. The argument does not replace this state by its prediction or
by activation marginal laws. Nor does it represent an arbitrary law in
finitely many scalar coordinates: its population state is expressly an
operator/field state. There is no finite-dimensional compression claim to
which an ambient-dimension or hidden-real-encoding loophole could apply.

The comparison oracle uses only a fixed finite law, the initialized arrays,
and population Euler coefficients computed causally from earlier nodes. It
does not use a future trajectory or coefficients fitted to the target
finite network. Its role is a proof approximation, with its length fixed
before the width limit.

## Component verdicts

| Component | Verdict | Necessary content checked |
|---|---|---|
| Frozen Gaussian-program dependencies, III.F and A.1–A.2 | Accept in the supplied scope | Adaptive conditioning, both action orientations, singular-query regularization, generated-space completion, bounded multiplier and fixed neural-product extensions |
| Weighted response dependency C.2 | Accept in the supplied scope | Causal response formulas, weighted derivative estimates, cap selection, marginal Gaussian tails independent of sample count and mesh |
| Finite-dynamics dependency | Accept | Exact gradients, mobilities, kernel/energy normalization, finite-flow continuation, initialization bounds |
| Part I, transport | Accept | Full-row changing-input estimate, a single cutoff power, weighted reference tails, cutoff optimization and displacement continuity |
| Part II, population | Accept | Common initialization, full-state construction, Bochner/HS integrals, integrated tail transfer, uniqueness and local restart |
| Part III, algorithm/statistics | Accept | Actual parameter GD, fixed proxy identification, arbitrary relative limit orders, risk limits, ghost replacement and paired observations |
| Part IV, activity | Accept | Actual-flow coefficients, adjunction-based positivity, positive time, relative open family and finite-width displacement transfer |
| Theorem, proof lines 45–134 | Accept | Its five assertions follow from these components without an additional unproved hypothesis |

## Detailed checks and adversarial outcomes

### 1. Finite normalization and the state topology

I reconstructed the gradients in dependency lines 1121–1159. Since
`delta^ell = n partial f/partial z^ell`, multiplying the first/readout
loss gradients by n gives respectively `-2∫r delta^1 u` and
`-2∫r H^2`; the middle update is `-2∫r delta^2(h^1)^T/n`.
Thus (T2)/(P4) and the rank-one convention use the exact physical clock and
the exact stated mobilities. No residual is hidden inside delta.

The full first matrix has normalized Frobenius norm, while the middle
action has operator norm. These are precisely the norms used in (T3)/(P2).
The first-row update has its explicit two-component input factor. Its
projection on any training direction recovers the Gram-weighted recursion,
without solving a Gram system. This is sufficient even when the active
directions fail to span the input plane.

The initial first-row squared RMS tends to 2, the middle norm is at most 10
with probability tending to one, and the actual readout has expected squared
RMS `n^-2`. The deterministic ball bounds are independent of all training
observations. The Euler bounds use increments evaluated at preceding states
and bounded elapsed physical time, not a gradient-flow energy inequality
applied to GD. Linear parameter interpolation followed by forward
recomputation is retained throughout Parts I and III.

### 2. Initialized Gaussian actions and their adjoints

The adaptive conditioning proof at dependency lines 214–274 correctly
conditions sequentially on a transcript. At each query only one residual
matrix factor receives an additional linear constraint. The minimum-norm
conditional mean satisfies both forward and transpose constraints, and the
remaining Gaussian matrix is projected on the two orthogonal complements.
The discarded projection of fresh Gaussian noise has expected normalized
squared norm `rank(U)/n`, which vanishes for a fixed transcript.

I checked the source-response derivation at lines 276–337. The orthogonality
of the new query residual eliminates the old forward-input terms. Gaussian
integration by parts identifies the reverse-input coefficient, and the old
response terms cancel when the conditioned answer is expanded. This gives
the actual joint forward/transpose limit. Independent *source groups* do
not imply independent action answers; the response corrections preserve
the dependence needed for adjunction.

The singular-query proof at lines 339–382 does not assume continuity of a
pseudoinverse. A fresh independent input perturbation at each call gives a
strictly positive Schur complement at fixed perturbation size. The original
and perturbed finite programs differ by O(epsilon) in normalized RMS on the
operator-bound event. In the finite scalar recursion, covariance square
roots and expected source derivatives converge as epsilon tends to zero.
This makes the order “fixed epsilon, width limit, then epsilon to zero”
valid, including zero or duplicate queries. On singular source supports,
the possible derivative ambiguity is killed by the same Gram's null space.

The countable generated language and density argument at lines 402–440
give an action on the whole generated L2 space, rather than an action on
only the current training fields. Exact finite linear identities and
second-moment convergence make the assignment well-defined on L2 classes.
Passing the finite pairing identity on a dense set proves that the reverse
assignment is the Hilbert adjoint. In Part II the full Gaussian root pair
is included from the start, and real inputs/coefficients are obtained by
completion. Thus the carrier need not be changed when the training law
changes, and passive input directions remain represented.

A.1 and A.2 were checked separately. A continuous coordinate map with a
linear envelope preserves L2 convergence using uniform integrability of
squared inputs. Smooth approximations are fixed before taking a width
limit. For a fixed product `b(z)q`, clipped scalar expressions have linear
value envelopes and polynomial first-derivative envelopes. SubGaussian
roots and the fixed Gaussian source list justify derivative uniform
integrability in A.2. This is a fixed-program statement; it does not assert
empirical higher moments or an increasing-transcript theorem.

### 3. Uniform weighted response bounds

The decisive quantitative dependency is C.2, dependency lines 563–1078.
The preliminary source RMS and residual bounds required there are supplied
by (P6); bounded tanh gives the stronger activation bound needed here.
The hypotheses use neither positive atom weights bounded away from zero nor
a lower Gram eigenvalue bound.

I followed both response estimates. The forward-source derivative row sum
obeys a discrete Gronwall inequality with random coefficient
`d_ell + sum_b omega_b |P_(b,u)^ell|`. Taking a maximum of derivative row
sums does not replace this weighted sum by a maximum of random backward
fields. Jensen applied with the time/input probability weights bounds the
exponential of its integrated coefficient. The resulting estimate (28)
uses an individual P L2 norm and the derivative-row L2 norm.

For a single backward-source pulse, the direct forcing is proportional to
`Delta omega_b`. The Gronwall estimate (31) retains that factor, leading to
the entrywise forward-response cap (32). There is no unweighted sum over
inputs and no reciprocal atom weight. This is the necessary mechanism for
constants independent of dataset cardinality.

I checked the cap selection and actual construction order at lines
961–1023. Forward caps are chosen from bottom to top; backward caps from
top to bottom. Once fixed, all exponential factors tend to one as the time
horizon tends to zero. At a given step, current forward coefficients use
already available lower fields and past backward fields; current backward
coefficients use already constructed upper backward fields. No estimate
requires its own unconstructed current coefficient. The induction therefore
does not assume future tails. Variable steps and affine interpolation
evaluations follow by preserving each pulse's own step length and total
elapsed time.

Outcome: the uniform *individual* exponential-square moment estimates
needed for the transport proof are justified. No bound on a maximum over
inputs, times, or neurons is needed or established.

### 4. Transport, tails, and the quantitative modulus

The key multiplier estimate (T10), proof lines 302–307, follows by splitting
only the reference multiplier. Expanding the top backward field, applying
the bounded adjoint, and then expanding the lower gate gives one factor
`1+R`, not a product of two such factors. The earlier backward error is
multiplied only by bounded operators or gates. The changing-input term in
the full first-row velocity is explicitly present at lines 332–346.

Integrating against a coupling places every tail on the reference marginal
alone. Therefore the finite and population estimates need neither a tail
bound for the actual changed-law trajectory nor a dataset-wide maximum.
The rank-one operator norm is exactly the product of the two field norms,
so the middle-block estimate has the required topology.

With Gaussian reference tails, Gronwall yields
`C exp(a R)[(1+R)q + exp(-c R^2)]`. Choosing R proportional to
`sqrt(log(e/q))` for `0<q<=1` gives the claimed modulus. For q=0, sending
R to infinity kills the remainder and identifies the full states. For q>1,
the bounded prediction estimate is used instead; the proof never evaluates
the displayed logarithm outside its domain. The difference-of-squared-norms
estimate (T19) controls paired activation displacement and its averaging
law, not merely marginal activation laws.

### 5. Strong population existence, integrals, tails, and restart

The joint backward-field continuity at proof lines 742–758 uses a valid
bounded-multiplier argument: isolate the changing L2 field, cut off the fixed
remaining field, and remove its L2 tail. It does not incorrectly assume
global L2 Lipschitzness or Fréchet differentiability of the nonlinear
backward map. Compactness of the input circle upgrades this continuity to
uniformity over inputs along a convergent sequence of states.

The vector-field integrands are continuous on compact data support, with
compact separable ranges in their Banach spaces and bounded norms. This
justifies their strong Bochner integrals despite the possibly nonseparable
ambient operator space. Rank-one continuity also holds in Hilbert–Schmidt
norm; the learned increments of the eventual strong solution are actual
HS integrals. The initial action need not be HS.

For a fixed finite law, Euler paths are Cauchy in the complete full-state
path space by (P13a), first making meshes small at fixed R and then making
R large. Continuity of the vector field passes the assigned velocities to
the strong integral equation and gives strong C1 regularity. Applying
(P14) to finite approximations of an arbitrary compactly supported law
gives the same full-state convergence. Equation (P9) justifies the change
of law inside the vector-field integral; the proof does not stop at
prediction convergence.

The law-tail transfer at proof lines 941–984 is also valid. At each fixed
time, backward fields converge uniformly in input in L2. Truncated
exponentials are bounded Lipschitz functions, so their expectations pass
through the state limit uniformly in input and then through the varying
law. Monotone convergence removes the truncation. This proves an integrated
input-law exponential moment with time-independent constants. It need not
prove a pointwise continuum-wide or path-supremum tail estimate. Applying
Cauchy–Schwarz in the input law gives exactly the integrated RMS tail
needed by the one-reference estimate.

An arbitrary other strong integral solution is kept in the common ball by
the first-exit bound. The constructed solution supplies the reference tails,
so the other solution needs no tail assumption. The q=0 comparison proves
uniqueness. The same argument on the remaining local interval gives
uniqueness after restart from a reached state. Restarted Euler convergence
is compared to the existing continuation, so the proof does not silently
assume fresh Gaussian roots at restart.

### 6. Actual GD, fixed-oracle identification, and limit order

At fixed finite reference law and fixed proof mesh, (A3) defines actual
finite proxy parameters on the same initialized first and middle arrays as
GD. It also retains the same random finite readout as an additive term.
The population oracle has zero readout root; their difference has vanishing
RMS, justified by its exact second moment rather than by silently modifying
the finite algorithm.

The learned middle action expansion reduces proxy/oracle discrepancies to
the finite list of contraction errors in (A4). The transpose expansion has
the corresponding backward contraction. Recomputed gate products are
controlled by (A5), with width taken to infinity at fixed cutoff before
removing that cutoff. The continuous cutoff domination used for (A6) avoids
assuming convergence against a discontinuous quadratic tail test. These
facts give the assigned-velocity defect and reference-tail control at the
fixed coarse grid.

The actual GD trajectory may have arbitrarily many samples or steps. It is
compared deterministically with that fixed proxy in the same-width state
norm. Its own tails are never inputs to the estimate. Grid/interpolant
distances cost only the two step sizes because the parameter speeds are
uniformly bounded. Thus (A7) remains valid for arbitrary empirical-law
sequences tending to the target law.

Input and time nets are legitimate: on the comparison ball, recomputed
forward fields and predictions are uniformly Lipschitz in input and in
time along the parameter interpolants. Adding finitely many passive input
and interior-time evaluations to the oracle still leaves a fixed finite
program. The identification is of the recomputed population parameter
interpolant, not of an interpolation of output values.

The approximation order at proof lines 1313–1321 is sufficient. For a
desired error, first choose a cutoff making the Gaussian remainder small,
then a finite law and a proof mesh making their errors small, and only
then take the actual width large and actual step small. This gives
convergence along every stated simultaneous sequence without a relative
growth constraint. No cross-width or finite-to-population operator-norm
distance is used.

### 7. Risks, replacement, and exact expectation order

The loss integrands have a uniform Lipschitz bound on the joint observation
space, using bounded predictors and their input Lipschitz constants. This
passes both the finite training loss and the population risk to the same
limiting risk uniformly in time in probability. The proof only uses the
high-probability initialization ball; it does not need an expectation bound
for the finite network outside that event.

The elementary finite-partition proof of empirical W1 convergence works
for arbitrary atomic, singular, or correlated observation laws. The
reference-program errors depend only on its fixed law and initialization,
so a union bound with the empirical-law event establishes the independent
iid case with arbitrary relative n, m, and step limits.

Replacing one observation changes empirical W1 by at most `(2+2Y)/m`.
The unspecialized cutoff estimate with R proportional to `sqrt(log(em))`
proves the asserted replacement bound directly, without relying on
monotonicity of a particular displayed enlarged modulus. The finitely many
small sample sizes are covered by the bounded-prediction estimate.

I checked the ghost exchange (A12): exchanging the iid pair `(Z_i,Z_i')`
turns the test loss of `f_S` at `Z_i'` into the loss of `f_(S^(i))` at
`Z_i`. Subtracting the original training loss then invokes sample
replacement at the same test observation. Bounded loss and continuity of
the empirical-law predictor map justify measurability and expectation.
The proof bounds the absolute value of the expectation at each
deterministic time, then takes the supremum of those bounds. It establishes
exactly `sup_t |E gap_t|`, not `E sup_t |gap_t|` or `E |gap_t|`.

### 8. Actual finite-time activity and paired observations

I independently checked the coefficients for the reference with two
orthogonal inputs, equal labels `y0=Y/2`, and `p=y0/2`. Its two lower
activations have covariance `q0 I_2`, and the first initialized forward
calculation makes the upper Gaussian coordinates independent with variance
q0. This is an initial Gaussian calculation, not a replacement of a
trained matrix by an independent matrix.

With the notation of Part IV, the readout derivative is `2S`, so
`c(t)=2tS+o(t)` and `delta_a^2(t)=2tU_a+o(t)`. The lower derivative then
integrates to `Z_a^1-g_a=2t^2 T_a+o(t^2)`, and the middle increment is
`2t^2 sum_b p U_b tensor h_b+o_op(t^2)`. The two contributions to upper
preactivation motion are both retained, giving
`2t^2[p q0 U_a + A0 C_a]+o(t^2)`. The bounded-multiplier argument and
the scalar integral identity for the tanh difference justify the
activation expansions in L2 along the existing strong trajectory. No
formal series is being used as an existence theorem.

Adjunction gives
`<h_a,P_a> = p E[xi_a tanh(xi_a) sech^2(xi_a)] > 0`.
Independence and oddness kill the other-input term, and the remaining
nonnegative integrand is strictly positive almost surely. Hence P_a and
`C_a=p sech^4(g_a) P_a` are nonzero. For the upper layer, identity (9)
is the sum of nonnegative quantities with a strictly positive term, so the
upper activation coefficients cannot all vanish. This proves positive
averaged activity in both layers, including the upper layer where either
one of the two preactivation contributions alone would be insufficient to
exclude cancellation.

The actual-flow asymptotic `A_ell(t)=2c_ell t^2+o(t^2)` makes the specified
positive t0 well-defined. Its margin j0 is positive. The paired displacement
continuity estimate then gives a relative open W1 neighborhood retaining
both margins. Spreading the atoms on small arcs and label intervals gives
nonatomic members; perturbing one angle gives nonorthogonal, correlated
members. No uniform positive activity is claimed outside this neighborhood.

For finite networks, the observable includes the same neuron's initial and
current activations. Both appear in the same fixed oracle program, so joint
second moments identify the squared difference. The same-width state
comparison, input-law transport, and time/input nets yield (A15), not merely
predictor convergence. The positive population margin and a union bound
over the two layers then imply the claimed finite-width probability result.

## Boundary-case audit

| Attack | Outcome |
|---|---|
| Arbitrary atom counts or arbitrarily small positive weights | The response pulse keeps its own weight; all aggregate bounds use weights summing to one. Constants remain uniform. |
| Zero-weight atoms | They can be deleted without changing the law or dynamics. |
| Coincident or repeated inputs; conflicting labels at one input | No inverse input Gram appears. The law formulation and residual integral retain label variation. |
| Singular or zero Gaussian query Grams | Fresh-input regularization and covariance-square-root continuity cover them; no rank-stability assumption is used. |
| One active input and passive first directions | The full Gaussian row is present, and passive predictions are obtained from the same bounded action and row. |
| Zero signal / zero conditional label mean | The zero-readout population state can be stationary; the theorem makes no universal activity assertion. |
| q=0 | The Gaussian cutoff remainder tends to zero, giving full-state equality. |
| q>1 | Uniform state/prediction bounds replace the logarithmic modulus. |
| m=1 and other small m | A bounded-prediction estimate and enlargement of a Y-dependent constant cover them. |
| Actual random finite readout | Its exact squared RMS expectation is n^-2; the proxy retains it and propagates its vanishing error. |
| Arbitrarily ordered width/sample/step limits | Only the fixed reference program is identified probabilistically; deterministic transport handles the growing actual program. |
| Paired initial/current activation observations | Joint oracle second moments retain the required pairing and give the displacement limit. |
| Activity at a specified positive time | The time is defined from a valid actual-flow asymptotic and is independent of width, sample count, and GD step. |

## Required corrections, optional suggestions, and limitations

Required corrections: **none**.

I have no optional presentation suggestion that is necessary to assess the
mathematics. Several parts deliberately repeat hypotheses and distinguish
their dependencies; those repetitions do not create an inconsistent claim.

This review establishes acceptance of the proof in its stated positive
local-time scope. It does not turn the result into a quantitative
finite-width rate, a finite-width sample-replacement theorem, a bound on
the expected absolute generalization gap, an excess-risk result, useful
fitting, feature-learning superiority, a global-time theorem, or a
finite-dimensional autonomous closure. Those statements are neither proved
nor claimed. The constants defining the positive activity time and margin
are mathematical quantities from the reference flow, not numerical lower
bounds. No training computation was used to support them.

Final decision: **ACCEPT R1 as a complete proof of the frozen theorem.**
