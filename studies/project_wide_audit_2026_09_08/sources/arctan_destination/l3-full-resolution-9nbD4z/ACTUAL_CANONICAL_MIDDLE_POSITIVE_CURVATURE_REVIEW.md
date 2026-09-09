# Independent adversarial reconstruction of the two-note scoped theorem

Verdict: **PASS for the complete two-note scoped theorem, with the quantifiers and exclusions stated below.** No mathematical correction to either frozen candidate is required. This verdict includes the initial empirical law for every continuous test of at most quadratic growth, its probability and \(L^1\) conclusions, strict positivity, the actual canonical feature-time estimates, unconditional expectations, and the positive fraction of scalar middle curvature coefficients. It certifies no larger theorem.

## Provenance and isolation

The two proof inputs were read completely and their SHA256 hashes independently verified:

1. GAUSSIAN_MIDDLE_CURVATURE_INITIAL_LAW.md, 468 lines:
   e028b6146db23f21ba0b35a876e997ff20d89ab3da8edcaa8f3e11e7db1417bb
2. ACTUAL_CANONICAL_MIDDLE_POSITIVE_CURVATURE.md, 422 lines:
   9f0b1a3c6cc334e533e0623d5d2e15413324037f7887914874f08e91a320a23e

Both are in /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/. The solve-math-rigorously skill at /etc/codex/skills/solve-math-rigorously/SKILL.md was read completely before the inputs. It supplied the review method, not a mathematical premise. No ledger, other proof note, previous review, prior mathematical conversation, external source, or experiment was used. Neither candidate was edited.

Equation references below identify their source as “initial note” or “dynamical note.” The reconstruction supplies the reasoning needed to evaluate those equations independently.

## 1. Exact scope and model

Set \(c=\pi/2\) and \(\phi(x)=\arctan x\). All vector norms are ordinary Euclidean norms; matrix norms are ordinary operator or Frobenius norms. Factors \(n^{-1}\) and \(n^{-1/2}\) are written explicitly. A superscript \(T\) denotes finite-dimensional transpose. Every horizon used below is finite, \(0<S<\infty\).

The first trained layer is the vector \(z^{(1)}=W^{(1)}\in\mathbb R^n\). The matrices \(W^{(2)},W^{(3)}\) are \(n\) by \(n\), and \(W^{(4)}\in\mathbb R^n\) is the rescaled readout. The initial variables are mutually independent, with
\[
z_i^{(1)}(0)\sim N(0,1),\qquad
W_{ij}^{(\ell)}(0)\sim N(0,1/n)\quad(\ell=2,3),\qquad
W_i^{(4)}(0)=G_i^{(4)}/n,\quad G_i^{(4)}\sim N(0,1).
\]
Thus the rescaled readout variance is exactly \(1/n^2\). The forward variables and backward factors are
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}).
\]
The scalar map \(\tau:\mathbb R\to\mathbb R\) is applied coordinatewise, is fixed throughout a trajectory, satisfies \(\tau(0)=0\), and has Lipschitz constant at most one. These conditions are equivalent to the two clipping inequalities in the dynamical note. They include the identity. There is no pruning mask and no loss residual inside either \(\delta\).

The feature equations being certified are exactly
\[
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)},\quad
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,
\]
\[
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\qquad
(W^{(4)})'=h^{(3)}.
\]
All dynamical conclusions refer to these equations in feature time \(s\). The separate scalar factor \(2(1-f)\) mentioned for physical time, where \(f=(W^{(4)})^Th^{(3)}/n\), is never used to transfer an interval or a limit.

The initial conclusion concerns empirical pairs \((z_{0,i}^{(2)},u_{n,i}^{(2)})\). “Every continuous quadratic-growth test” means that each fixed such test has the stated convergence in probability and \(L^1\). It does not mean an unrestricted supremum over tests or almost-sure convergence simultaneously for an uncountable test family.

The positive-interval quantifiers are: there exists a deterministic \(s_0>0\) such that, for every fixed \(a\in(0,s_0]\), sufficiently large widths admit a measurable event of probability tending to one on which all allowed fixed clippings and every \(s\in[a,s_0]\) satisfy the asserted bounds. The initial data, event, \(c_n\), \(s_0\), and constants are shared across clippings. The required width threshold can depend on \(a\).

## 2. Reconstruction of the original reused-Gaussian initial law

Write
\[
g(x)=\phi'(x)\phi(x),\qquad
u_n^{(2)}=(W_0^{(3)})^Tg(z_0^{(3)}),\qquad
m_{\ell,n}=\|h_0^{(\ell)}\|^2/n\quad(\ell=1,2).
\]
The elementary estimates used in the reconstruction are
\[
|\phi|\le c,\quad |\phi(x)|\le |x|,\quad 0<\phi'\le1,\quad
\phi''(x)=-\frac{2x}{(1+x^2)^2},\quad |\phi''|\le2,
\]
\[
|g|\le c,\quad |g(x)|\le |x|,\quad
0\le xg(x)\le x^2,\quad |xg(x)|\le c/2.
\]
Both \(\phi\) and \(g\) vanish exactly at zero.

### Conditional law and the meaning of the auxiliary Gaussian

Almost surely \(m_{1,n}>0\). Conditional on the first layer, the coordinates of \(z_0^{(2)}\) are independent \(N(0,m_{1,n})\), so \(m_{2,n}>0\) almost surely. Conditional on the lower layers, the coordinates of \(z_0^{(3)}\) are independent \(N(0,m_{2,n})\).

For fixed nonzero \(h_0^{(2)}\), put
\[
P_n^{(2)}=\frac{h_0^{(2)}(h_0^{(2)})^T}{\|h_0^{(2)}\|^2}.
\]
For each row of the original \(W_0^{(3)}\),
\[
(W_0^{(3)})_{j,:}^T
=\frac{h_0^{(2)}z_{0,j}^{(3)}}{\|h_0^{(2)}\|^2}
 +(I-P_n^{(2)})(W_0^{(3)})_{j,:}^T.
\]
The residual has covariance \((I-P_n^{(2)})/n\); its covariance with \(z_{0,j}^{(3)}\) is
\[
\frac1n(I-P_n^{(2)})h_0^{(2)}=0.
\]
The joint conditional distribution is Gaussian, so its characteristic function factors across these two components. Residuals in different rows remain independent. Independence of \(W_0^{(3)}\) from all lower variables justifies conditioning on the full lower-layer data, rather than only on \(h_0^{(2)}\).

Consequently, conditional on the lower-layer variables and the entire vector \(z_0^{(3)}\), the mean and covariance of the original query are exactly
\[
\beta_n h_0^{(2)},\qquad \sigma_n^2(I-P_n^{(2)}),
\]
where
\[
\beta_n=\frac{(z_0^{(3)})^Tg(z_0^{(3)})}{n m_{2,n}},
\qquad \sigma_n^2=\frac{\|g(z_0^{(3)})\|^2}{n}.
\]
This proves the conditional-law representation
\[
u_n^{(2)}\overset{\mathrm{law}}=
\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi,
\qquad \xi\sim N(0,I_n),
\]
with \(\xi\) independent of the conditioning variables. It retains both the conditional mean caused by matrix reuse and the residual projection.

On the null event \(h_0^{(2)}=0\), the original \(z_0^{(3)}\), \(g(z_0^{(3)})\), and \(u_n^{(2)}\) are zero. The stated conventions \(\beta_n=0\), \(P_n^{(2)}=0\), and \(\sigma_n=0\) therefore handle the zero denominator correctly. The case \(n=1\) is covered: for nonzero \(h_0^{(2)}\), \(I-P_n^{(2)}=0\).

An exact construction of the relevant joint law draws the original first layer and mutually independent standard Gaussian vectors \(\eta,\zeta,\xi\), independent also of that layer, then sets
\[
z_0^{(2)}=\sqrt{m_{1,n}}\,\eta,\quad
z_0^{(3)}=\sqrt{m_{2,n}}\,\zeta,\quad
u_n^{(2)}=\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi.
\]
Successive conditional laws prove equality in distribution with the original quadruple \((z_0^{(1)},z_0^{(2)},z_0^{(3)},u_n^{(2)})\). This construction is used only to prove claims about that quadruple. It does not assert preservation of an independently supplied joint coupling with every matrix observable, and none is needed later: combining the \(c_n\) event with the matrix-norm event uses a union bound, not independence.

The vectors \(\eta,\zeta,\xi\), and eventually the scalar \(G\), describe this distributional reconstruction. They do not change the actual initialization, introduce a new network readout, or assert independence of the original reused coordinate pairs.

### Random variances, ratios, and projection removal

Let \(G_1,G_2,G_3,G\) be mutually independent scalar standard Gaussians used to define the population quantities. The functions
\[
q\longmapsto\mathbb E\phi(\sqrt q\,G)^2,\quad
q\longmapsto\mathbb E[\sqrt q\,G\,g(\sqrt q\,G)],\quad
q\longmapsto\mathbb E g(\sqrt q\,G)^2
\]
are continuous on \([0,c^2]\). The respective uniform integrand bounds \(c^2,c/2,c^2\) prove this by dominated convergence, including at zero.

The variance of an average of independent identically distributed variables is the individual variance divided by \(n\). Applying this first to the bounded first layer and then conditionally at successive layers gives
\[
m_{1,n}\to m_1=\mathbb E\phi(G_1)^2,\qquad
m_{2,n}\to m_2=\mathbb E\phi(Z^{(2)})^2
\]
in probability, with the first convergence also in \(L^2\). For the second convergence, the conditional expectation of \(m_{2,n}\) is the first displayed continuous function evaluated at \(m_{1,n}\), and the conditional variance is at most \(c^4/n\). Here
\[
Z^{(2)}=\sqrt{m_1}G_2,\qquad Z^{(3)}=\sqrt{m_2}G_3.
\]
For the numerator \(n^{-1}(z_0^{(3)})^Tg(z_0^{(3)})\), the conditional variance is at most \(c^2/(4n)\). For \(\sigma_n^2\), it is at most \(c^4/n\). Hence
\[
\beta_n\to\beta=\frac{\mathbb E[Z^{(3)}g(Z^{(3)})]}{m_2},
\qquad
\sigma_n\to\sigma=\sqrt{\mathbb E g(Z^{(3)})^2}
\]
in probability. Nondegeneracy successively gives \(m_1,m_2,\sigma>0\). Since \(0<xg(x)\le x^2\) off zero, \(0<\beta\le1\).

Division is justified on \(m_{2,n}\ge m_2/2\), an event whose probability tends to one. No finite-width deterministic lower bound or inverse-variance moment is assumed.

Conditional on \(h_0^{(2)},z_0^{(3)}\), the projection has rank one and
\[
\mathbb E\left[\frac{\|\sigma_nP_n^{(2)}\xi\|^2}{n}
 \,\middle|\,h_0^{(2)},z_0^{(3)}\right]
=\frac{\sigma_n^2}{n}\le\frac{c^2}{n}.
\]
The null-event convention makes the left side zero there. Thus the normalized projection norm tends to zero in \(L^2\), as asserted.

### Empirical convergence for the full stated test class

On the construction space set
\[
\bar z_i^{(2)}=\sqrt{m_1}\eta_i,\qquad
\bar u_i^{(2)}=\beta\phi(\bar z_i^{(2)})+\sigma\xi_i.
\]
These comparison pairs, specifically, are independent and identically distributed with law
\[
(Z^{(2)},U^{(2)}),\qquad U^{(2)}=\beta\phi(Z^{(2)})+\sigma G,
\]
where \(G\) is independent of \(Z^{(2)}\). The original finite-width pairs are not claimed to be independent.

The identity
\[
\frac{\|z_0^{(2)}-\bar z^{(2)}\|^2}{n}
=(\sqrt{m_{1,n}}-\sqrt{m_1})^2\frac{\|\eta\|^2}{n}
\]
and the Gaussian second- and fourth-moment calculation give convergence to zero in probability. Lipschitz continuity of \(\phi\) then gives
\[
\begin{split}
\frac{\|u_n^{(2)}-\bar u^{(2)}\|}{\sqrt n}
&\le |\beta_n-\beta|\sqrt{m_{2,n}}
 +|\beta|\frac{\|z_0^{(2)}-\bar z^{(2)}\|}{\sqrt n}\\
&\quad+|\sigma_n-\sigma|\frac{\|\xi\|}{\sqrt n}
 +\frac{\|\sigma_nP_n^{(2)}\xi\|}{\sqrt n}
\longrightarrow0
\end{split}
\]
in probability. This step needs tightness of \(\|\xi\|/\sqrt n\), not independence of the random coefficient differences.

For a bounded uniformly continuous test, split paired points according to whether their distance exceeds a fixed \(\delta>0\). The fraction exceeding \(\delta\) is at most the average squared paired distance divided by \(\delta^2\). The difference of the two empirical averages is therefore at most the modulus of continuity at \(\delta\) plus twice the test's supremum norm times that fraction. Sending width to infinity and then \(\delta\) to zero proves convergence to the comparison average, whose variance tends to zero by independence.

The unbounded-test extension has adequate uniform moments. Gaussian moments give
\[
\mathbb E|z_{0,i}^{(2)}|^4\le3c^4.
\]
The potentially small denominator in \(\beta_n\) cancels before moments are taken:
\[
0\le\beta_n\le\frac{\|z_0^{(3)}\|^2}{n m_{2,n}}
=\frac1n\sum_j\zeta_j^2,\qquad
\mathbb E\beta_n^4\le\mathbb E\zeta_1^8=105.
\]
Each residual coordinate is conditionally centered Gaussian with variance at most \(c^2\), so its fourth moment is at most \(3c^4\). Thus
\[
\mathbb E|u_{n,i}^{(2)}|^4
\le8c^4\mathbb E\beta_n^4+24c^4\le864c^4.
\]
These estimates require no independence among the original output coordinates. The population pair has finite fourth moments as well.

For any continuous \(F\) satisfying \(|F(z,v)|\le C_F(1+z^2+v^2)\), multiply by the compactly supported cutoff in the initial note. For \(R\ge1\), the omitted part is bounded by
\[
\frac{2C_F}{R^2}(z^2+v^2)^2.
\]
Its empirical expected average and its population expectation are \(O(R^{-2})\), uniformly in width. This extends the bounded-test probability convergence to every test in the stated class.

Finally, Jensen's inequality bounds the second moment of each empirical test average uniformly in width by the average of the corresponding squared growth bounds. If \(X_n\) denotes that average and \(\mu\) its asserted limit, then
\[
\mathbb E|X_n-\mu|
\le \epsilon+
 \bigl(\mathbb E|X_n-\mu|^2\bigr)^{1/2}
 \mathbb P(|X_n-\mu|>\epsilon)^{1/2}.
\]
Probability convergence followed by \(\epsilon\downarrow0\) proves \(L^1\) convergence. Equality in distribution for each width transfers both conclusions back to the original Gaussian network; no coupling across different widths is needed.

### Strict positivity of the initial curvature constant

The test \(F(z,v)=[v\phi''(z)]_+\) is continuous and bounded by \(1+v^2\). It follows that
\[
c_n=\frac1n\sum_i[(u_n^{(2)})_i\phi''(z_{0,i}^{(2)})]_+
\longrightarrow
c_*=\mathbb E\!\left[\left[U^{(2)}\phi''(Z^{(2)})\right]_+\right]
\]
in probability and \(L^1\).

Its strictly positive lower bound is
\[
c_*\ge\frac2{25}
\left[\Phi\left(\frac2{\sqrt{m_1}}\right)
 -\Phi\left(\frac1{\sqrt{m_1}}\right)\right]
\Phi\left(-\frac{|\beta|c+1}{\sigma}\right)>0,
\]
where \(\Phi\) is the standard Gaussian distribution function. Indeed, on \(1\le Z^{(2)}\le2\) one has \(-\phi''(Z^{(2)})\ge2/25\), and on \(G\le-(|\beta|c+1)/\sigma\) one has \(U^{(2)}\le-1\). The two events are independent, and both probabilities are strictly positive. This proves the complete initial-note conclusion, including \(\mathbb E c_n\to c_*\).

## 3. Reconstruction along the actual trained trajectory

### Deterministic existence and parameter bounds

For arbitrary finite initial data define, as in the dynamical note,
\[
M=\max_{\ell=2,3}\|W^{(\ell)}(0)\|_{\rm op},\quad
\varepsilon=\frac{\|W^{(4)}(0)\|}{\sqrt n},\quad
\alpha=\|W^{(4)}(0)\|_\infty.
\]
In particular \(\varepsilon\le\alpha\le\sqrt n\,\varepsilon\). Integrating the readout equation gives
\[
\frac{\|\delta^{(3)}(s)\|}{\sqrt n}
\le\varepsilon+cs,\qquad
\|W^{(4)}(s)\|_\infty\le\alpha+cs.
\]
The rank-one update identity
\(\|uv^T/n\|_{\rm F}=\|u\|\|v\|/n\)
then gives
\[
\|W^{(3)}(s)-W^{(3)}(0)\|_{\rm F}
\le c(\varepsilon s+cs^2/2),\qquad
\|W^{(3)}(s)\|_{\rm op}\le K_3,
\]
\[
\frac{\|\delta^{(2)}(s)\|}{\sqrt n}\le K_3(\varepsilon+cs),\qquad
\|W^{(2)}(s)-W^{(2)}(0)\|_{\rm F}
\le cK_3(\varepsilon s+cs^2/2),\qquad
\|W^{(2)}(s)\|_{\rm op}\le K_2,
\]
where
\[
K_3=M+c(\varepsilon S+cS^2/2),\qquad
K_2=M+cK_3(\varepsilon S+cS^2/2).
\]
The first-layer velocity satisfies
\[
\|(z^{(1)})'(s)\|/\sqrt n\le K_2K_3(\varepsilon+cs).
\]
Thus every parameter remains bounded on a finite horizon at each fixed width. The vector field is locally Lipschitz even when \(\tau\) is only Lipschitz. Its integral equation is locally contractive on a sufficiently short interval in a finite-dimensional ball. A finite maximal endpoint would have a state limit, because the vector field is bounded on the bounded trajectory's closure, and local existence at that limit extends the trajectory. This proves existence and uniqueness on every prescribed finite horizon.

Differentiating the forward equations, with no differentiation of \(\tau\), gives
\[
(z^{(2)})'
=\left[\frac{\|h^{(1)}\|^2}{n}I
 +W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\right]\delta^{(2)},
\]
\[
(z^{(3)})'=\frac{\|h^{(2)}\|^2}{n}\delta^{(3)}
 +W^{(3)}\operatorname{diag}(\phi'(z^{(2)}))(z^{(2)})'.
\]
The unnormalized first-layer vector equation is responsible for the second term of the first identity; there is no extra \(1/n\) in that term. Hence, with
\[
J=K_3(c^2+K_2^2),\qquad K=c^2+K_3J,
\]
the velocities divided by \(\sqrt n\) are bounded by \(J(\varepsilon+cs)\) and \(K(\varepsilon+cs)\), respectively. Their displacements are bounded by \(J(\varepsilon s+cs^2/2)\) and \(K(\varepsilon s+cs^2/2)\). Every bounding factor here is a polynomial in \(M,\varepsilon\), with coefficients depending only on the fixed finite \(S\) and no further dependence on width or clipping.

### The complete query derivative and its integral

Since \(q^{(2)}=(W^{(3)})^T\delta^{(3)}\), direct product differentiation gives
\[
\begin{split}
(q^{(2)})'
={}&h^{(2)}\frac{\|\delta^{(3)}\|^2}{n}
 +(W^{(3)})^Tg(z^{(3)})\\
&+(W^{(3)})^T
 [W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'].
\end{split}
\]
The first term is the derivative of the trained matrix. Its sign and coefficient follow exactly from \((W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n\). The second and third terms follow from
\[
(\delta^{(3)})'=g(z^{(3)})
 +W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'.
\]
There is no omitted derivative, residual, clipping derivative, or transpose factor.

The identities
\[
g'=(\phi')^2+\phi\phi'',\qquad
\phi'''(x)=\frac{-2+6x^2}{(1+x^2)^3}
\]
give \(|g'|\le1+2c\), \(|\phi''|\le2\), and \(|\phi'''|\le8\). In particular
\[
\|u_n^{(2)}\|/\sqrt n\le Mc,\qquad
u_n^{(2)}=(W^{(3)}(0))^Tg(z^{(3)}(0)).
\]
Splitting the difference of the middle term using the trained matrix increment and the original matrix gives
\[
\frac{\|(W^{(3)}(s))^Tg(z^{(3)}(s))-u_n^{(2)}\|}{\sqrt n}
\le A(\varepsilon s+cs^2/2),\qquad
A=c^2+M(1+2c)K.
\]
The other two terms have normalized norms at most
\[
c(\varepsilon+cs)^2,\qquad
2K_3K(\alpha+cs)(\varepsilon+cs).
\]
Also \(\|q^{(2)}(0)\|/\sqrt n\le M\varepsilon\). Integrating each term separately therefore proves
\[
\frac{\|q^{(2)}(s)-s u_n^{(2)}\|}{\sqrt n}\le R(s),
\]
with exactly the candidate's remainder
\[
\begin{split}
R(s)={}&M\varepsilon
 +c\left(\varepsilon^2s+\varepsilon c s^2+\frac{c^2s^3}{3}\right)\\
&+A\left(\frac{\varepsilon s^2}{2}+\frac{cs^3}{6}\right)\\
&+2K_3K\left(\alpha\varepsilon s
 +\frac{c(\alpha+\varepsilon)s^2}{2}+\frac{c^2s^3}{3}\right).
\end{split}
\]
This is a bound on the actual nonzero-readout trajectory. The original readout contributes directly through \(M\varepsilon\), the other \(\varepsilon\) terms, and the \(\alpha\) terms. In particular, \(c_n\) is not being asserted to be the exact finite-width right derivative of the positive-part mean at zero.

### Positive-part product estimate

Let
\[
B_n(s)=\frac1n\sum_i[q_i^{(2)}(s)\phi''(z_i^{(2)}(s))]_+.
\]
The pointwise product difference, before taking positive parts, can be split as
\[
(q_i^{(2)}(s)-s(u_n^{(2)})_i)\phi''(z_i^{(2)}(s))
 +s(u_n^{(2)})_i
 [\phi''(z_i^{(2)}(s))-\phi''(z_i^{(2)}(0))].
\]
Using the Lipschitz constant one of the positive-part map, \(|\phi''|\le2\), \(\operatorname{Lip}(\phi'')\le8\), and Cauchy--Schwarz gives
\[
\begin{split}
|B_n(s)-s c_n|
&\le2R(s)
 +8s\frac{\|u_n^{(2)}\|}{\sqrt n}
       \frac{\|z^{(2)}(s)-z^{(2)}(0)\|}{\sqrt n}\\
&\le2R(s)+8McJ\,s(\varepsilon s+cs^2/2).
\end{split}
\]
Thus no coordinatewise bound on \(u_n^{(2)}\), or independence between the product's factors, is needed. For \(M\le M_*\), \(\varepsilon\le1\), and \(\alpha\le1\), collecting the displayed powers on \(0\le s\le S\) yields
\[
|B_n(s)-s c_n|
\le C_{S,M_*}(\varepsilon+\alpha s^2+s^3).
\]
For example, \(\alpha\varepsilon s\le S\varepsilon\), \(\varepsilon^2s\le S\varepsilon\), and \(\varepsilon s^2\le S^2\varepsilon\). All other contributions already have the required powers. This verifies dynamical equations (9)--(15), including their proportional normalizations.

## 4. Canonical probability, integrability, and joint qualifiers

Under the exact readout initialization,
\[
\varepsilon=\frac{\|G^{(4)}\|}{n^{3/2}},\qquad
\alpha\le\sqrt n\,\varepsilon.
\]
On
\[
\Omega_n=\{M\le10,\ \|G^{(4)}\|/\sqrt n\le2\},
\]
one has \(\varepsilon\le2/n\), \(\alpha\le2/\sqrt n\). For \(n\ge4\), the preceding restricted bound therefore gives, simultaneously in time and clipping,
\[
|B_n(s)-s c_n|\le C_S(n^{-1}+n^{-1/2}s^2+s^3),
\qquad 0\le s\le S.
\]

The constants in the claimed probability estimate are correct. A maximal \(1/4\)-separated set of unit vectors is a \(1/4\)-net; disjoint radius-\(1/8\) balls around its points lie in the radius-\(9/8\) ball, giving at most \(9^n\) points. Approximating both arguments of a matrix bilinear form incurs total error at most \(\|W\|_{\rm op}/2\). A fixed canonical bilinear form is \(N(0,1/n)\); the Gaussian exponential moment gives its two-sided tail at \(r/2\) as at most \(2e^{-nr^2/8}\). Union over both nets and both matrices yields
\[
\mathbb P(M>r)\le4e^{2n\log9-nr^2/8}.
\]
For the readout, \(\mathbb E e^{\|G^{(4)}\|^2/4}=2^{n/2}\). Markov's inequality at \(4n\), together with \(r=10\), proves exactly
\[
\mathbb P(\Omega_n^c)
\le4e^{-(25/2-2\log9)n}
 +e^{-(1-\frac12\log2)n}.
\]

For \(r\ge10\), the matrix tail is bounded by \(4e^{-r^2/16}\), uniformly over \(n\ge1\), so tail integration gives every fixed moment of \(M\) uniformly in width. Gaussian squared-norm moments give
\[
\mathbb E\varepsilon^{2k}
=n^{-3k}\prod_{j=0}^{k-1}(n+2j)\le C_k n^{-2k},\qquad
\mathbb E\alpha^{2k}\le C_k n^{-k}.
\]
The moment formula follows by differentiating \((1-2t)^{-n/2}\) at zero; exponential integrability for some \(0<t<1/2\) justifies those differentiations. Finite sums and Cauchy--Schwarz then bound all fixed moments of every polynomial factor in \(M,\varepsilon\) occurring above. This does not require independence of these polynomial factors and the small readout norms.

For each such factor \(P\), in particular,
\[
\mathbb E[|P|\varepsilon]=O(n^{-1}),\quad
\mathbb E[|P|\varepsilon^2]=O(n^{-2}),\quad
\mathbb E[|P|\alpha]=O(n^{-1/2}),\quad
\mathbb E[|P|\alpha\varepsilon]=O(n^{-3/2}).
\]
For the last estimate use \(\alpha\varepsilon\le\sqrt n\,\varepsilon^2\). Applying these to the unrestricted formula for \(R(s)\) and the product bound, with \(s\le S\), proves
\[
\mathbb E|B_n(s)-s c_n|
\le C_S(n^{-1}+n^{-1/2}s^2+s^3).
\]
This is an unconditional estimate. The complement of \(\Omega_n\) has been included through global polynomial domination; its contribution has not been discarded using probability alone.

The simultaneous and measurable-selection assertions also hold. For each finite initial state, the deterministic estimates above hold for every allowed scalar map and the entire continuous trajectory. Their common upper bound depends only on the initial norms, not on the map. Consequently the same measurable event \(\Omega_n\), and later its intersection with an event determined by \(c_n\), works for all maps and all indicated times.

For precision, a measurably selected fixed clipping can be formalized as a random element of the allowed scalar maps with the Borel sigma-field of uniform convergence on compact intervals. On this Lipschitz class, measurability of all rational evaluations suffices: continuity determines the remaining evaluations and the compact suprema. Such a random map can depend on the initialization but remains fixed in time.

Here is the needed measurability justification. On a bounded set of initial states and a finite horizon, the preceding path bounds give a common bounded set of states. The vector fields there have a Lipschitz constant in the state uniform over allowed maps. Uniform convergence of the maps on the bounded range of query coordinates gives uniform convergence of these vector fields. Subtracting their integral equations and integrating the resulting Lipschitz inequality proves continuous dependence of the trajectories on the initial state and on the map. Thus a measurable selection yields measurable trajectories and \(B_n(s)\). Their common polynomial domination proves the same unconditional expectation estimate. This argument supplies the meaning and justification of the random-selection clause without assuming a nonmeasurable supremum is integrable.

The indicator averages used for the positive fraction are also jointly measurable in the random outcome and time: each coefficient and its time-dependent threshold are continuous along the trajectory, and the threshold comparison is Borel measurable. The all-map, all-time assertion is made on an explicitly measurable sufficient event, so it does not require an exchange of an uncountable supremum with expectation. Time-adaptive or nonmeasurable clipping choices are outside the stated class.

Finally, \(c_n\) is exactly the same random variable for every clipping: it depends only on \(z^{(1)}(0),W^{(2)}(0),W^{(3)}(0)\). The readout and clipping do not enter its definition.

## 5. Positive common intervals, positive fraction, and order of limits

Take \(S=1\) and choose \(s_0\in(0,1]\) with \(C_1s_0^2\le c_*/8\), where \(C_1\) is the constant in the preceding eventwise bound. For any fixed \(a\in(0,s_0]\), put
\[
E_n=\Omega_n\cap\{c_n\ge3c_*/4\}.
\]
The initial-law convergence and the bound on \(\mathbb P(\Omega_n^c)\) give \(\mathbb P(E_n)\to1\), without any independence assumption between these events. For \(s\in[a,s_0]\), division by \(s\) gives
\[
\frac{B_n(s)}s
\ge\frac{3c_*}{4}
 -C_1(n^{-1}/a+n^{-1/2}s_0+s_0^2).
\]
Once the first two error terms total at most \(c_*/8\), this proves
\[
B_n(s)\ge\frac{c_*}{2}s
\]
on \(E_n\), simultaneously for every allowed fixed clipping and every \(s\in[a,s_0]\). This is precisely dynamical equation (23). It does not claim a finite-width bound all the way down to \(s=0\).

To verify (23a), increase the deterministic width threshold so that \(2/n\le a\). On \(E_n\), for \(a\le s\le s_0\),
\[
\left(\frac1n\sum_i
 |q_i^{(2)}(s)\phi''(z_i^{(2)}(s))|^2\right)^{1/2}
\le2K_3(\varepsilon+cs)\le Ds,
\]
with exactly
\[
D=2(1+c)[10+c(1+c/2)].
\]
Here \(K_3\le10+c(1+c/2)\) and \(\varepsilon\le a\le s\), which verify every constant in this estimate.

Let \(p_n(s)\) be the fraction of coordinates for which
\[
q_i^{(2)}(s)\phi''(z_i^{(2)}(s))\ge c_*s/4.
\]
On complementary coordinates the positive part is at most \(c_*s/4\). Cauchy--Schwarz bounds the contribution of selected coordinates by \(Ds\sqrt{p_n(s)}\). Therefore
\[
\frac{c_*s}{2}\le B_n(s)\le\frac{c_*s}{4}+Ds\sqrt{p_n(s)},
\qquad
p_n(s)\ge\left(\frac{c_*}{4D}\right)^2>0.
\]
This uses no independent-coordinate assertion at positive time. It holds on the same \(E_n\), for the same intervals, widths, and clippings. It is a statement about scalar curvature coefficients.

The unconditional comparison with the deterministic initial coefficient is
\[
\mathbb E|B_n(s)-s c_*|
\le C_S(n^{-1}+n^{-1/2}s^2+s^3)
 +s\,\mathbb E|c_n-c_*|.
\]
In addition, nonnegativity of \(B_n\) and the common event give
\[
\mathbb E B_n(s)\ge\frac{c_*}{2}s\,\mathbb P(E_n),
\qquad a\le s\le s_0,
\]
uniformly over prescribed or measurably selected fixed clippings. This confirms positive unconditional means on the same common intervals, without requiring the eventwise and expectation constants to coincide.

For each fixed \(0<s\le S\), the \(L^1\) convergence of \(c_n\) proves only
\[
c_*s-C_Ss^3
\le\liminf_{n\to\infty}\mathbb E B_n(s)
\le\limsup_{n\to\infty}\mathbb E B_n(s)
\le c_*s+C_Ss^3.
\]
The same constants permit a prescribed width-dependent sequence of allowed maps. Dividing by \(s>0\), keeping a finite horizon fixed, and then sending \(s\downarrow0\) proves
\[
\lim_{s\downarrow0}\liminf_{n\to\infty}\frac{\mathbb E B_n(s)}s
=\lim_{s\downarrow0}\limsup_{n\to\infty}\frac{\mathbb E B_n(s)}s
=c_*>0.
\]
The width limit comes first. The surviving \(C_Ss^3\) error does not prove convergence at a fixed positive time, and the notes do not claim that it does.

For any proposed finite coefficient multiplying \(s^5\), choose a fixed positive \(s\le s_0\) for which that fifth-order quantity is below \(c_*s/2\). The eventwise lower bound then contradicts the proposed canonical mean positive-part bound at sufficiently large width, with probability tending to one. The unconditional mean conclusion follows likewise from the expectation bounds. This is the precise obstruction established by the two-note chain.

## 6. Adversarial disposition and limits of certification

No unresolved gap remains in the scoped claims. The reconstruction verifies the original reused joint law, null events and ratios, projection removal, uniform fourth moments, the entire stated continuous test class, uniform integrability, and \(c_*>0\). It also verifies the full trained query derivative, every term of \(R(s)\), the positive-part product estimate, canonical probability constants, global expectation domination, simultaneous clipping and time qualifiers, measurability, the shared \(c_n\), and (23a).

No candidate fix is required. The explicit measurable-selection interpretation and quantifier statements in this report clarify the existing claims; they add neither an independence hypothesis nor a stronger convergence assertion.

This PASS does not certify a full global theorem, a positive fraction of eigenvalues of a parameter Hessian, a canonical population counterexample, a limiting trajectory at fixed positive time, a physical-time or exact-gradient-descent limit, a transported covariance estimate, a uniform tail envelope, or population restartability. The positive scalar coefficients have not been turned into a Hessian quadratic-form claim. The initial empirical-pair limit is the only population law established by this chain.
