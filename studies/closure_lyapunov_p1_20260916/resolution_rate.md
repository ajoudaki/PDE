# Sharp quadratic conditioning rate for the nearby symmetric seeds

2026-09-16. Scoped analytical extension; internal research only. No
experiments, no promotion, and no change to either frozen input. Scientific
inputs are `three_coordinate_candidate.md`, `resolution_open_family.md`,
`docs/README.md`, `docs/NOTATION.md`, the canonical characteristic equations
and well-posedness statements in `docs/global_nonlinear.md` C.4.7.9 and
C.4.7.10.C.1, and the complete `docs/observable_p1.md`.

## Statement and proof structure

Retain exactly the d=3 p=1 population closure, initialized correlated marks,
ridge eta=1/4096, evolving full matrix and actual transpose, and physical
population-L2/Frobenius metric of the two frozen inputs. Absorb the labels
(1,1,-1), so all three labels are +1 and the unit input directions are

    v_i(e)=(1+e e_i)/q_e,  q_e=sqrt(3+2e+e^2),  i=1,2,3.

Here `1=(1,1,1)` and `e_i` are coordinate vectors. Let X_e(s) solve the
exact auxiliary equation X_s=grad F_e from (G,0,D), where

    F_e=(f(v_1(e))+f(v_2(e))+f(v_3(e)))/3.

The full normalized tangent matrix is

    K_e(s)[i,j]=(1/3)<grad f(v_i(e)),grad f(v_j(e))>.

The inner product includes every physical gradient block. Put

    v_*=(1,1,1)/sqrt(3),  p_*=kappa(1/sqrt(3)),
    C_*=E2[tanh^2(p_*(Z_1+Z_2+Z_3))]>0,  S_*=2/C_*,
    mu_e=min_{0<=s<=S_*} lambda_min(K_e(s)).

There exist e_0>0 and finite constants c_->0 and c_+>0, independent of e,
such that

    c_- e^2 <= mu_e <= c_+ e^2,      0<e<e_0.                 (R1)

Thus the proposed lower rate holds, and its exponent is sharp for this
minimum over the fixed auxiliary interval. All constants below are specified
by initialized expectations, bounds, and one declared coincident reference
curve. No analytic dependence on e in row L-infinity is used.

The proof separates a fixed initial interval from its fixed positive-time
complement. On the initial interval, exact coefficient differences retain
an order-e readout contrast. On the complement, the first-layer gradient
has uniformly positive scalar strength, and the input Gram supplies e^2.

## 1. Uniform bounds and exact coefficient differences

Use the fields of the frozen inputs:

    a_i=E1[b1 tanh(w.v_i)],  z_i=b2^T M a_i,  H_i=tanh z_i,
    d_i=E2[b2 c sech^2 z_i], Q_i=b1^T M^T d_i,
    g_i=sech^2(w.v_i).

The feature maps z -> b_l^T z and their adjoints are contractions, and
B_l=ess sup |b_l| is finite. Set S=S_*, d_0=||D||op, and define the
following constants, each independent of e in [0,1]:

    Mbar=d_0+S^2/2,
    Wbar=sqrt(3)+B1(d_0 S^2/2+S^4/8),
    Vbar=B1 Mbar,
    Abar=Vbar(2 Wbar+1),
    Zbar=(1+Mbar Abar)/2.

The exact auxiliary bounds from the candidate give, for 0<=s<=S,

    ||c||infinity<=s,  ||M-D||op<=s^2/2,  ||M||op<=Mbar,
    ||w||2<=Wbar,  ||w_s||infinity<=Vbar s.                  (R2)

Fix i!=j and write delta=|v_i-v_j|=sqrt(2)e/q_e and
Delta a=a_i-a_j. Differentiation under the expectation is justified by
bounded b1 and g_i and the bounded row speed in (R2). It gives the exact
identity

    (Delta a)_s=E1[b1(g_i w_s.v_i-g_j w_s.v_j)].              (R3)

Decompose its scalar integrand as

    (g_i-g_j)(w_s.v_i)+g_j w_s.(v_i-v_j).

The gate bound |sech^2 x-sech^2 y|<=2|x-y|, contraction of the
feature adjoint, and (R2) yield

    |(Delta a)_s|
      <=||w_s||infinity (2||w||2+1) delta
      <=Abar delta s.

This uses the finite second moment of w, not a supremum bound on G.v_i.
Integrating and using the Gaussian covariance E1[GG^T]=I gives

    |Delta a(s)-Delta a(0)|<=(Abar/2) delta s^2,
    |Delta a(0)|<=||G.(v_i-v_j)||2=delta.                    (R4)

For Delta z=z_i-z_j the feature-map contraction then gives

    ||Delta z(s)-Delta z(0)||2
      <=|(M(s)-D)Delta a(0)+M(s)(Delta a(s)-Delta a(0))|
      <=Zbar delta s^2.                                    (R5)

All L2 norms in (R4) are lower-population norms and those in (R5) are
upper-population norms. This is the needed O(e s^2) statement for the
actual coefficient contrast. No differentiation with respect to e, and
no input continuity in the row L-infinity topology, enters the argument.

## 2. Readout coercivity on a fixed initial interval

Write a_e=(1+e)/q_e and b_e=1/q_e. For 0<=e<=1 both belong to the
compact interval

    I=[1/sqrt(6),2/sqrt(6)] subset (-1,1).

The candidate's exact initialized formula and strict continuous derivative
of kappa give constants

    k_-=min_I kappa'>0,  k_+=max_I kappa'<infinity.

The strictness and continuity here follow from the bounded Gaussian
expectation in candidate equation (30); they are not empirical bounds.
Let theta_e=kappa(a_e)-kappa(b_e). Then

    k_- e/q_e <= theta_e <= k_+ e/q_e,
    z_i(0)-z_j(0)=theta_e(Z_i-Z_j).

Since Z_i are independent, centered, and E2[Z_i^2]=tau,

    ||z_i(0)-z_j(0)||2=sqrt(2 tau) theta_e
                         >=k_- sqrt(tau) delta.             (R6)

Choose the fixed positive time

    s_0=min{S/2,1,sqrt(k_- sqrt(tau)/(2 Zbar))}>0.

Combining (R5)--(R6) gives, for 0<=s<=s_0,

    ||z_i(s)-z_j(s)||2 >=(k_- sqrt(tau)/2) delta.             (R7)

Also |a_i|<=1, so |z_i|<=B2 Mbar almost surely. Define the strictly
positive fixed number g_*=sech^2(B2 Mbar). The mean-value formula for
tanh on [-B2 Mbar,B2 Mbar] gives the pointwise bound

    |H_i-H_j|>=g_* |z_i-z_j|.

Permutation equivariance of the normalized dictionary and uniqueness of
X_e imply that the readout Gram

    K_e^c[i,j]=(1/3)E2[H_i H_j]

has one parallel and two equal transverse eigenvalues. The eigenvalue on
the subspace perpendicular to (1,1,1) is exactly

    lambda_perp(K_e^c)=(1/6)||H_i-H_j||2^2
       >=g_*^2 k_-^2 tau delta^2/24
       =g_*^2 k_-^2 tau e^2/(12 q_e^2)
       >=g_*^2 k_-^2 tau e^2/72.                           (R8)

The parallel eigenvalue is exactly C_e(s)=E2[((H_1+H_2+H_3)/3)^2].
The candidate's normalized-readout argument proves
C_e(s)>=C_e(0) throughout the auxiliary curve, including past fitting.
Initialized continuity and C_e(0)->C_* allow e_0<=1 to be reduced so that
C_e(0)>=C_*/2 for 0<e<e_0. Since e^2<=1, (R8) implies

    K_e(s)>=K_e^c(s)>=c_early e^2 I,   0<=s<=s_0,
    c_early=min{C_*/2,g_*^2 k_-^2 tau/72}>0.                 (R9)

This controls all tangent directions during the interval where the row
gradient is still becoming nonzero.

## 3. First-layer coercivity on the remaining fixed interval

At e=0 let w_0,M_0,c_0 be the coincident reference curve and define

    R_0(s)=E1[sech^4(w_0.v_*) Q_0(s)^2].

Sections 3--4 of `resolution_open_family.md` prove the precise facts
needed here: finite auxiliary-time Hilbert continuity in the input data,
and R_0(s)>0 at every s>0. For clarity, the positivity has the following
complete mechanism. At coincidence the upper preactivation is
p(s)(Z_1+Z_2+Z_3), with p(0)=p_*>0, and

    c_0(s)=integral_0^s tanh(p(r)(Z_1+Z_2+Z_3)) dr.

While p>0, its reverse coefficient is d_ref(s)=h(s)(1,1,1) on the active
coordinates. With S_Z=Z_1+Z_2+Z_3 and RZ=sqrt(tau+eta),

    h(s)=E2[S_Z c_0(s) sech^2(p(s)S_Z)]/(3 RZ)>0  (s>0).

The inequality holds because c_0(s) has the sign of S_Z and its law is
nondegenerate. Put B=E1[b1 b1^T sech^4(w_0.v_*)], which is positive
semidefinite. The exact single-input equations imply

    (M_0 a_0)_s=(|a_0|^2 I+M_0 B M_0^T)d_ref,
    3 RZ p_s=h(s)(3|a_0|^2+1^T M_0 B M_0^T 1)>=0.

Here the displayed matrices and vectors have their active dimensions.
A first zero of p is therefore impossible. Moreover
M_0 a_0=RZ p(s)(1,1,1) implies M_0^T(1,1,1)!=0. The six active lower
features are linearly independent: conditioning on G first eliminates
the three k coefficients by their independent positive conditional
variances, and then independence of tanh(G_j) eliminates the h
coefficients. Hence Q_0 is nonzero in L2. Multiplication by the strictly
positive finite-argument gate proves R_0(s)>0.

The constant entries of a and d, and the constant row and column of M,
are zero along these curves by the exact simultaneous-sign symmetry of
the initialization and vector field. The frozen feature columns themselves
still retain their nonzero constant entries.

Continuity and compactness now give

    r_0=min_{s_0<=s<=S} R_0(s)>0.                            (R10)

Here compactness concerns one fixed closed real interval with s_0>0.
It does not assume a positive infimum as s decreases to zero.

To verify the uniform transfer rather than just pointwise continuity,
put

    R_{e,i}(s)=E1[sech^4(w_e.v_i(e)) Q_{e,i}(s)^2].

On [0,S], the input-data dependence proved in the frozen open-family
input gives uniformly

    ||w_e-w_0||2 ->0,  ||Q_{e,i}-Q_0||infinity ->0.

The second assertion follows because Q is the bounded b1 pairing of
finite coefficients M^T d, which converge uniformly. The input mismatch
is also controlled in L2:

    ||w_e.v_i(e)-w_0.v_*||2
      <=||w_e-w_0||2+||w_0||2 |v_i(e)-v_*| ->0.

All Q are uniformly bounded on this interval. Since sech^4 is bounded
by one and is Lipschitz with constant at most four, these estimates imply
uniform convergence R_{e,i}->R_0. Explicitly, with a common bound Qbar,

    |R_{e,i}-R_0|
      <=2 Qbar ||Q_{e,i}-Q_0||2
        +4 Qbar^2 ||w_e.v_i(e)-w_0.v_*||1 ->0.

Reducing e_0>0 once more therefore yields

    min_i R_{e,i}(s)>=r_0/2,   s_0<=s<=S,  0<e<e_0.         (R11)

For every z in R^3 the exact first-layer gradient and the input Gram give

    3 z^T K_e^w(s) z
      =E1 |sum_i z_i sech^2(w_e.v_i)Q_{e,i} v_i|^2
      >=lambda_min([v_i.v_j]) sum_i z_i^2 R_{e,i}(s).

The direction matrix is (e I+11^T)/q_e, so the input Gram eigenvalues are
e^2/q_e^2, e^2/q_e^2, and (e+3)^2/q_e^2. Thus, using q_e^2<=6,

    K_e(s)>=K_e^w(s)>=(r_0/36)e^2 I,
                   s_0<=s<=S,  0<e<e_0.                   (R12)

Combining (R9) and (R12) proves the lower bound in (R1), with

    c_-=min{c_early,r_0/36}>0.

## 4. Matching upper bound and exact scope

At s=0 the readout c vanishes, so the row and matrix tangent blocks
vanish. Hence K_e(0)=K_e^c(0). The upper Lipschitz bound for tanh and
the transverse eigenvalue identity give

    mu_e<=lambda_perp(K_e(0))
      =(1/6)||H_i(0)-H_j(0)||2^2
      <=tau theta_e^2/3
      <=(tau k_+^2/9)e^2.                                 (R13)

Thus one may take c_+=tau k_+^2/9. The exponent two cannot be improved
to a larger lower scale uniformly in e for the declared minimum including
initialization. In particular, an e-independent positive lower bound is
false at this coalescing limit.

The open-family theorem may consequently choose its full tangent lower
bound k(e)=mu_e/2 with k(e)>=(c_-/2)e^2, after the permitted reduction
of its data neighborhood. Its mixed-potential rate there is
lambda(e)=min{2 C_e(0),mu_e}, so for the same small e it can be chosen
at least min{C_*,c_-}e^2. This does not quantify the neighborhood radius
delta(e), remove its possible shrinkage, or imply a generic arbitrary-input
theorem. The symmetric seed's scalar residual already has an order-one
decay estimate; (R1) concerns the weaker full three-direction conditioning
needed for nonsymmetric perturbations.

The constants above are positive analytic specifications, not numerical
calibrations. The late constant r_0 depends only on the explicitly declared
coincident reference over a fixed finite auxiliary interval. No experiment,
unbounded-Gaussian row L-infinity input expansion, varying long-time limit,
or assumption of upper-feature separation after s_0 is used.
