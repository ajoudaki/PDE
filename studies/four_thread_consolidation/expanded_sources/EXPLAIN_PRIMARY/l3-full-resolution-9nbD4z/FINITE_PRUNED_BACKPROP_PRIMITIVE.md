# A finite full/pruned backpropagation primitive with unweighted query source

Status: an exact nonlinear finite-pair representation and source estimate.
It is not a closed full/pruned comparison or a global population theorem.
Unlike a tangent calculation, this note compares two complete trajectories
at a finite separation. It retains all trained blocks. The ordinary query
difference is unweighted in its final scalar characteristic.

Use the canonical three-hidden-layer arctan feature-time equations, with
the transformed bottom coordinate X1=F(z1), F(s)=s+s^3/3. Vector norms are
||v||_n=||v||_2/sqrt(n), matrix norms are ordinary Frobenius/operator norms,
and u tensor v=uv*/n. Write C=W4 only within this note.

The full network and the network pruned on a FIXED middle set E start
from exactly the same parameter initialization. Hats denote the pruned
network. Its actual middle activation is Hhat2=Q phi(zhat2), Q=I-P_E,
and its backward field is deltahat2=Q Dhat2 tau(qhat2).
The full middle backward field is delta2=D2 tau(q2).
Here tau may be the identity, or the same prescribed Lipschitz clipping
in both networks, with |tau(x)|<=|x| and Lip(tau)<=1.
There is no assumption of differentiability of tau in this finite-pair
calculation. Both networks use the unchanged forward arctan activation.

Fix a feature interval [0,S] on which both trajectories have the usual
common primal operator bounds, normalized vector bounds, bounded readout
coordinates, and normalized velocity bounds. Constants below depend only
on those bounds and S, not on n, E or the common clipping threshold.
No lower coercivity bound or inverse Gram matrix is used.

## 1. The exact finite-pair field has a bounded lower transport

For any pair of vector or matrix objects, subscript av means their
arithmetic average; it does NOT mean recomputing a network at averaged
parameters. Put

    y=(x,A,B,c4)
     =(X1-Xhat1, W2-What2, W3-What3, C-Chat),
    p=delta2-deltahat2,       a(t)=integral_0^t p(s) ds.

Thus y(0)=0 and a(0)=0. Define the coordinatewise secant J1 by

    H1-Hhat1=J1 x,       H1=chi(X1), chi=phi o F^{-1}.

At equal coordinates use chi'. Since 0<chi'<=1, J1 is a symmetric
positive diagonal matrix with norm at most one. The exact preactivation
difference and lower updates are

    e=z2-zhat2=T y=A H1_av+W2_av J1 x,
    x'=W2_av* p+A*delta2_av,
    A'=p tensor H1_av+delta2_av tensor J1 x.             (1)

The two formulas follow from the identity
uv-uhat vhat=(u-uhat)v_av+u_av(v-vhat), including for a rank-one
product. In particular the averages in (1) involve the ACTUAL pruned
backward vector, which is zero on E.

Set

    R v=(W2_av* v, v tensor H1_av,0,0),
    m=||H1_av||_n^2,
    T R=A_pair=m I+W2_av J1 W2_av*.                    (2)

A_pair is symmetric positive semidefinite and bounded. We do not need
m to be bounded away from zero.

The top two difference equations are also a bounded linear map of y
plus a small purely top source. Here are explicit formulas. Let J2
be the secant of phi between z2 and zhat2. Then

    H2-Hhat2=J2 T y+d_E,
    d_E=P_E phi(zhat2),       ||d_E||_n<=a0 sqrt(rho),
    a0=pi/2,                 rho=|E|/n.                 (3)

Let J3 be the secant of phi between z3 and zhat3, and J3d the secant
of phi' between these two preactivations. Their norms are at most 1
and 2, respectively. Write D3_av=(D3+Dhat3)/2. Put

    e3_y=B H2_av+W3_av J2 T y,
    e3_source=W3_av d_E,
    d3_y=D3_av c4+diag(C_av) J3d e3_y,
    d3_source=diag(C_av) J3d e3_source.                 (4)

Then, exactly,

    z3-zhat3=e3_y+e3_source,
    delta3-deltahat3=d3_y+d3_source,
    B'=d3_y tensor H2_av+delta3_av tensor J2 T y
         +d3_source tensor H2_av+delta3_av tensor d_E,
    c4'=J3 e3_y+J3 e3_source.                          (5)

Every map multiplying y in (1), (4), and (5) has norm at most C_S
in the product Hilbert norm of y. For example,
||A*delta2_av||_n<=||A||_F||delta2_av||_n and
||delta2_av tensor J1x||_F<=C_S||x||_n.
The readout coordinates C_av are bounded in (4).

Consequently these EXACT equations have the form

    y'=L0(t)y+R(t)p+f_top(t),
    ||L0(t)||+||R(t)||+||T(t)||<=C_S,
    ||f_top(t)||<=C_S sqrt(rho).                       (6)

The source f_top is precisely the last two source terms in B' and
the last source term in c4' in (5); its two lower blocks are zero.
The lower two blocks of L0 are

    (A*delta2_av, delta2_av tensor J1x).

They depend only on the lower components of y, not on B or c4.
This remains true though all coefficients are evaluated on the two
coupled actual trajectories.

## 2. Integrating the complete finite backward difference

The primal updates give the useful exact derivative

    (W2_av)'=delta2_av tensor H1_av
                   +(1/4)p tensor (H1-Hhat1).          (7)

All factors have bounded normalized norms, so R' is bounded uniformly:
the other derivative in R is (H1_av)', also bounded in normalized norm.
There is no derivative of J1 in this assertion.

Let U0(t,s) be the evolution operator of L0 and set S0=L0 R-R'.
Both U0 and S0 have uniform operator bounds on [0,S]. In particular
the first block of S0 v is exactly

    -(1/4)(H1-Hhat1)<p,v>_n.                           (8)

Thus the cancellation of that block is not exact at a finite separation;
its retained remainder is bounded. It would vanish to first order when
passing to the infinitesimal representation.

Variation of constants and integration by parts, with a'=p, give

    y=y0+R a+integral_0^t U0(t,s)S0(s)a(s)ds,
    y0(t)=integral_0^t U0(t,s)f_top(s)ds.               (9)

The memory sign is PLUS because
partial_s[U0(t,s)R(s)]=-U0(t,s)S0(s).
The purely top subspace is invariant under L0, so y0 is purely top,
T(t)y0(t)=0, and ||y0(t)||<=C_S sqrt(rho).
Therefore

    e=A_pair a+v,
    v(t)=integral_0^t T(t)U0(t,s)S0(s)a(s)ds,
    ||y(t)||^2<=C_S[rho+||a(t)||_n^2
                              +integral_0^t||a(s)||_n^2ds]. (10)

All maps in v are bounded, but v is an actual returned response,
not an independent or a small additive source.

The top query difference is exactly

    q2-qhat2=B*delta3_av+
                        W3_av*(delta3-deltahat3).

Equations (4) and (10) give
||q2-qhat2||_n<=C_S(||y||+sqrt(rho)). Define the effective middle
queries

    g=tau(q2),       ghat=Q tau(qhat2),       u=g-ghat.

The common clipping is a contraction, hence

    ||u(t)||_n^2<=C_S[
       rho+||P_E qhat2(t)||_n^2+||a(t)||_n^2
                              +integral_0^t||a(s)||_n^2ds]. (11)

This is a proved ordinary-source estimate. In the zero-readout Gaussian
proxy, equation (4) and the event allocation in
SHARP_RARE_ACCUMULATED_FORCING.md give the simultaneous pruned-query
event that bounds its second
term by C_S[rho log(e/rho)+epsilon_n^2]. This use retains the exact
scope of that event (including a prescribed common clipping). No such
Gaussian estimate or tiny-readout transfer is asserted from (11) alone.
At rho=0, rho log(e/rho) means its continuous value zero.

## 3. An exact nonlinear scalar characteristic

For each middle coordinate set

    M=1+(z2^2+z2 zhat2+zhat2^2)/3,
    M_z=(2z2+zhat2)/3,       M_hat=(z2+2zhat2)/3,
    c=M a.                                                   (12)

All products in (12) are coordinatewise. M is the secant of F:
F(z)-F(zhat)=M(z-zhat), including its continuous diagonal value.
In particular M>=1 and ||a||_n<=||c||_n.

Write D=phi'(z2), Dhat=phi'(zhat2), and retain the exact scalar
residuals

    r1=z2'-m D g,       r2=zhat2'-m Dhat ghat,
    h=e-m a.

Here h contains both the nonscalar instantaneous part of A_pair
in (10) and its entire memory. Define

    A_gate=M_z D g+M_hat Dhat ghat.

The algebraic secant identities

    M+e M_z=D^{-1},       -M+e M_hat=-Dhat^{-1}

imply, without approximation,

    M p=u-e A_gate.

Also M'=m A_gate+M_z r1+M_hat r2. Consequently

    c'=u-A_gate h+
                   [(M_z/M)r1+(M_hat/M)r2]c.             (13)

The coefficient of the COMPLETE ordinary source u is exactly one.
No inverse activation gate or preactivation polynomial multiplies it.
This is not obtained by differentiating a primal norm estimate or by
replacing the finite pair with an infinitesimal response.

The residual coefficients in (13) are bounded functions of the two
preactivations. Indeed, with Q0=(z^2+z zhat+zhat^2)/3,
(2z+zhat)^2<=12Q0 and (z+2zhat)^2<=12Q0, so

    |M_z/M|<=1/sqrt(3),       |M_hat/M|<=1/sqrt(3).       (14)

No boundedness of A_gate as a multiplication operator is asserted.

The exact finite-pair energy is therefore

    (1/2)(||c||_n^2)'=<c,u>_n-<c,A_gate h>_n
          +<c^2,(M_z/M)r1+(M_hat/M)r2>_n.               (15)

By (11), M>=1 and Young's inequality, the FIRST term is bounded by

    |<c,u>_n|<=C_S[
       rho+||P_E qhat2||_n^2+||c(t)||_n^2
                              +integral_0^t||c(s)||_n^2ds]. (16)

The last two signed terms in (15) remain unestimated. Neither normalized
L2 primal bounds nor (14) controls their multiplication by this actual
finite error. Thus (9)--(16) establish a finite nonlinear counterpart
of the unweighted-source primitive, not a closed error estimate.
No clipping derivative, lower coercivity, covariance independence, or
population convergence premise is required for these identities.
