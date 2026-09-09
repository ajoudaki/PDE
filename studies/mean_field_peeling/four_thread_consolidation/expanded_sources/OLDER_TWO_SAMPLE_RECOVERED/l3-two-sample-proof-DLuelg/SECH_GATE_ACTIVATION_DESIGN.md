# Exponential gate tails with the old relative-gate bound retained

Root candidate, 2026-09-06. This is a self-contained activation-design
and prescribed-characteristic theorem, NOT the full two-sample limit.
It does not assume or prove that actual backpropagation controls keep
fixed signs. No external specialized theorem or experiment is used.

Fix the single activation

  phi(z)=1+(1/10)atan(sinh z),
  p(z)=phi'(z)=(1/10)sech z.                          (1)

It is independent of width, input angle, labels, and time. Two
properties hold together:

  5/6<phi<7/6, 0<phi'<=1/10, |phi''|<=1/10,
  |phi'(z)-phi'(z')|<=|phi(z)-phi(z')|.               (2)

For C=[[1,rho],[rho,1]], |rho|<1, consider the prescribed-control flow

  z'=C diag(p(z_1),p(z_2))u(t), z(0)=z0,
  u in L1([0,T];R²).

Assume there is a constant pair s_i in {-1,1} with s_i u_i>=0 almost
everywhere. Its frozen-control initial-state tangent satisfies

  ||D_z0 z(T)||_op
    <=sqrt((1+k)/(1-k)) exp(4) (exp(1)+U)^(16/(1-k)),
  k=|rho|, U=(1/10)integral_0^T ||u(t)||_1dt.         (3)

The bound is uniform over ALL initial points and all such integrable
controls, even with arbitrarily changing component ratios and vanishing
components. The derivative keeps the control fixed. It is not the
derivative of a coupled feedback system.

## 1. Activation eligibility and the relative-gate estimate

Differentiating atan(sinh z) gives cosh z/(1+sinh²z)=sech z.
The activation minus one is odd and strictly increasing. Its positive
tail amplitude is bounded using t=exp(-v):

  integral_0^infinity sech v dv
     =2 integral_0^1 (1+t²)^-1 dt<5/3.

For the strict inequality, on 0<t<1,
(1+t²)^-1<1-t²/2, since multiplication by 1+t² leaves the positive
remainder t²(1-t²)/2. Integrating the right side gives 5/6 and the
factor two gives 5/3. Multiplying by 1/10 proves the range in (2).
The derivative p is positive, at most 1/10, and

  p'(z)=-(1/10)sech z tanh z, |p'|<=1/10.

Every fixed higher derivative is bounded, by induction using
(sech)'=-sech tanh and (tanh)'=sech². The ratio

  p'(z)/phi'(z)=-tanh z

has absolute value at most one. Since phi is strictly increasing,
view p as a function of phi(z) on its open range. The preceding
ratio is that function's derivative. Integrating it between phi(z)
and phi(z') proves the relative-gate inequality in (2).

This last bound is useful because for any two current preactivations,
if V=[phi(z_1)-phi(z_2)]/2 and p_-=[p(z_1)-p(z_2)]/2, then
|p_-|<=|V| pointwise. No independence between a gate and a backward
query is implied. This statement is only an exact scalar inequality.

The activation is strictly nonaffine under any nondegenerate scalar
Gaussian law. Otherwise continuity and strictly positive Gaussian
density would make it affine everywhere, contradicting its nonconstant
derivative. Its squared best-affine approximation error is positive,
since the span of 1 and the Gaussian coordinate is a closed finite-
dimensional subspace of L2 and phi itself is bounded.

For completeness it also retains both initial label modes at all
three hidden layers under the canonical equal-width independent
Gaussian initialization. Start with a centered pair of variances one
and correlation rho in [-1,1). Oddness of phi-1 gives mean feature
one; hence its same-label mode squared norm is at least one. Its
opposite-label mode has positive squared norm, since the initial
Gaussian difference has positive variance and phi is strictly
increasing. The feature SECOND-MOMENT matrix is positive definite:
at rho=-1 the features are 1+g(G),1-g(G) with nonconstant odd g,
and a homogeneous linear dependence forces its constant and odd
coefficients both to vanish. At interior correlations, positive
two-dimensional Gaussian density and varying each argument exclude
any homogeneous linear dependence. Thus a fresh initial Gaussian
matrix at the next layer gives a nondegenerate centered Gaussian
pair; applying the same argument inductively gives both modes and
strict scalar Gaussian nonaffinity at every initial hidden layer.

This forward limit uses no matrix reuse. Conditional on preceding
feature vectors h_i in R², the new Gaussian rows are independent
N(0,n^-1 sum_i h_i h_i^T). Bounded feature products and bounded
continuous tests have empirical conditional variances O(1/n).
Their expectations vary continuously with this covariance, including
singular covariances, by coupling through its positive square root
and applying bounded convergence. Square-root continuity follows
by subsequences of bounded positive roots and uniqueness of the
positive root of a positive semidefinite matrix. Induction from the
independent first rows proves the separate same-neuron sample-pair
empirical laws jointly in probability across the three populations.
No matching of neuron indices between populations is required.
These initial checks do not prove nonaffinity or nonlazy dynamics
at positive training times.

## 2. Characteristic and tangent regularity for integrable controls

For a fixed u in L1, the speed and spatial derivative of the vector
field are bounded by (1+k)||u(t)||_1/10. The spatial derivative is
globally Lipschitz with an integrable coefficient because p'' is
bounded. A finite partition into intervals with small coefficient
integral makes the integral equation a contraction on continuous
paths and produces a unique absolutely continuous global path on
[0,T]. Its speed bound excludes finite-time escape.

The initial-state difference quotient solves the corresponding
integral equation with the averaged state derivative along two
solutions. The ordinary integral Lipschitz estimate bounds the
trajectory difference by a constant times the initial difference.
Bounded p'' then makes the remainder after the linear variational
solution O(||initial difference||²) uniformly on [0,T]. Thus the
initial-state Frechet derivative exists at every point and satisfies
the variational equation, with the prescribed u unchanged.

Reflect the coordinates by the constant signs s_i, calling them x,y.
Evenness of p gives

  (x,y)'=C_r(A,B), C_r=[[1,r],[r,1]], r=rho s_1s_2,
  A=alpha sech x, B=beta sech y,
  alpha=|u_1|/10, beta=|u_2|/10.                      (4)

For a tangent eta set E=eta^T C_r^-1 eta. Since the diagonal state
derivative before multiplication by C_r is
diag(-A tanh x,-B tanh y), direct differentiation gives

  E'=2[-A tanh x eta_1²-B tanh y eta_2²]<=2hE,
  h=A f(x)+B f(y), f(v)=(-tanh v)_+.

Here eta_i²<=E by completing the square, and 0<=f<=1. The eigenvalues
of C_r lie between 1-k and 1+k. The integrating-factor inequality
therefore proves

  ||D_z0 z(T)||_op<=sqrt((1+k)/(1-k)) exp(I),
  I=integral_0^T h(t)dt.                             (5)

No control derivative or sign crossing count is used in (4)-(5).

## 3. A truncated potential and occupation estimate

For Q>=1 choose continuous chi on [0,infinity), equal to one up to
one, equal to zero from two onwards, nonincreasing, and in [0,1].
Define

  f_Q(v)=f(v)chi(v_-/Q),
  H_Q(v)=integral_v^0 f_Q(s)ds for v<0, and 0 for v>=0.

Then H_Q is C1, H_Q'=-f_Q, 0<=H_Q<=2Q and 0<=f_Q<=1.
The discarded factor f-f_Q vanishes when v>=-Q and is at most one
otherwise. Since sech v<=2exp(-|v|), its total growth contribution
is at most

  2 exp(-Q) U.                                       (6)

If r>=0, differentiating H_Q(x)+H_Q(y) gives at most
-[f_Q(x)A+f_Q(y)B]. Its integral is at most the initial potential
sum, bounded by 4Q independently of the initial point. Together
with (6), this gives I<=4Q+2exp(-Q)U.

For r=-k<0 the exact identity instead is

  [H_Q(x)+H_Q(y)]'
     =-[f_Q(x)A+f_Q(y)B]+k[f_Q(x)B+f_Q(y)A].         (7)

On the central set {|x|<=2Q,|y|<=2Q}, the last bracket is at most
A+B. Also w=x+y satisfies w'=(1-k)(A+B)>=0, and that set is
contained in {|w|<=4Q}. Consequently

  integral_central (A+B)dt<=8Q/(1-k).                 (8)

To verify (8) for arbitrary absolutely continuous paths, clamp w
to [-4Q,4Q] and integrate its derivative. This derivative equals
w' on the open strip and zero outside. On a boundary level set,
w'=0 almost everywhere: almost every point of the level set is a
density point where w is differentiable, and difference quotients
through other points of that set force the derivative to be zero.
Thus using the closed strip changes no integral. The total increase
of the clamped coordinate is at most 8Q. Repeated visits or flat
portions cause no extra term.

Outside the central set a nonzero f_Q(x) requires -2Q<x<0, so the
other coordinate obeys |y|>2Q. Hence f_Q(x)B<=2beta exp(-2Q) there.
The symmetric estimate for f_Q(y)A gives

  integral_outside [f_Q(x)B+f_Q(y)A]dt
                                         <=2exp(-2Q)U.        (9)

Combining (6)-(9) and the endpoint potential bound 4Q proves

  I<=[4+8k/(1-k)]Q+2k exp(-2Q)U+2exp(-Q)U.         (10)

## 4. Optimize and state exactly what has been obtained

Let Q=2log(exp(1)+U)>=2. Then exp(-Q)U<=1, and the faster-decaying
term is no larger. Thus (10) yields

  I<=4+[8+16k/(1-k)]log(exp(1)+U)
    <=4+[16/(1-k)]log(exp(1)+U).

The preceding r>=0 estimate is also covered by this bound. Inserting
it in (5) proves (3), for zero cost as well as positive cost. It is
a finite-power upper bound; rounding the exponent upward to an
integer gives an ordinary polynomial if that terminology is desired.

The pointwise estimate has no dependence on z0. For a measurable
random control and initial point satisfying the fixed-sign premise,
the frozen-control tangent therefore has finite q-th moment whenever
E[(exp(1)+U)^(16q/(1-k))]<infinity. This requires no independence
from the initial state. It does not establish the required control
moments in a trained network or bound a feedback variation of u.

The activation (1) retains the bounded positive range, the same
first-two-derivative size bounds, and the relative-gate inequality
of the arctan route, while producing the polynomial characteristic
estimate (3) for changing ratios within a sign quadrant. It avoids
a derivative vanishing at finite preactivation and is not affine
under any initial nondegenerate Gaussian law. These are supporting
properties only. Actual sign changes, feedback response, uncut
population continuation, exact-GD/GF convergence, and nontrivial
feature learning at every finite time still require their own
proofs. No full two-sample theorem is asserted in this document.
