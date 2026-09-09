# Isolated adversarial audit: frozen-mask Gaussian response gap

## 1. Source, protocol, and verdict

Audited source:

    /tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_UNIFORM_GAUSSIAN_RESPONSE_GAP.md

The source was read in full: 263 lines, 12,036 bytes. All source-line references below refer to that version. No other mathematical files, histories, reviews, agent instructions, or external sources were read. No experiments, subagents, external imports, or numerical checks were used. The counterexamples below are direct analytic constructions. The source was not edited. This report was written using apply_patch.

SHA-256 before reading:

    a05a83e0ee5ea13d02a3ef51bb8967d1d3ddb7fd6eed601b4f1fdb4cea85c65a

SHA-256 after the audit and initial report write:

    a05a83e0ee5ea13d02a3ef51bb8967d1d3ddb7fd6eed601b4f1fdb4cea85c65a

The before and after hashes match exactly.

**Verdict: the finite-program inequality (6), including its factor \(\alpha\) for every deterministic combination of time nodes, is correct. The conditional covariance-supported contraction and inverse claims (10)–(13) are also correct. No required mathematical fix to those claims was found.**

The most important attempted counterexample—choosing time coefficients that cancel the entire frozen contribution—does not defeat the bound. The factor \(\alpha\) comes from independence of the mask and the standard Gaussian used in the integration-by-parts calculation. It does not require the tested feature combination to have positive energy on the frozen event.

There is one non-core verification limitation: the illustrative “upper program” at source lines 153–155 is not explicitly defined. Its particular integrability properties cannot be certified from this source alone. The actual theorem explicitly assumes the necessary integrability and second-moment consistency, so this is not a missing hypothesis in the theorem. Clarifying that illustration is classified separately below.

The audit does not impose or infer claims about full learned-memory contraction, mean-field uniqueness, model identification, global continuation, or a continuous-time limit. The document expressly excludes those conclusions.

## 2. Claim coverage

| Source claim | Audit result |
| --- | --- |
| Smooth compactly supported first derivative, bounded odd nonaffine activation, fixed across correlations; (1), lines 17–29 | Verified. |
| Finite, explicit, causal first population program; (2), lines 31–57 | Verified. Causality is dependence on earlier raw query coordinates; it does not assert independent Gaussian innovations. |
| Well-defined formal derivatives and finite moments, including singular query covariance; lines 59–75 | Verified by the derivative induction below. |
| Exact freezing for every query value and arbitrary finite coefficients; (4), lines 77–84 | Verified pointwise, including the saturation endpoints. |
| Positive mask-complement mass and a correlation-uniform upper bound below one; (5), lines 86–96 | Verified, including \(\rho=-1\). |
| Singular-covariance Gaussian integration by parts; (7), lines 109–123 | Verified without an inverse covariance or a density for the possibly singular query vector. |
| Masked covariance domination and arbitrary time-linear combinations; (6), (8), lines 100–140 and 224–230 | Verified. There is no dimension factor and no loss of \(\alpha\) under frozen-feature cancellation. |
| Assumed second-program consistency and unmasked response bound; (9), (10), lines 144–167 | Verified as a conditional theorem. No simultaneous construction is established or needed for the conditional conclusion. |
| Illustrative upper-program integrability sentence; lines 153–155 | Under-specified illustration. Not independently certified; not used as a premise in place of the explicit integrability hypothesis. |
| Exact range inclusions and pseudoinverse-square-root bounds; (11), lines 169–189 | Verified, with the stated ranges and orientations. |
| Covariance norms, both product contractions, and supported inverses; (12), (13), lines 191–220 | Verified. The contraction constant is \(\sqrt{\alpha}\), and the inverse bound is \(1/(1-\sqrt{\alpha})\). |
| Exclusions concerning memories, sample-wise derivatives, trace kernels, and uniqueness; lines 232–263 | Logically appropriate. The algebraic memory warning is correct; no network-limit identification is supplied or inferred. |

## 3. First program: construction, independence, and integrability

### 3.1 Activation

Write \(g=\phi_1'\). The given bump is positive for \(|z|<R\), is zero for \(|z|\ge R\), and is even. Inside its support, each derivative is a finite sum of a bounded polynomial in \(z\), powers of \((1-(z/R)^2)^{-1}\), and the original exponential. For any fixed power, the exponential tends to zero faster than that power diverges at an endpoint. Consequently every derivative extends by zero continuously across both endpoints. This establishes the stated smoothness and bounded derivatives for the example.

More generally, the initially allowed smooth compactly supported \(g\) has bounded derivatives by continuity on its compact support. Its primitive satisfies

\[
 |\phi_1(z)|\le B,\qquad
 \phi_1(z)=B\,\operatorname{sign}(z)\quad (|z|\ge R),
 \qquad
 B=\int_0^R g(u)\,du>0.
\]

Evenness of \(g\) gives oddness of \(\phi_1\). The derivative is positive on an interval and zero outside it, so \(\phi_1\) cannot be affine. None of these arguments depends on \(\rho\).

The endpoint derivative description at lines 24–26 should be understood as describing the displayed bump, not as a formula for every allowed smooth bump. That reading is sufficient and mathematically sound.

### 3.2 Causality and existence

Let \(d=2(N+1)\), and stack coordinates in increasing node order. Induction gives

\[
 Z^{(1)}_k,\ H^{(1)}_k
 \quad\text{as functions of}\quad
 (G,\zeta_0,\ldots,\zeta_{k-1}).
\]

At node \(k\), all terms in the sum defining \(Q^{(1)}_k\), including \(H^{(1)}_k\), have already been determined. Evaluating \(Q^{(1)}_k\) then determines \(Z^{(1)}_{k+1}\) explicitly. There is no circular equation at a node and no fixed point to solve.

Every finite input and every finite set of coefficients gives a finite trajectory. In particular,

\[
 |Q^{(1)}_{k,a}|
 \le |\zeta_{k,a}|+
 B\sum_{\ell\le k,b}|B_{ka,\ell b}|.
\]

The increments of \(Z^{(1)}\) are bounded by finite constants times \(1+|\zeta|\), because \(g\) is bounded. For each finite program one therefore also has a bound of the form

\[
 |Z^{(1)}_{k,a}|
 \le |G_a|+K_k(1+|\zeta|).
\]

There is no need for small coefficients, a small step size, or an infinite-horizon stability theorem.

The derivative blocks \(D_{\zeta_j}H^{(1)}_k\) vanish for \(j\ge k\). Thus \(S\) is strictly lower triangular in the time blocks. This is a valid additional check of the indexing, although neither the uniform gap nor the inverse estimate relies on this triangularity.

An arbitrary positive semidefinite \(\Sigma\) may correlate all query nodes. Thus the current \(\zeta_k\) need not be statistically independent of \(H^{(1)}_k\). The argument requires computational causality, not an independent-innovation interpretation of each node.

### 3.3 Precisely which variables are independent

The stated probabilistic assumption is independence of the entire vector \(\zeta\) and the entire root vector \(G\). It implies independence of \(F\), which is measurable in \(G\), and \(\zeta\).

For the proof one may equivalently construct the model from independent variables

\[
 G\sim N(0,C),\qquad Z\sim N(0,I_d),\qquad
 \zeta=\Sigma^{1/2}Z.
\]

This has exactly the prescribed joint law of \((G,\zeta)\), even when \(C\) or \(\Sigma\) is singular. In that representation \(F\) is independent of the full standard Gaussian vector \(Z\).

The memory-augmented \(Q^{(1)}\) is generally neither Gaussian nor independent of \(F\). This does not invalidate the proof: all differentiation and integration by parts are with respect to the raw coordinates \(\zeta\), represented through \(Z\).

For example, take \(N=0\), \(\Sigma=0\), and choose the response coefficients so that

\[
 Q^{(1)}_{0,1}=\phi_1(G_1).
\]

Then \(|Q^{(1)}_{0,1}|=B\) on \(F\), while
\(\Pr(|Q^{(1)}_{0,1}|<B)>0\). Since \(\Pr(F)>0\), this disproves independence of \(Q^{(1)}_{0,1}\) and \(F\). Its law has saturation atoms and is not Gaussian. The source's displayed formulas already distinguish the raw Gaussian source from this augmented query; the informal phrase “Gaussian query” could be tightened.

### 3.4 Derivative bounds

The needed bounds can be obtained uniformly in \(G\) for each fixed finite program. Let

\[
 J_{k,a}=D_\zeta Z^{(1)}_{k,a}
\]

be a row vector, and let \(e_{k,b}\) be the corresponding standard coordinate vector in \(\mathbb R^d\). Differentiating the explicit recursion gives

\[
 D_\zeta H^{(1)}_{k,a}
 =\phi_1'(Z^{(1)}_{k,a})J_{k,a},
\]

\[
 D_\zeta Q^{(1)}_{k,b}
 =e_{k,b}^{T}
 +\sum_{\ell\le k,c}B_{kb,\ell c}
       D_\zeta H^{(1)}_{\ell,c},
\]

and

\[
\begin{aligned}
 J_{k+1,a}
 =J_{k,a}+\lambda_k\sum_b C_{ab}c_{k,b}
 \bigl[
 &\phi_1''(Z^{(1)}_{k,b})Q^{(1)}_{k,b}J_{k,b}\\
 &+\phi_1'(Z^{(1)}_{k,b})D_\zeta Q^{(1)}_{k,b}
 \bigr].
\end{aligned}
\]

Here \(J_{0,a}=0\). The query has at most linear growth in \(|\zeta|\), and every displayed activation derivative is bounded. By induction, each \(J_{k,a}\) and \(D_\zeta H^{(1)}_{k,a}\) is bounded by a polynomial in \(1+|\zeta|\) with finite constants depending on the program.

At any fixed higher derivative order, repeated chain and product rules produce only finitely many products of bounded activation derivatives, previously bounded derivatives, and queries. The same induction therefore works at every fixed order.

This proves the asserted Gaussian integrability. The state itself also involves \(|G|\), as in the preceding state bound; the \(\zeta\)-derivative bounds do not require a polynomial factor in \(G\). Singular Gaussian vectors still have every polynomial moment because they are linear images of a finite-dimensional standard Gaussian.

No interchange of a derivative with a changing covariance, a changing response coefficient, or a self-consistency map is being made. All coefficients are held fixed exactly as required in the definition of \(S\).

### 3.5 Exact frozen event and its mass

On \(F\), both \(g(G_a)\) vanish, including when \(|G_a|=R\). If the state has stayed equal to \(G\) up to node \(k\), every term in its next increment contains a zero gate. Thus its increment is zero. Induction proves (4) for every value of the full ambient query vector.

In particular, it is not merely an almost-sure constancy along the support of one singular Gaussian: for a root in \(F\), the feature path is constant as a function of all formal query coordinates. All its \(\zeta\)-derivatives vanish there.

Each \(G_a\) is standard normal even at \(\rho=-1\). Consequently

\[
 0<\Pr(|G_1|<R)
 \le\alpha
 \le 2\Pr(|G_1|<R)
 \le \frac{4R}{\sqrt{2\pi}}=:a_R<1.
\]

The last strict inequality follows from \(R<1/4\). In particular \(\Pr(F)>0\).

At \(\rho=-1\), \(G_2=-G_1\) almost surely, and
\(\alpha=\Pr(|G_1|<R)\). No joint density of \(G\) was used. The quantity \(\alpha\) may depend on \(\rho\), but \(a_R\) is a single usable upper bound for every allowed correlation. No feature-Gram eigenvalue conclusion follows from this probability estimate.

## 4. Gaussian integration by parts and the uniform gap

### 4.1 Singular-covariance Stein calculation

For fixed deterministic \(v\in\mathbb R^d\), put \(L=v^TH\). The bound

\[
 |L|\le B\sum_i|v_i|
\]

holds for every \(G,\zeta\). For fixed \(G\) and all other standard Gaussian coordinates, integration by parts in \(Z_j\) gives

\[
 \int_{\mathbb R}z_jL\,\gamma(z_j)\,dz_j
 =
 \int_{\mathbb R}\partial_{z_j}L\,\gamma(z_j)\,dz_j.
\]

The boundary term vanishes since \(L\) is bounded and the Gaussian density tends to zero. The derivative has polynomial growth in the full vector \(Z\), since \(\zeta=\Sigma^{1/2}Z\). The derivative bound above is uniform in \(G\). Thus both sides are absolutely integrable over the other coordinates and \(G\), which justifies the iterated integrations.

The symmetric positive semidefinite square root has the orientation

\[
 D_ZH=(D_\zeta H)\Sigma^{1/2},
\]

so the resulting column-vector identity is exactly

\[
 \mathbb E[ZL]=\Sigma^{1/2}S^Tv.
\]

There is no inversion of \(\Sigma\), no assumption that \(\zeta\) has a full-dimensional density, and no missing transpose.

Formal derivatives normal to the support of \(\Sigma\) do not cause an ambiguity in this identity: the multiplication by \(\Sigma^{1/2}\) removes those directions. The recursion supplies the ambient extension used to define \(S\).

### 4.2 Where the factor \(\alpha\) comes from

Set \(A=F^c\). On \(F\), \(L\) is a function \(L_F(G)\) of the root alone. Therefore

\[
 \mathbb E[Z1_FL]
 =\mathbb E_G[1_F L_F(G)\,\mathbb E_Z Z]=0.
\]

For a deterministic Euclidean unit vector \(u\),

\[
\begin{aligned}
 |u^T\mathbb E[ZL]|^2
 &=|\mathbb E[1_A(u^TZ)L]|^2\\
 &\le \mathbb E[1_A(u^TZ)^2]\,
       \mathbb E[1_A L^2]\\
 &=\alpha\,\mathbb E[1_A L^2].
\end{aligned}
\]

The final equality uses independence of \(A\) and \(Z\) and
\(\mathbb E[(u^TZ)^2]=1\). It does not use independence of \(L\) and \(Z\).

Taking the supremum over deterministic unit \(u\) yields

\[
 \|\mathbb E[ZL]\|^2
 \le\alpha\,\mathbb E[1_A L^2].
\]

This operation produces no factor of \(d\). A weaker argument that used \(\mathbb E[1_A|Z|^2]=\alpha d\) would lose dimension independence, but that is not the argument in the source.

Using the Stein identity gives, for every deterministic \(v\),

\[
 v^TS\Sigma S^Tv
 \le\alpha\,v^T\Gamma_Av,\qquad
 \Gamma_A:=\mathbb E[1_AHH^T].
\]

Since \(0\preceq\Gamma_A\preceq\Gamma\), this proves both inequalities in (6).

These are uncentered second moments. No assumption \(\mathbb EH=0\) or \(\mathbb E\Delta=0\) is needed for the argument as written. Replacing the second moments with centered covariances would be a different assertion requiring its own check.

### 4.3 Time-node cancellation: the main adversarial test

For an arbitrary coefficient array \(v_{k,a}\), the frozen value is

\[
 L_F(G)
 =B\sum_{a=1}^2\operatorname{sign}(G_a)
       \sum_{k=0}^N v_{k,a}.
\]

Thus, for example, the conditions

\[
 \sum_{k=0}^Nv_{k,1}
 =\sum_{k=0}^Nv_{k,2}=0
\]

cancel the entire frozen contribution. A single difference
\(H^{(1)}_{j,a}-H^{(1)}_{i,a}\) is a basic such test. There are additional possible cancellations when the root covariance is singular.

If \(L=0\) on \(F\), then

\[
 \mathbb E[1_A L^2]=\mathbb E[L^2],
\]

but the other factor in the masked Cauchy–Schwarz inequality remains

\[
 \mathbb E[1_A(u^TZ)^2]=\alpha.
\]

Hence even for a combination with no frozen energy,

\[
 v^TS\Sigma S^Tv\le\alpha\,v^T\Gamma v.
\]

Equivalently, conditioning on \(A\) gives

\[
 \mathbb E[ZL]=\alpha\,\mathbb E[ZL\mid A],
\]

and the conditional Gaussian linear form still has second moment one. Squaring introduces \(\alpha^2\), while
\(\mathbb E[1_A L^2]=\alpha\mathbb E[L^2\mid A]\); the net coefficient is exactly the \(\alpha\) in (6). It cannot disappear through cancellation of \(L_F\).

All time coefficients may depend on the fixed program, its deterministic covariances, and \(N\). They must be deterministic in the tested inequality, rather than chosen from the realized \(G\) or \(Z\). This is precisely the quantification used in a matrix inequality.

The resulting relative gap can also be written

\[
 \Gamma-S\Sigma S^T\succeq(1-\alpha)\Gamma.
\]

It is positive definite as a quadratic form on \(\operatorname{ran}\Gamma\), unless that space is zero-dimensional, and is permitted to vanish on \(\ker\Gamma\). “Strict” here means a relative supported gap, not a positive multiple of the ambient Euclidean identity.

### 4.4 Why the bound is uniform

The only final constant is the initial mask probability. Neither derivative bounds, the size of \(v\), the number of time nodes, response coefficients, step sizes, nor positive covariance eigenvalues occur in that constant.

There can be arbitrarily large program-dependent bounds in the preliminary integrability proof; those bounds only establish that the exact integration identities exist. They are not used as numerical estimates in (6).

Consequently one can replace \(\alpha\) by \(a_R\) throughout to obtain a common bound across correlations and finite programs. This establishes the advertised time-node-uniform finite-dimensional conclusion. It does not supply convergence of an infinite-node program or justify passage to a continuous-time limit.

## 5. Second program, supports, and inverse norms

### 5.1 The conditional second-program statement

The input \(\xi\) has Gaussian covariance \(\Gamma\), while the output is assumed to satisfy the uncentered second-moment identity

\[
 \mathbb E[\Delta\Delta^T]=\Sigma.
\]

The required integrability and existence of \(D=\mathbb E[D_\xi\Delta]\) are explicit hypotheses. It is sufficient that the output be bounded and its derivatives be polynomially bounded; other conditions can also suffice.

Writing \(\xi=\Gamma^{1/2}Z'\), with \(Z'\) standard Gaussian, the same coordinate calculation yields

\[
 \mathbb E[Z'v^T\Delta]=\Gamma^{1/2}D^Tv.
\]

For every deterministic unit \(u\),

\[
 |\mathbb E[(u^TZ')v^T\Delta]|^2
 \le \mathbb E[(u^TZ')^2]\mathbb E[(v^T\Delta)^2]
 =v^T\Sigma v.
\]

Taking the supremum over \(u\) proves

\[
 D\Gamma D^T\preceq\Sigma.
\]

No mask, causality of \(D\), zero output mean, or coupling of \(Z'\) to the first population is required. A simultaneous covariance-consistent construction is not established: (9) is an assumption, exactly as the source states.

### 5.2 Exact range inclusions

If \(v\in\ker\Gamma\), then (6) implies

\[
 0\le\|\Sigma^{1/2}S^Tv\|^2
 =v^TS\Sigma S^Tv
 \le\alpha\,v^T\Gamma v=0.
\]

Thus every vector in \(\ker\Gamma\) is orthogonal to
\(\operatorname{ran}(S\Sigma^{1/2})\), and

\[
 \operatorname{ran}(S\Sigma^{1/2})
 \subseteq\operatorname{ran}\Gamma.
\]

Because a positive semidefinite matrix and its square root have the same range in finite dimensions, this is precisely

\[
 S\,\operatorname{ran}\Sigma\subseteq\operatorname{ran}\Gamma.
\]

Applying the identical argument to (10) proves
\(D\,\operatorname{ran}\Gamma\subseteq\operatorname{ran}\Sigma\).

These statements do not imply that \(S\) or \(D\) maps its entire ambient domain into the indicated range. They are restricted-domain inclusions, and that distinction is essential.

### 5.3 Weighted operators and the exact product constant

Define

\[
 T=\Gamma^{\dagger/2}S\Sigma^{1/2},\qquad
 U=\Sigma^{\dagger/2}D\Gamma^{1/2}.
\]

Congruence of (6) and (10) by the respective pseudoinverse square roots gives

\[
 TT^T\preceq\alpha P_\Gamma,\qquad
 UU^T\preceq P_\Sigma.
\]

Therefore
\(\|T\|_{\mathrm{op}}\le\sqrt{\alpha}\) and
\(\|U\|_{\mathrm{op}}\le1\).

The support identities are

\[
 T=P_\Gamma T P_\Sigma,\qquad
 U=P_\Sigma U P_\Gamma.
\]

On \(E_\Sigma:=\operatorname{ran}\Sigma\), the map
\(\Sigma^{\dagger/2}\) is an isometry from the norm
\(|x|_\Sigma=|\Sigma^{\dagger/2}x|\) to the ordinary Euclidean norm on \(E_\Sigma\), with inverse \(\Sigma^{1/2}\) restricted to that space. The analogous statement holds on \(E_\Gamma:=\operatorname{ran}\Gamma\).

Consequently the norms in (11) are exactly the corresponding supported operator norms:

\[
 \|S:E_\Sigma\to E_\Gamma\|=\|T\|_{\mathrm{op}},\qquad
 \|D:E_\Gamma\to E_\Sigma\|=\|U\|_{\mathrm{op}}.
\]

There is no missing covariance factor. In particular,

\[
\begin{aligned}
 \Sigma^{\dagger/2}DS\Sigma^{1/2}
 &=\Sigma^{\dagger/2}D P_\Gamma S\Sigma^{1/2}
 =UT,\\
 \Gamma^{\dagger/2}SD\Gamma^{1/2}
 &=\Gamma^{\dagger/2}S P_\Sigma D\Gamma^{1/2}
 =TU.
\end{aligned}
\]

The inserted projections can be removed or inserted exactly because of the established range inclusions.

Thus both supported products have operator norm at most \(\sqrt{\alpha}\), as in (12). A bound by \(\alpha\) for these operator norms would not follow: (6) is a squared-norm bound, while the second response contributes a norm bound of one.

The covariance norms are genuine norms on their indicated ranges, including when the covariances are singular. On the full ambient spaces they would only be seminorms; the source does not use them there.

### 5.4 Supported inverses

For \(K=DS|_{E_\Sigma}\) or \(K=SD|_{E_\Gamma}\), one has
\(\|K\|\le q:=\sqrt{\alpha}<1\). Thus

\[
 R_m=\sum_{j=0}^mK^j
\]

is a Cauchy sequence in the supported operator norm and satisfies

\[
 (I-K)R_m=R_m(I-K)=I-K^{m+1},\qquad
 \|K^{m+1}\|\le q^{m+1}\longrightarrow0.
\]

The limiting operator is a two-sided inverse, and

\[
 \|(I-K)^{-1}\|\le\sum_{j=0}^{\infty}q^j
 =\frac1{1-\sqrt{\alpha}}.
\]

The identity in this calculation is the identity of the relevant supported space. It is not an assertion that the full ambient matrix has an inverse, or an identification with its Moore–Penrose pseudoinverse.

A single correlation-uniform version is

\[
 \|(I-DS)^{-1}\|_\Sigma,\ 
 \|(I-SD)^{-1}\|_\Gamma
 \le
 \frac1{1-\sqrt{\,4R/\sqrt{2\pi}\,}}.
\]

No positive eigenvalue lower bound is required for this numerical constant. Small eigenvalues can still make comparisons to Euclidean norms arbitrarily poor. The proof neither overlooks nor resolves that separate issue.

## 6. Adversarial constructions and boundary cases

### 6.1 Full ambient invertibility can fail in an admissible program

This is a counterexample to an extension the source does not claim. It directly tests whether the supported restriction is doing substantive work.

Take \(N=1\), \(\rho=0\), all response coefficients \(B_{ka,\ell b}=0\), \(\lambda_0=1\), \(c_{0,1}=c_{0,2}=1\), and \(\Sigma=0\). Stack the two nodes as blocks of size two. Set

\[
 \gamma=\mathbb E[\phi_1(G_1)^2]>0,\qquad
 \beta=\mathbb E[\phi_1'(G_1)^2]>0.
\]

Since \(\zeta=0\) almost surely, both feature nodes equal
\(h=(\phi_1(G_1),\phi_1(G_2))\). Independence of the two root coordinates and oddness give

\[
 \Gamma=\gamma
 \begin{pmatrix}I_2&I_2\\I_2&I_2\end{pmatrix},\qquad
 S=
 \begin{pmatrix}0&0\\\beta I_2&0\end{pmatrix}.
\]

Now define the legitimate differentiable second program

\[
 \Delta(\xi)=D\xi,\qquad
 D=\beta^{-1}
 \begin{pmatrix}-I_2&I_2\\0&0\end{pmatrix}.
\]

The Gaussian \(\xi\) is supported on
\(E_\Gamma=\{(w,w):w\in\mathbb R^2\}\), so \(\Delta(\xi)=0\) almost surely. Hence
\(\mathbb E[\Delta\Delta^T]=0=\Sigma\), and (9) is satisfied. The derivative is constant, and Gaussian integration by parts is justified.

Nevertheless

\[
 DS=\begin{pmatrix}I_2&0\\0&0\end{pmatrix},\qquad
 SD=\begin{pmatrix}0&0\\-I_2&I_2\end{pmatrix}.
\]

Both \(I-DS\) and \(I-SD\) are singular on the ambient four-dimensional space.

On the claimed supports, however, \(E_\Sigma=\{0\}\) and \(SD\) vanishes on \(E_\Gamma\). The supported inverses therefore exist exactly as the theorem states. All range and norm claims survive.

This example also shows why off-support formal derivatives cannot be silently treated as zero: the ambient \(S\) and \(D\) are nonzero even though the Gaussian output of the second program is identically zero.

### 6.2 Mean-square derivative growth is not controlled

The distinction at source lines 138–140 is real even within the stated first program.

Take \(N=1\), \(\rho=0\), no response coefficients, and a single standard Gaussian raw query \(Z=\zeta_{0,1}\), independent of \(G\); take the other raw queries to be zero. Let the effective first-coordinate step be \(t\ge1\). With \(g=\phi_1'\),

\[
 Y=G_1+t\,g(G_1)Z,\qquad
 J:=\frac{\partial H^{(1)}_{1,1}}{\partial\zeta_{0,1}}
 =t\,g(G_1)g(Y).
\]

Fix \(r=R/2\). There are constants \(m>0\) and \(M<\infty\) such that
\(m\le g(x)\le M\) for \(|x|\le r\), with \(M\) also an upper bound globally.

For a fixed \(|G_1|\le r\), the event \(|Y|\le r\) corresponds to an interval of \(Z\) of length

\[
 \frac{2r}{t\,g(G_1)}\ge\frac{2r}{tM}.
\]

For \(t\ge1\), this interval is contained in the fixed compact interval
\([-2r/m,2r/m]\). The standard Gaussian density has a positive lower bound there. Consequently

\[
 \Pr(|Y|\le r\mid G_1)\ge \frac{c}{t}
 \quad\text{when }|G_1|\le r
\]

for a fixed \(c>0\). On this event \(J^2\ge t^2m^4\), so

\[
 \mathbb E[J^2]\ge c'\,t
\]

for another constant \(c'>0\). Meanwhile
\(\mathbb E[(H^{(1)}_{1,1})^2]\le B^2\).

Thus a uniform analogous domination for the mean-square derivative would be false. Every fixed-\(t\) derivative remains integrable, and the bound on the square of the expected derivative remains valid. This confirms the source's stated distinction and its lack of a uniform derivative-moment claim.

### 6.3 Other attempted failure mechanisms

| Attempt | Outcome |
| --- | --- |
| Increase the number of time nodes or use large alternating time weights | The proof tests the whole scalar combination at once; the constant remains \(\alpha\). |
| Cancel all frozen features with node differences | The feature second moment on \(F\) disappears, but the Gaussian mask factor remains. |
| Make the query covariance singular or strongly correlated across time | The standard-Gaussian representation and chain rule still apply; no covariance inverse occurs. |
| Use \(\rho=-1\) | The mask and its positive complement mass remain valid; singular feature supports are handled explicitly. |
| Let \(\rho\) approach \(1\) | The marginal density bound remains unchanged. No eigenvalue lower bound is used. |
| Choose arbitrarily large finite steps or deterministic coefficients | Finite integrability constants may grow, but freezing and the exact covariance estimate persist. |
| Use \(N=0\) | \(S=0\), so the first estimate is immediate and consistent with the causal indexing. |
| Test a direction in \(\ker\Gamma\) | The inequality forces the corresponding supported Gaussian response to vanish; no division by zero is needed. |
| Infer an ambient inverse from the supported statement | False, as the explicit admissible example above shows; the source correctly restricts its claim. |
| Replace the squared expected derivative by the expected squared derivative | False uniformly, as the preceding analytic construction shows; the source explicitly excludes this. |

## 7. Scope and the learned-memory warning

The source's memory example is a valid algebraic demonstration. With
\(\Gamma=\Sigma=\operatorname{diag}(1,0)\) and \(S=D=0\), the response inequalities are satisfied, and the supported inverses are identities. Choosing \(M_Ae_1=e_2\) maps a supported vector outside the supported range.

The inequalities cannot impose restrictions on an additional matrix that does not occur in them. Even imposing range preservation on extra memories would not produce a norm bound without another argument.

The example is expressly labeled algebraic rather than an actual trained trajectory. It need not arise from (2) in order to establish that those response inequalities alone do not control arbitrary added memories.

The document consequently makes the appropriate exclusions. It has not bounded the full learned-memory feedback inverse, the full sample-wise Jacobian, or the time-integrated cavity trace kernel. It has not established mean-field uniqueness or identified a particular network limit.

Its closing requirements for application are substantive: a network derivation would need to identify a raw Gaussian source independent of the root, justify freezing the deterministic coefficients for these derivatives, and establish the assumed second-program consistency and integrability. None of that identification is supplied by the finite-program inequality itself.

## 8. Required fixes and optional exposition

### 8.1 Required mathematical fixes

**None found for the stated finite-program lemma, the conditional supported inverse theorem, or their explicit scope.**

In particular, no repair is needed to the coefficient \(\alpha\), the treatment of combinations that cancel frozen features, the singular-covariance Stein identity, either range inclusion, the product order, the square root in the contraction factor, or the Neumann-series inverse bound.

### 8.2 Non-core illustration that remains under-specified

Source lines 153–155 refer to a finite upper program using \(\arctan\), a zero initial readout, bounded readout increments, and fixed causal coefficients. No recurrence for that particular program or its output \(\Delta\) is given. Thus this audit cannot independently verify its stated integrability properties.

Bounded readout increments alone do not control derivatives. For example, the smooth bounded scalar function

\[
 f(x)=\sin(e^{x^2})
\]

satisfies
\(f'(x)=2xe^{x^2}\cos(e^{x^2})\). If \(X\) is standard normal, then, restricting to \(x\ge1\) and setting \(u=e^{x^2}\),

\[
\begin{aligned}
 \mathbb E|f'(X)|
 &\ge \frac1{\sqrt{2\pi}}
       \int_1^\infty
        2xe^{x^2}|\cos(e^{x^2})|e^{-x^2/2}\,dx\\
 &=\frac1{\sqrt{2\pi}}
       \int_e^\infty |\cos u|\,u^{-1/2}\,du
 =\infty.
\end{aligned}
\]

The final integral diverges by restricting to a fixed positive-length interval around each sufficiently large multiple of \(2\pi\), on which \(|\cos u|\ge1/2\), and summing a constant times \(n^{-1/2}\).

This is not presented as a counterexample to the intended, unspecified upper network or to (9): it demonstrates why mere boundedness of an increment is not a derivative-integrability argument. A defined recurrence using controlled smooth operations could readily supply the missing verification.

For a completely standalone presentation, either give that recurrence and its induction, delete the illustrative sentence, or explicitly describe it as an application whose integrability must be checked. Because the main result already assumes the required integration by parts, and no actual upper-network application is claimed, this is an optional clarification rather than a required repair to the theorem.

### 8.3 Other optional improvements

1. **Distinguish raw and augmented queries.** At lines 53–54, “current query, formed from a raw Gaussian coordinate and already computed features” would avoid implying that \(Q^{(1)}_k\) itself is Gaussian or mask-independent.

2. **Make the common correlation-uniform constant explicit.** Defining \(a_R=4R/\sqrt{2\pi}\) once would distinguish the actual, correlation-dependent \(\alpha\) from a single bound usable for every correlation.

3. **Expand the derivative induction by one line.** The displayed formula for \(J_{k+1,a}\) above would make the integrability claim immediately checkable without changing any hypothesis.

4. **State the supported identity explicitly near (13).** Writing the inverse as that of \(I_{E_\Sigma}-DS|_{E_\Sigma}\), and similarly on \(E_\Gamma\), would emphasize that no ambient inverse or ambient pseudoinverse is asserted.

5. **State the meaning of the strict gap.** The formula
   \(\Gamma-S\Sigma S^T\succeq(1-\alpha)\Gamma\)
   succinctly shows strictness on the covariance support and compatibility with a singular ambient matrix.

6. **Give one explicit cancelling combination.** Using \(H^{(1)}_{j,a}-H^{(1)}_{i,a}\) would illustrate why losing all frozen feature energy does not lose the \(\alpha\) factor.

These suggestions improve precision or accessibility. They do not alter the proof or add missing premises to the principal claims.

## 9. Final audit conclusion

For every specified finite program (2), the proof establishes

\[
 S\Sigma S^T
 \preceq
 \alpha\,\mathbb E[1_{F^c}HH^T]
 \preceq\alpha\Gamma,
 \qquad
 0<\alpha\le\frac{4R}{\sqrt{2\pi}}<1.
\]

The proof remains valid for singular root and query covariances, arbitrary deterministic combinations across all time nodes, and arbitrary finite deterministic coefficients and step sizes.

Whenever the separately stipulated second program satisfies its integrability and consistency assumptions, both feedback products contract by at most \(\sqrt{\alpha}\) in the stated covariance norms on their respective supported spaces, and both supported inverse norms are bounded by \(1/(1-\sqrt{\alpha})\).

No in-scope counterexample was found. The limitations concerning unsupported directions, derivative second moments, additional learned memories, and model identification are essential and are respected by the source.
