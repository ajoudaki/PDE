# Exact Gaussian and kernel reduction of the p=1 closure

Claim type: exact identities and proved reformulations of the prescribed
population closure. These are study results, not a promotion. The finite
Gaussian expectations below are exact definitions, not assertions that tanh
integrals have elementary antiderivatives.

## 1. Scope and source conventions

Let mu=sum_a mu_a delta_(u_a,y_a), where u_a in S1, mu_a>=0,
sum_a mu_a=1, and |y_a|<=Y<infinity. Zero weights may be discarded.
No separation, rank, symmetry, balance, or label compatibility is assumed.
We use physical time and L=sum_a mu_a(f_a-y_a)^2. The state metric is
L2 for w and c, Frobenius for M. There is no neural-width or closure-order
limit in any statement below.

Sources read for the construction: docs/observable_p1.md in full;
docs/global_nonlinear.md Section 3, C.4.7.9 parts 2--4, C.4.7.10.B's
initialization construction, C.1's H3.N1--H3.N2 equations and C.3's
fixed-order existence argument; docs/gaussian_calculus.md Sections 1--4 and its finite
contraction/observable calculus. The p=1 dictionary here is specifically
C.4.7.10's tanh-core, eta=1/4096, inverse-Cholesky version, as specified
by docs/observable_p1.md. It is not the earlier pilot-sine dictionary.

The b_l are normalized initialized observable feature columns. They are
neither eigenvectors nor exactly orthonormal: the positive ridge remains.

## 2. Complete explicit initialization

Put eta=1/4096. Let G_1,G_2,Z_1,Z_2 be independent standard Gaussians
on population 1 and let Ztilde_1,Ztilde_2 be independent standard Gaussians
on the separate population 2. Define scalar constants and coordinate fields

    nu = E tanh(G)^2,
    H_i = tanh(sqrt(nu) Ztilde_i),
    tau = E H_i^2,       alpha = 1-tau,
    h_i = tanh(G_i),
    k_i = tanh(sqrt(tau) Z_i + alpha h_i),
    s = E k_i^2,        beta = E h_i k_i,       gamma = 1-s.

Here nu is the scalar called v in docs/observable_p1.md; it is renamed
only to keep v available for a vector kernel argument below. The response
alpha h_i is required by reuse of the actual transpose. In particular k_i
and G_i are correlated. Different coordinate pairs (G_i,Z_i) are independent.

Set

    ell_h = sqrt(nu+eta),
    ell_k = sqrt(s+eta-beta^2/(nu+eta)),
    ell_H = sqrt(tau+eta).

All are positive: beta^2<=nu*s, so
ell_k^2>=eta+s*eta/(nu+eta)>0. In the canonical feature ordering the full
columns and matrix are

    b1 = ((1+eta)^(-1/2), h1/ell_h, h2/ell_h,
          (k1-beta*h1/(nu+eta))/ell_k,
          (k2-beta*h2/(nu+eta))/ell_k),
    b2 = ((1+eta)^(-1/2), H1/ell_H, H2/ell_H),

             [0   0        0        0        0       ]
    D=M(0) = [0   d_h      0        d_k      0       ],
             [0   0        d_h      0        d_k     ]

    d_h = alpha*nu/(ell_h*ell_H),
    d_k = (alpha*beta*eta/(nu+eta)+tau*gamma)/(ell_k*ell_H).

Also w(0)=g=(G1,G2), c(0)=0. Thus M(0) does not depend on training
inputs or labels. Its two nonzero Euclidean singular values both equal
sqrt(d_h^2+d_k^2)>0. This is a statement about the coefficient matrix;
the dictionary functions themselves are not singular vectors of A0.

For completeness, the raw Gram matrices are

    G1 = diag-block(1, [nu I2, beta I2; beta I2, s I2]),
    G2 = diag(1,tau,tau).

The finite source rule gives, for bounded smooth core functions F and B,

    E2[B A0 F] = sum_i E1[F h_i] E2[partial_Xi_i B]
                + sum_i E1[partial_zeta_i F] E2[B H_i],

where Xi_i=sqrt(nu) Ztilde_i, zeta_i=sqrt(tau) Z_i, and the partials
hold other named coordinates fixed. The first term follows by Gaussian
regression and integration by parts; the second is the reverse-use response.
For B=H_i and F=h_j,k_j the raw coefficients are respectively
alpha*nu delta_ij and (alpha*beta+tau*gamma) delta_ij. Constant pairings
vanish. Multiplying by L2^{-1} and L1^{-T} gives exactly D above; the
subtraction of beta*h/(nu+eta) leaves the displayed eta term in d_k.
This reproduces the established initialization instead of replacing its
joint laws or normalization.

Only scalar and two-dimensional Gaussian expectations are needed for these
constants. An exact quadrature-free numerical value is not being asserted.

## 3. Exact invariant reduction, independent of the data geometry

Under simultaneous sign reversal of the four lower Gaussian roots, the
nonconstant b1 entries and g are odd. Under upper sign reversal, the
nonconstant b2 entries are odd. Initially w and c have these respective
odd parities, and the constant row and column of M are zero.

If this holds at a current state, tanh(w.u) is odd in lower marks, so
a_0(u)=0. The upper preactivation and activation are odd, their derivative
gate is even, and c is odd. Hence d_0(u)=0. The matrix velocity
-2 sum mu_a r_a d_a a_a^T has zero constant row and column; the lower
and upper velocities are odd in their own marks. Uniqueness of the
characteristic equations therefore preserves this class for every finite
time. No transformation of the data is used in this proof.

From now on b1 denotes the four nonconstant entries and b2 the two
nonconstant entries; M denotes the corresponding full 2 by 4 block.
Then

    M(0) = [d_h I2  d_k I2].

Deleting these identically inactive matrix entries is an isometry for the
moving state metric. No diagonal constraint is imposed at positive time.

All lower initial roots are recoverable from b1 on its probability-one
open support: h_i=ell_h b1_i, g_i=artanh(h_i),
k_i=ell_k b1_(i+2)+beta*h_i/(nu+eta), and
Z_i=(artanh(k_i)-alpha*h_i)/sqrt(tau). Likewise Ztilde is recoverable
from b2. Along the initialized trajectory w is a deterministic function
of b1 and c a deterministic function of b2. Consequently the populations
can be represented by characteristics over fixed four- and two-dimensional
Gaussian carriers. In this representation g is redundant information,
although it remains available for canonical initial/current observations.

## 4. Every initialized input geometry is an explicit integral

For rho in [-1,1], use independent standard G,Z,Z' and define

    A(rho) = E[tanh(G) tanh(rho*G+sqrt(1-rho^2)*Z')],
    B(rho) = E[tanh(sqrt(tau)*Z+alpha*tanh(G))
               tanh(rho*G+sqrt(1-rho^2)*Z')].

At rho=+-1 the sqrt term is simply zero. For u=(u1,u2) in S1,

    a_0(u) = ( A(u1)/ell_h, A(u2)/ell_h,
               [B(u1)-beta*A(u1)/(nu+eta)]/ell_k,
               [B(u2)-beta*A(u2)/(nu+eta)]/ell_k ).

Proof: condition the lower input G.u on the selected coordinate G_i;
its remaining independent Gaussian variance is 1-u_i^2. The reverse
noise for the unused coordinate integrates out. Substitution in E[b1 H1]
gives the formula. Thus v_0(u)=D a_0(u) has entries kappa(u_i), where

    kappa(rho) = d_h*A(rho)/ell_h
                 + d_k*[B(rho)-beta*A(rho)/(nu+eta)]/ell_k.

This is an explicit odd function, not an assumed linear one. The initialized
first-layer Gram for any pair is A(u.u'). The upper Gram is given in the
next section. Mixed dictionary/input tensors, gates, input derivatives, and
all finite products of these fields are integrals over at most four lower
or two upper independent Gaussians. Different populations are contracted
separately. The primitive expectations A and B require at most two and
three Gaussians respectively.

For angular input derivatives it is safer to differentiate tanh(G.u(theta))
directly than the sqrt(1-rho^2) parametrization at endpoints. At each fixed
order the resulting Gaussian polynomials are integrable, while tanh and
its derivatives are bounded. Dominated differentiation is therefore valid.
Neither input coincidence nor an antipodal pair creates an inverse-Gram
singularity in these formulas. No geometry-independent conditioning follows.

## 5. One fixed kernel computes the entire upper activation geometry

For vector arguments v,z in R2 define the fixed function

    K(v,z) = E2[tanh(b2.v) tanh(b2.z)]
           = E_{Ztilde in R2}[
               tanh(tanh(sqrt(nu) Ztilde).v/ell_H)
               tanh(tanh(sqrt(nu) Ztilde).z/ell_H)].                 (1)

This kernel is determined before seeing the training law. At every time set

    a_t(u) = E1[b1 tanh(w_t.u)],       v_t(u)=M_t a_t(u).

Then the exact current upper activation is H2_t(u)=tanh(b2.v_t(u)), and

    E2[H2_t(u) H2_s(u')] = K(v_t(u),v_s(u'))                       (2)

for any two times and inputs. In particular the paired upper displacement is
K(v_t,v_t)+K(v_0,v_0)-2K(v_t,v_0). Every finite upper activation joint
law is the pushforward of the same TWO Gaussian roots, regardless of the
number of inputs or elapsed time. All higher activation tensors are the
analogous two-dimensional expectations of products. This statement concerns
activations; products containing trained c also require its current value
or the equivalent representation below.

Since b2 is bounded, differentiation under (1) yields, for example,

    grad_1 K(v,z) = E2[b2 sech^2(b2.v) tanh(b2.z)],
    grad_1 grad_2 K(v,z)
       = E2[b2 b2^T sech^2(b2.v) sech^2(b2.z)].                    (3)

All higher derivatives are equally explicit. The kernel is positive
semidefinite because sum_ij e_i e_j K(v_i,v_j)
=E2[(sum_i e_i tanh(b2.v_i))^2]>=0. It respects the signed-coordinate
permutations of the b2 law. Its law is not replaced by a rotationally
invariant Gaussian law; K is not assumed to depend only on v.z and norms.

## 6. Exact autonomous replacement of the upper readout population

Define the evolving scalar function on R2

    F_t(v) = E2[c_t(b2) tanh(b2.v)].                                (4)

Then the two upper contractions used by the closure are exactly

    f_t(u)=F_t(v_t(u)),          d_t(u)=grad F_t(v_t(u)).             (5)

At fixed v, differentiating (4) and substituting the c equation gives

    partial_t F_t(v) = -2 sum_a mu_a r_a K(v,v_t(u_a)),
    F_0(v)=0,                 r_a=F_t(v_t(u_a))-y_a.                (6)

The full reduced system is (5)--(6) together with

    w_dot = -2 sum_a mu_a r_a sech^2(w.u_a)
                 [b1^T M^T grad F(v_t(u_a))] u_a,
    M_dot = -2 sum_a mu_a r_a grad F(v_t(u_a)) a_t(u_a)^T.          (7)

The remaining lower expectation in a_t is four-dimensional Gaussian
integration of the current characteristic w. Equations (6)--(7) are
autonomous in (w,M,F). They use neither a future path nor a growing list
of Gaussian sources. The function F is an infinite-dimensional state;
these equations are not advertised as finitely many scalar ODEs.

### Information and metric are preserved

Let V be the closed span in L2(population 2) of h_v(b)=tanh(b.v), v in R2.
For c in V define Tc(v)=<c,h_v>. If Tc vanishes for every v, c is
orthogonal to a dense subset of V, hence c=0. Give H=T(V) the inner
product <Tc,Tc'>_H=<c,c'>_2. This makes T an isometric bijection of
Hilbert spaces. Evaluation is bounded since |Tc(v)|<=||c||_2 ||h_v||_2.
Moreover K(.,z)=T h_z and <F,K(.,z)>_H=F(z). These facts directly
construct the needed reproducing-kernel space without an external theorem.

The initialized readout is in V. Its velocity is a finite combination of
h_v and therefore remains in V after time integration. Thus F determines
the entire reached readout c, not merely its values on the training inputs.
The directional derivatives of h_v belong to V too: their difference
quotients converge in L2 by bounded b2. It follows that the derivative
evaluations in (5) are also legitimate bounded linear functionals on H.

Conversely a sufficiently regular solution of (6)--(7) in H pulls back by
T^{-1} to the exact c equation. This proves equivalence, including restart,
on the canonical initialized trajectory. Norms satisfy

    ||c_t||_2 = ||F_t||_H,             ||c_dot_t||_2=||F_dot_t||_H.

The induced metric is exactly the original L2--Frobenius metric. No norm
or Gaussian law is reset during training. At an arbitrary ambient state,
a component of c orthogonal to V is invisible and stationary; retain it
separately if reconstructing that noncanonical state is required.

Integrating (6) also gives the causal identity

    F_t(v)=-2 sum_a mu_a integral_0^t r_a(s) K(v,v_s(u_a)) ds.       (8)

This is a useful Volterra representation, not a replacement finite saved
state. The autonomous formulation stores F, not the history in (8).

### Why F is a function rather than a fixed finite coefficient list

The kernel (1) has infinite rank on its coefficient domain. To prove this,
choose any N distinct positive scalars s_j and consider v_j=s_j e1.
The random coordinate b2_1 has positive density throughout
(-1/ell_H,1/ell_H). If sum_j e_j tanh(s_j b2_1)=0 almost surely,
continuity makes it zero on this interval. Differentiating its analytic
expression at zero gives

    sum_j e_j s_j^(2k+1)=0,       k=0,...,N-1.

The odd Taylor coefficients of tanh are nonzero: writing
tanh(x)=sum_{k>=1}(-1)^(k-1) a_k x^(2k-1), the local analytic equation
tanh'=1-tanh^2 gives a_1=1 and
(2k-1)a_k=sum_{i+j=k} a_i a_j>0 for k>=2.
The displayed linear system is an invertible Vandermonde system in s_j^2
after absorbing one factor s_j into e_j, so all e_j vanish. Therefore
the N by N Gram K(v_i,v_j) is strictly positive definite for every N.

Thus no fixed finite linear basis represents all functions h_v. This
does not exclude a special invariant family for particular data or a
different nonlinear finite-dimensional realization; neither is assumed
or proved here. Finite quadrature or a finite expansion of F introduces
a further approximation, separate from the exact p=1 closure.

### Moving kernel arguments retain hidden learning

The total derivative of a prediction is

    f_dot(u) = -2 sum_a mu_a r_a K(v_t(u),v_t(u_a))
               + grad F_t(v_t(u)).v_dot_t(u).                     (9)

The second term must not be omitted. The kernel in (1) is fixed on its
coefficient domain, but v_t(u)=M_t a_t(u) moves through that domain.
This reformulation preserves both hidden layers' updates.

## 7. Exact finite contractions of the current dynamics

Put G_ab=u_a.u_b and

    C_ab(t)=E1[b1 b1^T sech^2(w_t.u_a) sech^2(w_t.u_b)].

Differentiate a_t(u_a), substitute w_dot and contract b1. This gives

    a_dot_a=-2 sum_b mu_b r_b G_ab C_ab M^T d_b.                   (10)

With v_a=M a_a, v_dot_a=M_dot a_a+M a_dot_a. Substitution in (9) yields

    f_dot_a=-2 sum_b mu_b r_b Kfull_ab,
    Kfull_ab=K(v_a,v_b)+(a_a.a_b)(d_a.d_b)
                       +G_ab d_a^T M C_ab M^T d_b.                (11)

Each of the three summands is a Gram of a parameter-gradient block, so
Kfull is positive semidefinite. More explicitly, the last one is the
L2 Gram of sech^2(w.u_a)(b1^T M^T d_a)u_a; the middle one is the
Frobenius Gram of d_a a_a^T. This independently checks the transpose and
the unchanged physical metric.

Equations (10)--(11) are observable equations, not a claimed closure in
the finite list (a,M,f): differentiating C_ab introduces further gated
lower moments. Equation (7)'s lower characteristic remains the justified
state for these contractions. No finite-dimensional impossibility theorem
is asserted.

## 8. Initial velocities and the first hidden motion

Write a_a=a_0(u_a), v_a=D a_a, H_a=tanh(b2.v_a), K_ab=K(v_a,v_b).
All quantities in this section are explicit Gaussian expectations. At zero,

    w_dot=0,       M_dot=0,       c_dot=2 sum_b mu_b y_b H_b,
    f_dot_a=2 sum_b mu_b K_ab y_b,
    d_dot_a=2 sum_b mu_b y_b grad_1 K(v_a,v_b).                   (12)

The first hidden accelerations are

    M_ddot=4 sum_ab mu_a mu_b y_a y_b
                     grad_1 K(v_a,v_b) a_a^T,
    w_ddot=4 sum_ab mu_a mu_b y_a y_b sech^2(g.u_a)
                [b1^T D^T grad_1 K(v_a,v_b)] u_a.                 (13)

They follow by differentiating (7); at zero all terms except the derivative
of d vanish. Consequently a_dot_0=v_dot_0=0. The total tangent kernel
in (11) has first derivative zero: its first summand has stationary
arguments and each other summand contains two factors d=0. Thus

    f_ddot_a=-4 sum_bc mu_b mu_c K_ab K_bc y_c.                   (14)

This equality to the frozen-feature second output derivative does not mean
the hidden state is frozen: it starts moving at quadratic order by (13).
The first possible output difference is cubic order, and all its terms
are obtainable from the same finite recurrence described below.

There is a concise interpretation of (13). Regard theta=(w,M) with its
unchanged hidden-state metric, and define the current geometry functional

    J(theta)=||sum_a mu_a y_a H_a(theta)||_2^2
            =sum_ab mu_a mu_b y_a y_b K(v_a(theta),v_b(theta)).

Let J_a denote the derivative map delta theta -> delta H_a, only within
this paragraph. Differentiating J gives
grad_theta J=2 sum_a mu_a y_a J_a^*(sum_b mu_b y_b H_b).
The hidden gradient-flow equation and c_dot from (12) therefore imply

    theta_ddot(0)=2 grad_theta J(theta_0).                         (15)

Since theta_dot(0)=0, differentiating J(theta_t) twice gives

    (d/dt)J(theta_t)|_0=0,
    (d^2/dt^2)J(theta_t)|_0=2||grad_theta J(theta_0)||^2>=0.        (16)

This precisely describes the first hidden response: its acceleration
increases the squared norm of the label-weighted upper feature mean,
when that gradient is nonzero. Same-label and opposite-label pairings
enter J with opposite signs. This is a local identity, not a monotonicity
or convergence claim for later times and not a claim that each pair
moves in a prescribed direction.

## 9. Finite Gaussian DAGs for arbitrary finite derivative order

Use ordinary time coefficients X[k]=X^(k)(0)/k!. For each k evaluate
the forward expressions with convolution products, compose tanh through
degree k, form r,d,q with their full convolutions, and set

    (w[k+1],c[k+1],M[k+1])=RHS[k]/(k+1).                        (17)

At degree k all state coefficients through k are known, so this is
triangular. Bilinear convolution follows by multiplying finite Taylor
polynomials; scalar composition follows from the finite Taylor formula
for tanh. Induction proves that (17) produces the actual derivatives
of the closure, including derivatives of M, M^T, gates, and residuals.

Every initialization coefficient is a finite expression in the original
four lower or two upper Gaussian roots, bounded tanh derivatives, the
known dictionary, finite sums/products and population expectations.
Taking an expectation creates a deterministic scalar or tensor used by
later nodes. There are no new Gaussian source coordinates as k grows.
Mixed input derivatives add finite Gaussian-polynomial factors and remain
integrable. This is a finite computational DAG at each fixed order; the
number of nodes may grow rapidly and is not bounded uniformly in order.

Derivative contractions of loss, hidden Grams, forward/backward fields,
matrix singular-value invariants such as tr[(MM^T)^j], and their finite
mixed jets are all covered. Singular-value derivatives themselves require
care at multiplicities; polynomial invariants avoid that issue.

## 10. A convergent local expansion for this fixed closure

Here one can say more than formal coefficient correctness. The fixed-p
bounded dictionary implies a positive time-analyticity radius. This
statement is about the closure, not the infinite-order neural calculus.

At any reached real state let B_l>=1 bound |b_l| and put

    Q=max(2,Y,B1,B2,||c_*||_infty,||M_*||_F),
    delta=1/(128 Q^3),       V=128 Q^5,
    R=delta/(4V)=1/(65536 Q^8).

Use the maximum of the L-infinity norm of w-w_*, the L-infinity norm
of c-c_*, and the Frobenius norm of M-M_* as the increment norm.
The real field w_* itself can be unbounded; only its increment is complexified.

**Claim.** The solution increments are holomorphic for |t-t_*|<R and
bounded there by delta/2. For 0<=h<R, the degree-q Taylor remainder
in the increment norm is at most

    (delta/2) (h/R)^(q+1)/(1-h/R).                              (18)

**Proof.** On |Im z|<=pi/4,
|tanh z|^2=(sinh^2(Re z)+sin^2(Im z)) /
          (sinh^2(Re z)+cos^2(Im z))<=1,
and |sech^2 z|<=2. In the complex increment ball of radius delta,
the lower preactivation stays in this strip. Hence |a|<=B1,
|a-a_*|<=2B1 delta, and

    |b2^T M a - b2^T M_* a_*|
       <=B2[delta B1+||M_*|| 2B1 delta]
       <=3Q^3 delta=3/128<pi/4.

The initial quantity in this subtraction is real, so the upper gate is
also in the strip. Bounds |c|<=2Q, |M|<=2Q, |r|<=3Q,
|d|<=4Q^2 and |q|<=8Q^4 follow. Thus the three velocities are bounded
respectively by 96Q^5, 6Q, and 24Q^4, all at most V.
The vector field is holomorphic on this ball: pointwise scalar holomorphy,
uniform strip bounds, and bounded integration give norm-convergent local
Cauchy expansions; finite products and bounded linear operations preserve
them. No unbounded Gaussian product estimate is used.

Cauchy's one-variable formula along each unit increment direction bounds
the derivative operator on the ball of radius delta/2 by 2V/delta.
Picard iteration on holomorphic paths over |t-t_*|<=R, using integration
along the straight segment, stays within delta/2 since RV=delta/4.
Its contraction constant is at most R*2V/delta=1/2. Uniform convergence
of the iterates gives a holomorphic solution: pass to the limit in their
Cauchy integral formula on every strictly smaller disk. On the real
interval uniqueness identifies it with the closure solution. The solution
bound and Cauchy's coefficient formula give coefficient norms at most
(delta/2)R^(-k), by approaching R from below. Summing the geometric tail
proves (18).

On any finite real horizon, established energy/continuation bounds give
finite bounds for c and M, so the radii at reached states have a common
positive lower bound. This gives local analytic continuation along the
entire real trajectory. It does NOT prove that one Taylor series about
initialization converges for every positive time. At initialization all
coefficients in (18) are finite Gaussian DAGs from (17); at a reached
restart they are functionals of that complete current state. The small
explicit radius is a sufficient bound, not a claim of useful numerical cost.

## 11. Boundaries of the simplification

All initialized coefficients and geometries have explicit Gaussian-integral
provenance. All current upper activation geometries have the fixed kernel
(1), and the readout population has the exact equivalent function dynamics
(6). The remaining autonomous state is a lower characteristic w on four
Gaussian coordinates, a 2 by 4 matrix, and F on a two-dimensional domain
with its declared Hilbert-space norm. Both hidden layers still learn.

We have not reduced w or F to finitely many scalar coefficients, nor shown
that the current training Gram alone determines their evolution. Initial
Gaussian computability is not Gaussianity of trained w or c. Geometry is
not forced to depend only on input separation because the fixed dictionary
uses its specified coordinate axes. No fitting rate, long-time convergence,
neural-network identification, or order-to-infinity result is claimed.
