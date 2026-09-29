# Width-uniform response-memory bounds

**Direct quantitative closure attempt (28 September):**
[DIRECT_CLOSURE_QUANTITATIVE_ATTEMPT.md](DIRECT_CLOSURE_QUANTITATIVE_ATTEMPT.md)
records the completed direct-route estimates and their precise limit.
[DIRECT_CLOSURE_CLOCK_STABILITY.md](DIRECT_CLOSURE_CLOCK_STABILITY.md)
proves comparison of paired reconstructions under different actual clocks
with constants independent of order, and an all-time residual L1 resolvent
driven by source total variation.
[DIRECT_CLOSURE_EMPIRICAL_RATE.md](DIRECT_CLOSURE_EMPIRICAL_RATE.md)
proves root-width reference empirical covariance bounds for all learned
moment contractions without an order factor, including random clocks.
These do not yet construct the joint quantitative law of the initialized
forward/transpose actions. The original all-time predictor theorem retains
its qualitative width remainder; the `epsilon^(-5/2+o(1))` corollary remains
unproved. No maintained paper or book statement was changed.

**Common-width comparison and direct closure route (28 September):**
[RELATIVE_COMPLEXITY_UNKNOWN_WIDTH.md](RELATIVE_COMPLEXITY_UNKNOWN_WIDTH.md)
proves the relative moving-state count at a common sufficient width:
dense/closure is asymptotically `n/(2mq)`. Existence of an unknown
common width function does not determine an epsilon-power gain or the
minimum required widths. [DIRECT_CLOSURE_WIDTH_ROUTE.md](DIRECT_CLOSURE_WIDTH_ROUTE.md)
derives the finite-order empirical interactions and the exact order-uniform
moment-energy identity. These favor a direct closure width proof, while
adaptive fixed-matrix reuse, moving-clock comparison, and the growing-order
width constants remain explicit obligations.

**Second quantitative width attempt (28 September):**
[PREDICTION_WIDTH_SECOND_ATTEMPT.md](PREDICTION_WIDTH_SECOND_ATTEMPT.md)
proves an exact all-time prediction comparison through residual-weighted
two-time forward correlations, with no additional label restriction.
New nonlinear Gaussian-return, Hilbert-history feedback, and same-matrix
third-query comparisons are proved in the linked scoped notes. They do
not yet supply the joint trained forward/transpose law. The requested
`epsilon^(-5/2+o(1))` numerical moving-state corollary remains unproved;
the qualitative width remainder is not assigned a root-width rate.

**Quantitative width follow-up (28 September):**
[QUANTITATIVE_WIDTH_ATTEMPT.md](QUANTITATIVE_WIDTH_ATTEMPT.md) records the
focused attempt to prove the `epsilon^(-5/2+o(1))` moving-state corollary
under exactly the small-label hypotheses. It remains unproved. New
initialization, stopped-response, Gaussian-return and iid-history
covariance estimates are derived, but a quantitative trained same-matrix
response comparison is still missing. The current numerical width
remainder must not be replaced by an assumed root-width rate.

**Latest small-label result (28 September):**
[ACTIVATION_NEAR_QUADRATIC_ALLTIME.md](ACTIVATION_NEAR_QUADRATIC_ALLTIME.md)
extends the unchanged old-clock closure's
`C q^-2 exp(K sqrt(log(e+q))) + b_n` all-time bound to layer-dependent
C1,1 activations with globally bounded slopes and globally Lipschitz
derivatives. Activation values can be unbounded; softplus, GELU, SiLU,
unit ELU and softsign are included alongside tanh. Constants are independent
of width/order/time, and the dense-only remainder `b_n->0` in probability.
The hypotheses retain fixed depth/data, Gaussian initialization, zero
readout, a positive initial feature-Gram gap, and sufficiently small fixed
labels. Whole-input test bounds hold for every finite-second-moment input
law. This includes the tanh predecessor
[NEAR_QUADRATIC_ALLTIME_BOUND.md](NEAR_QUADRATIC_ALLTIME_BOUND.md).
Exact quadratic order, numerical width rates, exact ReLU, and arbitrary
unbounded local derivative moduli remain outside the proved extension.

User request: determine whether the width dependence can be removed from the constants in the response-memory theorems in `paper/main.tex`, and strengthen the paper only if a complete argument supports it.

This is a new theoretical investigation. Its authorized paper inputs are the current `paper/main.tex` and `paper/comparison_appendix.tex`; maintained `docs/` material may supply relevant established dependencies. No other studies, inherited reviews, training experiments, or literature campaign are inputs. The first attempt was local; a second focused proof round uses independent routes with selected paper/book inputs, as recorded below.

## Contract

- Preserve arbitrary fixed depth, nonlinear feature learning, the canonical block mobilities, paired response-memory algorithm, and finite training data.
- First test the theorem's literal unnormalized parameter error; separately investigate normalized parameter and predictor error, explicitly distinguishing any change of target.
- Seek constants and sufficient-order thresholds independent of width on each prescribed finite horizon, with initialization/regularity assumptions declared uniformly rather than hiding width in a norm bound.
- Analyze both residual-speed and joint clocks. Do not change the joint clock silently.
- Distinguish deterministic bounds for the theorem's arbitrary initializations from high-probability Gaussian-initialization bounds.
- Authorized work is theoretical derivation and deterministic algebraic verification. No new network-training campaign is authorized or needed initially.

## Initial state

The fixed-width proofs supply an `O(P^-1)` or `O(P^-2)` bound but use width-dependent Euclidean compact balls and feedback constants. Appendix E already has a dimension-free joint projection estimate conditional on bounded normalized response variation and feedback stability.

Investigate, in order: (1) replication/normalization obstruction; (2) width-uniform production of the memory defect for bounded activations; (3) the remaining feedback-stability estimate in population-scale norms. Preserve partial results and distinguish a failed proof route from a counterexample to prediction approximation.

## Results of this attempt

The complete derivations are in [WIDTH_UNIFORM_ANALYSIS.md](WIDTH_UNIFORM_ANALYSIS.md).

| Claim | Current status |
|---|---|
| Width-independent raw-parameter theorem over arbitrary initializations with uniform population-scale bounds | Falsified for the learning-speed closure: replicated two-layer tanh networks have nonzero fixed-order outer error growing as sqrt(n). |
| Width-independent learning-speed accumulated absolute velocity defect | Proved under bounded activations/slopes and uniform initial operator/readout RMS bounds; rate O(P^-1). |
| General autonomous normalized trajectory and test-prediction approximation | Qualitative convergence uniform over all widths; width-first rate with every exponent below two for zero limiting readout. Locally unconditional in the Gaussian model; longer horizons use explicit dense-only carrier regularity. A simultaneous all-width C_T/P rate remains open. |
| Uniform Lipschitz feedback from operator/RMS bounds alone | Falsified as a proof route by a same-activation concentration example. This does not disprove Gaussian-typical predictor convergence. |
| Original joint clock, uniform O(P^-2) full tracking in the intended Gaussian setting | Open: Appendix E's normalized-variation source estimate still needs uniform variation, stability, and continuation. |
| Finite total activity and fitting of the old closure | Proved for every order in a small-label regime with an initial feature-Gram gap; the latest endpoint argument strengthens this to exponential residual decay uniformly in width and order. Canonical Gaussian initialization supplies the initial gap with probability tending to one. Arbitrary-label, all-order Gaussian fitting remains open. |
| Joint width/order tracking with labels of RMS at most one | Proved on every compact time interval, at any fixed depth and for arbitrary finite data, without a Gram-gap or fitting assumption. A sufficient order grows exponentially in sqrt(n); the resulting C_T/P constant is width-independent on this joint region. |
| All-time joint width/order tracking without small labels | Proved for one sample, any fixed depth, initial feature norm bounded below, and zero or sufficiently small initial readout, including the canonical vanishing Gaussian readout. Every sufficiently large order fits; an explicit exponential-in-sqrt(n) order schedule gives C/P tracking for all time, uniformly over abs(y)<=1. The multi-input all-time extension remains open. |
| Activation-general multi-input small-label theorem | Proved for layer-dependent C1,1_loc activations with globally bounded slope, including unbounded activations. Fitting is exponential for every P with width-independent small-label threshold; all-time C/P tracking holds under joint P,n scaling using the local gate-Lipschitz modulus. Standard globally Lipschitz-gate activations preserve the tanh order scaling. |

The newest results and their different horizon/data scopes are in
[UNIT_LABEL_JOINT_ORDER.md](UNIT_LABEL_JOINT_ORDER.md) and
[UNIT_LABEL_SINGLE_SAMPLE.md](UNIT_LABEL_SINGLE_SAMPLE.md). They do not
prove a bound uniform over all unrestricted width/order pairs. The new
one-sample alignment invariant removes label smallness without assuming
dense fitting, and works at any fixed depth; this is stronger in label range
and depth than the earlier special scalar result, but its certified joint
order is much more expensive.

The latest general-case continuation is summarized in
[GENERAL_AUTONOMOUS_SYNTHESIS.md](GENERAL_AUTONOMOUS_SYNTHESIS.md). It proves
qualitative convergence of the original autonomous old-clock closure uniformly
over all finite widths, and a width-first C_T/P rate, for arbitrary fixed depth
and correlated finite data. A further width-first sharpening gives every
exponent strictly below two. These statements are unconditional on the local
Gaussian-population interval, and extend to prescribed longer intervals under
explicit dense-only Gaussian carrier regularity. The simultaneous all-width
C_T/P rate remains open. The earlier one-sample, two-hidden-layer result below
still supplies a stronger finite-width quantitative bound in its narrower scope.

These are study-level theoretical results with the internal checks specified
below, not promoted results. The original paper theorems are preserved: the
new limit-order statements do not justify simply deleting the width dependence
from the existing finite-width theorem. The remaining target is quantitative
uniformity in finite width at the stated memory-order rate.

## Verification

`check_width_algebra.py` performs deterministic algebra checks only: it compares the full finite-network vector field with the exact replicated scalar reduction, checks the initial projected-endpoint derivatives at several orders, and checks the concentration example against the full matrix formula. It runs no training or trajectory integration.

Executed successfully from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python -B studies/response_memory_width_uniform_20260927/check_width_algebra.py \
  --output data/generated/response_memory_width_uniform_20260927/algebra_01/results.json
```

Maximum checked matrix/scalar discrepancy was `2.22e-16`; the nonzero readout-error cubic coefficient is approximately `-0.0480306554`. Results and input/source hashes are retained under `data/generated/response_memory_width_uniform_20260927/algebra_01/`. The proof of the universal statements is the analytic derivation, not these finite numerical checks.

The first attempt used no agents, manuscript edits, commits, external searches, or network-training experiments. The second round below used three independent scoped agents. Only current paper inputs, designated instructions/skills, and the relevant maintained book passages were read. The book's scoped tail estimates were not silently transferred to the all-depth theorem.

## Second round: dense-limit regularity only

The user clarified that the desired theorem may assume existence and suitable explicitly stated regularity of the dense population flow, but may not assume closure bounds, finite-width feedback estimates, or other conclusions that the proof is meant to establish. The target remains the original order exponent (old P^-1 or joint P^-2) with both the constant and sufficient-order threshold uniform in width. The user's experimental observation motivates this claim but is not a proof premise.

Independent scoped routes, without inherited discussion or access to each other's results:

- `uniform_old_clock`: old-clock feedback and finite-width transfer; writes `OLD_CLOCK_ROUTE.md`.
- `uniform_joint_clock`: joint-clock/reference-oracle approach; writes `JOINT_CLOCK_ROUTE.md`.
- `uniform_limit_logic`: sufficiency of population regularity and network-specific obstructions; writes `LIMIT_REGULARITY_ROUTE.md`.
- Coordinator: investigate reference propagator control and distinguish admissible dense-limit regularity from assumed finite-width stability.

No manuscript or book edits are authorized by a failed proof attempt. Mathematical claims will be reconciled before any strengthened theorem is accepted. This round runs no training and does not broaden the literature search.

### Second-round outcome

The requested width-uniform trajectory theorem was **not proved**. The conditional theorem from the first round is not treated as an answer to the tightened request. The current paper's theorems and their width dependence remain unchanged.

The coordinator read all three complete reports and checked the normalization, projection-energy argument, and scope of their counterexamples against the current manuscript. The principal positive result is in [OLD_CLOCK_ROUTE.md](OLD_CLOCK_ROUTE.md): for tanh, any fixed finite depth and training set, the actual old-clock closure continues for every order, its physical bounds are uniform on bounded initialized-operator/readout-RMS sets, and its accumulated absolute velocity defect is at most `C_T/sqrt(P(P+1))`. The proof does not assume closure stability, bounded closure trajectories, or convergence of a population closure. An elementary Gaussian operator-norm bound gives uniform moments of this consistency constant under the prescribed initialization.

[JOINT_CLOCK_ROUTE.md](JOINT_CLOCK_ROUTE.md) also derives uniform physical bounds and variation, and a `C_T/P^2` accumulated-defect bound for the unchanged joint clock with two hidden layers, stopped before the residual falls below a fixed positive value. The stopped qualification and two-hidden-layer restriction are essential; this is not the requested full tracking theorem.

[LIMIT_REGULARITY_ROUTE.md](LIMIT_REGULARITY_ROUTE.md) proves a raw-parameter counterexample with zero initial readout: replication preserves the dense and old-clock scalar dynamics, while every nonzero scalar readout discrepancy is multiplied by `sqrt(n)` in the paper's unnormalized norm. Its explicit small-time coefficient is nonzero for every fixed finite order. This refutes an unrestricted width-uniform strengthening in that norm, even with an exact smooth dense population limit. It does not refute a predictor or normalized-parameter theorem, and it does not use the canonical independent Gaussian initialization.

The same report constructs a stationary dense tanh family with convergent operators and response fields but diverging positive variational eigenvalues. Both closures are exact on that family. Its role is solely to disprove the inference from regular dense paths to uniform stability against arbitrary perturbations. The old-clock report separately shows that a fixed-radius normalized tube around Gaussian initialization can contain states with an unbounded positive Jacobian quadratic form; these states are not shown to be reached in training.

The unresolved obligation is to control amplification of the **actual structured memory defect**, or bypass such an estimate, while retaining the order exponent. Neither dense population existence nor smoothness of its path supplies that control. Proposed oracle/tail and response-adapted-metric routes are recorded as incomplete; no population-to-finite-width transfer, exchange of limits, Gaussian prediction counterexample, or complete negative theorem for normalized tracking is asserted.

## Dense-driven oracle follow-up

The user next proposed isolating the matrix-compression error in an oracle
whose hidden matrices are reconstructed from the dense flow's histories.
The complete derivation is in [DENSE_DRIVEN_ORACLE.md](DENSE_DRIVEN_ORACLE.md);
an independent scoped derivation of the pass/gradient estimates is in
[DENSE_ORACLE_BACKPASS.md](DENSE_ORACLE_BACKPASS.md). The scoped agent read
only the current paper, comparison appendix and notation, then received the
coordinator's zero-readout and one-input transform proposals for checking.

The oracle must be distinguished from the autonomous closure:

- With the dense first layer and readout copied, arbitrary fixed-depth matrix
  approximation gives uniform test-function approximation by a direct forward
  recurrence, without temporal feedback.
- For two hidden tanh layers and zero initial readout, both dense old-clock
  histories are H1, including their prefixes. Their derivative bounds are
  derived from the dense equations. The paired projection therefore has
  **O(P^-2)** matrix error even with the old clock. Its fully recomputed forward
  and backward passes, predictions and gradient diagnostics have the same
  width-independent rate. This extends to any fixed finite training set.
- A nonzero initial backward history requires its prefix jump to be retained.
  The note proves a smooth O(P^-2) term plus a jump-amplitude O(P^-3/2) term;
  zero population readout removes that jump.
- For **one normalized training sample and two hidden tanh layers**, the oracle
  can evolve its own first layer and readout while receiving its middle matrix
  from dense histories. The change of variable
  G(u)=u/2+sinh(2u)/4 cancels the first-layer gate. Readout bounds, a clipped
  existence argument and a uniform Lipschitz estimate in these transformed
  coordinates give actual outer-weight and test-prediction error O(P^-2)
  throughout [0,T], with constants independent of width. No oracle closeness
  or stability assumption is made. This is a proved restricted oracle result;
  it is not an arbitrary-data or arbitrary-depth closure theorem.
- At larger depth, a dense carrier path continuous in L2 gives convergence of
  the copied-outer-weight oracle's backpass by compactness/uniform
  integrability. A numerical rate requires quantitative reference tails.

The coordinator checked the complete independent report and the scalar
transform, projection constants, normalization, and readout-energy identity.
These are analytic checks, without new training or numerical integration.
The general width-uniform autonomous tracking result remains open and the
manuscript has not been changed.

## Shared residuals and the reference-gate oracle

The user next asked for shared dense residuals and a common clock, then
explicitly allowed choosing the oracle definition to isolate difficult
feedback and approach the core theorem. The chosen all-depth oracle records
its **own** histories and reconstructs its own learned matrices, while
receiving dense residuals, the dense old clock, and **dense neuronwise
activation slopes in its backward pass**. The last item is an explicit
additional oracle input. Supplying residuals alone has not been proved to
control arbitrary correlated-input feedback.

The complete construction and proof are in
[SHARED_RESIDUAL_GATE_ORACLE.md](SHARED_RESIDUAL_GATE_ORACLE.md).
It proves global existence of this oracle for every order, a dimension-free
accumulated velocity-defect bound, and a derived common-gate Lipschitz
estimate. Their combination gives normalized parameter and test-prediction
error O(P^-1), uniform in width on every prescribed finite horizon, for any
fixed depth and finite training data with tanh activation. Its constants
depend on initial operator/readout RMS bounds, data, depth and horizon;
no oracle stability or closeness assumption is used.

Section 8 further restores the oracle's own residual and its own old clock
while keeping the dense backward gates. Readout energy bounds and an explicit
residual Lipschitz estimate prove the same width-uniform rate. Thus residual
and old-clock feedback can be handled for this supplied-gate oracle.
Restoring the oracle's own backward gates remains the core unresolved step;
the note gives the exact dense-carrier gate remainder to be controlled.

[SHARED_RESIDUAL_MULTIINPUT.md](SHARED_RESIDUAL_MULTIINPUT.md) contains the
scoped agent's complete independent calculations for residual-only forcing,
including the orthogonal-input result, the remaining correlated-input term,
and its subsequent check of the chosen shared-gate construction. The
coordinator read the complete report and checked the projection-energy
recursions, normalization and common-gate stability coefficients. These are
internally analyzed oracle results, not an autonomous closure theorem or a
promotion review. No new training, literature search or manuscript changes
were made.

## Restoring learned-interaction gate feedback

The user requested a strictly stronger width-uniform result with less oracle
intervention. Two steps were completed:

1. [TOP_GATE_RESTORATION.md](TOP_GATE_RESTORATION.md) removes the entire dense
   top-layer backward gate for bounded initial readout (including zero and
   uniform-probability events for the canonical small Gaussian initialization).
   The closure already uses its own residual, old clock and histories.
2. [LEARNED_GATE_RESTORATION.md](LEARNED_GATE_RESTORATION.md) restores the
   closure's own gate on **every learned backward interaction**, keeping dense
   gates only on initialized branches. This uses only the prior RMS-readout
   and initialized-operator assumptions. At zero readout the top dense gate
   disappears entirely. It proves O(P^-1) normalized parameter and test-output
   error, uniformly in width and over each compact horizon, for arbitrary
   fixed depth and finite correlated training data.

The new mechanism is a proved dense-reference bound:
the exact learned adjoint maps L2 to L-infinity with norm at most
2S beta_l, because its adjoint history uses bounded forward activations.
This controls the changing gate on the learned branch. The comparison is
only against the dense reference; it does not assert Lipschitz continuity
between arbitrary physical states.

Population existence is proved through inactive clipping of forward moment
coordinates in the backward calculation, and of the learned readout increment.
The history representation bounds those coordinates before any backward
estimate, making the clipping inactive and avoiding a circular stability
assumption. The source-defect proof is unchanged because it requires no
backward-gate derivative.

[TOP_GATE_CHECK.md](TOP_GATE_CHECK.md) contains the scoped agent's full analytic
check of both steps, including the exact difference recursion and existence
argument. The coordinator read the complete report and reconciled its sharper
constants with the stated looser constants. No substantive correction was
needed. These are internally checked oracle results, not a promotion or a
proof of the fully autonomous closure. The remaining gate forcing is confined
to the initialized backward carriers W_0^*delta (and the initial readout
component if nonzero). No manuscript edits, training or Git operations were
performed.

## Autonomous continuation, 28 September

The user asked to remove further oracle intervention and pursue the main
width-uniform theorem. Three bounded analytic routes were assigned separate
files in this existing study; none launched training, edited the manuscript,
or performed Git operations:

- `autonomous_one_sample`: the complete old-clock consistency result,
  dense-oracle coordinate transform, current paper and notation were its
  selected scientific inputs. It wrote
  [AUTONOMOUS_ONE_SAMPLE.md](AUTONOMOUS_ONE_SAMPLE.md).
- `tail_oracle`: the learned-gate oracle, old-clock consistency,
  supplied-gate oracle and notation were its selected inputs. It wrote
  [TAIL_ORACLE_ROUTE.md](TAIL_ORACLE_ROUTE.md).
- `energy_stability`: the learned-gate oracle, old-clock result,
  limit-regularity diagnostics, current paper and notation were its selected
  inputs. It wrote [ENERGY_STABILITY_ROUTE.md](ENERGY_STABILITY_ROUTE.md).

Each route began without inherited conversation or access to the other active
routes. The coordinator later sent the proposed P^-2 refinement to the
one-sample author, who had independently derived it before receiving that
message. Their agreement is disclosed in the candidate. The coordinator also
checked the maintained book's reference-only tail and Osgood passages in
`docs/05-continuation-boundaries.qmd`; their scoped assumptions were not
imported as a general Gaussian tail theorem.

### Complete autonomous result

For one normalized training input and two hidden tanh layers, the **actual
fully autonomous old-clock closure** exists globally at every order and
tracks dense training in normalized parameter norms and on bounded test-input
sets with error

`C_T [1/(P(P+1)) + ||delta_0||_RMS/(P sqrt(P+1))]`.

No dense gates, responses, residuals or clock are supplied. No closeness or
feedback-stability assumption is made. At zero initial readout the rate is
O(P^-2), despite using the old clock. For the canonical finite Gaussian
readout the bound becomes O(P^-2 + n^-1 P^-3/2) on common initialization
events with probability tending to one. All constants are independent of
width and order on those events.

The proof uses the first-layer coordinate
`G(u)=u/2+sinh(2u)/4` to cancel its backward gate. Its inverse is Lipschitz.
Readout energy bounds yield a bounded top multiplier. The old-clock squared
defect estimate gives a uniform H1 bound for the closure's own top backward
history, so the two history tails multiply to give the sharper rate. Shifted
G coordinates and an inactive readout clip construct the population system
for a given bounded initialized operator. Identification of the canonical
Gaussian width limit is a separate dense/source theorem, not a claim made
by this construction.

[AUTONOMOUS_SCOPE.md](AUTONOMOUS_SCOPE.md) gives the coordinator's scope
reconciliation, explicit Gaussian event calculations and the noncommuting
first-layer vector fields that obstruct simply applying the same coordinate
trick to correlated inputs. This is an obstruction to that trick, not to the
general approximation theorem.

### What remains at general depth and data

The tail route constructs a strictly weaker oracle intervention: own gates
act on every learned carrier and on the clipped portion of every initialized
carrier; dense gates act only on initialized-carrier overflow. Its uniform
bound is `C_comp exp((a+bM)T)/sqrt(P(P+1))`, with `a,b` independent of width,
order and clipping threshold M. For each regular population reference,
taking M to infinity slower than log P makes both error and remaining oracle
velocity intervention vanish. It does not prove that the autonomous closure
follows this oracle. Uniform disappearance across widths additionally needs
uniform reference tails.

For the autonomous general closure, the proved comparison contains the
amplified reference tail `exp((a+bM)T) H_T(M)`. Qualitative L2 continuity,
even unspecified finiteness of every moment, does not control this product.
The tail and energy reports derive Osgood comparison statements under
explicit stronger dense-tail hypotheses, without claiming those hypotheses
for arbitrary trained Gaussian networks. The energy route also proves an
unconditional O(P^-1) bound on total positive variation of the closure's
loss, for general fixed depth/data. This is approximate dissipation, not
dense-loss tracking.

The complete arbitrary-depth, correlated-input width-uniform tracking
theorem, retaining the original clock rates, is still open. This attempt
does not turn a special-case theorem or vanishing oracle intervention into
a claim that the broad target has been resolved.

### Check status

The full autonomous candidate was frozen at SHA256
`571c6eb4a31ae7195441713c584d5d3a87208be9c48b68927aa0145f717cd7a8`
before the energy-route agent was assigned a separate complete check.
The coordinator independently read every candidate proof section and the
complete tail and energy reports. The separate check is recorded in
[AUTONOMOUS_ONE_SAMPLE_CHECK.md](AUTONOMOUS_ONE_SAMPLE_CHECK.md) and passed
the complete stated theorem, including all constants, population continuation,
residual sign, both prefix cases and the Gaussian specialization. The
coordinator read that report in full. Its one exposition suggestion, the
reverse chain rule proving uniqueness in original coordinates, is explicitly
derived in the check and in `AUTONOMOUS_SCOPE.md`; it requires no new
assumption. The frozen candidate remains unchanged. These are study-level
analytic checks, not a promotion review or a change to the paper's theorem.

Check scope: these are internally analyzed proof attempts, not promotion reviews. The previous deterministic algebra evidence remains attached to its original examples; the second round's zero-readout expansion and stationary Hessian are analytically checked, not new training experiments. Main manuscript source hashes used were `a1d861c53a76959bd607aeb03cec39639b522bf48014a14cda597ef9b856c386` (`paper/main.tex`) and `688ad303f35f0cace7a4db0ca1015ae1bd4b7678fc66049a900790453b0e1c0e` (`paper/comparison_appendix.tex`), at HEAD `7ffb91ff331711756f7cb3b657c4102c8e018623`.

## General depth and correlated data: the next continuation

The user requested a stronger attempt at the general case. Three fresh scoped
routes began with selected current study and maintained book inputs, without
inherited conversation or each other's active work:

- `general_gaussian_transport` wrote
  [GENERAL_GAUSSIAN_TRANSPORT.md](GENERAL_GAUSSIAN_TRANSPORT.md), using the full
  local canonical Gaussian population proof and fixed-program specializations.
- `general_reference_projection` wrote
  [GENERAL_REFERENCE_PROJECTION.md](GENERAL_REFERENCE_PROJECTION.md), initially
  deriving signed reference consistency and an absorbable projection remainder.
- `general_geometric_stability` wrote
  [GENERAL_GEOMETRIC_STABILITY.md](GENERAL_GEOMETRIC_STABILITY.md), proving the
  top-link defect improvement for arbitrary samples, bounded learned-adjoint
  outputs, and a controlled-metric obstruction with its scope explicitly limited.

Candidates were frozen before cross-route synthesis. The coordinator then
derived the missing temporal regularity from the dense Gaussian carrier tails:
dense parameter Lipschitz continuity gives a backward-source modulus
`h sqrt(log(e/h))`. This avoids assuming dense-source bounded variation or
transferring derivatives from population to finite trained networks. Both
projection and Gaussian routes completed the finite-program reference bridge.
The final mechanism smooths only the source factor of `a_D/rho_hat`, retaining
the actual scalar reciprocal residual in H1. No supplied residual, gate, clock
or history is used by the implemented closure.

### Precise new results

For arbitrary fixed depth and arbitrary finite correlated data, let `e_nP` be
the supremum on the time interval of first-row RMS plus hidden Frobenius plus
readout RMS discrepancy between the autonomous closure and same-initialization
dense flow.

1. **Qualitative convergence uniform over every finite width:** for every
   `epsilon>0`, `lim_(P0->infinity) sup_n Pr{sup_(P>=P0) e_nP>epsilon}=0`.
   This covers arbitrary joint width/order sequences with order tending to infinity.
2. **Width-first quantitative convergence:** for each fixed order threshold,
   the probability that `sup_(P>=P0)e_nP` exceeds `C_T/P0+zeta` tends to zero
   as width tends to infinity, for every `zeta>0`.
3. **Sharper width-first envelope at zero limiting readout:**
   `C_T P0^-2 sqrt(log(e+P0)) exp(C_T sqrt(log(e+P0)))`, hence
   `C_(T,gamma) P0^-gamma` for every fixed `0<gamma<2`.
4. Forward recursion transfers these results to the entire prediction function
   on bounded test-input sets and to test-function RMS discrepancies.
5. A finite-head/tail deduction gives `e_nP <= C_T/P + a_n(T)` simultaneously
   over P, with `a_n(T)->0` in probability. No quantitative rate in width for
   this floor is claimed. The same conclusion holds with each exponent below
   two and its corresponding constant/floor.

The complete synthesis, proofs of the extra deductions and scientific scope are
in [GENERAL_AUTONOMOUS_SYNTHESIS.md](GENERAL_AUTONOMOUS_SYNTHESIS.md).

These results hold without extra assumptions on the local interval of maintained
C.1--C.2. On a longer prescribed interval the explicit permitted dense regularity
is a uniform exponential-square moment for the dense backward carriers. An exact
Gaussian innovation plus a bounded response-history term is sufficient; bounded
response-measure total variation supplies the latter for tanh. Mere strong L2
existence does not assert this stronger regularity. The proof assumes no trained
finite-network tails, no closure stability, and no fixed-order population-closure
existence theorem.

The core finite-width rate remains distinct: neither the qualitative supremum
over widths nor the width-first rate proves a uniform bound on `P e_nP` over
all widths. The fixed-program transfer supplies no quantitative relation between
its required width and projection order. The unchanged joint-clock P^-2
width-uniform theorem also remains open. These limitations have not been hidden
inside a redefinition of C_T.

### Internal verification and preserved workspace

[GENERAL_UNIFORM_CONVERGENCE_CHECK.md](GENERAL_UNIFORM_CONVERGENCE_CHECK.md)
passes the complete qualitative theorem and conditional whole-horizon extension,
including its Frobenius upgrade and all-width/all-order quantifiers.
[GENERAL_ENDPOINT_CHECK.md](GENERAL_ENDPOINT_CHECK.md) separately checks the
appended endpoint proof and records its exact source hashes and scope. The
coordinator read the full route reports and the relevant complete maintained
local-population, Gaussian-source, fixed-program and common-action proofs.
Subsequent sharpening/check additions are recorded in that check rather than
retroactively attributed to the earlier frozen review.

The completed endpoint check passes the exponent-below-two sharpening,
the simultaneous vanishing width floor, and the compact-test-input deduction.
It checks synthesis SHA-256
`8ea4888e9874250e8386f32c492781dbc111fceda17ad5afc4e77a1b6980e735`
and records its own final report hash
`6b7314606231f2fccf8b7dc543bd54ffc7931f663d6c23dd65c0f75c3b1d419f`.
The coordinator read that completed check and incorporated its explicit
common-event qualification for deterministic prediction constants. A separate
Gaussian-route check also passes the sharper envelope. None of these checks
certifies an all-width quantitative rate or a joint-clock theorem.

No training, external literature search, manuscript edit, Git commit, branch
change or promotion was performed. Unrelated existing modifications were left
untouched. The remaining research task is a quantitative finite-program or
structured-defect argument that removes the finite-width floor at a width-uniform
order rate; it is not another restoration of oracle-supplied residuals or gates.

## Time uniformity and closure loss decay

The user next asked whether sufficiently fast loss decay makes the finite-time
constant bounded for all time, and whether compatible separated data guarantee
that decay for every finite closure. The relevant old-clock condition is
finite total residual RMS, integral sqrt(loss) < infinity; convergence of loss
to zero by itself is insufficient. An all-time trajectory bound additionally
needs justified feedback stability. It is not supplied merely by making the
clock length finite.

The new results and complete initial Gaussian Gram proof are collected in
[LOSS_DECAY_SYNTHESIS.md](LOSS_DECAY_SYNTHESIS.md).

- [LOSS_DECAY_ACTIVITY_BOOTSTRAP.md](LOSS_DECAY_ACTIVITY_BOOTSTRAP.md)
  proves a time-independent activity-cap estimate for the original autonomous
  old-clock closure. Its accumulated absolute velocity defect is C(S)/P while
  activity stays below S. With zero initial readout and small S, the feature
  Gram moves by O(S^2), C(S)=O(S^3), and the integrated residual forcing is
  O(S^4/P). A first-exit argument proves that every order P>=1 fits sufficiently
  small labels, with integral rho <= 3Y/(2 lambda_0). For initial readout RMS
  B_0<=Y, the corresponding bound is 3Y/lambda_0. The bounds are uniform in
  width on common initialized-operator and initial-Gram events. This proof
  establishes the needed integrability directly; no exponential rate is claimed.
- The synthesis proves the initialized population tanh feature Gram is positive
  definite for any fixed nonzero inputs with no proportional pairs. Finite-width
  initialized Grams converge to it in probability. Together with elementary
  Gaussian norm bounds, this makes the all-order, small-label activity theorem
  applicable with probability tending to one as width increases, using a
  width-independent label threshold and activity bound.
- At fixed width, convergence of dense flow to an interpolating parameter with
  positive readout Gram implies that all sufficiently high memory orders also
  fit and have finite total activity. This proves decay of those closures from
  a dense regular-fit hypothesis, without assuming closure decay in advance.
- [LOSS_DECAY_OBSTRUCTION.md](LOSS_DECAY_OBSTRUCTION.md) gives realizable
  orthogonal two-sample data and invertible hidden matrices for which every
  order remains at positive loss. The exact stationary initialization is
  exceptional under the canonical Gaussian law. Finite-horizon continuous
  dependence gives arbitrarily long Gaussian plateaus on open sets, not a
  Gaussian population obstruction or almost-sure failure theorem.
- In response to the user's saddle question, synthesis Section 6 proves the
  explicit stationary physical network is a strict saddle, and proves that
  analyticity and realizability exclude positive-loss local minima at zero
  readout more generally. It makes no universal landscape claim at nonzero
  readout. The scalar loss z^4 illustrates why absence of bad minima alone
  does not imply residual integrability.

The small-label restriction is substantive; arbitrary-amplitude nonlinear
feature-learning convergence for every order remains unresolved. The original
joint clock and general width-uniform all-time feedback estimates have not been
proved by these arguments. No paper or book theorem was changed.

Verification: the coordinator read both complete scoped reports and derived the
Gaussian initial-Gram lemma. The obstruction agent then read the full activity
proof and synthesis, checked all-order normalization and first-exit logic, and
checked both saddle arguments. Its one clarification was incorporated: the
Gaussian theorem uses a common deterministic defect majorant, obtained by
setting B_0=Y and every initialized hidden norm to 10 in the monotone recursions.
These are internal analytic checks, not independent promotion reviews.
No training, external search, Git change or maintained-manuscript edit was made.

## Small labels: joint width/time continuation

The user asked to complete the actual all-time C/P tracking bound with a
width-independent constant, using only the small-label regime already obtained.
The full arbitrary-depth, multiple-input rate remains **open**. This turn
does not count an all-time defect bound, a width-first theorem, or a
width-dependent small-label threshold as completing that target.

The reconciled result is
[SMALL_LABEL_ALLTIME_SYNTHESIS.md](SMALL_LABEL_ALLTIME_SYNTHESIS.md).
Three fresh scoped routes used selected current-study artifacts and the
current paper/book equations, without inherited discussion or other-study
inputs. They initially worked separately; the coordinator subsequently
supplied the scalar-clock comparison idea and coordinated explicit checks.

- [SMALL_LABEL_ENERGY.md](SMALL_LABEL_ENERGY.md) derives the coupled
  residual/parameter estimate for the actual general closure. Residual
  coercivity removes physical time from feedback growth. The only remaining
  term is the dense-activity integral of the initialized backward carrier
  times the actual gate difference. The elementary estimate gives
  C Y^3/P exp(CY+C sqrt(n)Y^2), with all width dependence displayed.
  A dimension-free correlation estimate for that term is still missing.
- [SMALL_LABEL_GAUSSIAN.md](SMALL_LABEL_GAUSSIAN.md), Sections 1--4,
  globalizes the dense Gaussian population construction at sufficiently
  small labels. It applies the maintained variable-step response proof
  in accumulated activity, using stopped population Euler programs.
  A relative Euler remainder and the readout Gram gap close the activity
  bootstrap before the continuous flow is constructed. This supplies
  global dense existence, exponential residual decay and uniform marginal
  Gaussian carrier bounds, not a trained finite-width tail theorem.
- The coordinator's deterministic tail-transfer lemma bounds the all-time
  discrepancy by A times its compact-time discrepancy, plus
  B Y exp(-lambda_0 T)+D/P. Together with the preceding dense construction
  and the study's established qualitative compact-time theorem, it proves
  **qualitative all-time convergence uniform in width and all larger orders**
  on the small-label initialization events. It does not prove that the
  sufficient order is proportional to inverse accuracy.
- [SMALL_LABEL_STRUCTURED.md](SMALL_LABEL_STRUCTURED.md) closes both
  uniformities quantitatively for **one normalized input and two hidden
  tanh layers**. Its rate is C/[P(P+1)] at zero readout and
  C(P^-2+n^-1 P^-3/2) for the canonical small Gaussian readout on common
  events of probability tending to one. Every order is covered. It
  compares paths in activity using the exact first-layer coordinate
  transform, then proves contraction of the two scalar physical clocks.
  This gives actual same-physical-time parameter and bounded-test-set
  prediction tracking, not an oracle or merely endpoint fitting.

The scalar sign of a one-sample residual and the two-hidden-layer gate
cancellation are essential to that last proof. The current paper's general
theorem has not been changed to claim this special-case result universally.
The unresolved general rate concerns finite-width correlations of the
actual approximation error with initialized backward responses.

Internal verification: the coordinator read all complete candidates and
the relevant maintained C.1--C.2 arguments. The energy route checked the
tail-transfer proof and complete signed-clock theorem, then separately
checked the small-readout extension. The structured route checked the
Gaussian candidate's complete Sections 1--4. Clarifications were applied:
explicit compact-time all-width/all-order quantifiers; lifting original
population solutions into the transformed coordinate; nonzero initial
readout bounds; one common space containing programs for all integer
horizons; and stopped finite-width comparison on arbitrary finite horizons.
These were internal analytic cross-checks, not promotion reviews.

Final coordinator-checked SHA-256 versions:

- Energy: f53e24682c7c51ea70b09570aa1c478822c48466d5b5aa8f5bca57d1827d9119
- Gaussian: 1d7cecbf36bea7c5ced2caf1d336d9d70d12db14ffb7a61bde44b580f998becb
- Structured: d42f7b71821eddfae756c1db996077b4b9389f7ec7ff473e2bd2a45cc0f62556
- Synthesis: f5a01b31860174734439590cf52fed11795fab62adc5ca367418ecbe44e34f28

No training, external search, Git operation, or maintained paper/book edit
was performed. Existing unrelated workspace changes were preserved.

## Further small-label attempt: exponential fitting and stronger consistency

The user requested another attempt at the simultaneous all-width, all-time
`C/P` trajectory bound. The full arbitrary-depth, correlated-input result
is **still not proved**. The following are new deductions, rather than a
repetition of the activity cap or a change to a supplied-response oracle.

[SMALL_LABEL_SPECTRAL_SLACK.md](SMALL_LABEL_SPECTRAL_SLACK.md) proves:

- The endpoint Legendre kernel has `L1` norm at most `C sqrt(P)`, with a
  self-contained Sonin-energy proof. Combined with the forward `H1`
  endpoint estimate `C/sqrt(P)`, it gives the actual pointwise defect bound
  `sum_l ||E_l||_F <= C Y^(5/2) rho`, uniformly in width, order, and time.
- Consequently `||J E||_m <= C Y^(7/2) rho`. Reducing the existing
  width-independent small-label threshold yields
  `rho_hat(t) <= rho_hat(0) exp(-lambda_0 t/2)` for every order and width
  on the original initialized-operator/readout/Gram events. This supersedes
  the earlier absence of a closure exponential-decay conclusion. It uses
  neither trained Gaussian tails nor a closure stability assumption.
- A terminal cutoff in the closure's own clock gives a stronger absolute
  velocity-defect bound:
  `C[B_0 Y^(3/2) P^(-3/2) + Y^(5/2) sqrt(1+nY^4+log(e+P)) P^(-2)]`.
  It handles the backward-prefix jump explicitly and requires no limiting
  normalized-residual direction or comparison of the two residual clocks.
- The actual trajectory error is bounded by this expression times
  `C exp(CY+C sqrt(n)Y^2)`. Thus a genuine all-time `C/P` bound holds on
  the expanding order/width range `sqrt(n)Y^2 <= c log(e+P)` for a
  sufficiently small fixed `c`. This range is not the requested uniform
  theorem over all widths. The complementary range still needs a
  quantitative finite-width correlation or transfer estimate.

Two independently started routes clarify why the remaining step is real:

- [SMALL_LABEL_STRUCTURED_GAIN.md](SMALL_LABEL_STRUCTURED_GAIN.md)
  derives the exact comparison energy and an explicit deterministic
  small-label tanh example with uniform Gram gap but prediction-tangent
  expansion of order `sqrt(n)Y^2`. The actual order-one memory defect
  reaches the exceptional coordinate. This rules out two proposed energy
  shortcuts; it is explicitly not a counterexample under canonical
  Gaussian initialization or a counterexample to integrated tracking.
- [SMALL_LABEL_CAVITY.md](SMALL_LABEL_CAVITY.md) proves a finite-width
  Gaussian bound for the initial two-layer carrier dictionary, retaining
  same-row correlations and allowing adapted residual coefficients.
  The actual carrier also has an `O(Y^3)` moving-field remainder in RMS.
  Multiplying that remainder by the actual response error still needs a
  joint estimate. Exact source differentiation identifies the unresolved
  carrier-times-response term; residual differentiation itself supplies
  favorable Gauss--Newton damping in the Hilbert energy.

These routes read only explicitly scoped current-study and maintained
book/paper inputs. The coordinator read their complete reports and checked
the new terminal-cutoff argument. The structured route separately checked
the full endpoint-kernel proof, normalized vector estimate, prefix behavior,
zero-residual case, and exponential-decay deduction. These are internal
analytic checks, not promotion reviews. No new training, external search,
Git operation, or maintained-manuscript edit was performed.

The remaining claim must not be described as settled: small labels now
give uniform exponential fitting and consistency, but the proof of a
width-independent `C/P` trajectory constant for all widths still lacks
control of correlations between initialized backward carriers and the
actual gate error. No order/width limit has been interchanged to hide it.

## Unit-label extension under joint width/order scaling

The user requested an actual proof beyond the small-label regime, allowing
`P` to grow with `n`. Two new results remove label smallness, with distinct
quantifiers:

- [UNIT_LABEL_JOINT_ORDER.md](UNIT_LABEL_JOINT_ORDER.md) proves, for arbitrary
  finite inputs and fixed depth, tanh, `Y<=1`, initial readout RMS `B_0<=1`,
  and initialized hidden operator norm at most `K`,
  `sup_[0,T] d_n <= C_T exp(a_T(1+sqrt(n))) [B_0 P^-3/2 +(1+sqrt(n)) P^-2]`.
  No Gram gap, dense fitting, closure decay, Gaussian transport, or residual
  floor is assumed. The relative defect bound gives a derived residual
  comparison to its own initial value; forward/backward tail multiplication
  cancels the inverse-initial-residual intermediate term. Sufficient joint
  orders give a width-independent `C_T/P`. The single schedule `P>=ceil(exp(n))`
  works for each fixed horizon, with a horizon-dependent constant.
- [UNIT_LABEL_DENSE_ROUTE.md](UNIT_LABEL_DENSE_ROUTE.md) derives a new exact
  scalar invariant: with zero readout and one sample, the ratio
  `sign(y) f/(||w||/sqrt(n))` is nondecreasing from the initial feature RMS.
  Consequently the top feature norm cannot collapse, at any fixed depth
  or label size. Dense residual decay and finite activity follow without
  a small-label perturbation argument. A short initial activity interval
  extends the result to the canonical small nonzero readout.
- [UNIT_LABEL_SINGLE_SAMPLE.md](UNIT_LABEL_SINGLE_SAMPLE.md) transfers that
  invariant to the actual old-clock closure. Its decrease is bounded by
  the integrated compression defect, with no singularity from division by
  readout norm. At all orders above a width-independent threshold it proves
  fitting, a positive feature Gram, finite activity, and parameter limits
  uniformly over `abs(y)<=1`. Since the scalar residual direction is
  constant, both histories have bounded clock derivative after subtracting
  the readout-dependent prefix jump. Thus the displayed finite-time error
  estimate holds with one all-time constant. Choosing
  `P>=max(P_0,B_0^2 exp(2a(1+sqrt(n))),(1+sqrt(n))exp(a(1+sqrt(n))))`
  gives an all-time, width-independent `C/P` bound. Zero readout removes
  the first exponential threshold. Prediction errors uniformly on bounded
  input sets and test RMS discrepancies inherit this bound.
  A further endpoint estimate gives exponential closure residual decay at
  `P>=max(P_0,C(1+sqrt(n)))`, with width-independent rate, after fixing a
  sufficiently small initial-readout threshold. This is a consequence of
  the activity proof, not an assumption used to obtain it.
- [UNIT_LABEL_SCALAR_CHECK.md](UNIT_LABEL_SCALAR_CHECK.md) supplies a complete
  internal check of the zero-readout proof, including the sharper bound
  `C Y^2(1+sqrt(n)Y^2) exp(CY+C sqrt(n)Y^2)/[P(P+1)]`. The checker also
  checked the subsequent small-readout initial-activity extension in the
  single-sample report. The sign there is the direction of the initial
  residual toward the target, not necessarily the sign of the label.

The coordinator read the complete compact-horizon and scalar derivations;
the scalar check was a scoped internal analytic verification, not promotion.
These findings supersede the earlier inability to remove label smallness
on any general-depth all-time example. They do **not** settle all-time
tracking for arbitrary multi-input data at `Y<=1`. The scalar ratio loses
its sign argument when the residual direction rotates in sample space.
The sufficient order schedules also exceed width at large `n`; they prove
joint approximation, not an efficient large-width compression rate.

No training, external search, Git operation, or maintained paper/book change
was performed in this continuation.

## Activation-general all-time small-label extension

The user requested generalization of the multi-input small-label result.
The combined statement and proof are in
[ACTIVATION_EXTENSION.md](ACTIVATION_EXTENSION.md). This continues the
same autonomous old-clock investigation and does not change the algorithm.

The proved deterministic class is layer-dependent `C^{1,1}_loc(R)` with
globally bounded first derivative. Activations may be unbounded and need
not be odd, monotone, analytic, or twice continuously differentiable.
The initialization event now includes a bound on first-layer training
preactivation RMS, alongside hidden operator norms, small readout RMS
`B_0<=Y`, and a positive top feature-Gram gap. A fixed parameter tube and
linear growth replace the earlier pointwise activation bound.

The resulting `Y_*>0` is independent of width and memory order. Every
finite order has global existence, exponential residual decay, finite
activity, and convergence to an interpolating parameter. For tracking,
let `ell_n` be the maximum Lipschitz constant of the activation derivatives
on `[-R sqrt(n),R sqrt(n)]`, where `R` is the proved preactivation RMS
bound, and put `chi_n=ell_n sqrt(n)Y^2`. Then

`sup_(t>=0) d_n <= A exp(a(Y+chi_n)) [B_0Y^(3/2)P^(-3/2) + Y^(5/2)sqrt(1+chi_n^2+log(e+P))P^(-2)]`.

Thus `P>=ceil(exp(2a chi_n))` gives an all-time width-independent `C/P`
bound on that joint order/width region. At zero readout it suffices that
`P>=ceil((1+chi_n)exp(a chi_n))`. Globally Lipschitz derivatives bound
`ell_n` independently of width and preserve the earlier tanh scaling.
This is not an unrestricted all-width, fixed-order rate.

The component proofs and their checked roles are:

- [ACTIVATION_SMALL_LABEL_ROUTE.md](ACTIVATION_SMALL_LABEL_ROUTE.md):
  complete tube/activity/Gram bootstrap using RMS features; Legendre
  endpoint proof; all-order exponential fitting. The label threshold and
  all these source estimates use global slope bounds but no quantitative
  gate-curvature bound. Its globally Lipschitz-gate tracking proof also
  checks the unbounded-activation factors throughout.
- [ACTIVATION_LOCAL_MODULUS.md](ACTIVATION_LOCAL_MODULUS.md): complete
  implication from those now-proved source estimates to the broader local
  modulus tracking bound. Uses the full dense carrier, so no coordinate
  bound on unbounded activations is silently imported. The supplied-lemma
  wording in this component is its explicit dependency boundary; the
  combined theorem proves those lemmas rather than assuming closure decay
  or boundedness. Zero modulus, zero residual, prefix jump and terminal
  cutoff cases are included.
- [ACTIVATION_INITIAL_GRAM.md](ACTIVATION_INITIAL_GRAM.md): an elementary
  finite-difference/mollification proof of ridge independence. Any continuous
  nonpolynomial globally Lipschitz first activation, followed by nonconstant
  globally Lipschitz activations, gives a positive population initialization
  Gram for fixed nonzero pairwise nonproportional inputs. Conditional
  fourth-moment estimates prove finite-width Gram convergence, including
  unbounded activations. No analyticity hypothesis is needed. Together
  with the standard initialized Gaussian norm bounds, the event has
  probability tending to one for each fixed positive small label scale.

Examples covered with a width-independent gate modulus include tanh,
sigmoid, arctangent, sine/cosine, erf, softsign, softplus, exact GELU, SiLU,
and unit-parameter ELU. Affine activations obey the deterministic theorem
when their actual initial Gram has the requisite rank. ReLU/leaky ReLU and
standard SELU are excluded from the smooth dynamics theorem even though
their initial Grams can be nondegenerate. General local smoothness without
a global slope bound, as in the broader fixed-width paper theorem, remains
outside this width/time-uniform proof.

Verification: the coordinator read the complete three component derivations
and checked the tube closures, actual-history identities, RMS feature
factors, local absolute-continuity chain rule, absence of a second width
factor in feedback, terminal cutoff, order algebra, finite-difference
annihilation argument, and conditional Gaussian moment induction. The
component authors checked their derivations; no training or numerical
validation was claimed. These are internal analytic checks, not promotion
reviews. Checked component SHA-256 values:

- Source/fit proof: `ed4baec1cd4a322747fe076068d2308857ae6694e853b2dd9db4f379f32b8b56`.
- Local modulus proof: `953fc38db089066243286c4d2d81b43c4e819ac10eb0d62fba79cb6f95031732`.
- Initial Gram proof: `21b86b28ebeb4bacd8b0f07af0ea4e3209757f2439144cbcaf1d4bcc6cdbbb1a`.

No experiment, external literature search, Git mutation, or maintained
paper/book edit was performed. The multi-input all-time large-label question
and unrestricted width/order tracking remain unchanged and open.

## Activation-general unit-label finite-time extension

The requested `Y<=1` multiple-input extension is proved in
[ACTIVATION_UNIT_LABEL_FINITE_TIME.md](ACTIVATION_UNIT_LABEL_FINITE_TIME.md).
It uses the same layer-dependent `C^{1,1}_loc` activations with globally
bounded slope as the preceding all-time small-label result, including
unbounded softplus, GELU, and SiLU. This is the unchanged autonomous
old-clock closure at arbitrary fixed finite depth and sample count.

No initial Gram gap, geometric separation of inputs, small-label threshold,
assumed fitting, or assumed closure stability is needed. The deterministic
initial conditions are uniform hidden operator bounds, a first-layer
training preactivation RMS bound, readout RMS `B_0<=1`, and label RMS
`Y<=1`. Any fixed finite bounds on labels and readout are also allowed with
changed constants. The training-visible first-layer bound is needed to
control unbounded activations; it was unnecessary for the bounded tanh
source bounds.

For each fixed `T`, dense loss dissipation bounds normalized parameter
motion by `sqrt(T) rho(0)`. A radius-one comparison tube then bounds all
training feature and preactivation RMS values independently of width and
order. Let `R_T` bound preactivation RMS throughout that comparison region,
`ell_(n,T)=max_l Lip(phi_l';[-R_T sqrt(n),R_T sqrt(n)])`, and
`s_(n,T)=1+sqrt(n)ell_(n,T)`. The stopped source and feedback estimates give

`sup_(t<=T) d_n <= C_T exp(Lambda_T s_(n,T)) [B_0 P^(-3/2)+s_(n,T)P^(-2)]`.

Writing `H=exp(Lambda_T s_(n,T))`, the joint threshold
`P>=max{B_0^2 H^2,s_(n,T)H}` gives `sup_(t<=T)d_n<=2C_T/P` and proves
closure continuation through `T`. The exponent is chosen to contain the
fixed minimum order needed for a strict tube margin. Simpler sufficient
thresholds are `P>=ceil(exp(2Lambda_T s_(n,T)))` generally and
`P>=ceil(s_(n,T)exp(Lambda_T s_(n,T)))` at zero readout. For globally
Lipschitz derivatives, this preserves the tanh scale
`log(P)>=C_T(1+sqrt(n))`.

The new proof point is noncircular continuation for unbounded activations:
first prove forward clock energy, then the relative defect `e_E<=C_T rho`,
then residual comparability to its own initial value. The forward and
backward projection-tail product cancels the inverse residual arising in
the backward derivative energy. Local gate variation costs only the
explicit factor `sqrt(n)ell_(n,T)`. The joint order absorbs the Gronwall
factor, keeps the closure strictly within the tube, and bounds every raw
moment at finite width/order. No closure bound is assumed in the final
statement.

With an additional uniform initial `||W_1||_F/sqrt(n)` bound, the theorem
also gives test-prediction discrepancy `C_(T,mu)/P` for any test probability
measure with finite second input moment, uniformly over `[0,T]`, and the
same bound on the difference between the two test RMSEs. The proof uses
linear input growth, not bounded test-domain curvature.

[ACTIVATION_FINITE_TIME_CHECK.md](ACTIVATION_FINITE_TIME_CHECK.md) supplies
a separate scoped internal derivation and check of the continuation margin,
source estimates, residual cancellation, and local-gate feedback argument.
The coordinator read the complete check; the checker also read the complete
new theorem and verified the prediction corollary, prompting an explicit
statement that its constants additionally depend on the initial full
first-layer bound. These are internal checks, not promotion reviews.

Qualifications preserved: width uniformity is on the displayed joint
`(n,P)` region, not at unrestricted fixed order. The proof does not give
all-order finite-time continuation for unbounded activations; it proves
continuation at the certified orders. Super-square-root logarithmic order
sequences suffice eventually in width for globally Lipschitz gates, not
automatically for all finite exceptional widths/orders. The large
sufficient orders do not certify efficient low-rank compression. ReLU gate
jumps and arbitrary unbounded-slope activations remain outside this proof.
The arbitrary multi-input all-time `Y<=1` question remains separate.

No experiment, literature search, Git mutation, or maintained paper/book
edit was performed for this extension.

Final source SHA-256:
`02ef1219784f881a93c8ce36a0662a597a4f53c67e8a7110c479599b9648125e`.
The check's supplemental hash refers to the version before its requested
constant-dependency clarification; that clarification is incorporated in
Section 8 of this final version. No mathematical argument changed.

## Explicit horizon dependence and comparison with the paper

The follow-up is recorded in
[FINITE_TIME_CONSTANTS.md](FINITE_TIME_CONSTANTS.md), with the separate
scoped derivation/check in
[FINITE_TIME_CONSTANTS_CHECK.md](FINITE_TIME_CONSTANTS_CHECK.md).
The comparison uses the current paper's complete old-clock and joint-clock
theorem/proof sections. The new result quantitatively strengthens width
control on overlapping hypotheses; it does not replace the paper's broader
local activation class, arbitrary fixed initializations, joint-clock theorem,
or prove its fixed-order population conjecture. Its normalized outer-layer
metric must also be kept explicit.

For the preceding activation-general unit-label theorem, let
`U=1+sqrt(T)`, `gamma=sqrt(n)ell_(n,T)`, and `s=1+gamma`. A narrow physical
tube and a small-relative-defect bootstrap sharpen the source estimate to

`integral_0^T e_E <= C[B_0 U^(L+1)P^(-3/2)+s U^(3L+4)P^(-2)]`.

The key improvement is weighted backward derivative energy: the proved
relative-defect cap gives `rho(u)<=e rho(t)` for `t<=u<=T`, so future
activity divided by current residual is at most `eT`. In the weighted
Legendre estimate this cancels the inverse residual without exponential
source amplification. An auxiliary endpoint estimate still pays
`exp(C T U^(2L))` to prove the relative-defect cap at sufficient order.
The backward prefix step's exact endpoint error is at most one.
A further use of the perturbed loss dissipation identity bounds the
closure's physical squared-speed integral independently of the horizon
on the bootstrap. Applying the weighted Legendre bound to the forward
history as well gives the sharper displayed source powers.

One-sided gradient-flow comparison discards the positive semidefinite
prediction-Jacobian part of the loss Hessian. The propagation factor is
`exp(C T[U^(L-1)+gamma U^(2L-1)])`. Thus a sufficient order factor is

`H=exp(C[1+log U+log(1+gamma)+T U^(2L)+T gamma U^(2L-1)])`.

At `P>=max{B_0^2 H^2,sH}`, continuation and tracking give
`sup_(t<=T)d_n <= C U^(3L+4)/P`. In particular one can display a
width-independent `C_T<=C(1+T)^(3L/2+2)`. For globally Lipschitz gates,
a simple sufficient order condition is
`log P>=C[(1+T)^(L+1)+sqrt(n)(1+T)^(L+1/2)]`.
These are sufficient upper bounds, not optimality or necessity claims.

A prefactor cannot be interpreted separately from its order threshold.
Since the source has higher inverse powers than `1/P`, one can even make
the displayed parameter prefactor constant by increasing that threshold;
this does not prove uniformity in time at fixed order. The report keeps
the unabsorbed source and propagation estimates visible. Test-prediction
RMS has an additional forward factor `U^L`, assuming the initial full
first-layer normalized norm is bounded.

The coordinator checked the weighted energy, endpoint step formula,
noncircular double bootstrap, local-C1,1 directional second-derivative
argument, and the source/propagation time powers against the separate
scoped derivation. This is internal analytic verification, not promotion.
No training, external literature search, Git mutation or paper/book edit
was performed.

Final checked versions after the weighted forward-energy refinement:

- `FINITE_TIME_CONSTANTS.md`: `1cbdf54cb3602b8d8fadfb5b444b5bffef2c64b91d955ec351a6f15d68abdce4`.
- `FINITE_TIME_CONSTANTS_CHECK.md`: `b905f3ee18a3d19c6b5bcb8572cf38824ea874069952ab6e92c1dfa39fb3cac5`.

## Explicit depth dependence of the all-time small-label theorem

[DEPTH_SMALL_LABEL_CONSTANTS.md](DEPTH_SMALL_LABEL_CONSTANTS.md) combines
complete explicit source recurrences from
[DEPTH_SMALL_LABEL_SOURCE.md](DEPTH_SMALL_LABEL_SOURCE.md) and the separate
feedback derivation in
[DEPTH_SMALL_LABEL_FEEDBACK.md](DEPTH_SMALL_LABEL_FEEDBACK.md).
This continues the multi-input activation-general old-clock result, with
bounded global slopes, local Lipschitz gates, and `B_0<=Y`. It changes no
paper/book theorem and introduces no new experiment or literature source.

A hidden-operator tube of radius `1/L` and Minkowski's inequality before
squaring the forward clock derivative norm avoid artificial products of
large layerwise energy constants. The exact sufficient small-label
threshold, source-tail constants, Gram comparison coefficients, and feedback
amplification are all given as finite scalar recurrences. Their parameters
are data/input bounds, activation slopes/offsets, initialization bounds,
and the initial top-feature Gram gap `lambda_L`.

With `lambda=min(1,lambda_L)`, `g=max(1,vK)` and

`H_L=64 exp(v+1)(1+X+A_0+a+v+K)^4 (L+1) g^L`,

the transparent conservative envelopes are

`Y_* >= lambda^(3/2) H_L^(-10)`,
`A_L <= H_L^72 lambda^(-9)`, and
`a_L <= H_L^39 lambda^(-5)`.

The all-time raw discrepancy is bounded by

`A_L exp(eta_n)[B_0 Y^(3/2) P^(-3/2) + Y^(5/2) sqrt(1+chi_n^2+log(e+P)) P^(-2)]`,

where `chi_n=ell_n sqrt(n)Y^2` and `eta_n=a_L(Y+chi_n)`.
Thus `P>=exp(2eta_n)` gives the width- and time-uniform block-sum
parameter bound `3A_LY^(5/2)/P` without further label reduction. Zero
initial readout permits `P>=(1+eta_n)exp(eta_n)` with coefficient
`2A_LY^(5/2)`. The same exact source threshold still proves exponential
fitting and global existence at every order, independently of these
tracking order conditions. The gap, labels, order threshold and prefactor
must be interpreted together; arbitrarily enlarging the order region's
lower threshold can make a displayed prefactor artificially small.

For fixed elementary layer bounds, the propagation contribution is single
exponential in depth and polynomial in inverse Gram gap; when `vK<=1`
it is polynomial in depth and inverse gap. The exact recurrences are much
sharper than the conservative integer powers above. Compatibility alone
cannot keep the Gram gap bounded in depth: the synthesis gives a fixed
smooth activation `0.1 tanh(z)^3` and orthogonal inputs with a strictly
positive population initialization gap decaying superexponentially in
layer count. This is an initialization-conditioning example, not an
error lower bound. The unrestricted fixed-order width-uniform tracking
problem remains open.

The coordinator read both complete derivations, checked the source/feedback
combination and order absorption, and the feedback author separately
verified every combined depth-envelope exponent. These are scoped internal
analytic checks, not independent promotion reviews. No Git mutation or
maintained paper/book modification was performed.
The source author also read the complete synthesis and checked the unchanged
label threshold, source constants, and explicit orthogonal-input Gram
example. Its only requested correction was a display-math escape, now fixed.
Final synthesis SHA-256:
`7a82d99b181b91894d21ad3c284b8865c2509cc898e7d05c3951ac43f825a43f`.

Subsequent order-extraction refinement is in Section 7 of
`DEPTH_SMALL_LABEL_CONSTANTS.md`. Keeping `beta=B_0/Y` gives the sharper
sufficient threshold
`P>=ceil(max{beta^2 exp(2eta_n),sqrt(1+chi_n^2+eta_n) exp(eta_n)})`
for the same `3A_LY^(5/2)/P` all-time bound (coefficient two at zero
readout). The coordinator and a prompt-only algebra checker verified it
and its constant-factor sharpness for the displayed upper bound, not
necessity for the algorithm. The preceding synthesis hash identifies the
version before this appended refinement; previous theorem statements and
proofs remain unchanged. No manuscript edit or new neural estimate was
needed for this refinement.

## Slow orders: an all-time envelope and a dense-only width remainder

The user returned to the earlier arbitrary-slow-order convergence theorem
and requested an actual discrepancy bound, fixing **B_0=0** and one positive
small label RMS independent of width. The resulting synthesis and proof are
in [SLOW_ORDER_UNIFORM_BOUND.md](SLOW_ORDER_UNIFORM_BOUND.md).

For canonical Gaussian tanh, fixed finite data and depth, and the established
positive population initial feature-Gram gap and small-label hypotheses,
the unchanged autonomous old-clock closure now has, on common initialization
events of probability tending to one and simultaneously in every order q,

`sup_(t>=0) d_n <= C Phi(1/q+a_n)`,

where `Phi(s)=s exp(K sqrt(log(e+1/s)))` and `a_n->0` in probability.
The constants are independent of width, order and physical time. Crucially,
the remainder is defined from the dense trajectory's activity-weighted
empirical backward-carrier tails, not from the closure tracking error.
Equivalently the bound is

`C q^-1 exp(K sqrt(log(e+q))) + b_n`, with `b_n->0` in probability.

For every fixed `0<gamma<1` it implies
`C_gamma(q^-gamma+a_n^gamma)`. Thus every prescribed divergent order sequence,
including logarithms or iterated logarithms, has an explicit order-error term
plus a vanishing width remainder. No numerical power of width is assigned to
that remainder, and it cannot be silently discarded along a named schedule.

The proof uses the previously established all-time residual-damped comparison
and accumulated defect `C/q`. A carrier cutoff M gives amplification `exp(KM)`
in finite total activity. Fixed-program Gaussian transfer on each fixed
horizon, followed by a deterministic late-activity estimate, proves a fixed-M
bound on the dense weighted tail. Its monotonicity in M constructs one
vanishing simultaneous width remainder by a finite-head/tail argument.
Optimizing M gives the displayed explicit envelope without an assumed trained
finite-width Gaussian tail, closure-clock residual ratio, or population-closure
existence theorem.

Two further consequences retain their quantifiers:

- There exists a sufficiently slow deterministic schedule `q_n->infinity`,
  bounded above by `n^(1/4)` or any other prescribed divergent cap, for which
  `sup_t d_n<=C_gamma q_n^-gamma` with probability tending to one, for every
  fixed `0<gamma<1`. Its width thresholds are nonconstructive. This does not
  certify the explicit schedule `q_n=n^(1/4)` or `log(n)` at the pure rate.
- A confidence envelope tends to zero with q uniformly over widths and
  simultaneously over all orders/time. It combines a dense-floor quantile
  `alpha_N(delta)->0` with `N(q)` proportional to `log^2(e+q)`; its unknown
  quantile rate is stated explicitly. A supremum of failure probabilities
  over widths is not one event holding at every width simultaneously.

Bounded-test-set prediction discrepancies and test L2/RMSE differences inherit
the result by the all-time forward difference estimate. This strengthens the
earlier all-time qualitative Gaussian result. The broad-activation deterministic
exponential-order C/q certificate remains valid; an explicit floor-free C/q
rate in the general slow-order regime remains open. No new broad-activation
Gaussian transfer theorem is asserted here.

The scoped Gaussian route is [SLOW_ORDER_GAUSSIAN_ROUTE.md](SLOW_ORDER_GAUSSIAN_ROUTE.md).
The separate [SLOW_ORDER_TRANSFER_ROUTE.md](SLOW_ORDER_TRANSFER_ROUTE.md) derives
weaker envelopes from finite-horizon transfer alone and explains why those
premises alone do not imply a power rate. The new Gaussian argument uses the
additional all-time damping and Gaussian carrier structure.

Internal checks: the coordinator read both complete candidates and checked
the cutoff/energy, fixed-program transfer, monotonic-floor, optimization and
diagonal arguments. The Gaussian-route author checked the synthesis's core
proof; both scoped authors checked the uniform-confidence and slow-diagonal
quantifiers. The small-width confidence branch was simplified to use the
existing `C/q exp(k sqrt(n))` bound at `n<=c_gamma log^2(e+q)`, which supplies
`C_gamma q^-gamma` and avoids needing a sharper source theorem there. These
checks verify the new deductions from the stated study inputs, not every
underlying book proof and not promotion. Checked files:

- Synthesis: `eee609f0cdc64fb7cdb748c1f4bae49632ca38f8e896931b92a468057f0a2bb9`.
- Gaussian route: `8e14b5ec751161d9116de49576e40ff242346fa5e5ebad0d7d7fd73795bf1544`.
- Transfer route: `7b0d79ae4ae7573d756969629066376545f80a3b2c2dd20e0af72acd2516812f`.

No experiment, external literature search, Git mutation, or maintained
paper/book edit was made for this continuation. Concurrent unrelated changes
were preserved.

## Whole-input test prediction, uniformly over all physical time

The prediction-level continuation is
[POPULATION_TEST_ERROR.md](POPULATION_TEST_ERROR.md). It retains exactly zero
readout, canonical Gaussian tanh, fixed finite data and depth, a positive
limiting initial readout-feature Gram gap, and a fixed sufficiently small
label RMS. It uses the unchanged autonomous old clock.

Write `A(q)=C q^-1 exp(K sqrt(log(e+q)))`. The implemented finite closure
approximates the dense population predictor with

`[integral sup_(t>=0)|fhat_(n,q)(t,x)-f_D(t,x)|^2 dmu(x)]^(1/2)`
`<= Psi_mu(A(q)) + eta_(n,mu)`,

simultaneously in all orders on common initialization events of probability
tending to one. Here `eta_(n,mu)->0` in probability is a dense-only width
remainder, independent of q, and
`Psi_mu(s)^2=integral min{4B^2,C_*^2 ||x||^2 s^2/d} dmu(x)`, with `B<=CY`.
No input moments are needed for convergence under a fixed test law. A finite
second moment preserves the explicit near-first-order rate `A(q)`; a finite
p-th moment below two gives its p/2 power. An entire bounded input domain has
the stronger absolute-error bound `sup_(t,x in K)|error|<=C_K A(q)+eta_(n,K)`.
Thus circles and spheres are covered without a test mesh or adding passive
test inputs to the trained algorithm. The difference in test RMSE against
any square-integrable target is at most the corresponding prediction error.

The proof first establishes the no-bias observation inequality
`|fhat(x)-f(x)|<=min{2B,C_* ||x|| d_n/sqrt(d)}`. Fixed-time dense population
identification, uniform input Lipschitz bounds, and exponential late-time
activity give dense finite-to-population convergence on whole compact input
domains for all time. Bounded outputs control unbounded input tails. These
steps turn the existing parameter estimate into the displayed test bound.

There is also a genuine population-predictor conclusion. Uniform closure
velocity decay, input equicontinuity, and bounded outputs yield subsequential
predictor-law limits in the weighted whole-input/all-time uniform topology.
Every fixed-q limit obeys
`|F_q(t,x)-f_D(t,x)|<=min{2B,C_* ||x|| A(q)/sqrt(d)}` for every time and input,
almost surely. Consequently its test bound has no finite-width remainder.
This proves existence and accuracy of predictor limit points; it does not
identify a unique deterministic autonomous population moment ODE at fixed q.
The corresponding moment-state existence/identification remains open.

Every prescribed divergent order sequence still converges against the dense
population, including logarithmic and iterated-logarithmic orders. The theory
does not assign a numerical width rate to `eta`, obtain exact `C/q`, improve
the all-time order exponent by switching to outputs, or prove a vanishing
unweighted supremum over unbounded R^d. Weighted whole-space supremum and
full-domain test RMSE are proved. These qualifications are separate from
the complete whole-circle/sphere conclusion.

The scoped derivations are
[WHOLE_INPUT_PREDICTION_ROUTE.md](WHOLE_INPUT_PREDICTION_ROUTE.md) and
[POPULATION_TEST_LIMIT_ROUTE.md](POPULATION_TEST_LIMIT_ROUTE.md). The coordinator
read both complete derivations and verified the synthesis, including the
spectral-slack velocity/exponential-decay inputs. The observation author read
the complete synthesis and checked the forward recurrence, input-law modulus,
risk inequalities, time compactification, and weak-limit quantifiers, then
checked the final strengthening that places the time supremum inside the
input integral. Its compactness check took the explicitly supplied uniform
velocity and physical bounds as premises, without rechecking the source
theorems. These are scoped internal checks, not promotion reviews.

Checked final SHA-256 hashes:

- Synthesis: `9618e8cff7dca52a52e9fe63df00630ee8d07303a2b40d3171ed16db03744186`.
- Observation route: `af8e040d79fd85692d746f10b4867a6e3401e7d9ec4059cd25551c32fd8933f5`.
- Population route: `1f9aa8cc1f883e1e25eba7b86c78b87849216217fb5aee81dda157df6f359a04`.

No experiment, external literature search, Git mutation, or maintained
paper/book change was made. Concurrent unrelated changes were preserved.

## Dense baseline and the meaning of learned-state compression

[DENSE_VS_CLOSURE_TEST_COMPLEXITY.md](DENSE_VS_CLOSURE_TEST_COMPLEXITY.md)
compares actual finite dense and old-clock closure predictors with the same
dense population target, in the same all-time test norm and small-label
Gaussian tanh regime. The dense error tends to zero in probability, uniformly
over all time, but the fixed-program passage gives no numerical width rate.
The closure error is at most `C omega(q)+beta_n`, with a vanishing dense-only
remainder independent of q; that remainder is not known comparable to the
dense prediction error itself.

Excluding the fixed initialized matrices, the canonical dense implementation
has `(L-1)n^2+n(d+1)` evolving coordinates. The closure has
`2(L-1)mnq+n(d+1)+O(1)`. For fixed m,d,L>=2, every deterministic
`q_n->infinity` with `q_n=o(n)` therefore converges to the same all-time
population predictor using a vanishing fraction of the dense moving state.
At any fixed error tolerance and confidence, one may first choose fixed q,
then take width large enough that both models meet that tolerance; their
evolving sizes are then linear versus quadratic in width. This does not
compare their minimum sufficient widths or actual error rates.

The note isolates a quantitative matching criterion: if both width errors
have a common deterministic rate envelope r_n, sublinear order can match
that certificate exactly when `r_n/omega(n)->infinity`. Conditionally on
both errors being `O_p(n^-a)`, 0<a<1, it suffices to use
`q=n^a exp(K sqrt(a log n)+O(1))`, giving learned-state size
`n^(1+a+o(1))` versus `n^2`. Root-n behavior would yield the familiar
conditional epsilon costs `epsilon^(-3+o(1))` versus `epsilon^-4`.
Root-n behavior is not proved here, and neither sufficient cost is claimed
optimal. Dense finite-time convergence alone cannot supply that rate.

The coordinator verified the source comparison and complete deduction. A
prompt-only scoped checker independently derived the count, probability and
rate implications, then read the complete candidate with the imported
analytic inequalities treated as premises. It checked the general matching
criterion, same-tolerance quantifiers and conditional rate algebra; no
substantive issue remained. Checked SHA-256:
`615439ca2f85e4437f45e153510579ed5a927c1e1f65ac1c235d756ddd0bd3d7`.
This is an internal study-level check, not promotion. No experiments,
external searches, Git mutations or maintained paper/book edits were made.

## Near-quadratic order accuracy without changing the old clock

The user asked whether the learned-state accuracy trade-off could improve
by gaining a second power of memory order. The complete new theorem and
proof are in [NEAR_QUADRATIC_ALLTIME_BOUND.md](NEAR_QUADRATIC_ALLTIME_BOUND.md).
For the same fixed small-positive-label, zero-readout Gaussian tanh regime,
the actual autonomous old-clock closure satisfies, simultaneously in all
orders on the common initialization event,

`sup_(t>=0) d_n <= C Phi(q^-2+a_n)`,

where `Phi(s)=s exp(K sqrt(log(e+1/s)))` and `a_n->0` in probability is
dense-only. Equivalently the bound is
`C q^-2 exp(K sqrt(log(e+q)))+b_n`. Constants are independent of width,
order and time. Every fixed exponent below two follows. No new clock,
truncated backpropagation, oracle input, or clipping is added to the algorithm.

The new argument uses clipped auxiliary backward fields only in the proof.
Their physical derivatives are `C(1+M)rho_hat`, while their normalized
residual factor has bounded physical derivative. Freezing the proof history
after time T and using the remaining-activity estimate gives weighted
Legendre derivative energy `C(T+(1+M)^2)`. This yields backward-history
tail `(1+M+sqrt(T))/q+exp(-kappa T/2)`, with no dense/closure residual ratio.
The exact moving-endpoint energy identity converts the product of history
tails into a bound on the absolute accumulated velocity defect. The forward
tail supplies the other factor `1/q`.

Clipping mismatch is bounded using the dense reference by
`C(1+M)D+C sqrt(Z_n(M)+Q)`, where D is actual all-time parameter discrepancy,
Z is the dense activity-weighted carrier tail, and Q is integrated residual
discrepancy. The existing damping theorem controls Q. The remaining square-root
feedback has a coefficient `1/q`, so Young absorption contributes `1/q^2`.
Choosing M of square-root-logarithmic size and T logarithmic in the target
source error closes the bound with the same type of dense-only width floor.

The whole-input observation and predictor-limit theorem therefore inherits
the near-quadratic order envelope: all-time absolute error on entire bounded
input domains, or all-time test L2/RMSE error on any fixed finite-second-moment
input law. Actual finite closures retain a vanishing width remainder; every
fixed-q population predictor limit has the order envelope alone. No unique
fixed-order population moment dynamics or explicit width concentration rate
is established by this improvement.

The unconditional population order requirement improves from
`q=epsilon^(-1+o(1))` to `q=epsilon^(-1/2+o(1))`. If both relevant width
errors additionally had an all-time root-n certificate, the resulting moving
state budget would improve from `epsilon^(-3+o(1))` to
`epsilon^(-5/2+o(1))`, versus the dense implementation's `epsilon^-4`.
At matched root-n accuracy and the same width the corresponding order is
`n^(1/4+o(1))`, with `n^(5/4+o(1))` moving coordinates. These complexity
exponents remain conditional on the numerical width certificate; they
are not proved optimal costs.

The complete independent initial route is
[HIGHER_ORDER_DEFECT_ROUTE.md](HIGHER_ORDER_DEFECT_ROUTE.md). The separate
[HIGHER_ORDER_CLOCK_ALIGNMENT.md](HIGHER_ORDER_CLOCK_ALIGNMENT.md) first
investigated the old ratio obstruction and then independently reconstructed
the supplied weighted terminal-history lemma and endpoint-energy identity.
The coordinator read both complete derivations and checked the new source,
clipping comparison and feedback algebra. Both scoped authors then read the
complete frozen synthesis and passed the new analytic chain in Sections 1--6,
including the common order threshold and width-floor quantifiers. The
population observation/limit passage in Section 7 used the prior checked
POPULATION_TEST_ERROR.md theorem as an explicit supplied premise; neither
scoped checker reopened that theorem's dependencies. Conditional complexity
arithmetic was checked. These are internal study checks, not promotion.

Checked hashes:

- Synthesis: `89d85b31167ab5087e89f5a716655d6215e6e6b654e7563f8280c923b6afa259`.
- Defect route, including cross-check: `09defb9d8e5d4ce197f83d93e62ced8243fe8b5716dcc7ebd9f1ea290c8bdc71`.
- Terminal-history route, including cross-check: `354f096a56954b535451dbc3ba5098fb9dbd437ec9994ac666567b22d1bc2279`.

The earlier near-first-order bounds remain valid weaker consequences. Their
claims that no sharper all-time exponent had yet been obtained are superseded
by this continuation. Exact `C/q^2`, quantitative width rates, larger labels,
and, at this stage of the investigation, broad-activation Gaussian transfer
remained separate open claims; the continuation below settles the latter
for the stated global derivative-Lipschitz class. No new
experiment, external search, Git mutation, or maintained paper/book edit was
made; unrelated concurrent changes were preserved.

## Broad-activation near-quadratic all-time extension

The user asked to extend the new near-quadratic result to the broad
activation class. The synthesis and full quantitative proof chain are in
[ACTIVATION_NEAR_QUADRATIC_ALLTIME.md](ACTIVATION_NEAR_QUADRATIC_ALLTIME.md).
Each layer may have a different C1 activation with finite value at zero,
globally bounded slope, and globally Lipschitz derivative. No bounded
activation values, oddness, centering, monotonicity, or analyticity are
required. Zero initial readout and small fixed positive label RMS remain
essential hypotheses of the stated theorem; the threshold may depend on
depth, the initial feature-Gram gap, data, and the activation constants.

The actual autonomous old-clock closure satisfies, on common initialization
events of probability tending to one and simultaneously for every order,

`sup_(t>=0) d_n <= C Phi(q^-2+a_n) <= C q^-2 exp(K sqrt(log(e+q)))+b_n`,

where `a_n,b_n->0` in probability are dense-only and independent of order.
The constants are independent of width, order, and physical time. The
pure order term is bounded by every fixed `C_gamma q^-gamma`, gamma<2.
This is not a numerical width rate or a finite-width floor-free C/q^2
theorem. Any diverging deterministic order sequence still gives all-time
convergence in probability. All orders have exponential fitting, as in
the earlier activation-general small-label bootstrap.

Two complete routes provide the genuinely new inputs:

- [ACTIVATION_GAUSSIAN_ALLTIME.md](ACTIVATION_GAUSSIAN_ALLTIME.md) extends
  the dense strong population construction and sub-Gaussian full-carrier
  bounds using the complete maintained C.1--C.2 proof units. Deterministic
  population Euler steps are expressed in accumulated residual activity.
  A stopped response/tube construction, Gram margin, and one-step prediction
  remainder exclude activity exit before the continuous global limit is
  constructed. The proof treats unbounded forward features and full trained
  carriers together, includes the trained readout, and transfers fixed
  cutoffs to actual finite dense GF. Exponential remaining activity and a
  monotone cutoff argument produce the common dense-only width remainder.
  No trained closure Gaussianity or trained finite Gaussian-tail assumption
  is inserted.
- [ACTIVATION_QUADRATIC_DETERMINISTIC.md](ACTIVATION_QUADRATIC_DETERMINISTIC.md)
  extends damping, history regularity, and quadratic absorption using RMS
  feature bounds. The auxiliary proof recursion must clip the top readout
  as well as lower carriers: unbounded activations remove the tanh-specific
  coordinate bound on the evolving readout. This clipping is exclusively a
  proof device; no new operation is inserted into the closure. Its Section 7
  also records a conditional local-modulus extension, which is not part of
  the unconditional Gaussian theorem because its broader source hypotheses
  have not been proved.

For whole-input predictions, the common Gaussian event includes the full
first-matrix Frobenius bound divided by sqrt(n), not only its training
preactivations. The observation estimate becomes
`|fhat-fD| <= C(1+||x||/sqrt(d)) d_n`, covering nonzero offsets.
Passive probes in the same dense generated action spaces, finite input
nets, and the remaining-activity bound give all-time dense population
prediction convergence. A finite second moment controls unbounded test
domains, including the stronger norm with time supremum inside the input
integral. The resulting closure-to-dense-population error has the same
order term plus a vanishing dense-only width remainder. Every possibly
random fixed-order subsequential population predictor limit has the pure
order envelope; a unique fixed-order population moment ODE is not claimed.

The covered examples include tanh, sigmoid, arctan, erf, sine/cosine,
softsign, softplus, exact GELU, fixed-scale SiLU/Swish, unit ELU and smooth
ReLU approximations with bounded first/second derivatives. Exact ReLU and
leaky ReLU remain outside the theorem. The earlier merely local C1,1
activation result is larger formally; arbitrary growth of its local
derivative modulus cannot be silently admitted into the present Gaussian
rate proof. Positive initial feature Gram is supplied by
ACTIVATION_INITIAL_GRAM.md under its nonproportional-data/nonpolynomial
first-layer condition, or checked directly.

Moving-state counts and the population order certificate
`q=epsilon^(-1/2+o(1))` are unchanged. The conditional root-n width-cost
comparison remains conditional: no numerical width certificate has been
added by broadening the activations.

The coordinator read both new complete derivations, the complete earlier
activation bootstrap and initial-Gram proof, the tanh predecessor, and the
maintained C.1--C.2 units. The Gaussian-route author then read the complete
frozen synthesis and checked its Gaussian and whole-input bridges, treating
the deterministic near-quadratic estimate as a supplied premise. The
deterministic-route author read the same complete frozen synthesis and
checked its quantitative proof, treating the Gaussian bridge as supplied.
Both checks concern initial synthesis hash
`30d0eb49d29e09fe372a9ac1c9dcf5b267c401f6d54d2c23846c14f967ae8207`.

The coordinator incorporated and checked their precision corrections:
define the tail remainder off the good event; include the full first-layer
norm event and passive-probe construction; describe fixed-order predictor
limits as possibly random; write finite RMS factors explicitly; and clarify
the clock-length-one prefix. No substantive proof objection remained in
these scoped checks. These are internal author checks, not fresh complete
independent promotion reviews.

Final artifacts:

- Synthesis: `0801cb31acd77d8fbd157833090de3f88e5484a23cb471349b6e9c1b7e413bb7`.
- Gaussian bridge: `6385264a060893eb226e94b4302ff86a095e00bf34e9fa364f4e7759486139d0`.
- Deterministic route: `e80a5fd95786533c09d07a89a70d6e67fcbc5ec27794370a68d9f8cbf4b3a111`.

No experiment, external source search, Git mutation, or maintained paper/book
edit was made. Concurrent repository changes were preserved.
