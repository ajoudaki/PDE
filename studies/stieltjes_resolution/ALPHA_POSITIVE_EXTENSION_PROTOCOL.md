# Strictly positive block-metric extension: exact contract

Status: frozen before order-eleven/order-thirteen production, 18 August 2026.

## Decision question

For the same one-input quadratic network and Gaussian initialization, fix
$\beta=1$ and use

\[
D_{\alpha,1}=D_a+\alpha D_u+D_W,
\qquad \alpha\geq0.
\]

Does the shifted $3\times3$ output-kernel Hankel determinant that is negative
at $\alpha=0$ remain strictly negative on a certified interval
$[0,\varepsilon]$ with an explicit rational $\varepsilon>0$?

## Exact object and limit order

At width $n$,

\[
z_i=n^{-1/2}\sum_jW_{ij}u_j^2,
\qquad
f_n=n^{-1}\sum_i a_i z_i^2.
\]

For each fixed $k$, the width limit is taken first:

\[
F_\alpha^{(k)}(0)
=\lim_{n\to\infty}\mathbb E[D_{\alpha,1}^{k}f_n].
\]

The required primary artifact is the complete exact polynomial
$F_\alpha^{(k)}(0)\in\mathbb Z[\alpha]$ for every $0\leq k\leq13$.  Parity
must be checked rather than assumed.  No positive-time, width-first, or
finite-width trajectory claim is part of this task.

Write $F_\alpha(s)=s\psi_\alpha(s^2)$ and

\[
K_\alpha(y)=F_\alpha'(F_\alpha^{-1}(y)),
\qquad
R_\alpha(x)=
\frac{K_\alpha(\sqrt{x})-(63+48\alpha)}{x}
=\sum_{r\geq0}(-1)^r\mu_r(\alpha)x^r.
\]

The decision polynomial/rational function is

\[
\Delta(\alpha)
=\det(\mu_{i+j+1}(\alpha))_{i,j=0}^{2}.
\]

## Required exact gates

1. The new polynomials through order nine must equal the retained Campaign-4
   bivariate jets after substituting $\beta=1$.
2. At $\alpha=0$, every odd jet through order thirteen, every
   $\mu_0,\ldots,\mu_5$, and $\Delta(0)$ must reproduce
   `BLOCK_METRIC_COUNTEREXAMPLE.json` exactly.
3. At $\alpha=1$, the jets through order eleven must reproduce the accepted
   canonical certificates exactly.  The order-thirteen value is new and must
   not be inferred from an old bound or numerical estimate.
4. All arithmetic used for the scientific result must be exact.  A scan may
   guide the choice of $\varepsilon$ but cannot certify its sign.
5. The final interval proof must exhibit a rational $\varepsilon>0$, verify
   every denominator is positive on $[0,\varepsilon]$, and prove the
   determinant numerator is strictly negative throughout that closed
   interval by an exact coefficient, Bernstein, Sturm, or equivalent
   certificate.
6. A second implementation or algebraically distinct reconstruction must
   reproduce the decisive jet, determinant, and interval sign.

## Outcomes

- **Pass:** all exact gates hold and an explicit rational $\varepsilon>0$ is
  certified with $\Delta(\alpha)<0$ for every
  $0\leq\alpha\leq\varepsilon$.
- **Obstruction:** the complete exact jet cannot be obtained or an exact gate
  fails.  Report the smallest missing coefficient/lemma and its measured or
  proved resource obstruction; do not replace it by a scan.
- **Refutation of persistence:** exact algebra gives a zero or nonnegative
  determinant arbitrarily close to zero.  This would contradict continuity
  at the already negative value and therefore can occur only if a claimed
  width-limit or algebraic bridge fails; expose that failure explicitly.

## Scope

Any certified $\varepsilon$ proves failure for strictly positive-definite
block metrics $(\alpha,1)$ with $0<\alpha\leq\varepsilon$.  It does not by
itself reach the canonical point $\alpha=1$ unless the certified interval
does.  The user requested the complete polynomial through order thirteen, so
a proof based only on an unspecified continuity neighborhood or on finitely
many numerical evaluations is insufficient.

## Recorded outcome

**Pass.**  The complete exact jet through order thirteen was obtained, every
overlap gate passed, and
\[
\varepsilon=\frac1{100}
\]
was certified by exact convexity and Bernstein arguments.  A direct
\(\mathbb Q[\alpha]\)-valued implementation independently reproduced every
jet coefficient and the determinant interval.  A separate 37-node scalar
Lagrange-inversion reconstruction reproduced the complete degree-36
determinant numerator.
