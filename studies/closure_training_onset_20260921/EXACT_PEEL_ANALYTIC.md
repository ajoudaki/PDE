# Exact analytic peeling candidate

Status: independently derived, exact continuum extension; the strict finite Gaussian-terminal target remains unachieved. This note uses only the assigned definitions. It neither proves nor asserts that the strict target is impossible.

The construction below removes every nested occurrence of `tanh`, including those in the coefficients. Its price is an explicit integration over the bounded values of the inner activation. A Gaussian Stein identity identifies the coefficient row exactly, and a covariance differentiation identity records what direct Gaussian peeling produces before this change of variables.

## 1. Setup and allowed terminals

Write \(\sigma=\tanh\), \(\eta=1/4096\), and retain the assigned definitions

\[
v=\mathbb E\sigma(G)^2,\qquad
\tau=\mathbb E\sigma(\sqrt vG)^2,\qquad
\alpha=1-\tau.
\]

Both \(v\) and \(\tau\) lie strictly between zero and one. For \(q>0\) and \(-1<u<1\), define the explicit density

\[
p_q(u)=\frac{\exp\{-\operatorname{arctanh}(u)^2/(2q)\}}
 {\sqrt{2\pi q}\,(1-u^2)},
\qquad
\operatorname{arctanh}(u)=\frac12\log\frac{1+u}{1-u}.
\tag{1}
\]

It is the density of \(\sigma(\sqrt qG)\). In particular it integrates to one. Endpoint values may be set to zero: the quadratic decay in \(\log(1/(1-|u|))\) dominates the reciprocal factor in (1).

For a mean vector \(m\in\mathbb R^2\) and positive semidefinite covariance \(C\), use only the original-activation Gaussian terminal

\[
T(m,C)=\mathbb E[\sigma(Y_1)\sigma(Y_2)],\qquad
(Y_1,Y_2)\sim N(m,C).
\tag{2}
\]

Also set

\[
M(t,q)=\mathbb E\sigma(t+\sqrt qW),\qquad
D(t,q)=\mathbb E\sigma'(t+\sqrt qW),\quad q\geq0.
\tag{3}
\]

These are abbreviations for Gaussian expectations of the original activation or derivative, not new terminal nonlinearities. Degenerate Gaussian covariances are included: \(T(m,0)=\sigma(m_1)\sigma(m_2)\), \(M(t,0)=\sigma(t)\), and \(D(t,0)=\sigma'(t)\). Every covariance used below is specified explicitly. The additional non-Gaussian weight is exactly (1); it uses logarithm, exponential, and arithmetic, with no unevaluated nested activation or nested expectation.

## 2. Flattening all coefficients

For \(\rho\in[-1,1]\), the assigned scalar coefficients have the exact representations

\[
\begin{aligned}
\beta
 &=\int_{-1}^{1}u\,p_1(u)M(\alpha u,\tau)\,du,\\
s
 &=\int_{-1}^{1}p_1(u)
 T\!\left(
 \binom{\alpha u}{\alpha u},
 \tau\begin{pmatrix}1&1\\1&1\end{pmatrix}
 \right)du,\\
\gamma
 &=\int_{-1}^{1}p_1(u)D(\alpha u,\tau)\,du,\\
A(\rho)
 &=T\!\left(
 \binom00,\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}
 \right),\\
B(\rho)
 &=\int_{-1}^{1}p_1(u)
 T\!\left(
 \binom{\alpha u}{\rho\operatorname{arctanh}(u)},
 \begin{pmatrix}\tau&0\\0&1-\rho^2\end{pmatrix}
 \right)du.
\end{aligned}
\tag{4}
\]

The formula for \(\gamma\) agrees with \(1-s\), since \(\sigma'=1-\sigma^2\). To prove (4), put \(u=\sigma(G)\). Then \(G=\operatorname{arctanh}(u)\), its transformed density is \(p_1\), and the conditional Gaussian variables \(Z,V\) remain independent. The two arguments in the formula for \(B\), conditionally on \(u\), have exactly the displayed means and diagonal covariance. The formula for \(s\) uses two identical copies of its single argument, hence its rank-one covariance.

For explicit finite arithmetic after these integrations, set

\[
\begin{aligned}
\Delta&=(v+\eta)(s+\eta)-\beta^2,\\
c_1&=\frac{\alpha v(s+\eta)-\beta(\alpha\beta+\tau\gamma)}
 {(\tau+\eta)\Delta},\\
c_2&=\frac{\alpha\eta\beta+(v+\eta)\tau\gamma}
 {(\tau+\eta)\Delta}.
\end{aligned}
\tag{5}
\]

Then

\[
\Lambda(\rho)=c_1A(\rho)+c_2B(\rho),\qquad
a_\theta=\Lambda(\cos\theta),\quad
b_\theta=\Lambda(\sin\theta).
\tag{6}
\]

Cauchy–Schwarz gives \(\beta^2\leq vs\), so

\[
\Delta\geq\eta(v+s)+\eta^2>0.
\]

Thus every denominator in (5) is positive. No inverse matrix or coefficient in (5) conceals an additional nonlinear expectation.

There is no endpoint exception in (4). At \(\rho=\pm1\), the second Gaussian variance in \(B\) is zero, and
\(\sigma(\pm\operatorname{arctanh}(u))=\pm u\). Consequently

\[
B(1)=\beta,\quad B(-1)=-\beta,\quad B(0)=0,
\qquad
A(1)=v,\quad A(-1)=-v,\quad A(0)=0.
\tag{7}
\]

The logarithmic means diverge only at the integration endpoints, where the terminal remains bounded and no point evaluation is needed.

## 3. Exact nested-activation-free formula for the target

For every real \(\theta,\psi\),

\[
\begin{aligned}
K(\theta,\psi)
={}&\int_{-1}^{1}\int_{-1}^{1}
p_v(u)p_v(w)\\[-2mm]
&\quad\times T\!\left(
\binom{a_\theta u+b_\theta w}{a_\psi u+b_\psi w},
\begin{pmatrix}0&0\\0&0\end{pmatrix}
\right)\,du\,dw.
\end{aligned}
\tag{8}
\]

Equivalently, the terminal in (8) is simply
\(\sigma(a_\theta u+b_\theta w)\sigma(a_\psi u+b_\psi w)\).
This is a two-dimensional, absolutely convergent, exact no-series integral. Together, (1), (4)–(6), and (8) form a complete flattened formula for the assigned quantity.

To verify (8), the independent variables
\(U=\sigma(\sqrt vX_1)\) and \(W=\sigma(\sqrt vX_2)\)
have product density \(p_v(u)p_v(w)\). Substitute this density into the assigned expectation. Every outer activation now has an affine argument in deterministic integration variables; no occurrence of \(\sigma\) remains inside another activation argument. Every remaining Gaussian expectation in (4) evaluates only the original \(\sigma\) or \(\sigma'\) at a Gaussian affine argument.

All claims of absolute convergence follow directly from

\[
|\sigma|\leq1,\quad 0<\sigma'\leq1,
\quad \int_{-1}^1p_q(u)\,du=1.
\]

The extra factor \(u\) in \(\beta\) also has absolute value at most one. These bounds justify conditioning and interchanging the integrations and Gaussian expectations in (4) and (8), including at \(\rho=\pm1\). They also give \(|K|\leq1\), \(|A|\leq v\), and \(|B|\leq\sqrt{vs}\). Together with (5), they establish that all affine arguments in (8) have finite coefficients.

Formula (8) uses a degenerate Gaussian only to keep the terminal convention (2) uniform. It does not claim to replace the transformed probability density by a Gaussian probability density. If the requested class requires strictly positive definite covariances, the direct deterministic-product form of (8) should be used and classified as an explicit enlargement of that class.

## 4. What exact Gaussian Stein calculus gives

First, the special coefficient row has a useful exact interpretation. Put

\[
H=\sqrt\tau Z+\alpha\sigma(G),\qquad k=\sigma(H).
\]

Gaussian integration by parts in \(Z\) gives

\[
\mathbb E[H\sigma(G)]=\alpha v,\qquad
\mathbb E[Hk]
=\alpha\beta+\sqrt\tau\,\mathbb E[Z\sigma(H)]
=\alpha\beta+\tau\gamma.
\tag{9}
\]

Indeed, \(\partial_Z\sigma(H)=\sqrt\tau\sigma'(H)\) is bounded, so the Gaussian integration by parts has no boundary term, and \(\mathbb E\sigma'(H)=1-s\). Thus the numerator row of \(\Lambda\) is exactly the covariance of \(H\) with the two features \((\sigma(G),k)\). This explains that row but does not cancel its dependence on \(B\).

An exact covariance peeling identity is also available. For \(x\in\mathbb R^2\), define

\[
L_\theta(x)=a_\theta\sigma(\sqrt vx_1)
             +b_\theta\sigma(\sqrt vx_2),\qquad
F_\theta(x)=\sigma(L_\theta(x)).
\]

Let \(X,Y\) be independent standard Gaussian vectors in \(\mathbb R^2\), and for \(0\leq r\leq1\) put
\(X^{(r)}=rX+\sqrt{1-r^2}Y\). The joint covariance of \((X,X^{(r)})\) is

\[
\begin{pmatrix}I_2&rI_2\\rI_2&I_2\end{pmatrix}.
\]

Then

\[
\begin{aligned}
K(\theta,\psi)
={}&v\int_0^1\mathbb E\bigg[
\sigma'(L_\theta(X))\sigma'(L_\psi(X^{(r)}))\\
&\quad\times\Big\{
a_\theta a_\psi\sigma'(\sqrt vX_1)
                         \sigma'(\sqrt vX^{(r)}_1)
+b_\theta b_\psi\sigma'(\sqrt vX_2)
                         \sigma'(\sqrt vX^{(r)}_2)
\Big\}\bigg]dr.
\end{aligned}
\tag{10}
\]

For completeness, set \(J(r)=\mathbb E[F_\theta(X)F_\psi(X^{(r)})]\). For \(0<r<1\), differentiation and Gaussian integration by parts give

\[
\begin{aligned}
J'(r)
&=\sum_{j=1}^2\mathbb E\left[
F_\theta(X)\partial_jF_\psi(X^{(r)})
\left(X_j-\frac r{\sqrt{1-r^2}}Y_j\right)\right]\\
&=\mathbb E[\nabla F_\theta(X)\cdot\nabla F_\psi(X^{(r)})].
\end{aligned}
\]

The second-derivative terms from the two integrations by parts cancel. All derivatives involved are bounded, so differentiation is justified on compact subintervals of \((0,1)\). The resulting derivative has the uniform bound

\[
|J'(r)|\leq v\bigl(|a_\theta a_\psi|+|b_\theta b_\psi|\bigr).
\]

Dominated convergence supplies the endpoint limits. Since \(F_\theta\) and \(F_\psi\) are odd under simultaneous sign reversal of both coordinates, their means are zero; hence \(J(0)=0\) and \(J(1)=K(\theta,\psi)\). Integrating \(J'\) and substituting the two gradient components proves (10), with an absolutely convergent interpolation integral.

Equation (10) is an exact Gaussian Stein/peeling identity, but it is not a completed reduction to the proposed finite terminal class: its outer derivatives still have the composed arguments \(L_\theta,L_\psi\). Applying (1) jointly to the correlated coordinate pairs would flatten (10) as well, but increases the integration dimension and gives no simplification over (8).

## 5. Precise residual and a limited obstruction

The original strict target allows a finite arithmetic combination of finitely many Gaussian expectations of products of original activation derivatives at affine Gaussian arguments. Formula (8) adds a two-dimensional continuum integral, and (4) adds one-dimensional continuum integrals. These integrations have not been evaluated as finitely many allowed Gaussian terminals. The transformed density (1) is an explicitly declared extra weight. Thus the result is a complete exact no-series continuum representation, not a solution of the strict finite problem and not a disguised nested expectation.

There is a limited reason that a direct finite *pointwise algebraic* peeling is unavailable. For fixed real \(a\ne0\), the function \(\tanh(a\tanh z)\) cannot equal a finite arithmetic expression in derivatives of \(\tanh\) at affine arguments in \(z\), with constant coefficients. Every expression of the latter kind is meromorphic on the complex plane, with no finite accumulation point of poles. In contrast, taking the sign of the integers so that \(\pi(n+1/2)/a\to+\infty\), the points

\[
z_n=i\arctan\!\left(\frac{\pi(n+1/2)}a\right)
\longrightarrow i\pi/2
\]

are poles of \(\tanh(a\tanh z)\). They are genuine poles because the inner derivative is nonzero there and the outer poles are simple. Equality on the real line would, by analytic continuation in the strip \(|\operatorname{Im}z|<\pi/2\), force the same poles for the proposed meromorphic expression, contradicting their finite accumulation point. This argument applies to the narrowly described pointwise arithmetic route. Gaussian integration can create additional identities, so it is not an impossibility proof for the much broader finite expectation target.

The exact unresolved step is therefore an elimination of the explicit continuum integrations in (4) and (8), or another identity bypassing them while keeping every Gaussian terminal affine in the original \(\sigma\) and its derivatives. No such elimination is established here.
