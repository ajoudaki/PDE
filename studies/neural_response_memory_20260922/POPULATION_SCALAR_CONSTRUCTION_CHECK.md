# Scalar graph closure of the finite-width fixed-P response-memory system

2026-09-25. Scoped constructive theory check; no experiment or independent
promotion review. Scientific inputs read in full: `MOMENT_CONSTRUCTION.md`,
`DEEP_CIRCLE_DERIVATION.md`, and `docs/NOTATION.md`. No other research artifact
was read. Required process inputs: the rigorous-math skill and the conjecture
skill with its research-contract and adversarial-audit references.

**Conclusion.** There is an explicit, finite, autonomous system of global
scalar contractions obtained from the finite-width fixed-P Legendre
response-memory system X_{n,P}.
Its state at any fixed diagram cutoff has a list of types independent of
width. It needs no neuron vectors, initialized matrix multiplication, future
trajectory, or fitted conditional expectation at runtime. Its approximation
is precisely deletion of named terms in the exact diagram generator. This
provides a reference construction exposing the defect, not an endorsed
accurate or practical model or a proved convergent hierarchy. A conditional
finite-time error theorem is given below. In particular, neither successful
finite-width response-memory closure at fixed P nor rationality supplies its
missing scalar-tail estimate. Moreover, the entire raw diagram dictionary
has no coordinatewise finite population limit: a retained static diagram
already diverges with n, as shown in section 7. An infinite-population version
would require additional constructions and proofs not established here.

## 1. Target and admissible information

Fix finite width n, samples M, input dimension d, history order P, and a
realized initialization. The target X_{n,P} in this note is exactly the lifted
finite-width three-hidden-layer fixed-P response-memory system of
`DEEP_CIRCLE_DERIVATION.md`, equations (4)--(8). It has two reconstructed
internal matrices, not a dense tangent
system with frozen physical weights. Write L=1+s for the history length,
rho for residual RMS, and U_a=x_a/sqrt(d). These use the source's notation;
L here does not count layers.

The allowed preprocessing inputs are the data, P, the original equations,
W1(0), c(0), W20, and W30. Initial tanh responses and initial Legendre moments
can be computed from these. Preprocessing may be expensive, but it never
integrates a training trajectory. Runtime state must consist of finitely many
ordinary real scalars, with no per-neuron arrays or functions hidden inside
one coordinate. This is a fixed-n construction first. Width-independent
accuracy and cost require further bounds. An infinite-population system is
not the exact target of the identities below; identification with such a
system remains conditional on a separately justified population construction.

## 2. A computable family of global scalar aggregates

The dynamic scalar coordinate types attached to one neuron are:

| Layer | Types |
|---|---|
| 1 | W1[:,j], h1,a, B2,k,a |
| 2 | h2,a, A2,k,a, B3,k,a |
| 3 | c, h3,a, A3,k,a |

Here j=1,...,d, a=1,...,M, and k=0,...,P-1. The same species is evaluated
at every neuron of its layer. Rho and L are shared scalars, treated separately.
The only fixed edge types are

    C2(j,i) = n W20(j,i),    C3(j,i) = n W30(j,i).

This rescaling makes an initialized action a normalized sum:

    (W20 v)_j = (1/n) sum_i C2(j,i) v_i.

A diagram H is a finite graph with layer-colored vertices, edges of these
two types, and a finite multiset of dynamic species decorating each vertex.
Multiple edges and repeated decorations are allowed. Define

\[
 q_H(X)=n^{-|V(H)|}\sum_{\iota:V(H)\to\{1,\ldots,n\}}
       \prod_{(v,w,\ell)\in E(H)} C_\ell(\iota(v),\iota(w))
       \prod_{(v,\alpha)\in D(H)} X_{\alpha,\iota(v)}.
 \tag{1}
\]

Every assignment of indices is included, including collisions. Thus (1)
has no injectivity assumption, finite-width correction, or independence
approximation. Equivalent relabelings of a diagram define one type. Edges
always use the matrix with its original row and column layer; a transpose
changes which endpoint is summed, never the edge values. Consequently all
forward/reverse expressions inherit the same W20 and W30.

A one-vertex diagram gives an ordinary global moment, for example

\[
 q_{c h_{3,a}}=f_a,
 \qquad q_{B_{2,k,a}h_{1,b}}=B_{2,k,a}^{T}h_{1,b}/n.
\]

A two-vertex diagram with one C2 edge gives

\[
 q_{u,C2,v}=n^{-2}\sum_{j,i}u_jC2(j,i)v_i
          =u^TW20v/n.
\]

Most importantly, disjoint unions obey exactly

\[
 q_{H_1\sqcup H_2}=q_{H_1}q_{H_2}.
 \tag{2}
\]

Only connected diagram values therefore need independent storage. Remove
undecorated isolated vertices, whose factors are exactly one. Diagrams with
no dynamic decorations are static initialization contractions; they may be
stored as constant scalar coefficients, counted as part of total storage.

For definiteness the complexity of a connected diagram is

    size(H) = |V(H)| + |E(H)| + |D(H)|.

For a fixed cutoff K there are finitely many types with size at most K.
Their type count depends on K,P,M,d and the number of layers, but not n.
This statement concerns the length of the scalar list, not its evaluation
cost, numerical conditioning, or the cutoff needed for a requested error.

## 3. Compile the exact infinite hierarchy

Expand the finite-width response-memory RHS by the following finite rules:

1. Substitute the reconstructed matrix and its transpose using equation (5)
   of the source. A learned action is a local A or B factor times a global
   normalized pairing, with coefficient -2(2k+1)/(ML).
2. Expand the backward signals using the same initialized edges and learned
   factors. Expand tanh derivatives as 1-h^2, without replacing tanh by a
   polynomial approximation: the source's exact response lift already does
   this on its invariant manifold.
3. Compute the raw moment velocities and both matrix velocities first, then
   substitute them into the lifted response velocities, in the source's
   explicit evaluation order. This introduces no implicit solve.
4. Differentiate a diagram by the product rule. Replace each differentiated
   decoration by its rooted RHS expression, attach its summed neuron indices
   as new vertices, and turn global pairings into disconnected factors.
5. Canonically relabel each resulting diagram and factor disconnected
   components using (2).

All steps are symbolic algebra on finite expressions. The result for each
connected H is a finite list of the form

\[
 \frac{d}{dt}q_H
 =\sum_{\nu\in\mathcal T(H)}
   a_{H\nu}(\rho,L,r;U)
   \prod_{J\in\mathcal C(H,\nu)}q_J,
 \qquad r_a=q_{c h_{3,a}}-y_a.
 \tag{3}
\]

Each coefficient is explicitly rational in L, polynomial in rho and the
residuals, and computable from P,M and the data. Its denominator has only
powers of L. One may instead treat residuals as disconnected diagrams and
obtain a hierarchy linear in the complete, redundant collection of all
diagrams, with rho and L as shared coefficient variables. The connected
version (3) avoids storing products as independent states.

There is a finite number Delta, computable by scanning the rooted expressions
in steps 1--3, such that every connected component produced from H has size
at most size(H)+Delta. A substitution changes only one decoration and attaches
one of a finite list of rooted graphs; the largest increase in that list is
such a Delta. A finite retained equation therefore has a finite, identifiable
boundary of omitted diagrams. Iterating the operation gives an infinite
hierarchy, rather than closing after the first collection of pairings.

For example, set g_cb=U_c^T U_b and p=q_{B2,k,a h1,b}. Its derivative contains

\[
 \dot p=\rho q_{h1,a h1,b}
 -\frac\rho L\left(kp+\sum_{j<k}(2j+1)q_{B2,j,a h1,b}\right)
 -\frac2M\sum_c r_c g_{cb}
       q_{B2,k,a(1-h1,b^2)\delta1,c}.
 \tag{4}
\]

The final expression is shorthand to be expanded using delta1. Its initialized
part contains W20^T and then W30^T with higher vertex decorations; its learned
parts contain additional pairings. Hence ordinary pair moments alone do not
close. Equation (4) also identifies exactly how initialized forward/transpose
correlations enter the scalar construction.

## 4. A finite closure, specified without an unknown conditional law

Choose K large enough to include every training output diagram. Retain every
connected diagram of size at most K, with its exact initial value from (1).
If a retained equation contains a monomial with any connected component of
size greater than K, delete that whole monomial. Retain every other monomial
and its original coefficient. Call this algebraic operation Pi_K and let

\[
 \dot q_H^{K}=\Pi_K[\text{right side of (3)}](q^K,\rho^K,L^K),
 \qquad H\in\mathcal S_K,
 \tag{5}
\]

where S_K is the retained set. Equivalently all omitted connected diagram
values are replaced by zero, after factoring disconnected components.
Deleting only some factors from a product would be a different closure.
No regression, conditional expectation, or future forcing determines (5).
This zero-tail closure is a reference construction for making the omitted
terms explicit; no accuracy or practicality endorsement is implied.

Keep the activity clock exact as a function of the current approximate
outputs:

\[
 \rho^K=\left[M^{-1}\sum_a(q^K_{c h3,a}-y_a)^2\right]^{1/2},
 \qquad \dot L^K=\rho^K,\quad L^K(0)=1.
 \tag{6}
\]

The Euclidean norm in (6) is locally Lipschitz, including at zero. Thus (5)--(6)
is a locally Lipschitz, finite autonomous ODE on L>0. Local existence and
uniqueness follow, for example, by Picard iteration: on a sufficiently small
time interval its integral map is a contraction on a closed state ball.
This is local well-posedness only; deleted terms do not ensure a bounded
trajectory or positive-semidefinite moment matrices.

If an entirely rational evaluated RHS is required, retain rho as an additional
scalar and set

\[
 \dot\rho^K=\frac1{M\rho^K}\sum_a
    (q^K_{c h3,a}-y_a)\dot q^K_{c h3,a},\qquad \dot L^K=\rho^K.
 \tag{7}
\]

With consistent initialization, direct differentiation shows that
(rho^K)^2-M^{-1}sum_a(q^K_{c h3,a}-y_a)^2 stays zero. Equation (7) is
equivalent to (6) while rho^K>0, but its numerical conditioning near zero
requires care. At a consistent zero-residual state all local finite-width
RHS terms, and therefore every term of (3) and (5), vanish. Formula (6)
handles this point directly; formula (7) must not divide by zero.

Rho and L have not been frozen or approximated by a physical-time schedule.
The sole extra approximation relative to the finite-width fixed-P system is
the specified deletion in (5). The P truncation remains a separate, earlier
approximation relative to dense gradient flow.

After preprocessing, the runtime uses q^K, L^K and optionally rho^K, data
constants, static scalar contractions, and a finite symbolic coefficient
table. Its initialized matrices and initial neuron arrays can be discarded.
The numerical state is restartable: the same finite ODE continues from any
of its current states. Its state need not remain realizable by an actual
finite-width neural state; realizability is not claimed by this zero-tail closure.

## 5. Exact remainder and the conditional theorem it actually supports

Let X_{n,P}(t) be the finite-width fixed-P response-memory trajectory.
Evaluate all diagrams on this trajectory. For a retained H define

\[
 R_{H,K}(t)=
 \sum_{\substack{\nu\in\mathcal T(H):\ 
              \exists J\in\mathcal C(H,\nu),\ \operatorname{size}(J)>K}}
 a_{H\nu}(\rho_{n,P},L_{n,P},r_{n,P};U)
 \prod_{J\in\mathcal C(H,\nu)}q_J(X_{n,P}(t)).
 \tag{8}
\]

This is an explicit finite sum of boundary terms, not an unnamed closure
functional. By the definition of Delta, the largest needed component has
size at most K+Delta. It is a theoretical remainder evaluated on the target;
these unavailable evolving terms are not used by the surrogate.

Let z_{n,P,K}=(q_H(X_{n,P}):H in S_K,L_{n,P}), let z_K denote the finite
state (5)--(6), and call its vector field F_K. Its n and P dependence is
suppressed only in F_K and z_K. The exact identity is

\[
 \dot z_{n,P,K}=F_K(z_{n,P,K})+(R_K,0).
 \tag{9}
\]

**Conditional finite-time theorem.** Fix n, P, T and K. Suppose both trajectories
exist in a common convex set on which F_K is Lipschitz with constant Lambda_K
in a specified finite-dimensional norm. Their identical initialized retained
moments and clocks then satisfy

\[
 \|z_K(t)-z_{n,P,K}(t)\|
 \le\int_0^t e^{\Lambda_K(t-s)}\|(R_K(s),0)\|\,ds,
 \qquad 0\le t\le T.
 \tag{10}
\]

Indeed subtraction of the integral equations and the Lipschitz inequality
give e(t)<=int_0^t Lambda_K e(s)+||R_K(s)|| ds. Multiplication of the
corresponding scalar majorant by exp(-Lambda_K t) and integration yields
(10). A bound on a neighborhood of the target also proves the needed
surrogate containment if the right side stays below the distance to the
neighborhood's boundary; otherwise containment is an additional assumption.

For a family of cutoffs, use norms that control the named output coordinates
with constants C_K. A sufficient convergence condition is

\[
 C_K\sup_{t\le T}\int_0^t e^{\Lambda_K(t-s)}\|R_K(s)\|\,ds
 \longrightarrow0.
 \tag{11}
\]

Then the corresponding training outputs converge uniformly on [0,T] to the
finite-width fixed-P response-memory outputs. Condition (11) is a conditional theorem,
not a derived rate in K. A more useful theorem would provide, from permitted
initial data and invariant bounds, a decreasing estimate for (8) and an
adequate stability bound for the retained generators. Neither estimate is
established by the supplied sources.

One completely explicit way to expose the required production estimate is:
if bounds b_J(t)>=|q_J(X_{n,P}(t))| are available, then

\[
 |R_{H,K}(t)|\le\sum_{\nu\ \mathrm{deleted}}
 |a_{H\nu}(\rho_{n,P},L_{n,P},r_{n,P};U)|\prod_{J\in\mathcal C(H,\nu)}b_J(t).
 \tag{12}
\]

Bounding all neuron coordinates and all C entries merely gives bounds
growing like products of those coordinate and edge bounds. It does not make
(12) small when K grows. Moment order is not itself an approximation-small
parameter. Relying on fixed initial Gaussian laws to set later mixed graph
moments to zero would also introduce an unjustified approximation: training
creates correlations, and paired forward/reverse edges retain them.

The infinite hierarchy (3), with every diagram evaluated on X_{n,P}, is exact
for each finite n. This proves that the intended finite-width trajectory
provides an infinite solution. Infinite here counts diagrams, not neurons.
It does not prove uniqueness of arbitrary abstract moment solutions,
reconstruction of a finite-width neural state or an infinite population from such a
solution, or convergence of the finite closures (5). These are distinct
claims. Rationality and agreement of finitely many initial derivatives
cannot replace (11).

## 6. Readout on the input circle

Training-response moments alone do not determine the output at a new input.
For a fixed query set theta_1,...,theta_J, add the query response species
h1,theta, h2,theta, h3,theta to the diagram alphabet. Initialize them by the
exact original forward pass and evolve their chain rules using the same
current weight and operator velocities. Query responses do not enter the
training loss or its source sums. Include each query output diagram
q_c h3,theta in the mandatory retained set. Equations (1)--(12) then apply
to these observables as well, with larger state dimension.

For a whole circle U(theta), a finite query grid plus interpolation needs
an additional spatial regularity bound. At each consistent target state,
the derivative of tanh has magnitude at most one, so

\[
 |\partial_\theta f_{n,P}(t,\theta)|\le
 \frac{\|c(t)\|_2}{n}
 \|\widehat W_3(t)\|_{\mathrm{op}}
 \|\widehat W_2(t)\|_{\mathrm{op}}
 \|W_1(t)\|_{\mathrm{op}}
 \|U'(\theta)\|_2.
 \tag{13}
\]

If the right side is bounded by B_T on [0,T], and every angle is within eta
of a grid point, nearest-grid readout has error at most

    maximum query-output error + B_T eta.

Periodic linear interpolation has the same type of bound. This cleanly
separates scalar closure refinement from angular refinement. It does not
require a hidden neuron forward pass at each requested angle. It does require
the query-grid contractions at initialization; a fixed finite training-only
state is not silently promoted to an arbitrary-input representation.

## 7. Size, limits, and what remains unresolved

The diagram alphabet and number of diagram types at fixed K are independent
of n. Nevertheless brute-force initialization of a diagram can require
O(n^|V|) arithmetic; favorable tensor contractions can reduce this for some
graphs. The count of graphs and symbolic generator terms grows rapidly with
K,P,M,d and the query count. No efficiency advantage over the finite-width
response-memory system is proved. Constants can depend strongly on n: C=nW0 has entry size
typically of order sqrt(n) under the specified initialization, and crude
graph bounds are correspondingly poor.

There is also a definite obstruction to a coordinatewise finite population
limit of this entire dictionary. For K>=4 it contains the undecorated graph
H_parallel with two vertices joined by two parallel edges of the same
initialized matrix W0. Its size is 2+2+0=4 and its scalar value is

\[
 q_{H_{\rm parallel}}
 =n^{-2}\sum_{i,j}(nW0_{ij})^2
 =\|W0\|_F^2.
 \tag{14}
\]

With independent W0_ij distributed as N(0,1/n), each square has mean 1/n
and variance 2/n^2. Summing n^2 independent squares gives

\[
 \mathbb E q_{H_{\rm parallel}}=n,\qquad
 \operatorname{Var}(q_{H_{\rm parallel}})=2,\qquad
 \mathbb E\left|q_{H_{\rm parallel}}/n-1\right|^2=2/n^2.
 \tag{15}
\]

Thus q_H_parallel/n tends to one in L2, while the raw coordinate diverges
in probability. Storing this static coordinate as a constant coefficient
instead of a dynamic state does not remove its divergence. Fixed-n algebra
and width-independent type counts remain valid, but the full raw dictionary
cannot converge coordinatewise to finite population moments. Restriction
to generator-reachable diagrams or an appropriate renormalization would
be further work; neither is an established repair here. In particular, no
claim is made that this example is reachable from the required outputs,
or that deleting it alone produces a convergent dictionary.

An abstract initialized population operator need not have a kernel for which
all products in (1) are integrable. In particular, boundedness as an L2
operator does not justify arbitrary decorated graph contractions or their
Lp bounds. To take n to infinity one must prove existence and convergence
of the required typed contractions, control their generator and tails, and
retain the actual adjoint relations. These obligations cannot be replaced
by declaring the C entries independent at each action.

The correct scope and limit order for the proved identities is: fix n and P, define
the infinite graph hierarchy exactly, and then consider K refinement subject
to (11). Only afterwards could a separately justified P refinement connect
the result to dense training. Width limits, any interchange of these limits,
all-time bounds, and useful width-independent accuracy remain open here.

Thus this is a reference scalar construction exposing a precisely located
approximation and a conditional finite-width error theorem. It is not an
endorsed accurate or practical model, a certificate that small scalar
closures work, or a convergent infinite-population construction. For fixed
n and P the decisive missing step is a quantitative bound on the boundary
graph moments together with control of how the finite generator propagates
their omission. An infinite-population version additionally needs a justified
dictionary whose coordinates have the required finite limits.
