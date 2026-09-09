# Actual backpropagation primitive: no weighted-source premise

This is an exact finite-width response representation and a proved
source estimate. It is not a global response or population-limit
theorem. It improves the signed-range reduction by choosing the
time integral of the actual backpropagation variation as the range
coordinate. After the scalar arctangent cancellation, ALL remaining
non-curvature forcing is unweighted and has a width-uniform probe
bound. The signed residual/returned-response pairing remains open.

In the main proof the coefficients belong to the actual uncut canonical trajectory on
a finite feature horizon [0,S], on its established primal/operator
and bounded-readout-coordinate events. The argument works for zero
or prescribed tiny initial readout; it does not use q(0)=0.
Expectations below condition on that entire trajectory and average
only over the independent Gaussian derivative probe. No primal
inequality is differentiated with respect to initial data. The final
section extends the representation and source bound to the prescribed
continuously differentiable clipping family used in cutoff removal.

## 1. Separate the actual backpropagation variation before propagating

Use the tangent notation of ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md:
vectors have norm ||u||_n=||u||_2/sqrt(n), matrix variations have
ordinary Frobenius norm, and u tensor v=uv*/n. Write

    H=H1, D_l=diag(phi'(z_l)), C=W4,
    d=delta3=D3 C, q=W3* d, delta=delta2=D2 q,
    b=phi''(z2)q, beta=phi''(z2)/phi'(z2), |beta|<=1.

The probe varies initial W3 in the direction K=xi e_i*/sqrt(n),
where xi has ordinary standard Gaussian law. The state variation is
y=(x,A,B,c), with B the variation of the LEARNED part of W3.
Thus y(0)=0 although the total W3 variation is B+K.

Define the bounded middle-preactivation map

    T_t y=A H+W2 D1^2 x,
    R_t v=(W2* v,v tensor H,0,0).

The K=0 top variations and their backward query form bounded maps:

    zeta3_y=B H2+W3 D2 T_t y,
    d_y=D3 c+C phi''(z3) zeta3_y,
    Q_t y=B* d+W3* d_y.                                 (1)

Every coefficient multiplying a coordinate in these maps is bounded;
matrix-times-vector terms use the primal operator bounds. For example,
||B*d||_n<=||B||_F||d||_n. Hence ||Q_t||<=C_S.
Define the source quantities

    d_K=C phi''(z3) K H2,
    q_K=K* d+W3* d_K,
    f_top=(0,0,d_K tensor H2,D3 K H2).                  (2)

Let p(t) denote the ACTUAL initial-data variation of delta2(t).
The chain rule gives exactly

    p=D2[Q_t y+q_K]+b T_t y.                            (3)

Unlike the earlier curvature-only primitive, the new primitive is

    a_delta(t)=integral_0^t p(s) ds,   a_delta(0)=0.      (4)

Define a bounded state operator L0 by

    L0_t y=(
       A*delta,
       delta tensor D1^2 x,
       d_y tensor H2+d tensor D2 T_t y,
       D3 zeta3_y
    ).                                                  (5)

The complete first-variation equations are now

    y'=L0_t y+R_t p+f_top.                              (6)

Equations (1)--(6) differentiate every trained factor. In particular,
the lower A*delta and delta tensor D1^2 x terms are retained in L0.
All its norms are at most C_S independently of max|q|. The backward
vector delta occurs there only in rank-one or matrix-action terms
controlled by its normalized L2 norm.

## 2. Bounded return kernel and a purely top-layer direct response

Let U0(t,s) solve the bounded linear equation with generator L0.
The lower two components of L0 depend only on (x,A), so the fixed
subspace {(0,0,B,c)} is invariant. Therefore

    y0(t)=integral_0^t U0(t,s) f_top(s) ds

has zero lower components and satisfies T_t y0(t)=0 exactly.
The source map xi -> f_top has operator norm at most C_S/n from
ordinary Euclidean probe space to the tangent state space, because
K H2=H2_i xi/sqrt(n). Bounded propagation gives

    ||xi -> y0(t)||_op<=C_S/n,
    n E_xi||y0(t)||^2<=C_S.                             (7)

The second inequality follows from the n-dimensional probe identity
E||M xi||^2=||M||_HS^2<=n||M||_op^2.
Also, directly from (2),

    n E_xi||q_K(t)||_n^2<=C_S,                          (8)

since n E||K*d||_n^2=||d||_n^2 and
n E||K H2||_n^2=H2_i^2.

The exact primal equations give

    R_t' v=(H<delta,v>_n,v tensor H',0,0),
    H'=D1^2 W2*delta.

Thus R' is bounded. Put S_t=L0_t R_t-R_t'. For clarity it is
explicitly, with u=D1^2 W2*v and A2=T R,

    S_t v=(
       0,
       delta tensor u-v tensor H',
       d_v tensor H2+d tensor D2 A2 v,
       D3 W3 D2 A2 v
    ),
    d_v=C phi''(z3) W3 D2 A2 v.                        (9)

The cancellation of the first component uses
(v tensor H)*delta=H<v,delta>_n. Every operator in (9) is bounded.

Variation of constants in (6), followed by integration by parts
using (4), gives

    y(t)=y0(t)+R_t a_delta(t)
                   +integral_0^t U0(t,s) S_s a_delta(s) ds. (10)

Indeed partial_s[U0(t,s)R_s]=
U0(t,s)(R_s'-L0_s R_s)=-U0(t,s)S_s; the initial boundary
vanishes because a_delta(0)=0. No derivative of D1 or T is used.

Define the bounded response kernel

    N0(t,s)=T_t U0(t,s) S_s,        ||N0(t,s)||<=C_S.

Then the exact preactivation response is

    T_t y(t)=A2_t a_delta(t)
                    +integral_0^t N0(t,s)a_delta(s) ds. (11)

The direct top response contributes zero to (11).
Only the lower part of (9) contributes to N0: L0 has autonomous
lower dynamics, and T vanishes on pure-top vectors. In particular,
at equal time,

    N0(s,s)=delta_s tensor k_s-eta_s I,
    k=W2 D1^2 H, eta=<delta,k>_n.                       (12)

This is not the moving-orthogonal-range kernel N; its instantaneous
projection factor is absent. Equation (12) does not bound the
two-time kernel after multiplication by q.

## 3. Every non-curvature forcing term has a controlled probe norm

Set A_delta(t)=n E_xi||a_delta(t)||_n^2 and
Lambda(t)=n E_xi||y(t)||^2. From (7), (10), bounded R and S,
and time Cauchy--Schwarz,

    Lambda(t)<=C_S[
          1+A_delta(t)+integral_0^t A_delta(s) ds].     (13)

The complete non-curvature forcing in (3) is

    u(t)=Q_t y(t)+q_K(t).

The operator estimate for Q, (8), and (13) prove

    n E_xi||u(t)||_n^2<=C_S[
          1+A_delta(t)+integral_0^t A_delta(s) ds].     (14)

This includes BOTH the additive source and all response-dependent
linear terms. No inverse middle gate multiplies u in (14).
In particular no fourth moment of z2, nor any product of z2 with
an uncontrolled source coordinate, is assumed.

Combining (3), (4), and (11) gives the actual primitive equation

    a_delta'=D2 u+
       b[A2 a_delta+integral_0^t N0(t,s)a_delta(s) ds]. (15)

It is precisely the D2 factor on the ENTIRE u in (15) that will
remove the weighted-source premise of the previous coordinate.

## 4. Scalar cancellation with only signed response pairings left

Fix a coordinate set E in time, allowed to depend on the actual
trajectory and conditional probe covariance but not on the realized
probe. Use the exact actual scalar identity

    P_E z2'=alpha_E P_E delta+r_E.                      (16)

For example, the previously checked single-pruned construction gives
alpha_E and r_E=ghat_E+rho_E. This section needs only the identity,
not smallness or a tail premise for r_E.

Write

    h_E=P_E[(A2-alpha_E I)a_delta
                         +integral_0^t N0(t,s)a_delta(s) ds],
    c_E=D2_E^{-1}P_E a_delta.

All off-block and memory terms are retained in h_E. The scalar
chain rule gives (log D2_E)'=alpha_E b_E+beta_E r_E.
Applying this to (15) yields exactly

    c_E'=-beta_E r_E c_E+beta_E q_E h_E+P_E u.          (17)

The inverse gate has disappeared from the COMPLETE non-curvature
forcing. This does not assert that the two multiplicative terms
in (17) are bounded operators uniformly in width.

Let

    C_E(t)=n E_xi||c_E(t)||_n^2,
    U_j(t)=n E_xi c_E,j(t)^2,
    V_j(t)=n E_xi[c_E,j(t)h_E,j(t)],       j in E.

Finite width justifies differentiation and probe averaging, since
all responses are linear in the finite-dimensional Gaussian probe.
The exact signed energy is

    (1/2) C_E'=
      -<beta_E r_E,U>_n+<beta_E q_E,V>_n
                                  +n E_xi<c_E,P_E u>_n. (18)

The LAST term, unlike the prior weighted-source term, is now bounded:

    |n E_xi<c_E,P_E u>_n|
      <=C_S[1+C_E(t)+A_delta(t)
                              +integral_0^t A_delta(s) ds]. (19)

This follows from Young's inequality and the PROVED estimate (14).
If E is the entire middle layer, D2<=I implies A_delta<=C_E,
so the right side involves only C_E and its history.
For partial E the complementary part of A_delta remains explicit.

The unresolved quantity is the signed combination

    -<beta_E r_E,U>_n+<beta_E q_E,V>_n.                (20)

The earlier rare derivative/energy lemma bounds mean coordinate
primal action, not its pairing with U or V. The representation here
does not make those covariances independent or assign them a
favorable sign. Thus (20), not another weighted-source premise,
is the precise remaining resolver in this primitive coordinate.

All sets differentiated in (17)--(18) are fixed in time. A moving
exceptional support would require its own membership or weight
derivatives. The pure-top and source statements are actual response
facts, but neither (13) nor (19) estimates the still-unknown response
amplitude. No global continuation conclusion is drawn.

## 5. The same source bound for the prescribed smooth clipped family

Fix a continuously differentiable scalar clipping tau with
|tau(x)|<=|x| and |tau'(x)|<=1. These are the differentiable
clippings used in LOCAL_CUTOFF_BRIDGE.md; tau(x)=x gives the
uncut case. For this section the ACTUAL base trajectory is the
one with delta=D2 tau(q). Its forward activations and top
backward vector d=D3 C remain unchanged in definition.
The established primal estimates on a fixed feature horizon are
uniform in this prescribed clipping. No clipped coercivity
assertion is needed here: no inverse of R*R or A2 was used above.

The finite-width vector field is continuously differentiable,
so its initial-data variation obeys the chain rule. Equations
(1), (2), (5), (6), and (9)--(12) remain exact, with the actual
clipped delta in all primal coefficients. The ONLY replacements
in the primitive equation are

    b=phi''(z2)tau(q),
    u=diag(tau'(q))[Q_t y+q_K],
    p=D2 u+b T_t y.                                    (21)

For example, the derivative of the activation H2 is still D2 T y,
not a derivative of tau. The latter appears only in the backward
variation (21). Since |tau'|<=1, the proved source bound becomes

    n E_xi||u(t)||_n^2<=C_S[
          1+A_delta(t)+integral_0^t A_delta(s) ds],     (22)

with the SAME clipping-independent kind of constant.
The pure-top invariance, source scaling, bounded L0/R'/S kernels,
and representation (10) require no derivative of tau beyond this
first derivative. The primal bounds used in them hold because
||delta||_n<=||q||_n.

For any fixed-set scalar identity
P_E z2'=alpha_E P_E delta+r_E, the logarithmic gate identity is
still (log D2_E)'=alpha_E b_E+beta_E r_E. Thus the transformed
actual primitive now satisfies

    c_E'=-beta_E r_E c_E+
                     beta_E tau(q_E) h_E+P_E u.        (23)

Equations (18)--(20) therefore hold with tau(q_E) in place of q_E.
The complete non-curvature source remains controlled, with no
inverse-gate moment assumption. This holds for each prescribed
clipping, uniformly in its level under the stated primal bounds.
It does NOT prove a uniform response estimate over the clipping
family: the signed covariance term in (23) still requires its
own bound. No second derivative of tau is assumed.
