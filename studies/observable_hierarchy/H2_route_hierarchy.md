# H2 route: direct bounded-probe population closure

Status: **frozen first-route report; incomplete C-H2 construction**. The route
constructs genuine finite autonomous population equations, proves their
fixed-order well-posedness and Gaussian finite-array interpretation, and
identifies an indispensable missing compactness estimate. It does **not** prove
their convergence to canonical GF or exclude other admissible closures.

This report was derived independently, without reading another route, review,
study, or research history. Scientific inputs were the complete
`candidate_v3.md`, complete `dependencies_v1.md`, `docs/NOTATION.md`, and
`docs/gaussian_calculus.md` §§6, 7.2, 10. The two required mathematics skills
and their research-contract, adversarial-audit, and proof-search references
were also read. No training experiment or numerical prototype was run.

## 1. Contract and conclusion

Use exactly (H1)–(H3) of the candidate: two hidden tanh layers, full unhalved
mean square loss, stored Gaussian variances `(1,1/n,1/n²)`, mobilities
`(n,1,n)`, residual `f-y`, canonical initial row `g`, initialized Gaussian
action `A₀` with its actual adjoint, zero *limiting* readout, and a fixed
law ball about the opposite-label reference. Fix `T=1/200` and any positive
`ρ` strictly smaller than the candidate's radius. Neither varies with order.
The training law is separately fixed and can be nonatomic or have
nonorthogonal inputs. Finite Gaussian readout is preserved in the bridge below.

The intended limits are uniform in physical time for whole-circle prediction
and for each separately fixed same-layer finite C-H1 joint tuple in `W₂`,
including initial/current pairings, both action directions, and actual second
moments. No temporal analyticity, moment determinacy, Stieltjes representation,
future trajectory, arbitrary-vector action interface, dense representative
network, or original middle-parameter density is admitted.

The mechanism explored here is a **finite boundary closure of current probe
coordinates**. The state at order `j` is two probability laws on explicitly
finite-dimensional Euclidean spaces. Dynamic coordinates consist of moving
seeds and finitely many named current action outputs. Ordinary coordinate
operations are recomputed. The finite set of additional action outputs
required by the derivative compiler is held at its joint initialized value
obtained from the finite Gaussian rule. This is an explicit witness, not a claim that freezing the boundary is
accurate.

The first missing implication is:

> Bounds and consistency on the actual canonical path must imply
> order-uniform fixed-coordinate tightness, uniform integrability of squared
> values, and sufficiently small cutoff/boundary errors on the trajectories
> of these closed finite systems.

No argument below establishes that implication. Even if it were supplied,
one would still need a dynamic realization theorem for a resulting complete
hierarchy solution. Reached-state sufficiency in the candidate cannot be
applied to an arbitrary formal hierarchy curve.

## 2. Finite dictionaries and exact initialization

For `j≥10`, let `D_j` be the circle directions with angles
`2πk/j!`, and let `Q_j={k/j!: |k/j!|≤j}`. Both sets are finite and nested.
Every circle direction and real coefficient can be approximated by these sets.
Keep all legal acyclic alphabet programs with at most `j` nodes, directions
in `D_j`, and affine marks in `Q_j`. Keep a finite set of basic physical
programs at every order if they do not yet occur in this list. The list is
closed under taking ancestors. Call it `P_j`.

The increasing dictionary is only a means of specifying finite systems.
The finite observation request may ultimately have arbitrary real marks.
Passing from dictionary marks to such marks would require uniform continuity
estimates on the approximations; those estimates are not asserted here.

A **primitive** is a moving seed `w₁,w₂,c`, a frozen seed, or the output of
an action instruction `A b` or `A* b`. Affine, trigonometric, tanh, and product
nodes are deterministic functions of their primitive ancestors. Distinct
named occurrences are retained unless literally identical; equality of
different expressions is not silently assumed at a finite closed order.
Every same-population observation is evaluated from one joint vector.

Discretize the fixed law `μ` using a finite continuous partition of unity
`ψ_a` on the angle/label domain, with each support within distance `C_Y/j!`
of a fixed representative `(u_a,y_a)`. Periodic piecewise-linear hat
functions in angle and ordinary piecewise-linear hat functions in label,
multiplied together, give such a partition. Choose circle representatives
in `D_j`. Keep zero-weight representatives as well, so the dictionary does
not depend on atom counts. The resulting
law is

    μ_j = Σ_a α_a δ_(u_a,y_a),   α_a≥0,   Σ_a α_a=1,
    W₁(μ_j,μ) ≤ C_Y/j!.

Its weights are `α_a=∫ψ_a dμ`, exact integrals of fixed continuous functions.
Sending a point to representative `a` with probability `ψ_a` supplies
the claimed coupling bound. One may instead use the candidate's admitted
interface of finite atomic laws with certified vanishing `W₁` error.
The choice of representatives and all future coefficients are fixed before
evolution. The system uses finite sums for `μ_j`; no empirical TV
approximation is used. For every fixed `μ` in the chosen ball, `μ_j` is
eventually in the candidate's established neighborhood.

All primitive initial values, including initial copies of dynamic values,
are obtained by taking the finite union of their programs and applying (H6).
Thus their joint law is a pushforward of finitely many ordinary Gaussians by
an explicitly finite source-response calculation, including singular query
Grams. The same initialized action is used in both directions. No covariance
matrix is subsequently treated as an action at learned time.

## 3. A forward tangent compiler

The candidate gives a reverse weak compiler. A forward compiler is convenient
for constructing actual finite-dimensional population flows. The following
version produces bounded velocity fields at every fixed cutoff `R≥1`.
Put `T_R(v)=R tanh(v/R)` and `g_ℓ=1-h_ℓ²`. At one current state recompute

    h₁a = tanh(w·u_a),     z₂a = A h₁a,
    h₂a = tanh(z₂a),       d₂a = c g₂a,
    q_a = A* d₂a,          r_a = E₂[c h₂a]-y_a.

These are word evaluations. The occurrences of `A` and `A*` in this section
are syntax instructions; their implementation as primitive coordinates is
specified in §4 and does not call a retained operator.

The compiler returns each velocity as a finite sum

    D_R V = Σ_s a_s(P₁,P₂) B_s,

where `B_s` is a bounded alphabet expression and the scalar coefficients
are finite sums and products of fixed numbers and current within-population
contractions. Here `P_ℓ` denotes the current law on population `ℓ`.
The recursive rules are:

    D_R w_i = -2 Σ_a α_a r_a u_ai g₁a T_R(q_a),
    D_R c   = -2 Σ_a α_a r_a h₂a,
    D_R(frozen seed) = 0.

Affine nodes use the affine derivative rule. For `F=sin,cos,tanh`, use
`D_R F(V)=F'(V)D_RV`; their derivatives are bounded alphabet expressions.
For two bounded nodes use `D_R(VW)=W D_RV+V D_RW`. Scalar coefficients stay
outside these coordinate expressions.

If `D_R b=Σ_s a_s B_s`, the two action rules are

    D_R(A b)
      = -2 Σ_a α_a r_a d₂a E₁[h₁a b]
        + Σ_s a_s T_R(A B_s),                                  (F+)

    D_R(A* b)
      = -2 Σ_a α_a r_a h₁a E₂[d₂a b]
        + Σ_s a_s T_R(A* B_s).                                 (F−)

The operand `b` of an action is bounded by the alphabet contract. Every
`B_s` is bounded by induction, so all new action operands are legal.
The output saturation in `(F±)` makes their contributions bounded as well.
The derivatives of affine coefficients and current scalar contractions are
not taken: they are the scalar coefficients of a first time derivative,
not additional moving nodes being differentiated a second time.

These formulas are regularizations of the exact identities

    (A b)'=A' b+A b',          (A* b)'=A'^* b+A* b',
    A' b=-2 Σ_a α_a r_a d₂a E₁[h₁a b],
    A'^*b=-2 Σ_a α_a r_a h₁a E₂[d₂a b].

The rank formulas follow directly by applying (H2) to `b` and using the
actual adjoint. The sum representation follows by induction through the
finite graph. No multiplication of unrestricted L² fields is required as
an action operand.

For every **fixed** word and fixed finite training law, on the canonical
path,

    sup_(t≤T) ||D_R V(t)-V'(t)||₂ → 0   as R→∞.                 (C)

Here the compiler is evaluated with every newly requested word at its
actual current value, including words later used as boundary coordinates.
To prove (C), saturation is a contraction and

    ||T_R(v_R)-v||₂ ≤ ||v_R-v||₂+||T_R(v)-v||₂.

For a fixed L² variable the second term tends to zero by domination by
`|v|`; for a compact L² family it tends uniformly to zero by a finite net.
Use this first at `q`, then at each action output. Actions are bounded,
bounded gates preserve strong convergence, and the rank contractions
converge by Cauchy–Schwarz. Every exact intermediate field and velocity
forms a compact L² curve by the curve rules in the dependency packet.
This proves the induction, including uniformity in time.

The same assertion is valid with the training-law integral in place of the
finite sum. A derivative follows one branch of a finite graph, hence each
term has one training integral and finitely many current contractions.
For fixed words, the relevant integrands are jointly continuous in time
and input in L²; their domains are compact. Finite nets give uniform
saturation convergence over that family. Approximation of the law then
uses the Banach-valued modulus argument of C.4.2.3. This verifies
consistency with general fixed Borel laws, not just orthogonal two-atom data.

Equation (C) is a consistency statement on the known target. It is not an
error estimate for the closed systems introduced next.

## 4. Actual finite autonomous systems

Set `R=j`. For every dynamic primitive of `P_j`, form its complete finite
compiled right side from §3 with training law `μ_j`. Let `B_j` consist of
all primitive coordinates in these finitely many right sides that are not
already dynamic primitives or frozen seeds. Close this finite list under
primitive ancestors needed for evaluation. Every member has a finite
Gaussian initial value by §2.

In the finite system the coordinates of `B_j` are frozen at those jointly
initialized values. They are **initial** observations, not stored past
training states. Let `X_ℓ` collect, in one vector:

1. the dynamic primitives of population `ℓ`;
2. all frozen seeds and `B_j` coordinates of that population;
3. initial copies of every dynamic primitive.

If these three counts are `d_ℓ,b_ℓ,s_ℓ` (with the initial copies included
explicitly), then the retained population dimension is their sum,
`m_ℓ=d_ℓ+b_ℓ+s_ℓ<∞`. Each count is obtained by finite enumeration and finite
compilation. All finite same-layer joints are marginals or pushforwards of
`P_ℓ=Law(X_ℓ)∈P₂(R^{m_ℓ})`; no additional replica or joint is hidden.
There are two population types and no continuous state mark domain.
Dictionary observations have finite discrete labels. Their number can be
enormous but is independent of network width.

Evaluate every deterministic coordinate node from its primitive ancestors.
Evaluate an action node by reading its one specified coordinate of `X_ℓ`.
It never accepts an arbitrary vector. Evaluate every scalar contraction
by integration against the current joint law of its own population. With
these evaluation rules, the explicit closed equations are

    ∂_t P_ℓ + div_x(P_ℓ b_j^ℓ(x;P₁,P₂))=0,                 (PDE-j)

where the drift of a dynamic primitive is precisely its compiled `D_j`
formula, and the drift of every other coordinate is zero. Equivalently,

    X_ℓ'(t)=b_j^ℓ(X_ℓ(t);Law(X₁(t)),Law(X₂(t))).            (ODE-j)

The equations are autonomous. They store no time coordinate, history,
current middle matrix, raw parameter distribution, or arbitrary-vector
action interface. Their only external data are Gaussian initialization,
fixed dictionary/cutoffs, and the fixed quadrature weights.

The readout does not cause an unbounded drift coefficient. Every second
activation is recomputed as tanh of its action primitive, and hence lies
in `[-1,1]`, even when that primitive is inaccurate. If
`C(t)=||c(t)||∞`, the readout equation gives

    C(t) ≤ C(0)+2∫₀ᵗ(C(s)+Y)ds.

Starting at zero, iteration of this integral inequality yields
`C(t)≤Y(e^{2t}-1)`. For a globally Lipschitz extension, replace occurrences
of `c` in evaluating the drift by a fixed smooth nonexpansive clip equal
to the identity on `[-C_*,C_*]`, with `C_*>Y(e^{2T}-1)+1`.
Choose the clip to satisfy `|clip(c)|≤|c|`. The same inequality proves that
this auxiliary extension is inactive on every population solution through
T. A larger fixed `C_*` accommodates initial supremum at most one in §5.
This clip is a bounded auxiliary operation of the finite equations, not a
change to the Gaussian initialization or the target activation.

For fixed `j`, all scalar coefficients of the drift are bounded and
globally Lipschitz functions of the two laws in `W₂`. Indeed each
integrand is a bounded Lipschitz function of a finite primitive vector:
products have bounded parents, and action outputs are coordinate reads
followed by the stipulated saturation whenever used in velocities.
For such an integrand `f`, any coupling gives

    |∫f dP-∫f dQ| ≤ Lip(f) W₂(P,Q).

Every drift component is consequently bounded and Lipschitz jointly in
its finite coordinates and the two current laws, with some finite constant
`L_j`. The constant is allowed to grow with `j`.

Here is a direct well-posedness proof. Realize each finite initial law on
its own Gaussian probability space. On the product of the two path spaces
`C([0,h];L²)`, the integral right side of `(ODE-j)` is a contraction for
sufficiently small `h`, because the identical-carrier coupling gives
`W₂(Law X,Law Y)≤||X-Y||₂`. The same estimate shows uniqueness.
Iteration constructs the solution on every finite interval; bounded drift
prevents finite-time escape. Taking laws gives `(PDE-j)` and preserves
positivity and total mass. Thus these are genuine autonomous finite
population systems, with no signed characteristic-function surrogate.

They need not obey all exact algebraic/action identities of an actual
middle operator. In particular the finite construction does not preserve
every adjoint contraction or a common operator norm. This limitation is
central to the remaining proof gap, not an omitted implementation detail.

## 5. Fixed-order Gaussian finite-array bridge

At each separately fixed `j`, initialize a finite particle vector by
evaluating the complete union of §2's programs on the actual initialized
network arrays. Include the actual independent finite readout
`W_i^(3)∼N(0,1/n²)` in its moving readout coordinate; do not set it to zero.
Use the same initial array in both matrix orientations and retain every
initial/current copy in the same neuron tuple.

The zero-readout version of this finite union obeys III.F.1–7. Its bounded
products admit smooth Lipschitz extensions on their prescribed bounded
parent ranges. For the actual readout,

    P(max_i |W_i^(3)|>ε) ≤ 2n exp(-n²ε²/2) → 0,
    E[||W^(3)||₂²/n]=n⁻².

On the initialized operator-norm event, finite instruction-by-instruction
subtraction propagates this vanishing readout discrepancy through every
node. Both its RMS and its supremum vanish, so every fixed bounded parent
range is legitimate with arbitrarily small fixed slack. Consequently the
actual initial empirical joint laws converge in probability in `W₂` to
the prescribed population initial laws, including actual second moments.

Evolve these finite particles with `(ODE-j)`, replacing population
contractions by empirical contractions. This is a **probe surrogate**, not
the original finite network training algorithm. Couple any two initial
joint laws and solve their deterministic characteristic equations on that
coupling. The Lipschitz estimate gives, for the sum of the two population
L² distances `e(t)`,

    e(t) ≤ e(0)+C_j∫₀ᵗ e(s)ds,
    sup_(t≤T)e(t) ≤ exp(C_jT)e(0).

The exponential bound follows by iterating the integral inequality (or
differentiating its integral upper bound). Taking the infimum over initial
couplings proves the corresponding `W₂` bound. Thus for each fixed order
the actual-Gaussian-initialized finite probe surrogate converges to
`(PDE-j)` uniformly in time in every retained joint `W₂` law.

No independence of trained coordinates is needed: finite empirical laws
themselves solve the measure equation, and the deterministic law stability
estimate applies. There is no exchange of an increasing program limit with
the width limit. This bridge identifies the finite **surrogate** only.
It supplies no comparison to the actual finite-network GF after time zero.

## 6. The first missing estimate

For each fixed order, bounded drift proves finite second moments on `[0,T]`.
Its bound depends on that order. It does not prove, for a fixed low primitive
`V` followed across orders,

    lim_(M→∞) sup_j sup_(t≤T)
       E[|V_j(t)|² 1_(|V_j(t)|>M)] = 0,                    (UI)

or a time equicontinuity estimate with a constant independent of `j`.
For example the first-row drift contains `T_j(q_j)`; its elementary bound
is proportional to `j`, and no common actual-action norm controls `q_j`.
Higher action velocities contain the same issue recursively. Constants
from fixed-graph Lipschitz well-posedness therefore do not yield (UI).

The target's passive Gaussian tails do not imply tails for these closures.
The tails in the dependency packet were proved for actual raw Euler
programs, whose forward and reverse calls reuse one bounded operator and
whose learned increment is a sum of the correct ranks. A boundary-frozen
probe system is not such a program at positive time. Its initialized
Gaussian law alone does not recover those structural hypotheses.

The finite upward rule also does not make boundary influence small.
Differentiating one low coordinate requests finitely many higher ones;
iterating its integral equation requests successively higher levels.
At each order a new terminal derivative has been replaced by zero.
To estimate the resulting defect, one needs a bound on propagation of
this omitted information through the intervening levels. None of
`finite upward dependency`, `each finite system is Lipschitz`, or
`pointwise consistency (C)` gives that bound.

Thus the precise earliest unresolved obligation for this witness is
compactness plus consistency **on its own approximate trajectories**:
fixed-coordinate `W₂` tightness and time equicontinuity, and vanishing
cutoff terms when passing the integrated weak equations. It is not merely
an unknown numerical convergence rate. No closed-family subsequence has
yet been shown to satisfy the full exact hierarchy.

### Two exact checks against shortcuts

**L² boundedness is insufficient for W₂ compactness.** The probability laws

    ν_m=(1-m⁻²)δ₀+m⁻²δ_m

converge weakly to `δ₀`, have second moment one, and satisfy
`W₂(ν_m,δ₀)=1`. This directly blocks a passage from characteristic-function
compactness plus an L² bound to the requested topology.

The problem survives even on a common bounded raw ball with the canonical
initialized action. On its nonatomic population 2 choose sets `E_m` of
probability `m⁻²`, put `b_m=m 1_(E_m)`, and let

    K_m=b_m⊗1,     A_m=A₀+K_m,     w_m=g,     c_m=0.

Then `||K_m||HS=1` and `||A_m||≤||A₀||+1`. For the allowed observation
`A_m1=X+b_m`, where `X=A₀1∈L²`, the laws converge weakly to `Law(X)`:
outside `E_m` the variables agree. But

    E|X+b_m|² = E|X|²+1+2E[X b_m],
    |E[X b_m]| ≤ ||X 1_(E_m)||₂ → 0.

The last convergence is absolute continuity of the integral of `|X|²`.
The second moments therefore gain one, so these laws have no `W₂`
convergence to their weak limit. These are arbitrary raw states, not
asserted reachable states. The example refutes using only the established
raw-ball bounds to obtain the required compactness.

**A compact bounded hierarchy need not select a unique curve.** Let
`h(t)=exp(-1/t²)` for `t>0` and `h(t)=0` for `t≤0`. Every derivative for
positive t is a polynomial in `1/t` times `h(t)`, by differentiation;
such products tend to zero at zero. Hence `h` is smooth with every
derivative initially zero. On `[0,T]` select finite positive constants
`M_k≥max(1,sup|h^(k)|)`, and define

    x_k'=a_k x_(k+1),   a_k=M_(k+1)/M_k,   x_k(0)=0.

Both the zero curve and `x_k(t)=h^(k)(t)/M_k` solve every equation, and
both remain in the compact product `[-1,1]^N`. Each coordinate is smooth;
the dependency is exactly one level upward. Freezing a terminal coordinate
at zero produces a unique all-zero finite system. Thus compactness,
boundedness, exact upward identities, and agreement of all initial data
do not by themselves identify an infinite solution. This example is a
logical check, not a network counterexample or a proposed playback model.

## 7. The separate dynamic-identification gap

Suppose the first gap were repaired and a compatible hierarchy curve
`H(t)` satisfying all exact weak equations were obtained. At every fixed
time its complete joint laws might reconstruct observable probability
algebras and an action, provided all algebraic relations, adjunction,
and bounded-action inequalities were verified. That is a **static**
reconstruction. It does not yet give one pair of probability spaces on
which the reconstructed fields solve (H2) strongly in time, with
Hilbert–Schmidt middle increments from the canonical initialized action.

The natural distribution-space idea is to use a superposition construction
for the countable joint coordinate continuity equations. Even granting
such a construction, one would have to prove that:

* all coordinate algebra identities and both action directions survive;
* the time-dependent generated L² spaces can be represented coherently on
  fixed carriers;
* the reconstructed actions satisfy `A(t)-A(0)=∫₀ᵗ A'(s)ds` in HS norm
  with exactly the rank velocity in (H2), rather than merely having the
  correct separate-time distributions;
* the initial action on those carriers is the prescribed common Gaussian
  action, without additional unobserved randomness affecting continuation.

No superposition or lifting theorem with these checked conclusions is
proved here or supplied by the inputs. The countable coordinate law alone
does not specify cross-time couplings. Adding a full trajectory law as a
finite population coordinate would violate the contract.

If a strong lift with these properties were established, canonical
identification would then be direct: apply the dependency packet's
one-reference raw comparison to the lift and the canonical solution,
use only the latter's exponential query tails, and integrate the Osgood
bound with zero initial discrepancy. It forces equality of the raw paths.
The candidate's observation passage would then give all required joints,
their second moments, and whole-circle prediction. This final implication
is available; the hypotheses needed to invoke it are not.

## 8. Claim ledger and route disposition

| Claim | Status | Reason |
|---|---|---|
| Finite dictionary and finite joint dimensions at each order | Proved construction | Literal finite enumeration and one joint vector per population |
| Joint Gaussian initialization with both orientations | Established dependency applied | Complete finite union meets III.F/H6 hypotheses |
| Explicit autonomous finite population equations | Proved construction | `(F±)`, primitive evaluation, and `(ODE-j)` |
| Fixed-order existence, uniqueness, positivity, and mass | Proved | Bounded Lipschitz drift and L² contraction construction |
| Fixed-word cutoff consistency on canonical paths | Proved | Compact L² saturation and finite tangent induction |
| Fixed-order finite-array surrogate bridge | Proved | Gaussian program initialization and deterministic W₂ flow stability |
| Order-uniform compactness/tail control of the finite closures | Open; first indispensable gap | Existing bounds and source tails apply to different trajectories |
| Limit satisfies the complete exact hierarchy | Open | Depends on the previous gap and passage of cutoff terms |
| Formal hierarchy curve admits the required strong canonical lift | Open; separate major gap | Static reconstruction and reached restart are insufficient |
| Uniform-time whole-circle and every fixed C-H1 joint W₂ convergence | Not proved | Both preceding bridges are missing |
| Nonexistence of any admissible C-H2 family | Not claimed | Failure of this witness's proof does not decide existence |

The hierarchy route should be recorded as **incomplete, with an explicit
finite witness and two isolated major gaps**. Reopening it requires a
structural invariant that controls approximate current actions/tails and
survives finite closure, or a checked dynamic realization theorem that
also provides the missing compactness mechanism. Replacing these steps by
Taylor convergence, a moment representation, Gaussianity of learned
answers, or formal-hierarchy uniqueness would not repair the route.
