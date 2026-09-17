# Second-order geometry of the full three-coordinate correlation family

2026-09-16. Frozen scoped theoretical report. No experiment, code change,
network-limit claim, or promotion is made. The new conclusions are exact
second-order formulas, a two-scalar characterization of any symmetric
transverse rank loss, its isolated quadratic-contact structure, and an
endpoint-regularity extension theorem. Positivity at every broad-family
endpoint remains unproved.

Scientific inputs were the complete `three_coordinate_candidate.md`,
`perturbation_metric_template.md`, `perturbation_metric_check.md`, and
`resolution_open_family.md` in this study, and the assigned established
`docs/README.md`, `docs/NOTATION.md`, `docs/observable_p1.md`, and the relevant
C.4.7.9/C.4.7.10 B/C.1/D.3 material. No other research reports were read.
The investigate-conjectures and solve-math-rigorously skills governed this
bounded derivation. Statements below are internal research results.

## 1. Contract and parameter geometry

Retain the exact prescribed dimension-three, order-one tanh closure: the
correlated initialized lower marks, eta=1/4096 Cholesky coefficients, the
full evolving 4-by-7 matrix and its actual transpose, and both moving
populations. The state is X=(w,c,M), initialized by (G,0,D), with physical
metric

    ||delta X||^2 = E1|delta w|^2 + E2|delta c|^2 + ||delta M||F^2.

Absorb the labels y=(1,1,-1) into the unit inputs, writing v_i=y_i u_i.
The labels are then all +1, because f(-u)=-f(u) as a function of the full
state. Let v_1=(a,b,b), v_2=(b,a,b), v_3=(b,b,a), where

    a^2+2b^2=1, a!=b, rho=2ab+b^2.

Set p=a-b and q=a+2b. Direct calculation gives

    p^2=1-rho, q^2=1+2rho,
    a=(q+2p)/3, b=(q-p)/3, -1/2<=rho<1.                 (1)

Consequently rho alone does not specify a point of the canonical dictionary
family: away from the boundaries the signs of p and q specify branches.
The fixed dictionary has coordinate-permutation and simultaneous-sign
symmetries, not arbitrary rotation invariance. A statement indexed only by
rho must either specify its branch or prove independence of that choice.
At rho=-1/2 the three input vectors have a linear relation, although their
initialized upper features remain independent by the supplied candidate.

For one current input v, use

    h1=tanh(w.v), a_v=E1[b1 h1], z_v=b2^T M a_v,
    H_v=tanh(z_v), d_v=E2[b2 c sech^2(z_v)],
    Q_v=b1^T M^T d_v, f_v=E2[c H_v].

The full physical gradient is

    g_v=grad_X f_v=(sech^2(w.v) Q_v v, H_v, d_v a_v^T). (2)

For three inputs define

    r_i=(f_i-1)/sqrt(3), L=|r|^2,
    J h=(<g_i,h>/sqrt(3))_i, K=J J*,
    X_dot=-2J*r, r_dot=-2Kr.                            (3)

All state norms and adjoints below use the displayed physical metric.
The target is all-time decay on freely perturbed triples in (S^2)^3,
using a potential evaluated from their present state and fixed inputs.
No unknown endpoint is supplied to a potential or to the dynamics.

## 2. Spatial derivatives and where mixed input Hessians occur

First hold the current full state fixed. For a tangent vector epsilon at v,
the first directional derivatives are

    a_v'[epsilon]=E1[b1 tanh'(w.v)(w.epsilon)],
    z_v'[epsilon]=b2^T M a_v'[epsilon],
    f_v'[epsilon]=E2[c tanh'(z_v) z_v'[epsilon]].          (4)

Use the sphere chart v(epsilon)=(v+epsilon)/|v+epsilon| for epsilon.v=0.
Its second derivative at zero is -(epsilon.delta)v. Therefore the
intrinsic second derivatives are

    a_v''[epsilon,delta]
      =E1[b1 {tanh''(w.v)(w.epsilon)(w.delta)
                    -(epsilon.delta)tanh'(w.v)(w.v)}],
    z_v''[epsilon,delta]=b2^T M a_v''[epsilon,delta],
    f_v''[epsilon,delta]
      =E2[c {tanh''(z_v) z_v'[epsilon]z_v'[delta]
                            +tanh'(z_v)z_v''[epsilon,delta]}]. (5)

The radial correction is necessary; using an unconstrained Euclidean
input Hessian would describe a different perturbation. At any fixed
finite time w=G plus a bounded increment, c is bounded and M is finite.
All displayed derivatives are dominated by a constant times 1+|G|^2;
Gaussian moments justify the differentiations under the expectations.

It is useful to differentiate the entire gradient, rather than only its
readout block. With s_v=tanh'(w.v),

    d_v'[epsilon]=E2[b2 c tanh''(z_v)z_v'[epsilon]],
    Q_v'[epsilon]=b1^T M^T d_v'[epsilon],

    (g_v'[epsilon])_c=tanh'(z_v)z_v'[epsilon],
    (g_v'[epsilon])_M=d_v'[epsilon]a_v^T+d_v(a_v'[epsilon])^T,
    (g_v'[epsilon])_w
      =tanh''(w.v)(w.epsilon)Q_v v
                      +s_v Q_v'[epsilon]v+s_v Q_v epsilon. (6)

In particular, for distinct input indices i,j, the exact mixed derivative
of the corresponding full tangent entry is

    D_i D_j K_ij[epsilon_i,delta_j]
        =<g_i'[epsilon_i],g_j'[delta_j]>/3.               (7)

Every other entry has the corresponding dependence on its own two input
slots; diagonal second derivatives also contain the second derivative
of g_i. Formula (7) retains the derivatives of the actual backward action.
Its sign is not determined by a scalar input inner product.

By contrast, the fixed-state loss is a sum of three separate terms, so

    D_i D_j L=0 for i!=j,                                (8)
    D_i^2 L[epsilon,delta]
       =(2/3){f_i'[epsilon]f_i'[delta]+(f_i-1)f_i''[epsilon,delta]}.

There is no contradiction between (7) and (8). Inter-input curvature in
the trained response comes from the shared evolving state and from its
tangent geometry, not a cross term in the fixed-state loss itself.

For example, let H_i^0 denote the initialized upper fields and
C_ij=<H_i^0,H_j^0>. The exact original-initialization physical flow gives

    f_i(t)=(2t/3) sum_j C_ij+O(t^2).                    (9)

Indeed c_dot(0)=2 sum_j H_j^0/3 and both hidden velocities vanish at
initialization. For i!=j, differentiating the leading coefficient with
respect to the two input slots gives

    D_i D_j f_i(t)[epsilon_i,delta_j]
       =(2t/3)<(H_i^0)'[epsilon_i],(H_j^0)'[delta_j]>+O(t^2). (10)

This is an exact short-time jet of the fully trained flow. It does not
replace later hidden motion by a frozen kernel.

For completeness, write its vector field as V(X,p), where p denotes the
six local sphere coordinates of the data. The finite-horizon first and
mixed second responses satisfy

    (X_alpha)_dot=V_X X_alpha+V_alpha,
    (X_alpha,beta)_dot=V_X X_alpha,beta
       +V_XX[X_alpha,X_beta]+V_Xalpha X_beta
       +V_Xbeta X_alpha+V_alpha,beta,                    (11)
    X_alpha(0)=X_alpha,beta(0)=0.

If alpha and beta vary different examples, V_alpha,beta=0 at fixed X,
because the physical vector field is a sum over individual examples.
The other three second-response sources generally remain. Thus dropping
mixed response because the direct source vanishes would be incorrect.
These are directional response equations along the actual characteristic
flow. They do not assert unrestricted C2 Nemytskii calculus on an L2 ball.
One may justify them by difference quotients on a fixed finite interval:
the first row response is bounded pointwise by C_T(1+|G|), the second by
C_T(1+|G|^2), and readout/matrix responses have bounded coefficients.
Subtract the integral equations, use bounded gate derivatives and these
Gaussian moment bounds, and apply the scalar integrating-factor estimate.
Dominated convergence identifies the quotient limits and (11).

## 3. The complete inverse-correction second jet

On K>0 let A=K^(-1) and E=r^T A r. The minimum physical squared norm of
a linear correction h satisfying Jh=-r is E: the minimizer is
-J*K^(-1)r, and every other correction differs by an orthogonal vector
in ker J. This is a present-state linear correction cost.

For any twice differentiable scalar perturbation, primes denoting its
derivatives at zero, differentiation of AK=I gives

    A'=-A K' A,
    A''=2A K' A K' A-A K'' A.

Hence the full second jet is

    E'=2(r')^T A r-r^T A K' A r,
    E''=2(r'')^T A r+2(r')^T A r'
       -4(r')^T A K' A r
       +2r^T A K' A K' A r-r^T A K'' A r.               (12)

For two distinct perturbation directions alpha,beta the polarized form is

    E_alpha,beta=2r_alpha^T A r_beta+2r_alpha,beta^T A r
       -2r_alpha^T A K_beta A r-2r_beta^T A K_alpha A r
       +r^T A(K_alpha A K_beta+K_beta A K_alpha-K_alpha,beta)A r. (13)

The moving-metric terms cannot be dropped away from a fitted state.

To display the geometry at a symmetric reference, let n=(1,1,1)/sqrt(3), and
let V be a 3-by-2 orthonormal frame of n-perp. Define

    F=(f1+f2+f3)/3, e=1-F, zeta=V^T r,
    k=n^TKn, b=V^TKn, H=V^TKV.

At a symmetric state K=k nn^T+nu(I-nn^T), b=zeta=0, and k>=C0>0
along the supplied auxiliary curve. Block elimination gives exactly

    E=e^2/k+(zeta+e b/k)^T(H-bb^T/k)^(-1)(zeta+e b/k).  (14)

If nu>0 at the reference, the second derivative along a perturbation is

    E''=(e^2/k)''+(2/nu)|zeta'+e b'/k|^2,              (15)
    (e^2/k)''=(2(e')^2+2e e'')/k-4e e'k'/k^2
                    -e^2 k''/k^2+2e^2(k')^2/k^3.

This follows because the transverse vector in (14) vanishes at zero;
derivatives of its inverse metric therefore first enter at cubic order.
The e,k in its first term still carry their full variations. At a fitted
reference e=0, (15) reduces to

    E''=2(e')^2/k+(2/nu)|zeta'|^2.                    (16)

Thus the mean/transverse coupling square matters during learning, but its
leading cross term vanishes at a regular fitted reference. This does not
make the trained input response diagonal: e' and zeta' already contain
the common-state response (11).

If nu=0, neither (15) nor a uniform cubic remainder follows. For example,
the elementary family K=diag(k,epsilon^2,1),
r=(-e,epsilon,0) has E=e^2/k+1 for epsilon!=0, although its transverse
residual tends to zero. This is an inverse-metric obstruction, not an
example asserted to be reached by the closure.

## 4. A genuine trained Hessian effect at the start of the scalar curve

This subsection uses the symmetric auxiliary curve X_s=grad F supplied
by the candidate. Write h=(w,M), H_i=H_i(h), U=(H1+H2+H3)/3, and let
B=D_h U, viewed as a bounded linear map from hidden variations to upper
L2 along these smooth characteristic variations. Then

    c_s=U, h_s=B*c,
    c(0)=0, h_s(0)=0, c_s(0)=U0, h_ss(0)=B0*U0.       (17)

For a unit z in 1-perp put

    H_z=sum_i z_i H_i/sqrt(3), B_z=D_h H_z.

The mean and transverse tangent eigenvalues are

    k=||U||^2+||B*c||^2,
    nu=||H_z||^2+||B_z*c||^2.                          (18)

Permutation equivariance makes the second expression independent of the
chosen unit transverse vector. Differentiate (18), using (17). One obtains

    k_s(0)=nu_s(0)=0,
    k_ss(0)=4||B0*U0||^2>=0,                          (19)
    nu_ss(0)=2||B_z,0*U0||^2
                  +2<H_z,0,B_z,0 B0*U0>.             (20)

For example the first term ||U||^2 contributes
2<U0,B0 B0*U0>=2||B0*U0||^2, and differentiating ||B*c||^2
contributes the other identical term. The same calculation for H_z
gives (20). The second summand in (20) measures the change of the
transverse feature under the actual hidden acceleration. It has no
sign fixed by a squared norm or by the scalar noncollapse theorem.
No assertion that it is negative for an actual rho is made here.

Consequently a nonnegative initial improvement of mean conditioning is
not itself a proof of transverse protection. This is a specific missing
term, not just a generic warning about nonlinear Hessians. Both hidden
blocks and the trained transpose occur inside B and B_z.

## 5. Every possible symmetric transverse rank loss is a double collapse

The following statement covers every admitted (a,b), including rho=-1/2.
It does not use linear independence of the three input vectors.

**Proposition.** At a finite point of the symmetric auxiliary curve with
F>0, nu=0 if and only if

1. all three upper preactivation coefficient vectors M a_i coincide;
2. their then-common backward vector d_i is zero.

Moreover, every such zero of nu is an isolated quadratic contact:

    nu(s0)=0 implies nu_s(s0)=0 and nu_ss(s0)>0.         (21)

**Proof of the characterization.** Permutation symmetry gives equal
gradient norms and

    nu=||g_i-g_j||^2/6 for every i!=j.                  (22)

If nu=0, the readout components imply H_i=H_j almost surely. Tanh is
injective, so b2^T M(a_i-a_j)=0 almost surely. The three active upper
features have a positive-definite Gram; hence M a_i=M a_j. The constant
coordinate is inactive by the initialized sign symmetry. Write the common
active vector as zbar. It is permutation invariant, so zbar is a multiple
of (1,1,1). The common H and invariant c then make d_i=d a multiple of
the same vector. The vector zbar is nonzero: otherwise H=0 and F=0.

The row components of g_i=g_j give

    tanh'(w.v_i)Q_i v_i=tanh'(w.v_j)Q_j v_j almost surely.

The two constant vectors v_i,v_j are linearly independent. Indeed equality
or antipodality would force a=b or violate a^2+2b^2=1, as checked in the
candidate. Both scalar coefficients must therefore vanish. Every tanh'
is strictly positive at a finite argument, giving Q_i=0. Linear
independence of the active lower features implies M^T d=0. For clarity,
that independence follows by conditioning a linear relation on G: the
independent conditional reverse noises have positive conditional
variances and remove the k coefficients; independent tanh G_j remove
the remaining h coefficients. Cholesky normalization is invertible.

Since zbar=M a_i is a nonzero parallel vector, M^T 1 is nonzero. The
parallel vector d with M^T d=0 must consequently be zero. Conversely,
common H and d=0 make all hidden gradient blocks zero and all readout
gradient blocks identical, proving nu=0. This proves the equivalence.

**Proof of quadratic contact.** At such a point all hidden velocities in
the auxiliary flow vanish and c_s=H. Thus a_i,s=0, M_s=0 and z_i,s=0.
Differentiating the backward vector yields a common vector

    d_i,s=d'=E2[b2 H tanh'(z)], z=b2^T zbar.             (23)

Its pairing with zbar is

    zbar^T d'=E2[z tanh(z)sech^2(z)]>0.                (24)

The integrand is nonnegative and is positive wherever z!=0; nonzero
zbar and the positive density of the upper marks give such a set of
positive measure. Hence M^T d' is nonzero, since its pairing with a_i
is (24). The lower feature independence gives
Q'=b1^T M^T d' nonzero in lower L2.

The derivative of the difference of row gradients at s0 is

    Q'{tanh'(w.v_i)v_i-tanh'(w.v_j)v_j}.                (25)

The vector in braces cannot vanish because v_i,v_j are nonparallel and
both gates are positive. Thus (25) is nonzero on a set of positive
measure. If G_ij=g_i-g_j, then G_ij(s0)=0 but G_ij,s(s0)!=0. Differentiating
(22) gives nu_s=0 and nu_ss=||G_ij,s||^2/3>0. Continuity of this second
derivative yields nu(s)>=c(s-s0)^2 near s0 for some c>0, proving isolation.
All quantities are smooth in auxiliary time in the bounded-increment
characteristic space, so the derivatives used here exist. End of proof.

At s=0, nu>0 by the supplied exact initialization-rank proof. Therefore
there are at most finitely many transverse rank-loss points on the compact
segment from initialization through its fitting endpoint: an infinite
sequence would accumulate, and its limiting zero would contradict the
local isolation just proved. The auxiliary curve exists beyond the endpoint,
so an endpoint zero also has the same two-sided local structure.

This result supplies a sharper obstruction than loss of the input Gram.
The coplanar boundary rho=-1/2 is not automatically singular for the full
tangent. Any actual rank loss requires simultaneous upper-feature collapse
and reverse-response cancellation. What remains unproved is that one of
these finitely many possible contacts cannot occur exactly at F=1.

## 6. Endpoint regularity suffices for a free all-time neighborhood

The existing nearcoincident proof protected the full tangent Gram along a
whole auxiliary segment. The next theorem requires less. Its hypothesis
is geometric at the already-proved symmetric endpoint, not a proposed
moving-metric differential inequality.

**Theorem.** Fix any admitted symmetric triple and its initialized fitting
endpoint X_*. If nu_*>0, then there is a free neighborhood of that triple
in (S^2)^3, and lambda>0 uniform in that neighborhood, on which the
original present-state potential

    Phi=L W,
    W=1+C0(1+q_c)/(C0+F^2),
    q_c=E2[c^2], F=(f1+f2+f3)/3,
    C0=E2[(H1^0+H2^0+H3^0)^2]/9                       (26)

satisfies Phi_dot<=-lambda Phi, L<=Phi, and Phi(0)=2 for all physical
times. Every such initialized flow has a fitting strong state limit.
Here C0 is recomputed from the actual perturbed inputs at initialization.

**Proof.** The symmetric result gives k_*>=C0>0. Hence nu_*>0 is exactly
positive definiteness of K_*; let mu be its smallest eigenvalue. The
field estimates in the supplied open-family proof establish continuity
and locally uniform Lipschitz bounds of the gradients and K in the physical
Hilbert state and unit inputs. Choose a state radius R and a data radius
delta0 such that in the radius-R ball around X_* for those inputs,

    K>=k I, k=mu/2, ||K||op<=Lambda,
    ||grad_X W||<=B, C0>=C0_seed/2.                    (27)

The last bounds hold because the ball has bounded c,M, the features are
bounded, and the denominator of W is at least its positive C0. In particular

    grad W=2C0(0,c,0)/(C0+F^2)
           -2C0 F(1+q_c)grad F/(C0+F^2)^2.

In the ball, the exact energy identity and (3) give

    L_dot=-4r^TKr, ||X_dot||^2=4r^TKr,
    -d(sqrt(L))/dt>=sqrt(k)||X_dot||                  (28)

where L>0. Zero loss gives a stationary solution, so creates no exception.
Also, differentiating every factor of Phi gives

    Phi_dot=W L_dot+L<grad W,X_dot>
       <=-4k Phi+2B sqrt(Lambda)L^(3/2).               (29)

When sqrt(L)<=k/(B sqrt(Lambda)), equation (29) gives
Phi_dot<=-2k Phi; if B=0 the smallness condition is unnecessary.

The seed converges to X_* and has L tending to zero. Select finite T such
that its distance to X_* is less than R/4 and its loss is strictly below
both the threshold in (29) and a value with sqrt(L/k)<R/8. Finite-horizon
dependence on the six data coordinates allows delta0 to be reduced so all
perturbed solutions at T are within R/2 of X_* and satisfy the same
strict small-loss bounds, with sqrt(L(T)/k)<R/4.

As long as a perturbed solution remains in the ball after T, (28) bounds
its entire subsequent displacement by sqrt(L(T)/k)<R/4. It therefore
cannot leave the radius-R ball. Global finite-time existence excludes any
other continuation failure. Loss decreases, so (29)'s smallness condition
persists. This establishes the tail decay and finite length without any
claim about earlier full-tangent coercivity.

On the fixed compact interval [0,T], the symmetric seed satisfies
Phi_dot/Phi<=-4C0_seed. Its loss is strictly positive at finite times, so
Phi has a positive minimum there. The exact derivative of (26) is
continuous in state and data. Uniform finite-horizon dependence therefore
permits a further reduction of delta for which

    Phi_dot/Phi<=-2C0_seed on [0,T].

Combining with the tail proves the claim with
lambda=min(2C0_seed,2k)>0. In particular L(t)<=2 exp(-lambda t).
The finite-length estimate after T implies a strong Hilbert endpoint;
continuity of the predictions and vanishing loss show that it fits.
The identical initialized-mark coupling supplies convergence of the saved
joint laws in W2. The endpoint X_* is used to prove trapping, but neither
it nor T occurs in (26) or the actual evolution. End of proof.

This theorem applies to any broad-family seed whose endpoint is regular,
even if K has isolated zero eigenvalues earlier. It strictly separates
the all-time perturbation issue from an unnecessary demand for a positive
minimum of K along the entire reference path. Sections 5 and 6 reduce
the missing broad-family fact to exclusion of the specified double
collapse at the fitting level F=1.

## 7. What the endpoint Hessian does and does not determine

At a fitted state r=0, the physical state Hessian of loss is

    Hess_X L=2J*J.                                    (30)

There is no residual-weighted network Hessian term. If A_data maps input
tangent vectors epsilon to (f_i'[epsilon_i]/sqrt(3))_i, then the quadratic
joint state/input expansion is

    L(X_*+h,p+epsilon)
        =||J h+A_data epsilon||^2+o(||h||^2+|epsilon|^2). (31)

The sphere charts are understood in this expression. It follows directly
from differentiability of r and r(X_*,p)=0; no unrestricted C2 assumption
on the underlying L2 Nemytskii map is needed. The Hessian is twice the
Gram of the combined map [J,A_data]. At a symmetric regular endpoint its
nonzero state eigenvalues are 2k_*,2nu_*,2nu_*; state directions in ker J
are neutral to quadratic order.

Minimizing the quadratic expression over h makes it zero when K>0. The
minimum-norm compensating displacement is

    h_normal=-J*K^(-1) A_data epsilon,
    ||h_normal||^2=epsilon^T A_data^* K^(-1) A_data epsilon. (32)

Consequently the reduced loss Hessian after allowing the state to refit
is zero. The nonzero quantity in (32) is the normal displacement cost,
not a reduced loss curvature and not a selection rule for the actual
trained endpoint. Tangential endpoint motion in ker J is undetermined
by (30)--(32). If an actual endpoint derivative exists, its normal
component must satisfy (32); existence or all-time differentiability of
that selected endpoint map is not inferred just from finite-horizon jets.

A local branch of nearby fitting states itself can be constructed in a
finite-dimensional normal slice without such an inference. In the slice
X_*+J*K^(-1)z, the derivative in z of the residual map is the identity
at z=0. The residual minus z has derivative as small as desired on a
sufficiently small slice/data neighborhood, by continuity. Thus the map
z -> z-r(X_*+J*K^(-1)z,p') is a contraction on a small ball after reducing
the input neighborhood. Its fixed point fits p'. All these slice
directions are bounded characteristic variations, so the required local
derivatives are valid. This supplies representability near a regular
endpoint, not identification with the trajectory-selected fitting state.

## 8. Gluing across correlation branches and the remaining obstruction

There is a simple valid gluing rule when local potentials are proved.
Suppose finitely many neighborhoods U_alpha of the fixed data p have
present-state potentials Phi_alpha with L<=Phi_alpha and

    D_X Phi_alpha V_p<=-lambda_alpha Phi_alpha

on all initialized trajectories belonging to U_alpha. Choose nonnegative
smooth weights chi_alpha(p), supported inside those neighborhoods and
summing to one. Because the data do not move during training,

    Phi=sum_alpha chi_alpha(p)Phi_alpha,
    Phi_dot<=-min_alpha(lambda_alpha)Phi, L<=Phi.        (33)

For a compact covered family, finitely many balls inside the U_alpha
suffice; explicit smooth nonnegative bump functions on the finite
sphere-coordinate charts, divided by their positive sum, construct
these weights. They depend on prescribed inputs, not an endpoint or a
training clock. If all local proofs use (26), no gluing of formulas is
needed at all: the same formula already works on the union, with local
rates and a finite minimum on a compact subfamily.

This does not prove that the whole rho family is covered. Section 6
covers exactly the seeds for which endpoint regularity has been proved,
and section 5 identifies the unresolved exceptional geometry. Nor can a
state-dependent partition be substituted silently: it would add
sum_alpha <grad_X chi_alpha,X_dot>Phi_alpha with no controlled sign.

At a double-collapse fitting endpoint, nu_*=0, the transverse part of
(30) is zero. Section 5 implies nu(s) is quadratically small in s-s_*
near that endpoint. The scalar reference residual obeys
1-F(s)=k_*(s_*-s)+o(|s-s_*|), with k_*>0; physical time approaches s_*
exponentially. Therefore transverse linear damping along that reference
has an integrable tail:

    integral_T^infinity nu(s(t)) dt < infinity.        (34)

For the homogeneous transverse residual equation zeta_dot=-2nu(t)zeta,
the factor exp(-2 integral_T^t nu) consequently tends to a strictly
positive number. The reference's direct output damping therefore does
not remove that homogeneous disagreement. A complete coupled first
variation also has the source 2e b', as seen by differentiating (3);
that source has not been discarded or bounded in an all-time theorem
here. This is the precise second-order obstruction to
using the reference endpoint as a uniformly normally coercive anchor.
It is not a proof that actual perturbed nonlinear trajectories fail to
fit, or that no different potential can work after further adaptation.

The initialized upper Gram loses transverse rank as rho approaches 1,
so a uniform positive full-Gram lower bound over the entire closed-to-
coincidence family is already impossible at initialization. This does
not rule out geometry-dependent rates, or a uniform rate for a narrower
observable along specially constrained initialized residuals.

## 9. Claim ledger and bottleneck

| Claim | Status | Boundary |
|---|---|---|
| Sphere Hessians, full-gradient mixed kernels, and actual finite-horizon response equations | Exact identities | No uniform all-time perturbation expansion asserted |
| Inverse-correction second jet and Schur square | Proved on K>0 | Singular limits need separate analysis |
| Mean and transverse auxiliary curvature formulas | Proved | The sign of the transverse curvature term is not resolved |
| Any symmetric rank loss is simultaneous upper collapse and zero backward response | Proved for every admitted (a,b), F>0 | Does not prove that the collapse occurs |
| Such rank losses are isolated quadratic contacts | Proved | Does not exclude a contact at F=1 |
| A regular symmetric endpoint gives a free all-time potential neighborhood | Proved conditional on nu_*>0 | The condition is established by supplied work near coincidence only |
| Data-dependent gluing of already certified local potentials | Proved | Supplies no missing coverage or uniform noncompact rate |
| Full broad-rho free-perturbation theorem | Open | Requires exclusion or treatment of double collapse at the fitting level |

The highest-leverage remaining task is to prove that a symmetric auxiliary
curve cannot satisfy all three conditions

    F=1, M a1=M a2=M a3, d1=d2=d3=0,

for the prescribed initialized coefficients and every permitted (a,b),
or to develop a separate nonlinear tail mechanism at such a state. Initial
rank, the scalar q_c/F^2 monotonicity, and a positive mean Hessian alone
do not close this obligation. No endpoint-oracle coefficient, frozen
feature replacement, experiment, or unproved analytic-zero-set argument
has been used to claim otherwise.
