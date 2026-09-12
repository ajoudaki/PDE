# C-H1: current bounded-probe populations determine nonlinear training

Candidate theorem, version 1. Author/assembler: `/root`. This is study material,
not established theory. The proof uses the canonical population flow and the
complete finite Gaussian program construction specified in the dependency packet.
No training experiment, finite closure, or numerical efficiency claim is made.

## 1. Model, fixed family, and statement

Fix Y≥1. Put u=x/√2 and equip
Z=√2 S¹×[-Y,Y] with d((x,y),(x',y'))=|u-u'|+|y-y'|.
All Wasserstein distances between training laws below use this metric.
The finite model is exactly

    f_n(x)=n⁻¹ (W^(3))ᵀ tanh(W^(2) tanh(W^(1)u)),

with no biases, independent stored Gaussian variances (1,1/n,1/n²), block
mobilities (n,1,n), residual f-y, and unhalved mean-square-loss physical GF.
Its canonical population aliases are w=W^(1), A=W^(2)=A₀+K, c=W^(3).
Here w∈L²(Ω₁;R²), c∈L²(Ω₂), A:L²(Ω₁)→L²(Ω₂) is bounded, K is
Hilbert–Schmidt, and the reverse action is the actual adjoint. Initially
w=g=(g₁,g₂)∼N(0,I₂), K=0, c=0. The zero limiting readout does not replace
the finite random initialization.

Write E₁,E₂ for the separate population expectations. For u∈S¹ define

    z₁(u)=w·u,             h₁(u)=tanh(z₁(u)),
    z₂(u)=A h₁(u),         h₂(u)=tanh(z₂(u)),
    d₂(u)=c[1-h₂(u)²],     q(u)=A* d₂(u),
    d₁(u)=[1-h₁(u)²]q(u),  f(u)=E₂[c h₂(u)],  r(u,y)=f(u)-y.       (1)

Lowercase aliases in (1) stand for the canonical capitalized population
fields Z^(ℓ),H^(ℓ),Δ^(ℓ); q is the first reverse query. They are scalar
random variables, not finite-width coordinates. Every product is within one
population. A rank a⊗b acts as v↦a E₁[bv]. The physical equations are

    w'=-2∫r d₁(u)u dμ,  A'=-2∫r d₂(u)⊗h₁(u) dμ,
    c'=-2∫r h₂(u) dμ.                                         (2)

Let δ_Y>0 be a fixed radius supplied by global_nonlinear C.4.7.1–5,
including the uniform passive-query tails of C.4.7.3. Fix T₀=1/200.
Section 8 defines a positive δ_act,Y from explicit nonzero Gaussian
expressions and continuity, independent of hierarchy order. Fix once and for all

    δ=min(δ_Y/4, δ_act,Y, 1/4),
    U={μ∈P(Z): W₁(μ,ν*)<δ},
    ν*=½δ_(√2 e₁,+1)+½δ_(√2 e₂,-1).                           (3)

Neither δ nor T₀ depends on the level. Constants here need not have useful
numerical size. The theorem also gives exact identities on the entire established
[0,40]; the stated C-H1 interval is [0,T₀].

**Theorem.** There is an explicit nested hierarchy H_n, n≥1, with finitely
many population types at each level, each a probability law on R^m with m≤n,
and finite-dimensional real/input marks, having the following properties.

(a) Its observation maps, within-population joints, Gaussian initialization,
and exact continuum-law integration interface are given in Sections 2–3.
It retains all current fields (1), whole-circle prediction, and joint initial/
current hidden observations. Every separately fixed finite tuple has the actual
finite-network interpretation in probability in W₂. No all-moment determinacy
assumption is used.

(b) For every fixed level, each characteristic-function coordinate is C¹ in
physical time, including one-sided endpoint derivatives. Its exact weak evolution
is (8), evaluated by the finite compiler in Section 4. The right side uses only
H_N with N=10⁶(n+1)⁶, current scalar contractions, one training-law integral,
and a specified limit in one real cutoff mark R→∞. This is a finite higher-level
dependency; the cutoff does not add coordinates or increase level. Finite levels
are not asserted to be closed or to have an effective cutoff error bound.

(c) Let S be any state reached at time s≤T₀ on a canonical trajectory for
μ∈U. Let S̃ be any realization on two probability spaces with square-integrable
row and frozen seed fields, bounded readout, and a bounded middle action with
its actual adjoint. If H_n(S̃)=H_n(S) for every n, there exists a unique strong
continuation from S̃ under the same law μ on [0,T₀-s], in the affine raw space
with Hilbert–Schmidt middle increments. Throughout this interval its complete
hierarchy equals that of S's continuation. Consequently predictions agree at
every input on the circle, and every declared same-population joint hidden,
initial/current, and action observation agrees. Competing strong continuations
need no independently imposed tail assumption. The proof reconstructs the
observable probability algebras and their dynamically relevant action, proves
invariance, and transports (2); it does not infer sufficiency solely from
uniqueness of a prescribed initialized path.

In particular the assertion compares two reached states, including states
obtained from different training laws or different reached times, whenever their
complete hierarchies agree; the continuation law in the theorem is μ. Existence
under that law for the matching realization is part of the conclusion. No
existence assertion is made for switching an arbitrary unmatched reached state
to an arbitrary law. There is no uniqueness claim for arbitrary formal moment
or characteristic-function sequences.

## 2. A finite alphabet and finite-dimensional populations

Keep frozen seed fields g₁,g₂ on population 1 and

    z₂⁰(v)=A₀ tanh(g·v), v∈S¹,

on population 2. These are initial observations, retained jointly with current
observations; their time derivative is zero. They are not previous training states.
In particular h₁⁰(u)=tanh(g·u) and h₂⁰(u)=tanh(z₂⁰(u)) are reconstructible.

Use two sorts, B (bounded) and L (square integrable), on each population;
B is also an L expression. The following finite instruction alphabet defines
acyclic scalar observation programs. Each instruction creates one node.

1. Seeds: w₁,w₂,g₁,g₂ on population 1; c and z₂⁰(v) on population 2;
   the constant 1 on either population. The seed c has sort B, all other
   nonconstant seeds have sort L. Its bound on canonical paths is 80Y on [0,40].
2. Affine node aV+bW+d on one population, a,b,d∈R. It has sort B if its
   parents are B, otherwise sort L. Unary affine nodes use a zero coefficient.
3. sin(V), cos(V), tanh(V), for V of sort L, giving sort B.
4. VW when both parents have sort B, giving sort B.
5. A V from population 1 to 2, or A*V from population 2 to 1, with V of
   sort B, giving sort L.

No product of unrestricted L nodes is a coordinate instruction. Every B node
has a deterministic finite bound computed from its syntax, marks, and the
readout bound. In particular products have bounded partial derivatives on the
actual parent range; their ordinary global product extension is never invoked
as an L² algebra bound. The smooth saturation

    T_R(V)=R tanh(V/R), R≥1,                                  (4)

is a three-node B expression. It satisfies |T_R(V)|≤|V|, is 1-Lipschitz,
and converges to V in L² for each V∈L². Its parameter R is an observation mark.

A level-n population type consists of: a correctly typed acyclic program with
at most n nodes; an ordered list of m≤n nodes of one population, repetitions
allowed; and its graph shape, with all real coefficients and all seed directions
left as marks. The corresponding population is the *joint law*

    Law_ℓ(V₁(α),...,V_m(α)) ∈P₂(R^m).                         (5)

All combinations of marked programs with total union size at most n are included.
Thus two inputs, or two different choices of the same probe's marks, are placed
in one same-neuron tuple by taking their finite union. They are never sampled
independently within that tuple. Every finite joint collection appears at some
level. Independent neuron replicas, if desired, are products of these laws:
no cross-layer pairing of neuron indices is asserted or needed. Products of
expectations in (8) use independent population sampling, not a missing mixed
same-neuron correlation.

For fixed n the graph/type list is finite: every node chooses from the finite
alphabet and from at most n earlier node positions. A crude upper bound on the
number of graph and output-list choices is (20(n+1)²)^(3(n+1)). Mark space is a
finite union of products R^p×(S¹)^q with p≤3n and q≤n. Each population dimension
is m≤n. To read its characteristic function add a frequency λ∈R^m and record
both E cos(λ·V) and E sin(λ·V). These are bounded determining tests, not a
power-moment sequence. Restrictions from level n+1 to n are literal marginals
and repeated program evaluations. H_n is the whole such finite-type family.

The word 'finite' here counts types, replicas, and dimensions, not scalar
storage after quadrature: each law and each finite-dimensional mark domain is
an unevaluated field. C-H1 permits population fields and does not prove their
manageable discretization. No mark is an arbitrary function, an L² vector, a
matrix, or a code for a parameter distribution. To request more arguments or
more joint replicas requires a higher level. In particular an action coordinate
means the law index of a specified finite B program, not an interface accepting
an arbitrary vector and returning A times that vector. Infinite-order recovery
of the relevant action is proved only in Section 5.

Observation recovery is explicit. Binary affine nodes give w·u and g·u;
(1) except d₁ uses only this alphabet since c is bounded and φ'=1-tanh².
The joint law of d₁ with any finite declared tuple is the pushforward of the
joint law including q,z₁ by (q,z₁)↦q(1-tanh²z₁); this is an L² field because
the gate is bounded. Prediction is the integral E₂[c h₂(u)] of its joint law.
Likewise all quadratic pairings of L² fields are integrals of their joint law,
finite by Cauchy–Schwarz. Initial/current displacements use the joint tuple
(h_ℓ,h_ℓ⁰), not a coupling chosen from its separate marginal distributions.

These declarations include arbitrary finitely nested action observations in
this alphabet and their bounded-gate pushforwards and quadratic contractions.
They do not include arbitrary unbounded products followed by another action.
All circle inputs are available as marks; full-row L² bounds make h₁,h₂ and f
continuous uniformly in input on each compact trajectory interval. Thus dense
input marks also determine their entire continuous versions.

## 3. Exact finite Gaussian initialization and the law interface

At initialization replace w by g, c by zero, and every A,A* in the program
by the two orientations of the *same* initialized Gaussian action. First
construct every requested seed z₂⁰(v) by its two instructions tanh(g·v), A₀
applied to it. Take a finite union before computing any joint law. There are
at most 3n extra instructions and no dependence on training duration or width.

Here is the complete scalar initialization rule for that finite program.
On population 1 retain g∼N(0,I₂). Maintain two independent centered Gaussian
source groups ξ (population 2 forward sources) and ζ (population 1 reverse
sources), independent of g. At a forward call with already constructed input b,
set

    A₀ b = ξ_b + Σ_(earlier reverse calls j) d_j E₁[∂_(ζ_j)b].

At a reverse call with input d, set

    A₀* d = ζ_d + Σ_(earlier forward calls i) b_i E₂[∂_(ξ_i)d].   (6)

The source covariance extensions are E[ξ_b ξ_b']=E₁[bb'] and
E[ζ_d ζ_d']=E₂[dd']. Every named derivative in (6) differentiates the full
finite coordinate expression with all already selected deterministic
coefficients and covariances frozen; unavailable sources have derivative zero.
This is a source derivative used only for initialization, not a temporal derivative.
Previous reverse inputs d_j and forward inputs b_i are coordinate expressions
on the output population of the relevant formula. The full uncentered input
Grams supply the centered source covariances.

For an old covariance C, new covariance vector b and variance v, realize the
next source by bᵀC†ξ+sqrt(v-bᵀC†b)G. The input Gram is positive semidefinite;
testing its quadratic form on (tz,1) for z∈ker C proves b⊥ker C, and completing
the square proves the nonnegative radicand. Thus this is a finite construction
also at duplicated or zero-variance queries. All expectations in (6), in the
Grams, and finally in (5) are finite-dimensional Gaussian expectations using
these covariance matrices. No inverse-continuity or empirical minimum-eigenvalue
assumption is made.

The initialization program's B operands have finite deterministic bounds.
Replace each bounded product, for applying the finite-program theorem, by a
smooth globally Lipschitz product equal to it on its parent ranges. Induction
shows that every fixed expression has a linear growth envelope in its finite
Gaussian source list and bounded first named-source derivatives: action outputs
are sources plus finite linear combinations of bounded inputs, and every
coordinate derivative has bounded factors and previously fixed finite coefficients.
Consequently all expectations in (6) exist. Special-data III.F.1–7 proves the
joint W₂ limit from the actual Gaussian matrices, source rule, singular-query
passage, and common bounded action/adjoint realization. All its hypotheses
have just been checked; its probability and conditioning proofs are included
in the dependency packet. In particular the reverse answer in (6) has its
own surviving Gaussian source as well as the response correction. Replacing it
by only an adjoint of an isonormal embedding would give the wrong model.

The finite stored readout has RMS and supremum tending to zero in probability.
For the supremum, the union bound is P(max_i|W_i^(3)|>ε)≤2n exp(-n²ε²/2).
At every fixed observation program, a same-array finite induction on the
operator-norm event, bounded parent ranges, and Lipschitz gates transfers this
vanishing discrepancy to every node. Thus the population c=0 initialization
is the actual limit of the prescribed finite random readout.

For a Borel training law μ the integration interface is exact evaluation of
∫_Z G(u,y)dμ for the continuous scalar integrands specified in (2),(8), and
finite products of such integrals if an observation requires them. Alternatively
one may supply a sequence of finite atomic laws with certified W₁ distance
→0 and evaluate finite sums, followed by that limit. Compactness gives such a
sequence by partitioning Z into cells of vanishing diameter and assigning each
cell mass to a representative. No label-function or atom-count assumption is
needed. This is an integration interface, not a claimed quadrature algorithm
with computable rates. Scalar continuity and boundedness justify all these
limits. Initialization itself is independent of μ.

Along learned paths, C.4.7.5 supplies the finite-network interpretation for
our fixed observation programs: continuous globally Lipschitz maps, finite
bounded actions, and bounded gates are within its scope, and our products
have globally Lipschitz extensions on their bounded parent ranges. Frozen and
current observations occur in the same tuple. Fix the level, marks and finite
tuple first, then take width→∞. Law approximation and proof meshes are removed
in the order in that theorem; there is no growing-program invocation and no
claim uniform over all marks at once. Physical-time derivatives below are proved
directly on the strong population path, not by exchanging finite-width derivatives.

## 4. Exact weak evolution by a finite reverse compiler

Fix a level-n tuple and either test Ψ(V)=cos(λ·V) or sin(λ·V), and put
J(t)=E_ℓ Ψ(V(t)). All marks remain fixed. Each L node is C¹ in L² along a
strong raw solution with bounded readout on a compact interval. For sin, cos,
tanh this follows from the scalar mean-value identity and the following
bounded-multiplier fact: if z_j→z in probability, v_j→v in L², and b is bounded
continuous, then b(z_j)v_j→b(z)v in L². Subtract the varying v; truncate the
remaining fixed v at |v|≤M and then send M→∞. Products of two B nodes follow
by subtraction using their uniform bounds and that same fact. Action nodes use
(Ab)'=A'b+Ab' in L², obtained by expanding the difference quotient; the cross
increment is bounded by the product of operator and L² increments. This proves
the induction and J∈C¹. It does not assert ambient L² Fréchet differentiability
or take a second temporal derivative.

Use reverse differentiation of this finite graph for the scalar J. Seed each
output covector by ∂_iΨ(V), sum multiple contributions at shared nodes, and
process nodes in reverse topological order. Covectors p_v lie in L² of their
node's population. The exact rules are:

- aV+bW+d sends a p to V and b p to W;
- sin(V), cos(V), tanh(V) send respectively p cos(V), -p sin(V),
  p[1-tanh²(V)] to V;
- bounded product VW sends pW to V and pV to W;
- A b sends A* p to b and records the action occurrence (p,b,+);
- A* b sends A p to b and records the action occurrence (p,b,-).

Freeze derivatives of g,z₂⁰ and the constant seeds at zero. Let p_w₁,p_w₂,p_c
be the total covectors at moving seeds. Integration of the ordinary curve
chain rules and actual adjunction gives

    J'=Σ_i E₁[p_wi w_i']+E₂[p_c c']
          +Σ_+ E₂[p A'b]+Σ_- E₁[p A'*b].                   (7)

To verify reverse differentiation, maintain the pairing of each unprocessed
node's covector with its velocity. The coordinate rules replace that pairing
by its parent pairings; an action rule uses adjunction for its Ab' term and
records its A'b term. The scalar pairing sum is unchanged at each step. There
are finitely many steps, all products have one bounded multiplier or two L²
factors, and Cauchy–Schwarz justifies every expectation. At the leaves this
invariant is (7).

Substituting (2) and using the rank formula yields the exact identity

    J'=-2 ∫ r(u,y) {
       E₁[(u₁p_w₁+u₂p_w₂)(1-h₁(u)²)q(u)]
       +E₂[p_c h₂(u)]
       +Σ_+ E₂[p d₂(u)] E₁[b h₁(u)]
       +Σ_- E₁[p h₁(u)] E₂[b d₂(u)] } dμ.                  (8)

This formula includes both orientations and every occurrence of the current
moving action. Residuals, readout, gates and contractions are recomputed from
the current hierarchy. They are not frozen coefficients in time. Source
coefficients from (6) are never used to evolve a learned state.

The covectors in (7) are a *proof device*, not extra unbounded response fields
silently added to the state. To evaluate (8) from H_N, perform the following
finite current-probe compilation at a fixed R≥1. Replace each action on a
covector p by an action on T_R(p). Replace each multiplication b p, where b is
a bounded derivative/gate factor, by b T_R(p). Leave finite sums and scalar
multiplications unchanged. Seed covectors are already bounded. Every resulting
covector p^R is an allowed L observation program: inputs to actions are B,
and products have two B operands. Derivatives of sin, cos and tanh use the
same alphabet, as do derivatives of affine or B-product nodes. Evaluate the
right side of (8) using p^R and then let R→∞.

Here are the convergence and complexity details. For any v_R→v in L²,

    ||T_R(v_R)-v||₂ ≤ ||v_R-v||₂+||T_R(v)-v||₂ →0.

Reverse induction therefore gives p^R→p in L² at every node. The same induction,
using ||T_R(v)||₂≤||v||₂, gives sup_R||p^R||₂<∞, with a bound depending on the
fixed graph, marks, action norm and bounded-node envelopes. No higher moment
of an arbitrary action output is required. In (8) the error of each pairing
is at most the L² covector error times a fixed L² norm. The fields h₁,h₂,d₂,q
have uniformly bounded L² norms in u on the path, and r is bounded. Thus the
integrand errors tend uniformly to zero in u,y for this fixed graph, permitting
the law integral and R limit. The same proof is locally uniform in t: all
exact covectors form compact L² curves, saturation converges uniformly on a
compact L² set by a finite net and its 1-Lipschitz property, and reverse
induction preserves this uniform convergence. Equation (8) has the stated
continuous derivative, or equivalently its integrated weak identity.

For a literal bound, build λ·V with at most n affine nodes and its terminal
sine/cosine with one node. The resulting forward graph has at most 2n+1 nodes
and at most 4n+2 edges. Each processed edge needs at most 20 nodes for its
bounded local derivative, saturation, propagated contribution and addition
into an accumulated covector. Shared forward nodes are retained. This uses
fewer than 200(n+1)² nodes. Formula (1) at one new training input needs fewer
than 40 nodes. Each scalar pairing in (8) uses at most three further nodes
as an integrand outside the law or is an integral of the corresponding joint
law; collect all forward and covector nodes and the fields at that one input
in a finite union. Even duplicating whole graphs for each of at most 4n+2
terms stays below 10⁶(n+1)⁶ nodes and tuple dimension. This bound is deliberately
loose and independent of R, μ, elapsed time, and quadrature support size.
The one law integral is outside the hierarchy population: its input u is a
mark, not a growing list of simultaneous training coordinates.

Thus (8), with the explicit finite compiler and R limit, reads only H_N.
It does not apply a retained operator to an arbitrary new vector. Evaluating
an individual law integral of p^R q times a bounded gate uses its at-most-
quadratic joint statistic, not an unbounded multiplication instruction followed
by an action. Computing the limit effectively or uniformly in level is a
separate C-H2/C-H3 problem.

## 5. What the complete hierarchy determines

Let S be any realization of the alphabet with w,g,z₂⁰ square integrable,
c bounded, and A bounded with its actual adjoint. Let G_ℓ be the sigma-field
generated by *all finite current word values* on population ℓ, and put
H_ℓ^obs=L²(G_ℓ). This is a proof reconstruction from the complete hierarchy,
not a stored finite-level space or an additional finite-state coordinate.

Bounded word values span a dense subspace of H_ℓ^obs. To see this explicitly,
finite-coordinate cylinders approximate any measurable L² variable: the class
of measurable sets whose indicators admit such approximation contains the
cylinder algebra and is closed under monotone limits, by continuity of probability;
then use simple functions and truncation. On each finite coordinate tuple,
linear combinations of sine/cosine affine tests are dense in L² of its law.
Here is a proof avoiding a moment assumption. A function orthogonal to these
tests defines a finite signed measure η with zero Fourier transform. Convolve
η with a centered Gaussian of variance ε>0. The Gaussian Fourier integral,
obtained by completing the square one coordinate at a time, and Fubini show
that its continuous density is zero. Integration against bounded Lipschitz
functions and ε↓0 then gives ∫b dη=0 for every bounded Lipschitz b. Approximate
indicators of compact subsets of open sets with distance functions and then
Borel sets by countable rational boxes to obtain η=0. Orthogonality therefore
forces the original function to vanish. The affine sine/cosine tests of every
finite tuple are finite words at some level, proving density.

If S and S̃ have equal complete hierarchies, the map sending each bounded
Borel function of any finite named word tuple to that same function of its
counterpart is well defined and isometric in L². Equality of their *joint laws*
proves this assertion even when two different expressions agree almost surely.
The maps extend to surjective real unital isometries

    U_ℓ:H_ℓ^obs → H̃_ℓ^obs.                                  (9)

They preserve expectation, bounded Borel coordinate operations, multiplication
by bounded measurable functions, and positive cones. For instance approximate
in L² by bounded cylinders, extract almost-surely convergent subsequences, and
use bounded convergence for bounded continuous compositions; indicators and
bounded Borel functions follow by the same finite-measure approximation used
above. For a bounded multiplier b and arbitrary v∈L², approximate v by bounded
cylinders and use ||bv||₂≤||b||∞||v||₂. Unbounded seeds are mapped by applying
this argument to T_R(seed), then R→∞.

For a bounded word b, its action output is another word. Hence

    U₂ A b = Ã U₁ b,    U₁ A* d = Ã* U₂ d                   (10)

for bounded words of the appropriate populations. Density and boundedness
extend these identities to every member of the corresponding observable
Hilbert spaces. Moreover A H₁^obs⊂H₂^obs and A*H₂^obs⊂H₁^obs. If P_ℓ is the
orthogonal projection onto H_ℓ^obs, adjunction proves

    A P₁=P₂ A,                                               (11)

since <Av,z>=<v,A*z>=0 for v⊥H₁^obs,z∈H₂^obs, and the first invariance
handles v∈H₁^obs. Thus the two observable spaces are a reducing pair for A;
its complementary block cannot feed them. The same holds for Ã. Equations
(9)–(11), not a uniqueness assumption about a moment sequence, are the state
information extracted from equality of H_∞.

## 6. Invariance, reached restart, and uniqueness

We give the argument on any remaining interval of a reached canonical path
under its law μ. On [0,40] that path has bounded raw/action norms, bounded c,
and, by C.4.7.3–4, uniform constants a,M>0 with

    τ_R(c(t))+∫τ_R(q(t,u))dμ ≤ M exp(-aR), R≥1,               (12)

where τ_R(v)=||v 1_|v|>R||₂. The established theorem in fact gives stronger
passive Gaussian tails; (12) is enough. We use its complete one-reference
comparison, valid on any two common bounded raw balls,

    ||F_μ(θ)-F_μ(θ̄)||_sum
      ≤C(1+R)||θ-θ̄||_sum+C[τ_R(c̄)+∫τ_R(q̄(u))dμ].          (13)

Only θ̄ needs tails. The sum norm is row L² + HS increment + readout L².
For completeness, forward differences are L²-Lipschitz on bounded balls.
For a backward product split the difference into a changed vector and a
changed gate times the reference vector; the latter is bounded by
2R||z-z̄||₂+2τ_R(reference vector). Apply first to d₂, then its adjoint
q, then d₁. The cutoff errors add rather than multiply, so the dependence is
linear in R. Middle differences use the rank norm identity and the same
subtractions. Integrate with bounded residuals to get (13). Its proof is
carrier-independent and requires no Gaussian hypothesis on the first endpoint.

Fix s and generate H_ℓ^obs from S=θ_μ(s). Ordinary Euler steps for (2), starting
at S, stay within these fixed spaces in row and readout and change A only by
ranks between them. Indeed coordinate operations preserve the generated
sigma-fields, A and A* preserve the spaces by (11), and a law integral stays
in a closed space by approximation with finite sums. The updated action has
the same invariant subspaces. This proves the assertion by induction for every
separately fixed Euler mesh, including continuum μ with exact integration.

These restarted Euler paths converge to the reference restriction. This step
must be proved: invariance of an Euler sequence alone would not imply flow
invariance without its convergence. Bounded activations give common crude
Euler bounds on the fixed remaining interval: if C_k=||c_k||∞, then
C_(k+1)+Y≤(1+2h_k)(C_k+Y); summing rank and row increments then bounds A,w
and all raw speeds independently of the mesh. Compare its interpolant to
θ_μ(s+t) in (13) with the latter as the tail-bearing reference. Its node/current
discrepancy is at most Vh. For e equal to their sum distance, set v=e+Vh
(and add ε>0 when needed). Choose R=1+a⁻¹log(1/v) for 0<v≤1. Increasing constants,

    v'≤L v log(e/v),
    v(t)≤exp(1-α(t)) v(0)^α(t),  α(t)=exp(-Lt).               (14)

The distance is absolutely continuous and satisfies this inequality almost
everywhere where positive. To integrate, let z=log(e/v), so z'≥-Lz.
A positive ε regularization and its zero limit handle initial zero. For small
h, the displayed bound stays below 1 on the fixed interval, justifying the
cutoff by first exit. Thus e→0 uniformly. This proves the required Euler
convergence without a tail assumption on restarted Euler states.

Closedness of the observable spaces and of the subspace of HS operators
supported between them proves that the actual future w,c stay in H^obs and
A(t)-A(s) has only that block. Frozen g,z₂⁰ are unchanged. This proves flow
invariance from retained current information and actual evolution.

Now take any matching realization S̃ as in Theorem (c), and its isometries
(9). Write B(t)=A(s+t)-A(s) restricted between the observable spaces. Transport
w(s+t), c(s+t), and B(t) by U₁,U₂; extend U₂ B(t)U₁⁻¹ by zero on the orthogonal
complement, and add it to S̃'s original full action Ã(s). Because HS norm is
preserved under unitary maps on these subspaces, these transported increments
are strongly C¹ in the raw metric. Isometries preserve bounded coordinate
operations, pairings, and Bochner integrals. Equations (10)–(11) and invariance
therefore give exactly (1)–(2) for this transported path. This constructs a
strong continuation from S̃; its complementary action stays constant. It also
proves equality of every future word and joint law under U, by finite induction
on the observation graph. Bounds on c and (12) transfer as distributional
properties of their joint observations.

Finally let another strong continuation from S̃ be given in the same affine
raw space. Its continuous raw path has bounded norms on each compact interval.
Apply (13) with the transported continuation as reference and zero initial
difference. Formula (14), obtained by adding ε and then sending it to zero,
forces their distance to vanish. This proves uniqueness with no tail condition
on the competitor. The complement cannot create an alternative solution.
Prediction equality is pointwise for all u; continuity makes it equality of
the continuous whole-circle maps, hence zero uniform norm difference. Equality
of population observations means equality of all finite-dimensional same-layer
joint laws, with their second moments and the declared pushforward/contraction
observations, not a cross-layer neuron pairing or equality of finite matrices.

This is the precise restart domain: any canonical reached state for μ∈U at
s≤T₀, and every bounded-action, bounded-readout L² realization having its
complete current hierarchy. The remaining horizon is T₀-s (or 40-s if using
the larger established interval). Time s is a validity bound in the theorem,
not a saved coordinate queried by the hierarchy equations. The equations are
autonomous in their current hierarchy and the continuation law. No existence
or uniqueness on arbitrary unrealizable formal hierarchy sequences is claimed.

## 7. Determinacy, limiting interpretation, and information audit

Characteristic tests determine each finite law by the Gaussian convolution
argument in Section 5. Thus the hierarchy records laws themselves; equality
of all power moments is neither assumed nor substituted. Second moments are
used for integrability and W₂ interpretation, not to determine distributions.
Every initial/current pairing and every pair of input marks enters a common
finite tuple at some explicitly finite level. Separate marginals would not
support (9), (10), or even E[c h₂(u)].

All limits have distinct roles. Fixed finite Gaussian constructions initialize
a level before width tends to infinity. The canonical strong flow is then the
established population limit. At a learned current state the R limit in (8)
only evaluates a derivative using a family of current marked probes at one
higher fixed level. It is not a new time coordinate, a Taylor summation, a
source-to-time derivative identification, or a trajectory reconstruction from
future samples. The only infinite completion used in predictive sufficiency
is over current observation levels and their L² generated spaces.

Finite states contain neither A nor K as an operator-valued coordinate. No
entrywise parameter law, full row of the middle matrix, arbitrary query vector,
or stored elapsed transcript is admitted. First row w is a two-dimensional
neuronal observable (recoverable from two passive first preactivations), and c
is a scalar neuronal observable; the remaining seeds are specified initial
observations. Real marks have fixed finite dimension at a level. The complete
hierarchy may determine an infinite dynamically relevant action, as allowed by
C-H1; no assertion of finite scalar compression follows from this fact.

## 8. A fixed genuinely nonlinear learned family

We supply a qualitative self-contained choice of δ_act,Y, so that no numerical
training or numeric Gaussian certificate is needed for C-H1. Work first at ν*.
Let h_a=tanh(g_a), q₀=E tanh²G>0, and ξ_a=A₀h_a. The initial forward rule gives
independent ξ₁,ξ₂∼N(0,q₀). Put y₁=1,y₂=-1 and define

    S=y₁tanh ξ₁+y₂tanh ξ₂,
    U_a=S φ'(ξ_a), P_a=A₀*U_a, V_a=φ'(g_a)²P_a,
    R_a=q₀U_a+A₀V_a, E_a=φ'(ξ_a)R_a,  φ=tanh.                (15)

All products have bounded multipliers and all fields are L². From (2), the
strong multiplier rule, and integration of a field converging in L²,

    c(t)=t S+o_L²(t),        d₂(t,e_a)=t U_a+o_L²(t),
    w_a(t)-g_a=(y_a/2)t² φ'(g_a)P_a+o_L²(t²),
    K(t)=(t²/2)Σ_b y_b U_b⊗h_b+o_HS(t²),
    h₁(t,e_a)-h_a=(y_a/2)t² V_a+o_L²(t²),
    h₂(t,e_a)-tanh ξ_a=(y_a/2)t² E_a+o_L²(t²).               (16)

Here r(0,e_a,y_a)=-y_a and the atom weights are 1/2, fixing every factor.
For example divide the readout equation by t to get S, propagate the upper
gate and adjoint limits, and integrate the first velocity t y_aφ'(g_a)P_a.
For an activation use its mean-value identity on the L² convergent normalized
increment. In z₂ expand K h_a+A₀(h₁-h_a)+K(h₁-h_a); the last term is O_L²(t⁴)
and E[h_bh_a]=q₀1_a=b, giving (16). No temporal analyticity is used.

Actual adjunction gives

    E₁[h_a P_a]=E₂[ξ_a U_a]
      = y_a E[ξ_a tanh ξ_a φ'(ξ_a)] ≠0.                     (17)

The other coordinate contributes zero by independence and oddness; the final
integrand is strictly positive except at zero and bounded by |ξ_a|. Thus each
P_a, and each V_a since φ'>0, is nonzero. Also

    Σ_a E₂[U_a R_a]
      =q₀Σ_a||U_a||₂²+Σ_a E₁[φ'(g_a)²P_a²]>0.              (18)

Hence the R_a, and therefore the E_a, cannot all vanish. Define
b₁²=(1/8)Σ_a||V_a||₂²>0 and b₂²=(1/8)Σ_a||E_a||₂²>0.
The paired training-averaged squared displacements satisfy

    J_ℓ(ν*,t):=½Σ_a||h_ℓ(t,e_a)-h_ℓ(0,e_a)||₂²
                =b_ℓ²t⁴+o(t⁴), ℓ=1,2.                    (19)

To check nonlinearity on visited distributions as well, set for a real L²
preactivation Z with positive variance

    N(Z)=inf_(a,b∈R) E|tanh Z-aZ-b|².

This equals Var(tanh Z)-Cov(Z,tanh Z)²/Var(Z). The formula follows by first
minimizing over b and then completing the square in a. It is continuous under
L² convergence while the denominator stays positive. At either initial
nondegenerate Gaussian Z, N(Z)>0: otherwise continuity and Gaussian full support
would make tanh(z) affine for every real z, which is false (it is bounded and
nonconstant). Consequently there is t_a∈(0,T₀) such that (19) gives
J_ℓ(ν*,t_a)>0 and N(z_ℓ(ν*,t_a,e₁))>0 for both layers. This is an existential
constant fixed from the specified reference and its proved continuity, not a
coefficient supplied to the hierarchy equations.

For μ near ν*, the law-continuity theorem gives uniform-in-time raw continuity.
The forward bounds give uniform-in-u L² convergence of hidden and preactivation
fields. Their initialized fields are held on the same carrier. Since hidden
values are bounded by one, a paired squared-displacement change is at most
4 times the hidden L² change. For the remaining change of the law integral,
the fixed reference paired integrand is continuous on compact Z and bounded,
so its integrals are W₁-continuous. Thus J_ℓ(μ,t_a)→J_ℓ(ν*,t_a).
The same L² continuity and the explicit formula above give continuity of N at
the two reference preactivation laws. Choose δ_act,Y>0 so that all four
positive quantities exceed half their reference values whenever W₁(μ,ν*) is
less than δ_act,Y within the C.4.7 ball. This proves the positivity required
in (3) for every μ∈U. Both hidden layers learn and remain nonaffine at the
same positive time, in the actual canonical population dynamics.

The ball includes nonorthogonal laws: rotate the second reference input by a
small nonzero angle toward the first, keeping its label and mass. Its W₁ cost
is half the displacement in normalized input. It includes nonatomic laws:
replace each reference input atom by normalized uniform measure on a small
circle arc around it, retaining the respective label ±1. Transport each arc
to its center; the cost is bounded by its radius and tends to zero. These laws
have no joint atoms, include nonorthogonal input pairs, and satisfy the same
fixed bounds. Labels ±1 are admitted for every Y≥1; the full ball also includes
other bounded labels and noise. No orthogonality restriction is imposed on U.

## 9. What remains for C-H2

C-H1 supplies a sufficient observable state, explicit Gaussian initialization,
exact weak identities, a finite upward dependency rule, and reached restart
without history. It supplies no autonomous finite closure, no quantitative
control of the R cutoff or missing higher levels, no order-uniform stability,
no population/input quadrature cost, and no certified solver. In particular
(8)'s explicit limit is an exact information interface, not a finite numerical
algorithm. C-H2 must produce finite autonomous equations and prove that their
omitted information has vanishing effect on one fixed positive nonlinear
interval and fixed law family. The present construction leaves that theoretical
risk open. The Stieltjes proposition and unrestricted same-norm product/jet
bounds excluded by Gaussian calculus §§6,10 play no role.
