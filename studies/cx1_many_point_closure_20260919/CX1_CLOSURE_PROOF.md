# C-X1: dimension-general observable closure and executable numerical hierarchy

Status: conditional closure theorem proved below; independent review pending.
This is a proof unit of this study, not a proof of the study's long-horizon
canonical-flow input, learning bound, or geometric radius. Those obligations
are stated explicitly in §1. No training experiment supports any assertion here.

## 1. Precise input and conclusion

Fix integers d,m≥1, a finite time T, Y<∞, unit directions u_a∈S^(d−1),
labels |y_a|≤Y, and probabilities p_a≥0 with sum one. Mean loss uses p_a=1/m.
The original inputs are x_a=√d u_a. The network has two tanh hidden layers,
independent stored Gaussian variances (1,1/n,1/n²), output cᵀh₂/n, and
mobilities (n,1,n), with unhalved mean squared loss. Finite random readout is
retained in the network; its population limit is zero.

**Input C (to be supplied by the canonical-flow proof unit).** On the canonical
initialized Gaussian action carrier, A₀:L²(Ω₁)→L²(Ω₂) and its actual adjoint
have norm at most two. There is a strong C¹ solution θ=(w,K,c),
A=A₀+K, through T, with initial (g,0,0), g∼N(0,I_d), and

    h₁(u)=tanh(w·u),  z₂(u)=A h₁(u),  h₂(u)=tanh z₂(u),
    δ₂(u)=c(1−h₂(u)²),  q(u)=A*δ₂(u),  f(u)=E₂[c h₂(u)],
    r_a=f(u_a)−y_a,
    w'=−2Σ_a p_a r_a (1−h₁(u_a)²)q(u_a)u_a,
    K'=−2Σ_a p_a r_a δ₂(u_a)⊗h₁(u_a),
    c'=−2Σ_a p_a r_a h₂(u_a).                         (1)

Its raw state space is L²(Ω₁;R^d) ⊕ HS(Ω₁,Ω₂) ⊕ L²(Ω₂), c is bounded,
and for finite constants C₀,a₀>0

    sup_(t≤T) Σ_a p_a ||q(t,u_a) 1_|q(t,u_a)|>R||₂
                   ≤ C₀ exp(−a₀R),  R≥1.             (2)

A uniform subGaussian bound is stronger than (2). The canonical flow has the
actual finite-GF interpretation, including whole-sphere prediction and fixed
same-population finite joint initialized/current/action observations in W₂.
The finite Gaussian program rule used below is the initialized rule in
`docs/global_nonlinear.md` §3 and C.4.7.8.3, for the actual reused matrix.
All constants may depend on fixed d,m,Y,T and the admitted data family, but
not on closure order or numerical resolutions. Only the canonical target
needs (2). A theorem giving (2) uniformly in passive u can be used directly;
this closure comparison itself only requires its training average.

**Conditional theorem.** Under Input C, the explicit nested dictionaries in
§3, initialized by §2 and evolved by §4, are autonomous and restartable.
They converge to this same canonical flow uniformly in time in row L²,
learned-increment HS, and readout L² on the canonical carrier. Predictions
converge in C([0,T]×S^(d−1)). Every separately fixed admissible same-population
joint observation tuple from §2 converges uniformly in time in Euclidean W₂,
including frozen/current hidden pairs, either action orientation, bounded-gate
pushforwards, and quadratic contractions. The finite numerical implementation
has the iterated convergence in §6. No parameter depends on neuron width or
elapsed step count. No monotone order error, useful order rate, arbitrary
refinement diagonal, practical high-order cost, or finite-resolution accuracy
certificate is asserted.

The proof works for every fixed finite data set for which Input C is available;
m≤d and proximity to coordinate axes are conditions of the separate canonical
learning theorem, not restrictions inserted into closure coefficients. A
learning horizon supplied by that theorem is used unchanged. In particular,
a short-time version of Input C would only yield short-time closure.

## 2. H1: current information, joint Gaussian initialization and sufficiency

Use the maintained two-population observation language with d first-coordinate
seeds w_i,g_i instead of two. The other seeds are c, constants on both
populations, and frozen z₂⁰(v)=A₀ tanh(g·v), v∈S^(d−1). There are two sorts:
bounded and L²; bounded is also L². Affine operations preserve the sort,
sin/cos/tanh send L² to bounded, products require two bounded parents, and
A or A* accepts a bounded parent and returns L². Products of arbitrary L²
fields followed by an action are not admitted. A named bounded continuous
gate times a named L² field may be read as a joint-law pushforward, without
being an unrestricted multiplication instruction. c has a uniform bound
along each trajectory considered here, derived below.

At level j retain every correctly typed acyclic program with ≤j nodes,
and every same-population tuple of ≤j nodes, keeping its scalar/direction
marks. For fixed d,j there are finitely many graph types and finite-dimensional
mark domains. Take graph unions before joint evaluation; separate marginals
cannot replace a same-neuron tuple. Characteristic tests E cos(λ·V),
E sin(λ·V) determine each finite law. Cross-layer neuron pairing is neither
used nor asserted. Directions live on the whole sphere.

For initialization replace w by g, c by zero and A by A₀. Expand every
frozen upper seed into its finite affine projection, tanh and action. Keep
independent centered Gaussian source groups ξ on Ω₂ and ζ on Ω₁, independent
of g. In the causal finite program the exact rules are

    A₀ b = ξ_b + Σ_(earlier reverse j) d_j E₁[∂_(ζ_j)b],
    A₀*d = ζ_d + Σ_(earlier forward i) b_i E₂[∂_(ξ_i)d].  (3)

Source covariances are the *uncentered* operand Grams E₁[bb'] and E₂[dd'].
Derivatives differentiate full earlier coordinate expressions with deterministic
coefficients and source covariances frozen. A previous response term is
therefore differentiated too. Both groups are independent Gaussian sources;
the answers are not independent operators. A new source in an old group C
with covariance vector v and variance s is vᵀC†ξ+√(s−vᵀC†v)G. Positivity of
the extended operand Gram gives v⊥ker C and s−vᵀC†v≥0: test (tz,1) for
z∈ker C and then complete the square on range C. Thus singular or repeated
queries are included. Every requested tuple is built by one complete finite
union, not independent initialization of coordinates.

Bounded operands and smooth gates give finite polynomial envelopes in the
finite Gaussian source lists, also for every fixed named-source derivative.
At action nodes this follows from source plus finite bounded response inputs;
coordinate chain/product rules preserve such envelopes. Thus all expectations
exist. Each product of bounded parents can be replaced, for the finite-program
theorem, by a smooth globally Lipschitz product extension agreeing on their
known bounded ranges. Its bounded first derivatives and all other coordinate
instruction hypotheses are then satisfied. The finite Gaussian program theorem applies in any fixed dimension:
there are finitely many Gaussian first seeds, correctly typed calls of both
orientations of one Gaussian matrix, and smooth bounded operands/derivative
envelopes. It gives precisely (3) and the finite-neural initialized joint W₂
interpretation. Finite stored c has P(max_i|c_i|>ε)≤2n exp(−n²ε²/2), so its
replacement by zero occurs only in this population limit.

For clarity, the hierarchy also has exact finite upward weak equations.
Reverse-differentiate EΨ(V) for Ψ=sin/cos(λ·V). Affine/gate/product nodes
have their ordinary chain rules. An A b node sends A*p to b and records
(p,b,+); an A*b node sends Ap and records (p,b,−). Frozen seeds have zero
time derivative. Pairing each unprocessed covector with its velocity shows
that every reverse step preserves the chain-rule sum. Substitution of (1)
therefore gives

    (EΨ(V))' = −2Σ_a p_a r_a {
      E₁[(u_a·p_w)(1−h₁(u_a)²)q(u_a)] + E₂[p_c h₂(u_a)]
      + Σ_+ E₂[p δ₂(u_a)] E₁[b h₁(u_a)]
      + Σ_- E₁[p h₁(u_a)] E₂[b δ₂(u_a)] }.             (4)

All pairings are L²×L² or contain a bounded multiplier. C¹ chain rules follow
from the mean-value identity and this multiplier fact: if z_n→z in probability,
v_n→v in L² and β is bounded continuous, then β(z_n)v_n→β(z)v in L².
Subtract v_n−v, truncate fixed v, use bounded convergence on the bounded part,
then remove truncation. This avoids claiming an L² algebra or global Frechet
differentiability.

To read (4) from a finite higher level, replace each backward covector action
or bounded multiplication on p by its operation on R tanh(p/R). This gives
admissible bounded operands at every step. Since saturation is 1-Lipschitz,
contractive in L², and converges to identity, finite reverse induction gives
p^R→p in L². Uniformity on compact time curves follows from a finite L² net.
A loose bound 10⁶(j+d+1)⁶ on nodes and tuple length covers the entire compiler,
including a new d-coordinate input projection. The R limit does not increase
node count; it is a scalar mark. H1 alone is not finite scalar storage.

Let H_l^obs be L² of the sigma-field generated by all finite initialized words.
Rational marks suffice: inductively approximate a real marked graph in L²,
using bounded actions, Lipschitz gates, and local bounded syntax envelopes.
Bounded word spans are dense. Indeed measurable finite cylinders approximate
L² variables by simple functions and truncation. On each finite tuple, sines
and cosines of affine forms are dense: an orthogonal function defines a finite
signed measure with zero Fourier transform; convolution with a Gaussian has
zero density by its elementary Gaussian Fourier integral and Fubini. Letting
the variance decrease to zero annihilates every bounded Lipschitz test and
hence every Borel set, using continuous approximations of indicators. This
proves density without moment determinacy.

Actions of bounded words are words, so boundedness and density show A₀ and A₀*
map these spaces into one another. Adjointness makes them a reducing pair:
A₀P₁=P₂A₀ for their orthogonal projections. The full flow remains in them.
Here is the needed justification rather than an assumption of invariance:
Euler steps from initialization remain in the generated spaces and add ranks
between them. On a finite horizon their bounded gates imply common bounds on
c, A and w and on speeds; for example ||c_(k+1)||∞+Y≤(1+2h_k)(||c_k||∞+Y).
Comparison against the tail-bearing target gives

    e' ≤ C(1+R)(e+Vh)+C exp(−a₀R).                       (5)

The changed lower gate is split at |q_target|=R; other factors are Lipschitz
on the common ball. Taking R=1+a₀^−1 log(1/v) for v=e+Vh+ε≤1 gives
v'≤Lv log(e/v), hence

    v(t)≤exp(1−α(t)) v(0)^α(t),  α(t)=exp(−Lt)>0.      (6)

Integrate z=log(e/v), z'≥−Lz, and use first exit from v≤1. Send ε↓0 and
h↓0. Thus Euler converges to the target, and closedness gives its membership
in H_l^obs and K(t),K'(t) in their HS block.

The same argument proves reached sufficiency for the *complete current*
hierarchy. Equal finite joint laws define unital L² isometries on bounded
cylinders, extend by density, preserve bounded measurable operations, and
intertwine the current A,A*. These spaces reduce the reached action. Restarted
Euler plus (5)–(6) proves future invariance; transporting the canonical
continuation by the isometries gives a strong continuation of any matching
bounded-action, bounded-readout realization, with constant complementary action.
Against this transported reference (5)–(6) forces uniqueness of any competing
strong continuation, without imposing tails on it. Thus the complete hierarchy
is sufficient current information, not a uniqueness claim about arbitrary
formal moment sequences. Only the remaining portion of the supplied horizon
is asserted at a reached restart.

## 3. A dense dimension-general dictionary, with genuine enrichments

Put, for i=1,…,d,

    h_i=tanh g_i, ξ_i=A₀h_i, H_i=tanh ξ_i,
    R_i=A₀*H_i, k_i=tanh R_i,
    v=E tanh²G, τ=E tanh²(√v G), α=1−τ.

Formula (3) gives jointly ξ∼N(0,vI_d), R=√τ Z+αh, with independent lower
standard Gaussians (g,Z). All v,τ,α are strictly positive. Retain every
Chebyshev product of total degree ≤N in X₁=(h,k)∈(−1,1)^(2d) and in
X₂=H∈(−1,1)^d. Use total degree followed by descending lexicographic order.
The recurrence T₀=1,T₁=x,T_(k+1)=2xT_k−T_(k−1) expresses every product
as a bounded observation word. T_k(cos θ)=cos(kθ) proves its actual bound one;
the implementation may keep a larger finite syntax bound.

The following exhaustive tail is essential; the core alone is not assumed to
generate the full Gaussian action space. Codes 0,1 are population constants,
and codes 2,…,d+1 are g₁,…,g_d. For n=d+2+8k+j, j=0,1,2,3 means
sin,cos,tanh,action applied to code k. For j=4,5,7 Cantor-unpair k=(a,b)
and use add,multiply,add. For j=6 multiply code b by rational r(a), where
Cantor-unpair a=(s,t), r(a)=signed(s)/(t+1), signed(0)=0,
signed(2h−1)=h, signed(2h)=−h. Reject invalid types and their dependents.
Every dependency is strictly below its code; every finite rational tree has
a code by recursively pairing upward. DAGs unfold into finite trees.

At order N append *every bounded valid code ≤N*, retaining duplicates even
when the same function or literal word is already in the polynomial core.
This explicit choice differs harmlessly from maintained duplicate suppression.
The raw counts are at most binom(N+2d,2d)+N+1 and binom(N+d,d)+N+1. The
raw spans are nested, although coordinate list positions need not be prefixes.
They are dense in H_l^obs by exhaustion and §2's bounded-cylinder proof.

The core spans strictly increase: (g,R) has positive joint density on R^(2d),
and the coordinatewise tanh map gives X₁ positive density on its open cube;
X₂ has the analogous property. A polynomial vanishing almost surely vanishes
on the open cube by continuity, hence identically by successive one-variable
root arguments. Chebyshev products have distinct leading monomials, so their
span dimensions are exactly binom(N+2d,2d) and binom(N+d,d).

Odd enrichments also carry genuinely new action information. For odd k≥3 let
P_k be the monic degree-k polynomial orthogonal to lower-degree polynomials
under H₁'s positive density. The positive Gram guarantees existence. Symmetry
makes P_k odd. Its k roots are simple and interior: otherwise the product of
its fewer than k sign-changing interior roots would have lower degree and
would give a fixed-sign nonzero pairing with P_k, contradicting orthogonality.
Interpolate artanh at those roots by L of degree k−1. Repeated Rolle gives

    P_k(x)(artanh x−L(x))
       = artanh^(k)(ξ_x) P_k(x)²/k! >0

off the roots, since artanh^(k)(x)=(k−1)![(1−x)^−k+(1+x)^−k]/2>0.
The product is integrable because artanh(H₁)=ξ₁ is Gaussian and P_k bounded.
Thus E[P_k(H₁)ξ₁]>0. Independence makes P_k(H₁) orthogonal to every upper
core polynomial of total degree ≤k−2, but

    E₂[P_k(H₁)A₀h₁]=E[P_k(H₁)ξ₁]>0.                       (7)

At the executable first transition N=1→3, the prefix contains only constants
and seeds (or, for d=1, sin(1)); therefore it adds no nonconstant upper feature.
Equation (7) proves new action information beyond the whole previous upper
span, not only a larger coefficient array. No claim that every new even order
changes a particular odd trajectory is made.

Let ψ_l be the entire raw dictionary, G_l=E_l[ψ_lψ_lᵀ],
η_N=1/[1024(N+1)²], L_l L_lᵀ=G_l+η_NI, and b_l=L_l^−1ψ_l. Set

    C_N=E₂[ψ₂(A₀ψ₁)ᵀ],  D_N=L₂^−1 C_N L₁^−T.            (8)

Compute C_N by the complete finite program: append A₀ on each lower feature,
and, for diagnostics, A₀* on each upper feature, before any joint expectation.
The program includes all dependencies. Runtime reverse is D_Nᵀ, not a second
independently estimated matrix. The familiar core-only reduction is valid in
every d,

    E₂[B A₀F] = Σ_i E₁[Fh_i]E₂[∂_(ξ_i)B]
                 + Σ_i E₁[∂_(ζ_i)F]E₂[BH_i],            (9)

by appending A₀F in (3), regressing its Gaussian source on ξ, and integrating
E[Bξ_i]=vE[∂_(ξ_i)B] by parts. Both terms are required. The implementation
uses the generic program at all orders, so it does not accidentally apply
(9) when exhaustive-tail features contain additional sources.

If U_l a=b_lᵀa and Q_l=U_lU_l*, then ||U_l||≤1 and
Q_l=S_l(G_l+η_NI)^−1S_l*, where S_la=ψ_lᵀa. Diagonalization gives

    ||(I−Q_l)S_la||²
      = Σ_j η_N²λ_j/(λ_j+η_N)² |a_j|² ≤ η_N|a|²/4.     (10)

Represent a fixed earlier word combination at every later order by its fixed
coefficients placed in the corresponding list entries; their Euclidean norm
is unchanged. Density, (10), and ||I−Q_l||≤1 prove Q_l→I strongly on H_l^obs,
without any smallest Gram eigenvalue bound. Hence

    B_N=U₂D_NU₁*=Q₂A₀Q₁ → A₀,
    B_N* → A₀*,       ||B_N||≤2,                         (11)

strongly. Both convergences are uniform on compact L² subsets by finite nets.

## 4. H2: autonomous finite population equations and well-posedness

Save M∈R^(k₂×k₁), fixed D_N, and exactly two current joint populations:
Γ₁=Law(b₁,g,w) on R^(k₁+2d), Γ₂=Law(b₂,c) on R^(k₂+1).
Initially M=D_N, Γ₁=Law(b₁,g,g), Γ₂=Law(b₂,0). The static mark marginals
and their correlations are part of these joint laws. For every sphere input,

    a(u)=E₁[b₁ tanh(w·u)], z₂,N(u)=b₂ᵀM a(u), h₂,N=tanh z₂,N,
    d(u)=E₂[b₂ c(1−h₂,N(u)²)], q_N(u)=b₁ᵀMᵀd(u),
    f_N(u)=E₂[c h₂,N(u)], r_N,a=f_N(u_a)−y_a,
    w_N'=−2Σ_a p_a r_N,a (1−tanh²(w_N·u_a))q_N(u_a)u_a,
    c_N'=−2Σ_a p_a r_N,a h₂,N(u_a),
    M_N'=−2Σ_a p_a r_N,a d(u_a)a(u_a)ᵀ.                 (12)

The laws push forward under these characteristics; their other coordinates
are frozen. Equation (12) is a finite population system, not finite scalar
storage until quadrature. It has no missing-level call, cutoff limit, action
oracle, target-dependent coefficient, time coordinate, or retained transcript.
On the canonical carrier its action is A_N=B_N+K_N, with

    K_N=U₂(M_N−D_N)U₁*,
    K_N'=Q₂[−2Σ_a p_a r_N,a δ₂,N(u_a)⊗h₁,N(u_a)]Q₁.     (13)

This is filtering on both factors, not projection of w,c onto the dictionary.

For each fixed N all b coordinates are bounded. Use bounded increments w−g,
bounded c, and finite M as a Banach state. The RHS is locally Lipschitz there:
tanh and its gate are Lipschitz, g is fixed inside gates, all other products
have bounded factors, and expectations have norm at most one. The integral
map on a sufficiently short time interval maps a closed ball into itself and
contracts if time times the local Lipschitz constant is <1. Its Cauchy iterates
give the unique local solution. This argument also covers atomic mark laws.

Differentiating the mean loss gives

    L_N'=−||w_N'||₂²−||c_N'||₂²−||M_N'||_F².              (14)

For example δf=dᵀ(δM)a; the M loss gradient is 2Σ p r daᵀ, and its adjoint
backpropagation gives the other two gradients in their population L² metrics.
Thus Σ p|r|≤Y, and contraction of U_l gives

    ||c_N(t)||∞≤2Yt, ||M_N−D_N||_F≤2Y²t²,
    ||A_N(t)||≤2+2Y²t²,
    ||w_N(t)||₂≤√d+4Y²t²+2Y⁴t⁴.                         (15)

The M speed bound is 4Y²t since |a|≤1, |d|≤2Yt; the row speed bound is
4Y²t(2+2Y²t²). At fixed order |q_N|≤|b₁| ||M|| |d|, so w−g also remains
bounded in supremum norm. Bounded speeds give endpoint limits and local
continuation prevents escape at any finite time. The same characteristic
argument from saved Γ₁,Γ₂,M gives unique own-state restart, including their
conditional joint correlations. No elapsed time is required by the equations.

## 5. Convergence on the supplied horizon and all declared observations

Input C's energy follows from the strong chain rule for the finite sum in
(1); the bounded c hypothesis justifies its first derivative. It gives the
same raw bounds as (15), with K replacing M−D. Thus target and approximants
occupy one bounded raw/action ball independent of N.

Joint continuity in (t,u) of h₁,δ₂ follows from strong raw continuity and the
bounded-multiplier lemma; the sphere is compact for every fixed d, including
the two-point sphere for d=1. Therefore their images are compact L² sets.
K' is a compact HS curve supported on the observable block by §2. Equations
(10)–(11) imply the vanishing consistency source

    ε_N = sup_(t,u)||(B_N−A₀)h₁(t,u)||₂
        + sup_(t,u)||(B_N*−A₀*)δ₂(t,u)||₂
        + sup_t||Q₂K'(t)Q₁−K'(t)||_HS →0.               (16)

For the last term approximate an HS operator by finite sums of ranks, apply
strong Q convergence to their factors, and use contraction on the remainder;
a finite net of the compact curve makes this uniform. Equation (16) produces
the missing-source bound. It is a proof quantity, never an algorithm input or
an order-selection oracle.

Set e_N=||w_N−w||₂+||K_N−K||_HS+||c_N−c||₂. Forward subtraction uses

    z₂,N−z₂=A_N(h₁,N−h₁)+(K_N−K)h₁+(B_N−A₀)h₁,

so hidden and prediction errors are ≤C(e_N+ε_N), uniformly in u. For upper
backward fields first subtract c_N−c and use bounded target c. For q subtract
A_N*(δ₂,N−δ₂)+(K_N−K)*δ₂+(B_N*−A₀*)δ₂. Their errors have the same bound.
The remaining lower-gate difference obeys

    ||(1−h₁,N²)q_N−(1−h₁²)q||₂
       ≤C(e_N+ε_N)+2R e_N+2||q1_|q|>R||₂.               (17)

Use gate Lipschitz constant two below R and bounded gates above it. Only q
of the target is truncated. The middle difference is exactly

    K_N'−K'=Q₂(F_K(θ_N)−F_K(θ))Q₁ +(Q₂K'Q₁−K'),         (18)

and the rank inequality ||a⊗b−a'⊗b'||_HS≤||a−a'||₂||b||₂+
||a'||₂||b−b'||₂ bounds it. Subtract residuals and the row/readout factors
in (12), sum the finite data weights, and apply (2), obtaining

    D⁺e_N≤C(1+R)(e_N+ε_N)+C C₀e^(−a₀R), e_N(0)=0.      (19)

Hilbert-curve norms are absolutely continuous; their norm derivative is bounded
by the velocity norm, also at zero in upper-derivative form. Applying (6) to
e_N+ε_N+ε proves sup_t e_N→0. A subGaussian input instead permits fixed-R
Gronwall followed by N→∞ and R→∞. Exponential tails require the Osgood cutoff
argument on a long horizon; fixed-cutoff Gronwall alone would not suffice.

The forward estimate proves uniform whole-sphere prediction. For any fixed
observation graph, bounded-node envelopes are common across N,t. Affine and
Lipschitz operations preserve L² convergence; products satisfy
||V_NW_N−VW||₂≤||V_N||∞||W_N−W||₂+||W||∞||V_N−V||₂.
For an action node,

    A_NV_N−AV=A_N(V_N−V)+(K_N−K)V+(B_N−A₀)V.              (20)

The last term vanishes uniformly on the compact target curve V(t); reverse
nodes use the same argument with actual adjoints. Frozen upper seeds are
B_N tanh(g·v), so they converge too. The multiplier lemma and a compact-curve
finite net give convergence of the declared bounded-gate pushforwards.
Induction proves all node errors tend to zero uniformly in t. On their shared
population carrier,

    W₂²(Law(V_N,1,…,V_N,k),Law(V₁,…,V_k))
                     ≤ Σ_i ||V_N,i−V_i||₂².             (21)

Quadratic contractions converge by Cauchy–Schwarz. This preserves initialized/
current pairs, their squared displacements and their RMS norms, not merely
separate marginals. Loss convergence follows from bounded predictions and
|a²−b²|≤|a−b|(|a|+|b|). The limit has the actual finite-network interpretation
by the separately supplied identification in Input C. No operator-norm
convergence of A_N−A, joint order/width rate, or raw-GD statement is inferred.

## 6. H3: actual finite arithmetic, quadrature and time limits

`cx1_closure.py` implements (8),(12) in all fixed d. Its dictionary matches
§3, including redundant bounded prefix outputs. `DimensionCompiler` reuses
the maintained finite-union structural compiler, frozen named-source reverse
AD, arithmetic and resource checks; it changes seed validation and the lower
Gaussian offset from two to d. It does not patch global modules. The generic
compiler is used at every order, including N=1 and the enriched N=3.

Numerical axes are independent: positive source regularization ε, Q coefficient
Gaussian points, P population replay points, J Heun steps, and precision b.
The finite data law is evaluated by its exact finite sum. For coordinates
specified only by convergent numerical representations, include a separate
finite-data approximation index s with μ_s→μ; rational sphere points exist
densely by stereographic coordinates, and near each axis its own chart suffices.
For exactly represented data the s limit is absent. No claim of computing
noncomputable real input constants is needed.

Source covariance at each compiler prefix is its full empirical operand Gram
plus εI. Its positive Schur pivot is kept; failure to resolve it raises an
error rather than deleting a mode. New source derivatives use frozen response
links and covariances. After all coefficients and G,C are computed at Q,
replay at P freezes them and evaluates the entire joint mark tuple, including
g. Empirical normalization uses the strictly positive η_N in (8). Both runtime
actions use one full M and Mᵀ. Numerical M is not constrained to the coordinate
blocks of a first-order initializer.

Here are the required numerical bridges, with their hypotheses verified.

1. **Gaussian cubature.** The maintained Halton/Box–Muller rule is jointly
   equidistributed and converges with every finite polynomial moment. For a
   base-b radical inverse U_(k,b), endpoint distances are ≥1/(bQ), and its
   interval discrepancy is O_b(log Q/Q), by splitting digit-aligned blocks.
   The Chinese remainder bijection proves joint rectangle frequencies.
   For X=−log U, layer cake bounds its empirical r-tail by
   L^r e^−L+∫_L^∞rt^(r−1)e^−t dt+D_(Q,b)log(bQ)^r. If log(bQ)>L≥r+1,
   the last expression is bounded uniformly in Q by a constant times
   L^(r+1)e^−L; otherwise its empirical tail is zero. Box–Muller radius
   squared is −2log U. Truncation away from endpoints, followed by these
   tails, proves joint Gaussian weak convergence and uniform moments,
   hence W_r convergence by coupling small cells on a bounded box and then
   discarding the moment tail. These arguments hold in every finite Gaussian
   dimension, without dimension-independent rates.

2. **Adaptive finite initialization.** At fixed ε>0 every source covariance
   prefix is positive definite. Every value, frozen-source derivative,
   coefficient and covariance is a continuous finite expression with a common
   polynomial Gaussian envelope on bounded coefficient sets. If θ_Q→θ, then
   E_Q F(θ_Q,z)→E F(θ,Z): use uniform continuity on a ball, then a higher
   moment for its complement. Induction in the finite causal program, using
   continuity of Cholesky at a positive definite matrix, proves the Q limit.
   At fixed Q,ε, frozen P replay converges in joint W₂ by the same envelope
   argument. After Q→∞ remove ε: represent each whole named source vector by
   its positive semidefinite covariance square root times standard normals.
   These roots are continuous, since bounded positive roots have subsequential
   limits, their squares converge, and the positive root is unique. Induction
   and the same Gaussian envelopes give (3), even at singular covariances.
   Formal derivative slots survive; no singular-Cholesky continuity is used.

3. **Mark-law stability at fixed order.** Each exact or empirical normalized
   feature has common bound |b_l|≤B_l/√η_N=:K_l, where
   B_l²=Σ_j||ψ_l,j||∞². This follows from G_l+η_NI≥η_NI and the inverse
   Cholesky singular values. For arbitrary probability mark laws with those
   bounds, finite D, and E|g|²<∞, the characteristic Picard proof applies.
   Its energy gives ||c||∞≤2Yt, ||M−D||_F≤2K₁K₂Y²t² and
   ||w'||∞≤4K₁K₂Y²t||M||_F. Couple two lower joint mark laws and two upper
   mark laws. Writing ρ_b=||b₁−b̃₁||₂+||b₂−b̃₂||₂, factor subtraction gives
   |a−ã|≤||b₁−b̃₁||₂+K₁||w−w̃||₂; splitting b₂ᵀMa then f,d,q gives a
   bound C(e+ρ_b) for each subsequent field. The lower product uses bounded
   q̃ (fixed finite features), so it too is Lipschitz. For distinct u,v,
   ||tanh(w·u)−tanh(w·v)||₂≤||w||₂|u−v|, and all remaining factors inherit
   this bound. Thus coupling μ,μ̃ adds CW₁(μ,μ̃) to the drift difference.
   Integrating and expanding the scalar Gronwall series yields

       sup_t e(t) ≤ e^(CT)[||g−g̃||₂+||D−D̃||_F
                            +CT(ρ_b+W₁(μ,μ̃))].         (22)

   All constants are finite at fixed N and along each convergent inner
   sequence. Exact empirical feature contraction is not assumed: the common
   envelope suffices. This removes data representation, P, Q and ε in order.

4. **Time discretization.** The maintained simultaneous Heun method updates
   w,c,M from the same old state at each stage. At fixed finite inputs/marks,
   with h=T/J, B_k=Y+||c_k||∞ obeys B_(k+1)≤(1+2h+2h²)B_k. Thus all stages
   have a common bound through fixed T. Bounds on M speed and then w speed
   follow from the bounded features, without a discrete energy assertion.
   On a larger bounded set the finite smooth field is Lipschitz. Its exact
   Euler defect and the Heun-to-Euler difference are O(h²), so
   e_(k+1)≤(1+Ch)e_k+Ch² and sup-time interpolated error tends to zero.
   Intermediate states are linearly interpolated, then nonlinear fields are
   recomputed. This is a numerical ODE method, not a raw neural-GD bridge.

5. **Arithmetic.** The maintained rational backend rounds to integer multiples
   of 10^−b. Basic operations and elementary-function series are locally
   uniformly consistent; integer square root has error below 10^−b,
   logarithm uses power-of-two reduction and its geometric atanh series,
   exponential uses reduction to |x|≤1/2 and guarded Taylor powering, and
   trigonometric evaluation uses a rational Machin pi approximation and its
   alternating series. At fixed finite Q,P,J and positive ε,η_N all exact
   source/normalization pivots have positive margins. Induction gives eventual
   success and convergence as b→∞; resource limits must be increased as
   needed. Rounded probability mass and rounded unit-sphere norms are checked
   with tolerance proportional to count or d times 10^(5−b); their rounding
   errors are O(count·10^−b) and O(d·10^−b), so these checks eventually pass.
   The latter generalizes the maintained circle validator explicitly. The
   finite computation is uniform over rounded sphere queries by compactness
   and local uniform arithmetic consistency. Float64 alone has no precision
   refinement guarantee.

Consequently the observation error tends to zero in the order

    lim_(N→∞) lim_(ε↓0) lim_(Q→∞) lim_(P→∞)
                      lim_(s→∞) lim_(J→∞) lim_(b→∞).   (23)

The s limit is omitted for exactly represented finite data. At each inner limit
fixed-graph observations obey the same finite product/action subtractions as
(20), on the mark couplings of (22); their L² errors and joint W₂ errors vanish.
This covers all declared fixed action observations, not just prediction.
The outer limit is §5 on the same horizon and data family.

At finite arithmetic precision, an observation law means the normalized
pushforward of its returned nonnegative population weights (and normalized
data weights when an input mark is included). The operational prediction,
risk and RMS formulas retain their literal working weights. At fixed array
sizes their total masses tend to one as b tends to infinity. Dividing by
these masses therefore changes the joint laws by a vanishing amount, and
raw squared RMS differs from its normalized counterpart by the product of
the relevant masses. Precision is removed first, so the subsequent ODE and
W2 limits use probability laws exactly. No normalization is silently inserted
into the numerical dynamics or used to infer a finite-resolution certificate.

Saved numerical state consists of b₁,g,w,p₁,b₂,c,p₂,M,D, the finite data law,
and arithmetic metadata. The source compiler is discarded after initialization.
Checkpoints preserve hexadecimal floats, exact decimals or rational integer
units. Loading calls no initializer; continuation with the same arithmetic,
steps and reduction order reproduces the working state. Own-state storage is
P₁(k₁+2d+1)+P₂(k₂+2)+2k₁k₂ scalars, plus O(md+m) data and metadata.
Heun has a fixed number of stage arrays. Requested observation panels may add
workspace, but elapsed training steps do not change current-state dimension.
The following bounds make initialization and evolution costs explicit; none
contains neural width.

### 6.1. Scalar arithmetic work and workspace

Count each scalar addition, multiplication, division, comparison and elementary
function call as one operation in this subsection; their different bit costs
are charged in §6.2. Dense matrix products use their classical cubic/bilinear
operation bounds. These are upper bounds for the displayed implementation,
not claims about optimized hardware timings.

Let V be the number of nodes in the complete structurally merged compiler DAG,
S=S₁+S₂ its number of named action sources, and k=k₁+k₂ its retained feature
count. There are at most E=2V+S² coordinate/response edges: each ordinary node
has at most two parents, and each source has at most S earlier response links.
Constants, seeds and terminal forward/reverse feature actions are counted in V.
The initialized independent Gaussian dimensions are d+S₁ on the lower
population and S₂ on the upper population. In these terms a conservative
initializer work bound is

    W_init = O(Q S E + Q S² + S³ + (Q+P)E
                 +(Q+P)(k₁²+k₂²+k₁k₂)
                 +k₁³+k₂³+k₁k₂(k₁+k₂)).                (24)

To obtain (24), each of at most S frozen-source reverse-AD walks visits at
most E edges on Q coordinates, giving QSE. Operand covariances and Gaussian
source evaluation cost O(QS²); the new triangular covariance rows cost
O(S³) altogether. Primal evaluation and frozen replay cost O((Q+P)E).
The two Grams and forward contraction cost O(Q(k₁²+k₂²+k₁k₂)); feature
normalization of the replay costs O(P(k₁²+k₂²)). Dense Cholesky and inverse
triangular construction cost O(k₁³+k₂³), and the two contractions producing
L₂^−1 C L₁^−T cost O(k₁k₂(k₁+k₂)). The deliberately larger Pk₁k₂ term
in (24) is harmless. Simultaneously retained compiler, AD and normalization
arrays occupy at most

    S_init = O((Q+P)(V+d+S+k)+S²+k₁²+k₂²+k₁k₂)          (25)

scalar slots, plus the syntax/metadata and Gaussian-node generator integer
storage. This covers both the Q cloud and its frozen P replay cache, source
factors and diagnostics, primal values, one reverse-AD walk's covectors, raw
feature tables, contractions and normalization factors. The implementation
keeps at most one P replay cache. P=Q can reuse Q arrays but is not needed to
obtain this bound.

Gaussian node generation is an additional explicit cost. Put D=d+S+2, which
bounds the total number of paired uniform coordinates used by the two
populations, and let p_D denote the D-th prime. The elementary Box–Muller
transforms require O((Q+P)D) elementary calls and ordinary scalar operations.
The exact radical-inverse digits require O((Q+P)D log(Q+P+1)) integer steps;
trial generation of prime bases is bounded by O(D p_D) integer divisibility
and comparison steps. The integers here have O(log p_D+log(Q+P+1)) bits.
These bounds include the repeated generation for Q and P, changing only a
constant. They use no unproved dimension-independent integration rate.

For dictionary syntax construction, let V₀ be the total number of Word objects
created before structural merging, including polynomial recurrence nodes and
prefix entries. A direct bound is

    V₀ = O(d(N+1)+d[binom(N+2d,2d)+binom(N+d,d)]+N+d).

Constructing exponent tuples and the polynomial products uses the displayed
O(d times feature count) work. The executable exponent iterator is iterative:
start a fixed total degree with (total,0,...,0), reduce its rightmost nonzero
nonterminal coordinate by one, and place one plus its former suffix sum in
the next coordinate, zeroing the rest. This is exactly the next descending
lexicographic weak composition: later coordinates were already minimal under
the preserved prefix, and the new suffix is the maximal one for its total.
It stops when only the final coordinate is nonzero. Thus it exhausts each
degree once, with O(d) work and storage per emitted tuple and no recursive
dimension ceiling. Each new prefix code uses a bounded number of
Cantor-unpairing and exact rational operations. Compiling each object once and
canonicalizing by its operation and child node indices gives O(V₀) dictionary
operations with ordinary amortized hash-table accounting. Integer indices and
exact rational syntax-envelope lengths are additional bit costs; those lengths
are not treated as unit storage. Alternatively a deterministic comparison-map
implementation would introduce a logarithmic V₀ factor. These syntax costs
occur only during initialization.

For evolution allow different finite population counts P₁,P₂ and let

    S_save=P₁(k₁+2d+1)+P₂(k₂+2)+2k₁k₂,
    S_move=P₁d+P₂+k₁k₂.

The exact finite-data RHS in (12), including state/data validation, costs

    W_rhs = O(S_save+md+m[P₁(d+k₁)+P₂k₂+k₁k₂]).          (26)

More explicitly the leading matrix-product scalar multiply/add count is at
most

    m(4P₁d+4P₁k₁+4P₂k₂+6k₁k₂)

up to lower-order elementwise, accumulation and validation operations. The
terms come respectively from w u and its row-gradient product, the two lower
feature contractions, the two upper feature contractions, and Ma, Mᵀd and
the coefficient gradient daᵀ. In addition there are exactly
m(P₁+P₂) scalar tanh evaluations per RHS, charged as elementary calls below.
Input blocking does not change the total arithmetic order. For block size
B≤m, additional working arrays beyond saved state/data can be bounded by

    S_work,rhs = O(S_move+B(P₁+P₂+k₁+k₂+d)).              (27)

This includes velocity accumulators and block hidden/forward/backward fields.
Together with saved state/data, peak scalar storage is
O(S_save+md+S_move+B(P₁+P₂+k₁+k₂+d)). The maintained Heun integrator uses
two RHS evaluations and O(S_move) stage/update work per step. Therefore J
steps cost O(J W_rhs+S_save), including its initial state copy, and require
the same peak scalar order as (27) plus saved state/data. A constant number
of stage states, velocities and validation scans changes constants only.

Prediction on a panel of v sphere directions has forward work
O(S_save+vd+v[P₁(d+k₁)+P₂k₂+k₁k₂]); its current implementation evaluates
that whole panel together, with O(v(P₁+P₂+k₁+k₂+d)) additional slots.
Blocked paired observations use (27) with m replaced by panel size, and their
optional returned pair arrays add 2(P₁+P₂)v slots; streamed RMS avoids those
arrays. Fixed extra observation graphs add their own explicitly finite node
and action-contraction work. No finite panel certifies a sphere supremum.

### 6.2. Bit work at finite precision

For the rational backend at precision b, a retained scalar of magnitude at
most M_* stores integer units and scale with

    β=O(b+log(1+M_*))                                     (28)

bits. Thus retained numerical state/data uses O((S_save+md+m)β) bits, plus
metadata and exact syntax. Initializer/RHS scalar-slot counts similarly use
their own maximum intermediate scalar magnitude. At fixed graph and fixed
outer resolutions, sufficiently accurate computations have a common finite
M_*: Gaussian nodes are bounded by C_D sqrt(log(p_D max(P,Q))), every
coefficient is a finite continuous expression at positive ε,η_N pivots, and
the finite-time Heun bounds control the dynamic states. Large N, small pivots,
or a long horizon can make M_* and all operand-dependent constants large.

Let I(L) be an upper bound for the integer addition, multiplication, division,
gcd and square-root work used on L-bit operands. One may use the conservative
schoolbook bound I(L)=O(L³), without assuming fast arithmetic. Basic fixed-point
operations outside elementary-function routines then cost O(I(Cβ)) bits each;
constant-factor longer integer numerators and denominators are included by C.
Their temporary storage is O(β) bits per concurrently evaluated scalar.

Elementary calls have an additional cost because the rational backend uses
exact temporary Fractions. On a fixed bounded operand set, away from zero for
logarithm and division, each series uses O(b+1) terms and temporary numerator/
denominator sizes

    β_el=O((b+1)² log(b+2))                              (29)

bits, with operand-dependent constants. For log/exp, denominators divide
powers of an O(b)-bit base denominator times products of O(b) small integer
factors, giving O(b²+b log(b+2)) bits; geometric/Taylor tails give O(b) terms.
The rational pi approximation has O(b log(b+2)) denominator bits, and the
trigonometric powers enlarge this to (29). Exact exponential squaring uses a
fixed operand-dependent number of stages. These facts give the conservative
per-call bit bound O((b+1) I(Cβ_el)) and scalar temporary space O(β_el).
They do not treat tanh, trigonometric functions or logarithms as constant-cost
operations. Float64 instead has fixed-size storage and backend-dependent
fixed primitive costs on finite representable inputs; its lack of a precision
refinement limit is unchanged.

In particular, if W is the ordinary scalar work bound for an initializer or
J-step integration and E_fun its elementary-call count, then a bit-work bound is

    O(W I(Cβ)+E_fun(b+1)I(Cβ_el)),                       (30)

plus the exact prime/digit/syntax integer work specified above. A safe generic
initializer count is
E_fun=O((Q+P)(d+S)+Q(S+1)V+PV+S+k₁+k₂): it covers Gaussian transforms,
primal gates, all reverse walks, replay and square-root pivots. Integration
uses E_fun=2Jm(P₁+P₂), with optional observation calls counted separately.
Peak numerical bit storage is its scalar-slot bound times β, plus O(β_el)
scalar elementary scratch and the exact integer/syntax storage. Only a bounded
number of scalar series is active at once in the rational implementation;
vectorized results remain counted in the scalar arrays. The familiar constants
for a fixed operand set suffice because precision is the innermost limit in
(23). Nothing here promises those constants uniformly in the outer limits.

Compiler `max_work_units`/`max_working_bytes` and dictionary limits are adjustable
planning guards. They are not certified process-wide peaks, and their internal
estimates do not replace the complete initializer bounds (24)–(25) or the bit
accounting above. An external runtime/memory cap can enforce a validation
budget. Mathematical refinement presumes enough resources for each finite
request; neither fixed default limits nor a successful small run prove an
accuracy-versus-cost guarantee.

## 7. Deterministic checks and unresolved obligations

The original executable checks were fixed before their run: d∈{1,2,3,7}, N∈{1,3};
source identities and the d=2 adapter against the maintained compiler;
nontrivial odd enrichment counts; supplied-state adjunction, coordinate loss
gradients and full energy directional derivative; joint observation evaluation;
float/rational backend agreement and bitwise own-state restart. The only ODE
updates are one or two tiny steps from a supplied state to check restart.
One process, one numerical thread, at most 120 seconds, no search or training
campaign. Exact results and source hashes are saved in
`data/generated/cx1_many_point_closure_20260919/closure/deterministic_v2/results.json`.
The v2 run supersedes v1 after a data-validation and metadata cleanup; v1 is retained.
These checks verify implementation identities; they do not certify neural
approximation accuracy, source-tail bounds, fitting, or an order error.

The iterative enumerator described in §6.1 has an additional deterministic
regression: exact agreement with the inherited
enumeration at dimensions 1--4/degrees 0--4, and construction of the
d=600/order=1 dictionary without initialization or trajectory evolution.
The seven-test suite is run under the same resource cap in the
fresh `closure/deterministic_v4/` namespace. Its final observed result is
recorded in VALIDATION.md.

The read scope was this study README; required mathematics/research skills;
`docs/NOTATION.md`, `docs/observable_p1.md`; complete relevant H1,H2,dictionary,
numerical H3 and H4 closure arguments in `docs/global_nonlinear.md`;
`code/README.md` relevant maintained API sections; and the maintained
`observable_words`, `observable_initialization`, `observable_compiler`,
`observable_arithmetic`, `observable_fixed`, `observable_solver` modules.
No other study, history, task conversation or sibling output was read.
Only this proof, `cx1_closure.py`, `test_cx1_closure.py` and this unit's generated
check directory were written. No maintained file, Git index or commit changed.

Remaining study obligations are exactly Input C on its proposed positive
geometric family through its proposed learning horizon; the final loss bound;
positive paired motion at a specified time; and a separately justified actual
raw-GD step condition if that conclusion is required. This closure unit neither
assumes those study conclusions in its own convergence proof nor supplies them.
Once Input C is proved independently for the proposed family and horizon,
this unit applies directly and its approximations inherit the target's limiting
loss and motion observations. A finite chosen resolution still needs separate
accuracy evidence to certify numerical margins.
