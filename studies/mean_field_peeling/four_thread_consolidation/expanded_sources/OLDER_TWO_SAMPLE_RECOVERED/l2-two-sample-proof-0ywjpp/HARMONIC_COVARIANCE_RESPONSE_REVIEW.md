# Isolated adversarial audit of the covariance-supported response claim

Date: 2026-09-06.

## Verdict and isolation

The mathematical core passes for the explicitly stated finite causal law (1)–(4). The mean/root-resolved projection identities, singular-support contractions, finite-support quantitative strictness, full learned-kernel row bounds, field moment bounds, and expected-source-response bounds are valid. The two-update support-leakage example is attained by that law, with both learned memories retained.

One correction is required for a fully self-contained statement: Section 8 does not define its quadratic functional \(\mathcal Q_B\) in terms of \(B\) and a source history, including any time weights. Its displayed scalar is correct and positive. It refutes nonpositivity for the explicitly defined, unweighted, label-paired quadratic form specified below. Without a definition in the candidate, the asserted refutation of a source-class sign property is underspecified. This is a local definition/scope gap, not an error in the block calculation.

No mesh-uniform strict covariance gap, full learned-feedback contraction, uniform squared-sensitivity estimate, storage closure, global continuation result, or limiting identification is established by this audit.

Isolation record:

- Sole mathematical source: `/tmp/l2-two-sample-proof-0ywjpp/HARMONIC_COVARIANCE_RESPONSE_TEST.md`, read completely, lines 1–635.
- Its named dependency was not opened. No project files, prior reviews, history, external mathematical sources, experiments, or agents were used.
- Procedural guidance only: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, read completely. It guided hypothesis checks, explicit derivations, and separation of proved claims from missing definitions; it supplied no additional mathematical setup.
- Source SHA256 before reading: `a80acb79d32a42828eb7618e365ad3dfeebc0a9ee89ad2729effaec352840ced`.
- Source SHA256 after review: `a80acb79d32a42828eb7618e365ad3dfeebc0a9ee89ad2729effaec352840ced`.
- Integrity result: before and after hashes match exactly.
- The candidate was not edited. This review is the sole audit deliverable.

All equation numbers below refer to the candidate. Assertions concerning an upstream model or the contents of the unopened dependency are outside this verdict. The finite law itself is sufficient for the positive mathematical conclusions checked here, subject to the definition correction in Section 8.

## 1. Consistency and attainment of the finite causal law

**Finding: internally consistent; the apparent statistical feedback does not create a same-time selection loop.**

For \(-1\le\rho<1\), \(C\) is positive semidefinite, including its singular endpoint \(\rho=-1\). Equations (2) deliberately assign raw feature/field second moments to the covariances of centered Gaussian sources. This is consistent: the assigned matrices are positive semidefinite, and there is no requirement that the source mean equal the mean of the field whose second moment is used.

The finite construction can be checked directly, without the dependency. Suppose the rows before time \(k\), their source marginals, and their selected coefficients have been constructed.

1. The bottom equation computes \(F_k\) using only \(G\), \(\zeta_{<k}\), and the already selected rows of \(B\). Thus the new row and diagonal block of \(\Gamma=E_1FF^T\), and \(S_{k,<k}\), can be computed before \(\zeta_k\) exists.
2. The new \(\Gamma\) block matrix is an actual raw Gram. It therefore defines a Gaussian extension of \(\xi_{<k}\) to \(\xi_{\le k}\), even when singular. The new row \(A_{k,<k}\) is now determined by (3)–(4).
3. With that row frozen, the top causal recursion computes \(Z_k,w_k,\delta_k\) and \(D_{k,\le k}\). Its raw Gram supplies the new blocks of \(\Sigma\).
4. Those blocks define a Gaussian extension of \(\zeta_{<k}\) to \(\zeta_{\le k}\). The new row of \(B\) and then \(q_k\) can be computed.

The Gaussian extensions exist because each enlarged Gram is positive semidefinite and agrees with the previously constructed principal block. All covariance choices here are deterministic expectations; the independent Gaussian groups can consequently be realized with the independence required in the candidate. No inverse Gram is needed in this construction. This verifies attainment for the finite prefixes used in the examples; it is not a continuum or global continuation theorem.

The initialization also closes directly:

\[
w_0=\delta_0=0,\quad D_{0,*}=B_{0,*}=0,
\quad\Sigma_{0,*}=0,\quad\zeta_0=q_0=0.
\]

Here \(D_{0,*}=0\) concerns the source derivatives actually defined in (3), with the readout fixed. Consequently,

\[
Z^1_0=Z^1_1=G,\qquad F_0=F_1=\ell(G).
\]

The bottom function at time \(k\) depends on reverse-source times strictly before \(k\), so \(S\) and \(A\) are strictly lower in time. The top field at time \(k\) depends only on \(\xi_{\le k}\), so \(D\) and \(B\) are lower in time. Including the current block of \(D\) is essential and is respected later in Section 8.

For the stated activations, the bounds on \(h,p,\ell\) and the identity \(p'=-h\) are correct. Cancellation of the constant part of \(H\) gives

\[
w_k=\lambda\sum_{r<k}\{h(Z_{r1})-h(Z_{r2})\},
\]

which proves both bounds in (5), including their factors of two.

The differentiation assumptions in lines 106–111 are justified within this law. In the bottom population,

\[
|q_i|\le |\zeta_i|+L\sum_j|B_{ij}|.
\]

Differentiating its finite recursion introduces products of previous derivatives, such \(q_i\), and bounded derivatives of \(\ell\). Induction gives polynomial bounds in the finitely many Gaussian coordinates. In the top population, differentiation of \(Z,w,\delta\) uses finite fixed rows of \(A\), bounded activation derivatives, and the deterministic finite-prefix bound on \(w\); induction gives finite deterministic bounds for the first source derivatives. These arguments also ensure that the next selected coefficients are finite in the construction above. The default \(\ell\), as well as the explicitly named alternatives \(\sin\) and \(\arctan\), has the bounded derivatives needed here. No fact about an alternative model in the dependency is required.

## 2. Gaussian integration by parts, means, and the bottom root

**Finding: (6)–(11) are correct, with singular Grams and raw second moments treated properly.**

Write a centered Gaussian vector as \(X=L_0g\), with \(g\) standard Gaussian and \(V=L_0L_0^T\). One-dimensional integration by parts, applied componentwise, gives

\[
E[U(X)X^T]
=E[U(L_0g)g^T]L_0^T
=E[\partial_XU]L_0L_0^T
=E[\partial_XU]V.
\]

The preceding finite-prefix derivative bounds justify the boundary terms and integrability. An independent auxiliary Gaussian group can be conditioned on and then integrated out. This proof permits rectangular \(L_0\), so singularity of \(V\) causes no difficulty.

If \(T=E\partial_XU\), the residual \(U-TX\) is orthogonal to every coordinate of \(X\). The random vector \(TX\) lies in their centered linear span and is therefore the orthogonal projection, coordinate by coordinate. An uncentered \(U\) is allowed. Its constant component is orthogonal to that span.

Applying this to the independent bottom Gaussian groups \(G,\zeta\), and separately to the top source \(\xi\), proves exactly (7)–(9). In particular,

\[
R_F=m_Fm_F^T+RCR^T+E_1U_FU_F^T,
\qquad
R_\delta=m_\delta m_\delta^T+E_2U_\delta U_\delta^T.
\]

All terms are positive semidefinite. The residuals have zero mean and are orthogonal to their displayed Gaussian coordinates. Independence is used for the orthogonality of the two bottom Gaussian spans; it does not assert independence of an evolved field from its sources.

The bottom-root term is substantive. Already at time zero for the default activation,

\[
R_0=\alpha I_2,\qquad
\alpha=E\ell'(G_1)>0,
\]

so its contribution is \(\alpha^2C\), including when \(C\) has rank one. It cannot be omitted from the exact defect identity. The readout is deterministic and fixed in (1), and contributes no Gaussian first-chaos component to (9). None of these identities controls a nonzero variation of that readout by assigning it zero covariance cost.

The first-update mean formula can also be derived entirely locally. Let \(K=E[\ell(G)\ell(G)^T]\). Since \(F_0=F_1\), the centered Gaussian source has \(\xi_0=\xi_1=X\) almost surely, with covariance \(K\). Moreover \(Z_0=X\) and \(Z_1=X\), since \(\delta_0\) is identically zero. Thus

\[
\delta_{11}=\lambda\{h(X_1)-h(X_2)\}p(X_1).
\]

Exchangeability gives equal marginal variance \(\sigma^2=K_{11}\). The identities

\[
h(x)p(x)=\varepsilon^2\cos(2x),
\qquad
h(y)p(x)=\varepsilon^2\{\sin(y-x)+\cos(x+y)\}
\]

give the expectations in (11), using \(E\cos(a^TX)=\exp(-a^TKa/2)\) and the vanishing of centered Gaussian sine expectations. The latter cosine identity follows directly from the one-dimensional Gaussian integral for the scalar Gaussian \(a^TX\), including zero variance. This yields

\[
E\delta_{11}=\lambda\varepsilon^2
\{e^{-2\sigma^2}-e^{-(\sigma^2+K_{12})}\},
\qquad E\delta_{12}=-E\delta_{11}.
\]

For the default strictly increasing \(\ell\), \(\rho<1\) implies

\[
\chi=\tfrac12E\{\ell(G_1)-\ell(G_2)\}^2>0.
\]

Hence the first displayed mean is strictly negative and nonzero. Replacing the raw \(\Sigma\) by the centered covariance of \(\delta\) would remove a real mean-square contribution and change the specified law.

## 3. Support maps, composite defects, and nilpotence

**Finding: (10), (12)–(15), and the qualifications concerning formal slots are correct.**

The use of \(V^\dagger\) is confined to \(\mathcal H_V=\operatorname{Ran}V\), where it defines a norm. If \(TVT^T\preceq W\) and \(z\in\ker W\), then

\[
0\le\|V^{1/2}T^Tz\|^2\le z^TWz=0.
\]

Thus \(T\mathcal H_V\subseteq\mathcal H_W\). Also

\[
(W^{\dagger/2}TV^{1/2})(W^{\dagger/2}TV^{1/2})^T
\preceq P_{\mathcal H_W}.
\]

Applying this operator to the minimum-norm representation \(V^{\dagger/2}v\) of a supported vector proves the claimed covariance-norm contraction. This establishes both maps in (13), without controlling arbitrary ambient-coordinate columns of \(S\) or \(D\).

Substitution of the definitions of the defects gives

\[
R_\delta+DR_FD^T
=\Sigma-D\Gamma D^T+D(\Gamma-S\Sigma S^T)D^T
=\Sigma-DS\Sigma S^TD^T,
\]

which verifies (14) and retains the means, bottom-root contribution, and both residual contributions. The identity with \(S,D\) interchanged is equally valid.

Both \(DS\) and \(SD\) are strictly lower in time: one factor is strictly lower and the other is lower, even with the latter's current block retained. There are \(N+1\) time blocks. The asserted powers therefore vanish on the full ambient space, hence also on the invariant covariance supports. The geometric inverse and the bound \(N+1\) in (15) follow. They concern \(DS\), not \(BA\), and are not mesh-uniform at fixed positive \(T=\lambda N\).

A useful degeneracy check is the first prefix. Although \(F_1=F_0\) on the attained law, its ambient formal derivative need not vanish:

\[
(S_{1,0})_{ab}
=\lambda C_{ab}y_bE[\ell'(G_a)\ell'(G_b)].
\]

The zero-variance slot \(\zeta_0\) remains present in this derivative. Supported reverse directions nevertheless have \(u_0=0\), so this column contributes nothing to the supported map. This agrees with the candidate's distinction between formal slots and supported directions.

## 4. Quantitative strict defect

**Finding: the bounded-output lemma and (16)–(20) are valid with the stated constants.**

For nonzero \(V=EHH^T\), a vector \(c\in\mathcal H_V\) normalized by \(c^TVc=1\) satisfies

\[
\|c\|_2\le(\lambda_{\min}^+(V))^{-1/2},
\qquad |c^TH|\le B_V.
\]

Its projection \(L_c=c^TPH\) is a centered Gaussian with variance \(v\le1\). Projection orthogonality and the pointwise bound on \(c^TH\) give

\[
1-v=E(c^TH-L_c)^2
\ge E(|L_c|-B_V)_+^2.
\]

For \(v\ge1/2\), comparison with \(|g|/\sqrt2\) yields

\[
E(|g|/\sqrt2-B_V)_+^2
=\int_{\sqrt2B_V}^{\infty}(z-\sqrt2B_V)^2\varphi(z)\,dz.
\]

The two Gaussian tails and the factor \(1/2\) from scaling cancel; there is no missing factor of two in (16). For \(v<1/2\), the defect exceeds \(1/2\), which is at least this tail integral. The integral is strictly positive for every finite \(B_V\) and at most \(1/2\). Integration of its three polynomial terms gives exactly

\[
(1+a^2)\overline\Phi(a)-a\varphi(a),\qquad a=\sqrt2B_V.
\]

If \(c\in\ker V\), then \(c^TH=0\) almost surely and its projection vanishes. Decomposition into support and kernel consequently extends the normalized estimate to the matrix inequality (17).

For \(F\), the squared coordinate-bound sum is \(2(N+1)L^2\). For \(\delta\), it is \(8b^4\sum_{k=0}^Nt_k^2\). These are precisely the numerators in (18) after taking square roots. The relevant projections are \(S\zeta\) and \(D\xi\); thus (19) follows. The operator norms of the two supported maps are bounded by the square roots of the two factors in (19), proving \(r\) and the finite geometric-sum resolvent estimate in (20).

The zero-Gram cases are correctly separated. A map from a zero support is trivial; a covariance inequality with zero destination Gram forces the supported image to be zero. No positive-eigenvalue formula is then needed.

This is strictness on each fixed attained finite support. Its constants involve both the smallest positive eigenvalues and the number/time distribution of history coordinates. Neither a positive lower bound uniform in the mesh nor closeness to first chaos along a sequence of histories is resolved. The candidate correctly does not infer either outcome from bounded individual gates.

## 5. Exact learned-kernel bounds

**Finding: (21)–(24) control the complete rows of \(A,B\) on supported inputs, with no omitted memory.**

For \(u\in\mathcal H_\Sigma\), write \(u=\Sigma^{1/2}\alpha\) with \(\|\alpha\|=\|u\|_\Sigma\). Coordinate Cauchy–Schwarz gives \(|u_j|\le d_j\|u\|_\Sigma\). The analogous inequality for \(v\) is \(|v_j|\le f_j\|v\|_\Gamma\). The projection inequalities give

\[
|(Su)_i|\le f_i\|u\|_\Sigma,
\qquad |(Dv)_i|\le d_i\|v\|_\Gamma.
\]

Raw Gram Cauchy–Schwarz, \(|\Gamma_{ij}|\le f_if_j\) and \(|\Sigma_{ij}|\le d_id_j\), then proves the two memory estimates in Section 5. Adding the response term proves (22). The fact that \(M_B\) is strictly lower does not remove the current block of \(D\); it remains in the projection term.

The exact upper-bound sum is

\[
s_k\le\lambda\sum_{r=0}^{k-1}2L(2b^2\lambda r)
=2Lb^2\lambda^2k(k-1)
\le2Lb^2t_k^2,
\]

as in (21). In particular the bound is zero at \(k=0,1\), consistently with \(d_0=0\).

Summing the squared coordinate estimates in the specified output norm uses

\[
\lambda\sum_{k=0}^N\sum_{a=1}^2 1=2(T+\lambda),
\]

and proves exactly (23)–(24). At fixed \(T>0\), \(\lambda=T/N\) with \(N\ge1\) implies \(\lambda\le T\), so these constants are uniformly bounded. The conclusions are coordinate bounds and bounds for the time-weighted full-history Euclidean norm. They do not imply a mesh-uniform bound in the unweighted full-history Euclidean norm, nor a map into the destination covariance support.

## 6. Field moments, expected responses, and root scope

**Finding: (25)–(30) follow with their stated expected-response scope.**

The exact supported row norm of a deterministic row \(a_i\) acting on \(\mathcal H_\Sigma\) is \((a_i\Sigma a_i^T)^{1/2}\). Therefore (22), together with \(E_2\delta\delta^T=\Sigma\), gives

\[
\|(A\delta)_i\|_2^2=A_i\Sigma A_i^T
\le f_i^2(1+s_k)^2.
\]

The same argument applies to \(BF\) using its raw Gram \(\Gamma\). Centering either field here would be an error; the candidate does not do so. Since \(\|\xi_i\|_2=f_i\) and \(\|\zeta_i\|_2=d_i\), Minkowski's inequality proves (25)–(26) without requiring independence of a source and its memory term.

For a deterministic supported top direction \(v\), differentiating the frozen-coefficient equation gives

\[
\partial_vZ=v+A\partial_v\delta.
\]

Taking expectations gives (27). Because \(Dv\in\mathcal H_\Sigma\), the supported contraction for \(D\), the complete row bound for \(A\), and \(|v_i|\le f_i\|v\|_\Gamma\) prove (28). For a supported reverse direction \(u\), the corresponding identities are

\[
E_1\partial_uF=Su,\qquad
E_1\partial_uq=u+BSu,
\]

which prove (29) in the same way. Coefficients and covariance selection parameters remain frozen throughout; no derivative of the statistical selection map is introduced.

For joint bottom-root and reverse-source variation, (8) implies

\[
[R\ S]\begin{pmatrix}C&0\\0&\Sigma\end{pmatrix}[R\ S]^T
\preceq\Gamma.
\]

The singular-support map argument from Section 3 applies to this block covariance. Thus \(\|Rg+Su\|_\Gamma\le J\), with the candidate's direct-sum norm. Also

\[
|u_i+B_i(Rg+Su)|
\le d_i\|u\|_\Sigma+d_i(1+s_k)J
\le d_i(2+s_k)J,
\]

proving (30), including \(\rho=-1\).

The estimates bound expected formal Jacobians. They do not bound their second moments uniformly on a feature horizon: controlling \(|EV|\) cannot bound \(E|V|^2\). The finite-prefix regularity argument does ensure finiteness of source-derivative moments at each fixed prefix; it does not supply the missing uniform quantitative estimate. Likewise, an \(L^2\) bound on \(q\) does not control its product with an uncontrolled correlated sensitivity.

The candidate's exclusion of a nonzero formal readout-root direction is correct. No such direction is part of the covariance-supported domain in (30). If a later calculation is to differentiate that root, its off-root extension must be specified, for example by explicitly including \(w_*\) in the readout equation. No such extension is needed for any estimate verified here.

The particular storage identity mentioned in lines 469–471 is in the unopened dependency and has not been verified. Only the local limitation is established here: these estimates provide no closure of additional correlated sensitivity products.

## 7. Attained two-update support leakage

**Finding: (31)–(34) give an exact attained counterexample to support preservation by \(A\).**

Set \(\rho=-1\) and \(N=2\). The columns of \(C\) sum to zero, as do its rows, and \(G_1+G_2=0\) almost surely. Summing the bottom update across samples therefore preserves \(Z^1_{k1}+Z^1_{k2}=0\), regardless of the attained values of \(q\) or its learned memory. The shifted odd activation gives \(F_{k1}+F_{k2}=2\).

Every temporal difference of two sample-average coordinate functionals annihilates \(F\) almost surely. It belongs to \(\ker\Gamma\), which proves the support restriction (32). The same conservation identity holds for arbitrary formal \(\zeta\) variations with \(G\) held at its attained zero-sum value. Hence \(e_+^TS_{k,r}=0\), including off-support reverse slots.

Writing \(G=(g,-g)\) gives \(F_0=(1+U,1-U)\), with \(EU=0\) and \(\nu=EU^2>0\). Thus the initial source covariance has diagonal \(1+\nu\) and off-diagonal \(1-\nu\). The Gaussian variables

\[
x=(X_1+X_2)/2,\qquad d=(X_1-X_2)/2
\]

are independent, with variances \(1\) and \(\nu\). Direct trigonometric subtraction gives

\[
h(x+d)-h(x-d)=2\varepsilon(\cos x-\sin x)\sin d,
\]

\[
p(x+d)-p(x-d)=-2\varepsilon(\sin x+\cos x)\sin d.
\]

Their product proves (33), including its sign and factor \(2\sqrt2\). Both Gaussian variances are positive, so \(\sin^2d\cos(2x)\) is not almost surely zero. Consequently \(a_-=E(e_-^T\delta_1)^2>0\).

Under sample exchange \(P\), the first-update formula satisfies \(\delta_1(PX)=-P\delta_1(X)\). Since \(X\) has an exchange-invariant law, its raw field Gram satisfies \(P\Sigma_{11}P=\Sigma_{11}\). Therefore \(\Sigma_{11}e_-=a_-e_-\). This verifies the exchange argument despite the nonzero antisymmetric mean of \(\delta_1\).

The constructed vector \(u=\Sigma c\), with \(c_1=e_-/a_-\) and its other blocks zero, is supported by definition. It has \(u_0=0\) and \(u_1=e_-\), and its last block is whatever the actual full covariance supplies. As an additional check, \(\|u\|_\Sigma^2=c^T\Sigma c=1/a_-<\infty\). No unsupported independent choice of \(u_2\) is made.

Strict causality now gives zero output at times zero and one. At time two,

\[
e_+^T(Au)_2
=\lambda e_+^T\Gamma_{21}Ye_-
=\lambda E[(e_+^TF_2)(F_1^Te_+)]
=2\lambda.
\]

The response term vanishes in this sample average; \(Ye_-=e_+\); and each sample average of \(F\) equals \(\sqrt2\). This verifies (34) without needing to calculate or alter \(u_2\), \(F_2\), or later learned reverse coefficients. The finite causal construction above supplies all those attained objects for every finite \(\lambda>0\).

For example, the history vector with blocks \((-e_+,0,e_+)\) belongs to \(\ker\Gamma\) and has pairing \(2\lambda\) with \(Au\). Thus \(Au\notin\mathcal H_\Gamma\). This is a failure of support preservation itself, stronger than a failure of a proposed contraction constant for that map. It does not establish that \(B\) alone fails support preservation, or that every possible estimate for \(BA\) fails.

There is a minor wording issue at lines 549–550: projection back to the support necessarily removes a nonzero temporal sample-average contrast. The calculation does not say that projection sets the entire time-two sample average to zero; it can redistribute averages between times. This does not affect the counterexample.

## 8. Supported constant-source sign test

**Finding: the complete blocks, supported direction, and positive scalar are correct. The quadratic functional itself needs an explicit definition.**

On \(k=0,1\), the initialization in Section 1 gives the repeated-block \(\Gamma\) in the candidate. Also \(M_B=0\) on this prefix: its only possible earlier-time blocks contain \(\delta_0=0\).

Before identifying the duplicate attained Gaussian slots, the formal equations have

\[
\delta_{1a}
=\lambda\{h(\xi_{01})-h(\xi_{02})\}p(\xi_{1a}).
\]

Therefore the two distinct formal derivative blocks, evaluated on \(\xi_0=\xi_1=X\), are

\[
D_{1,0}=\lambda E[p(X)p(X)^T]Y=\lambda J_pY,
\]

\[
(D_{1,1})_{aa}
=-\lambda E[\{h(X_1)-h(X_2)\}h(X_a)],
\]

with zero off-diagonal entries in the current block. Using the centered Gaussian sine/cosine identities gives

\[
J_p=\varepsilon^2\begin{pmatrix}1&c\\c&1\end{pmatrix},
\quad E[h(X_a)^2]=\varepsilon^2,
\quad E[h(X_1)h(X_2)]=\varepsilon^2c,
\]

where \(c=e^{-\chi}\). Thus \(B_{0,0}=0\), \(B_{1,0}=\lambda J_pY\), and \(B_{1,1}=-\lambda\kappa Y\) exactly as claimed. Differentiating only after collapsing the duplicate slots would lose this distinction; the candidate correctly retains it.

The proposed constant-in-time direction \(v=(e_-,e_-)\) is supported because \(Ke_-=\chi e_-\), with \(\chi>0\), and

\[
\Gamma\begin{pmatrix}e_-/(2\chi)\\e_-/(2\chi)\end{pmatrix}=v.
\]

Its squared covariance norm is \(1/\chi\), also as claimed. The complete kernel acts by

\[
(Bv)_0=0,\qquad
(Bv)_1=\lambda(J_p-\kappa I)e_+
=2\lambda\varepsilon^2c\,e_+.
\]

Now explicitly define, for this audit's locally specified sign claim,

\[
Q_B^{\rm unweighted}(v)
:=\sum_{k=0}^{1}v_k^TY(Bv)_k
=\sum_{k=0}^{1}\sum_{r\le k}v_k^TYB_{kr}v_r.
\]

Then

\[
Q_B^{\rm unweighted}(v)
=e_-^T\{\lambda YJ_pY-\lambda\kappa I\}e_-
=2\lambda\varepsilon^2e^{-\chi}>0.
\]

This rederives the scalar in (35) and proves a counterexample to nonpositivity of this particular label-paired quadratic form on supported histories. If the intended definition includes the time weight \(\lambda\), its value is instead \(2\lambda^2\varepsilon^2e^{-\chi}\), still positive. The pairing matters: the ordinary unweighted form \(\sum_kv_k^T(Bv)_k\) equals zero on this same example because \(e_-\perp e_+\).

The candidate first introduces \(\mathcal Q_B\) at (35), only through its evaluated expression for this one direction. It never defines the history functional or weights. Consequently the positive scalar is verified, but the unqualified sign-refutation claim in lines 596–601 and the corresponding row of Section 9 needs the explicit definition above, or a different declared definition followed by its own check. The missing definition cannot be supplied by reading the prohibited dependency.

The remaining qualifications are correct. Supported directions on this prefix must have \(v_0=v_1\); fixing the initial top source forces both to zero. Other roots can remain fixed. On the reverse support, \(u_0=0\), while \(S\) on this prefix can use only that reverse block. Hence \(S|_{\mathcal H_\Sigma}=0\) and \(DS=0\) there. There is no contradiction between this contraction statement and the positive label-paired scalar above. No assertion about the precise contents of an external storage inequality is needed or verified.

## 9. Required and optional corrections

**Required — define and scope the sign functional (Section 8, especially lines 589–601; Section 9, line 618).** Insert an explicit definition of \(\mathcal Q_B(v)\) as a function of the history and \(B\), including label factors and time weights. If it is the unweighted form \(\sum_kv_k^TY(Bv)_k\), (35) is correct unchanged. If it is time-weighted, adjust the value accordingly. State the counterexample as refuting nonpositivity of that named form on the allowed supported-source class. Without this correction, that one refutation is not self-contained.

**Optional — describe the removed support component precisely (lines 549–550).** Replace the claim about deleting the nonzero component in (34) by: “Projecting back onto \(\mathcal H_\Gamma\) removes a nonzero temporal sample-average contrast of the actual output.” This states exactly what the annihilating support functional proves.

**Optional — make the constant first-prefix input explicitly ‘constant in time’ (Section 8 title).** The vector is \(e_-\) at both times, but is antisymmetric across samples. The displayed definition already makes this clear; the title can avoid any alternative reading of “constant-source.”

**Optional — specify a readout-root extension only if it is later differentiated.** Equations (1)–(4) fix the deterministic root. The current exclusion of its nonzero variation is sufficient; a future derivative in that root would require an explicitly stated off-root equation. This is not an additional hypothesis needed for the present results.

No correction is required to the displayed mean formula, the singular Gaussian argument, the strict-gap constant, the exact learned-row constants, the expected-versus-squared sensitivity distinction, or the attained leakage construction.

## 10. Coverage and precise final scope

| Candidate claim | Audit result |
|---|---|
| Finite law (1)–(4), frozen derivatives, singular Gaussian inputs | Internally consistent; causal finite construction supplied above. |
| Readout/field bounds (5) and derivative integrability | Verified from the stated activations and finite recursion. |
| IBP/projection and mean/root identities (6)–(11) | Verified, including nonzero first-update mean and independent bottom root. |
| Support norms/maps and composite identity (12)–(14) | Verified on the actual covariance supports. |
| Nilpotence and finite resolvent (15) | Verified for derivative-only compositions; not a learned-feedback estimate. |
| Quantitative strictness (16)–(20) | Verified on each fixed nonzero support; zero-Gram cases handled separately. No mesh-uniform gap established. |
| Complete learned-kernel estimates (21)–(24) | Verified for supported inputs and full coordinate/time-weighted outputs. |
| Field moments and expected-source responses (25)–(30) | Verified with all memories and the supported bottom-root variation. No uniform squared-sensitivity or selection-map derivative bound. |
| Attained support-leakage construction (31)–(34) | Verified for \(\rho=-1,N=2\), every \(\lambda>0\); the input is constructed from the actual full \(\Sigma\). |
| First-prefix blocks, direction, norm, and positive scalar (35) | Verified. A sign-refutation statement requires the missing functional definition and weight convention. |
| Alleged identity or result located only in the named dependency | Not examined or imported. In particular no external storage identity is certified. |
| Uniform learned-feedback/storage closure; global or limiting theorem | Not established, and not inferred from these finite results. |

Subject to the explicit sign-functional correction, the candidate establishes a coherent bounded result for its stated finite law. The supported learned-row bounds use a weaker destination norm than the derivative-only covariance contractions. The attained leakage example proves that this distinction is necessary for the claimed direct map involving \(A\). Closing full learned feedback and correlated sensitivity products remains a separate, unresolved obligation.
