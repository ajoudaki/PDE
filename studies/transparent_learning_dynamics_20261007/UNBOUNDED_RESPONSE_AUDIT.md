# Audit of the unbounded gap-free reciprocal response block

2026-10-07. Complete frozen-input audit of UNBOUNDED_GAP_FREE_RESPONSE.md, 297 lines, SHA-256 bd9da092fb75b0b3d8ef4b2692e45db875770267b3e72343314088f84572327a.

Scientific inputs were the complete frozen note and the covariance-factor/Gaussian-conditioning arguments directly checked in this author's preceding bounded-block audit. No other verdict, integrated study, other study, literature, experiment, or Git history was consulted. No original source was edited.

## Verdict

The covariance coupling, Gaussian-tail calculation, preservation of exact dense-program marginals, population-end independence, and reciprocal-block bound all pass. The unbounded vector is not clipped in either the target circuit or its final response law. The proof genuinely avoids a uniform bound on the weighted leverage moment involving \(T^\dagger\).

The displayed constants are valid. A simple additive-tail realization gives the optional sharper covariance bound
\[
\mathbb E|\xi_n-\xi|^2
\le\frac{A^2}{n}\bigl[2+(1+R_n)^2r_D\bigr],
\qquad
R_n^2=8\log(8n)+4r\log2,
\]
and hence a sharper reciprocal-block right side
\[
\frac{A^2}{n}\left[
4r_H(r+2)+2+(1+R_n)^2r_D
\right].
\]
The original larger constants are not errors. Both forms have the same \(n^{-1/2}\sqrt{\log n}\) root-mean-square order for fixed dimensions and envelope constant.

One minor distributional wording clarification is advisable: explicitly specify that the entries of both initialized \(G\) and completion noise \(W\) are independent \(N(0,1/n)\). This is clearly the intended model and is used in the proof; merely specifying one-entry Gaussian marginals would not imply it.

## 1. The population tail bound is correct

Let \(g\sim N(0,I_r)\), \(r\ge1\), and suppose
\[
|v(g)|\le A(1+|g|).
\]
For \(s=|g|^2\),
\[
(1+\sqrt s)^2\le2(1+s),\qquad
\max_{s\ge0}(1+s)e^{-s/8}=8e^{-7/8}<4.
\]
On \(s>R_n^2\),
\[
2(1+s)
\le8e^{s/8}
\le8e^{-R_n^2/8}e^{s/4}.
\]
Therefore
\[
\tau_R:=\mathbb E[|v(g)|^2\mathbf1_{\{|g|>R_n\}}]
\le8A^2e^{-R_n^2/8}\mathbb E e^{|g|^2/4}.
\]
The Gaussian integral gives \(\mathbb E e^{|g|^2/4}=2^{r/2}\). With the stated radius,
\[
e^{-R_n^2/8}
=(8n)^{-1}2^{-r/2},
\qquad
\tau_R\le A^2/n.
\]
Every factor in the source's equation (3) is correct. In particular, this controls the population truncation error whether or not any realized sample falls outside the ball. No sample-maximum event is substituted for a population bias estimate.

The linear envelope also implies \(T=\mathbb E[vv^\top]\) is finite. No derivative regularity is needed for this covariance argument.

## 2. Singular support and the three Gaussian pairings

Put
\[
v_R=v\,\mathbf1_{\{|g|\le R_n\}},\qquad
T_R=\mathbb E[v_Rv_R^\top],\qquad
T_{n,R_n}=\frac1n\sum_i v_{R_n,i}v_{R_n,i}^\top.
\]
The truncated vector is bounded by \(A(1+R_n)\). If \(u\in\ker T\), then \(u^\top v=0\) almost surely, so \(u^\top v_R=0\) almost surely. Consequently
\[
\operatorname{range}T_R\subseteq\operatorname{range}T,
\qquad \operatorname{rank}T_R\le r_D:=\operatorname{rank}T.
\]
The bounded covariance-factor lemma is therefore applicable and yields
\[
\mathbb E|\xi_{n,R_n}-\xi_R|^2
\le A^2(1+R_n)^2\operatorname{rank}T_R/n.
\]
Its fresh Gaussian seed can be chosen independently of the complete root sample \((g_1,\ldots,g_n)\). Since the population covariance factor \(T_R^{1/2}\) is deterministic, \(\xi_R\) is independent of that complete sample. Independence from the truncated vectors alone would be insufficient for the desired statement; the source explicitly supplies the stronger construction.

The empirical block second-moment matrix of \((v_i,v_{R_n,i})\) is positive semidefinite and has the already prescribed \(T_{n,R_n}\) marginal. Thus a conditional Gaussian extension of an existing \(\xi_{n,R_n}\) exists. Likewise the population block second-moment matrix gives an extension of the existing \(\xi_R\). Gaussian regression on each support, with independent residual Gaussian noise, works at singular covariances as stated.

There is no incompatible-couplings problem: start with the actual coupled pair \((\xi_{n,R_n},\xi_R)\), then extend each of its two members using independent fresh seeds. This preserves both members and their initial joint coupling. The empirical extension has exactly the conditional law \(N(0,T_n)\). The population extension uses deterministic coefficients and fresh randomness, so its full-sample independence is preserved.

The costs of the two extensions are exactly \(\tau_R\), because the Gaussian pairings reproduce the full uncentered second moments of the corresponding vector differences. Combining the three pairs with Minkowski gives exactly the source bound
\[
\mathbb E|\xi_n-\xi|^2
\le \left[
2\sqrt{\tau_R}
+A(1+R_n)\sqrt{r_D/n}
\right]^2.
\]
Substitution of \(\tau_R\le A^2/n\) proves its equation (2). There is no hidden reciprocal eigenvalue.

The source correctly does not require the full four-vector to be jointly Gaussian unconditionally. Conditional on the sample the proposed constructions may, in fact, all be chosen linear Gaussian; the conditional end marginals are the important property.

## 3. A simpler exact realization and optional sharper constant

Because the truncation is an indicator, the preceding Gaussian extension can be made particularly explicit. Define the positive-semidefinite tail covariances
\[
T_{n,\mathrm{tail}}=T_n-T_{n,R_n}
=\frac1n\sum_i v_iv_i^\top\mathbf1_{\{|g_i|>R_n\}},
\qquad
T_{\mathrm{tail}}=T-T_R.
\]
The identities hold without cross terms: the retained and discarded vector parts have disjoint support as functions of \(g\).

After constructing \((\xi_{n,R_n},\xi_R)\), take fresh independent standard Gaussian vectors \(a,b\), independent of that construction and of the full root sample, and set
\[
\eta_n=T_{n,\mathrm{tail}}^{1/2}a,\qquad
\eta=T_{\mathrm{tail}}^{1/2}b,\qquad
\xi_n=\xi_{n,R_n}+\eta_n,\qquad
\xi=\xi_R+\eta.
\]
Then, conditional on the full sample,
\[
\operatorname{Cov}(\xi_n)=T_{n,R_n}+T_{n,\mathrm{tail}}=T_n.
\]
The population end has covariance \(T_R+T_{\mathrm{tail}}=T\), and is independent of the sample because both of its terms are constructed from sample-independent seeds with deterministic factors.

All cross terms in
\[
\xi_n-\xi=(\xi_{n,R_n}-\xi_R)+\eta_n-\eta
\]
have zero expectation. Indeed, condition first on the sample and the truncated-pair seed; the two new noises are independent and centered. Therefore
\[
\begin{aligned}
\mathbb E|\xi_n-\xi|^2
&=\mathbb E|\xi_{n,R_n}-\xi_R|^2
 +\mathbb E|\eta_n|^2+\mathbb E|\eta|^2\\
&=\mathbb E|\xi_{n,R_n}-\xi_R|^2+2\tau_R\\
&\le\frac{A^2}{n}\left[
(1+R_n)^2\operatorname{rank}T_R+2
\right].
\end{aligned}
\]
This proves the optional sharpening stated in the verdict. It does not alter any target field or require a new assumption. It also avoids Gaussian regression inverses altogether in the tail-extension construction, although their occurrence in the source proof was not a defect.

To generate many rows, use independent triples of fresh seeds for each row. The empirical end rows are independent conditional on the shared root sample. The population end rows are independent of the entire sample and of each other. Their unconditional independence is not spoiled by the empirical end's shared covariance.

## 4. Whitened Gaussian moments and the reciprocal-block constant

Here \(R\) denotes the response matrix \(R_{aj}=\mathbb E[\partial_{Y_a}\Psi_j(Y,Z)\mid H]\); the truncation radius is \(R_n\). Condition on \(H\), put \(Q=H^\top H/n\), and choose a minimal factorization
\[
Q=LL^\top,\qquad L\in\mathbb R^{k\times r_H},\qquad
r_H=\operatorname{rank}Q.
\]
For \(Y=Lg^{(1)}\), one has
\[
L^\top Q^\dagger L=I_{r_H},
\qquad |Q^{\dagger/2}Y|^2=|g^{(1)}|^2.
\]
This follows from an orthonormal singular-vector factorization of \(L\). It is an exact identity, not a bound using the smallest positive eigenvalue of \(Q\).

Append the independent Gaussian roots for the auxiliary fields, giving a standard Gaussian \(g\in\mathbb R^r\). Under the supplied actual-circuit envelope
\[
|\Psi(Lg^{(1)},Z(g^{(2)}))|\le A(1+|g|),
\]
the weighted regression moment is bounded by
\[
\begin{aligned}
\mathbb E[|Q^{\dagger/2}Y|^2|\Psi|^2]
&\le2A^2\mathbb E[|g^{(1)}|^2(1+|g|^2)]\\
&=2A^2r_H(r+3).
\end{aligned}
\]
The Gaussian moment identity used here is
\[
\mathbb E[|g^{(1)}|^2|g|^2]
=r_H(r_H+2)+r_H(r-r_H)=r_H(r+2).
\]
Also
\[
\operatorname{tr}T=\mathbb E|\Psi|^2
\le2A^2(1+r).
\]
Thus the regression error bound and the population projection loss sum to
\[
\frac{2A^2r_H(r+3)+2A^2r_H(r+1)}n
=\frac{4A^2r_H(r+2)}n,
\]
exactly as claimed. No factor of two or root dimension is missing.

The singular Stein identity \(\mathbb E[Y\Psi^\top]=QR\) applies to the original smooth circuit, not to its truncated intermediary. The source's integration-by-parts hypotheses are sufficient; a \(C^1\) circuit whose derivatives have polynomial growth in the full Gaussian roots is an explicit sufficient case.

## 5. Exact target completion and population-end independence

The actual posterior return is
\[
G^\top D
=H Q^\dagger Y^\top D/n+(I-P_H)\Xi_n.
\]
The covariance coupling in Sections 1–3 supplies rows of \(\Xi_n\) with exactly the conditional covariance \(D^\top D/n\), and population end rows of \(\Xi\) independent of the entire upper Gaussian root sample conditional on \(H\).

Conditioning on the complete Gaussian root sample does not introduce an unobserved constraint on \(G\). In the minimal factorization, \(g^{(1)}=L^\dagger Y\) is determined by \((H,Y)\). The other root coordinates are initially independent of \(G\). Thus the usual posterior conditioned on \(H,Y\) remains valid after this additional conditioning.

Even if some auxiliary roots are not recoverable from their displayed fields \(Z\), the constructed \(\Xi_n\) has conditional product-Gaussian law with covariance \(D^\top D/n\), which is a function of \((H,Y,Z)\). Integrating over those hidden auxiliary roots leaves the same product-Gaussian conditional law. The stronger population-end independence is retained.

For the error decomposition
\[
H(Q^\dagger Y^\top D/n-R)
-P_H\Xi+(I-P_H)(\Xi_n-\Xi),
\]
the last term is spatially orthogonal to the first two. The expected cross term between the first two is zero because the population \(\Xi\) is centered and independent of the full upper sample conditional on \(H\). Consequently the covariance coupling cost is added to the regression and projection costs without a triangle-inequality factor.

The source's bound (8) therefore follows exactly. Substituting the optional cost from Section 3 instead gives the sharper constant in this audit's verdict.

To recover the full matrix as well as its return, choose a fresh matrix \(W\) with independent \(N(0,1/n)\) entries, independent of all previously generated variables, and set
\[
\widetilde G^\top=\Xi_nD^\dagger+W^\top(I-P_D),\qquad
G=YH^\dagger+\widetilde G(I-P_H).
\]
Conditional on the upper sample, the two terms in \(\widetilde G^\top\) are independent Gaussian row projections with covariances \(P_D/n\) and \((I-P_D)/n\). Different rows are independent. The result is the exact posterior Gaussian matrix, satisfies both specified matrix actions, and has the original dense-program marginal after averaging over the upper sample.

The constructed target matrix may be correlated with the reference primitive \(\Xi\). This is allowed: the required reference independence is from upper fields and roots conditional on \(H\), not from the whole target matrix. The note explicitly distinguishes these two notions.

## 6. Degenerate cases and scope

If the full Gaussian root dimension is zero, \(v\) is deterministic and \(T_n=T\); the covariance coupling can have zero error. If \(T=0\), then \(v=0\) almost surely and both covariance endpoints vanish. Singular nonzero \(T_R,T_{n,R}\), including a rank-zero truncated covariance, are handled directly by positive-semidefinite square roots and independent tail noise.

If \(Q=0\), the forward-query matrix \(H\) is zero and the regression/projection contribution vanishes; the covariance coupling still treats any randomness in the auxiliary roots. If \(T=0\), Stein implies \(HR=0\), so the actual and reference returns vanish even if a formal off-support derivative coefficient is nonzero.

The source proves a conditional one-reciprocal-block estimate. For fixed \(A,r,r_H,r_D\), it is a normalized RMS \(O(n^{-1/2}\sqrt{\log n})\) coupling bound. Its Markov fixed-confidence statement is correct. It does not give polynomially small failure probability with only logarithmic losses.

The actual upper query is always the original \(D_i=\Psi(Y_i,Z_i)\), and the final response coefficient and covariance are always the original \(R\) and \(T\). No derivative of the discontinuously truncated auxiliary circuit is taken. No modified training trajectory is substituted for the target. This is therefore proof truncation, not clipping the neural model.

The supplied linear Gaussian envelope and fixed Gaussian root dimension remain genuine hypotheses. Their uniform verification for an evolving or growing neural history is not established by this block. Nor does the proof treat a second adaptive direction switch, empirically fitted shared coefficients, a deterministic-population transfer for all lower covariances, mesh-uniform convergence, or all physical times. The note explicitly acknowledges these restrictions and adds no label cap.

## 7. Corrections and optional refinement

No substantive mathematical correction is required.

For self-contained distributional precision, use:

- At the start of Section 2: “\(G\) has independent \(N(0,1/n)\) entries.”
- In matrix completion: “\(W\) has independent \(N(0,1/n)\) entries and is independent of every variable already constructed.”

This spells out the iid structure already intended and used by the Gaussian conditioning argument.

Optionally replace the two regression-based tail extensions by the independent additive-tail construction in Section 3. It makes singular support and full-root independence transparent and permits replacing
\[
[2+(1+R_n)\sqrt{r_D}]^2
\quad\hbox{by}\quad
2+(1+R_n)^2r_D
\]
throughout the covariance and reciprocal-block bounds. Retaining the original conservative constant is fully valid.

The audited result successfully removes the bounded-query and weighted-\(T^\dagger\)-moment impediments for its stated one-block program. It is not, by itself, the candidate's global quantitative bridge.
