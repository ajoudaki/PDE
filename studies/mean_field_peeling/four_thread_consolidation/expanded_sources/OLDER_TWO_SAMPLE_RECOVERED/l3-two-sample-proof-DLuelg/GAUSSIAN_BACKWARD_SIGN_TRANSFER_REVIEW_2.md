# Independent adversarial review of the Gaussian backward sign transfer

## Verdict and provenance

**PASS for the stated initialization lemma.** I found no mathematical error requiring a repair to the scalar transfer, either actual reused transpose law, or the stated joint empirical and moment convergence in probability. The proof uses the specified finite arrays, and the two conditioning arguments are valid for those arrays. The comments at the end concern making already satisfied hypotheses and routine calculations more explicit; they do not require changing the result.

This is an independent mathematical audit, not an adoption of the candidate's reference to an earlier audit. No prior review, project ledger, history, other mathematical file, agent, experiment, or external mathematical source was used. I read the procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` in full and reconstructed the needed Gaussian arguments directly.

The mathematical inputs were exactly:

1. `/tmp/l3-two-sample-proof-DLuelg/GAUSSIAN_BACKWARD_SIGN_TRANSFER.md`, all 419 lines, 18,407 bytes. Its measured SHA256 was
   `5ff166e2c9ab7faf504be74795d513d61fae14a1b8d789e3759606dba09670e8`,
   exactly matching the hash supplied in the request. The same hash was measured again after the mathematical inspection, before writing this review, and after creating the review.
2. `/tmp/l3-two-sample-proof-DLuelg/GAUSSIAN_INITIAL_SIGNED_RESPONSE.md`, only the text of lines 1–315, comprising Sections 1–4 and the blank line 315. This prefix contains 13,159 bytes and has SHA256
   `9467e7031ad054239bece6a80b4ee3d7a8270e57f7d2887bafb774baf2370c08`.
   This is a hash of the permitted prefix, including its line endings, not a hash of the whole dependency. It was rechecked after creating the review using the byte stream from `head -n 315` on that dependency. The candidate's historical whole-dependency hash and audit status were not independently verified and are not evidence for this verdict.

The provenance checkpoint before writing was 2026-09-06 15:42:34 UTC. Line references below refer to the candidate unless explicitly described as dependency lines. The candidate was not edited. This review concerns initialization only and imposes no global continuation, trained-path, or time-dependent response requirement.

## 1. Scalar identities, exchanges, and endpoint behavior

Candidate lines 19–43 are correct. Here is a direct verification of the facts imported from the permitted dependency.

Write \(f(x)=\arctan x\), \(h(x)=(1+x^2)^{-1}\), and

\[
w_q(u,v)=e^{-u-v-q(u^2+v^2)/2}.
\]

The three Laplace formulas in dependency lines 53–65 follow by integrating \(e^{-(1-ix)u}\) for \(h\), differentiating under an integrable bound for \(f''\), and integrating \(h=f'\) from zero for \(f\). The bound \(|\sin(ux)|/u\le |x|\) controls the first integral; \(e^{-u}\) and \(u e^{-u}\) control the two differentiations.

For the Gaussian pair, applying the scalar Gaussian characteristic function to \(uZ_1\pm vZ_2\) gives the stated cosine/cosine and sine/sine expectations. This remains true at singular covariance: a zero-variance linear combination is identically zero. Consequently

\[
B_q(t)=\iint w_q(u,v)\cosh(tuv)\,du\,dv,
\qquad
J_q(t)=\frac12\iint\left(\frac uv+\frac vu\right)
w_q(u,v)\sinh(tuv)\,du\,dv.
\]

The exchanges here are valid, including the apparently singular factors \(u/v\) and \(v/u\). Before expectation is exchanged with integration,

\[
\mathbb E|\sin(uZ_1)\sin(vZ_2)|
\le uv\mathbb E|Z_1Z_2|\le uvq.
\]

Thus the nonsymmetric curvature integrand is bounded in absolute expectation by \(qu^2e^{-u-v}\); its transposed version has the corresponding \(qv^2e^{-u-v}\) bound. The cosine product is bounded by \(e^{-u-v}\). These bounds justify both Fubini and the symmetrization.

For every \(|t|\le q\),

\[
e^{-q(u^2+v^2)/2+|t|uv}\le1.
\]

Together with \(|\sinh s|\le |s|e^{|s|}\), this gives the dependency's domination bounds for the integrands and their covariance derivatives. In particular, the differentiated \(B\) integrand is bounded by \(uv e^{-u-v}\), and the differentiated symmetrized \(J\) integrand by \((u^2+v^2)e^{-u-v}/2\). These are integrable bounds uniform over the entire closed covariance interval. No interior-only differentiation argument is being extended without justification to an endpoint.

Evenness and strict positivity of \(B_q\), oddness of \(J_q\), and strict positivity of \(J_q'(t)\) follow from these integrals. Differentiating their difference gives exactly

\[
T_q'(t)=-\frac14\iint w_q(u,v)
\bigl((u-v)^2e^{tuv}+(u+v)^2e^{-tuv}\bigr)\,du\,dv<0.
\]

The second summand is strictly positive throughout the positive quadrant; the strict inequality therefore also holds for the continuous one-sided endpoint derivatives. The displayed integrand is dominated by an integrable polynomial times \(e^{-u-v}\).

Finally, \(g(x)=f(x)h(x)\) has bounded derivative

\[
g'(x)=h(x)^2+f(x)f''(x).
\]

Integrating \(g'\) against a variance-\(q\) Gaussian density, whose boundary term vanishes, gives

\[
D_q=\frac1q\mathbb E\frac{Z\arctan Z}{1+Z^2}>0.
\]

The numerator is positive except at zero, and a nondegenerate Gaussian assigns zero probability to zero. Since \(T_q(q)=D_q\), integration of the strictly negative derivative proves \(T_q(t)>D_q\) for every \(t<q\), including \(t=-q\). This verifies every scalar fact used in (1).

## 2. Exact transfer, labels, and both singular endpoints

Candidate lines 47–112 are algebraically and analytically correct. The random variables \(Q_a,D_a\) have all finite moments because the activation and its derivatives are bounded and the independent Gaussian source has finite moments, whether or not its covariance is invertible.

The derivative is taken in the ambient variables before evaluating their Gaussian law. Holding the Gaussian source and the deterministic coefficients fixed gives

\[
\partial_bD_a
=\mathbf1_{a=b}\phi''(Z_a)
\left(\zeta_a+\sum_jC_{aj}\phi(Z_j)\right)
+\phi'(Z_a)C_{ab}\phi'(Z_b).
\]

There is no missing derivative of the feature sum. The expectation of its source contribution vanishes by independence and centering. The constant part of each feature vanishes against the odd function \(\phi''\), so

\[
\mathbb E[\phi''(Z_a)\phi(Z_a)]=-\varepsilon^2J_q(q),
\qquad
\mathbb E[\phi''(Z_a)\phi(Z_j)]=-\varepsilon^2J_q(c)
\quad(j\ne a).
\]

As \(y_aC_{aj}=M_{aj}\), the diagonal entry of the new label-left-weighted matrix is

\[
\varepsilon^2\bigl(B_q(q)m-J_q(q)m-J_q(c)b\bigr)
=\varepsilon^2\bigl(D_qm-J_q(c)b\bigr),
\]

and the off-diagonal entry is \(\varepsilon^2B_q(c)b\). Thus (3) has the correct signs, factor, and matrix orientation. Left multiplication by \(Y\), rather than an inadvertent conjugation of \(C\), is used consistently.

Put \(\lambda_y=m+\sigma b\), \(\lambda_\perp=m-\sigma b\). Substituting their inverse expressions into the two eigenvalues gives

\[
\begin{aligned}
\nu_y&=\frac{\varepsilon^2}{2}
\bigl[(D_q+B_q(c)-\sigma J_q(c))\lambda_y
+(D_q-B_q(c)+\sigma J_q(c))\lambda_\perp\bigr],\\
\nu_\perp&=\frac{\varepsilon^2}{2}
\bigl[(D_q-B_q(c)-\sigma J_q(c))\lambda_y
+(D_q+B_q(c)+\sigma J_q(c))\lambda_\perp\bigr].
\end{aligned}
\]

These are exactly (4), using \(T_q(\sigma c)=B_q(c)-\sigma J_q(c)\) and \(T_q(-\sigma c)=B_q(c)+\sigma J_q(c)\). Since \(T_q(t)\ge D_q>0\), the strict cone implication (5) follows term by term. Its strictness does not require either off-diagonal mixing coefficient to be strictly negative.

For an explicit endpoint check, set \(A=B_q(q)\), \(J=J_q(q)>0\), and \(D=A-J>0\). If \(\sigma c=q\), then

\[
\nu_y=\varepsilon^2D\lambda_y,
\qquad
\nu_\perp=\varepsilon^2(-J\lambda_y+A\lambda_\perp).
\]

If \(\sigma c=-q\), then

\[
\nu_y=\varepsilon^2(A\lambda_y-J\lambda_\perp),
\qquad
\nu_\perp=\varepsilon^2D\lambda_\perp.
\]

Both pairs have the asserted strict signs. In particular, the proof does not divide by a vanishing covariance eigenvalue. It also does not replace an ambient partial derivative by a derivative along \(Z_2=\pm Z_1\). Such a replacement would change the problem and can give incorrect derivatives.

The source covariance is absent from the expected derivative but remains present in the reverse law and its second moments. The candidate makes this distinction correctly.

## 3. The actual initial law and the starting matrix

The finite normalization in lines 181–200 is internally consistent with the initial scalar laws in the permitted dependency. For a matrix with independent \(N(0,1/n)\) entries acting on an independent \(n\)-by-2 feature array \(h\), each forward row has conditional covariance \(h^Th/n\). The corresponding reverse Gaussian covariance is \(u^Tu/n\), as derived below. There is no missing \(n\), \(\sqrt n\), or sample-average factor in (6) or (7). The factor \(1/2\) is already present in the displayed finite top input \(u^{(3)}\).

The dependency's covariance map can be verified from the same elementary integrals. For variance \(s>0\), define \(F_s(t)=\mathbb E[f(X)f(Y)]\) and \(R(s)=F_s(s)\). The double sine representation is absolutely integrable by the bound \(s e^{-u-v}\); differentiation in \(t\) is dominated by \(e^{-u-v}\). It follows directly that

\[
F_s'(t)=B_s(t)>0,\qquad F_s(0)=0,
\qquad 0<R(s)<\pi^2/4.
\]

The actual layer-two covariance entries are

\[
q_2=1+\varepsilon^2R(1),
\qquad c_2=1+\varepsilon^2F_1(\rho).
\]

Here \(c_2\ge1-\varepsilon^2R(1)>0\), and

\[
q_2-c_2
=\frac{\varepsilon^2}{2}\mathbb E[(f(G_1)-f(G_2))^2]>0.
\]

For every allowed \(\rho<1\), the Gaussian difference \(G_1-G_2\) has positive variance and is nonzero almost surely. Strict monotonicity of \(f\) proves the strict inequality, also at \(\rho=-1\). Thus \(K_1\), with diagonal \(q_2\) and off-diagonal \(c_2\), is positive definite.

The top covariance entries are

\[
q_3=1+\varepsilon^2R(q_2),
\qquad c_3=1+\varepsilon^2F_{q_2}(c_2).
\]

Since \(0<c_2<q_2\), strict increase of \(F_{q_2}\) gives

\[
1<c_3<q_3<1+\pi^2/400.
\]

Consequently \(K_2\) is positive definite as well. Exchangeability gives equal limiting diagonal entries at each layer. Finite empirical diagonal entries need not be equal, and the proof nowhere assumes they are.

The geometric argument in lines 230–237 gives the same conclusion. At \(\rho=-1\), the two first-layer features have the form \(1+\varepsilon f(G)\), \(1-\varepsilon f(G)\). A homogeneous linear relation between them would make both its constant and its nonconstant odd part zero. Their affine relation that their sum is two is not a homogeneous dependence and does not make their second-moment matrix singular. For interior correlations, the positive joint density and strict monotonicity give the stated independence of the feature coordinates in the linear-algebraic sense.

The starting response matrix can also be checked without accepting the dependency's conclusion on authority. With \(V=(\phi(Z_1)+\sigma\phi(Z_2))/2\) and \(U^{(3)}_a=V\phi'(Z_a)\),

\[
\partial_bU^{(3)}_a
=\frac{y_b}{2}\phi'(Z_b)\phi'(Z_a)
+\mathbf1_{a=b}V\phi''(Z_a).
\]

Oddness and exchangeability give

\[
\mathbb E[V\phi''(Z_a)]
=-\frac{y_a\varepsilon^2}{2}
\bigl(J_{q_3}(q_3)+\sigma J_{q_3}(c_3)\bigr).
\]

Therefore

\[
M^{(3)}=YC^{(3)}
=\frac{\varepsilon^2}{2}
\begin{pmatrix}
D_{q_3}-\sigma J_{q_3}(c_3)&\sigma B_{q_3}(c_3)\\
\sigma B_{q_3}(c_3)&D_{q_3}-\sigma J_{q_3}(c_3)
\end{pmatrix}.
\]

Its eigenvalues are \(\varepsilon^2[D_{q_3}+T_{q_3}(\sigma c_3)]/2>0\) and \(\varepsilon^2[D_{q_3}-T_{q_3}(-\sigma c_3)]/2<0\). Strictness follows from \(|c_3|<q_3\), for both labels. The exceptional arbitrary-Gaussian endpoint in the dependency is therefore absent from the actual top initialization. Applying the transfer at \((q_2,c_2)\) establishes the claimed signs of \(M^{(2)}\).

The finite objects are explicitly backward velocities with the hidden initialization fixed, not ordinary deltas at a zero readout. The proof does not accidentally identify those two quantities. The static queries have a complete mathematical definition without needing a physical-time normalization beyond the one stated.

## 4. Forward convergence and inverse control

The conditional averaging argument in lines 202–241 is sufficient for every forward empirical limit subsequently used. Indeed, \(|\phi|<7/6\) bounds the conditional covariance matrices in a fixed compact set of positive semidefinite matrices. For any fixed continuous test \(g\) of polynomial growth,

\[
|g(x)|\le A(1+\|x\|^p),
\]

all corresponding conditional second moments are bounded by a constant depending on the test. Conditional independence of the new rows then gives a conditional variance at most \(C_g/n\) for their empirical average. Conditional Chebyshev removes the fluctuation.

The conditional mean is continuous in the covariance matrix: represent a Gaussian vector as \(K^{1/2}N\), use the uniform bound on \(K^{1/2}\), and dominate by a polynomial in the fixed standard Gaussian \(N\). The square-root continuity argument in lines 222–228 is valid. Bounded roots have convergent subsequences; every subsequential limit is positive semidefinite and squares to the limiting matrix; uniqueness of that root identifies the limit. Uniqueness follows since a root commutes with its square and acts by the nonnegative scalar square root on each eigenspace of the square. Singular source covariances cause no exception.

Induction from the independent root rows proves the needed forward laws, including \(K_{\ell,n}\to K_\ell\) and \(\|z^{(2)}_0\|_F/\sqrt n=O_p(1)\). Since the limiting feature matrices are positive definite for each fixed allowed \(\rho\), their smallest eigenvalues are bounded away from zero on suitable neighborhoods. Convergence puts \(K_{1,n},K_{2,n}\) in those neighborhoods with probability tending to one, proving the inverse bounds used later.

Discarding the complementary events is legitimate for convergence in probability. No inverse-moment estimate or bound uniform as \(\rho\uparrow1\) is needed for the stated result, and neither is claimed.

## 5. Exact finite transpose conditioning

The projection identity in lines 243–273 is correct in both applications. The needed exogeneity condition is that, conditional on the forward input \(h\), the matrix \(W\) still has its independent \(N(0,1/n)\) entry law. This condition holds in both uses because \(h^{(2)}_0\) is independent of \(W^{(3)}_0\), and \(h^{(1)}_0\) is independent of \(W^{(2)}_0\).

For a row \(w\), conditioning on \(wh=z_i\) determines its projection onto the column span of \(h\). Its remaining projection is a centered Gaussian with covariance \((I-\Pi_h)/n\). The parallel and perpendicular projections have zero cross covariance, and their joint Gaussian characteristic function factors. Additional exposed variables in the two applications do not reveal this perpendicular part.

Thus, in an exact conditional Gaussian representation,

\[
W=z(h^Th)^{-1}h^T+\widetilde W(I-\Pi_h),
\qquad
\Pi_h=h(h^Th)^{-1}h^T.
\]

One can realize this on an extension of the original probability space by adding independent Gaussian parallel components to the original perpendicular residual. The resulting \(\widetilde W\), conditional on the exposure, has the full iid Gaussian entry law. Hence the representation can be used without modifying the distribution of the original arrays.

For an exposed reverse input \(u\), transposition gives

\[
W^Tu=hK_n^{-1}T_n+(I-\Pi_h)b,
\quad
K_n=h^Th/n,quad T_n=z^Tu/n,quad b=\widetilde W^Tu.
\]

For row indices \(i,j\) and sample indices \(a,b\), the conditional covariance of the new Gaussian array is

\[
\operatorname{Cov}(b_{i,a},b_{j,b}\mid\text{exposure})
=\mathbf1_{i=j}\frac1n\sum_k u_{k,a}u_{k,b}.
\]

This proves the claimed conditional row independence and covariance \(S_n=u^Tu/n\). It is the uncentered second moment. Subtracting a mean or a regression covariance would be wrong: the forward exposure has removed directions in the input-coordinate space through \(I-\Pi_h\); it has not centered or projected the exposed reverse vector \(u\) in the output-coordinate space.

Since \(\Pi_h\) is an orthogonal projection,

\[
\mathbb E[\|\Pi_h b\|_F^2/n\mid\text{exposure}]
=\operatorname{rank}(\Pi_h)\operatorname{tr}(S_n)/n.
\]

For any \(\delta,L>0\), the probability that \(\|\Pi_hb\|_F/\sqrt n>\delta\) is at most

\[
\mathbb P(\operatorname{tr}S_n>L)
+\frac{2L}{n\delta^2}
\]

on the invertibility event. Tightness of the trace, followed by \(n\to\infty\) and \(L\to\infty\), proves the required RMS negligibility. This explicitly verifies that bounded rank alone is not the argument.

## 6. First reused transpose and its joint empirical law

For the first application, expose the complete lower data and \(z^{(3)}_0=W^{(3)}_0h^{(2)}_0\). The reverse input \(u^{(3)}\) is a bounded function of the exposed top forward rows. This is a legitimate application of the preceding conditional representation.

The forward averaging theorem applies to \(z^{(3)}_bu^{(3)}_a\), which is continuous with at most linear growth, and to \(u^{(3)}_au^{(3)}_b\), which is bounded. It gives exactly the two limits in lines 281–282.

For completeness, if \(Z\) has nondegenerate covariance \(K\), its density \(p\) satisfies \(\partial_jp(z)=-(K^{-1}z)_jp(z)\). Integration by parts therefore gives

\[
\mathbb E[Z_bv(Z)]
=\sum_jK_{bj}\mathbb E[\partial_jv(Z)]
\]

for the bounded differentiable top inputs, with zero boundary terms. Taking \(v=U^{(3)}_a\) and \(K=K_2\) yields

\[
T_3=K_2(C^{(3)})^T.
\]

The transpose here is essential and is correctly tracked in the candidate. Combining coefficient convergence, bounded features, and the projection estimate gives (10):

\[
\frac1{\sqrt n}
\|q^{(2)}-h^{(2)}_0(C^{(3)})^T-b_3\|_F\longrightarrow0
\quad\text{in probability}.
\]

The conditional covariance \(S_{3,n}\) of \(b_3\) is uniformly bounded, since each top reverse coordinate is uniformly bounded. The rows of \(b_3\) are independent conditionally, but neither finite unconditional independence nor independence of the actual projected query is asserted.

Let \(g\) be a bounded Lipschitz test of the full layer-two tuple. Replacing \(q^{(2)}\) by its displayed approximation, and \(u^{(2)}\) by its product with the bounded gate, changes the empirical test average by at most a constant times the RMS error. This follows from the Lipschitz bound and the deterministic Cauchy–Schwarz inequality.

Conditional on the exposure, the approximating tests are independent across rows, though not identically distributed. Boundedness gives conditional-average variance \(O(1/n)\). For their conditional means, represent a source row as \(S_{3,n}^{1/2}N\). Replacing this by \(S_3^{1/2}N\) costs at most

\[
C_g\|S_{3,n}^{1/2}-S_3^{1/2}\|\,\mathbb E\|N\|,
\]

uniformly in the fixed forward row; the gate is uniformly bounded. The remaining source-averaged test is a bounded continuous function of \(z^{(2)}_0\). The forward law identifies its empirical limit.

This proves precisely the local joint law

\[
Q^{(2)}=C^{(3)}H^{(2)}_0+\zeta^{(2)},
\qquad U^{(2)}=\operatorname{diag}(\phi'(Z^{(2)}_0))Q^{(2)},
\]

where \(\zeta^{(2)}\sim N(0,S_3)\) is independent of the layer-two forward pair. This independence is obtained because the covariance limit is deterministic; it is not inferred from unjustified independence of finite reused coordinates.

## 7. The unbounded reverse input: second and mixed moments

Lines 318–362 supply the moment argument needed before the second transpose. They do not try to extract unbounded moments from weak convergence alone.

In the first conditional representation, put

\[
\mu_i=C^{(3)}h^{(2)}_{0,i,:},
\qquad d_{i,a}=\phi'(z^{(2)}_{0,i,a}),
\qquad \widehat u_{i,a}=d_{i,a}(\mu_{i,a}+b_{3,i,a}),
\]

interpreting the row feature as a column in the first formula. Both \(\mu_i\) and \(d_i\) are uniformly bounded, and (10) gives

\[
\|u^{(2)}-\widehat u\|_F/\sqrt n=o_p(1).
\]

The exact conditional product mean is

\[
\mathbb E[\widehat u_{i,a}\widehat u_{i,b}\mid\text{exposure}]
=d_{i,a}d_{i,b}\bigl(\mu_{i,a}\mu_{i,b}+(S_{3,n})_{ab}\bigr).
\]

The fourth moment bound required here holds for the actual approximating rows: their Gaussian covariance and their mean and gate are uniformly bounded. Gaussian scalar fourth moments and Cauchy–Schwarz therefore bound the conditional second moment of each product \(\widehat u_{i,a}\widehat u_{i,b}\) by a deterministic constant. Conditional row independence gives variance at most \(C/n\) for the empirical product average.

Its conditional mean converges by the forward law and \(S_{3,n}\to S_3\), giving \(\widehat u^T\widehat u/n\to S_2\). In particular, \(\|\widehat u\|_F/\sqrt n=O_p(1)\). The actual \(u^{(2)}\) is also tight in this norm by the triangle inequality and the RMS approximation; this supplies the implicit tightness used in line 351 without circular reasoning.

For the mixed moment, the centered random part of entry \((b,a)\) of \((z^{(2)}_0)^T\widehat u/n\) is

\[
\frac1n\sum_i z^{(2)}_{0,i,b}d_{i,a}b_{3,i,a}.
\]

Its conditional variance is exactly

\[
\frac{(S_{3,n})_{aa}}{n^2}
\sum_i(z^{(2)}_{0,i,b}d_{i,a})^2
\le\frac Cn\left(\frac1n\sum_i(z^{(2)}_{0,i,b})^2\right)
=O_p(1/n).
\]

To convert this conditional estimate into convergence in probability, restrict the empirical root second moment to be at most a fixed \(R\), apply conditional Chebyshev with the deterministic bound \(CR/n\), and then increase \(R\). This is the tightness restriction specified in the candidate. The conditional mean is an empirical average of a continuous function with linear Gaussian growth. Its limit is \(\mathbb E[Z^{(2)}_bU^{(2)}_a]\), since the independent scalar source has zero mean.

The deterministic inequalities in lines 349–355 are correct:

\[
\left\|\frac{u^Tu-\widehat u^T\widehat u}{n}\right\|_F
\le\frac{\|u-\widehat u\|_F}{\sqrt n}
\frac{\|u\|_F+\|\widehat u\|_F}{\sqrt n},
\]

\[
\left\|\frac{z^T(u-\widehat u)}n\right\|_F
\le\frac{\|z\|_F}{\sqrt n}
\frac{\|u-\widehat u\|_F}{\sqrt n}.
\]

In each case the first relevant error factor tends to zero and the other factors are tight. Correlation between these factors does not invalidate the inequalities or the \(o_p(1)O_p(1)=o_p(1)\) conclusion. Thus (12), including tightness of \(S_{2,n}\), is established for the original finite \(u^{(2)}\).

The scalar \(U^{(2)}\) itself has all finite moments: its mean term and gate are bounded, and its source is Gaussian. This does not by itself prove the finite-array moment convergence; the preceding calculation is what supplies that missing implication, and the candidate includes it.

## 8. Second reused transpose: exposure and coefficient identification

The exposure in lines 366–372 is valid for the same initial \(W^{(2)}_0\). In terms of the original finite arrays, use the sigma-field generated by

\[
z^{(1)}_0,\ h^{(1)}_0,\ z^{(2)}_0,\ W^{(3)}_0.
\]

All of \(h^{(2)}_0,z^{(3)}_0,u^{(3)},q^{(2)},u^{(2)}\) are determined by this field. In particular, \(u^{(2)}\) is a function of \(z^{(2)}_0\) and \(W^{(3)}_0\); its dependence on \(W^{(2)}_0\) is only through the two forward columns \(W^{(2)}_0h^{(1)}_0\).

The original \(W^{(3)}_0\) is independent of the pair consisting of the root and \(W^{(2)}_0\). Including it in this exposure therefore leaves the Gaussian perpendicular residual of \(W^{(2)}_0\) unchanged. This verifies the conditional independence needed for the second application of (8), even though the finite reverse input has complicated dependence across its rows.

These are two separate conditional arguments on the original probability space. They need not form a nested exposure procedure: the first argument exposed the complete lower data, which could include \(W^{(2)}_0\), whereas the second uses the specified smaller information about that matrix. The unconditional convergence statements proved by the first argument remain true when the second conditional calculation is performed. Neither argument requires the first auxiliary Gaussian array to be independent of the second exposure. This is not an illicit reuse of a residual that has been conditioned away.

Consequently the exact second representation is

\[
q^{(1)}=h^{(1)}_0K_{1,n}^{-1}T_{2,n}+(I-\Pi_{h^{(1)}})b_2,
\]

with conditional row covariance \(S_{2,n}\). Its tightness has already been proved, so the projection is negligible in RMS.

To identify the mean coefficient, condition on the independent limiting \(\zeta^{(2)}\). For fixed source value,

\[
U^{(2)}_a(z)=\phi'(z_a)
\left(\zeta^{(2)}_a+\sum_jC^{(3)}_{aj}\phi(z_j)\right).
\]

Both this function and its first derivatives are bounded in \(z\) by a constant times \(1+\|\zeta^{(2)}\|\). The layer-two Gaussian covariance is the positive definite \(K_1\). The density integration-by-parts identity therefore applies for each fixed source value, with vanishing boundary terms. Its integrands are absolutely integrable after averaging over the Gaussian source, so the source averaging can be exchanged with the integrals. It gives

\[
T_2=K_1(C^{(2)})^T,
\qquad
C^{(2)}_{ab}=\mathbb E[\partial_bU^{(2)}_a].
\]

This derivative holds the source, \(C^{(3)}\), and all covariance parameters fixed, precisely as stipulated. The term \(\mathbf1_{a=b}\phi''(z_a)\sum_jC^{(3)}_{aj}\phi(z_j)\) is included, as is the derivative of the feature sum. No limit of finite-network derivatives, derivative of an empirical covariance, or unsupported differentiation through convergence is used. The limiting mixed moment identifies the coefficient directly.

This yields

\[
\frac1{\sqrt n}
\|q^{(1)}-h^{(1)}_0(C^{(2)})^T-b_2\|_F=o_p(1).
\]

The same bounded Lipschitz conditional averaging now applies to the first-layer tuple. The covariance \(S_{2,n}\to S_2\) need only be tight and convergent, not uniformly bounded; bounded tests have uniformly bounded conditional variance regardless of this covariance. Square-root continuity handles singular \(S_2\). The resulting source \(\zeta^{(1)}\sim N(0,S_2)\) is independent of the first-layer root. Singularity of that root at \(\rho=-1\) presents no problem: no inverse of its own covariance is used. The inverse used for this transpose is \(K_1^{-1}\), which is nonsingular.

## 9. Final quadratic moments, complete local tuples, and joint convergence

The final moment paragraph, lines 389–400, is compressed but valid. The following expansion makes explicit why tightness suffices.

For the second transpose write the approximation as \(\widehat q_i=\mu_i+b_{2,i}\), where \(\mu_i=C^{(2)}h^{(1)}_{0,i,:}\) is uniformly bounded. Conditional on its exposure,

\[
\mathbb E[\widehat q_{i,a}\widehat q_{i,b}\mid\text{exposure}]
=\mu_{i,a}\mu_{i,b}+(S_{2,n})_{ab}.
\]

On \(\operatorname{tr}S_{2,n}\le L\), conditional fourth moments give a variance at most \(C_L/n\) for the empirical product average. Its mean converges by the root feature law and \(S_{2,n}\to S_2\). The removed event has arbitrarily small limiting probability by tightness. Thus

\[
\frac1n(q^{(1)})^Tq^{(1)}
\longrightarrow C^{(2)}K_1(C^{(2)})^T+S_2.
\]

For a mixed moment with root coordinate \(z^{(1)}_{i,b}\), the conditional variance of the centered average is

\[
\frac{(S_{2,n})_{aa}}{n^2}\sum_i(z^{(1)}_{i,b})^2.
\]

Restricting both the trace and the empirical root second moment bounds it by \(LR/n\). Conditional Chebyshev, then tightness, gives convergence. The conditional mean converges by the forward law. Mixed moments with bounded root features are even more directly covered by the same calculation. The RMS error transfers these limits to actual \(q^{(1)}\) by the same two deterministic inequalities used above; the approximating query norm is tight by its quadratic calculation, and the actual norm is tight by the triangle inequality.

At layer two, setting the middle gates to one in the Section 3.4 calculation gives

\[
\frac1n(q^{(2)})^Tq^{(2)}
\longrightarrow C^{(3)}K_2(C^{(3)})^T+S_3
\]

and the analogous mixed forward/query moments. Cross products involving one query and one gated query also cause no difficulty: for example their conditional mean is

\[
\mathbb E[\widehat q_{i,a}\widehat u_{i,b}\mid\text{exposure}]
=d_{i,b}\bigl(\mu_{i,a}\mu_{i,b}+(S_{3,n})_{ab}\bigr).
\]

The same bounded fourth moments control the variance of this product, and the bounded gate preserves the RMS error bounds. Products with \(z^{(2)}\) use its empirical second-moment bound; products with features use their boundedness. Together with the forward moments and the already established \(u^{(2)}\) moments, this covers the second-moment control of the complete local tuples. It does not need a claim of uniform finite-array moments of every higher order.

For each fixed finite collection of bounded Lipschitz tests and the specified moment entries, all error probabilities tend to zero; a union bound makes the assertions simultaneous, including across the distinct neuron populations. Independence between those error events or populations is unnecessary. If “empirical convergence” is expressed in a metric for weak convergence of probability measures, one may take a countable determining collection of bounded Lipschitz tests and a metric given by a summable weighted series of their truncated discrepancies. A finite initial part is handled by the union bound and the remaining tail by its deterministic summable bound. The fixed-test proof therefore also gives that formulation of convergence in probability.

The claims do not identify neurons in different layers by equal indices, assert iid finite reused coordinates, assert independence of the two limiting source arrays as a cross-population coupling, or claim almost-sure convergence. None of those stronger properties is needed. Source independence from the forward/root tuple in its own population is exactly what the conditional averaging proves.

## 10. Required repairs versus optional presentation changes

**Required mathematical repairs: none for the stated initialization lemma.** All displayed scalar identities, eigenvalue signs, normalizations, matrix orientations, conditional Gaussian covariances, and moment estimates used in the proof check out under the finite model and parameter range stated in the candidate.

The following are optional presentation improvements, with their precise mathematical status:

1. **Record the exogeneity hypothesis in the generic conditioning paragraph (245–248).** Say explicitly that, conditional on \(h\), \(W\) retains its iid Gaussian entry law. An arbitrary \(W\)-dependent choice of \(h\) would not justify that standalone conditioning formula. Both actual applications already satisfy the hypothesis by the initial independence assumptions, so this is not a missing assumption or a repair to the initialization theorem.
2. **Clarify that the two exposures are separate conditional arguments (277 and 366).** A short phrase such as “recondition the original arrays on the following sigma-field” would prevent an interpretation as a single ever-growing exposure history. The explicit second sigma-field is sufficient and correct; no change to the random arrays, proof, or result is required.
3. **Expand one final moment calculation (389–397), if more detail is desired.** The conditional product mean and the \(C_L/n\) variance bound displayed in Section 9 of this review make the stated analogy precise. The necessary ingredients are already proved in the candidate, so this is an exposition choice rather than an unproved new estimate.

The derivative convention is already explicit enough and should be retained. In particular, the complete static expression must be differentiated before evaluation on a Gaussian support, with deterministic coefficients and independent Gaussian sources held fixed. The remarks about current and historical time-mesh slots are not needed as mathematical premises for either static conditioning argument; they do not supply or require a result about an unexamined time-dependent program.

The scope statements in lines 403–419 are appropriate. The result establishes the indefinite two-mode sign pattern for the deterministic expected-derivative coefficients at both reused hidden transposes at initialization. No global continuation mechanism is needed to validate that claim, and this review makes no judgment about the separate global work.
