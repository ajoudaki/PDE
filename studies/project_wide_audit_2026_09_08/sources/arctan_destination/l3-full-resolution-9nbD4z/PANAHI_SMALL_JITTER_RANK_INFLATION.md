# Small frozen jitter can keep the comparison perturbation macroscopic

This tests robustness of the frozen-history estimate, not the canonical
network theorem. It shows that a uniformly small change of history,
at the same scale as the Cholesky regularization, cannot simply be
discarded. No assertion is made that the actual perturbed neural-network
history has the law used below.

Use the exact frozen perturbation formulas in
PANAHI_EULER_PERTURBATION_SIZE.md, with both population sizes equal to
\(m\). Fix \(T,B>0\), set \(K=m^2\), \(\eta=T/K\), and take any
\(\sigma=\sigma_m>0\) tending to zero.
Let \(U\in\mathbb R^{m\times K}\) have independent standard Gaussian
entries, independently of the auxiliary \(\Gamma\). Define
\[
\theta_l=\frac{\sigma}{\sqrt m}U_l,\qquad
\omega_l=\sqrt m\,B e_1,\qquad 1\le l\le K.
\]
After conditioning on \(U\), these are frozen histories and all exact
Gaussian identities from the cited note apply. The assertions are
\[
\max_{l\le K}\|\theta_l\|_2\longrightarrow0,\qquad
\frac{r_{\rm eff}(\Theta,\sigma)}m\longrightarrow1,
\]
\[
\|g_K\|_2^2\longrightarrow B^2,\qquad
\left\|\eta\sum_{l=1}^K g_l\right\|_2^2
\longrightarrow T^2B^2
\]
in probability. In particular, neither the raw perturbation nor its
time integral vanishes. The limiting zero history itself has zero
covariance-matching perturbation.

## Proof

For a standard Gaussian vector \(V\in\mathbb R^d\),
\(\mathbb E e^{t\|V\|_2^2}=(1-2t)^{-d/2}\) for \(t<1/2\).
Chernoff's inequality gives, for \(0<a<1\),
\[
\Pr\!\left(\left|\|V\|_2^2/d-1\right|>a\right)
\le2e^{-da^2/8}.
\]
For completeness, the optimized upper exponent is
\(-d[a-\log(1+a)]/2\), bounded by \(-da^2/8\);
the lower exponent is \(-d[-a-\log(1-a)]/2\), which is smaller.
A union bound over \(K=m^2\) columns, with \(a=1/2\), shows that
\(\max_l\|U_l\|_2/\sqrt m\le\sqrt{3/2}\) with probability tending
to one. This proves the first claim for every \(\sigma_m\to0\).

Let \(p=\lceil m^{3/2}\rceil\), which is at most \(K\), and let
\(U_{[p]}\) denote the first \(p\) columns. With probability tending
to one,
\[
\frac1p U_{[p]}U_{[p]}^\top\succeq\frac12 I_m.                 \tag{1}
\]
Here \(A\succeq B\) means \(v^\top(A-B)v\ge0\) for every \(v\).
To prove (1), take a \(1/4\)-net of the unit sphere with at most
\(9^m\) points. Such a net follows by taking a maximal separated
set and comparing the volumes of its disjoint radius-\(1/8\) balls.
For each net vector \(v\), \(\|U_{[p]}^\top v\|_2^2\) has the
chi-squared law with \(p\) terms. The preceding bound with \(a=1/4\)
and a union bound give net error at most \(1/4\), except on an event
of probability at most \(2\exp(m\log9-p/128)\).
For any symmetric \(A\), approximation by this net gives
\(\|A\|_{\rm op}\le2\max_v|v^\top A v|\). Apply this to
\(A=U_{[p]}U_{[p]}^\top/p-I_m\), proving (1).

Write \(\Theta_{[p]}=\sigma U_{[p]}/\sqrt m\). Its effective rank is
\[
r_p=\operatorname{tr}\!\left[
  \frac{U_{[p]}U_{[p]}^\top}{m}
  \left(\frac{U_{[p]}U_{[p]}^\top}{m}+I_m\right)^{-1}
\right].
\]
The factor \(\sigma\) has canceled exactly. On (1), every eigenvalue
inside the fraction is at least \(p/(2m)\), whence
\[
\frac{p}{p+2m}\le \frac{r_p}{m}\le1.
\]
Thus \(r_p/m\to1\). Effective rank increases on adding columns:
indeed \(A\mapsto I-(I+A)^{-1}\) preserves the order on positive
matrices. Hence \(r_p\le r_K\le m\), proving \(r_K/m\to1\).

Let \(A_\theta\) be the regularized upper Cholesky factor, and write
\(t_i=(\Theta A_\theta^{-1})_i\). Prefix Cholesky factors agree with
the corresponding leading blocks, so
\[
\sum_{i\le p}\|t_i\|_2^2=r_p,\qquad
\sum_{i\le K}\|t_i\|_2^2=r_K,\qquad
\sum_{i\le K}t_it_i^\top\preceq I_m.                          \tag{2}
\]
The last identity follows from
\(\Theta(\Theta^\top\Theta+\sigma^2I)^{-1}\Theta^\top
\preceq I_m\).

Conditional on \(U\), the vector \(g_K\) is centered Gaussian, with
\[
\operatorname{Cov}(g_K\mid U)
=\frac{B^2+\sigma^2}{m}\sum_{i\le K}t_it_i^\top.
\]
Its covariance trace is \((B^2+\sigma^2)r_K/m\to B^2\) in
probability, and its largest eigenvalue is at most
\((B^2+\sigma^2)/m\). For a centered Gaussian vector of covariance
\(C\), independence in an orthonormal eigenbasis gives
\(\operatorname{Var}(\|Z\|_2^2)=2\operatorname{tr}(C^2)\).
Consequently the conditional variance here is at most
\(2(B^2+\sigma^2)^2/m\). Conditional Chebyshev's inequality proves
\(\|g_K\|_2^2\to B^2\).

The exact suffix calculation also gives, for
\(P_K=\eta\sum_{l=1}^K g_l\),
\[
\operatorname{Cov}(P_K\mid U)
=\frac{\eta^2}{m}\sum_{i=1}^K
 \left[B^2(K-i+1)^2+\sigma^2(K-i+1)\right]t_it_i^\top.
\]
Its trace lies between
\[
T^2B^2\left(1-\frac{p-1}{K}\right)^2\frac{r_p}{m}
\quad\hbox{and}\quad T^2B^2+\sigma^2T\eta.
\]
Both bounds tend to \(T^2B^2\). By (2), its largest covariance
eigenvalue is at most \((T^2B^2+\sigma^2T\eta)/m\). The same
conditional variance calculation proves the asserted convergence of
\(\|P_K\|_2^2\).

## Scope

The history is uniformly close to zero. In the smooth-history theorem's
scaling regime \(\sigma\gg m^{-1/2}\), it is not uniformly
time-Lipschitz: already
\(\|\theta_2-\theta_1\|_2/\eta
=(\sqrt2+o_{\mathbb P}(1))\sigma m^2/T\) diverges.
For much smaller \(\sigma\) it can instead have bounded temporal
Lipschitz constants, but then the smooth-history theorem's sufficient
regularization regime is not satisfied. That theorem remains valid
in both cases. This example rules out extending its conclusion merely
by saying that the history has an additional \(O(\sigma)\) jitter that
vanishes uniformly. Regularized effective rank is sensitive to that
jitter when the number of queries greatly exceeds the width.

This also explains why an adaptive effective-rank bound, even if
proved, would not automatically settle the network comparison.
Its rank or temporal premise would have to be verified for the actual
perturbed history, which receives fresh additive query noise.
The present construction is a frozen algebraic test, not a proof that
the canonical comparison has macroscopic perturbations, and not a
counterexample to the requested MF/GF limit. No experiments were used.
