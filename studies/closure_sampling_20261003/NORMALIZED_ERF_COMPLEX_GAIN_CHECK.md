# Reconstruction of the normalized erf initialization and complex-radius calculation

2026-10-04. Internal study check by the scoped beta-envelope auditor, after
that auditor's own route was frozen. This is a reconstruction of the complete
candidate `NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md`, SHA-256
`8368603ca1a6bd449dc478810befce7aa62dc8cc1dc05869c9a68114a19599ef`.
The candidate was read in full and its hash verified. No other new sibling
route was read, no referenced scientific dependency was fetched, and the
candidate was left unchanged. The previously read canonical-notation,
neural-reference, rigorous-proof, and shared-workflow instructions apply.

Verdict: the stated initialization identities, fixed-depth finite-width
limits, complex derivative-moment radius of order \(L^{-1/2}\), and
fixed-dataset limiting gap \(\gamma_L\sim6/L\) pass this reconstruction.
No correction is required for their stated scope. These results do not
establish a new all-time compression theorem or a uniform growing-depth
finite-width limit. The details below make the moment and limit conditions
explicit, especially at the complex integrability boundary.

## 1. Activation, Gaussian normalization, and real covariance

The candidate uses independent standard Gaussian first weights and
independent hidden weights of variance \(1/n\), unit input vectors, and
the common activation
\[
\phi(x)=A\operatorname{erf}(x/\sqrt2)+b,\qquad
A^2=\frac{\pi\sqrt3}{2},\qquad
b^2=1-\frac{\pi}{2\sqrt3},
\]
with positive square roots. The offset is allowed by the user's conditions;
no centering condition was imposed. Since \(\Phi(Z)\) is uniform on
\([0,1]\), the identity \(\operatorname{erf}(Z/\sqrt2)=2\Phi(Z)-1\)
gives zero mean and second moment \(1/3\) for the erf term. Hence
\(\mathbb E\phi(Z)^2=A^2/3+b^2=1\).

Differentiation gives
\[
\phi'(x)=3^{1/4}e^{-x^2/2},\qquad
\phi''(x)=-3^{1/4}xe^{-x^2/2}.
\]
Using
\(\mathbb Ee^{-tZ^2}=(1+2t)^{-1/2}\) and its derivative gives
\[
\mathbb E\phi'(Z)^2=\sqrt3\,3^{-1/2}=1,
\qquad
\mathbb E\phi''(Z)^2=\sqrt3\,3^{-3/2}=1/3.
\]
All stated normalizations are exact. The activation is entire. Integrating
its derivative vertically from \(x\) to \(x+iy\) yields the bound
\[
|\phi(x+iy)|\le A+b+
3^{1/4}|y|e^{-x^2/2+y^2/2},
\tag{1}
\]
which proves boundedness on every finite horizontal strip and supplies
the domination used later.

For a centered real Gaussian pair with both variances \(q\ge0\) and
covariance \(c\), the density differentiation calculation in the
candidate gives
\[
\partial_c\mathbb E[\phi(X)\phi(Y)]
=\frac{\sqrt3}{\sqrt{(1+q)^2-c^2}}.
\]
For \(q>0\) the argument applies first to \(|c|<q\). The real
activation and derivatives are bounded, so the two integrations by parts
are justified; continuity extends the result integrated in \(c\) to
\(c=\pm q\). At \(c=0\) the expectation is \(b^2\), since the
nonconstant part is odd. Thus at unit variance
\[
F(c)=b^2+\sqrt3\arcsin(c/2),\qquad
F'(c)=\frac{\sqrt3}{\sqrt{4-c^2}},\qquad
F''(c)=\frac{\sqrt3c}{(4-c^2)^{3/2}}.
\tag{2}
\]
In particular \(F(1)=F'(1)=1\) and \(F''(1)=1/3\).
Setting \(c=q\) in the general formula gives
\[
V(q)=b^2+\sqrt3\arcsin\frac{q}{1+q},\qquad
V'(q)=\frac{\sqrt3}{(1+q)\sqrt{1+2q}},
\]
so \(V'(1)=1/2\). There is no conflation of the marginal-variance
derivative with the fixed-marginal covariance derivative.

The only arithmetic command executed was Python evaluation of these
elementary constants. It returned scale `1.649454166187`, offset
`0.305123446957`, and \(F''(3/2)\) `1.122263435499`, consistent with
the candidate's rounded values and its upper bound two. This was not a
network experiment or a substitute for the exact checks above.

## 2. Real first and second query derivatives

For \(d\ge2\), the input circle
\(v(\theta)=\cos\theta\,e_1+\sin\theta\,e_2\) has covariance
\(v(\theta)^\top v(\theta')=\cos(\theta-\theta')\).
At every fixed hidden depth \(L\), conditional independence of the
Gaussian rows gives the feature covariance limit
\[
K_L(\theta,\theta')=H_L(\cos(\theta-\theta')),
\qquad H_L=F^{\circ L}.
\tag{3}
\]
Because the covariance diagonal stays one, no extra variance factor is
missing from this composition.

The derivative version can be proved without differentiating a bare
pointwise limit. At a fixed finite set of angles, retain each row's
preactivation jet \((z,z',z'')\). At the first layer it is Gaussian;
at a single angle it has the form \((X,Y,-X)\) with independent
standard \(X,Y\). The activation jet is
\[
(\phi(z),\ \phi'(z)z',\
 \phi''(z)(z')^2+\phi'(z)z'').
\tag{4}
\]
Conditional on lower layers, the next row's preactivation jet is a
centered Gaussian vector whose covariance is the preceding empirical
Gram of (4). On a bounded set of covariance matrices, all fourth moments
of (4) are uniformly bounded: they are bounded by a polynomial of
Gaussian coordinates of degree at most eight, because the needed real
derivatives of phi are bounded. Conditional Chebyshev therefore proves
convergence of the empirical jet Gram. Covariance tightness follows
inductively from this same statement, allowing restriction to an
arbitrarily large bounded covariance set. Continuity of Gaussian
expectations of these polynomially bounded jet functions identifies
the limit. This also covers singular jet covariance matrices.

Differentiating the Gaussian covariance recursion under the same moment
domination identifies the limiting jet Gram with the derivatives of
(3). It follows directly by the chain rule that
\[
H_L'(1)=1,\qquad H_L''(1)=L/3.
\]
For \(s=\theta-\theta'\), the second derivative of
\(H_L(\cos s)\) at zero is \(-H_L'(1)\), and its fourth derivative
is \(H_L'(1)+3H_L''(1)\). The mixed angle derivative for first
tangents contributes the opposite sign, while the second-tangent
mixed derivative has positive sign. This verifies
\[
\frac1n\|\partial_\theta h_n^{(L)}\|_2^2\longrightarrow1,
\qquad
\frac1n\|\partial_\theta^2 h_n^{(L)}\|_2^2\longrightarrow1+L
\]
in probability for each fixed finite set of angles and fixed \(L\).
The circle-curvature term is exactly one, so the second formula has no
missing input-geometry contribution. No uniform finite-width query net
or trained-state statement has been established here.

## 3. Complex heat equation and integrability

For \(r\ge1\), let \(U=X+iY\), with independent centered real
Gaussians of variances \((r+1)/2\) and \((r-1)/2\). Then
\(\mathbb EU^2=1\) and \(\mathbb E|U|^2=r\).
Differentiating both variances with respect to \(r\) yields
\[
\frac d{dr}\mathbb EG(X,Y)=\frac14\mathbb E\Delta G(X,Y).
\tag{5}
\]
The coefficient is correct: each variance derivative is \(1/2\),
and Gaussian integration by parts supplies another factor \(1/2\).
For a holomorphic phi,
\(\Delta(\phi^2)=0\) and \(\Delta|\phi|^2=4|\phi'|^2\).

Equation (1) bounds all needed terms by polynomials times
\(e^{Y^2}\), after harmless constants. On a compact interval
\(1\le r\le r_*<2\), \(\operatorname{Var}Y<1/2\) with a
strict uniform margin, so Gaussian differentiation and the integrations
by parts are justified. The endpoint \(r=1\) is obtained by continuity
from above; the degenerate imaginary part causes no divergence. Thus
\(\mathbb E\phi(U)^2\) remains one. Also
\[
\mathbb E|\phi'(U)|^2
=\sqrt3\,\mathbb Ee^{-X^2}\mathbb Ee^{Y^2}
=\frac{\sqrt3}{\sqrt{r+2}\sqrt{2-r}}.
\tag{6}
\]
Integrating (5)--(6) from one proves
\(\mathbb E|\phi(U)|^2=F(r)\) for \(1\le r<2\).
At \(r\ge2\), the second factor in (6) diverges, so the derivative
moment is infinite. This is a Gaussian-moment failure despite entire
pointwise finite-network activations. The candidate correctly does not
claim that the feature moment itself diverges at the endpoint \(r=2\),
nor does it use an arcsine continuation beyond the stated interval.

There is a finite-width subtlety, but it does not invalidate the claimed
bridge. After the first layer the conditional pseudo-covariance is an
empirical quantity, and is not identically one. If a preactivation row has
conditional moments
\(p_n=\mathbb EU_n^2\) and \(r_n=\mathbb E|U_n|^2\), its real
covariance entries are
\[
\operatorname{Var}X_n=(r_n+\Re p_n)/2,\quad
\operatorname{Var}Y_n=(r_n-\Re p_n)/2,\quad
\operatorname{Cov}(X_n,Y_n)=\Im p_n/2.
\tag{7}
\]
When \((p_n,r_n)\to(1,r)\) with \(r<2\), a fixed neighborhood of
these limiting covariances has \(\operatorname{Var}Y_n<1/2\) with
a strict margin. Choose \(\epsilon>0\) so small that
\((1+\epsilon/2)\operatorname{Var}Y_n<1/2\) throughout this
neighborhood. Equation (1) then gives a uniform \(2+\epsilon\)
moment bound for the feature, and the exponential derivative formula
gives the same type of bound for its derivative. Independence of
\(X_n,Y_n\) is unnecessary for this upper bound, since the negative
\(-X_n^2\) term can be discarded.

For conditionally independent rows, truncate the squared feature modulus
at a fixed level \(M\). The variance of its empirical mean is at most
\(M^2/n\). The tail expectation is uniformly at most a constant
times \(M^{-\epsilon/2}\). First let \(n\to\infty\), then let
\(M\to\infty\). The same truncation controls the complex square
because \(|\phi(U)^2|=|\phi(U)|^2\). Gaussian coupling and uniform
integrability make the corresponding expectations continuous in (7).
Induction consequently yields the stated deterministic recursions
\[
p_j=1,\qquad r_0=\cosh(2\tau),\qquad r_{j+1}=F(r_j)
\]
for each fixed depth and fixed complex query for which every input
\(r_j<2\). Only finitely many covariance neighborhoods are needed.
This proves the candidate's finite-width bridge without requiring
fourth moments of complex features or exact finite-width
pseudo-covariance one.

## 4. Necessity and sufficiency of the radius scale

Put \(e_j=r_j-1\). For \(1\le r<2\), equation (2) gives
\(F''(r)\ge1/3\). Taylor's formula with an integral remainder
therefore gives
\[
e_{j+1}\ge e_j+e_j^2/6.
\]
For \(e_j>0\) and \(e_j<1\), reciprocation yields
\[
\frac1{e_j}-\frac1{e_{j+1}}
\ge\frac1{6+e_j}\ge\frac17.
\]
Finite derivative moments through \(L\) activation layers require
\(e_0,\ldots,e_{L-1}<1\). Summing only the \(L-1\) justified
increments, and retaining \(1/e_{L-1}>0\), gives
\((L-1)e_0<7\). Since \(e_0=\cosh(2\tau)-1\ge2\tau^2\),
the candidate's strict upper bound follows for \(L\ge2\).
The separate case \(\tau=0\) is stationary and requires no reciprocal.

For the sufficient bound, \(F''\) increases on \([1,3/2]\), and
\[
F''(3/2)=\frac{12\sqrt3}{7\sqrt7}<2.
\]
If \(e_0\le1/(8L)\), an induction that assumes all previous
\(e_j\le2e_0\) gives
\[
e_j\le e_0+4je_0^2\le\tfrac32 e_0<2e_0
\]
for \(j\le L\); the zero case is exact. This stays inside
\([1,3/2]\), closing the assumption. Moreover
\[
F'(1+e_j)\le1+2e_j\le e^{2e_j},\qquad
\prod_{j=0}^{L-1}F'(r_j)\le e^{4Le_0}\le e^{1/2}.
\]
For \(|\tau|\le1/(8\sqrt L)\), the elementary
\(\cosh x-1\le x^2\) for \(0\le x\le1\) gives
\(e_0\le1/(16L)\), sufficient with slack. Thus the lower and upper
radius bounds have the same \(L^{-1/2}\) order.

The radius concerns finite Gaussian derivative moments along the complex
circle, and the displayed product is the derivative of the scalar
Hermitian-moment iteration. It does not equal every finite-width
parameter-response norm. For each \(L\), the finite-width justification
takes \(n\to\infty\) separately. Nothing here controls a joint
limit \(L=L(n)\), a uniform random supremum over complex queries, or
the corresponding trained quantities.

## 5. Gap asymptotics and boundary cases

On \([-1,1]\), \(F'\le1\), strictly inside. Hence
\[
F(c)-c=\int_c^1[1-F'(s)]\,ds>0\qquad(c<1),
\]
and \(F(c)<F(1)=1\). Iterates starting from any \(c<1\), including
\(c=-1\), therefore increase to the only fixed point one. With
\(e_j=1-F^{\circ j}(c)>0\), Taylor expansion gives
\[
e_{j+1}=e_j-e_j^2/6+O(e_j^3),\qquad
\frac1{e_{j+1}}-\frac1{e_j}=1/6+O(e_j).
\]
The increments converge to \(1/6\). Averaging them yields
\(1/(je_j)\to1/6\), or \(je_j\to6\). This checks the
constant six and the order of the reciprocal argument.

For two distinct inputs the correlation is eventually positive, making
the smaller eigenvalue equal to \(1-F^{\circ L}(c)\), not merely
its absolute-value expression. For fixed \(m\ge2\) distinct unit
inputs, each off-diagonal correlation has this asymptotic and the
diagonal is exactly one. There are finitely many pairs, so entrywise
\(o(L^{-1})\) is operator-norm \(o(L^{-1})\). The comparison matrix
\[
(1-6/L)\mathbf1\mathbf1^\top+(6/L)I
\]
has eigenvalue \(6/L\) on the \(m-1\) dimensional orthogonal
complement of \(\mathbf1\), and eigenvalue
\(m-6(m-1)/L\) along \(\mathbf1\). Rayleigh/min-max bounds under
the operator perturbation therefore give \(\gamma_L\sim6/L\).

The qualifications in the candidate are necessary and correctly retained:
duplicate inputs have zero gap; \(m=1\) has gap one and is excluded
from this asymptotic; \(m\) is fixed; and finite-depth gaps must be
checked separately. The large-depth limit is taken for the deterministic
covariance recursion obtained after the fixed-depth width limit.

## Scope of the passing check

Every scientific line of the frozen candidate was checked against the
calculations above. The attacks addressed normalization versus centering,
the variance/covariance derivative distinction, derivative-limit exchange,
complex non-Gaussian features versus Gaussian preactivations, fluctuating
finite-width pseudo-covariance, the strict integrability boundary, layer
indexing in the reciprocal argument, zero imaginary displacement,
antipodal/duplicate inputs, and fixed versus growing depth and sample count.
No blocking defect was found.

This is an internal reconstruction by a participating study agent, not
an isolated promotion review. Its passing verdict is restricted to the
initialization and limiting-covariance statements. The candidate explicitly
leaves the all-time mixed term involving
\(\phi''(z)\dot z J\), the learned adaptive law, and all-time
compression constants unresolved; this check does not close those gaps.
