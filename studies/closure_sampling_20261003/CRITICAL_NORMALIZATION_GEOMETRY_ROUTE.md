# Critical normalization and initialization geometry

Author: scoped agent `critical_activation_geometry`. Date: 2026-10-04.

Scope: independent, prompt-only mathematical route within the assigned study.
Scientific inputs were only the supervisor's assignment: independent Gaussian
mixers with variance inverse width, sphere queries, and one analytic activation
\(\phi\) satisfying
\[
\mathbb E\phi(Z)^2=\mathbb E\phi'(Z)^2=1,
\qquad Z\sim N(0,1).
\]
I read the required repository process instructions, canonical-notation skill
and its neural-network reference, and rigorous-math skill. I read no book,
code, study history, other route, or external scientific source. The statements
below are self-contained results for an initialization covariance recursion.
They are not a training or compression theorem, and are not promoted material.

## 1. Precise model and the normalization issue

Let \(x\in S^{d-1}\subset\mathbb R^d\) have ordinary Euclidean norm one. To
obtain first-layer preactivations of variance one using
\(W^{(1)}_{ij}\sim N(0,1/d)\), set
\[
h^{(0)}(x)=\sqrt d\,x,
\quad z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),
\quad h^{(\ell)}(x)=\phi(z^{(\ell)}(x)),
\]
where \(W^{(\ell)}\in\mathbb R^{n_\ell\times n_{\ell-1}}\),
\(n_0=d\), and all entries and layers are independent, with entry variance
\(1/n_{\ell-1}\). Equivalently, use an unscaled unit vector with first-layer
weight variance one. Literal unscaled Euclidean unit inputs and first-layer
variance \(1/d\) instead give variance \(1/d\); the displayed conditions at a
standard Gaussian do not then describe the first-layer variance fixed point.

For jointly standard normal \((X,Y)\) with correlation \(c\in[-1,1]\), define
\[
F(c)=\mathbb E[\phi(X)\phi(Y)],
\qquad K_0(c)=c,\qquad K_{\ell+1}(c)=F(K_\ell(c)).
\]
These definitions make sense under the two given square-integrability
conditions. They are the exact objects studied below. Under, for example,
continuous polynomially growing \(\phi\), or bounded continuous \(\phi\),
they are also the fixed-depth, infinite-width activation covariance recursion
of the network above, at initialization.

Here is the elementary reason for that interpretation in these growth classes.
Conditional on all preceding layers, rows of each next preactivation array on
a finite query set are independent Gaussian vectors with covariance equal to
the preceding empirical feature Gram matrix. Their coordinate products after
applying \(\phi\) have locally bounded second moments in the polynomial-growth
case, and uniformly bounded second moments in the bounded case. Conditional
Chebyshev bounds therefore make their empirical average converge to its
conditional expectation. Gaussian integration makes that expectation continuous
in the covariance, using a common standard normal vector and dominated
convergence; locally bounded covariance matrices provide the needed Gaussian
polynomial moment bound. Induction over a fixed number of layers proves the
recursion, including diagonal entries one. A separate centered Gaussian
readout with variance inverse width produces a Gaussian-process limit with
covariance \(K_L(x^\top y)\), by its conditional Gaussian law.

The two given moments alone need not provide the local moment control needed
in that finite-width argument. No finite-width convergence theorem for arbitrary
analytic \(\phi\) is asserted here. No width grows jointly with depth in these
arguments, and there is no training time, loss, learning-rate, or closure state.

## 2. Hermite reduction, with its dependencies proved

Write \(\gamma(dx)=(2\pi)^{-1/2}e^{-x^2/2}dx\). Define the probabilists'
Hermite polynomials by
\[
e^{tx-t^2/2}=\sum_{k=0}^\infty H_k(x)\frac{t^k}{k!},
\qquad h_k=H_k/\sqrt{k!}.
\]
Taking the expectation of the product of two generating functions gives
\(e^{st}\) for one standard Gaussian, and \(e^{cst}\) for two correlated
standard Gaussians. Comparison of coefficients proves
\[
\mathbb E[h_j(Z)h_k(Z)]=\mathbf1_{j=k},\qquad
\mathbb E[h_j(X)h_k(Y)]=\mathbf1_{j=k}c^k.
\]
Differentiating the generating function gives
\(h_k'=\sqrt k\,h_{k-1}\) and
\(xh_j-h_j'=\sqrt{j+1}\,h_{j+1}\).

For completeness, these orthonormal polynomials span \(L^2(\gamma)\).
Indeed, if \(g\in L^2(\gamma)\) is orthogonal to every polynomial, then
\(M(z)=\int g(x)e^{zx}\gamma(dx)\) is entire: on each compact set of complex
\(z\), Cauchy--Schwarz bounds the integrand and every differentiated integrand
by integrable Gaussian exponential moments. Every derivative of \(M\) at zero
vanishes, so \(M\) is zero. In particular the Fourier transform of the
integrable function \(g(x)(2\pi)^{-1/2}e^{-x^2/2}\) vanishes. This implies that
function is zero: convolve it with a Gaussian density of variance \(s>0\),
express that density by its Gaussian Fourier integral, and apply Fubini. Every
such convolution is zero. As \(s\downarrow0\), the convolutions converge to
the original function in \(L^1\), because translations are continuous in
\(L^1\) and the Gaussian masses outside each fixed neighborhood tend to zero.
This proves the needed Fourier uniqueness and completeness here.

Consequently, with \(a_k=\mathbb E[\phi(Z)h_k(Z)]\),
\[
\phi=\sum_{k\ge0}a_kh_k\quad\hbox{in }L^2(\gamma),\qquad
\mathbb E\phi(Z)^2=\sum_{k\ge0}a_k^2.
\]
Gaussian integration by parts yields
\[
\mathbb E[\phi'(Z)h_j(Z)]=\sqrt{j+1}\,a_{j+1}.
\]
This integration by parts does not assume an unproved boundary condition.
First insert a smooth cutoff equal to one on \([-R,R]\), supported in
\([-2R,2R]\), with derivative bounded by \(C/R\). The cutoff derivative term
tends to zero by Cauchy--Schwarz and Gaussian polynomial integrability, and
both main terms converge by the same bound. The assumptions
\(\phi,\phi'\in L^2(\gamma)\) therefore suffice. Parseval gives
\[
\mathbb E\phi'(Z)^2=\sum_{k\ge1}k a_k^2.
\]
Set \(p_k=a_k^2\). The hypotheses are exactly
\[
p_k\ge0,\qquad \sum_{k\ge0}p_k=1,\qquad
\sum_{k\ge0}k p_k=1.
\tag{1}
\]
Using the correlated Hermite identity and Cauchy--Schwarz to pass to the
\(L^2\) limit proves
\[
F(c)=\sum_{k\ge0}p_kc^k,\qquad -1\le c\le1.
\tag{2}
\]
The series converges absolutely there. Its derivative at one from the left
is \(F'(1)=\sum k p_k=1\), by monotone convergence applied to
\([1-F(c)]/(1-c)\) as \(c\uparrow1\). Thus \(F\) is precisely the probability
generating function of a nonnegative integer random variable of mean one.

Define the possibly infinite number
\[
\chi_2=\sum_{k\ge2}k(k-1)p_k=F''(1-).
\tag{3}
\]
If \(\phi''\in L^2(\gamma)\), another cutoff integration by parts and Parseval
give \(\chi_2=\mathbb E\phi''(Z)^2\). Conversely, finite \(\chi_2\) implies
this integrability: the Hermite partial sums for \(\phi'\) converge in
\(L^2(\gamma)\), and their derivatives converge in that space when the sum
in (3) is finite. On compact intervals these convergences hold in ordinary
\(L^2\), so testing against compactly supported smooth functions identifies
the second limit as the distributional derivative of \(\phi'\). Since
\(\phi\) is smooth, it is its classical second derivative. Hence (3) equals
\(\mathbb E\phi''(Z)^2\), including the possibility of infinity.

## 3. Centering rigidity and explicit nonlinear activations

Subtracting the two equations in (1) gives
\[
p_0=\sum_{k\ge2}(k-1)p_k.
\tag{4}
\]
Because \(a_0=\mathbb E\phi(Z)\), a centered activation has \(p_0=0\).
Equation (4) then forces \(p_k=0\) for every \(k\ge2\), and (1) gives
\(p_1=1\). Therefore
\[
\mathbb E\phi(Z)=0\quad\Longrightarrow\quad\phi(x)=x
\text{ or }\phi(x)=-x.
\tag{5}
\]
The equality first holds Gaussian-almost everywhere; continuity makes it hold
everywhere. More generally the same calculation proves the Gaussian Poincare
inequality \(\operatorname{Var}(g(Z))\le\mathbb E g'(Z)^2\), with equality
only for affine \(g\), whenever \(g,g'\in L^2(\gamma)\). No separate theorem
is being imported.

Thus centered smooth nonlinear activations cannot satisfy both unit conditions
with weight variance one and no separate variance/bias adjustment. The absence
of centering in the assignment materially changes feasibility.

For any integer \(r\ge2\), an entire polynomial example is
\[
\phi(x)=\sqrt{\frac{r-1}{r}}+\frac{h_r(x)}{\sqrt r},
\qquad
F(c)=\frac{r-1+c^r}{r},\qquad \chi_2=r-1.
\tag{6}
\]
Its two unit moments follow directly from Hermite orthogonality and
\(h_r'=\sqrt r\,h_{r-1}\). In particular \(\chi_2\) has no bound imposed by
the two unit conditions. Arbitrarily small positive \(\chi_2\) are also
possible: take \(p_0=p_2=\varepsilon/2\), \(p_1=1-\varepsilon\), with
\(0<\varepsilon\le1\), and \(a_k=\sqrt{p_k}\). Then \(\chi_2=\varepsilon\).

There are bounded entire examples with bounded derivatives of every order.
For any real \(t>0\), define
\[
b^2=\frac{2}{t^2(1+e^{-2t^2})},\qquad
a^2=1-\frac{\tanh(t^2)}{t^2},\qquad
\phi(x)=a+b\sin(tx),
\tag{7}
\]
taking positive square roots. Since \(0<\tanh u<u\) for \(u>0\), \(a\) is
real and positive. The Gaussian characteristic function gives
\[
\mathbb E\sin(tZ)=0,\quad
\mathbb E\sin^2(tZ)=\frac{1-e^{-2t^2}}2,\quad
\mathbb E\cos^2(tZ)=\frac{1+e^{-2t^2}}2.
\]
Substitution proves both prescribed unit moments, and
\[
\chi_2=t^2\tanh(t^2),\qquad
F(c)=1-\frac{\tanh(t^2)}{t^2}
       +\frac{\sinh(t^2c)}{t^2\cosh(t^2)}.
\tag{8}
\]
For the covariance formula, expand \(\sin(tX)\sin(tY)\) as the difference of
two cosines and use the variances \(2(1-c)\) and \(2(1+c)\) of \(X-Y\) and
\(X+Y\). These examples show that bounded activation derivatives do not
contradict noncentered criticality. They also have
\(\sup_x|\phi'(x)|=\sqrt{2/(1+e^{-2t^2})}>1\), although
\(\mathbb E\phi'(Z)^2=1\). A product of derivative supremums can consequently
grow exponentially even when the exact covariance derivative below is constant.
This observation concerns a proof bound; it does not establish exponential
growth of a typical network derivative.

Analyticity alone does not make \(\chi_2\) finite. Let
\[
\psi(x)=\int_0^x\sin(e^{u^2})\,du,\qquad
A=\mathbb E\psi'(Z)^2,\qquad B=\mathbb E\psi(Z)^2.
\]
The integrand is entire and even, so \(\psi\) is entire and odd.
Also \(|\psi(x)|\le|x|\), \(|\psi'(x)|\le1\), and \(A>0\). Strictness in
the Poincare calculation above gives \(B<A\), since \(\psi\) is not affine.
Then
\[
\phi(x)=\sqrt{1-B/A}+\psi(x)/\sqrt A
\tag{9}
\]
is entire and satisfies both unit moments, but
\(\psi''(x)=2xe^{x^2}\cos(e^{x^2})\) has infinite Gaussian second moment.
Indeed, on the positive half-line the substitution \(v=e^{x^2}\) makes that
moment a positive constant times
\[
\int_1^\infty \sqrt{\log v}\,v^{1/2}\cos^2 v\,dv=\infty.
\]
Restricting to fixed-length subintervals of successive periods where
\(\cos^2v\ge1/2\) proves the divergence. Thus this activation has
\(\chi_2=\infty\), despite bounded first derivative and at most linear growth.
In particular it is inside the elementary fixed-depth covariance-limit growth
class in Section 1. This is a substantive obstruction to any finite second-query
bound deduced from the two original moments alone.

## 4. Depth derivatives at correlation one

For all \(L\ge0\),
\[
K_L(1)=1,\qquad K_L'(1)=1.
\tag{10}
\]
If \(\chi_2<\infty\), then
\[
K_L''(1)=L\chi_2.
\tag{11}
\]
These are left derivatives at the endpoint. The chain rule gives
\(K_{\ell+1}'(1)=F'(1)K_\ell'(1)\), initialized by \(K_0'(1)=1\), and
\[
K_{\ell+1}''(1)
=F''(1)K_\ell'(1)^2+F'(1)K_\ell''(1)
=\chi_2+K_\ell''(1),
\]
initialized by zero. Finite \(\chi_2\) gives the endpoint Taylor expansions
needed for this chain rule by dominated convergence in (2). Equivalently
compose the one-sided quadratic expansions directly. If \(\chi_2=\infty\),
then \(K_L''(1)=\infty\) for every \(L\ge1\): the quadratic remainder of
\(F\) has infinite ratio to \((1-c)^2\), while every inner iterate has first
derivative one and nonnegative quadratic remainder.

For illustration at the next order, if \(\phi'',\phi'''\in L^2(\gamma)\) and
\(\chi_3=\mathbb E\phi'''(Z)^2\), repeated Hermite integration by
parts gives \(F'''(1)=\chi_3\), and the third derivative chain rule gives
\[
K_L'''(1)=L\chi_3+\frac32L(L-1)\chi_2^2.
\tag{12}
\]
Indeed the increment is \(\chi_3+3\chi_2K_\ell''(1)\); summing (11) proves
the formula. These are polynomial depth laws for the exact fixed-order
endpoint derivatives, with activation-dependent coefficients.

## 5. What “query sensitivity” follows from these identities

An exact deterministic feature realization of the covariance kernel avoids
confusing a mean-square statement with a bound on a finite random network.
Each composition in (2) again has nonnegative coefficients summing to one:
write \(K_L(c)=\sum_{k\ge0}q_{L,k}c^k\). For a unit vector \(x\), define
the feature vector in a Hilbert direct sum of tensor spaces by
\[
\Phi_L(x)=\bigoplus_{k\ge0}\sqrt{q_{L,k}}\,x^{\otimes k},
\qquad x^{\otimes0}=1.
\tag{13}
\]
Its squared norm is one and
\(\langle\Phi_L(x),\Phi_L(y)\rangle=K_L(x^\top y)\).

Let \(v\in T_xS^{d-1}=\{v:x^\top v=0\}\). The derivative of
\(x^{\otimes k}\) in direction \(v\) is a sum of \(k\) mutually orthogonal
tensor terms, so its squared norm is \(k\|v\|^2\). Summing (13) and (10)
proves
\[
\|D\Phi_L(x)[v]\|^2=\|v\|^2.
\tag{14}
\]
Existence of this Hilbert-space derivative follows by dominated convergence:
along a great circle the degree-\(k\) component has constant speed
\(\sqrt k\|v\|\), which bounds its difference quotients, and
\(\sum kq_{L,k}=1\).

For a unit tangent vector \(v\), use the unit-speed great circle
\(x(s)=x\cos s+v\sin s\). The second derivative of \(x(s)^{\otimes k}\)
at zero has a radial term \(-k x^{\otimes k}\) and a term of coefficient
two for each of the \(\binom{k}{2}\) placements of two copies of \(v\).
These terms are mutually orthogonal. Thus its squared norm is
\(k^2+4\binom{k}{2}=k+3k(k-1)\). When \(\chi_2<\infty\), summing gives
\[
\left\|\frac{d^2}{ds^2}\Phi_L(x(s))\bigg|_{s=0}\right\|^2
=1+3L\chi_2.
\tag{15}
\]
The same expression bounds the difference quotients of the first derivative
componentwise, using their integral formula and the constant second-derivative
norm along the great circle. Dominated convergence therefore also justifies
existence of the second derivative in the Hilbert space. If \(\chi_2=\infty\),
no such Hilbert-space second derivative
can exist for \(L\ge1\), since its finite-degree projections already have
unbounded squared derivative norms.

For completeness, let \(\nabla_S^2\Phi_L(x)[v,w]\) denote the Riemannian
Hessian on the unit sphere, evaluated on tangent vectors \(v,w\). Its full
bilinear norm identity is
\[
\|\nabla_S^2\Phi_L(x)[v,w]\|^2
=L\chi_2\|v\|^2\|w\|^2
 +(1+2L\chi_2)(v^\top w)^2.
\tag{16}
\]
To verify the associated covariance tensor without assuming it, expand the
inner product of the great-circle features in two variables. For tangent
\(v,w\), the coefficient of \(s^2t^2\) in their input inner product is
\(\|v\|^2\|w\|^2/4\), the coefficient of \(st\) is \(v^\top w\), and
the pure quadratic coefficients are \(-\|v\|^2/2\) and
\(-\|w\|^2/2\). Differentiating \(K_L\) consequently gives
\[
\langle\nabla_S^2\Phi_L[v,v],\nabla_S^2\Phi_L[w,w]\rangle
 =(1+L\chi_2)\|v\|^2\|w\|^2+2L\chi_2(v^\top w)^2.
\]
Polarization in the two tangent slots gives the four-linear tensor
\((1+L\chi_2)\delta_{ij}\delta_{kl}
+L\chi_2(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})\)
in any orthonormal tangent basis, and setting its slots to \((v,w,v,w)\)
gives (16).

Thus the feature-map first tangent derivative has operator norm exactly one,
and its second tangent derivative has bilinear operator norm
\(\sqrt{1+3L\chi_2}\) whenever the tangent space is nonzero. In dimension
\(d=1\) the sphere consists of two isolated points and has no nonzero tangent
directions; the tangent statements are then vacuous. If \(f_L\) is the
centered Gaussian process with this covariance, the same formulas give the
variances of its mean-square first and second tangent derivatives. For example,
\(\mathbb E[(d^2 f_L(x(s))/ds^2|_0)^2]=1+3L\chi_2\).

For a scalar feature-space function \(f(x)=\langle u,\Phi_L(x)\rangle\),
Cauchy--Schwarz further gives the uniform bounds
\[
|D f(x)[v]|\le\|u\|\|v\|,\qquad
|\nabla_S^2f(x)[v,w]|
\le\|u\|\sqrt{1+3L\chi_2}\,\|v\|\|w\|.
\tag{17}
\]
A sample of an infinite-dimensional Gaussian process need not correspond to a
finite-norm \(u\); (17) is not asserted for it with an implicit unit norm.

These formulas concern tangent queries on the unit sphere. They do not bound
ambient radial derivatives of the actual network: those change the marginal
preactivation variances and require differentiating a two-variance covariance
map, not just \(F(c)\). Nor do they bound a finite-width network's random
Jacobian or Hessian uniformly over its Gaussian weights. Unbounded Gaussian
weight support already precludes deterministic finite uniform bounds even at
one layer. Training also changes the law used in the normalization moments.

## 6. A finite input Gram gap loses only a polynomial factor when chi2 is finite

Let \(x_1,\ldots,x_m\) be unit inputs, and define symmetric matrices
\[
C_0=(x_a^\top x_b)_{a,b=1}^m,\qquad
C_L=(K_L(x_a^\top x_b))_{a,b=1}^m.
\]
Assume \(\gamma_0=\lambda_{\min}(C_0)>0\). Since its trace is \(m\),
\(0<\gamma_0\le1\). Let the scalar sequence \(\eta_L\) be
\[
\eta_0=\gamma_0,\qquad
\eta_{L+1}=1-F(1-\eta_L).
\tag{18}
\]
Then, without assuming finite \(\chi_2\),
\[
C_L\succeq\eta_L I,\qquad
\eta_L=1-K_L(1-\gamma_0)>0.
\tag{19}
\]

Here is the complete matrix argument. If a correlation matrix \(C\) obeys
\(C\succeq\eta I\), set \(B=C-\eta I\succeq0\); its diagonal is
\(1-\eta\). For each integer \(k\ge1\), the entrywise powers satisfy
\[
C^{\circ k}=B^{\circ k}+[1-(1-\eta)^k]I.
\]
Every \(B^{\circ k}\) is positive semidefinite: factor \(B\) as a Gram
matrix of vectors \(b_a\), then it is the Gram matrix of \(b_a^{\otimes k}\).
For \(k=0\), the entrywise zeroth power is by definition the all-ones matrix
\(J\), also positive semidefinite. Sum with weights \(p_k\) to obtain
\[
F[C]=\sum_{k\ge0}p_k B^{\circ k}+[1-F(1-\eta)]I
\succeq[1-F(1-\eta)]I.
\]
Convergence follows entrywise and hence in matrix norm, since
\(|B_{ab}|\le1-\eta\le1\) and \(\sum p_k=1\). The notation \(F[C]\)
means apply \(F\) to each entry. This matrix is again a correlation matrix.
Induction proves (19); strict positivity holds since (1) puts positive mass
on positive integers and \(1-\eta<1\).

If \(\chi_2<\infty\), (19) has the useful explicit bound
\[
\lambda_{\min}(C_L)\ge\eta_L
\ge\frac{\gamma_0}{1+L\chi_2\gamma_0}.
\tag{20}
\]
For \(0<\eta\le1\) and integer \(k\ge1\),
\[
1-(1-\eta)^k\ge\frac{k\eta}{1+(k-1)\eta}.
\]
For \(\eta<1\), this follows from
\((1-\eta)^{-(k-1)}\ge1+(k-1)\eta\), which follows by integrating its
derivative lower bound \(k-1\); the endpoint \(\eta=1\) is immediate.
The weights \(k p_k\), \(k\ge1\), sum to one by (1). The convexity of
\(s\mapsto(1+s)^{-1}\), or its supporting line at the weighted mean, gives
\[
1-F(1-\eta)
\ge\eta\sum_{k\ge1}\frac{k p_k}{1+(k-1)\eta}
\ge\frac{\eta}{1+\chi_2\eta}.
\]
The supporting-line proof works for the countable sum because its mean
\(\chi_2\eta\) is finite. Thus
\(1/\eta_{L+1}\le1/\eta_L+\chi_2\); iteration proves (20).
In particular
\[
\|C_L^{-1}\|_{\mathrm{op}}\le\gamma_0^{-1}+L\chi_2.
\tag{21}
\]
This is a population feature Gram bound with explicit activation and initial
data dependence, not a sample-complexity statement.

The polynomial depth order is sharp for every fixed nonlinear activation with
finite \(\chi_2\), and every fixed positive-definite input Gram matrix with
\(m\ge2\):
\[
\lambda_{\min}(C_L)\sim\frac{2}{\chi_2L}
\quad\text{as }L\to\infty.
\tag{22}
\]
Here \(\chi_2>0\) for every nonlinear activation by (3)--(5). To prove (22),
first use (1) and (4) to write, for \(-1\le c\le1\),
\[
F(c)-c=\sum_{k\ge2}p_k[(k-1)-kc+c^k].
\]
For each \(k\ge2\), the bracket vanishes at one and has derivative
\(k(c^{k-1}-1)\le0\) on this interval. It is strictly positive for
\(-1\le c<1\), because the derivative is strictly negative at every point
in \((-1,1)\). Hence a nonlinear \(F\) satisfies \(F(c)>c\) for \(c<1\).
Also \(|c|<1\) implies \(F(c)<1\), since positive mass occurs at positive
degrees and \(|c|^k<1\). Iteration from such a \(c\) therefore increases to
the only possible fixed point, one.

Set \(\delta_L=1-K_L(c)\) for fixed \(|c|<1\). Finite \(\chi_2\) gives
\[
\delta_{L+1}
=\delta_L-\frac{\chi_2}{2}\delta_L^2+o(\delta_L^2),
\]
so \(\delta_{L+1}/\delta_L\to1\) and
\[
\frac1{\delta_{L+1}}-\frac1{\delta_L}
=\frac{\delta_L-\delta_{L+1}}{\delta_L\delta_{L+1}}
\longrightarrow\frac{\chi_2}{2}.
\]
Averaging these increments yields \(L\delta_L\to2/\chi_2\). Positive
definiteness of \(C_0\) forces \(|(C_0)_{ab}|<1\) for \(a\ne b\), by its
two-by-two principal minors. There are only finitely many such pairs, so
entrywise, and hence in operator norm,
\[
C_L=J+\frac{2}{\chi_2L}(I-J)+o(L^{-1}).
\]
The displayed comparison matrix has eigenvalues
\(m-(m-1)2/(\chi_2L)\) on the constant vector and \(2/(\chi_2L)\) on its
orthogonal complement. The difference in each minimum Rayleigh quotient is
bounded by the operator norm of the error. Since \(m\ge2\), this proves
(22). If the activation is linear, \(F(c)=c\) and \(C_L=C_0\) instead. If
\(m=1\), the minimum eigenvalue is always one.

Even if \(\chi_2=\infty\), exponential asymptotic collapse is excluded for
this fixed-activation covariance recursion and positive-definite input Gram
matrix. From \(F'(1)=1\), the sequence (18) has
\(\eta_{L+1}/\eta_L\to1\) in the nonlinear case. Consequently
\(L^{-1}\log\eta_L\to0\), by averaging its logarithmic increments.
Using (19) and \(\lambda_{\min}(C_L)\le1\) gives
\[
\lim_{L\to\infty}\frac1L\log\lambda_{\min}(C_L)=0.
\tag{23}
\]
No explicit polynomial bound uniform over the allowed activations follows
from the present proof when \(\chi_2\) is infinite; the finite second-query
bound already fails in (9).

A positive input gap is a real assumption. For example, choose even \(r\)
in (6) and the antipodal pair \(x,-x\). Their input Gram gap is zero, and
\(F(-1)=1\), so their two feature vectors coincide after one layer and the
feature Gram gap remains zero. The normalization conditions cannot supply a
missing input nondegeneracy condition.

## 7. Meaning, limitations, and the exponential-versus-polynomial question

For a fixed activation with finite \(\chi_2\), the exact initialization
covariance model has first tangent feature sensitivity one, second tangent
feature sensitivity of order \(\sqrt L\), second correlation derivative
\(L\chi_2\), and inverse finite-data Gram norm bounded by
\(\gamma_0^{-1}+L\chi_2\). These objects therefore do not themselves force
an exponential depth constant. Merely multiplying \(\sup|\phi'|\) or a
one-step Gram-gap contraction misses the critical covariance structure.

This does not justify replacing any exponential constant in an unrelated
estimate with a polynomial. A proof must identify its actual query objects,
norm, width limit, activation derivative requirements, probability level,
parameter perturbations, and training horizon, then establish the appropriate
comparison. In particular these calculations do not control finite-width
operator-norm products, uniform concentration over a large query family,
radial derivatives, trained non-Gaussian laws, higher response-memory
derivatives, or accumulated approximation errors in an autonomous closure.
The assignment supplied none of those systems or estimates, so I did not
infer their definitions or import sources about them.

## 8. Executed checks and freeze record

Before writing, I checked shared HEAD, tracked-worktree status, and staged
paths. HEAD was `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`; the index was empty.
Concurrent tracked changes in two unowned paths were observed as metadata and
were not read or modified. This file is the only written artifact for this route.

I executed the following deterministic numerical sanity check from the checkout
root using Python and NumPy 1.26.4, with exit status zero. Its purpose was to
check signs, the explicit bound, and the asymptotic constant against the exact
polynomial covariance maps, not to replace the proofs. It makes no files and
uses fixed seed 1947. All assertions passed.

```python
import math
import numpy as np
rng = np.random.default_rng(1947)
x = rng.normal(size=(5, 9))
x /= np.linalg.norm(x, axis=1)[:, None]
c0 = x @ x.T
np.fill_diagonal(c0, 1.0)
gamma = float(np.linalg.eigvalsh(c0)[0])
for r in (2, 3, 11):
    c = c0.copy()
    scalar = gamma
    for ell in range(1, 10001):
        c = (r - 1 + c**r) / r
        np.fill_diagonal(c, 1.0)
        scalar = (-math.expm1(r * math.log1p(-scalar)) / r
                  if scalar < 1 else 1 / r)
        if ell in (1, 10, 100, 1000, 10000):
            gap = float(np.linalg.eigvalsh(c)[0])
            lower = gamma / (1 + ell * (r - 1) * gamma)
            assert gap >= scalar - 2e-12
            assert scalar >= lower - 2e-12
for t in (0.1, 1.0, 3.0):
    b2 = 2 / (t*t * (1 + math.exp(-2*t*t)))
    a2 = 1 - math.tanh(t*t) / (t*t)
    second_moment = a2 + b2 * (1 - math.exp(-2*t*t)) / 2
    derivative_moment = b2 * t*t * (1 + math.exp(-2*t*t)) / 2
    chi2 = b2 * t**4 * (1 - math.exp(-2*t*t)) / 2
    assert abs(second_moment - 1) < 1e-13
    assert abs(derivative_moment - 1) < 1e-13
    assert abs(chi2 - t*t * math.tanh(t*t)) < 1e-13
```

The initial eigenvalue was `0.267140694691`. At depth 10,000, the minimum
eigenvalues for \(r=2,3,11\) were respectively `0.000199743399`,
`0.0000999216074`, and `0.0000199907837`; the ratios to
\(2/((r-1)L)\) were `0.998716997`, `0.999216074`, and `0.999539187`.
Every checked gap exceeded both the exact scalar bound (19) and the explicit
bound (20), up to the stated numerical tolerance. The three sine examples
satisfied their exact two moments to floating-point tolerance, with
\(\chi_2\) approximately `0.0000999966668`, `0.761594156`, and `8.999999726`.

The persisted proofs were manually checked for centering, the linear and
single-query cases, antipodal degeneracy, endpoint derivatives, infinite
\(\chi_2\), sphere-versus-radial derivatives, and the order of limits. This is
an author check of a scoped route, not an independent promotion audit.
The immutable candidate's SHA-256 is reported to the supervisor separately
after writing, so the content can be frozen before any cross-route exposure.
