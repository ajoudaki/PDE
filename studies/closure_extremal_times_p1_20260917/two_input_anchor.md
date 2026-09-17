# A rederived two-input anchor and the terminal-loss regime

2026-09-17. This proof is derived in the present study from the exact p=1
initialization, symmetries and physical gradient. No earlier study is an input.
Use the model, notation and complete initialization calculation of
extremal_hitting_times.md, Sections 1 and 7, and their declared docs sources.

## 1. The admitted close pair has a scalar residual

Let u_+=(cos(delta),sin(delta)), u_-=(cos(delta),-sin(delta)), with equal
weights and labels (+1,-1). Take any sufficiently small fixed delta>0.
The initialization calculation (21)--(23) in the companion proof gives
kappa(cos(delta)) near kappa(1)>0 and kappa(sin(delta))!=0. Therefore

    U0=[H0(u_+)-H0(u_-)]/2,
    C0=E2 U0^2>0.                                        (1)

No lower bound uniform as delta->0 is asserted. The proof below also applies
at any separation at which this same reflection-pair contrast is nonzero.

To verify the required symmetry for the actual dictionary, set
R=diag(1,-1), T1=diag(1,1,-1,1,-1), T2=diag(1,1,-1), in its canonical
constant,h1,h2,k1,k2 and constant,Z1,Z2 ordering. Let rho1 negate G2 and
its reverse Gaussian noise, and let rho2 negate the second upper Gaussian.
Both preserve their full population laws; b1(rho1)=T1 b1, g(rho1)=R g,
b2(rho2)=T2 b2. The initialized matrix satisfies T2 D T1=D.

The following transformation of characteristic states is an isometric
involution in the physical metric:

    w_bar(omega)=R w(rho1 omega),
    c_bar(omega)=-c(rho2 omega), M_bar=T2 M T1.

Substitution into the exact feature integrals gives
a_bar(u)=T1 a(Ru), H_bar(u,omega)=H(Ru,rho2 omega), and
f_bar(u)=-f(Ru). It fixes the initialized state and leaves the two-point
loss invariant. Equivariance of its gradient and uniqueness of the exact
flow thus imply f(u_-)=-f(u_+) along the initialized trajectory.

Define at any state

    U=[H(u_+)-H(u_-)]/2, F=E2[c U], q=E2 c^2,
    C=E2 U^2, K=||grad F||^2.

On the symmetry-fixed states L=(1-F)^2. Its FULL physical gradient is
grad L=-2(1-F)grad F there, because the two residuals are exact opposites.
Hence all three parameter blocks obey

    X'=2(1-F)grad F.                                    (2)

The symmetry restriction does not freeze any entry of M or either hidden layer.

## 2. A global auxiliary curve, established before fitting

Solve X_s=grad F from initialization. The same involution leaves F invariant,
so it preserves this curve too. It exists on each finite s interval: bounded
dictionary marks give local existence in the characteristic L-infinity
increments, while the exact gradient bounds give

    ||c||infty<=s, ||M-D||F<=s^2/2,
    ||w-g||infty<=B1(d0 s^2/2+s^4/8).                    (3)

Indeed c_s=U has supremum at most one; the average difference of the two
matrix gradients has norm at most ||c||2<=s; the row gradient is bounded
by B1||M||op||c||2. Integration gives (3), preventing a finite-s escape.
The canonical polynomial local Lipschitz estimates then extend the curve.

Along it,

    F_s=K=C+||grad_(w,M)F||^2, q_s=2F, F^2<=q C.          (4)

At s=0, hidden gradients vanish, c_s=U0, and F_s=C0. Consequently

    F(s)=C0 s+o(s), q(s)=C0 s^2+o(s^2).

For s>0, F>0 by F_s>=0 and its initial derivative, and q>0 by F^2<=qC.
Differentiating q/F^2 gives

    (q/F^2)_s=-2(qK-F^2)/F^3<=0,
    lim_(s downarrow0) q/F^2=1/C0.

Thus for all s>0,

    q<=F^2/C0, C>=C0, K>=C0.                             (5)

In particular F reaches one at a unique finite s_*, with s_*<=1/C0.
Existence at that endpoint follows from (3), and K is finite and positive
there. These are derived facts, not supplied endpoint premises.

The physical clock ds/dt=2(1-F(s)), s(0)=0, stays in [0,s_*), increases
to s_*, and reproduces (2). To see that it does not hit s_* at finite t,
its error e=1-F solves e'=-2K(s(t))e with continuous finite K on [0,s_*].
Thus e=exp(-2 integral_0^t K(s(v))dv)>0 at finite t. Since K>=C0,
e<=exp(-2C0 t), and the clock approaches s_*. Uniqueness identifies this
curve with the canonical initialized physical solution.

## 3. Exact time integral and the two asymptotic regimes

Since F_s=K>=C0, F is an admissible coordinate on [0,s_*]. Write
k(F)=K(X(s(F))). It is positive and continuously differentiable, because
the characteristic vector field and feature maps are smooth on the bounded
increment region (3). Directly integrating (2)--(4) gives, for 0<ell<1,

    tau_delta(ell)=integral_0^(1-sqrt(ell))
                               dF/[2(1-F)k(F)].          (6)

In particular

    tau_delta(ell)<=log(1/ell)/(4 C0).                    (7)

Let K_*=k(1)>0. The difference 1/k(F)-1/K_* is O(1-F), by positivity
and continuous differentiability near F=1. Thus its contribution to (6)
is integrable through F=1, proving the sharp FIXED-DATA asymptotic

    tau_delta(ell)=log(1/ell)/(4K_*)+O_delta(1)
                                     as ell->0.         (8)

At the other endpoint k(0)=C0 and 1-sqrt(1-epsilon)=epsilon/2+O(epsilon^2),
so the same integral gives

    tau_delta(1-epsilon)=epsilon/(4C0)+O_delta(epsilon^2)
                                      as epsilon->0.    (9)

The coefficients controlling the high-loss start and the small-loss tail
are DIFFERENT: the initialized hidden contrast C0 versus the full learned
gradient strength K_*. Equations (8)--(9) do not justify exchanging the
epsilon or ell limits with delta->0.

For every fixed ell, the companion proof's lower bound also applies:

    1/(2K1 delta)<=tau_delta(ell)<=log(1/ell)/(4C0(delta))  (10)

for all sufficiently small delta. It proves divergence even in this
family whose actual global fitting has just been established.
These bounds do not match in general. In particular one must not declare
the true delay to be 1/C0 from the initial slope or the upper bound alone.
The analytic kappa calculation implies C0(delta) is comparable to delta^(2m)
for some finite odd m>=1: if kappa(r)=a r^m+O(r^(m+2)), then U0 divided by
kappa(sin(delta)) converges in L2 to Z2 sech^2[Z1 kappa(1)], whose squared
norm is strictly positive. This observation supplies a polynomial upper
bound, but the present study does not evaluate m or sharpen (10).

## 4. A state potential and what a common rate would require

For this scalar-residual family define

    W=1+C0(1+q)/(C0+F^2), Phi=L W.

Equations (4)--(5) yield 1<=W<=2 and

    W_s= -2 C0 F[(qK-F^2)+(K-C0)]/(C0+F^2)^2<=0.

Together with L'=-4K L this proves

    L<=Phi<=2L, Phi(0)=2, Phi'<=-4C0 Phi.                 (11)

This is an independent derivation within the present study. It is fully
consistent with the hitting-time lower bounds: its guaranteed rate 4C0
depends on delta and tends to zero, while the initial potential is fixed.
There is no common-rate conclusion in (11).

The length estimate ||X'||=2(1-F)sqrt(K)<=-d(1-F)/dt /sqrt(C0)
gives integral_t^infinity ||X'||<=sqrt(L(t)/C0). Thus the complete physical
state has a fitting limit; this is stronger than vanishing loss alone.

If one demands instead a common lambda and L<=C Phi^alpha, (8) forces
alpha lambda<=4K_*(delta) for every admitted pair. The present proof gives
K_*>=C0(delta), but this LOWER bound does not show that K_* tends to zero.
Neither existence nor impossibility of such a common-rate potential follows
from the pair's long transient alone. Its necessarily large initial value
and its possible asymptotic exponent are separate constraints.
