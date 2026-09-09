# Euler accumulation of the Panahi perturbation

This refines the previous source-scope note: growth of the raw
\(\|\Gamma\|\) is not by itself an obstruction after contraction with
a simple query history. No canonical transfer is proved.

Use [Panahi v1, PDF equations (6), (9)](https://arxiv.org/pdf/2603.09310v1),
with one mixture component, \(R=I,J=1,z=0\).

**Exact frozen-history lemma.** Let \(n,m,K\) be positive integers,
\(\eta,\sigma>0\), and \(T=K\eta\). Fix deterministic columns
\(\theta_l\in\mathbb R^n,\omega_l\in\mathbb R^m\) for
\(1\le l\le K\), and let \(\Gamma\in\mathbb R^{K\times K}\)
have independent standard real Gaussian entries. Put
\(\Theta=[\theta_1,\ldots,\theta_K]\),
\(\Omega=[\omega_1,\ldots,\omega_K]\), and take upper Cholesky
factors with positive diagonal:
\[
A_\theta^TA_\theta=\Theta^T\Theta+\sigma^2I,\qquad
A_\omega^TA_\omega=\Omega^T\Omega/m+\sigma^2I.
\]
Set \(t_i=(\Theta A_\theta^{-1})_i\) and
\(s_i=(\Omega A_\omega^{-1})_i/\sqrt m\), for column index \(i\).
The two covariance-matching terms in (9) are exactly
\[
g_l=\frac1{\sqrt m}\sum_{i\le l}t_i(\Gamma A_\omega)_{il},\qquad
k_l=\frac1{\sqrt m}\sum_{i<l}s_i(\Gamma^TA_\theta)_{il},
\]
where \(k_l\) is the perturbation of \(p_l/\sqrt m\).

Then the following identities and estimates hold. They evaluate the added
forcing, not the difference between two adaptive solutions.
\[
\mathbb E\left\|\eta\sum_{l=1}^K g_l\right\|^2
=\frac{\eta^2}{m}\sum_{i=1}^K\|t_i\|^2
\left[\frac1m\left\|\sum_{l=i}^K\omega_l\right\|^2
+\sigma^2(K-i+1)\right],                                      \tag{A}
\]
\[
\mathbb E\left\|\eta\sum_{l=1}^K k_l\right\|^2
=\frac{\eta^2}{m}\sum_{i=1}^{K-1}\|s_i\|^2
\left[\left\|\sum_{l=i+1}^K\theta_l\right\|^2
+\sigma^2(K-i)\right].                                       \tag{B}
\]
**Proof of the identities.** Group each independent \(\Gamma_{ij}\) in (A):
its coefficient is \(\eta t_i\sum_{l\ge i}(A_\omega)_{jl}/\sqrt m\).
Summing over \(j\) produces the suffix quadratic form of
\(A_\omega^TA_\omega\). For (B), the coefficient of
\(\Gamma_{ji}\) is
\(\eta s_i\sum_{l>i}(A_\theta)_{jl}/\sqrt m\), giving the
strict suffix and (B). Cross terms between distinct Gaussian entries
have zero expectation. The strict inequality in (B) is essential.

For repeated queries \(\theta_l=\theta,\omega_l=\omega\), put
\(a=\|\theta\|>0,b=\|\omega\|/\sqrt m>0\). The regularized upper
Cholesky factor of \(a^2\mathbf1\mathbf1^T+\sigma^2I\) satisfies
\[
(A_a)_{ii}=\sigma\sqrt{\frac{\sigma^2+ia^2}{\sigma^2+(i-1)a^2}},
\quad
(A_a)_{ij}=\frac{a^2\sigma}
 {\sqrt{(\sigma^2+(i-1)a^2)(\sigma^2+ia^2)}}\quad(i<j).
\]
Consequently \(t_i=\theta d_i(a)\), where
\[
d_i(a)=\frac{\sigma}
 {\sqrt{(\sigma^2+(i-1)a^2)(\sigma^2+ia^2)}},\qquad
\sum_{i=1}^l d_i(a)^2=\frac{l}{\sigma^2+la^2}.
\]
Substitution gives
\[
\mathbb E\left\|\eta\sum_lg_l\right\|^2
=\frac{a^2\eta^2}{m}\sum_{i=1}^Kd_i(a)^2
 [b^2(K-i+1)^2+\sigma^2(K-i+1)]
\le\frac{b^2T^2+\sigma^2T\eta}{m}.                            \tag{C}
\]
The analogous bound for \(\eta\sum_lk_l\) is
\((a^2T^2+\sigma^2T\eta)/m\), using \(i<K\) and \(K-i\).
In the fixed-\(K\), \(\sigma\downarrow0\) limit,
\(g_l\to(\theta/a)(b/\sqrt m)\Gamma_{11}\) for every \(l\),
whereas \(k_1=0\) and
\(k_l\to(\omega/(b\sqrt m))(a/\sqrt m)\Gamma_{11}\) for \(l\ge2\).
The forcing is coherent in time: Euler integration yields \(T/\sqrt m\),
not a \(\sqrt K\) growth. Inequality (C) is already uniform in both
\(K\) and \(\sigma\), so this conclusion does not exchange limits.

More generally, with \(\|\omega_l\|/\sqrt m\le B\), (A) is bounded by
\[
\frac{T^2B^2+\sigma^2T\eta}{m}\,
r_{\rm eff}(\Theta,\sigma),\qquad
r_{\rm eff}=\operatorname{tr}\!\left[
\Theta^T\Theta(\Theta^T\Theta+\sigma^2I)^{-1}\right].           \tag{D}
\]
A deterministic finite-rank path has bounded effective rank, including
an affine slowly changing history. This follows because
\(\sum_i\|t_i\|^2=r_{\rm eff}\), by cyclicity of the trace and
\(A_\theta^{-1}A_\theta^{-T}=(\Theta^T\Theta+\sigma^2I)^{-1}\).
The reverse orientation has the analogous estimate with
\(r_{\rm eff}(\Omega/\sqrt m,\sigma)\) and
\(A=\max_l\|\theta_l\|\).

These estimates also give convergence in the supremum norm of the
integrated path, not merely convergence at its last time. Specifically,
\[
\mathbb E\max_{1\le j\le K}
 \left\|\eta\sum_{l=1}^j g_l\right\|^2
\le \frac{T^2(B^2+\sigma^2)}m\,r_{\rm eff}(\Theta,\sigma),      \tag{E}
\]
and the reverse orientation has bound
\(T^2(A^2+\sigma^2)r_{\rm eff}(\Omega/\sqrt m,\sigma)/m\).
Indeed, pathwise Cauchy–Schwarz bounds the maximum by
\(T\eta\sum_l\|g_l\|^2\), while Gaussian isometry gives
\(\mathbb E\|g_l\|^2=(\|\omega_l\|^2/m+\sigma^2)
 \sum_{i\le l}\|t_i\|^2/m\).

The unintegrated frozen queries also admit a uniform maximum bound:
\[
\mathbb E\max_{1\le l\le K}\|g_l\|^2
\le\frac{4(B^2+\sigma^2)}m\,
 r_{\rm eff}(\Theta,\sigma)\log(2K),                           \tag{F}
\]
with the analogous reverse-orientation estimate. To verify this without
any independence between times, let \(Z_l\) be centered Gaussian
vectors with \(\mathbb E\|Z_l\|^2\le v^2\). For \(v>0\), the
covariance eigenvalues \(\lambda_j\) are at most \(v^2\), and
\[
\log\mathbb E e^{\|Z_l\|^2/(4v^2)}
=-\tfrac12\sum_j\log(1-\lambda_j/(2v^2))\le\tfrac12.
\]
Here \(-\log(1-x)\le2x\) for \(0\le x\le1/2\) was used.
Jensen's inequality and \(\max_l e^{x_l}\le\sum_l e^{x_l}\)
give \(\mathbb E\max_l\|Z_l\|^2\le4v^2\log(2K)\).
The case \(v=0\) is immediate. Apply this with
\(v^2=(B^2+\sigma^2)r_{\rm eff}/m\), using the per-query identity
above. Thus (F) also includes arbitrarily correlated frozen query times.

**Slow-history bound, including integer choices.** Assume only the discrete
Lipschitz estimate
\(\|\theta_l-\theta_j\|\le M\eta|l-j|\). Then
\[
r_{\rm eff}\le r+\frac{KM^2T^2}{\sigma^2r^2}\quad(1\le r\le K).
\]
To prove this, partition the indices into the nonempty blocks
\(\lfloor(j-1)K/r\rfloor<l\le\lfloor jK/r\rfloor\),
\(1\le j\le r\), replacing each column by the first column of its
block. Each block spans at most \(\eta(\lceil K/r\rceil-1)\le T/r\)
in physical time. This rank-at-most-\(r\) matrix approximation therefore
has squared Frobenius error at most \(K(MT/r)^2\). The sum of squared
singular values after the first \(r\) is no larger than that error;
the first \(r\) terms of the effective rank are at most one each, and
the rest are at most their squared singular values divided by
\(\sigma^2\). This proves the estimate.

Set \(x=(KM^2T^2/\sigma^2)^{1/3}\) and choose
\(r=\min\{K,\max\{1,\lceil x\rceil\}\}\). If \(x\le K\),
the estimate is at most \(1+2x\); if \(x>K\), use
\(r_{\rm eff}\le K\) directly. Thus
\[
r_{\rm eff}\le\min\{K,1+2(KM^2T^2/\sigma^2)^{1/3}\}.
\]
For \(K=O(m^2)\), uniformly bounded \(M,T\), and
\(\sigma\gg m^{-1/2}\), this proves \(r_{\rm eff}/m\to0\).
Choosing additionally \(\sigma\to0\), for example
\(\sigma=m^{-\beta}\), \(0<\beta<1/2\), removes the added
regularization forcing below. The reverse orientation needs the same
Lipschitz control of \(\omega_l/\sqrt m\).

The additive \(\sigma U/\sqrt m\), \(\sigma V\) terms in (9) have
Euler-integrated mean-square norms \(\sigma^2(n/m)T\eta\) and
\(\sigma^2T\eta\), respectively, in the same two normalized spaces.
For independent standard Gaussian \(U,V\), their partial sums are
square-integrable vector martingales; the expected squared maximum is at
most four times these quantities by the \(L^2\) maximal inequality.
The same Gaussian maximum argument bounds the expected squared maximum
of their unintegrated query values by
\(4\sigma^2(n/m)\log(2K)\) and \(4\sigma^2\log(2K)\).

Thus, for deterministic histories with uniformly bounded
\(A,B,T,n/m\) and both discrete Lipschitz constants,
\(K\asymp m^2\), and \(\sigma=m^{-1/4}\), each expected squared
supremum of the integrated covariance perturbation is \(O(m^{-1/6})\).
Each additive-noise bound is \(O(m^{-5/2})\). Both orientations of the
full frozen primitive consequently vanish in \(L^2\) of the supremum
norm. This is a consequence of (E), without a union bound or logarithmic
loss; it is not a statement about the unfrozen dynamics.
Furthermore, (F) gives expected squared raw-query maxima
\(O(m^{-1/6}\log m)\), and the additive terms contribute
\(O(m^{-1/2}\log m)\). Hence the unintegrated frozen perturbations
also vanish uniformly over the mesh.

The implication is scoped. Simple deterministic histories resolve the
raw Gaussian-matrix-size concern, even with \(K\asymp m^2\).
However, in the actual comparison dynamics the Cholesky factors and
queries depend on \(\Gamma\); conditioning on those histories does not
preserve the independent Gaussian law used in (A)–(B) or (F). The actual
preactivation/backprop perturbations enter nonlinear queries before their
effect reaches an Euler update. An actual causal covariance estimate and
propagation bound are still required. The canonical middle multiplier
\(\operatorname{diag}(\phi''(z)b)\) is one unresolved propagation term;
this calculation does not show it is the only remaining obligation.
Claim 1 is unused. No experiments were performed.

## Which actual network histories satisfy the temporal premise?

This section concerns the canonical finite three-hidden-layer flow in
feature time \(s\), not an extra claim about the perturbed comparison
process. All hidden vectors and the rescaled readout \(W^{(4)}\) have
length \(n\), and \(W^{(2)},W^{(3)}\) are \(n\) by \(n\). Write
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),
\]
\[
q^{(2)}=(W^{(3)})^\top\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},\qquad
\phi(z)=\arctan z.
\]
Here \(q^{(2)}\) names the repeatedly used ungated backward result.
One can instead use common \(C^1\) clipping
\(\delta^{(2)}=\phi'(z^{(2)})\odot\tau_R(q^{(2)})\), with
\(|\tau_R(a)|\le |a|\), \(|\tau_R(a)|\le2R\), and
\(|\tau_R'(a)|\le1\).
The feature-time equations, with or without this clipping, are
\[
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^\top\delta^{(2)},\quad
(W^{(2)})'=\frac{\delta^{(2)}(h^{(1)})^\top}{n},\quad
(W^{(3)})'=\frac{\delta^{(3)}(h^{(2)})^\top}{n},\quad
(W^{(4)})'=h^{(3)}.
\]
Assume on \(0\le s\le S\) that the two matrix operator norms and
\(\|W^{(4)}\|_\infty\) are at most \(B_S\), independently of \(n,R\).
These are the already available primal bounds; the following implication
can also be read simply as a deterministic statement on that event.
Throughout this section \(C_S\) depends only on \(S,B_S\) and arctangent.

Because \(h^{(\ell)},\phi'\), and \(\phi''\) are bounded,
\(\|\delta^{(3)}\|_2/\sqrt n\), \(\|q^{(2)}\|_2/\sqrt n\), and
\(\|\delta^{(2)}\|_2/\sqrt n\) are bounded by \(C_S\).
Differentiating the actual forward equations gives
\[
(h^{(1)})'=\phi'(z^{(1)})^2\odot(W^{(2)})^\top\delta^{(2)},
\]
\[
(z^{(2)})'
=\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
 +W^{(2)}\!\left[
   \phi'(z^{(1)})^2\odot(W^{(2)})^\top\delta^{(2)}
 \right],
\]
\[
(h^{(2)})'=\phi'(z^{(2)})\odot(z^{(2)})',\qquad
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
 +W^{(3)}(h^{(2)})',
\]
\[
(\delta^{(3)})'
=h^{(3)}\odot\phi'(z^{(3)})
 +W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'.
\]
Every derivative displayed has Euclidean norm divided by \(\sqrt n\)
at most \(C_S\). Therefore \(h^{(1)}/\sqrt n\),
\(h^{(2)}/\sqrt n\), and \(\delta^{(3)}/\sqrt n\) have the
uniform time-Lipschitz property used in the frozen-history lemma.

This also yields an exact distinction for the lower backward query:
\[
(q^{(2)})'
=h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
 +(W^{(3)})^\top(\delta^{(3)})',
\]
so \(\|(q^{(2)})'\|_2/\sqrt n\le C_S\). In the uncut flow,
\[
(\delta^{(2)})'
=\phi''(z^{(2)})\odot(z^{(2)})'\odot q^{(2)}
 +\phi'(z^{(2)})\odot(q^{(2)})'.
\]
Cauchy--Schwarz gives
\[
\frac1n\sum_i|(\delta_i^{(2)})'|
\le \|\phi''\|_\infty
 \frac{\|(z^{(2)})'\|_2\|q^{(2)}\|_2}{n}
 +\frac{\|(q^{(2)})'\|_2}{\sqrt n}\le C_S.
\]
It does not supply a uniform Euclidean derivative bound for the product
\((z^{(2)})'\odot q^{(2)}\). For the clipped flow the same product
contains \(\tau_R(q^{(2)})\), and direct differentiation instead gives
\(\|(\delta^{(2)})'\|_2/\sqrt n\le C_S(1+R)\).
Thus all required lower-matrix frozen histories are time-Lipschitz for
fixed \(R\), but this argument is not uniform as \(R\) grows.

The scaling into the comparison lemma is explicit. For the top matrix
use \(m=n\), \(G=\sqrt n\,W_0^{(3)}\),
\(\theta_l=\delta_l^{(3)}/\sqrt n\), and \(\omega_l=h_l^{(2)}\).
Then its initial-matrix responses are
\[
G\omega_l/n=W_0^{(3)}h_l^{(2)}/\sqrt n,\qquad
G^\top\theta_l=(W_0^{(3)})^\top\delta_l^{(3)}.
\]
The lower matrix uses \(G=\sqrt n\,W_0^{(2)}\),
\(\theta_l=\delta_l^{(2)}/\sqrt n\), and \(\omega_l=h_l^{(1)}\).
The trained-matrix corrections remain present in the histories; they
are not being identified with these initialization-only responses.

Freeze an unperturbed flow path and sample the auxiliary \(\Gamma,U,V\)
independently of its initialization. Conditional on that path, the
frozen-history lemma applies. The top-matrix temporal constants just
proved are uniform in \(R\), while the lower-matrix backward constant
above is not. On any fixed primal-bounded event the resulting conditional
estimates have uniform constants. This is a forcing estimate along the
frozen path, not along the solution after adding that forcing.
Nothing here permits conditioning on a \(\Gamma\)-dependent perturbed
trajectory, removing clipping, or concluding unique autonomous restart.
