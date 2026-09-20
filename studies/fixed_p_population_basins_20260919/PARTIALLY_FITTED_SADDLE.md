# A genuine three-input, partially fitted bad equilibrium

2026-09-19. Direct derivation from established fixed-order equations and
polynomial dictionaries, independently of any other study. Internal result.
This construction applies to exact p=1,2,3 on the circle and preserves
the canonical mark-parity subsystem. It is not a reachability example.

## Construction

Use the state definitions and physical Hilbert metric in
ESCAPE_AND_LIMITS.md. Write v_i=x_i/sqrt(2) only in this proof. Set t=1,

\[
b=\tanh 1,\qquad a=b/\sqrt2,\qquad
\cos\theta=\operatorname{artanh}(a)\in(0,1).
\]

Thus a=tanh(cos theta), and 0<theta<pi/2. Choose three distinct,
nonparallel and nonantiparallel inputs and mixed labels

\[
v_+=(\cos\theta,\sin\theta),\ y_+=1;\quad
v_-=(\cos\theta,-\sin\theta),\ y_-=-1;\quad
v_3=(1,0),\ y_3=1,
\]

with masses 1/3 each. Let s=sign(g_1), and set

\[
w_*=s(1,0),\qquad v_0=E_1[b_1s].
\]

The vector v0 is nonzero: tanh(g1) belongs to the lower dictionary
span, and E[tanh(g1)sign(g1)]>0. The lower moments are
a_+=a_-=a v0 and a_3=b v0.

Let X=tanh(xi_1), Y=tanh(xi_2) be the upper polynomial-core coordinates.
There is a coefficient e with b2^T e=X because the full dictionary
contains X and its normalization is invertible. Set

\[
M_*=\frac{e v_0^T}{|v_0|^2}.
\]

Then the upper preactivations are aX,aX,bX. Let V be the finite span
in upper L2 of

\[
\phi(aX),\qquad
(b_2)_j\phi'(aX),\qquad
(b_2)_j\phi'(bX)\quad(1\le j\le d_2).
\]

We show below that phi(bX) is not in V. Hence, with orthogonal projection
P_V, the bounded field

\[
R=\phi(bX)-P_V\phi(bX),\qquad c_*=\frac{R}{\|R\|_2^2}
\tag{1}
\]

is well-defined. It satisfies

\[
E[c_*\phi(aX)]=0,\quad E[c_*\phi(bX)]=1,\quad
E[b_2c_*\phi'(aX)]=E[b_2c_*\phi'(bX)]=0.
\tag{2}
\]

Thus the three predictions are (0,0,1), all backward coefficient
vectors d_i are zero, and the loss is 2/3. The first-row and middle
velocities vanish because d_i=0. The readout velocity also vanishes:
the first two residuals are -1,+1 and multiply the identical upper
feature phi(aX); the third residual is zero. This is therefore an
exact positive-loss equilibrium with a nonzero predictor.

## The independence used in the construction

If phi(bX) were in V, the positive density of (X,Y) on the open
square and continuity would give an identity there of the form

\[
\tanh(bX)=\lambda\tanh(aX)
       +P(X,Y)\operatorname{sech}^2(aX)
       +Q(X,Y)\operatorname{sech}^2(bX),
\tag{3}
\]

where P,Q are polynomials of degree at most p. Set Y=0.
Real-analytic identity extends (3) along the real line, and then
to its meromorphic complex continuation. One can justify the latter
without any choice of analytic branches by multiplying through by
cosh^2(aX)cosh^2(bX): the two sides become entire functions, equal
on an interval, hence equal everywhere by their convergent Taylor
series and continuation on overlapping disks.

At every z_k=i pi(k+1/2)/b, cosh(bz_k)=0 and cosh(az_k) is nonzero,
because a/b=1/sqrt(2) is irrational. The left side of (3) has a
simple pole. On the right the only potentially singular term is
Q(X,0) sech^2(bX), with leading coefficient
-Q(z_k,0)/(b^2(X-z_k)^2). Therefore Q(z_k,0)=0 for every k.
A one-variable polynomial with infinitely many distinct roots is
zero, so Q(X,0) vanishes identically. Then (3) has no right-side pole
at any z_k, a contradiction. Thus R in (1) is nonzero.

All constraints use the complete dictionary. No coordinates are
removed from the evolving matrix or from the allowed readout.

## Negative curvature involves two moving blocks

Take the bounded lower-row perturbation delta w=s(0,1), keeping M
fixed. Set kappa=sin(theta) phi'(cos(theta))>0. Direct differentiation
gives

\[
\delta H_+=\kappa X\phi'(aX),\qquad
\delta H_-=-\kappa X\phi'(aX),\qquad
\delta H_3=0.
\]

Let U=span{phi(aX),phi(bX)}, and put

\[
k=X\phi'(aX)-P_U[X\phi'(aX)].
\]

This is a nonzero bounded readout perturbation. Indeed X sech^2(aX)
cannot be a linear combination of tanh(aX),tanh(bX): at every
a-pole, which is not a b-pole, its nonzero factor X leaves a double
pole, whereas the other side has at most a simple pole. The same
entire-function continuation justifies comparing poles.

It follows that the mixed coefficient of ESCAPE_AND_LIMITS.md (4) is

\[
B(k,\delta w)
=-\frac{2\kappa}{3}\|k\|_2^2<0.
\]

The second loss variation along (w_*+h delta w,c_*+h alpha k,M_*)
has the form A+4alpha B. A finite choice of alpha makes it negative.
This equilibrium is a strict saddle in an actual two-block population
perturbation, although each hidden backward vector d_i is zero.

The first two per-sample readout gradients here are nonzero and cancel
in full batch. Therefore this example differs from (w,0,0), where all
individual sample gradients vanish. No SGD escape theorem is inferred
from the distinction alone.

## Symmetry and reachability

The state belongs to the invariant parity subsystem of canonical
initialization. The field w_* is odd under lower mark reversal.
The vector v0 has only odd dictionary coordinates, as does e, so
M_* has only an odd-to-odd block. The target phi(bX) in (1) is odd
under upper reversal. The span V is invariant under that reversal:
its odd generators and even generators are mutually orthogonal.
Its orthogonal projection therefore preserves odd parity, so c_* is
odd. The perturbations delta w and k used above have the same parities.

Thus parity alone does not exclude this bad state. The initial energy
exclusion of loss-one states also does not exclude it, since its loss
is 2/3. We have not shown that the canonical trajectory approaches it,
or that any nearby trajectory is attracted to it. Negative curvature
shows a local direction of loss decrease; the basin statement below
requires a separate argument.

## A basin criterion beyond the zero-predictor examples

Here is a useful extension of the difference-cone mechanism. Suppose
S_* is any stationary state of the finite-data fixed-order closure
such that q_i=0 as a lower-population function for every data point.
Suppose its second variation has a negative bounded direction.
Then its gradient vector field admits on the physical Hilbert space

\[
F(S_*+h)=A h+R(h),
\]

where A is bounded, selfadjoint and finite-rank with a positive
eigenvalue, R(0)=0, and the Lipschitz constant of R on a radius-r ball
tends to zero as r tends to zero.

To verify this assertion rather than assuming Hilbert C2 regularity:
the lower moment map w->(a_i)_i is C1 with locally Lipschitz derivative
into a finite-dimensional space. Its derivative is the bounded
integral in ESCAPE_AND_LIMITS.md (4), and the operator-norm difference
of derivatives is bounded by C||w-w'||_2. All scalar coefficients
r_i and coefficient vectors M^T d_i are C1 maps with locally
Lipschitz derivatives: upper preactivations live in a fixed finite
span and are bounded in L-infinity on a state ball; c enters bounded
linear pairings. Since q_i(S_*)=0, in the lower vector field the only
linear terms are fixed functions phi'(w_* dot x_i/sqrt2) times the
finite-dimensional linear variations of r_i q_i. Its nonlinear
remainder has Lipschitz constant O(r): the coefficient remainder
does, and the product of a coefficient O(r) with the L2-Lipschitz
gate has the same bound. The middle and readout components have
C1, locally Lipschitz finite-dimensional gate dependence and hence
the same remainder bound. Their linear ranges are finite-dimensional.

This proves finite rank and the remainder assertion. Since -F is the
C1 loss gradient, differentiability of F at S_* makes -A a symmetric
second derivative. Symmetry can also be checked by differentiating the
finite contractions in both orders along bounded directions and then
using density; boundedness extends the identity to H. Its negative
loss variation gives a positive eigenvalue of A. The elementary cone
argument in CLOSURE_ROUTE.md therefore applies: the local set of
points whose entire future stays in a sufficiently small closed ball
lies on a Lipschitz graph over a subspace of positive finite
codimension. It is closed with empty interior, and its intersections
with fibers parallel to the unstable eigenspace have at most one
point. In particular its conditional Lebesgue measure on each such
fiber is zero. The global basin converging to this fixed S_* is contained
in a countable union of inverse images of these local trapped sets and is
meagre, using openness of the finite-time flow as proved there.

The explicit state (1) has d_i=0 and hence q_i=0, and the preceding
mixed calculation provides its negative direction. Therefore this
actual nonparallel three-input equilibrium has the stated local
conditional-null trapped set and a meagre global point basin.
This is not a global Gaussian-nullity theorem on H, and meagreness
must not be equated with probability zero under an unspecified law.
