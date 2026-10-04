# Internal reconstruction of initialized fluctuations and label response

2026-10-04. Scoped internal check; this is not an independent promotion review.

**Verdict: PASS for the initialized and exact zero-label derivative claims in
the reviewed revision, subject to their stated fixed-dimension and
distributional scope.** No fixed nonzero-label predictor lower bound is
certified. The singular-covariance derivative, conditional central limit
argument, finite-width fitted-endpoint derivative, sample-count factors, and
depth factor have all been reconstructed below.

The complete scientific input was
`studies/closure_sampling_20261003/INTEGRATED_INITIAL_VARIABILITY.md`, with
SHA-256
`97cdb707c082acf1579e3f73fea6d448e6941a0a06e98568fc4383b3f93a5c6d`.
The earlier revision with SHA-256
`fddf7431497ee88962432c37272dc97df5914fb0cb042fd0b760caa76329e2f6`
was also read completely during this check. Three issues reported during the
check were corrected in the reviewed revision: the linear residual is now
defined; the endpoint observable is extended explicitly on singular-Gram
events; and the standard-deviation statement concerns the limiting Gaussian,
without claiming convergence of finite-width moments. The last correction is
necessary: an explicit admissible activation below gives infinite endpoint
second moments at every finite width.

Input scope was the single assigned scientific note, including its revised
version, plus the required `explain-with-canonical-notation` skill, its
neural-network reference, and `solve-math-rigorously`. No book, code, study
history, other research note, external mathematical source, or numerical
experiment was used as evidence. Only this report was written. All statements
below are proved directly in the stated finite-query model; elementary
characteristic-function convergence and finite-dimensional ODE differentiation
are used in the forms explained below.

## Model, signs, and parameter scaling

Fix integers \(m,d,L\ge1\) and width \(n\). The training inputs are
\(v_a=x_a/\sqrt d\in\mathbb R^d\), \(1\le a\le m\), and \(v_0\) is a
fixed query. The read-in matrix is \(A\in\mathbb R^{n\times d}\), the hidden
matrices are \(W^{(\ell)}\in\mathbb R^{n\times n}\), \(2\le\ell\le L\),
and the readout is \(w\in\mathbb R^n\). The forward maps are those in the
input:

\[
h^{(1)}(x)=\phi_1(Av),\qquad
h^{(\ell)}(x)=\phi_\ell(W^{(\ell)}h^{(\ell-1)}(x)),\qquad
f(x)=n^{-1}w^\top h^{(L)}(x).
\]

All activations act componentwise. They are \(C^2\), have bounded first and
second derivatives, and therefore have at most linear growth. The initialized
entries of \(A\) and \(W^{(\ell)}\) are independent Gaussians of variance
\(1\) and \(1/n\), respectively, and \(w(0)=0\).

For labels \(\eta y\in\mathbb R^m\), use the residual convention
\(r=f_X-\eta y\), where \(f_X=(f(x_a))_{a=1}^m\), and loss
\(\mathcal L=m^{-1}\|r\|_2^2\). This is the sign convention selected by the
revised note's definition of \(r_{\rm lin}\). Let \(\theta_h\) collect hidden
parameters, let \(M_h\) be their positive diagonal mobility matrix, and let
\(J_h=\partial f_X/\partial\theta_h\). The mobility of \(A\) is \(n\), each
hidden \(W^{(\ell)}\) has mobility \(1\), and the readout has mobility \(n\).
If \(H(t)\in\mathbb R^{m\times n}\) has rows \(h^{(L)}(t,x_a)^\top\), then

\[
\dot w=-\frac2mH^\top r,\qquad
\dot\theta_h=-\frac2mM_hJ_h^\top r,\qquad
\dot r=-\frac2m\mathcal K(t)r,
\]
\[
\mathcal K(t)=\frac1nH(t)H(t)^\top+J_h(t)M_hJ_h(t)^\top.
\tag{A}
\]

Thus the initialized readout Gram is exactly \(K_n=H(0)H(0)^\top/n\).
There is no missing factor of \(n\), \(m\), or \(2\) in the note. Every hidden
parameter derivative of \(f\) is linear in \(w\), which is the key fact for
both the onset and the small-label endpoint calculation.

## Equations (1)--(7): the full covariance fluctuation argument

Let \(p=m+1\), and index symmetric \(p\times p\) matrices by their upper
triangular entries. All operator transposes and covariance matrices in this
paragraph refer to that fixed vector representation. The pairings in the
Gaussian differentiation formula still sum over all ordered matrix indices.

Given the earlier initialized layers, the preactivation vectors across the
\(p\) inputs of distinct neurons in layer \(\ell\) are conditionally
independent \(N(0,K_n^{(\ell-1)})\). At layer \(1\), the covariance is the
deterministic input Gram \(Q^{(0)}\). Thus

\[
K_n^{(\ell)}=\frac1n\sum_{i=1}^n
 \phi_\ell(Z_i)\phi_\ell(Z_i)^\top,
\]

and its conditional mean is \(F_\ell(K_n^{(\ell-1)})\). This proves the
exact recursion underlying (1). The covariance of one summand is exactly
(2), including repeated indices. Neither independence across input indices
nor nonsingularity of the conditional Gaussian law is needed.

For a positive semidefinite covariance \(R\) with bounded operator norm,
write \(Z=R^{1/2}G\), \(G\sim N(0,I_p)\). Linear growth of the activation
bounds every fixed moment of a summand uniformly over such \(R\). The
positive square root is continuous on the positive semidefinite cone.
Pointwise convergence under this coupling and the common Gaussian moment
bound therefore prove continuity of \(F_\ell(R)\), of the summand covariance,
and of all Gaussian expectations needed below. Conditional Chebyshev on a
bounded covariance set, followed by tightness of the earlier covariance,
gives inductively

\[
K_n^{(\ell)}\longrightarrow Q^{(\ell)}\quad\hbox{in probability}.
\tag{B}
\]

Here is a direct check of differentiation at a singular covariance. Fix
\(Q\succeq0\) and \(H=H^\top\) with \(Q+H\succeq0\), and let
\(g_{ab}(z)=\phi_\ell(z_a)\phi_\ell(z_b)\). For \(\varepsilon>0\), the
Gaussian covariance \(Q+sH+\varepsilon I\) is positive definite for
\(0\le s\le1\). Differentiating its density gives the heat identity

\[
\frac d{ds}\mathbb E g_{ab}(Z_s)
=\frac12\sum_{u,v}H_{uv}\mathbb E\,\partial_{uv}g_{ab}(Z_s).
\tag{C}
\]

For completeness, the density \(p_R(z)\) satisfies
\(\partial_s p_{R+sH}=\tfrac12\sum_{u,v}H_{uv}\partial_{uv}p_{R+sH}\),
as is verified by differentiating
\((\det R)^{-1/2}\exp(-z^\top R^{-1}z/2)\). Two integrations by parts
transfer these derivatives to \(g_{ab}\). The function \(g_{ab}\), its first
derivatives, and its second derivatives have at most quadratic, linear, and
linear growth, respectively. Gaussian tails therefore eliminate every
boundary term, including when the activation itself is unbounded.

Integrating (C) over \(s\) proves (7) for positive \(\varepsilon\). The common
Gaussian coupling and moment domination let \(\varepsilon\downarrow0\).
The result is the exact segment formula

\[
F_\ell(Q+H)-F_\ell(Q)=\int_0^1T_\ell(Q+sH)[H]\,ds,
\tag{D}
\]

where \(T_\ell(R)\) denotes (3) with covariance \(R\). When \(a\ne b\),
the two mixed ordered derivatives \(\partial_{ab}g_{ab}\) and
\(\partial_{ba}g_{ab}\) combine with the factor \(1/2\) to give
\(H_{ab}\mathbb E[\phi_\ell'(Z_a)\phi_\ell'(Z_b)]\). The diagonal
derivatives give the other two terms in (3). When \(a=b\),

\[
\frac12\frac{d^2}{dz_a^2}\phi_\ell(z_a)^2
=(\phi_\ell'(z_a))^2+\phi_\ell(z_a)\phi_\ell''(z_a),
\]

which verifies the special coefficient quoted in the note. Continuity of
\(T_\ell(R)\) in operator norm in this finite-dimensional space now yields

\[
\|F_\ell(Q+H)-F_\ell(Q)-T_\ell(Q)[H]\|
\le\|H\|\sup_{0\le s\le1}\|T_\ell(Q+sH)-T_\ell(Q)\|
=o(\|H\|).
\tag{E}
\]

This is a derivative along feasible covariance increments. No extension of
\(F_\ell\) to indefinite matrices and no inverse of \(Q\) are being assumed.

To verify the probabilistic step, let

\[
V_{n,\ell}=\sqrt n\bigl(K_n^{(\ell)}-
 F_\ell(K_n^{(\ell-1)})\bigr).
\]

Write \(B_\ell(R)\) for the summand covariance at covariance \(R\).
For any fixed vector of coefficients \(u\) in symmetric-matrix coordinates,
the centered conditional summand \(X_i\) obeys

\[
\mathbb E[e^{i\langle u,X_i\rangle/\sqrt n}\mid\mathcal F_{\ell-1}]
=1-\frac{u^\top B_\ell(K_n^{(\ell-1)})u}{2n}
 +O(n^{-3/2}).
\]

The remainder bound is uniform on bounded covariance sets because

\[
|e^{iv}-1-iv+v^2/2|\le |v|^3/6
\]

and the third absolute moment of the centered summand is uniformly finite.
Conditional independence raises this expression to its \(n\)-th power.
Equation (B) and continuity of the covariance give

\[
\mathbb E[e^{i\langle u,V_{n,\ell}\rangle}\mid\mathcal F_{\ell-1}]
\longrightarrow \exp(-u^\top B_\ell u/2)
\]

in probability. Since the conditional characteristic functions are bounded
by one, convergence to this constant also holds in \(L^1\). If \(U_n\) is
the vector of earlier layer fluctuations, it is
\(\mathcal F_{\ell-1}\)-measurable, and

\[
\mathbb E e^{i\langle v,U_n\rangle+i\langle u,V_{n,\ell}\rangle}
-e^{-u^\top B_\ell u/2}\mathbb E e^{i\langle v,U_n\rangle}
\longrightarrow0.
\tag{F}
\]

This explicitly proves the independence of the new Gaussian innovation in
the limit. It does not assert finite-\(n\) independence of the layer
fluctuations. Applying (E) to the earlier tight fluctuation gives

\[
\sqrt n(K_n^{(\ell)}-Q^{(\ell)})
=T_\ell\sqrt n(K_n^{(\ell-1)}-Q^{(\ell-1)})+V_{n,\ell}+o_P(1).
\]

For finite-dimensional laws, pointwise convergence of characteristic
functions to a characteristic function continuous at zero implies weak
convergence to its law. Here the limiting Gaussian characteristic function
is continuous at zero, including in the degenerate case. Applying this
criterion inductively yields the joint Gaussian recursion (4). Its innovations are
independent and centered, so its covariance is (5). This also handles
degenerate \(B_\ell\) and singular input covariances. For example, identical
inputs produce identically equal columns at every finite width; the
degenerate limit preserves these constraints. There is no hidden
nondegeneracy assumption in the central limit theorem.

## Equations (8)--(12): onset, finite time, and fitted endpoint

At \(t=0\), \(J_h=0\) because \(w=0\). For the unscaled label vector \(y\),
\(r(0)=-y\), so (A) gives

\[
\dot f(0,x_0)=\frac1n h^{(L)}(0,x_0)^\top\dot w(0)
=\frac2m\kappa_n^\top y.
\]

This is exactly (8). The single-copy limiting variance after multiplication
by \(\sqrt n\) is
\(4m^{-2}\sum_{a,b}y_a C_{L,0a,0b}y_b\). Independence doubles it, giving
(9) and its factor \(8\). A zero variance means a degenerate Gaussian; the
note correctly makes nondegeneracy conditional on positivity.

At label scale \(\eta=0\), the entire initialized state is stationary. The
finite-dimensional vector field is \(C^1\), since the activations are \(C^2\),
so solutions on a fixed finite time interval are differentiable in
\(\eta\). The hidden velocity contains both \(r\) and \(w\), each of which
vanishes at this stationary state. Consequently the hidden label derivative
is identically zero. Writing \(s(t)=\partial_\eta w^\eta(t)|_{\eta=0}\)
and \(H_0=H(0)\) gives

\[
\dot s=\frac2mH_0^\top\left(y-\frac1nH_0s\right),\qquad s(0)=0.
\tag{G}
\]

If \(K_n>0\), its solution is

\[
s(t)=H_0^\top K_n^{-1}(I-e^{-2tK_n/m})y.
\]

Multiplication by the query feature row divided by \(n\) proves (10).
For finite time, positivity is stronger than necessary: replacing
\(K_n^{-1}(I-e^{-2tK_n/m})\) by
\(\int_0^t(2/m)e^{-2sK_n/m}\,ds\) makes the formula valid even for singular
\(K_n\). This observation is not used to justify the fitted nonlinear
endpoint at a singular initialized Gram.

Here is the complete small-label endpoint estimate for one fixed finite
initialization with \(\lambda=\lambda_{\min}(K_n)>0\). Choose a compact
parameter neighborhood of that state on which the readout-feature Gram
satisfies

\[
\frac1nH(t)H(t)^\top\succeq\frac\lambda2 I.
\]

The neighborhood may depend on this realization and on \(n\). The hidden
Jacobian is linear in \(w\); all its coefficients and the feature maps are
bounded on this neighborhood. Before a first exit from it, (A) implies

\[
\|r(t)\|_2\le |\eta|\|y\|_2e^{-\lambda t/m},\qquad
\|\dot w(t)\|_2\le C_n\|r(t)\|_2,
\]
\[
\|\dot\theta_h(t)\|_2\le C_n\|r(t)\|_2\|w(t)\|_2.
\tag{H}
\]

Integration first gives \(\sup_t\|w(t)\|_2\le C_n|\eta|\), and then

\[
\int_0^\infty\|\dot\theta_h(t)\|_2\,dt\le C_n\eta^2.
\]

For sufficiently small \(|\eta|\), these two bounds are strictly inside
the chosen neighborhood, excluding a first exit. They establish global
continuation, exponential fitting, convergence of all parameters, and

\[
H^\eta(t)=H_0+O_n(\eta^2),\qquad
h^{(L),\eta}(t,x)=h^{(L)}(0,x)+O_n(\eta^2),
\tag{I}
\]

uniformly in \(t\ge0\) and on any fixed bounded query set. The second
statement follows by bounded parameter derivatives of the forward map on
the compact parameter and query sets.

The full training kernel in (A) satisfies

\[
\mathcal K^\eta(t)=K_n+E^\eta(t),\qquad
\sup_t\|E^\eta(t)\|\le C_n\eta^2,
\]

because the readout Gram changes by \(O_n(\eta^2)\), while the hidden
Jacobian contribution is quadratic in \(w=O_n(\eta)\). Define

\[
r_{\rm lin}(t)=-e^{-2tK_n/m}y,
\qquad d^\eta(t)=r^\eta(t)-\eta r_{\rm lin}(t).
\]

Variation of constants gives

\[
d^\eta(t)=-\frac2m\int_0^t e^{-2(t-s)K_n/m}
 E^\eta(s)r^\eta(s)\,ds.
\]

Integrating its norm in time, using the exponential semigroup bound and
(H), yields the stronger norm statement

\[
\int_0^\infty\|d^\eta(t)\|_2\,dt\le C_n|\eta|^3.
\tag{J}
\]

Finally, (I), (J), and the readout equation imply

\[
w^\eta(\infty)
=-\frac2m\int_0^\infty H^\eta(t)^\top r^\eta(t)\,dt
=\eta H_0^\top K_n^{-1}y+O_n(|\eta|^3).
\]

The limiting query feature differs from its initialized value by
\(O_n(\eta^2)\), so

\[
f_n^\eta(\infty,x_0)=\eta\kappa_n^\top K_n^{-1}y+O_n(|\eta|^3).
\tag{K}
\]

This proves (11) as a derivative of the actual fitted nonlinear endpoint.
It supplies the needed justification for taking the label derivative at
infinite time; simply taking \(t\to\infty\) in (10) would not have supplied
that justification. The argument uses only the stated \(C^2\) regularity,
and its constants are allowed to depend on \(n\), the initialization, and
the fixed direction \(y\).

For the limit theorem, assume the population training block \(Q>0\).
Equation (B) gives \(\Pr(K_n>0)\to1\). On this high-probability event, the
derivative of \(g(\kappa,K)=\kappa^\top K^{-1}y\) is

\[
Dg[H]=H_{0X}Q^{-1}y-\kappa^\top Q^{-1}H_{XX}Q^{-1}y,
\]

by \(D(K^{-1})[H]=-K^{-1}HK^{-1}\). This verifies (12). The first-order
inverse remainder is quadratic on a neighborhood with a fixed positive
spectral gap. Combining it with (4) gives a centered Gaussian for one
copy's centered response, and twice its variance for the difference of
independent copies. Setting the response to zero on \(K_n\not>0\), as the
revised source now does, does not change convergence in distribution.

For finite \(t\), set \(c=2t/m\). Differentiating the power-series solution
of the matrix exponential, or its linear ODE, gives

\[
D(e^A)[H]=\int_0^1e^{(1-s)A}He^{sA}\,ds.
\]

It therefore gives the derivative of (10), including the dependence on
\(K_n\). There is no commuting-matrix assumption. In particular,

\[
D(K^{-1}(I-e^{-cK}))[H]
=-K^{-1}HK^{-1}(I-e^{-cK})
 +cK^{-1}\int_0^1e^{-(1-s)cK}He^{-scK}\,ds.
\tag{L}
\]

When the query is training point \(b\), 
\(\kappa_n^\top=e_b^\top K_n\), so (11) equals \(y_b\) identically.
The differential also vanishes on the corresponding constrained augmented
Gram perturbations: \(H_{0X}=e_b^\top H_{XX}\) and
\(\kappa^\top=e_b^\top Q\) cancel its two terms. This verifies the source's
endpoint cancellation and falsifies any inference from onset variability
alone to variability of fitted training predictions.

## Equations (13)--(17): sample count, depth, and normalization

Now take \(d\ge m+1\), \(v_a=e_a\), \(1\le a\le m\), and
\(v_0=e_{m+1}\), with odd activations and the stipulated positive scalar
variances \(q_\ell\). Induction shows
\(Q^{(\ell)}=q_\ell I_{m+1}\): centered independent Gaussian coordinates
remain uncorrelated after applying odd scalar activations, and each output
second moment is \(q_\ell\). Thus the population training gap is
\(\gamma=q_L\), with no division by \(m\), and the population query vector
is zero.

At diagonal covariance and distinct indices \(0,a\), the two
diagonal-perturbation terms of (3) vanish, since the other factor has zero
mean. The off-diagonal term is

\[
(T_\ell H)_{0a}=a_\ell^2H_{0a},\qquad
a_\ell=\mathbb E\phi_\ell'(\sqrt{q_{\ell-1}}Z).
\]

Moreover,

\[
B_{\ell,0a,0b}
=\mathbb E[\phi_\ell(Z_0)^2\phi_\ell(Z_a)\phi_\ell(Z_b)]
=q_\ell^2\mathbf1_{\{a=b\}}.
\]

Equation (5) therefore propagates

\[
C_{\ell,0a,0b}=\nu_\ell\mathbf1_{\{a=b\}},\qquad
\nu_\ell=q_\ell^2+a_\ell^4\nu_{\ell-1},\qquad\nu_0=0,
\]

which is (13). Possible fluctuations of the diagonal Gram entries do not
enter this recursion, since their coefficients in this particular
off-diagonal derivative are zero.

Writing \(Y=\|y\|_2/\sqrt m\), (9) becomes

\[
\sigma_{\rm onset}^2
=\frac8{m^2}\nu_L\|y\|_2^2
=\frac{8\nu_LY^2}{m},
\]

which proves (14). In the finite-time and endpoint functionals, every
training-block derivative is multiplied by the population query vector
\(\kappa=0\), so only the query-row fluctuation remains. Since \(Q=q_LI\),
its coefficient on \(y\) is

\[
\frac{1-e^{-2q_Lt/m}}{q_L},
\]

with the endpoint value \(1/q_L\). The single-copy variance is
\(\nu_L\|y\|_2^2(1-e^{-2q_Lt/m})^2/q_L^2\), and independence doubles it.
This proves (15), including its factors \(2m\), \(q_L^{-2}\), and the
time exponent \(2q_Lt/m\). At \(t=m/(2\gamma)\), the exponent is \(1\), so
the squared fitting factor is \( (1-e^{-1})^2\). At \(t=0\) the limit is
zero, and differentiating the time factor at zero recovers the variance
in (14).

For \(q=q_{\ell-1}>0\), one-dimensional Gaussian integration by parts is
justified by the bounded derivative and linear growth of the activation:

\[
\mathbb E[Z\phi_\ell(\sqrt qZ)]
=\sqrt q\,\mathbb E\phi_\ell'(\sqrt qZ)=\sqrt q\,a_\ell.
\]

Cauchy--Schwarz gives \(q a_\ell^2\le q_\ell\), and hence
\(a_\ell^4\le q_\ell^2/q_{\ell-1}^2\). Dividing (13) by \(q_\ell^2\),

\[
\frac{\nu_\ell}{q_\ell^2}
=1+\frac{a_\ell^4q_{\ell-1}^2}{q_\ell^2}
       \frac{\nu_{\ell-1}}{q_{\ell-1}^2},\qquad
0\le\frac{a_\ell^4q_{\ell-1}^2}{q_\ell^2}\le1.
\]

Starting with \(\nu_1/q_1^2=1\) proves (16): the ratio lies in \([1,L]\).
This proves that the endpoint limiting Gaussian standard deviation in the
two-copy, \(\sqrt n\)-scaled CLT lies between
\(\sqrt{2m}Y\) and \(\sqrt{2Lm}Y\). It does not prove finite-\(n\) moment
convergence.

If the same odd activation is used at every layer and
\(\mathbb E\phi(Z)^2=1\), then \(q_\ell=1\) for every \(\ell\). The scalar
recursion has constant coefficient \(a^4\), and solving it gives (17),
\(\nu_L=\sum_{j=0}^{L-1}a^{4j}\), with \(a=\mathbb E\phi'(Z)\).
The integration-by-parts formula gives \(a=\mathbb E[Z\phi(Z)]\).
Equality \(|a|=1\) in Cauchy--Schwarz forces
\(\phi(Z)=aZ\) almost surely; continuity and the positive Gaussian density
force \(\phi(z)=az\) for every real \(z\). Thus any nonlinear
continuous normalized activation has \(|a|<1\) and
\(\nu_L\le(1-a^4)^{-1}\). For identity, \(a=1\) and \(\nu_L=L\).
These calculations concern coefficients of the fixed-depth CLTs and do
not provide a theorem for a depth \(L=L_n\to\infty\).

## Falsification checks and the necessary moment distinction

The following counterexample disproves the stronger reading that endpoint
standard deviations themselves must exist or converge under the note's
activation assumptions. It leaves the stated distributional CLT intact.

Take one training input and an orthogonal query, nonzero scalar label
\(y\), and use

\[
\phi(z)=
\begin{cases}
z e^{-1/z^2},&z\ne0,\\
0,&z=0.
\end{cases}
\tag{M}
\]

This activation is odd and \(C^\infty\). Away from zero,

\[
\phi'(z)=e^{-1/z^2}(1+2/z^2),\qquad
\phi''(z)=e^{-1/z^2}(-2/z^3+4/z^5).
\]

Both derivatives extend continuously by zero at the origin and are
bounded; at infinity they tend to \(1\) and \(0\), respectively. Also
\(|\phi(z)|\le|z|\), so \(q=\mathbb E\phi(Z)^2\in(0,\infty)\).
Thus all assumptions in the note are satisfied. Multiplying the
activation by \(q^{-1/2}\) can additionally impose forward normalization
without removing this example.

For \(L=1\), let \(a_i=\phi(Z_i)\) and \(b_i=\phi(U_i)\), where all
\(Z_i,U_i\) are independent standard Gaussians. Orthogonal input coordinates
make \(a\) and \(b\) independent. Let \(S=\sum_i a_i^2>0\) almost surely.
Equation (11) gives

\[
F_n(\infty,x_0)=y\frac{a^\top b}{S},\qquad
\mathbb E[F_n(\infty,x_0)^2\mid a]=\frac{y^2q}{S}.
\tag{N}
\]

For \(0<\varepsilon\le1\), on the event
\(\max_i|Z_i|\le\varepsilon\),

\[
S\le n\varepsilon^2e^{-2/\varepsilon^2},\qquad
\Pr(\max_i|Z_i|\le\varepsilon)
\ge (2\varphi(1)\varepsilon)^n,
\]

where \(\varphi(1)=(2\pi)^{-1/2}e^{-1/2}\) is the standard Gaussian density
at \(1\). Consequently

\[
\mathbb E\frac1S
\ge\frac{(2\varphi(1))^n}{n}
 \varepsilon^{n-2}e^{2/\varepsilon^2}\longrightarrow\infty
\quad\hbox{as }\varepsilon\downarrow0.
\]

Equation (N) and nonnegative integration give
\(\mathbb E[F_n(\infty,x_0)^2]=\infty\) for every finite \(n\), even though
\(K_n>0\) almost surely and the population gap is positive. Nevertheless
(15) holds: for \(L=m=1\), the two-copy limiting Gaussian variance is
\(2y^2\).

The same example extends to any prescribed depth \(L\ge2\) by taking
identity activations in layers \(2,\dots,L\). Write
\(P=W^{(L)}\cdots W^{(2)}\) and \(M=P^\top P\). This product is invertible
almost surely: the determinant of each square Gaussian matrix is a
nonzero polynomial in variables with a joint density, whose zero set has
Lebesgue measure zero. It is independent of \(a,b\), and

\[
F_n(\infty,x_0)=y\frac{a^\top Mb}{a^\top Ma},\qquad
\mathbb E[F_n(\infty,x_0)^2\mid a,M]
=y^2q\frac{a^\top M^2a}{(a^\top Ma)^2}
\ge\frac{y^2q}{\|a\|_2^2}.
\]

The inequality is Cauchy--Schwarz applied to \(a^\top Ma\). Thus the
endpoint second moment is again infinite at every width. Differences of
independent copies also have infinite second moment: choose a finite
\(R\) for which one copy lies in \([-R,R]\) with positive probability;
on that event, the squared difference from an independent copy of
magnitude above \(2R\) is at least one quarter of the latter's square.
The tail second moment of that latter copy is infinite.

A separate check shows why the revised singular-event convention is also
needed. Take a nonzero odd smooth activation that is identically zero on
\([-1,1]\), for example

\[
\phi(z)=\operatorname{sgn}(z)\,\psi(|z|-1),\qquad
\psi(t)=\begin{cases}e^{-1/t^2},&t>0,\\0,&t\le0.\end{cases}
\]

Its first and second derivatives are bounded, and its population second
moment is positive. With one training input and one layer, the event that
all training preactivations lie in \([-1,1]\) has positive probability at
every width. On it \(K_n=0\), the readout remains zero, and no nonzero
label is fitted. A positive population Gram therefore does not imply
almost-sure finite-width fitting. The exceptional-event definition in
the revised source resolves exactly this issue for its asymptotic
distributional statement.

Finally, the small-label result proved in (K) cannot be transferred to a
fixed nonzero label by taking \(n\to\infty\). Even a bound
\(|R_n(y)|\le C\|y\|^3\) uniform in \(n\) gives a scaled bound proportional
to \(\sqrt n\|y\|^3\), which does not vanish at fixed \(y\ne0\). The note
correctly requires additional control of the two-copy nonlinear
remainder. This is a stated boundary of the result, not a missing step
in the theorem being checked.

There are no remaining substantive gaps in equations (1)--(17) with the
revised endpoint conventions and limiting-Gaussian interpretation. Their
exact scope is finite \(m,d,L\), finitely many fixed queries, initialized
Gram fluctuations, onset, and the true derivative of the trained predictor
at zero label. Uniformity in growing dimensions, convergence of endpoint
moments, and a fixed-label trained fluctuation theorem remain unproved.
