# Independent audit of the gap-free reciprocal response step

2026-10-07. Complete frozen-input audit of GAP_FREE_RESPONSE_STEP.md, 495 lines, SHA-256 b469edebd54034a250a5a2485e951d147af9c643441642d0b32b8eec60eb8c42.

Scientific inputs were exactly that complete note and this author's existing Gaussian-conditioning background. No cited audit, other verdict, integrated study, other study, literature, experiment, or Git history was consulted. The original note was not edited.

## Verdict

The covariance-factor lemma, conditional reciprocal-block theorem, deterministic-population corollary, and conditional weighted-moment extension are mathematically sound within their stated chronological scope. I found no missing spectral-gap hypothesis and no hidden loss from taking an ordinary covariance square root.

Two local statement corrections should be made:

1. Introductory equation (1) should be conditional on \(H\), or its right side should average the random ranks. The formal theorem (15) already has the correct conditional form.
2. In matrix completion (19), the newly introduced matrix \(W\) must be specified to have **independent Gaussian** \(N(0,1/n)\) entries, independent of all previously constructed variables. An unspecified matrix with entry variance \(1/n\) is not sufficient for the asserted Gaussian completion. This is a correction to the construction's wording, not an additional assumption on the target problem.

There are also useful minor clarifications concerning finite second moments in the unbounded extension and independence from the complete lower-root sample; both can be supplied without changing a bound. Exact replacements are listed in Section 8.

| Source component | Audit result |
|---|---|
| Lemma 1, including noncommuting covariance factors | Pass |
| Conditional posterior and regression mean | Pass |
| Exact completion of the entire initialized matrix | Pass after explicitly choosing Gaussian \(W\) |
| Orthogonal decomposition and \(M^2(2r_H+r_D)/n\) bound | Pass |
| Simultaneous actual/reference coupling and reference independence | Pass |
| Singular support, zero ranks, and off-support extensions | Pass |
| Population covariance and response-coefficient transfer | Pass under the explicit assumption (29) |
| Unbounded weighted-moment formula | Pass when \(T,R\) and the displayed weighted moments are finite and well defined |
| Probability, pairing consequences, and exclusions | Pass |

## 1. Notation and precise object being compared

The source conditions on a lower-query matrix \(H\in\mathbb R^{n\times k}\), independent of the initialized \(G\in\mathbb R^{n\times n}\), and puts
\[
Q=H^\top H/n,\qquad Y=GH,\qquad
D_i=\Psi(Y_i,Z_i),\qquad X=G^\top D.
\]
The upper roots \(Z_i\) are independent copies, independent of \((H,G)\). The same row map is used throughout the block, with coefficients fixed after conditioning on \(H\). Thus the upper rows are independent conditional on \(H\), even when the lower rows themselves are not independent.

With \(Y_*\sim N(0,Q)\) and an independent upper root \(Z_*\), the response and primitive covariance are
\[
R_{aj}=\mathbb E[\partial_a\Psi_j(Y_*,Z_*)\mid H],
\qquad
T=\mathbb E[\Psi(Y_*,Z_*)\Psi(Y_*,Z_*)^\top\mid H].
\]
Here \(R\) is \(k\times\ell\), and \(T\) is \(\ell\times\ell\). The intended comparison is
\[
\overline X=HR+\Xi,
\]
where the rows of \(\Xi\) are independent \(N(0,T)\) conditional on \(H\), and independent of the actual upper fields conditional on \(H\). No independence of \(\Xi\) from the entire target matrix \(G\) is required. Imposing that additional independence would rule out useful couplings and is not what the source states.

This chronology is important: \(H\) has not previously queried this \(G\), and \(D\) has not used a prior reverse answer. The proof does not extend unchanged to a later alternating query or to coefficients estimated from the realized upper rows.

## 2. Noncommuting covariance-factor lemma

Write \(B=\mathbb E[vv^\top]\), \(A=n^{-1}\sum_i v_iv_i^\top\), and \(E=\operatorname{range}B\). Almost surely \(v_i\in E\), since each covariance-null linear functional vanishes almost surely. A finite basis of \(\ker B\) is enough to make this a simultaneous assertion. Hence no null-space leakage of the sample covariance is being ignored.

On \(E\), \(B>0\). Put
\[
C=B^{-1/2}AB^{-1/2},\qquad
\zeta=B^{1/2}z,\qquad
\zeta_n=B^{1/2}C^{1/2}z,
\]
for a fresh standard Gaussian \(z\) on \(E\). The factor for the empirical Gaussian is correct:
\[
(B^{1/2}C^{1/2})(B^{1/2}C^{1/2})^\top
=B^{1/2}CB^{1/2}=A.
\]
No commutation of \(B\) and \(C\) is used. In particular this factor need not be the positive square root \(A^{1/2}\).

For \(c\ge0\), \((\sqrt c-1)^2\le(c-1)^2\). Spectral calculus therefore gives
\[
(C-I)^2-(C^{1/2}-I)^2\succeq0.
\]
Its trace against \(B\succeq0\) is nonnegative, regardless of commutation. Consequently
\[
\begin{aligned}
\mathbb E_z|\zeta_n-\zeta|^2
&=\operatorname{tr}[B(C^{1/2}-I)^2]\\
&\le \operatorname{tr}[B(C-I)^2]\\
&=\operatorname{tr}[(A-B)B^\dagger(A-B)].
\end{aligned}
\]
The last equality is a cyclic trace identity: writing \(\Delta=A-B\),
\[
\operatorname{tr}\!\left[
B(B^{-1/2}\Delta B^{-1/2})^2\right]
=\operatorname{tr}[\Delta B^{-1}\Delta]
\]
on \(E\). It does not move noncommuting factors past each other outside a trace.

Independence of the centered sample covariance summands gives exactly
\[
\mathbb E\operatorname{tr}[\Delta B^\dagger\Delta]
=\frac1n\left(
\mathbb E[|v|^2v^\top B^\dagger v]-\operatorname{tr}B
\right).
\]
Under \(|v|\le M\), the first expectation is at most
\[
M^2\mathbb E[v^\top B^\dagger v]
=M^2\operatorname{rank}B.
\]
This proves the advertised bound. The population Gaussian is independent of the sample because its covariance factor is deterministic and its fresh Gaussian seed is independent of that sample. Applying the same construction with independent seeds to many output rows preserves their conditional independence, despite their shared empirical covariance.

There is no measurable-selection obstruction when \(B\) depends on \(H\) or its rank changes. One may work in the ambient space, use the spectral pseudoinverse and positive square root, and project an ambient fresh standard Gaussian onto \(\operatorname{range}B\). These are measurable matrix functions; a measurable choice of eigenbasis is unnecessary.

## 3. Exact conditioning, completion, and the main error estimate

### 3.1. Posterior and completion

Let \(P\) project onto \(\operatorname{range}H\). The posterior
\[
G\mid(H,Y,Z)\ \stackrel{\rm law}=
YH^\dagger+\widetilde G(I-P)
\]
is correct: the additional conditioning on \(Z\) changes nothing, since it is initially independent and \(D\) is only a function of \((Y,Z)\). Consistency \(Y=YH^\dagger H\) holds on the Gaussian support, including when \(H\) is rank deficient.

For \(T_n=D^\top D/n\), the resulting transpose action is
\[
X=H A_n+(I-P)\Xi_n,\qquad
A_n=Q^\dagger Y^\top D/n,
\]
with conditionally independent Gaussian rows of \(\Xi_n\) having covariance \(T_n\). The powers of \(n\) are correct: \((H^\top H)^\dagger=Q^\dagger/n\).

Given such a Gaussian \(\Xi_n\), the source completes the matrix using
\[
\widetilde G^\top
=\Xi_nD^\dagger+W^\top(I-P_D).
\]
With \(W\) chosen to have independent \(N(0,1/n)\) entries independently of everything already sampled, this is exact. Indeed, each row of the first term has covariance
\[
(D^\dagger)^\top\frac{D^\top D}{n}D^\dagger
=P_D/n.
\]
Each row of the second has covariance \((I-P_D)/n\); the two terms are independent centered Gaussian vectors. Different rows are independent. Thus the sum has precisely the required independent-entry Gaussian law conditional on \((H,Y,Z)\). Also
\[
\widetilde G^\top D
=\Xi_nD^\dagger D=\Xi_n
\]
because every row of \(\Xi_n\) is supported in the row space of \(D\).

The completed \(G\) satisfies \(GH=Y\) and \(G^\top D=X\) simultaneously. Integrating the correct conditional posterior against the already constructed correct forward law recovers the original joint marginal of \((G,H,Y,Z)\), including the original independence of \(G\) from the lower inputs and upper roots. Coupling the primitive \(\Xi\) with this \(G\) introduces no contradiction, since their independence was never required.

### 3.2. Response mean and singular support

The singular Gaussian Stein identity
\[
\mathbb E[Y_*\Psi(Y_*,Z_*)^\top\mid H]=QR
\]
follows by writing \(Y_*=Lz\), integrating in the independent Gaussian coordinates of \(z\), and applying the chain rule. No inverse of \(Q\) is used in this identity.

Set \(B_n=Y^\top D/n\). Since each column of \(B_n-QR\) lies in \(\operatorname{range}Q\), and \(H\) annihilates \(\ker Q\), the source's weighted identity is exact:
\[
\|H(A_n-R)\|_{F,n}^2
=\|Q^{\dagger/2}(B_n-QR)\|_F^2.
\]
The centered summands on the right are independent conditional on \(H\). Their second moment is at most \(M^2r_H\), where \(r_H=\operatorname{rank}Q\). Therefore the mean-square bound \(M^2r_H/n\) follows without estimating individual regression coefficients. A large pseudoinverse coefficient in a small-variance direction is not silently bounded by a gap-dependent constant.

### 3.3. Orthogonality and constants

The exact difference decomposition is
\[
X-\overline X
=H(A_n-R)-P\Xi+(I-P)(\Xi_n-\Xi).
\]
The last term is spatially orthogonal to the first two for every realization. The cross term between the first two vanishes in conditional expectation because \(\Xi\) is centered conditional on \((H,Y,Z)\). Finally
\[
\mathbb E[\|P\Xi\|_{F,n}^2\mid H]
=r_H\operatorname{tr}T/n\le r_HM^2/n.
\]
Lemma 1 contributes \(M^2r_D/n\), where \(r_D=\operatorname{rank}T\). Adding the three contributions proves
\[
\mathbb E[\|X-\overline X\|_{F,n}^2\mid H]
\le \frac{M^2}{n}(2r_H+r_D).
\]
No factor from a triangle inequality has been omitted: orthogonality and the centered cross term are exactly what avoid it.

## 4. Simultaneous population-reference coupling

The deterministic-population corollary has a stronger premise than the conditional theorem: the lower rows are independent bounded copies, and the row circuit is the same for every realization of \(H\). The stated response stability assumption (29) is necessary to the provided proof; the source does not infer it from covariance continuity.

Let \(Q_0=\mathbb E[h(U)h(U)^\top]\). Lemma 1 supplies row pairs \((Y_H,Y_0)\) with the correct covariances \(Q,Q_0\), and
\[
\mathbb E\delta_H^2\le B^2\operatorname{rank}Q_0/n,
\qquad
\delta_H^2=\mathbb E[|Y_H-Y_0|^2\mid H].
\]
The \(Y_0\) marginal is the same product Gaussian law for every lower sample. Using fresh Gaussian seeds independent of the complete lower-root sample ensures that all \(Y_{0,i}\) are independent of those roots, not just of the statistic \(H\).

Now couple \(d_H=\Psi(Y_H,Z_*)\) and \(d_0=\Psi(Y_0,Z_*)\) with the same independent auxiliary root. The uncentered block second-moment matrix of \((d_H,d_0)\) is positive semidefinite. A centered Gaussian pair \((\xi_H,\xi_0)\) with this block covariance therefore exists, and
\[
\mathbb E[|\xi_H-\xi_0|^2\mid H]
=\mathbb E[|d_H-d_0|^2\mid H].
\]
This equality would generally fail if means were subtracted from the query covariances. The source correctly does not subtract them.

The fresh Gaussian pairs can be generated independently of the entire actual/reference upper row sample, conditional on the lower sample. Their \(\xi_0\) marginal is the same \(N(0,T_0)\) law for every lower sample. Hence the resulting \(\Xi_0\) is independent jointly of the lower roots and all upper fields. This proves the claimed independence of the two reference populations:
\[
(H_i,X_{0,i})=(h(U_i),h(U_i)R_0+\Xi_{0,i})
\]
are independent copies and are independent of the independent upper reference rows \((Y_{0,i},Z_i,D_{0,i})\).

The local empirical-covariance coupling can be performed on this same space, rather than in a second incompatible coupling. On \(E_H=\operatorname{range}T_H\),
\[
T_H^{\dagger/2}\Xi_{H,i}
\]
is a standard Gaussian, independent of the realized upper sample conditional on the lower sample. Applying Lemma 1's covariance factor to it constructs \(\Xi_n\) with covariance \(T_n\), while leaving the pre-existing joint law of \((\Xi_H,\Xi_0)\) untouched. The sample reverse covariance is supported in \(E_H\) almost surely. Matrix completion from Section 3 then recovers the exact dense program on this same space.

Thus the corollary does not merely combine two separate Wasserstein bounds without checking whether their reference variables can coexist. Its displayed construction supplies the needed simultaneous coupling.

## 5. Population coefficient transfer and the stated constant

The source's assumption (29) supplies
\[
\|R_H-R_0\|_F^2\le L_1^2\delta_H^2,\qquad
\mathbb E[|\xi_H-\xi_0|^2\mid H]\le L_0^2\delta_H^2.
\]
A uniformly Lipschitz Jacobian of \(\Psi\) is indeed sufficient for the first estimate: take the expectation of the difference of the coupled Jacobians and apply Jensen. A uniform Lipschitz bound on \(\Psi\) gives the second estimate before the Gaussian transfer. Their constants are conditional and uniform as stated.

The mean and noise difference have zero expected cross term, and \(\|Q\|_{\rm op}\le B^2\). Therefore
\[
\mathbb E[\|HR_H+\Xi_H-(HR_0+\Xi_0)\|_{F,n}^2\mid H]
\le (B^2L_1^2+L_0^2)\delta_H^2.
\]
Combining this with the conditional theorem and the squared triangle inequality gives exactly
\[
C_{\rm block}
=2M^2(2k+\ell)+2(B^2L_1^2+L_0^2)B^2k.
\]
The factor two is correctly included here, unlike the orthogonal decomposition within the conditional theorem where it is unnecessary.

No positive eigenvalue enters this bound. However, a family-dependent response constant \(L_1\) could itself deteriorate unless (29) is established uniformly. The source explicitly assumes that uniformity and does not hide it in a claim that all smooth neural circuits satisfy it.

The off-support extension issue does not invalidate this conclusion. For a fixed singular \(Q\), changing a smooth extension while preserving its values on the Gaussian support changes \(R\) only by a matrix annihilated by \(Q\), and therefore by \(H\). The observable \(HR\) is invariant. The stronger unweighted difference \(R_H-R_0\) in (29) may depend on the selected circuit extension; the corollary fixes the actual row circuit and explicitly assumes this bound. It does not claim an extension-invariant bound for individual derivative coefficients.

## 6. Rank-zero cases and the unbounded weighted extension

If \(Q=0\), then \(H=Y=0\). There is no response mean or forward-projection loss; the covariance replacement remains exactly Lemma 1. If \(T=0\), then \(D=0\) almost surely. Stein gives \(QR=0\), hence \(HR=0\); both actual and reference returns vanish. These conclusions do not require passing through nearby positive definite covariances.

For the unbounded extension, \(T=\mathbb E[\Psi\Psi^\top\mid H]\) must first be a finite matrix, \(R\) must be well defined, and Stein's identity must apply. With
\[
K_H=\mathbb E[|Q^{\dagger/2}Y_*|^2|\Psi|^2\mid H],
\qquad
K_D=\mathbb E[|\Psi|^2\Psi^\top T^\dagger\Psi\mid H],
\]
finite, the regression variance is in fact
\[
\mathbb E[\|H(A_n-R)\|_{F,n}^2\mid H]
=\frac{K_H-\|Q^{1/2}R\|_F^2}{n}
\le K_H/n.
\]
The projected primitive term remains \(r_H\operatorname{tr}T/n\). The covariance-factor estimate is
\[
\mathbb E[\|\Xi_n-\Xi\|_{F,n}^2\mid H]
\le (K_D-\operatorname{tr}T)/n,
\]
with \(K_D-\operatorname{tr}T\ge0\) by the exact sample-covariance variance identity. Thus the source's equation (39),
\[
\mathbb E[\|X-\overline X\|_{F,n}^2\mid H]
\le\frac{K_H+r_H\operatorname{tr}T+K_D-\operatorname{tr}T}{n},
\]
is valid, including at zero ranks.

Under bounded \(\Psi\), \(K_H\le M^2r_H\), \(K_D\le M^2r_D\), and \(\operatorname{tr}T\le M^2\), recovering the stated simpler bound after discarding the negative trace term.

The unbounded statement is conditional, not uniform over arbitrary neural circuit families. Ordinary Gaussian moment bounds do not on their own bound every covariance-normalized direction in \(K_D\). The note expressly leaves that verification open. I found no illicit inference from a finite Gaussian envelope to a uniform weighted fourth-moment estimate, and no hidden clipping assumption.

## 7. Probability, observables, and limits of the result

The probability conclusion follows directly from Markov applied to the mean-square coupling error. It gives \(O_{\mathbb P}(n^{-1/2})\) at fixed failure probability. The note correctly declines to turn this into probability \(1-n^{-r}\) with only logarithmic losses.

For a finite list of pairings, the decomposition
\[
|\langle A,B\rangle_n-\langle A_0,B_0\rangle_n|
\le \|A-A_0\|_{2,n}\|B\|_{2,n}
 +\|A_0\|_{2,n}\|B-B_0\|_{2,n}
\]
and Cauchy–Schwarz give expected absolute error \(O(n^{-1/2})\) whenever the displayed second moments are controlled. Independent reference sampling then uses fourth moments to control a pairing's variance. The source accurately distinguishes these moment requirements from the field coupling bound and expressly requires uniform reference moments before claiming a uniform family result.

The scalar examples concerning the square-root covariance singularity are correct. A variance perturbation of size \(\varepsilon\) against a zero-variance law has Gaussian root-mean-square cost \(\sqrt\varepsilon\), and the bounded Lipschitz test \(\min(|x|,1)\) has expectation of that order. Neither argument conflicts with Lemma 1, which exploits the particular covariance-weighted structure of empirical sampling.

This proves one independent-forward/reciprocal-reverse block. It does not prove stability of a further forward query depending on \(X\), concentration of empirically fitted shared coefficients, a growing-history estimate, a mesh-uniform limit, or an all-time neural approximation. The source explicitly preserves these distinctions.

## 8. Actual corrections and recommended wording

The following edits preserve all theorem qualifications and constants.

**Required notation correction to introductory (1).** Replace its left side by
\[
\mathbb E\!\left[
\frac1n\|G^\top D-(HR+\Xi)\|_F^2\,\middle|\,H\right].
\]
Alternatively, if retaining an unconditional expectation on the left, use
\[
\frac{M^2}{n}\mathbb E[2\operatorname{rank}Q+\operatorname{rank}T]
\]
on the right. The formal theorem already uses the first convention correctly.

**Required completion wording at (19).** Replace “\(W\) is an independent matrix with entry variance \(1/n\)” by:

“\(W\) has independent \(N(0,1/n)\) entries and is independent of every variable already constructed.”

This fixes a genuine missing distributional specification in that proof sentence. Choosing such a fresh Gaussian matrix is allowed and completes the proof as intended.

**Useful clarification for the population construction.** State that its fresh Gaussian seeds are independent of the complete lower-root sample and the actual/reference upper data; their deterministic factors depend on the lower sample only through \(H\). This makes the claimed independence from all lower roots immediate, not merely independence from \(H\).

**Useful clarification at the start of Section 6.2.** Add “Assume \(T\) is finite, \(R\) is well defined, and the Stein identity holds,” before defining \(K_H,K_D\). Those prerequisites are already implicit in the formulas, but should be explicit when boundedness is removed.

With these local wording corrections, the note supplies a valid gap-free \(n^{-1/2}\)-scale coupling for its declared reciprocal block. It is a sound prerequisite for further work, not a completed global bridge.
