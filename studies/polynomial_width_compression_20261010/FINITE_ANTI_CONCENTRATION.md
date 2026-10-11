# A finite, shift-uniform replacement for the qualitative scalar CLT

Author calculation, 2026-10-10. This lemma is self-contained. It does not,
by itself, establish a dense-trajectory or compression theorem. Its purpose
is to remove the qualitative central-limit step in the current initial
prediction-velocity argument once a conditional variance lower bound has
been supplied. All notation below is local.

## Lemma

Let independent identically distributed real variables have mean zero,
variance \(\sigma^2>0\), and third absolute moment \(M_3<\infty\).
For \(0<\delta<1\), if

\[
n\ge 2000\frac{M_3^2}{\sigma^6}\delta^{-2}
                    \log(16/\delta),
\]

then, for every real shift \(b\),

\[
\Pr\left\{\left|\frac1{\sigma\sqrt n}\sum_{i=1}^n X_i-b\right|
                       \le\frac\delta{10}\right\}\le\delta.
\]

The same assertion holds conditionally on a sigma-field when the variables
are conditionally independent and identically distributed, with conditional
moments satisfying the displayed bounds and with any measurable shift.
No nonlattice assumption or covariance nonsingularity is needed.

## Proof

For an independent copy \(X'\), the characteristic function satisfies

\[
|\mathbb E e^{itX}|^2
=\mathbb E\cos(t(X-X'))
\le1-\sigma^2t^2+\frac43M_3|t|^3.
\]

Here the quadratic term uses \(\mathbb E(X-X')^2=2\sigma^2\),
the cubic Taylor remainder is at most \(|t|^3\mathbb E|X-X'|^3/6\),
and \(|x-y|^3\le4(|x|^3+|y|^3)\) gives
\(\mathbb E|X-X'|^3\le8M_3\).
For \(|t|\le3\sigma^2/(8M_3)\), therefore,

\[
|\mathbb E e^{itX}|\le e^{-\sigma^2t^2/4}.
\]

Consequently the characteristic function of
\(Z=\sum_iX_i/(\sigma\sqrt n)\) has modulus at most
\(e^{-u^2/4}\) when
\(|u|\le R=3\sigma^3\sqrt n/(8M_3)\).

For any \(a>0\), the pointwise inequality
\(1_{|Z-b|\le a}\le\sqrt e\exp(-(Z-b)^2/(2a^2))\)
and the Fourier transform of the Gaussian give

\[
\Pr(|Z-b|\le a)
\le\frac{\sqrt e\,a}{\sqrt{2\pi}}
 \int_{\mathbb R}e^{-a^2u^2/2}|\mathbb E e^{iuZ}|\,du
\le\sqrt{2e}\,a+2\sqrt e\,e^{-a^2R^2/2}.
\]

The Gaussian Fourier identity follows by completing the square (or solving
its differentiated Gaussian integral); its integrable modulus justifies
Fubini. For the first integral use \(e^{-u^2/4}\) and enlarge its domain
to the line. For the remaining integral use modulus at most one and the
bound \(\Pr(|G|>s)\le2e^{-s^2/2}\), obtained by the Gaussian moment
generating function and Markov's inequality separately on both tails.
None of these estimates depends on \(b\).

Set \(a=\delta/10\). The width assumption implies

\[
\frac{a^2R^2}{2}
=\frac{9\delta^2\sigma^6 n}{12800M_3^2}
\ge\log(16/\delta).
\]

Thus the probability is at most
\((\sqrt{2e}/10+\sqrt e/8)\delta<\delta\).
Applying the same deterministic calculation to each conditional law proves
the conditional version. \(\square\)

## Exact use and remaining obligations

At zero readout the current dense model satisfies

\[
\dot f_n(0,x_a)=\frac2{mn}\sum_i
 h_i^{(L)}(0,x_a)\sum_b y_bh_i^{(L)}(0,x_b).
\]

Conditioned on lower initialized layers, the final-layer row products are
iid. One may condition additionally on the complete independent reference
network, which enters only as the shift. An index chosen from the conditional
lower-layer information is permitted by the lemma. This potentially avoids
matching the two conditional means or invoking a recursive matrix CLT.
To apply the mean-zero lemma, subtract the conditional mean from each row
product first; the sum of those means is absorbed into the same measurable
shift. The shift is not allowed to depend on the remaining unconditioned
last-layer rows.

Still required for a full application: a polynomial-width event giving a
quantitative conditional variance lower bound and third-moment upper bound;
and a quantitative derivative-to-actual-trajectory estimate. Neither is
asserted by this standalone lemma. It must not be cited as a completed
polynomial-width dense-variability theorem.
