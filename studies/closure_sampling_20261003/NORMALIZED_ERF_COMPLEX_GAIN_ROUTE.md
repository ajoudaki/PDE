# A variance-normalized critical erf: polynomial depth and the complex query radius

2026-10-04. Coordinator derivation continuing the activation/depth-constant
question in this study. The ultimate target remains all-time compression of
the same canonical finite Gaussian dense network, with all hidden layers of
width n, trained hidden weights and zero initialized readout. This note proves
initialization results and explains a source-radius mechanism. It does not
claim a new all-time compression theorem, or a lower bound against arbitrary
compressors. No network experiment was run. The only numerical evaluation
was of displayed elementary constants.

Scientific inputs: the model and interpretation in
INPUT_DIMENSION_REFINEMENT.md and the complete initialization/training
distinction in NONEXPANSIVE_INITIAL_QUERY_ROUTE.md. All Gaussian calculations
needed below are proved here. Required research, rigorous-proof, canonical
notation and neural-reference instructions were applied. This candidate was
developed without reading the concurrent normalized-activation routes.

## 1. An ordinary-sized nonlinear activation meeting both moment conditions

Let Z be a standard real Gaussian. Define Phi as its distribution function
and erf(x/sqrt(2))=2 Phi(x)-1. Set

\[
b=\sqrt{1-\frac{\pi}{2\sqrt3}},\qquad
\phi(x)=\sqrt{\frac{\pi\sqrt3}{2}}\,
                 \operatorname{erf}(x/\sqrt2)+b.
\tag{1}
\]

Numerically the scale is 1.6494541662 and the offset is 0.3051234470.
The exact formulas, not these rounded numbers, define the activation.
It is entire, bounded on every horizontal strip, smooth, monotone on the
real line, and has order-one output. In particular this is not a small-output
contractive activation. Its derivatives are

\[
\phi'(x)=3^{1/4}e^{-x^2/2},\qquad
\phi''(x)=-3^{1/4}x e^{-x^2/2}.
\tag{2}
\]

The uniform random variable Phi(Z) gives
E erf(Z/sqrt(2))=0 and E erf(Z/sqrt(2))^2=1/3.
The elementary Gaussian integral E exp(-t Z^2)=(1+2t)^(-1/2)
and its derivative give

\[
\mathbb E\phi(Z)^2=1,\qquad
\mathbb E\phi'(Z)^2=1,\qquad
\mathbb E\phi''(Z)^2=\frac13.
\tag{3}
\]

Every hidden layer of the Gaussian initialization recursion therefore has
unit feature second moment. For completeness, along a horizontal line,
integrating the entire derivative vertically gives
|phi(x+iy)|<=sup_R|phi|+3^(1/4)|y| exp(y^2/2), so every finite strip has a
finite value bound. It also satisfies the newer bounded-strip-derivative
condition. That membership alone does not give beta=1 in the old theorem.

## 2. The exact covariance and variance maps

For unit-variance correlated real Gaussians X,Y with E[XY]=c, define
F(c)=E[phi(X)phi(Y)]. Direct Gaussian differentiation gives

\[
F'(c)=\mathbb E[\phi'(X)\phi'(Y)]
      =\frac{\sqrt3}{\sqrt{4-c^2}}.
\]

Here the first equality follows by differentiating the bivariate Gaussian
density: its covariance derivative is its mixed spatial derivative.
Two integrations by parts transfer those derivatives to phi. The functions
and their first two derivatives are bounded on the real line, so Gaussian
domination justifies both operations for |c|<1. The second equality is the
two-dimensional Gaussian integral of exp(-(X^2+Y^2)/2): diagonalizing the
covariance gives determinant (1+1)^2-c^2=4-c^2. At c=0 independence gives
F(0)=b^2. Integration and continuity at the endpoints yield

\[
F(c)=1-\frac{\pi}{2\sqrt3}+\sqrt3\arcsin(c/2),
\qquad -1\le c\le1.
\tag{4}
\]

Consequently F(1)=F'(1)=1 and F''(1)=1/3. The same Gaussian calculation
with marginal variance q gives the variance map

\[
V(q)=\mathbb E\phi(\sqrt q Z)^2
 =b^2+\sqrt3\arcsin\!\left(\frac{q}{1+q}\right).
\tag{5}
\]

Indeed the derivative with respect to covariance c at fixed marginal
variance q is sqrt(3)/sqrt((1+q)^2-c^2); integrate from zero to c=q.
This proves V(1)=1 and V'(1)=1/2. Thus ordinary variance perturbations
are locally contracted, while angular first-order sensitivity is critical.
These two different derivatives must not be conflated.

## 3. Exact real query sensitivities at initialization

For d>=2 use the great-circle query v(theta)=cos(theta)e_1+sin(theta)e_2.
Let h_n^(L)(theta) be the initialized top hidden feature of the canonical
width-n network. At fixed L the limiting normalized covariance is

\[
\lim_{n\to\infty}\frac1n
 h_n^{(L)}(\theta)^\top h_n^{(L)}(\theta')
 =F^{\circ L}(\cos(\theta-\theta')).
\tag{6}
\]

The limit is in probability for each finite set of angles. Its derivative
versions used next follow by the same conditional Gaussian argument:
include a row's value and first two angle derivatives as a finite jet.
At the next linear layer that jet is conditionally centered Gaussian;
its covariance is the preceding empirical jet Gram. Differentiating phi
gives polynomial expressions in that Gaussian jet with bounded real
derivatives. Conditional fourth-moment bounds and Chebyshev give empirical
second-moment convergence at each fixed layer. Those fourth-moment bounds
are finite by induction, starting with the two Gaussian first-weight
coordinates. They also justify differentiation of the limiting covariance.
This is a fixed-depth, fixed-query argument, not an all-query/all-time net.

Put H_L=F composed L times. Repeated differentiation at its fixed point 1
gives H_L'(1)=1 and H_L''(1)=L/3. Differentiating (6) in both angle
variables therefore proves

\[
\frac1n\|\partial_\theta h_n^{(L)}(\theta)\|_2^2
 \longrightarrow1,
\qquad
\frac1n\|\partial_\theta^2 h_n^{(L)}(\theta)\|_2^2
 \longrightarrow1+L.
\tag{7}
\]

For the second identity, the fourth derivative at zero of H_L(cos t)
is H_L'(1)+3H_L''(1). The +1 is the curvature of the input circle itself.
Thus critical normalization really removes exponential growth from the
first tangent, but cannot keep all response orders independent of depth.
This is an actual initialized neural-feature statement, not just a generic
smooth-function example. It is not a lower bound on prediction compression.

## 4. A polynomial, and necessarily shrinking, complex query tube

Analytic source compression needs more than real tangent variance. Consider
a complex Gaussian U=X+iY with independent real Gaussian parts and

\[
\mathbb EU^2=1,\qquad \mathbb E|U|^2=r\ge1.
\]

Equivalently Var(X)=(r+1)/2 and Var(Y)=(r-1)/2. For 1<=r<2,

\[
\mathbb E\phi(U)^2=1,\qquad
\mathbb E|\phi(U)|^2=F(r),\qquad
\mathbb E|\phi'(U)|^2=\frac{\sqrt3}{\sqrt{4-r^2}}.
\tag{8}
\]

Here F(r) is the real formula (4) continued to 1<=r<2. A proof avoiding
formal analytic continuation is useful. For every suitable function G of
X,Y, covariance differentiation and one-dimensional integration by parts
give d E G/dr=(1/4)E(Delta G). For holomorphic phi, Delta(phi^2)=0 and
Delta|phi|^2=4|phi'|^2. The derivative integral in (2) gives the domination
|phi(X+iY)|<=C+3^(1/4)|Y|exp(-X^2/2+Y^2/2).
On compact subintervals of r<2, its square and all needed differentiated
expressions are integrable, since Var(Y)<1/2. Gaussian differentiation is
therefore valid. The first formula in (8) stays at its value 1 at r=1.
The derivative moment equals sqrt(3) E exp(-X^2+Y^2), the product of two
elementary Gaussian integrals. Integrating it from r=1 gives the middle
formula. At r>=2 the derivative moment is infinite, directly from the Y
integral. This last statement requires no extension of F beyond its domain.

For a complex great-circle query v(i tau)=cosh(tau)e_1+i sinh(tau)e_2,
the initial preactivation has

\[
r_0=\cosh(2\tau),\qquad r_{j+1}=F(r_j)
\tag{9}
\]

as long as r_j<2. The pseudo-covariance stays one. These are the exact
Gaussian initialization moment recursions, justified by fresh conditional
Gaussian rows and truncation at each fixed depth. Fourth moments of complex
features are unnecessary for that assertion: on compact subsets of r<2,
some 2+epsilon moment is finite, giving uniform integrability and a truncated
conditional law of large numbers. No recursion after loss of integrability
is claimed.

Write e_j=r_j-1. On 1<=r<2, F''(r)>=1/3, so

\[
e_{j+1}\ge e_j+e_j^2/6.
\tag{10}
\]

If e_j<1, it follows that
1/e_j-1/e_{j+1}>=1/(6+e_j)>=1/7. Thus finite derivative moments through
L activation layers require, for tau!=0 and L>=2,

\[
(L-1)(\cosh(2\tau)-1)<7,
\qquad |\tau|<\sqrt{\frac7{2(L-1)}}.
\tag{11}
\]

Conversely, for 1<=r<=3/2 the displayed derivative of (4) gives F''(r)<=2.
If e_0<=1/(8L), induction using F(1+e)-1<=e+e^2 gives

\[
0\le e_j\le2e_0\quad(0\le j\le L),
\qquad
\prod_{j=0}^{L-1}F'(r_j)\le e^{4Le_0}\le e^{1/2}.
\tag{12}
\]

For example |tau|<=1/(8 sqrt(L)) suffices: for 0<=x<=1,
cosh(x)-1<=x^2 follows from its power series and cosh(1)-1<1;
use x=2|tau|. Then e_0<=1/(16L), stronger than the needed bound.
The induction has margin because L(2e_0)^2<=e_0/2. The product bound
uses F'(1)=1 and F''<=2.

Equations (11)--(12) show a complex mean-square regularity radius of order
L^-1/2, rather than an exponentially small one, for this normalized,
nonlinear activation. They simultaneously rule out a depth-independent
complex mean-square derivative tube for this same example. Finite networks
are entire in the query; it is the Gaussian moment bound that fails outside
the indicated scale, not finite-network pointwise analyticity.

The factor product in (12) is the derivative of the scalar Hermitian moment
recursion. It is not by itself the norm of every trained network response.
That distinction is essential when using this result to guide a source proof.

## 5. Dataset gap and honest implications for compression

For any c<1 in [-1,1], F(c)>c and F(c)<1. Indeed F'(c)<=1 on that
interval, strictly inside it, and F(1)=1. Therefore every pair of distinct
normalized inputs has initialized feature correlation tending to one as
L grows. Taylor expansion of (4) at one gives

\[
1-F(1-e)=e-e^2/6+O(e^3).
\]

If e_L=1-F composed L times(c), then e_L decreases to zero and
1/e_(L+1)-1/e_L tends to 1/6. Averaging these increments proves
L e_L tends to 6. For two distinct inputs the smaller covariance eigenvalue
is 1-|F composed L times(c)|, hence gamma_L is asymptotic to 6/L.
For a fixed collection of m>=2 pairwise distinct inputs, every off-diagonal
entry has this same leading asymptotic. In matrix form

\[
Q^{(L)}=(1-6/L)\mathbf1\mathbf1^\top+(6/L)I+o(L^{-1}),
\qquad \gamma_L\sim6/L.
\tag{13}
\]

The error is in operator norm because m is fixed. Eigenvalue perturbation
can be justified directly by Rayleigh quotients, without a new theorem:
an operator perturbation of norm epsilon changes every ordered eigenvalue
by at most epsilon, by the min-max characterization. In particular the gap
is eventually positive; a particular finite-depth theorem still checks its
actual gap. Duplicate inputs are excluded because they give zero gap.

These are encouraging polynomial-depth mechanisms: unit forward scale,
unit real first-tangent scale, a radius L^-1/2, and gap L^-1. They do not
prove that the current all-time compressor can replace beta by one. A
source approximation on a tube of radius L^-1/2 would normally still cost
a power of L in its number of query coefficients, and actual trained
source responses require adaptive mixed moments that (8)--(12) do not
control. Some depth growth might be absorbed by the explicit inverse gap;
this note does not prove either its sufficiency or its impossibility.

In particular the actual time derivative of a query tangent includes
W[phi''(z) dot(z) J]. At present the required all-time, whole-query bound
on the learned response times J remains the same unclosed product recorded
in NONEXPANSIVE_INITIAL_QUERY_ROUTE.md. The initialized calculations cannot
be substituted for that trained estimate. The old theorem's numerical
floors also absorb universal constants and cannot be set to one by a
definition change.

Status: complete candidate derivation, awaiting a separate reconstruction.
The positive initialization theorem and the limitation of a constant
complex moment radius are distinct from the unresolved all-time target.
