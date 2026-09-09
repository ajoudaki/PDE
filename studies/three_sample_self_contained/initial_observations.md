## V.I. A derivative-valid observational extension at initialization

Fix any deterministic three coefficients \(p_j\), and write
\[
 H_0=\sum_{j=1}^3p_j\phi(Z_j^3),\qquad d_j^\ell=\phi'(Z_j^\ell),
 \qquad \beta_i^3=H_0d_i^3.
\]
Here \(Z^2,Z^3\) are the initialized forward Gaussian tuples, and \(h_i^\ell=\phi(Z_i^\ell)\). Their covariances may be singular. All named source coordinates remain distinct formal arguments, with all scalar coefficients and covariances frozen in source derivatives.

The fixed-program lemma of Part F extends to the finite appended chain
\[
 \beta_i^3,\quad q_i^2=B_0^*\beta_i^3,\quad
 \beta_i^2=d_i^2q_i^2,\quad q_i^1=A_0^*\beta_i^2,\quad
 \beta_i^1=d_i^1q_i^1.
\]
The extension has joint empirical \(\mathcal W_2\) convergence and the following exact source formulas:
\[
 q_i^2=\zeta_i^2+\sum_jD^3_{ij}h_j^2,\qquad
 D^3_{ij}=E[p_jd_j^3d_i^3+\mathbf1_{\{i=j\}}H_0\phi''(Z_i^3)],
                                                        \tag{V.I.1}
\]
\[
 q_i^1=\zeta_i^1+\sum_jD^2_{ij}h_j^1,\qquad
 D^2_{ij}=E[\mathbf1_{\{i=j\}}\phi''(Z_i^2)q_i^2
                         +d_i^2D^3_{ij}d_j^2].           \tag{V.I.2}
\]
The reverse source covariances are the full input Grams:
\[
 E[\zeta_i^2\zeta_j^2]=E[\beta_i^3\beta_j^3],\qquad
 E[\zeta_i^1\zeta_j^1]=E[\beta_i^2\beta_j^2].               \tag{V.I.3}
\]
Each reverse source family is independent of the forward source families and the first-layer roots in the source construction. This does not assert independence of \(q_i^\ell\) from its same-layer features: the return terms in (V.I.1)--(V.I.2) remain.

**Proof.** The map \(\beta_i^3=H_0d_i^3\) has an unbounded derivative, so first set \(\beta_{i,M}^3=\tau_M(H_0)d_i^3\). At fixed \(M\), this is a \(C^1\) bounded-derivative function of the top preactivation tuple. The Part F lemma gives its transpose query, with coefficients
\[
 D^{3,M}_{ij}
 =E[\tau_M'(H_0)p_jd_j^3d_i^3+
          \mathbf1_{\{i=j\}}\tau_M(H_0)\phi''(Z_i^3)].
\]
Since \(\phi'\) and \(\phi''\) are bounded, these integrands are bounded in absolute value by \(K(1+|H_0|)\), independently of \(M\), and \(H_0\in L^p\) for every finite \(p\). Dominated convergence gives \(D^{3,M}\to D^3\). Also \(\beta^3_M\to\beta^3\) in \(L^2\); hence their Gram matrices converge. Realize all reverse Gaussian tuples through the positive-semidefinite square roots of these finite Gram matrices on one fresh Gaussian root. Square-root continuity, which does not require invertible covariances, gives \(\zeta^{2,M}\to\zeta^2\) in \(L^2\), jointly with the independent forward tuple. The formulas
\[
 q_i^{2,M}=\zeta_i^{2,M}+\sum_jD^{3,M}_{ij}h_j^2
\]
therefore converge in \(L^2\) to (V.I.1), jointly with all primary observations. Along a coupled almost-sure subsequence they converge pointwise as well. Their formal first derivatives in the named layer-2 forward sources are
\[
 \partial_{\xi_j^2}q_i^{2,M}=D^{3,M}_{ij}d_j^2;
\]
they converge pointwise and are bounded independently of \(M\).

For the second gate set \(\beta_{i,M,N}^2=d_i^2\tau_N(q_i^{2,M})\). At fixed \(M,N\), the original bounded-derivative theorem applies to the whole finite chain. Its expected forward-source derivative is
\[
 E\!\left[
 \mathbf1_{\{i=j\}}\phi''(Z_i^2)\tau_N(q_i^{2,M})
       +d_i^2\tau_N'(q_i^{2,M})D^{3,M}_{ij}d_j^2
 \right].                                                   \tag{V.I.4}
\]
First keep \(N\) fixed and send \(M\to\infty\). The integrand is bounded by a constant depending on \(N\), and is continuous in \(q_i^{2,M},D^{3,M}_{ij}\). Thus (V.I.4) converges to the same expression with \(q^2,D^3\). Now send \(N\to\infty\): the integrand is bounded by \(K(1+|q_i^2|)\), which is integrable because (V.I.1) is a finite sum of Gaussian variables and linear-growth Gaussian functions. Its limit is \(D^2_{ij}\) in (V.I.2). The same ordered limits give \(\beta^2_{M,N}\to\beta^2\) in \(L^2\); source Gram convergence and square-root coupling then give (V.I.2)--(V.I.3). The last gate follows by the same \(L^2\) product argument below; if its expected derivatives are needed, the identical additional truncation has an integrable Gaussian-linear envelope.

For completeness, the empirical passage from truncated to actual gates uses only empirical second moments and bounded operator norms. If \((z_n,q_n)\) converges in joint \(\mathcal W_2\), use a coupling with \(L^2\) convergence and write
\[
 \|\phi'(z_n)q_n-\phi'(z)q\|_2
 \le \|\phi'\|_\infty\|q_n-q\|_2
       +\|[\phi'(z_n)-\phi'(z)]q\|_2.
\]
For the second term, truncate the fixed \(q\) at level \(L\). Its bounded part is at most \(\|\phi''\|_\infty L\|z_n-z\|_2\), and its tail part is at most \(2\|\phi'\|_\infty\|q\mathbf1_{\{|q|>L\}}\|_2\). Let \(n\to\infty\), then \(L\to\infty\). Also \(|q|\mathbf1_{\{|q|>L\}}\le2(|q|-L/2)_+\), and positive-part tail norms converge under \(\mathcal W_2\). Thus the finite truncation discrepancies vanish in the width-limit \(L^2\) sense. The high-probability uniform norm bounds for \(A_0,B_0\) transfer every such input discrepancy to its actual transpose answer. Their population actions are bounded on the common generated \(L^2\) spaces, so the population discrepancy vanishes as well. A triangle inequality proves the joint empirical law of the complete untruncated chain.

The limits are fixed transcript and fixed \(M,N\), then width, then \(M\to\infty\) at fixed \(N\), then \(N\to\infty\). No inverse covariance, arbitrary \(L^p\) operator theorem, or unproved derivative-limit interchange is used.
