# A causal slow history invalidating the frozen Gaussian isometry

This is an exact test of one proof step. It is not a counterexample to a
vanishing perturbation bound, Panahi's theorem, or the canonical network
limit. The previously audited frozen-history lemma is unchanged.

Use [Panahi v1, PDF (2)–(3), (6), (9)](https://arxiv.org/pdf/2603.09310v1)
for the perturbed-original process, with one centered mixture component,
\(R=I,J=1,z=0\), and \(n=m\ge1\). Thus \(X\) has independent
standard Gaussian entries. All auxiliary Gaussian arrays are independent
of \(X\) and each other, as in the source. Let \(\sigma>0\),
\(K\ge2\), \(\eta>0\), \(T=K\eta\), and let \(e_1\) denote
the first coordinate vector. Define the queries by
\[
\theta_l=e_1,\qquad \omega_1=\sqrt m\,e_1,\quad w_1=1,\qquad
\omega_l=\sqrt m\,w_l e_1,\quad
w_l=1+\tau_l\tanh S,\quad \tau_l=(l-1)\eta,\quad l\ge2,
\]
where \(S=\sqrt m\,(q_1)_1\). This is a valid smooth causal query
rule: \(\theta_l\) ignores previous outputs, and \(\omega_l\)
uses only the already observed \(q_1\) when \(l\ge2\). Every
\(p_l\) is generated in the prescribed order but is ignored by these
query maps. Hence the order remains
\(\theta_l\to p_l\to\omega_l\to q_l\).

The first step of (9) gives exactly
\[
q_1=\frac{X e_1+\sigma U_1+\Gamma_{11}e_1}{\sqrt m},\qquad
S=X_{11}+\sigma(U_1)_1+\Gamma_{11}\sim N(0,v),\quad v=2+\sigma^2.
\]
Indeed, both first Cholesky diagonals are
\(\sqrt{1+\sigma^2}\), so their factors cancel in the first
\(\Gamma\)-term. The reverse \(\Gamma\)-term at \(p_1\) is zero
because its triangular part excludes the diagonal.

Both histories satisfy the proposed path premises, almost surely:
\[
\|\theta_l\|=1,\quad\|\omega_l\|/\sqrt m\le1+T,\quad
\|\omega_l-\omega_j\|/\sqrt m\le\eta|l-j|.
\]
Both history matrices have rank one; each regularized effective rank is
at most one. These are temporal bounds. No dimension-independent
Lipschitz bound of the query map as a function of arbitrary inputs is
being asserted.

Write \(s=\sigma^2\), and let
\[
d_i=\frac{\sigma}{\sqrt{(s+i-1)(s+i)}},\qquad
(\Theta A_\theta^{-1})_i=e_1d_i,\qquad
\sum_{i=1}^l d_i^2=\frac{l}{s+l}.
\]
The covariance perturbation of \(q_l\) is
\[
g_l=\frac{e_1}{\sqrt m}\sum_{i\le l}d_i(\Gamma A_\omega)_{il}.
\]
Here \(A_\omega\) is a function of \(S\) alone. For \(l\ge2\),
\((A_\omega)_{1l}=w_l/\sqrt{1+s}\), so the coefficient of
\(\Gamma_{11}\) in \(g_l\) is
\(e_1w_l/[\sqrt m(1+s)]\). Every other entry of \(\Gamma\)
is independent of \(S,\Gamma_{11}\) and remains centered. Therefore
Gaussian integration by parts gives
\[
\mathbb E g_l=
\frac{e_1\tau_l}{\sqrt m(1+s)}\,
\mathbb E\operatorname{sech}^2S\ne0\quad(l\ge2).              \tag{1}
\]

There is also a strict failure of the frozen second-moment formula. Put
\[
F_l=\frac1m\mathbb E\left[(w_l^2+s)\sum_{i\le l}d_i^2\right],
\qquad
C_s=\mathbb E[(\Gamma_{11}^2-1)\tanh^2S].
\]
The expression \(F_l\) is what the deterministic-history isometry would
give if inserted under expectation without an adaptation correction.
Conditioning on \(S,\Gamma_{11}\), all cross terms with the other
Gaussian entries vanish, yielding exactly
\[
\mathbb E\|g_l\|^2-F_l
=\frac{\mathbb E[(\Gamma_{11}^2-1)w_l^2]}{m(1+s)^2}
=\frac{\tau_l^2 C_s}{m(1+s)^2}>0\quad(l\ge2).                 \tag{2}
\]
The constant and linear terms in \(w_l^2\) vanish respectively by
centering and the simultaneous sign symmetry of
\((S,\Gamma_{11})\). Strict positivity follows from
\[
\mathbb E[\Gamma_{11}^2-1\mid S]=\frac{S^2-v}{v^2},\qquad
C_s=\frac{\operatorname{Cov}(S^2,\tanh^2S)}{v^2}>0.
\]
To check the last sign, \(x\mapsto\tanh^2\sqrt x\) is strictly
increasing on \([0,\infty)\), and for an independent copy \(Y'\)
of the nondegenerate variable \(Y=S^2\), twice this covariance is
\(\mathbb E[(Y-Y')(f(Y)-f(Y'))]>0\).

The integrated isometry fails in the same explicit way. For
\(P_K=\eta\sum_{l=1}^K g_l\), let
\[
\mathcal F_K=\frac{\eta^2}{m}\mathbb E
 \sum_{i=1}^K d_i^2
 \left[\left(\sum_{l=i}^K w_l\right)^2+s(K-i+1)\right],\qquad
H=\eta\sum_{l=2}^K\tau_l=\frac{\eta^2K(K-1)}2.
\]
This is the frozen suffix formula evaluated on the adaptive history.
Because \(g_1=e_1\Gamma_{11}/\sqrt m\), the coefficient of
\(\Gamma_{11}\) in \(P_K\) is
\(e_1[T+\eta s+H\tanh S]/[\sqrt m(1+s)]\). The preceding
conditioning and symmetry argument therefore gives
\[
\mathbb E P_K=\frac{e_1H}{\sqrt m(1+s)}
 \mathbb E\operatorname{sech}^2S,\qquad
\mathbb E\|P_K\|^2-\mathcal F_K
=\frac{H^2C_s}{m(1+s)^2}>0.                                   \tag{3}
\]
For \(K=2\), \(H=\eta^2\), recovering the two-step discrepancy
\(\eta^4C_s/[m(1+s)^2]\). For fixed physical \(T\) and
\(\eta\downarrow0\), \(H\to T^2/2\): small temporal increments
do not remove this correction relative to the natural \(1/m\)
second-moment scale. Nevertheless the displayed correction itself is
\(O(1/m)\), and is fully compatible with a vanishing-width bound.

The useful conclusion is precise: causality, bounded norms, temporal
Lipschitz control, and both Gram ranks being one do not preserve the
frozen Gaussian isometry or conditional centering. A prospective adaptive
bound must estimate the retained covariance with the query-dependent
Cholesky coefficients, or supply a different self-normalized argument.
This example does not refute such a bound. It establishes no failure of
canonical trajectories, nonlinear stability, or unique restart.
No experiments were performed.
