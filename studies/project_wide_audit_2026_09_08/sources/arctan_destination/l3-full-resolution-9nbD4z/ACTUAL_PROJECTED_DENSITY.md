# Actual hidden projection: exact entropy balance and its remaining term

Status: exact finite-width identities and a new qualitative density result
for the canonical arctan flow. No O(n) hidden relative-entropy estimate is
proved or disproved. The existing primal and ordinary-divergence estimates
reduce that estimate to a precise conditional-entropy term. The gradient
structure alone does not prevent the branchwise projection term from
becoming negative or the hidden Jacobian from becoming singular. A fully
realizable, explicitly noncanonical construction below establishes these
structural limitations, not a sign claim about the canonical mixture's
conditional entropy. It is not a canonical counterexample.

Scope: the first 35 lines of CONTRACT_AND_LEDGER.md and the actual dynamics
in ACTUAL_GAUSSIAN_DIVERGENCE_SCOPE.md. All trained blocks and the canonical
Gaussian scalings are retained. This is a bounded theoretical resolver;
there are no simulations, source changes, or assumed response estimates.

## 1. Exact canonical gradient coordinates

Use hidden Gaussian coordinates

    X=(z,sqrt(n)U,sqrt(n)V) in R^d,       d=n+2n^2,
    C=W^(4) in R^n,                       sigma=1/n.

The initialization is X_0~N(0,I_d), C_0~N(0,sigma^2 I_n), independently.
Let h(X)=arctan(V arctan(U arctan(z))), with U,V recovered from X,
and let J(X)=D_X h(X). In feature time the exact all-trained equations are

    X'=J(X)^T C,                  C'=h(X).                 (1)

Thus in these coordinates the full vector field is the Euclidean gradient
of C^T h(X). Define the symmetric d-by-d matrix

    A(X,C)=sum_a C_a D_X^2 h_a(X).

Its full Jacobian and divergence are

    Db = [ A  J^T ; J  0 ],       div b=Tr A.              (2)

Neither the symmetry of this instantaneous matrix nor positivity of
exp(t Db) for a constant matrix makes a time-ordered flow Jacobian
symmetric or makes its hidden principal block invertible.

Write H_dif for differential entropy, to avoid confusing entropy with the
hidden state. Let rho_s be the density of X_s and m_s(x)=E[C_s|X_s=x].
For every smooth compactly supported test function psi,

    d/ds E psi(X_s) = E[D psi(X_s) J(X_s)^T C_s].

Consequently the unconditional weak continuity equation is

    partial_s rho_s + div_x(rho_s J^T m_s)=0.             (3)

On regions where m_s is differentiable its velocity divergence is

    div_x(J^T m_s)
       = E[Tr A(X_s,C_s)|X_s=x] + Tr(J^T D_x m_s).        (4)

The second term is present even though div_C(C')=0 in the joint flow.
Equation (3), rather than an unverified smoothness assertion about marginal
scores, is the unconditional form of this statement.

## 2. An exact, finite entropy identity

For the actual nondegenerate Gaussian initialization, full change of
variables gives

    H_dif(X_s,C_s)-H_dif(X_0,C_0)
                       = E integral_0^s Tr A(X_u,C_u) du.

The moment and trace bounds in ACTUAL_GAUSSIAN_DIVERGENCE_SCOPE.md ensure
that the full entropy and second moments are finite at every finite width
and finite time. The hidden relative entropy is finite by data processing
against a widened readout reference; its hidden Gaussian energy is finite.
Thus the entropy chain rule can be used without subtracting infinities.
It yields exactly

    D(law(X_s)||gamma_d)
      = E[(|X_s|^2-|X_0|^2)/2 - integral_0^s Tr A du]
        + H_dif(C_s|X_s)-H_dif(C_0).                     (5)

Define the expectation in square brackets as E_s^H. The previously proved
primal estimates give the two-sided bound

    |E_s^H| <= C_S n,                         |s|<=S.     (6)

The initial conditional entropy is exactly

    H_dif(C_0)= (n/2) log(2 pi e) - n log n.             (7)

Therefore the presently unresolved quantity is

    H_dif(C_s|X_s) - H_dif(C_0).                         (8)

In particular the proposed D(law(X_s)||gamma_d)=O_S(n) assertion is,
up to the already controlled additive O_S(n) term, exactly the assertion
that (8) is bounded above by O_S(n). This is an equation identifying the
gap, not an additional hypothesis under which the target is declared
resolved. A bound on the unconditional norm of C_s only gives
H_dif(C_s|X_s)<=H_dif(C_s)<=O_S(n), leaving an n log n gap.

The time-matched widened reference gives, by data processing,

    D(law(X_s)||gamma_d)
       <= (n/2) log(1+n^2 s^2) + O_S(n).                (9)

This is the already available estimate, not a new resolution. Notice also
that nonnegativity of relative entropy and (5)-(6) give the actual lower
bound (8)>=-C_S n. The missing bound is in the opposite direction.

If differentiations and entropy integrations are justified, the
differential version of (5) is

    d/ds D(law(X_s)||gamma_d)
      = E[X_s^T J^T C_s-Tr A] - E Tr(J^T D_x m_s),

    d/ds H_dif(C_s|X_s) = -E Tr(J^T D_x m_s).           (10)

The integrated identity (5) does not require these extra score-regularity
assumptions. In particular a pointwise derivative calculation is not used
to assert an unproved width-uniform integrability property.

The conditional mean has its own exact weak moment law. With
Sigma_s(x)=Cov(C_s|X_s=x),

    partial_s(rho m_a)
      + sum_i partial_i[rho ((Sigma+mm^T)J)_(ai)]
      = rho h_a.                                      (11)

Where differentiable, this becomes

    (partial_s + (J^T m) dot grad)m
        = h - rho^(-1) div_x(rho Sigma J).             (12)

Thus conditional differentiation introduces a covariance flux and a
density derivative; it is not replaced by the primal equation C'=h.

At physical time, replace b by B=alpha b, alpha=2(1-f). The weak hidden
velocity is E[alpha J^T C|X], not simply J^T m. The entropy identity (5)
holds with integral div B in place of integral Tr A. Its bracket is still
O_T(n) by the already proved div B=alpha Tr A-2K identity and primal
bounds. Hence the same conditional-entropy gap survives physical time.

## 3. Canonical positive result: hidden densities exist at fixed width

Fix n, a finite feature time s, and any deterministic initial readout c.
Let

    F_(s,c)(x)=pi_X Phi_s(x,c),

where Phi is the complete actual feature flow. Then F_(s,c) is real
analytic, its Jacobian determinant is not identically zero, and the
pushforward of the hidden initialization Gaussian by F_(s,c) is
absolutely continuous. This includes c=0. No uniform-in-n bound on this
density or its entropy follows from the proof.

Proof of analyticity. Arctan is real analytic at every real argument,
and the finite-width vector field is composed of arctan, its derivatives,
and finite sums and products. Near a compact segment of any fixed real
trajectory it has local holomorphic extensions. Uniform Picard iteration
on a sufficiently small complex neighborhood gives holomorphic dependence
of the short-time solution on the initial data. Finitely many such
short-time maps cover the fixed compact trajectory interval; their
composition is analytic near that initial point. This proves local real
analyticity everywhere, with no width-uniform radius claimed. The analytic
initial-data fact is also stated in Theorem 4.2 of
[Teschl's author-hosted ODE text](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).

Proof of a nonzero determinant. At U=V=0, for any z and c, one has h=0
and J=0. This full state is stationary. The variational generator is the
constant block matrix [A,0;0,0], with A symmetric, so

    D_x F_(s,c)=exp(sA),       det D_x F_(s,c)>0.

Indeed A has only the mixed U,V Hessian blocks there, so Tr A=0 and this
determinant is 1. For c=0, A=0 and the hidden derivative is the identity.
Thus the determinant is a nontrivial analytic scalar on connected R^d.

A nontrivial real analytic scalar has a Lebesgue-null zero set. One short
proof is as follows. At each zero some derivative has minimal positive
order and is nonzero; otherwise the local Taylor series vanishes and
analytic continuation on the connected domain makes the function zero
everywhere. Subtract one derivative from a minimal nonzero multi-index.
The resulting derivative vanishes at that point and has a nonzero first
derivative. Its regular zero set is locally a smooth hypersurface.
Stratifying by the countably many derivative multi-indices covers the
original zero set by these null regular zero sets. This is the argument in
[Mityagin, Proposition 0](https://arxiv.org/pdf/1512.07276).

Outside this null critical set, the inverse function theorem supplies a
countable collection of neighborhoods on which F_(s,c) is a smooth
diffeomorphism. Images of target-null sets under each local inverse
are null, since that inverse is locally Lipschitz. A Gaussian initial law
gives zero mass to the critical set, so
its pushforward gives zero mass to every target null set. This proves
absolute continuity. Mixing over the actual C_0 Gaussian preserves it.

The same argument works for fixed physical time. The physical vector
field is analytic and at the same stationary point its hidden variational
matrix is 2A, so its hidden determinant is again nonzero.

This settles qualitative hidden absolute continuity even for the
zero-readout proxy. It does not settle the density bounds for the canonical
tiny-readout sequence and supplies no zero-to-tiny stability transfer.

## 4. Exact geometry of the missing term

Along a full actual trajectory, write the initial-hidden derivatives as

    P=D_(X_0) X_s,           R=D_(X_0) C_s.

They obey exactly

    P'=A P+J^T R,       R'=J P,       P_0=I, R_0=0.     (13)

On intervals where P is invertible, the conditional graph derivative
K=R P^(-1) obeys

    K'=J-K A-K J^T K,
    d/ds log|det P| = Tr A+Tr(J^T K).                  (14)

This K fixes the initial readout and one inverse branch. It is not the
conditional-mean derivative Dm for the actual Gaussian mixture. Folding,
branch weights, and the distribution of C_0 must still be retained when
passing from (14) to a marginal law.

At regular values the fixed-c density can equivalently be expressed by
the area formula as a sum of gamma_d(x_0)/|det P(x_0,c)| over preimages.
The actual density then integrates that expression against gamma_C(dc).
One may instead apply coarea directly to the submersion pi_X Phi_s;
the fiber Jacobian is sqrt(det(D(pi_X Phi_s) D(pi_X Phi_s)^T)).
Neither formula permits replacing the projected/fiber Jacobian by the
full determinant exp(integral Tr A).

## 5. Realizable structural sign test (explicitly noncanonical)

This paragraph changes the feature map and dimension solely to test the
proposed implication from the gradient form (1). It is not an arctan
network example and does not disprove its O(n) entropy bound.

Take x=(u,v) in R^2, C=(c_1,c_2) in R^2. Near the compact reference
trajectory define the smooth feature map

    h_1(u,v)=j(v)u,
    h_2(u,v)=v+(1/2)a(v)u^2.                            (15)

Choose smooth time profiles j_*(t), A_*(t) made from three separated
single smooth bumps, each strictly of its indicated sign in the
interior of its support:

    j_*>0 in a subinterval of (0,1), integral_0^1 j_*=1;
    A_*<0 in a subinterval of (1,2), integral_1^2 A_*=-2;
    j_*<0 in a subinterval of (2,3), integral_2^3 j_*=-1;

and zero outside these three phases. Set

    j(v)=j_*(arcosh v),
    a(v)=A_*(arcosh v)/sqrt(v^2-1)

on the supports, extending smoothly by zero elsewhere. All supports are
away from v=1, so these are smooth functions. Multiply both components
of (15) by a smooth compact cutoff, even in u and equal to one on a
neighborhood of the reference trajectory. This makes h bounded and smooth
without changing
any calculation below.

From u(0)=0, v(0)=1 and C(0)=0 the exact gradient system (1) has

    u=c_1=0,           v=cosh t,           c_2=sinh t,
                                                        0<=t<=3.

The transverse derivatives p=partial u_t/partial u_0 and
r=partial c_(1,t)/partial u_0 obey the genuinely realized subsystem

    p'=A_*(t)p+j_*(t)r,       r'=j_*(t)p,
    p(0)=1, r(0)=0.                                      (16)

The disjoint phases give exactly

    (p(1),r(1))=(cosh 1,sinh 1),
    (p(2),r(2))=(e^(-2) cosh 1,sinh 1),
    p(3)=e^(-2) cosh^2 1-sinh^2 1<0.                    (17)

The last inequality follows from tanh 1>1/2>e^(-1).
Hence p crosses zero in the third phase. The longitudinal hidden
derivative is cosh t>0, so the full hidden determinant also vanishes.
The full-flow trace along this trajectory is A_*, its integral is -2,
and the full determinant at t=3 is e^(-2). Primal states, feature map,
and the full trace integral all remain bounded.

Before the first crossing, r>0 and p>0 while j_*<0. Thus the transverse
contribution j_*r/p in (14) is negative and tends to minus infinity as
the crossing is approached. The bounded longitudinal contribution cannot
restore a pointwise nonnegative sign. This is an actual vector-feature
gradient flow, not a merely prescribed time-dependent block matrix.

There is also genuine global noninjectivity for the fixed-time hidden map,
not merely a zero derivative. Denote its two outputs at time 3 by
U_3(u_0,v_0) and V_3(u_0,v_0), always with initial C=0. The even cutoff
preserves the symmetry (u,c_1)->(-u,-c_1), while (v,c_2) are unchanged.
Thus U_3 is odd and V_3 is even in u_0. At v_0=1, (17) shows
U_3(u_0,1)<0 for sufficiently small u_0>0. For sufficiently large
u_0 the initial point is outside the cutoff support, hence stationary,
so U_3(u_0,1)=u_0>0. Continuity gives u_*>0 with U_3(u_*,1)=0.
Evenness of V_3 then yields identical hidden outputs from the distinct
initial points (u_*,1) and (-u_*,1).

This proves that gradient structure and bounded primal/full-trace data
alone do not give a strictly positive pointwise lower bound on |det P| or
injectivity of the hidden projection. No claim that the reference
singularity is a generic Whitney fold is made. It does not prove that
the averaged Gaussian
conditional-entropy term (8) is large; it does not replace the canonical
initialization, and no limiting Gaussian claim is inferred from this
single trajectory.

## Scoped outcome

Established for the canonical model: (3), (5), (11), the exact response
system (13), and finite-width hidden absolute continuity even at zero
initial readout. The available entropy estimate remains (9).

The exact remaining equation is (5)-(8): O(n) hidden relative entropy
requires an O(n) upper bound on the increase of the readout's conditional
differential entropy. The existing primal and full-divergence estimates
control the other term only. Gradient form alone does not justify dropping
the conditional derivative or asserting pointwise monotone contraction.

No canonical counterexample to O(n) hidden entropy has been obtained, and
no O(n) proof has been obtained. Even such an entropy bound would still
need a separate bridge to the specific adaptive deleted-query likelihood
and its required uniform integrability; it is not itself the requested
global mean-field theorem.
