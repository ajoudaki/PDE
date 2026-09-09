# PASS — isolated mathematical audit of UNIVERSAL_ANGLE_ROUTE.md

Date: 2026-09-05.

**Verdict: PASS within the candidate's expressly partial scope.** The necessary displacement and feature-time bounds, normalized coordinate identities, parity cancellation with its stated conditional radius bound, multiplication obstruction, and affine Gaussian negative-sign fraction are correct. No substantive gap was found in these claims. This verdict does not certify a universal activation, nonlinear response continuation, or any downstream MF/GF/exact-GD theorem. Those conclusions remain OPEN, as the candidate states.

The one wording clarification below concerns uniform convergence of the common map alone. It does not invalidate the joint common/contrast obstruction.

## Isolation and source hashes

The candidate's SHA-256 matches the user-specified digest:

```text
20dbd9164881bf475ec5d684c43b4d122708338a145ae2934b70b3629ca46cdf
/tmp/l3-two-sample-Un7kw9/UNIVERSAL_ANGLE_ROUTE.md

e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd
/tmp/l3-two-sample-Un7kw9/CONTRACT.md

40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4
/tmp/l3-two-sample-Un7kw9/SYMMETRY_RADIAL_CLOCK.md

9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
/etc/codex/skills/solve-math-rigorously/SKILL.md
```

The skill was read in full. The candidate was read in full. The contract and the permitted symmetry/raw-metric/energy dependency were inspected, including the affine local-existence equations needed for the small-time claim. No other route proposal, history, or review was read. The optional generic local proof was unnecessary: the particular fixed Gaussian conditioning calculation is derived below. No agents, numerical experiments, or finite-width flow construction were used. Novelty and the candidate's historical/procedural remarks are outside this mathematical audit. The candidate was not edited.

## 1. Necessary displacement and feature-time divergence: PASS

Use opposite labels with their overall sign absorbed into the readout. All norms below are the separate population norms and the raw metric specified in the contract. Write \(\Delta w=w-w_0\). Since \(\|v\|=\sqrt d\,\delta\),

\[
\|D_1-D_{1,0}\|_2^2
=\mathbb E|\Delta w\cdot v|^2
\le d\delta^2\mathbb E\|\Delta w\|^2
\le\delta^2R^2.
\]

The initial covariance gives \(\|D_{1,0}\|_2=\delta\). Hilbert--Schmidt perturbations satisfy
\(\|A\|_{\rm op},\|B\|_{\rm op}\le K+R\). The pointwise Lipschitz inequality gives

\[
\left\|\frac{\phi(z_1)-\phi(z_2)}2\right\|_2
\le L\left\|\frac{z_1-z_2}2\right\|_2.
\]

Applying it successively through the three activations, and using \(\|C\|_2\le R\), proves

\[
|g|\le\delta L^3R(1+R)(K+R)^2
\le\delta L^3K^2(1+R)^4.
\]

The final inequality uses \(R\le1+R\) and \(K+R\le K(1+R)\), valid for \(K\ge1\). No symmetry of the current state, monotonicity of \(\phi\), or control of its intercept is needed. Thus (1) and the rearrangement (2) hold for every fixed Lipschitz activation with a finite positive Lipschitz bound.

For the time statement, on a constructed strong feature-gradient path with the stated chain rule and energy identity, \(g(0)=0\) and

\[
R(S)^2
=\left\|\int_0^S\Theta'(s)\,ds\right\|^2
\le S\int_0^S\|\Theta'(s)\|^2ds
=Sb.
\]

This proves (3). For fixed \(b,L,K>0\), the necessary scales as \(\rho\uparrow1\) are

\[
R=\Omega(\delta^{-1/4})=\Omega((1-\rho)^{-1/8}),\qquad
S=\Omega(\delta^{-1/2})=\Omega((1-\rho)^{-1/4}).
\]

Here \(K\) is held fixed, as permitted by the bounded initialized Gaussian actions. The statement about arbitrary Lipschitz activations does not assert existence or regularity of a gradient flow for every nonsmooth activation. The time bound is conditional on the constructed gradient path and energy identity. Constant activations cannot reach the opposite-label target and do not supply an exception. These are necessary lower bounds, not matching upper bounds or a nonexistence theorem.

## 2. Normalized common/contrast coordinates, including the antipodal case: PASS

For \(\mu>0\), the vectors
\(m/(\sqrt d\,\mu)\) and \(v/(\sqrt d\,\delta)\) are orthonormal. The corresponding components of \(w\) are \(U/\sqrt d\) and \(V_1/\sqrt d\). Hence the restriction of \(d\mathbb E\|dw\|^2\) is exactly

\[
\|dU\|_2^2+\|dV_1\|_2^2.
\]

The normalized Gaussian root coordinates \(U,V_1\) are independent standard Gaussians. A feature-gradient update of \(w\) lies in their span, so the remaining component is frozen.

At \(\rho=-1\), \(\mu=0\), \(\delta=1\), and \(M_1=0\); \(U\) is omitted entirely. There is no inverse Gram matrix or division by zero. In particular \(P_1(0,V_1)=1\), so \(M_2=A\mathbf1\): the common fields at later layers are retained even for antipodal inputs.

Substituting \(z_a^{(\ell)}=M_\ell+(-1)^{a-1}\delta V_\ell\) gives (4)--(5) directly, including \(g=\delta G_\delta\). Both hidden operators and their common-field actions remain present.

For the scalar derivatives,

\[
\phi'(z)=1+\frac e{1+z^2},\quad
\phi''(z)=\frac{-2ez}{(1+z^2)^2},\quad
\phi'''(z)=\frac{-2e(1-3z^2)}{(1+z^2)^3}.
\]

Thus \(1\le\phi'\le1+e=L\), \(\|\phi''\|_\infty\le2e\), and \(\|\phi'''\|_\infty=2e\). Differentiation gives

\[
P_M=Q_V=a,\quad P_V=\delta^2b,\quad Q_M=b,
\qquad
b=\frac{-2eMV}{[1+(M+\delta V)^2][1+(M-\delta V)^2]}.
\]

In particular the off-diagonal factors in (6) are correct. The identities

\[
b=\frac V2\int_{-1}^1\phi''(M+t\delta V)\,dt,
\qquad
Q_{MM}=\frac V2\int_{-1}^1\phi'''(M+t\delta V)\,dt,
\]
\[
Q_{MV}=\frac{\phi''(M+\delta V)+\phi''(M-\delta V)}2,
\qquad Q_{VV}=\delta^2Q_{MM}
\]

prove every bound in (7), with the stated constants and powers of \(\delta\). Symmetric second- and third-order Taylor remainders give respectively \(e\delta^2V^2\) and \((e/3)\delta^2|V|^3\), as in (8). Fourth and sixth moments suffice for the displayed \(L^2\) remainder rates.

At fixed \(M,V\in L^2\), convergence of \(Q_\delta\) to \(\phi'(M)V\) follows pointwise and in \(L^2\), since its difference is bounded by \(2L|V|\). The analogous convergence for \(P_\delta\) also holds.

**Minor wording clarification, candidate lines 146--149:** the common map alone actually has the uniform bound

\[
\|P_\delta(M,V)-\phi(M)\|_2\le L\delta\|V\|_2.
\]

Thus a denial of uniform convergence for \(P_\delta\) alone would be too broad. The candidate's joint common/contrast warning is correct: uniform convergence of \(Q_\delta\) fails on arbitrary \(L^2\) balls. For an analytic witness, take \(M=0\) and \(V_\delta=\delta^{-1}\mathbf1_{E_\delta}\), with \(\mathbb P(E_\delta)=\delta^2\). Then \(\|V_\delta\|_2=1\), but

\[
\|Q_\delta(0,V_\delta)-\phi'(0)V_\delta\|_2
=e(1-\pi/4)>0.
\]

This clarification leaves the obstruction and all numbered estimates intact.

The isometric parameter coordinates also give \(\nabla g=\delta\nabla G_\delta\) for each fixed \(\delta>0\). Therefore \(u=\delta s\) gives (9), and \(g=1\) means \(G_\delta=1/\delta\). At \(\delta=0\) the tangent forward maps are well-defined on \(L^2\), but their common-field derivatives contain \(CV\phi''(M)\), which need not be in \(L^2\). The note correctly makes no assertion of gradient convergence on arbitrary Hilbert balls or of a bounded target after this rescaling.

## 3. Parity cancellation and all curvature factors: PASS

Use precisely the constructed-state exchange involutions from the permitted dependency. With opposite labels they satisfy

\[
T_\ell z_1^{(\ell)}=z_2^{(\ell)},\quad
T_\ell q_{1,\ell}=-q_{2,\ell},\quad
T_\ell M_\ell=M_\ell,\quad T_\ell D_\ell=-D_\ell.
\]

The identity for the backward inputs follows at the top from the odd readout, and at lower layers from the intertwining of the operators and their adjoints with the involutions. Hence \(q_M\) is odd and \(q_D\) is even. Measure preservation gives

\[
\mathbb E[q_M\phi''(M+D)]
=-\mathbb E[q_M\phi''(M-D)],
\quad
\mathbb E[q_D\phi''(M+D)]
=\mathbb E[q_D\phi''(M-D)].
\]

Adding these identities with the appropriate halves proves (10). This argument uses sample-exchange parity, not oddness in a scalar neuron coordinate or cross-layer neuron pairing.

Because \(|\phi''(M+D)-\phi''(M-D)|\le4e|D|\), the first summand is at most

\[
2e\mathbb E|q_MD|\le2e\|q_M\|_2\|D\|_2.
\]

At layer \(\ell\), forward propagation contributes \(L^{\ell-1}(K+R)^{\ell-1}\), and the backward input contributes \(L^{3-\ell}(K+R)^{3-\ell}\). Together with the bottom and readout bounds, their product is

\[
\|q_{M,\ell}\|_2\|D_\ell\|_2
\le\delta L^2R(1+R)(K+R)^2.
\]

This verifies (11)--(12) at all three layers; no extra gate or label factor is missing. If \(R\le M_*\delta^{-1/4}\), then, since \(0<\delta\le1\), each of \(R\), \(1+R\), and the two factors \(K+R\) is bounded by its corresponding constant times \(\delta^{-1/4}\). The four powers cancel the prefactor \(\delta\), proving exactly (13).

At the top \(q_{D,3}=0\), so this controls the complete scalar return \(\mathbb E[C\phi''(z_1^{(3)})]\); applying the involution makes the sample-2 return its negative. At lower layers (10) retains its second summand, with (14) obtained directly from the two top gates. The candidate does not infer a nonlinear radius upper bound, a bound for the full causal response row, or control of its random source-derivative factors from this scalar calculation.

## 4. Rare-field multiplication obstruction: PASS at the stated scope

For \(0<\eta\le1\), on \(E_+\) the gate difference divided by two is

\[
\frac{\phi'(2)-\phi'(0)}2=-\frac{2e}{5},
\]

and on \(E_-\) it is \(+2e/5\). Multiplying by the respective values \(\pm\eta^{-1/2}\) of \(C\) gives the same value \(-2e/(5\sqrt\eta)\) on both sets. Consequently

\[
\|C\|_2=1,\quad \|D\|_2=\sqrt\eta,\quad
\left\|C\frac{\phi'(M+D)-\phi'(M-D)}2\right\|_2^2
=\frac{4e^2}{25}.
\]

All claimed parities hold. Taking \(\delta=\sqrt\eta\) gives \(\|D/\delta\|_2=1\) as stated. Thus bounded second moments and exchange symmetry cannot alone force this product norm to vanish with the contrast norm, even after normalization.

This is a counterexample to a general multiplication estimate. It neither constructs a reached Gaussian-network state nor proves that the actual \(B^*\) fails to attenuate the product. Operator-specific cancellation, mixed moments, or reached-state tail information are not ruled out. The candidate explicitly respects this limitation.

## 5. Restoring sign and the affine Gaussian fraction 1/4: PASS

Direct subtraction of the two rational gates gives

\[
\partial_MF=\frac{-2eMD}{[1+(M+D)^2][1+(M-D)^2]},
\quad
MC\partial_MF=\frac{-2eCDM^2}{[1+(M+D)^2][1+(M-D)^2]}.
\]

The denominator is strictly positive. For a local common-coordinate update \(M'=C\partial_MF\), this is \(\frac12(M^2)'\), and is nonpositive under \(CD\ge0\). This checks (16); it is not a claim about the sign of every term in a coupled network update.

For the affine comparator, the permitted dependency supplies local strong existence for the polynomial feature gradient. With the overall label sign absorbed, \(C'=D_3\), \(C(0)=0\), and all gates equal one. Strong continuity therefore gives

\[
C(s)=sD_{3,0}+o_{L^2}(s),\qquad
q_{M,2}(s)=B_s^*C(s)=sB_0^*B_0D_{2,0}+o_{L^2}(s).
\]

There is no missing physical-time factor two: these are feature-time expansions with \(\Theta'=\nabla g\).

Here is the fixed-transcript conditioning in detail. At finite width write \(d=D_{2,0}\in\mathbb R^n\) and \(y=B_0d\), with ordinary Euclidean norms in this paragraph. The vector \(d\) is independent of \(B_0\). Conditional on \(d,y\), each row of \(B_0\) has mean \(y_i d^T/\|d\|^2\) and residual covariance \(n^{-1}P_{d^\perp}\). The residual rows are conditionally independent. Therefore

\[
B_0^Ty\mid(d,y)
\ \overset{\mathrm{law}}{=}
\frac{\|y\|^2}{\|d\|^2}d
+\frac{\|y\|}{\sqrt n}P_{d^\perp}Z,
\qquad Z\sim N(0,I_n),
\]

where \(Z\) can be chosen independent of \((d,y)\). This proves the claimed mean and covariance, including the factor \(1/n\).

The first contrast root has iid \(N(0,\delta^2)\) entries. Conditional on that root, the coordinates of \(d=A_0D_{1,0}\) are iid centered Gaussians with variance \(\|D_{1,0}\|^2/n\to\delta^2\). Thus \(d\) has limiting coordinate law \(\delta X\), and \(\|d\|^2/n\to\delta^2\). Conditional on \(d\), the coordinates of \(y\) are iid \(N(0,\|d\|^2/n)\). The elementary Gaussian square law of large numbers yields

\[
\frac{\|y\|^2}{\|d\|^2}\longrightarrow1,\qquad
\frac{\|y\|^2}{n}\longrightarrow\delta^2.
\]

The removed projection has empirical RMS

\[
\|(I-P_{d^\perp})Z\|_n
=\frac{|d^TZ|}{\sqrt n\,\|d\|},
\]

whose conditional squared expectation is \(1/n\); it therefore vanishes in probability. Before this vanishing projection, \(Z\) is independent of \(d\). The joint limiting coordinate law is consequently exactly

\[
\bigl(D_{2,0},B_0^*B_0D_{2,0}\bigr)
\ \overset{\mathrm{law}}{=}\bigl(\delta X,\delta(X+Y)\bigr),
\qquad X,Y\text{ independent }N(0,1).
\]

This proves (17) as a population coordinate law, not as an exact finite-width iid identity.

Since \(\delta>0\), negativity of the product is equivalent to \(X(X+Y)<0\). The regions \(X>0,Y<-X\) and \(X<0,Y>-X\) are each wedges of angle \(\pi/4\). Rotational invariance therefore gives total probability \((\pi/2)/(2\pi)=1/4\), proving (18). The limiting product has no atom at zero, and its expectation is \(\delta^2>0\). All these conclusions include \(\rho=-1\).

Finally, \(D_2(s)\to D_{2,0}\) in \(L^2\) and the displayed expansion gives \(q_{M,2}(s)/s\to B_0^*B_0D_{2,0}\) in \(L^2\). Cauchy--Schwarz implies

\[
D_2(s)q_{M,2}(s)/s
\longrightarrow D_{2,0}B_0^*B_0D_{2,0}\quad\text{in }L^1.
\]

Convergence in probability and absence of mass at zero then imply convergence of the negative-sign probability to \(1/4\). Thus the last small-time sign statement is justified, rather than inferred solely from a formal expansion. At \(e=0\) the curvature itself vanishes; what this calculation disproves is the proposed pointwise nonnegativity of the contrast/backward product. It does not establish nonlinear dynamical failure or exclude an averaged estimate, exactly as the candidate explains.

## Scope of the verdict

The radial/energy dependency gives a finite pair-dependent pre-target budget only on a constructed strong uncut branch; it supplies neither existence past a limiting state nor the missing response continuation. The candidate preserves this qualification and labels the universal theorem and downstream bridges OPEN. The scoped verdict is PASS, with the common-map wording clarification above and no required mathematical repair to the numbered partial results.

The candidate and dependency digests were rechecked after the review was written and remained identical to the values listed above.
