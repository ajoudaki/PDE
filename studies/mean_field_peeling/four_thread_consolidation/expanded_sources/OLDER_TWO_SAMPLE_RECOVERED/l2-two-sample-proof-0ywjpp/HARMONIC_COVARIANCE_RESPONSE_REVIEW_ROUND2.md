# Isolated full bounded-note audit — round 2

## Verdict

**PASS within the stated finite, frozen-coefficient law. No required mathematical corrections identified.**

The note's projection identities, covariance-supported contractions, finite-support strictness estimate, complete learned-kernel row bounds, field moment bounds, expected-source-response bounds, attained support obstruction, and specified label-paired sign counterexample all follow from (1)–(4). The constants, the two-sample factors, and the time weights check out. Singular Grams, nonzero means, and the independent bottom Gaussian root are handled correctly.

The verdict does not extend the results to mean-square sensitivities, derivatives of selected statistics, a mesh-uniform strict covariance gap, a complete learned-feedback storage estimate, or a global continuation/limit theorem. The note expressly leaves those conclusions unproved.

## Isolation, procedure, and source integrity

- Mathematical source: /tmp/l2-two-sample-proof-0ywjpp/HARMONIC_COVARIANCE_RESPONSE_TEST.md, read completely, lines 1–651, 23,629 bytes.
- Sole mathematical setup: the explicit finite causal law (1)–(4), its stated activations, and its stated frozen-coefficient differentiation convention.
- Procedural skill read: /etc/codex/skills/solve-math-rigorously/SKILL.md.
- No dependency, prior review, project file, research history, external mathematical source, or other task's work was read. No agents, experiments, numerical tests, or heavy external theorems were used.
- Only this review file was written. The source was not edited.
- The source author's statements about what they previously read are provenance assertions, not mathematical conclusions verifiable from the allowed source. Likewise, references to an external storage identity are assessed only as limitations on what this note proves; the unprovided identity itself is not certified here. “Open” is understood as unresolved by this note, not as a surveyed claim about the literature.

Source SHA-256 before the audit:

    cb1ccec3a4431815b17ef6a8268c168a5feb5f6fe55b0a7c4a6b155ba7c69fb5

Source SHA-256 after the audit:

    cb1ccec3a4431815b17ef6a8268c168a5feb5f6fe55b0a7c4a6b155ba7c69fb5

The before/after hashes match. Source integrity verification passed.

## Coverage ledger

| Source location | Claim audited | Finding |
|---|---|---|
| §1, (1)–(5), lines 37–115 | Exact law, causality, bounded gates/readout, raw second moments, finite derivative integrability | Pass |
| §2, (6), lines 119–134 | Gaussian integration by parts and projection with singular covariance | Pass; no covariance inverse is needed |
| §2, (7)–(10), lines 136–173 | Mean/root/residual decomposition and matrix contraction inequalities | Pass; both mean terms and the independent bottom root are retained |
| §2, (11), lines 175–190 | Nonzero first-update mean of the backward field | Pass; sign and exponential factors verified |
| §3, (12)–(14), lines 194–230 | Supported inverse-covariance norms, supported maps, exact composite defects | Pass |
| §3, (15), lines 232–248 | Nilpotence and finite-prefix supported resolvent bound | Pass; the norm bound concerns the derivative-only composition |
| §4, (16)–(17), lines 252–287 | Elementary quantitative bounded-output projection lemma | Pass, including the tail's factor of two and the kernel case |
| §4, (18)–(20), lines 289–328 | Specific strictness constants, composite contraction factor, zero-Gram cases | Pass; no uniform gap follows from these constants |
| §5, (21)–(22), lines 332–372 | Exact historical time sum and complete learned-kernel row bounds | Pass; the current block of B is included through D |
| §5, (23)–(24), lines 374–396 | Time-weighted output bounds and fixed-horizon uniformity | Pass; the inclusive endpoint contributes T + lambda |
| §6, (25)–(26), lines 400–420 | Actual-field second-moment bounds | Pass; no independence or extra rank factor is required |
| §6, (27)–(30), lines 422–471 | Expected source sensitivities, combined bottom-root/reverse-source direction, scope exclusions | Pass; not bounds on second moments of sensitivities |
| §7, (31)–(34), lines 475–555 | Attained, supported input whose full learned forward response leaves the destination support | Pass; the last input block is supplied by the actual full covariance |
| §8, (35) and its preceding definitions, lines 559–623 | Fully specified label-paired quadratic form, complete first-prefix blocks, supported direction constant in time, positive value | Pass; the initial top source must be allowed to vary |
| §9 and opening synopsis | Separation of finite results, uniform weaker-output bounds, and unresolved stronger conclusions | Pass with the precise scopes below |

## 1. Finite causal setup and early-time bootstrap

The matrix C is positive semidefinite for the stated range, including the singular endpoint rho = -1. The default activation satisfies

\[
|\ell|\le L=1+\pi/20,\qquad |h|,|p|\le b=\sqrt2\,\varepsilon,
\qquad p'=-h.
\]

The stated alternatives sin and arctan also have bounded outputs and the bounded derivatives needed for the finite calculations. Nothing in the projection or row-bound arguments requires the default shift by 1. The support obstruction in §7 does require that shift and is correctly restricted to the default activation.

The cancellation of the constants in H is exact at every time:

\[
w_k=\lambda\sum_{r<k}\bigl(h(Z_{r1})-h(Z_{r2})\bigr).
\]

There are k prior times and two terms per time, so

\[
|w_k|\le2b\lambda k,\qquad
|\delta_{ka}|\le2b^2\lambda k.
\]

This verifies (5), including the factors later used in (18), (21), and (24)–(26).

For fixed finite coefficients the derivative-integrability assertion is justified directly. In the bottom population,

\[
|q_i|\le|\zeta_i|+L\sum_{j\le i\ {\rm in\ time}}|B_{ij}|.
\]

Differentiating the finite causal bottom recursion introduces bounded activation derivatives, finitely many such q factors, and earlier derivatives. Induction bounds each first source derivative by a polynomial in the finitely many Gaussian coordinates, with constants depending on the selected finite coefficients. In the top population, w is bounded on the finite prefix and the gate derivatives are bounded; differentiating its causal recursion gives finite bounds for fixed A. These facts justify the integrations by parts used here. They provide no uniform-in-prefix derivative bound.

Several later calculations use the following consequences of (1)–(4):

\[
\delta_0=0,\quad \Sigma_{0r}=\Sigma_{r0}=0,\quad
\zeta_0=0\ {\rm a.s.},\quad D_{0r}=B_{0r}=0.
\]

Here delta at time zero is identically zero as a function of the xi slots when the deterministic readout root is fixed. Thus its xi derivatives vanish, not just its attained value. Consequently q_0 = 0 almost surely,

\[
F_1=F_0=\ell(G),\qquad
\Gamma_{\{0,1\},\{0,1\}}=
\begin{pmatrix}K&K\\K&K\end{pmatrix}.
\]

The centered Gaussian difference xi_1 - xi_0 has zero covariance, hence xi_1 = xi_0 = X almost surely. Also Z_0 = xi_0 and Z_1 = xi_1 because A is strict in time and delta_0 is identically zero. These conclusions remain valid when these initial times are embedded in the longer prefix used in §7.

This bootstrap concerns attained values and the stated formal derivatives separately: F_1 can have a nonzero formal derivative with respect to the zero-variance reverse slot zeta_0, even though attained F_1 = F_0. The note correctly preserves that distinction.

## 2. Singular projection, means, and the independent root

For X = L_0 g with g standard Gaussian, the chain rule and scalar Gaussian integration by parts give

\[
E[U(X)X^T]
=E[U(X)g^T]L_0^T
=E[\partial_XU]L_0L_0^T.
\]

An independent auxiliary Gaussian group can be integrated out after conditioning. Setting J = E[partial_X U] gives

\[
E[(U-JX)X^T]=0.
\]

Each component of JX belongs to the linear span of the coordinates of X, so JX is precisely the orthogonal projection onto that span. Degeneracy does not affect this reasoning. A formal derivative in a null direction may be nonzero, but its contribution to JX and to JVJ^T is zero.

Applying this separately to the independent G and zeta groups gives

\[
E[FG^T]=RC,\qquad E[F\zeta^T]=S\Sigma.
\]

The constant, RG, S zeta, and U_F terms in (7) are pairwise orthogonal in the relevant vector-valued second-moment expansion. For example, independence gives E[G zeta^T] = 0; (6) gives the orthogonality of U_F to both groups; and its definition gives E U_F = 0. Thus (8) follows with no missing cross terms. The same calculation with the single xi group gives (9).

The Grams in (2) are raw second moments. Consequently the defects are exactly

\[
R_F=m_Fm_F^T+RCR^T+E[U_FU_F^T],
\qquad
R_\delta=m_\delta m_\delta^T+E[U_\delta U_\delta^T].
\]

All summands are positive semidefinite, yielding (10). Replacing the raw moments with centered covariances would remove genuine terms and change the law.

For completeness, the elementary Gaussian trigonometric identity used in the early-time calculations is

\[
E\cos L=e^{-\operatorname{Var}(L)/2},\qquad E\sin L=0
\]

for any centered Gaussian scalar L, including variance zero. It follows from scalar Gaussian integration by parts applied to its characteristic function, and requires no nondegeneracy.

On the first update,

\[
\delta_{11}=\lambda(h(X_1)-h(X_2))p(X_1).
\]

The product identities

\[
h(x)p(x)=\varepsilon^2\cos(2x),
\qquad
h(x_2)p(x_1)=\varepsilon^2
\{\sin(x_2-x_1)+\cos(x_1+x_2)\}
\]

therefore give exactly (11):

\[
E\delta_{11}=\lambda\varepsilon^2
\left(e^{-2\sigma^2}-e^{-(\sigma^2+K_{12})}\right),
\qquad E\delta_{12}=-E\delta_{11}.
\]

For the default activation and rho < 1, strict monotonicity and
Var(G_1 - G_2) = 2(1 - rho) > 0 give

\[
\chi=\tfrac12E(F_{01}-F_{02})^2>0.
\]

Since sigma^2 + K_12 = 2 sigma^2 - chi, the first mean in (11) is strictly negative. The rank-one mean contribution is indeed nonzero.

The independent bottom root is accounted for by RCR^T even when C is singular. The deterministic zero readout root has no Gaussian first-chaos contribution. Nothing in these identities grants a zero-cost nonzero variation of that deterministic root.

## 3. Supported maps, composite defects, and the finite resolvent

Suppose TVT^T is bounded above by W. If z belongs to ker W, then

\[
\|V^{1/2}T^Tz\|_2^2=z^TTVT^Tz\le z^TWz=0.
\]

Thus Ran(TV^{1/2}) is contained in Ran W, proving the asserted support inclusion. Moreover,

\[
(W^{\dagger/2}TV^{1/2})
(W^{\dagger/2}TV^{1/2})^T
\preceq P_{\mathcal H_W}.
\]

For u in H_V, write u = V^{1/2}z with
z = V^{dagger/2}u. Then ||z||_2 = ||u||_V and

\[
\|Tu\|_W
=\|W^{\dagger/2}TV^{1/2}z\|_2
\le\|u\|_V.
\]

This proves both the domains and the norm bounds in (13). It does not assign a meaningful covariance norm to an arbitrary output outside H_W.

The composite identity (14) is an exact expansion:

\[
\Sigma-DS\Sigma S^TD^T
=(\Sigma-D\Gamma D^T)+D(\Gamma-S\Sigma S^T)D^T.
\]

The stated analogous identity for SD is also correct. The defects retain the mean and root terms verified above.

Both DS and SD are strictly lower in the N + 1 time blocks because S is strict and D is lower, including its diagonal blocks. Their (N + 1)st powers vanish. The finite inverse polynomial in (15) is therefore exact. On the invariant support, each summand has operator norm at most one, giving N + 1.

This does not give that same operator-norm bound for BA. Causality also makes BA nilpotent in the full finite space, but a useful norm bound on its inverse would require control of its powers in a suitable space. The note does not conflate these two statements.

## 4. Quantitative strictness: constants and zero-Gram cases

The lemma in (16)–(17) is valid for an uncentered bounded vector and a projection onto a centered Gaussian span.

For c in H_V with c^T V c = 1, the smallest positive eigenvalue bounds

\[
\|c\|_2\le(\lambda_{\min}^+(V))^{-1/2},
\qquad |c^TH|\le B_V.
\]

Its projected scalar L_c is centered Gaussian with variance v at most one. Projection orthogonality gives

\[
1-v=E(c^TH-L_c)^2
\ge E(|L_c|-B_V)_+^2.
\]

If v is at least 1/2, monotonicity in the standard deviation gives the lower bound

\[
E(|g|/\sqrt2-B_V)_+^2
=2\int_{\sqrt2B_V}^{\infty}
(z/\sqrt2-B_V)^2\varphi(z)\,dz
=\eta(B_V).
\]

This verifies the potentially delicate factor of two: Gaussian symmetry contributes 2 and squaring the 1/sqrt(2) factor cancels it. If v < 1/2, the defect exceeds 1/2, which is at least eta(B_V). The integral is strictly positive for finite B_V, and integration by parts gives

\[
\eta(B_V)=(1+a^2)\overline\Phi(a)-a\varphi(a),
\qquad a=\sqrt2B_V.
\]

For c in ker V, c^T H vanishes almost surely and so does its projection. Splitting arbitrary coefficient vectors into support and kernel therefore extends the inequality to the whole matrix. There is no gap at a singular V.

The sums of squared coordinate bounds used in (18) are

\[
\sum_i L_i^2=2(N+1)L^2\quad\hbox{for }F,
\qquad
\sum_{k,a}(2b^2t_k)^2=8b^4\sum_{k=0}^N t_k^2
\quad\hbox{for }\delta.
\]

Their square roots reproduce both displayed B constants. Applying the lemma to S zeta and D xi gives (19). The corresponding supported operator norms are bounded by the square roots of the two defect factors, so their product is exactly the r in (20). The resolvent bound is the sum of the first N + 1 powers of r.

When a Gram vanishes its positive eigenvalue is not defined, and the note correctly avoids that expression. The supported source space is then zero, or the relevant map into the zero target vanishes by (10). The compositions are zero on the corresponding supports.

The strictness is a finite-support conclusion. The displayed constants depend both on the smallest positive attained eigenvalues and on a bound for normalized combinations of all history coordinates. They do not furnish a positive gap uniform in N at fixed T. Conversely, this limitation does not prove that such a uniform gap is impossible. The note makes the correct distinction.

## 5. Complete learned kernels and every time-weight factor

For u in H_Sigma and v in H_Gamma, covariance Cauchy–Schwarz gives

\[
|u_j|\le d_j\|u\|_\Sigma,\qquad
|v_j|\le f_j\|v\|_\Gamma.
\]

Applying the same coordinate inequality after the supported contractions gives

\[
|(Su)_i|\le f_i\|u\|_\Sigma,\qquad
|(Dv)_i|\le d_i\|v\|_\Gamma.
\]

The learned parts are bounded using the raw-Gram inequalities
|Gamma_ij| <= f_i f_j and |Sigma_ij| <= d_i d_j:

\[
|(M_Au)_i|\le f_i\,\lambda\sum_{j<i}f_jd_j\,\|u\|_\Sigma,
\qquad
|(M_Bv)_i|\le d_i\,\lambda\sum_{j<i}f_jd_j\,\|v\|_\Gamma.
\]

The label factors have absolute value one. Their removal in these absolute-value bounds costs no additional factor. The memory sums are strict in time exactly as (4) requires; the complete current block of B is still retained in D. Adding the two parts verifies (22).

The two samples and the historical arithmetic sum give

\[
s_k
\le \lambda\sum_{r=0}^{k-1}2L(2b^2\lambda r)
=4Lb^2\lambda^2\frac{k(k-1)}2
=2Lb^2\lambda^2k(k-1)
\le2Lb^2t_k^2.
\]

In particular s_0 = s_1 = 0. There is no missing factor of 2 or lambda in (21).

For the output norm used in (23)–(24),

\[
\lambda\sum_{k=0}^{N}\sum_{a=1}^2 1
=2\lambda(N+1)=2(T+\lambda).
\]

Using f_i <= L, d_i <= 2b^2 T, and s_k <= 2Lb^2T^2 then gives precisely

\[
\|Au\|_{\lambda,2}
\le L(1+2Lb^2T^2)\sqrt{2(T+\lambda)}\,\|u\|_\Sigma,
\]

\[
\|Bv\|_{\lambda,2}
\le2b^2T(1+2Lb^2T^2)\sqrt{2(T+\lambda)}\,\|v\|_\Gamma.
\]

For a fixed positive T and lambda = T/N, N >= 1, lambda <= T. For example the two coefficients are respectively bounded by

\[
2L(1+2Lb^2T^2)\sqrt T,\qquad
4b^2T(1+2Lb^2T^2)\sqrt T.
\]

This confirms fixed-horizon uniformity in the stated operator norms. The source norms are the unweighted raw-Gram support norms from (12); the output norm carries the displayed time weight. No extra source weight or continuum identification is implicit. An unweighted Euclidean norm on the entire output history would instead acquire a factor growing like sqrt(N + 1). Coordinate bounds are already uniform without that issue.

These estimates require supported inputs but allow every output coordinate, including components outside the destination covariance support. That is why they are compatible with §7.

## 6. Actual fields and expected, not mean-square, sensitivities

A row bound in (22) is equivalent to

\[
\|(A\Sigma^{1/2})_{i,\cdot}\|_2\le f_i(1+s_k),
\qquad
\|(B\Gamma^{1/2})_{i,\cdot}\|_2\le d_i(1+s_k).
\]

Since the attained fields have the exact raw second moments (2),

\[
E_2|(A\delta)_i|^2=(A\Sigma A^T)_{ii},
\qquad
E_1|(BF)_i|^2=(B\Gamma B^T)_{ii}.
\]

Thus the L2 bounds stated before (25) follow directly, with no square root of a support dimension or rank. Applying a pointwise supported-vector bound to a random vector and then bounding its random covariance norm would be a weaker route; the note correctly uses the exact row covariance instead.

The Gaussian source norms are ||xi_i||_2 = f_i and ||zeta_i||_2 = d_i. Minkowski's inequality yields

\[
\|Z_i\|_2\le f_i+f_i(1+s_k)=f_i(2+s_k),
\]

\[
\|q_i\|_2\le d_i+d_i(1+s_k)=d_i(2+s_k).
\]

The same-population terms need not be independent. The factors in (25)–(26), including the 2 and 2b^2t_k, are correct.

For a deterministic supported xi direction v, frozen-coefficient differentiation gives the pathwise identity

\[
P=v+A T_\delta.
\]

By the definition of D and the finite derivative integrability already checked,

\[
E_2T_\delta=Dv,\qquad E_2P=v+ADv.
\]

The crucial domain condition holds: Dv belongs to H_Sigma. Therefore

\[
|(E_2P)_i|
\le f_i\|v\|_\Gamma+
f_i(1+s_k)\|Dv\|_\Sigma
\le f_i(2+s_k)\|v\|_\Gamma.
\]

The supported norm bound on E_2 T_delta is exactly (13). This proves (27)–(28) while retaining A in full.

For a supported zeta direction u with the bottom root fixed,

\[
E_1\partial_uF=Su,\qquad
E_1\partial_uq=u+BSu.
\]

Here Su belongs to H_Gamma, so the complete B row bound applies and gives (29).

For simultaneous supported bottom-root and reverse-source variations, set

\[
V_0=\operatorname{diag}(C,\Sigma),\qquad T_0=[R\ S].
\]

Equation (8) implies T_0 V_0 T_0^T <= Gamma. The supported-map argument above therefore yields

\[
\|Rg+Su\|_\Gamma
\le(\|g\|_C^2+\|u\|_\Sigma^2)^{1/2}=J.
\]

Because the mean q variation equals u + B(Rg + Su), its coordinate norm is at most

\[
d_i\|u\|_\Sigma+d_i(1+s_k)J
\le d_i(2+s_k)J.
\]

This verifies both parts of (30), including the singular C case. Only the bottom Gaussian root and reverse-source directions receive these supported norms; the deterministic readout root is excluded as stated.

All of these identities concern expectations of formal derivatives at fixed selected coefficients and covariances. They do not differentiate the statistical selection map. Nor does a bound on |E X| give a bound on E|X|^2: the variance is absent. Consequently the note has not controlled second moments of the pathwise sensitivities or products of those sensitivities with correlated fields. Its explicit refusal to infer those stronger bounds is correct.

## 7. Attained support leakage: complete verification of (31)–(34)

Take exactly N = 2, rho = -1, the default ell, and any lambda > 0. Since both column sums of C vanish and G_1 + G_2 = 0, summing the bottom equation across samples gives

\[
Z^1_{k1}+Z^1_{k2}=0
\]

at every time. The source's reference to row sums is harmless because this C is symmetric. The identity holds with the selected coefficients fixed for arbitrary reverse-source slot variations. The default shifted odd activation then gives F_k1 + F_k2 = 2, hence (31).

For any two times, the coefficient vector testing the difference of their e_+ components annihilates F almost surely. It belongs to ker Gamma because Gamma is the raw second-moment matrix. Thus every vector in H_Gamma has a constant e_+ component across time, proving (32). Differentiating the same exact identity at fixed G also proves e_+^T S_kr = 0, including derivatives in zero-variance reverse slots.

Write G = (g,-g), U = arctan(g)/10, and nu = E U^2 > 0. The initial K has entries

\[
K_{11}=K_{22}=1+\nu,\qquad K_{12}=K_{21}=1-\nu.
\]

For X ~ N(0,K), x = (X_1 + X_2)/2 and d = (X_1 - X_2)/2 have variances 1 and nu and zero covariance; their joint Gaussian law therefore makes them independent.

The required trigonometric differences are

\[
h(x+d)-h(x-d)
=2\varepsilon(\cos x-\sin x)\sin d,
\]

\[
p(x+d)-p(x-d)
=-2\varepsilon(\sin x+\cos x)\sin d.
\]

Multiplying and dividing by sqrt(2) gives exactly

\[
e_-^T\delta_1
=-2\sqrt2\,\lambda\varepsilon^2\sin^2d\cos(2x).
\]

This verifies the sign and coefficient in (33). Its raw second moment is

\[
a_-=8\lambda^2\varepsilon^4 E[\sin^4d]E[\cos^2(2x)]>0.
\]

Both factors are positive because the respective nondegenerate Gaussian variables avoid the discrete zero sets almost surely. An explicit check is

\[
a_-=\frac{\lambda^2\varepsilon^4}{2}
(3-4e^{-2\nu}+e^{-8\nu})(1+e^{-8}).
\]

Let P_swap exchange the two samples. The first-update function obeys

\[
\delta_1(P_{\rm swap}X)=-P_{\rm swap}\delta_1(X).
\]

Since X is exchangeable, Sigma_11 commutes with P_swap. The one-dimensional antisymmetric eigenspace is therefore invariant, with eigenvalue a_-. This verifies Sigma_11 e_- = a_- e_- even though the mean of delta_1 is nonzero.

The note then uses the full attained N = 2 Gram to set c_1 = e_-/a_-, c_0 = c_2 = 0, and u = Sigma c. This gives

\[
u\in\mathcal H_\Sigma,\qquad u_0=0,\qquad u_1=e_-,
\qquad u_2=\Sigma_{21}e_-/a_-.
\]

The input is genuinely supported; its squared covariance norm is finite and equals

\[
\|u\|_\Sigma^2=c^T\Sigma c=1/a_-.
\]

The last input block is neither prescribed independently nor assumed zero.

Strict causality now gives (Au)_0 = (Au)_1 = 0. In the last row, the response term has zero e_+ component, while the learned term gives

\[
e_+^T(Au)_2
=\lambda e_+^T\Gamma_{21}Ye_-
=\lambda E[(e_+^TF_2)(F_1^Te_+)]
=2\lambda.
\]

Here Ye_- = e_+ and both feature factors equal sqrt(2). The u_2 value cannot enter this row because A is strictly lower in time. This verifies every factor in (34).

The resulting temporal e_+ profile, (0,0,2 lambda), violates the necessary support condition (32). Consequently Au is outside H_Gamma. The argument uses the actual full covariance and retains both learned memories throughout the law; no freely assigned unsupported temporal forcing is used.

This refutes universal support preservation by A. It invalidates transferring the S/D supported-contraction argument to A/B without additional work. It does not, by itself, prove that BA fails to preserve a support, that a BA resolvent must be large, or that every enlarged norm/storage construction must fail. The note's conclusions respect these limits. Projecting the output onto H_Gamma necessarily discards a nonzero temporal-average contrast; it need not erase the entire last-time average.

## 8. Fully specified supported sign test and time weights

The functional under audit is exactly

\[
\mathcal Q_B(v)=\sum_{k=0}^N v_k^TY(Bv)_k.
\]

It is an unweighted, label-paired quadratic form. Although B can be nonsymmetric, this scalar quadratic form is well-defined. It is not the ordinary unlabelled pairing.

On the first prefix N = 1, the bootstrap above supplies the duplicate-source covariance. With the default ell and any allowed rho,

\[
\chi=K_{11}-K_{12}>0,\quad c=e^{-\chi},\quad
K e_-=\chi e_-.
\]

For the gates, direct expansion gives

\[
p(X_a)p(X_b)
=\varepsilon^2\{\cos(X_a-X_b)-\sin(X_a+X_b)\}.
\]

The centered Gaussian expectations therefore yield

\[
J_p=\varepsilon^2
\begin{pmatrix}1&c\\c&1\end{pmatrix}.
\]

It is essential here to differentiate the formal xi_0 and xi_1 slots before restricting to their attained equality. With the deterministic readout root fixed, delta_0 is identically zero and

\[
\delta_{1a}
=\lambda\bigl(h(\xi_{01})-h(\xi_{02})\bigr)p(\xi_{1a})
\]

as a formal function of these slots. Hence

\[
D_{10}=\lambda J_pY.
\]

The current derivative block is diagonal. Since p' = -h and

\[
E[h(X_a)h(X_b)]
=\varepsilon^2
\begin{cases}
1,&a=b,\\
c,&a\ne b,
\end{cases}
\]

its entries are -lambda epsilon^2(1 - c) and
+lambda epsilon^2(1 - c). Thus

\[
D_{11}=-\lambda\kappa Y,\qquad
\kappa=\varepsilon^2(1-c).
\]

The learned reverse term vanishes throughout this prefix because its only possible historical factor is Sigma_10 = 0. Also B_00 = 0. Therefore the complete blocks quoted in §8 are exactly

\[
B_{10}=\lambda J_pY,\qquad B_{11}=-\lambda\kappa Y.
\]

The constant-in-time direction v = (e_-,e_-) is supported because

\[
\Gamma
\begin{pmatrix}e_-/(2\chi)\\e_-/(2\chi)\end{pmatrix}
=\begin{pmatrix}e_-\\e_-\end{pmatrix}.
\]

It is an eigenvector of Gamma with eigenvalue 2 chi and ordinary squared length 2, giving ||v||_Gamma^2 = 1/chi.

Since Ye_- = e_+ and J_p e_+ = epsilon^2(1 + c)e_+,

\[
(Bv)_0=0,\qquad
(Bv)_1=2\lambda\varepsilon^2c\,e_+.
\]

Consequently

\[
\mathcal Q_B(v)=2\lambda\varepsilon^2e^{-\chi}>0,
\]

exactly as in (35). There is no small-lambda approximation. The time-weighted variant equals

\[
\lambda\mathcal Q_B(v)
=2\lambda^2\varepsilon^2e^{-\chi}>0.
\]

For comparison, the ordinary unlabelled pairing is zero on this same direction because e_- is orthogonal to e_+. Thus the label specification changes the tested assertion in a substantive way.

If a unit covariance-norm direction is desired, sqrt(chi) v has that norm and its unweighted functional is 2 lambda epsilon^2 chi exp(-chi), still strictly positive. The example asserts positivity, not a positive lower bound uniform as rho approaches 1.

The range of the duplicate-source Gram consists of pairs of equal blocks in Ran K. If the initial xi_0 direction is fixed to zero, the entire supported direction on this prefix must be zero. The note correctly states that its test is then unavailable and fixes all other roots.

Finally, supported reverse directions have u_0 = 0. Strict causality makes S_0 zero and allows S_1 to depend only on that zero reverse block. Thus S vanishes on H_Sigma on this prefix, and DS is zero there. The positive label-paired value is fully compatible with that contraction statement.

## 9. Required corrections versus optional improvements

### Required

**None.** No false displayed identity, missing hypothesis necessary for the claimed finite result, unsupported input construction, omitted learned block, wrong time factor, or unjustified strengthening of a response estimate was found.

No source edits were made.

### Optional

1. **Display the early-time bootstrap once.** A short chain showing delta_0 = 0, B_0 = 0, q_0 = 0, F_1 = F_0, and xi_1 = xi_0 would make §§2, 7, and 8 easier to check directly from (1)–(4). The chain is derivable as written; this is an exposition improvement.
2. **Spell out the signed exchange transformation in §7.** Writing delta_1(P_swap X) = -P_swap delta_1(X) immediately explains why the raw second-moment block commutes with sample exchange despite the nonzero mean.
3. **Keep “label-paired” in the summary-table sign claim.** §8 fully specifies the functional, but the shorter §9 row “Supported-source nonpositivity alone” would be harder to misread if it repeated that qualifier.
4. **Optionally display the weighted sign value and a lambda-free horizon constant.** The values 2 lambda^2 epsilon^2 exp(-chi) and the two fixed-T bounds derived above make conventions especially easy to compare. They are already consequences of the note's explicit definitions, not missing factors.

## 10. Exact boundary of the pass

The audited results establish finite, attained, mean/root-resolved Gaussian projection identities; strict contraction of the derivative-only supported maps with attained-Gram-dependent constants; complete A/B row bounds into ordinary coordinates and a time-weighted history norm; actual-field second moments; and expected formal source responses. They also establish two separate obstructions to proposed stronger inferences: learned A can leave the destination covariance support, and the specified label-paired Q_B can be positive on a supported direction constant in time.

They do not establish a uniform strict gap in the covariance norms, uniform mean-square pathwise sensitivities, control of the missing correlated sensitivity products, a closed learned-feedback storage estimate, or a global continuation or limiting-training theorem. The two counterexamples do not prove those stronger objectives impossible. The note preserves these distinctions throughout, and its bounded verdict is mathematically supported.
