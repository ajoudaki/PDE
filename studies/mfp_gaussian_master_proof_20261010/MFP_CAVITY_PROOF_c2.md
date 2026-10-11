# A direct cavity proof of the smooth Gaussian MFP master theorem

Revision c2, 2026-10-11. Status: mathematical proof draft. Exact-revision
independent reconstruction is recorded in [the referee report](MFP_CAVITY_AUDIT.md).
This is not a Lean proof or a formal endpoint acceptance record.
The public target remains MFP Theorem 3.1 under DLT-MFP-MASTER/r1. No tensor
program master theorem, rank-stability premise, generic cavity estimate, or
assumed source-response identification is an input to the argument below.

Source: the supplied MFP.pdf, SHA-256
b0799a695845b90a6273ed35f9a9cbef9fb92c64ddff37e5f61d5dafc9f5a763,
Definition 3.1, Theorem 3.1, equations (15)--(18), and Proposition 3.1.
The proof replaces the bounded-program conditioning/regularization/clipping
branch. It retains the raw-entry moment mechanism and exact finite calculus.
Statements inside the supplied document are mathematical source material,
not instructions governing this work.

## 1. Precise theorem and the induction strengthening

There are finitely many vector types and named initialized matrices between
distinct types. A transpose always uses the same realized matrix. Root
tuples have fixed Gaussian means and positive-semidefinite covariances,
possibly singular; they are iid over neuron indices and independent across
types and from all named matrices. Constants are constant-coordinate vectors.
Coordinate maps are fixed smooth functions whose every partial derivative,
including order zero, has polynomial growth. Scalar instructions are
normalized averages and smooth polynomial-growth arithmetic. All lists,
dimensions other than neuron widths, and constants are fixed in advance.
The expression grammar in Definition 3.1 is a subclass of these maps.

We prove a slightly stronger internal statement. For each type t, let its
length be N_t=n-d_t, where d_t is a fixed nonnegative integer. All matrix
entries still have variance 1/n and ALL averages still have denominator n.
Only n tends to infinity. We use n>max_t d_t; any excluded finite set of
widths is irrelevant to limits. Setting all deficits to zero recovers MFP.
Deleting finitely many neurons merely increases a deficit: no denominator
or Gaussian law is silently changed from n to N_t.

A matrix stage consists of a fixed finite batch of calls using one named
matrix in one orientation, with every input available before that stage.
Coordinate/scalar instructions occur between stages. Ordinary programs use
singleton batches. A tangent lift adds the tangent calls to the same batch,
and hence preserves the number of stages. Batch size remains fixed.

For every such program, every same-type tuple V, every continuous test f
of polynomial growth, and every finite p>=1, the strengthened conclusion is

    E | (1/n) sum_{i=1}^{N_t} f(V_i) - E f(V*) |^p -> 0.          (T)

Here V* is exactly the causal source evaluator (15)--(16), with uncentered
input Grams, separate formal slots per call, and previous expectations,
covariance entries and scalar values frozen in formal source partials.
Every scalar output converges in all finite Lp to its evaluator value.
Every node has the uniform moments in (14).

The factor N_t/n tends to one. Thus empirical PROBABILITY measures in the
strengthened statement use 1/N_t; the 1/n average in (T) has the same limit.
For the public theorem d_t=0, so this distinction disappears.

We prove joint one-site convergence and two-distinct-site convergence to
independent copies of each same-type tuple along with (T). They are auxiliary
inductive conclusions used to obtain the empirical law, not additional
assumptions about the initialized or computed program.

The induction variable is the number of matrix stages, not the number of
individual matrix calls. It ranges over ALL finite batch sizes, root lists,
smooth maps and deficit vectors. This quantification is essential to the
noncircular tangent-probe step in Section 5.

## 2. Uniform moments, before any limit theorem

For each already constructed node prove simultaneously every finite moment
and every fixed order of differentiation in unconstrained raw matrix entries.
Allow independent entry variances anywhere in [0,1/n]. At each fixed width,
values and all these derivatives have polynomial growth in the finite
Gaussian input array, hence are integrable to every finite power.

Root bounds are Gaussian moments. Coordinate/scalar maps follow from finite
product and chain rules and Holder, using higher moments of earlier nodes.
For an average of N<=n terms and p>=1,

    |(1/n) sum_i a_i|^p <= (1/n) sum_i |a_i|^p.

At y=Wv a raw derivative of order k has the form

    partial_alpha y_i = sum_j W_ij partial_alpha v_j + R_i,

where R_i is a sum of at most k earlier-node derivatives of order k-1.
A transpose has the identical column calculation. Expand an even moment m
of the displayed sum. For one index tuple let b be the number of distinct
indices, S its singleton indices, and s=|S|. Put Z=product_a z_{j_a},
z_j=partial_alpha v_j, and let M_0 contain the nonsingleton weight factors.
Gaussian integration by parts once in each singleton raw coordinate gives
the exact identity

    E[(product_{u in S} w_u) M_0 Z]
       = (product_{u in S} variance(w_u)) E[M_0 partial_S Z].

All reuse, transpose and scalar-feedback dependence remains inside Z.
No assertion that w and z are independent is made. A zero-variance singleton
makes both sides zero. Gaussian moments give
||M_0||_2 <= C n^{-(m-s)/2}. The product rule and the simultaneous
earlier-node induction give ||partial_S Z||_2 <= C. Thus this tuple costs

    C n^{-(m+s)/2} <= C n^{-b},

because m>=s+2(b-s). Each fixed equality pattern has at most n^b labelings.
There are finitely many patterns at fixed m. Summation closes the induction.
Larger even moments cover every real finite p. The integration-by-parts
identity follows from the one-dimensional Gaussian density, vanishing
polynomial-times-Gaussian boundary terms, and Fubini; its hypotheses were
verified by fixed-width polynomial integrability.

Consequently, for every node and finite p,q,

    sup_{n,i} E|v_i|^p < infinity,   sup_n E|s|^q < infinity,
    E[(1/n) sum_i |v_i|^p]^q <= (1/n) sum_i E|v_i|^{pq} <= C.     (M)

These bounds also hold for every fixed tangent/reverse program used below.
They hold for every deficit vector and for the restricted cavity program.
All uniformity here concerns fixed graphs, orders, and maps, not growing
depth or derivative order.

For each initialized rectangular matrix, a 1/4-net and Gaussian scalar tail
give uniform operator-norm moments of every finite order. One may pad it
to a square matrix with independent variance-1/n entries and restrict;
restriction contracts the operator norm. For a square matrix, two sphere
nets of size at most 9^n yield

    P(||W||op>2t) <= 2*9^(2n)*exp(-n*t^2/2).

Integrating this bound above a fixed sufficiently large t proves the claim.

Write X=O_*(n^a) when for every p>=1 and epsilon>0,
||X||Lp <= C_{p,epsilon} n^{a+epsilon}. Finite sums and products preserve
the expected exponents, by Holder; epsilon can be divided among the fixed
number of factors. Equation (M) implies that the maximum of all O(n)
node coordinates and any fixed collection of their polynomially bounded
derivative coefficients is O_*(1): choose an arbitrarily high moment before
bounding the maximum. All constants can depend on the fixed program.

## 3. Exact one-type cavity and its small remainder

Fix a target type tau and delete k=1 or k=2 of its coordinates. No other
type is deleted. A named matrix has distinct endpoints, so it loses rows OR
columns, never both. There are no corner blocks. Let B_W be the retained
matrix and g_{W,i} the omitted row or column, viewed as a vector on the
other endpoint. All g_{W,i} are independent Gaussians with covariance I/n,
independent of the retained initialization and the deleted root tuples.
Reuse preserves the same g_{W,i} in every occurrence.

The old cavity program runs on the retained coordinates, with unchanged
variance and averaging denominator n. Denote its nodes by v^0,s^0.
The exact retained part of the full program can be expressed as follows.

* At a matrix call q away from tau, add sum_i g_{W,i} x_{q,i},
  where x_{q,i} is the actual input coordinate of the deleted neuron.
* At a matrix call into tau, its retained output is just the B_W action;
  its deleted output will be reconstructed as g_{W,i} dot h_q.
* At an average on tau, add beta_b/n, where beta_b is the sum of the
  actual integrand values at the deleted coordinates.
* Keep all coordinate maps, other averages, scalar arithmetic, and all
  dependence on preceding scalar values unchanged.

Treat the finite list x,beta as external values while doing the following
Taylor expansion. Substituting their actual random values gives EXACTLY
the full retained execution by chronological induction. Their moments of
all finite orders are bounded by (M). They need not be independent of g.
Setting all additive injections to zero gives the old cavity, independent
of both g and these external values.

Use Euclidean norm for vector nodes and sqrt(n)|s| for scalar nodes;
use the sum norm on any fixed finite node collection. At the old cavity,
each instruction derivative has operator norm O_*(1). In particular a
scalar-to-vector coefficient a has scaled norm ||a||2/sqrt(n), and an
average's vector-to-scalar coefficient a/n has scaled norm
||a||2/sqrt(n). Both are bounded by max_i |a_i|. Matrix blocks use ||B||op.
Finite composition proves the same bound for every old-cavity Jacobian
between an additive injection and a later node. These Jacobians depend
ONLY on the retained initialization.

Let A_{v,q} be the old derivative of vector node v with respect to an
additive vector injection after matrix call q; let B_{v,b} be its
derivative with respect to an ordinary scalar injection after average b.
The exact first variation L in the specified external forcing is

    L_v = sum_{q,i} x_{q,i} A_{v,q} g_{W(q),i}
                         + (1/n) sum_b beta_b B_{v,b}.          (L)

There is the corresponding scalar formula. Weighted operator bounds imply
||A||op=O_*(1), ||B_v||2=O_*(sqrt(n)), the unscaled vector-to-scalar row
norm is O_*(n^-1/2), and scalar-to-scalar derivatives are O_*(1).

Conditional on the retained initialization, each coordinate of A g is
Gaussian of variance at most ||A||op^2/n. For any q>=p, its coordinate
maximum has Lp norm at most C_q n^{1/q-1/2} || ||A||op ||Lq.
Its Euclidean norm is O_*(1). A scalar response row applied to g is
O_*(n^-1), since that row already has an n^-1/2 factor. Scalar injections
beta/n have weighted norm O_*(n^-1/2). There are only finitely many basis
responses in (L). Apply these estimates FIRST, and then Holder with the
actual x,beta. This proves

    ||L_v||2=O_*(1),  ||L_v||infinity=O_*(n^-1/2),
    |L_s|=O_*(n^-1).                                           (LB)

This step does not assert that L remains Gaussian after adaptive
substitution. No independence of x from g or uniform control-net theorem
is needed: (L) is a finite linear decomposition with old-only coefficients.

Put Delta=v_ret-v^0 (and similarly for scalars), and R=Delta-L.
We claim

    ||R_v||2=O_*(n^-1/2),  sqrt(n)|R_s|=O_*(n^-1/2).            (R)

Prove this along the original finite instruction DAG. Assuming it for
parents, (LB) gives Delta_v norm O_*(1), coordinate maximum
O_*(n^-1/2), and Delta_s=O_*(n^-1). The second partials of each map
on the segment between actual and cavity parent arguments have a common
O_*(1) cap H, by polynomial growth and (M). Taylor's formula bounds the
Euclidean norm of a coordinate-map remainder by

    C H (sum_j ||Delta u_j||infinity + sum_b |Delta s_b|)
        (sum_j ||Delta u_j||2 + sqrt(n) sum_b |Delta s_b|).

This is O_*(n^-1/2). The linear part propagates earlier R with weighted
operator norm O_*(1). For an average, the WEIGHTED remainder is at most

    C H n^-1/2
        (sum_j ||Delta u_j||2 + sqrt(n) sum_b |Delta s_b|)^2.

The external beta/n term cancels exactly against L. Scalar arithmetic
has the same weighted quadratic estimate. At a matrix instruction the
external vector forcing also cancels exactly, leaving B_W R_input.
Roots have zero retained error. Finite induction proves (R).

The proof uses second derivatives only along segments joining ACTUAL and
CAVITY values, both controlled by (M). It makes no unsupported claim about
arbitrary controlled nonlinear trajectories. The crucial estimate is
||z^2||2 <= ||z||infinity ||z||2; an L2-only Taylor estimate would lose decay.

## 4. Gaussian source plus normalized trace

For a call r into tau, let h_r be its input. At deleted coordinate i,
the exact output is g_{W,i} dot h_r. Substitute (L) and (R):

    g_{W,i} dot h_r
      = xi_{r,i} + sum_{q,j} x_{q,j} g_{W,i}^T A_{h_r,q} g_{W(q),j}
        + (1/n) sum_b beta_b g_{W,i} dot B_{h_r,b}
        + g_{W,i} dot R_{h_r},

where xi_{r,i}=g_{W,i} dot h_r^0. The last two terms are O_*(n^-1/2),
by Holder and the norm bounds, without an independence claim.

Conditionally on the old cavity, for g~N(0,I/n),

    E[g^T A g | old]=tr(A)/n,
    Var(g^T A g | old) <= 2 ||A||F^2/n^2
                            <= 2 ||A||op^2/n.

For independent g,h the corresponding bilinear form has mean zero and
variance ||A||F^2/n^2, with rectangular dimensions at most n. These identities
follow by expanding Gaussian second/fourth moments; symmetrize A in the
first one. Since ||A||op=O_*(1), Chebyshev gives convergence of each centered
form to zero in probability. A finite union suffices. Actual x values are
tight by (M), so multiplication by x preserves this convergence even when
x depends on the same omitted entries.

The same Gaussian vector occurs exactly when j=i and q is an earlier
opposite-orientation call of the same named matrix. Otherwise the ports
are independent. Later q have A_{h_r,q}=0 by acyclicity. Therefore

    output_{r,i}
       = xi_{r,i}
         + sum_{q<r, opposite same W} x_{q,i} tr(A_{h_r,q})/n
         + o_P(1).                                            (C)

Conditional on the retained initialization, all xi for one probe are
jointly centered Gaussian. In an oriented named group,

    Cov(xi_{r,i},xi_{t,i} | old)=(1/n)<h_r^0,h_t^0>.

Different named groups ending in tau, different deleted sites, and the
deleted root tuples are independent. The two orientations of one matrix
end in distinct types, so cannot share a source group on this one target
type. These are exact finite-width conditional facts from entry partitioning.
They do not use conditioning on an adaptive matrix transcript.

Optional finite-width check of scalar freezing: the difference between
A_{h_r,q} and its version omitting every scalar tangent path is a finite
sum of rank-one maps. Each path's weighted operator norm is O_*(1), so its
normalized trace is O_*(1/n). Scalar VALUES remain in all coefficient maps.
This explains why physical scalar feedback contributes no extra limiting
trace coefficient. Section 5 also proves the identification directly for
the full physical Jacobian.

## 5. Noncircular identification of the traces

Assume (T) and scalar convergence for all programs with at most l-1
matrix stages, for all fixed deficits and batch sizes. Let H be a node
in such a prefix and q an earlier matrix-call output of the same type.
Let J_n be the derivative of H under an additive vector perturbation
immediately after q, including physical scalar feedback.

Add an independent standard Gaussian root vector z of this type. Execute
the ordinary forward tangent program, with all initial tangents zero,
matrices fixed, and tangent z added after q. At each matrix stage put
primal and tangent calls in the same batch. Hence the tangent program has
at most l-1 stages. Its coordinate maps are derivatives/products of the
original maps, so satisfy the same smooth polynomial-growth class.
Finite chain rules give T_H=J_n z EXACTLY. In particular

    A_n=(1/n) sum_i z_i T_{H,i},
    E_z A_n=tr(J_n)/n.                                         (P)

We now identify A_n's source limit without interchanging a limit and a
derivative. Give each original matrix-call source xi_r a separate tangent
source eta_r. Retain all formal slots even if their joint covariance is
singular. Write Z for the new scalar Gaussian root. On expressions of each
type define the formal derivation

    D = sum_r eta_r partial_{xi_r} + Z partial_{xi_q},            (D)

where the Z term appears only on q's type. D fixes original roots, all
expectation/covariance coefficients and every original scalar value.

A simultaneous causal induction proves: primal fields are unchanged;
tangent fields are D applied to primal fields; tangent scalar limits are
zero; and every primal/tangent source cross-covariance is zero.

For coordinate maps this is the chain rule. For an average, D of its
integrand is linear in the centered tangent Gaussian sources and Z, with
coefficients depending only on primal sources/roots, so its expectation
vanishes. Scalar arithmetic preserves zero tangents. The matrix-input
cross Gram E[H_r D H_t] likewise vanishes. Thus new primal/tangent Gaussian
blocks may be constructed independently, with their prescribed within-block
Grams, also independently of all roots. Their Gram matrices are PSD; no
inverse or nonsingularity is used. These constructions preserve prefix laws.

At a forward call, let U_s be earlier reverse inputs, with primal source
slots zeta_s and tangent slots theta_s. The tangent source rule gives

    T_Y = eta_r + sum_s U_s E[partial_{zeta_s}(D H_r)]
                     + sum_s (D U_s) E[partial_{theta_s}(D H_r)].

The first expectation is zero by centered tangent linearity. Formally,

    partial_{theta_s}(D H_r)=partial_{zeta_s} H_r.

Consequently T_Y=eta_r+sum_s(D U_s)E[partial_{zeta_s}H_r], exactly D Y.
At the designated call q also add Z. The primal response has no extra
tangent term because its input has no tangent-source dependence. Reverse
calls are identical with endpoint types exchanged. This closes the claimed
induction, including zero-variance and duplicate sources: the identities
were calculated BEFORE restriction to Gaussian support.

All expressions have polynomial growth in a fixed finite Gaussian list,
so every expectation in this induction exists. The tangent Gaussian blocks
are independent of Z and of primal blocks; their fields need not be
independent because the coefficients depend on primal fields. Thus

    E[Z D H*]=E[partial_{xi_q} H*].

Apply the STRICTLY EARLIER-STAGE hypothesis to A_n. Conditional Jensen in
(P) gives, for every p>=1 and c=E[partial_{xi_q}H*],

    E|tr(J_n)/n-c|^p <= E|A_n-c|^p -> 0.                        (J)

This supplies exactly the traces in (C) when r is in stage l: its input
and all its nonzero influence Jacobians belong to the prefix of at most
l-1 stages. No equal-complexity master theorem is assumed. The same
argument works for the cavity dimensions by the deficit strengthening.

## 6. Closing the stage induction

At zero stages, root tuples are iid. Their empirical polynomial-growth
tests converge in L2 by independence and finite Gaussian moments; higher
Lp convergence follows by uniform moments and interpolation. Constants
have the prescribed limit because N_t/n->1. Close finite coordinate,
average and scalar instructions by the rule explained below.

Suppose all programs with at most l-1 stages satisfy the theorem. First
consider a program ending immediately after its l-th matrix batch. Every
input of this batch, every earlier scalar, and every input of an earlier
matrix call belongs to a prefix with at most l-1 stages.

Fix a type tau. Apply Sections 3--4 with one and with two deleted sites.
The cavity Gram entries in the conditional Gaussian source covariance
converge in all Lp to E[H_r* H_t*], by the earlier-stage hypothesis applied
to the retained prefix with its increased deficit. Section 5 proves the
normalized trace limits E[partial_{source q}H_r*]. Earlier scalar values
in the full and retained programs converge to the same deterministic
evaluator values by that hypothesis.

A centered Gaussian vector with random PSD covariance K_n converging in
probability to a deterministic K converges in law to N(0,K): conditionally
its characteristic function is exp(-t^T K_n t/2), whose bounded expectation
converges to exp(-t^T K t/2). The same calculation with the independent
deleted roots proves joint convergence. For two deleted sites, the exact
conditional covariance is two independent copies of K_n; hence the joint
limit has two independent Gaussian source lists, also independent of their
respective root tuples. No invertibility assumption occurs here.

Together with the trace and scalar limits, Slutsky's lemma gives joint
convergence of all these inputs and coefficients. Process (C) and the
coordinate instructions in chronological order. Each is a fixed continuous
map of earlier probe values, the Gaussian source list, and coefficients,
plus errors tending to zero in probability. The recurrence is exactly
(15)--(16), since its covariance is the uncentered input Gram and its
opposite-orientation coefficient is the formal derivative expectation in
(J). This proves one-probe convergence to the complete same-type source
tuple and two-probe convergence to two INDEPENDENT copies of that tuple.
Earlier nodes and the entire new batch are included jointly.

All probe tuples have uniform coordinate moments of every order by (M).
For a continuous polynomial-growth f, this gives uniform integrability
of f(V_i), f(V_i)^2, and f(V_i)f(V_j). Their expectations therefore
converge under the preceding one/two-probe weak convergence. Exchangeability
of neuron labels of type tau now gives

    E[(1/N_t)sum_i f(V_i)] = E f(V_1),
    Var[(1/N_t)sum_i f(V_i)]
      = Var(f(V_1))/N_t
        + (N_t-1)/N_t * Cov(f(V_1),f(V_2)) -> 0.

Thus empirical averages converge in L2 to E f(V*). The factor N_t/n->1
gives (T). Jensen and (M) uniformly bound all higher moments of these
averages. For p>2 choose q>p and use L2/Lq interpolation; for p<=2 use
Lp monotonicity. This proves (T) in every finite Lp.

Finally close the finite coordinate/scalar instructions AFTER stage l.
This is chronological, not an assumption that their averages already
converge. Suppose preceding scalars converge in every Lp to s*. Replacing
their random values by s* in a smooth polynomial-growth map has vanishing
empirical error in every fixed Lp: the mean-value bound is a polynomial
in parent magnitudes times the scalar difference, so Holder, Jensen and
(M) apply. A coordinate map with scalar s* pushes forward the already
known joint empirical law. Bounded Lipschitz tests transfer under the
vanishing empirical error; arbitrary continuous polynomial-growth tests
follow by truncation on compact balls and higher moments. A normalized
average is just the corresponding empirical test and therefore converges;
scalar sums/products preserve all-Lp convergence by Holder. Adjoin each
new node to its type's joint tuple and continue. This proves the induction
for programs ending anywhere between stages and completes (T).

## 7. Original conclusions and exact finite derivatives

Take every deficit zero. Scalar convergence is already included, or can
be recovered by broadcasting a scalar and testing with the identity.
The uniform bounds (14) were proved independently in Section 2.

For empirical W2, (T) gives convergence in probability against a countable
bounded-Lipschitz convergence-determining class and for the squared Euclidean
norm. These imply weak convergence and convergence of second moments, hence
W2 convergence in probability. Here is the needed deterministic argument.
Along a sequence of probability measures, weak convergence plus convergence
of second moments gives uniform smallness of quadratic tails by bounded
continuous truncations of ||x||^2. Partition a large ball into finitely many
small-diameter cells whose boundaries have zero limiting mass. Match common
mass within each cell; its cost is at most the squared cell diameter.
Couple the remaining mass arbitrarily; the unmatched bounded-region mass
tends to zero, while its unbounded-region cost is controlled by the quadratic
tails and ||x-y||^2<=2||x||^2+2||y||^2. Increase the radius and refine the
partition. For random measures, all width laws can be realized on their
countable product probability space: convergence in probability to the
deterministic target depends only on the width marginals. Extract from every
subsequence a further subsequence on which the countably many test values
and second moments converge almost surely, and apply this deterministic
argument. All quantities are measurable. Indeed matching the coordinates
gives W2(emp(x),emp(y)) <= ((1/N) sum_i ||x_i-y_i||^2)^(1/2), so distance
from the empirical measure to the fixed finite-second-moment target is
continuous in the finite coordinate array. This is the
same elementary topological bridge stated in MFP Appendix A.1, not its
Gaussian-program convergence theorem.

It remains to connect the admitted derivative language to primitive graphs;
the probability proof never differentiates a width limit. The finite rules
(25)--(32) supply this independent exact construction:

* Every partial of an admitted expression remains in the expression algebra.
  Forward differentiation uses finite product/chain rules and the same matrix
  name for each differentiated forward/transpose action.
* Reverse differentiation of a scalar uses vector adjoints b_u=n*dO/du and
  scalar adjoints a_s=dO/ds. Initialize a_O=1 and all other adjoints to zero.
  At v=F(u;s), add b_v*F_{u_j} to b_{u_j} and avg(b_v*F_{s_b}) to a_{s_b}.
  At t=avg(F(u;s)), add a_t*F_{u_j} to b_{u_j} and a_t*avg(F_{s_b}) to a_{s_b}.
  Products here are coordinatewise. The matrix contribution is b*u^T/n for a forward
  call and u*b^T/n for a transpose call. Summing ALL shared occurrences gives
  the ambient gradient. This follows by matching the finite differential
  in Euclidean/Frobenius pairings; no probabilistic result is involved.
  Vector mobility n*kappa therefore gives velocity -kappa*b_u and matrix
  mobility kappa gives -kappa*grad_A O. Admitted vector contractions satisfy
  n*<grad_u O,grad_u S>=avg(b_u^O*b_u^S). Rank-one matrix contractions satisfy
  <u*v^T/n,p*q^T/n>_F=avg(u*p)*avg(v*q). Fixed block multipliers are scalars.
* A represented update W+sum c*u*v^T/n acts as W h+sum c*u*avg(v*h).
  Its transpose and admitted Frobenius contractions have the same finite
  normalized-pairing expansions. Product rules preserve this finite form.
  Form the current ambient gradient before substituting prior update factors.
* A fixed number of updates therefore produces one finite graph. Repeated
  derivatives do likewise, with frozen directional seeds evaluated only
  after taking the requested derivative. In one Frechet derivative the
  direction is held fixed at its base value. After assignment, its value
  retains all its explicit source dependence in Gaussian evaluation.
  These are auxiliary deterministic differentiation arguments with assigned
  program values, not additional independently sampled random roots.
  Physical seed freezing does not freeze formal source paths. Parameter
  derivatives act on the realized program, never on the sampling law.
  All blocks of a simultaneous update are computed from the same pre-update
  state before any updated block is substituted into the next step.
* For any fixed jet order, finite Taylor's theorem and finite polynomial
  coefficient extraction implement composition. Along an actual smooth
  finite-dimensional ODE, (r+1)*theta_[r+1] is coefficient r of
  V(sum_{j<=r} theta_[j] t^j). Local existence follows from local Lipschitz
  regularity of the smooth vector field; repeated differentiation verifies
  these coefficients. Mixed finite jets use the same multivariate coefficient
  rule. In particular O''=D²O[V,V]+DO[DV[V]], including the moving field.

These steps give ONE primitive graph for every fixed requested construction,
valid at EVERY positive width. Compilation does not choose a new graph
after observing width or initialization. They are the unchanged finite
calculus argument of Proposition 3.1; all jets are finite and no analyticity,
common existence horizon, or differentiation/limit interchange is asserted.
Applying the proved primitive theorem after this exact expansion yields
Theorem 3.1 for all admitted derivative programs. A finite union of programs
retaining shared root and matrix names gives their joint assertion.

## 8. Checks, dependencies, and what this artifact does not claim

The proof uses finite Gaussian moments/IBP, elementary Gaussian quadratic
variance identities, Gaussian characteristic functions and their continuity
theorem, finite-dimensional smooth calculus, basic probability convergence
and uniform-integrability facts, and the elementary Euclidean W2 bridge.
The matrix-stage induction discharges the ONLY program-limit hypothesis
used inside the trace lemma. Neither MFP's bounded-program lemma nor a TP
master theorem appears in the dependency list. There is no clipping limit,
query perturbation limit, inverse Gram, small-label assumption, or analytic
activation assumption. Only width tends to infinity.

Discriminating checks:

1. For y=W1, v=W^T y, the trace correction is 1, so V=Z+1 and avg(v²)->2.
   A refreshed reverse matrix has no same-port trace and gives limit 1.
2. Duplicate calls Y1=WH, Y2=WH keep separate formal arguments. For
   W^T(Y1²Y2), the two response coefficients are E[2Y1Y2] and E[Y1²],
   giving 2H+H when the input is standard Gaussian, not a merged derivative.
3. For s=avg(y²), H=s*y, the physical injection Jacobian has normalized
   trace s+2*avg(y²)/n; its limit freezes the scalar s as required.
4. Naively scaling all deleted entries and Taylor expanding the complete
   adaptive trajectory FAILS: for W(t)=QW+tPW,
   W(t)^T W(t)1-W(0)^T W(0)1=t² W^T P W1. Its first derivative at zero
   vanishes, while the remainder has nonvanishing Euclidean L2 norm. The
   external-history construction retains this term as g*x exactly.

Lean status: no theorem in this document has been kernel checked by this
workstream. Existing Compression modules provide reusable Gaussian coordinate
partitions, quadratic variance/tail tools and finite calculus, but their
mere existence is not formal verification of this assembled argument.
No frozen endpoint, acceptance lifecycle, or public assumption is changed.

Research evidence: the cavity remainder was checked independently in two
worker notes; the source-response lemma was derived by a separate worker;
the supervisor reconstructed their assembly. A fresh referee reconstructed
the unified argument without relying on those favorable assessments. The
linked referee report identifies reviewed revisions and its precise scope.
Working notes are subordinate to this unified proof, not separate
authoritative theorem statements. No Lean acceptance gate is discharged by
a favorable mathematical review alone.
