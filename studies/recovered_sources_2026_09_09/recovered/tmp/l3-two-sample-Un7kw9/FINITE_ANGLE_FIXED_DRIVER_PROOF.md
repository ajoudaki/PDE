# Finite-angle arctangent q-channel: complete fixed-driver candidate

Status: new main candidate, not independently audited. This completes
the clock step left open in FINITE_ANGLE_Q_CHANNEL_ROUTE.md. It proves
only a LOCAL TWO-COORDINATE q-channel theorem, not the coupled network.
The uncontrolled p channel and late-injection distinction remain.

Use phi(z)=1+z+e arctan z, e>0 fixed, L=1+e, gamma=e/L,
0<=delta<=1, mu^2=1-delta^2, and the smooth definitions

    a_delta(M,V)=[phi'(M+delta V)+phi'(M-delta V)]/2,
    b_delta(M,V)=-2e M V/
         [(1+(M+delta V)^2)(1+(M-delta V)^2)].

The autonomous q-channel is M_r=mu^2 b_delta, V_r=a_delta. At delta=0
these formulas are the tangent channel; at delta=1 the common coordinate
is frozen. Its global C1 flow Psi_{delta,r} exists for all real r:
1<=a_delta<=L and |b_delta|<=2e|V| give bounded states on each finite
driver interval, and smooth local existence continues them. V increases
onto R, so an orbit has a unique point with V=0.

## 1. Previously proved orbit estimates used precisely

FINITE_ANGLE_Q_CHANNEL_ROUTE.md, completed portions through (10), supplies
the following exact scalar equation and estimates. They are also the
starting facts verified in SIGNED_DRIVER_ISOLATED_REVIEW.md, but that
review is not a mathematical dependency needed for this proof.

Write m(v)=M on the orbit at contrast v, Y=v^2, Y0=V0^2, and

    F(X,Z)=(1+X+Z)(1+X+Z+e)-4XZ,
    f(m,Y)=-e mu^2 m/F(m^2,delta^2 Y),
    m_Y=f(m,Y), m(Y0)=M0.

This scalar equation is smooth through m=0 and Y=0. The radius and
initial-common-coordinate derivative at fixed terminal Y obey

    |m(v)|<=|m(0)|<=sqrt(M0^2+(e/2)V0^2)<=B,
    0<J(v):=partial_{M0}m(v)<=E,
    B=1+|M0|+sqrt(e)|V0|,
    E=exp(C_0|M0|)+exp(gamma V0^2),
    C_0=4/sqrt(L)+2(2+e)/L.                            (1)

For clarity, the proof of the response input (1) uses f_m>=-e/L
backwards in Y. For forward Y it uses
integral(f_m)_+ dY <= integral_0^{M0^2} sup_Z |F_X|/F dX,
F>=L(1+X), and |F_X|<= [2+(2+e)/sqrt(L)]sqrt(F).
It does not require that m(v) tend to zero for delta>0.

All constants denoted C_e below are finite functions only of fixed e.
They may increase from line to line. No such constant depends on delta,
initial coordinates, driver, or terminal contrast.

## 2. Uniform integral and slope estimates for clock differentiation

We prove the two estimates

    integral_R |partial_M a_delta(m(v),v)| dv <=C_e B^4,
    sup_v |partial_v m(v)| <=C_e B^4.                  (2)

These statements remain valid when m(0)=0, when their left sides vanish.

First note the global and large-argument bounds

    |partial_M a_delta(m,v)|<=2e|m|,
    |partial_M a_delta(m,v)|<=2e,
    |partial_M a_delta(m,v)|<=128e |m|/|delta v|^4
                                if |delta v|>=2(B+1),  (3)
    F(m^2,delta^2v^2)>=|delta v|^4/16
                                on the same region.   (4)

For the first bound, phi'' is odd and ||phi'''||_infinity=2e:
the average of phi''(m+delta v),phi''(m-delta v) equals half their
odd-symmetrized difference around delta v. The mean value estimate
therefore gives 2e|m|. The second follows from ||phi''||<=2e.
If |delta v|>=2(B+1), all arguments between delta v-m and delta v+m
have absolute value at least |delta v|/2>=1. On |z|>=1,
|phi'''(z)|<=8e/|z|^4, giving the third bound. Both factors in the
original product defining F are at least (|delta v|/2)^2, which
proves (4). The additional positive e term only increases F.

Suppose first 0<delta<=1/2. Put D=2(B+1). For |v|<=1/delta,
m^2<=B^2 and delta^2v^2<=1 give

    F(m^2,delta^2v^2)<=(B^2+2)(B^2+2+e)
                         <=K_e B^4,
    K_e=3(3+e).

Since mu^2>=3/4, the scalar equation for log|m| gives, from Y=0,

    |m(v)|<=B exp(-alpha v^2),
    alpha=3e/(4K_e B^4)=c_e/B^4,
                          for |v|<=1/delta.           (5)

For larger |v|, monotone decrease in Y gives the plateau bound

    |m(v)|<=B exp(-alpha/delta^2).                     (6)

The elementary maximization x exp(-alpha x^2)<=1/sqrt(2alpha exp(1))
implies

    delta^(-1) exp(-alpha/delta^2)<=C_e B^2.           (7)

Split the integral in (2) into |v|<=1/delta,
1/delta<|v|<=D/delta, and |v|>D/delta. The three bounds in (3),
with (5)--(7), bound these portions respectively by

    2eB sqrt(pi/alpha)<=C_e B^3,
    4eBD delta^(-1)exp(-alpha/delta^2)<=C_e B^4,
    (256eB/(3delta D^3))exp(-alpha/delta^2)<=C_e B^4.

This proves the integral assertion. The last estimate follows by
integrating |v|^-4 on both tails. It does not bound an integral of
|m| over all R, which need not converge at positive delta.

For the slope, the scalar equation gives

    |m_v|=2e mu^2 |v m|/F.

On the core use F>=L and sup |v|exp(-alpha v^2)<=1/sqrt(2alpha exp(1))
to get C_e B^3. On the middle region, use |v|<=D/delta and (6)--(7)
to get C_e B^4. On the tails use (4) and (6):

    |m_v|<=32eB exp(-alpha/delta^2)/(delta D^3)
             <=C_e B^4.

This proves the second assertion in this delta range.

For delta=0, (5) holds for every v because F(m^2,0)<=K_e B^4 and
mu^2=1. The core estimates alone prove both assertions in (2).

For 1/2<=delta<=1, split at |v|=D/delta. The inner interval has length
2D/delta<=4D. Use the constant bound 2e in (3) to bound its integral
by 8eD, and use |v m|<=2DB, F>=L to bound its slope by C_e B^2.
On the tails, (3)--(4) and |m|<=B bound the integral by
256eB/(3delta D^3), and the slope by 32eB/(delta D^3). These are
bounded by C_e B^4. In particular delta=1 creates no singularity.
This completes the proof of (2) uniformly over the entire angle range.

## 3. Initial contrast derivative for the nonautonomous orbit equation

Because f in the scalar Y equation depends on Y when delta>0, the
autonomous identity m_{V0}=-2V0 f(m,Y) cannot be imported from the
tangent proof. The correct formula is

    partial_{V0}m(v;M0,V0)=-2V0 f(M0,Y0) J(v).          (8)

To verify it, let S(Y,Y0,M0) denote the scalar flow. Differentiating
S(Y,Y0+h,S(Y0+h,Y0,M0))=S(Y,Y0,M0) at h=0 gives
partial_{Y0} S=-(partial_{M0}S)f(M0,Y0). The displayed identity follows
since Y0=V0^2. Equivalently it follows by differentiating the initial
condition and solving the scalar variational equation. Local smooth
ODE dependence justifies these derivatives on every finite Y interval.
The formula also holds at V0=0 and M0=0. Since F>=L, (1) gives

    |partial_{V0}m(v)|<=2gamma |V0 M0| E<=C_e B^2 E.    (9)

No derivative of delta is being taken.

## 4. Invert the clock at fixed driver

The exact signed clock is

    r=integral_{V0}^{V} dv/a_delta(m(v;M0,V0),v).        (10)

Its terminal derivative lies in [1/L,1]. For finite r, ordinary
differentiation of this finite integral is legitimate. The estimates
in (2) control it uniformly as the terminal contrast varies. There
is no differentiation of an improper integral.

Writing subscripts on V(r),M(r) for fixed-r derivatives yields

    V_{M0}=a_delta(M,V) integral_{V0}^{V}
            [a_M(m,v) m_{M0}(v)/a_delta(m,v)^2] dv,
    V_{V0}=a_delta(M,V)/a_delta(M0,V0)
        +a_delta(M,V) integral_{V0}^{V}
            [a_M(m,v) m_{V0}(v)/a_delta(m,v)^2] dv.

The moving endpoint in the second formula is included. Bounds (1),
(2), and (9) imply

    |V_{M0}|<=C_e B^4 E,   |V_{V0}|<=C_e B^6 E.

The terminal-coordinate chain rules are

    M_{M0}=m_{M0}(V)+m_v(V)V_{M0},
    M_{V0}=m_{V0}(V)+m_v(V)V_{V0}.

Using (2) once more gives

    |M_{M0}|<=C_e B^8 E,  |M_{V0}|<=C_e B^10 E.

Also partial_r V=a_delta<=L and partial_r M=m_v a_delta, so
the full uniform bound is

    sup_{delta in[0,1], r in R}
      (||D_{(M0,V0)}Psi_{delta,r}||+||partial_r Psi_{delta,r}||)
      <=C_e B^10[exp(C_0|M0|)+exp(gamma V0^2)].         (11)

All arguments, including (8)--(10), are smooth at M0=0; there the
orbit is m=0, a_M=0, m_v=m_{V0}=0, and J is the scalar linearization
already covered by (1). Thus (11) has not excluded a zero coordinate.

For jointly Gaussian initial coordinates of finite variances,
(11) has a finite p-th moment if p gamma Var(V0)<1/2. Polynomial
factors in the coordinates and linear exponentials in |M0| do not
alter this strict threshold: condition M0 on V0, integrate its
Gaussian residual, and absorb resulting linear terms into an arbitrarily
small extra quadratic term. If Var(V0)=0 all positive moments are finite.
For M0=mu G_1, V0=G_2 with independent standard Gaussians and mu in[0,1],
the constants in this moment bound can be chosen uniform in mu. In
particular e=1/10 permits a uniform fourth-moment local response over
all input angles, with that single fixed activation.

## 5. Exact scope

Locally integrable signed q drivers compose with the global autonomous
flow via r(t)=integral q. Initial-state derivatives hold q fixed; a
differentiable q selection adds partial_r Psi times the derivative of
that integral. Neither term controls the derivative of q's selection
rule. The actual first-layer equation has the additional p vector field
M_u=mu^2(ap+bq), V_u=aq+delta^2 bp. Higher layers also have trained
operator transport terms. Equation (11) gives no bound on arbitrary
late p injections or on those coupled responses. The uniform local
q-channel theorem is therefore NOT the user's universal full-network
theorem, and no cutoff removal is inferred from it alone.
