# A Gaussian-decaying gate removes the fixed-sign changing-control obstruction

Root candidate, 2026-09-06. This is an activation-design theorem for
prescribed two-coordinate characteristics and an initialization check.
It is NOT a global trained-network mean-field theorem. The control
sign premise and the distinction between a frozen control derivative
and a coupled training derivative are essential.

Choose once and for all

  phi(z)=1+(1/10)integral_0^z exp(-v^2)dv,
  phi'(z)=(1/10)exp(-z^2).                            (1)

This is the same scalar activation at all layers, independent of
width, time, labels, and input angle. It is strictly increasing and
nonaffine, with bounded positive range. It is a shifted, scaled error
function, specified by its integral so no convention for erf is needed.

For C=[[1,rho],[rho,1]], |rho|<1, prescribe u in L1([0,T];R^2)
whose coordinate signs are fixed on the interval. Let

  z'=C diag(phi'(z_1),phi'(z_2))u(t), z(0)=z0,
  U=(1/10)integral_0^T ||u(t)||_1dt,
  k=|rho|, delta=1-k, kappa=(1+k)/(1-k).

Then, uniformly in the initial point and in every such control,

  ||D_z0 z(T)||_op
       <=sqrt(kappa) exp(6) (exp(1)+U)^(64/delta).     (2)

The derivative in (2) holds the prescribed control fixed. Arbitrary
changing control ratios, vanishing components, and merely integrable
time dependence are allowed. Unlike a power of the initial point,
the constant in (2) is uniform over all z0. No control-sign-change
bound is asserted.

## 1. Activation properties and strict initial nonlinearity

For v>=1, exp(-v^2)<=v exp(-v^2), so

  integral_0^infinity exp(-v^2)dv
       <=1+exp(-1)/2<3/2.

It follows that 17/20<phi<23/20, hence 5/6<phi<7/6.
Also 0<phi'<=1/10 and

  |phi''(z)|=(1/5)|z|exp(-z^2)<=1/10<1/5,

because exp(z^2)>=1+z^2>=2|z|. All fixed higher derivatives
are bounded: differentiating exp(-z^2) repeatedly produces a
polynomial times exp(-z^2), which tends to zero at both tails.
These are exactly the activation size/first-two-derivative bounds
used in the existing short-time bootstrap; this assertion concerns
those numerical hypotheses, not automatic transfer of its entire
population construction or of any global conclusion.

On every nondegenerate scalar Gaussian, phi cannot agree almost
surely with an affine function. A continuous difference vanishing
almost everywhere for a positive Gaussian density vanishes everywhere,
whereas the derivative in (1) is nonconstant. The squared best-affine
approximation error is therefore strictly positive: the span of 1
and the Gaussian coordinate is a finite-dimensional closed subspace
of L2, and equality to zero error would be such an affine equality.

The same activation retains both initial label modes for every
admissible two-input correlation rho in [-1,1). Here is a direct
forward-law check, including the singular endpoint. Let the first
pair be centered Gaussian of variances one and correlation rho.
Since phi-1 is odd, each feature mean is one. Thus

  E[(phi(Z_1)+phi(Z_2))^2]/4>=1,
  E[(phi(Z_1)-phi(Z_2))^2]/4>0.

The second inequality follows since Z_1-Z_2 is a nondegenerate
Gaussian and phi is strictly increasing. More strongly, the feature
second-moment matrix is positive definite. At rho=-1, its two fields
are 1+g(G),1-g(G), where g=phi-1 is odd and nonconstant; a homogeneous
linear relation forces both its constant and odd coefficients to
vanish. At interior correlations, the pair has positive density on
R^2 and strict monotonicity again excludes any homogeneous linear
relation. A fresh initial N(0,1/n) matrix therefore produces a
limiting centered nondegenerate Gaussian pair with this feature
second-moment matrix as covariance. Iterating gives the same two
strict mode statements and strict Gaussian marginal nonaffinity
at all three hidden initial layers.

For clarity, this limiting forward assertion uses only independent
initial matrices: conditional on preceding features, new rows are
independent centered Gaussians with empirical feature second moments.
Bounded feature products have conditional average variance O(1/n).
Their expectations depend continuously on the covariance, by a
common standard-Gaussian square-root coupling and bounded convergence.
Induction from the independent first rows proves the stated joint
empirical initial forward laws in probability. This is not a trained
matrix-reuse assertion. Nonlinearity at all positive times and actual
nonlazy learning require additional proofs; they are not inferred
from these initial properties.

## 2. Reflected characteristic and its tangent energy

Existence, uniqueness, and initial-state differentiability for the
prescribed equation follow directly from its integral equation:
both its global Lipschitz coefficient and speed bound are at most
a constant times ||u(t)||. Subdivide its finite integral into small
pieces for contraction, and use dominated convergence in the
initial-state difference quotient equations. This gives an absolutely
continuous solution and its linear variational equation on [0,T].

Choose constant signs s_i so s_i u_i>=0 almost everywhere, and reflect
the coordinates, writing them x,y. Put alpha=|u_1|/10, beta=|u_2|/10,
A=alpha exp(-x^2), B=beta exp(-y^2), and r=rho s_1s_2. Then

  (x,y)'=C_r(A,B), C_r=[[1,r],[r,1]].                 (3)

For a tangent eta define E=eta^T C_r^-1 eta. The variational equation
gives exactly

  E'=2[-2x A eta_1^2-2y B eta_2^2]
          <=2h E,
  h=2x_- A+2y_- B,

since eta_i^2<=E by completing the square in C_r^-1. Hence

  ||D_z0 z(T)||<=sqrt(kappa) exp(I),
  I=integral_0^T h(t)dt.                             (4)

Reflections preserve the Euclidean propagator norm. The growth
estimate is valid even when a control vanishes on an interval.

## 3. A bounded potential separates the central region from the tails

Fix Q>=1. Choose a continuous nonincreasing function chi on [0,infinity)
which equals one on [0,1], vanishes on [2,infinity), and lies in [0,1].
For example take its linear interpolation on [1,2]. Define

  f_Q(v)=2v_- chi(v_-/Q),
  H_Q(v)=integral_v^0 f_Q(s)ds for v<0, and 0 for v>=0.

Then H_Q is C1, H_Q'=-f_Q, 0<=H_Q<=4Q^2, and 0<=f_Q<=4Q.
The derivative loss outside the truncation satisfies

  0<=2v_- - f_Q(v)<=2|v| 1_(v<=-Q).

For |v|>=Q>=1 the function |v|exp(-v^2) is decreasing with |v|,
so the integral of the corresponding discarded part of h is at most

  2Q exp(-Q^2) integral_0^T(alpha+beta)dt
                                     =2Q exp(-Q^2)U.          (5)

If r>=0, differentiation of H_Q(x)+H_Q(y) using (3) yields at most
-[f_Q(x)A+f_Q(y)B]. Thus its retained growth integral is at most
8Q^2, and (5) proves I<=8Q^2+2Q exp(-Q^2)U.

Now suppose r=-k<0. The exact potential identity is

  [H_Q(x)+H_Q(y)]'
     =-[f_Q(x)A+f_Q(y)B]+k[f_Q(x)B+f_Q(y)A].         (6)

Let the central set of times be those with |x|<=2Q and |y|<=2Q.
On it the last bracket is at most 4Q(A+B). Moreover w=x+y satisfies
w'=delta(A+B)>=0, and that set is contained in {-4Q<=w<=4Q}.
It follows that

  integral_central (A+B)dt<=8Q/delta.                (7)

One direct justification of (7) is to integrate the derivative of
the scalar function that clamps w to [-4Q,4Q]. This Lipschitz
piecewise-linear function obeys the absolutely continuous chain
rule away from its two corners. On a level set of an absolutely
continuous real function its derivative is zero almost everywhere,
so the corners contribute nothing. This level-set fact follows
at every differentiability and density point of the level set:
a nonzero derivative would make that point isolated on one side
up to a set of density zero. The exceptional sets have measure zero.
Thus (7) also holds with arbitrary flat portions or infinitely many
visits to the boundary; no crossing count is needed.

Outside the central set, a nonzero f_Q(x) requires -2Q<x<0,
so the other coordinate must have |y|>2Q. Its B is at most
beta exp(-4Q^2). The symmetric observation for f_Q(y)A gives

  integral_outside [f_Q(x)B+f_Q(y)A]dt
                                <=4Q exp(-4Q^2)U.    (8)

Integrating (6), using its endpoint bound 8Q^2, and then (5),
(7), and (8), proves

  I<=(8+32k/delta)Q^2
                 +4kQ exp(-4Q^2)U+2Q exp(-Q^2)U.    (9)

No initial-coordinate size appears in (9). The construction uses
the fast-decaying gate, not a bound on initial-state Gaussian density.

## 4. Optimize the truncation and interpret the result

Take Q=sqrt(2 log(exp(1)+U)). It is at least sqrt(2), and

  Q exp(-Q^2)U<=1.

Indeed, setting E0=exp(1)+U, one has U<=E0 and
sqrt(2 log E0)<=E0 for E0>=exp(1). The latter follows from
2 log E0<=E0^2, whose right side minus left side is increasing
for E0>=1 and positive at 1. The term with exp(-4Q^2) is smaller.
Consequently (9), and also the earlier r>=0 bound, give

  I<=6+(16+64k/delta)log(exp(1)+U)
    <=6+(64/delta)log(exp(1)+U).

Here 16+64k/delta=(16+48k)/delta<=64/delta. Inserting this in
(4) proves (2) for every allowed control and initial state.

For a random initial point and a random control whose signs are
fixed along each realized interval, the POINTWISE frozen-control
propagator bound implies finite q-th moments whenever
E[(exp(1)+U)^(64q/delta)]<infinity. Independence from the initial
point is unnecessary because the bound is uniform in that point.
This does not turn the frozen-control derivative into the derivative
of a feedback-controlled or coupled network: variations of the
control itself add a separate forcing term to the tangent equation.

The activation (1) therefore retains the old positive-range and local
smoothness bounds, remains strictly nonlinear under the initial
Gaussian laws, and removes the polynomial-sensitivity failure caused
by changing ratios WITHIN A FIXED SIGN QUADRANT. Actual backward
queries can change signs; their high moments on clipped continuations
and their feedback variations are not proved here. Nothing in this
document establishes those missing hypotheses or the requested
unconditional all-time joint MF/GF/GD limit.
