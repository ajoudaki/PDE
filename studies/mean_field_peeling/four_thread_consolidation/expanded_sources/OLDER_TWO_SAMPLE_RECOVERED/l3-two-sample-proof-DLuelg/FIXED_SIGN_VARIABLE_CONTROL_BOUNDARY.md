# Fixed-sign changing controls: a sublinear sensitivity bound and its sharp scale

Root candidate, 2026-09-06. This document concerns a prescribed
two-dimensional control equation, NOT a canonical trained trajectory.
It is self-contained and does not invoke the separate constant-control
lemma. It tests what survives when the forcing changes with time.

Let phi(z)=1+atan(z)/10, p(z)=phi'(z)=1/[10(1+z^2)],
C=[[1,rho],[rho,1]], |rho|<1. On [0,T], prescribe an integrable
u=(u_1,u_2) with fixed coordinate signs: there are constants
s_i in {-1,1} such that s_i u_i(t)>=0 almost everywhere.
Consider the ordinary controlled equation

  z'=C diag(p(z_1),p(z_2))u(t), z(0)=z0.              (1)

Put k=|rho|, delta=1-k, kappa=(1+k)/(1-k),
R=1+||z0||_1, and U=(1/10)integral_0^T ||u(t)||_1 dt.
Then its initial-state tangent satisfies

  ||D_z0 z(T)|| <= sqrt(kappa)
        exp(min{U, 3[R+U^(1/3)]/delta}).              (2)

If the reflected correlation rho s_1 s_2 is nonnegative, the stronger
time/control-independent exponent 2R can replace the second exponent
in the minimum. The constants permit zero controls and vanishing
components. This estimate holds for arbitrary changing component
ratios. In contrast, a polynomial in U is FALSE in this generality:
an explicit smooth positive control below has U of order T^3 and
tangent norm at least exp(c T), for a fixed initial state and fixed
strictly negative rho. Thus the exponent power 1/3 in (2) cannot be
replaced by a smaller power uniformly over this control class.

## 1. Reduction, well-posedness and tangent energy

For a fixed integrable control the vector field is measurable in time,
smooth in the state, has speed bounded by a constant times ||u(t)||,
and has a global state-Lipschitz bound of that same form. Iteration
of the integral equation on intervals with sufficiently small control
integral is a contraction. A finite partition suffices for any finite
total integral, and proves existence and uniqueness on [0,T]. The
same integral estimates applied to difference quotients give the
initial-state derivative and its variational equation: use the average
state derivative along the two solutions, dominated by C||u(t)||,
and dominated convergence. Hence all subsequent identities hold
almost everywhere for absolutely continuous curves.

Reflect z_i by s_i, writing the coordinates as x,y. In original time
put alpha(t)=|u_1(t)|/10, beta(t)=|u_2(t)|/10 and
A=alpha/(1+x^2), B=beta/(1+y^2). The reflected equation is

  (x,y)'=C_r(A,B), r=rho s_1 s_2.                    (3)

Reflection is independent of the initial state and preserves tangent
operator norms and R. Define

  H(v)=log(1+v_-^2),
  f(v)=-H'(v)=2|v|/(1+v^2) for v<0, and 0 for v>=0.

H is C1, 0<=f<=1. If eta is a tangent and E=eta^T C_r^-1 eta,
direct differentiation gives

  E'=2[-2alpha x/(1+x^2)^2 eta_1^2
                       -2beta y/(1+y^2)^2 eta_2^2]
     <=2[A f(x)+B f(y)]E.

Here eta_i^2<=E, as follows by completing the square in C_r^-1.
Thus, with I=integral_0^T[A f(x)+B f(y)]dt,

  ||D_z0 z(T)||<=sqrt(kappa) exp(I), I<=U.           (4)

The last inequality uses A+B<=alpha+beta. The energy inequality
follows by multiplying by the integrating factor exp(-2 integral h);
no bounded number of zero crossings or differentiability of the
control is used.

When r>=0, x'>=A and y'>=B. Therefore
[H(x)+H(y)]'<=-[A f(x)+B f(y)], giving I<=2R.

## 2. Negative correlation and the cubic control cost

Suppose r=-k<0. Set L=integral_0^T(A+B)dt and w=x+y.
Equation (3) gives w(T)=w(0)+delta L, and I<=L.
Since x'=A-kB<=A and y'=B-kA<=B, the C1 positive-part cube satisfies

  [x_+^3+y_+^3]'<=3[x_+^2 A+y_+^2 B]
                          <=3(alpha+beta).

Integration yields x_+(T)^3+y_+(T)^3<=R^3+3U.
For nonnegative a,b, (a+b)^3<=4(a^3+b^3): expansion reduces it to
3ab(a+b)<=3(a^3+b^3), or (a-b)^2(a+b)>=0. Consequently

  delta L=w(T)-w(0)
     <=x_+(T)+y_+(T)+|w(0)|
     <=4^(1/3)(R^3+3U)^(1/3)+R
     <=(1+4^(1/3))R+12^(1/3)U^(1/3)
     <=3[R+U^(1/3)].                                 (5)

The penultimate step follows by cubing
(R^3+3U)^(1/3)<=R+(3U)^(1/3). Equations (4)-(5) prove (2).
They do not require a positive lower bound on either control ratio.

For a random initial state with any Gaussian law, and any fixed
deterministic such control, (2) has finite moments of every order:
its logarithm is bounded by a constant times 1+||z0||_1 plus a finite
constant. The Gaussian exponential-absolute moment is finite, as
seen from exp(lambda||z0||_1)<=sum_(s in {+-1}^2)exp(lambda s^T z0)
and completing the square in each scalar Gaussian integral. If the
control is random and state-dependent, this observation alone says
nothing about the distribution of U or its correlation with z0.

## 3. A smooth fixed-sign control with exponential tangent growth

Fix k in (0,1), take rho=-k, and let d=1-k^2. For all t>=0 prescribe

  u_1(t)=20k, u_2(t)=10[1+(2+dt)^2], z0=(-1,2).      (6)

These controls are strictly positive and smooth. The exact solution
of (1) is x(t)=-1, y(t)=2+dt, since A=k and B=1. Its control cost is

  U(T)=(2k+5)T+2d T^2+d^2 T^3/3.                   (7)

The prescribed control is held FIXED when the initial state is
varied. Put b(t)=2y(t)/(1+y(t)^2), so 0<b(t)<=1. The tangent equation
along this solution is

  (xi,eta)'=[[k,kb],[-k^2,-b]](xi,eta).              (8)

To see a growing tangent without an eigenvector approximation, solve
the scalar equation

  s'=k^2-(k+b)s+kb s^2, s(0)=0.                    (9)

At s=0 its derivative is k^2>0, and at s=k its derivative is
-kb(1-k^2)<0. A first-contact argument proves 0<=s<=k throughout,
so the scalar solution is global. Define

  xi(t)=exp(integral_0^t k[1-b(r)s(r)]dr),
  eta(t)=-s(t)xi(t).

Differentiating these expressions verifies (8) with initial tangent
(1,0). Moreover xi(t)>=exp(k(1-k)t). Hence

  ||D_z0 z(T)||>=exp(k(1-k)T).                       (10)

For T>=1, (7) is bounded above and below by positive multiples
of T^3 depending only on k. Thus (10) rules out C(1+U)^p for any
fixed finite C,p, even with constants allowed to depend on rho and
z0. It also rules out exp(C[1+U^gamma]) for gamma<1/3. This confirms
the scale of (2); it does not assert optimal constants.

The example can equally be placed on the fixed interval [0,1]: for
L>=1 prescribe u_L(t)=L u(Lt). Its solution is z_L(t)=z(Lt), its
control cost is U(L), and its initial-state tangent at time one is
the tangent in (10) at time L. The controls depend only on t and L,
not on the perturbed initial condition. No feedback derivative has
been silently included in (8).

## 4. Exact research boundary

The equation (1) has the form of a first-layer characteristic under
prescribed backward forcing, up to its specified factor 1/2. This
note does not prove that actual trained backward queries have fixed
signs, the control schedule (6), or the exponential-integrability
needed to average (2) with random trained controls. In particular,
(6) is not a trained-network or typical-Gaussian counterexample.
It shows why a constant-control polynomial estimate cannot simply
be applied to a changing forcing and then passed to a fine mesh.
The new positive estimate is the fixed-sign cube-root control bound;
arbitrary sign-changing controls and the full population continuation
remain separate obligations.
