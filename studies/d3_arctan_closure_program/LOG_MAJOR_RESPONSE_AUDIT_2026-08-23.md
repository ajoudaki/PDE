# Log-majorization audit for the reachable response

**Date:** 23 August 2026.

**Verdict:** ordinary Gaussian functional inequalities and random-Lipschitz
arguments return the missing response norm or an infinite derivative
hierarchy.  Exterior-power log-majorization gives a useful replacement for
operator-norm Gronwall: it controls averaged tangent singular values and
handles unbounded Gaussian row multipliers without a \(\sqrt{\log n}\) loss.
It does not yet control the adaptive off-diagonal transport on the reachable
column-response subspace.

## 1. Continuous-time log-majorization

Let \(U'=K(t)U\), \(U(0)=I_m\), and
\(S(t)=\tfrac12(K(t)+K(t)^*)\).  For every \(1\le k\le m\),

\[
 \prod_{r=1}^k s_r(U(t))
 \le
 \exp\left\{\int_0^t\sum_{r=1}^k\lambda_r(S(s))\,ds\right\}.          \tag{1.1}
\]

Indeed, \(\wedge^kU\) solves the induced exterior-power evolution.  Its
logarithmic operator-norm derivative is at most the largest eigenvalue of the
induced symmetric generator, namely
\(\sum_{r\le k}\lambda_r(S)\).  Integrating proves (1.1).

Unlike \(\|U\|_{\rm op}\le e^{\int\|S\|_{\rm op}}\), (1.1) retains the
whole spectral profile.  A few localized expanding directions need not
destroy the normalized Frobenius response when its source has
\(n^{-1/2}\)-scale overlap with those directions.

## 2. Weighted Gaussian blocks

Let \(A_i\) be iid standard Gaussians, let \(G_{ik}\sim N(0,1/n)\), and
consider

\[
 H=\begin{pmatrix}0&D_AG\\G^*D_A&0\end{pmatrix}.                     \tag{2.1}
\]

Its nonzero eigenvalues are \(\pm s_i(D_AG)\), while singular-value
majorization gives

\[
 s_i(D_AG)\le\|G\|_{\rm op}|A|_{(i)}.                               \tag{2.2}
\]

Consequently, for each fixed \(a\), there are \(c_a,C_a>0\) such that

\[
 \left\|\frac1{2n}\operatorname{tr}e^{a|H|}\right\|_q
 \le C_a,
 \qquad 2\le q\le c_a\log n.                                       \tag{2.3}
\]

To prove (2.3), condition on \(L=\|G\|_{\rm op}\), use

\[
 n^{-1}\sum_i e^{a s_i(D_AG)}
 \le n^{-1}\sum_i e^{aL|A_i|},                                     \tag{2.4}
\]

and combine the Gaussian operator-norm tail with Rosenthal's inequality for
the empirical exponential moment.  The same estimate holds for
\(D_{c(t)A_0}G\) whenever \(\|c(t)\|_\infty\le C\), even when \(c(t)\)
is adapted to \(G\), because (2.2) is deterministic.

Thus the \(\sqrt{\log n}\) norm of a weighted Gaussian block is an artifact
of taking the largest singular value.  Its averaged exponential spectral
profile is uniformly controlled.

## 3. Why standard Gaussian inequalities stop earlier

Gaussian log-Sobolev applied to the response \(J=D_gB_3\) asks for
\(D_gJ=D_g^2B_3\).  Higher-order concentration asks for an a priori top
derivative tensor; second-order Poincare asks for the same unavailable next
variation; and Ornstein--Uhlenbeck hypercontractivity only gives
\((p-1)^{m/2}\) on chaos \(m\).  The entire function \(e^{tG}\) shows that
analyticity and vanishing higher derivatives of the vector field do not
prevent lognormal \(e^{cp}\) moment growth.

An ambient Hilbert--Schmidt multiplier estimate is also false.  If
\(i_*\) maximizes \(|A_i|\) and \(V=e_{i_*}e_1^*\), then

\[
 \|V\|_{\rm HS}=1,\qquad
 \|D_AV\|_{\rm HS}=\max_i|A_i|\asymp_{L^2}\sqrt{\log n}.             \tag{3.1}
\]

Any successful estimate must therefore be restricted to the actual
delocalized response image; it cannot hold for arbitrary Hilbert--Schmidt
directions.

## 4. Precise remaining spectral lemma

Let \(\mathcal K(t)\) be the exact natural-coordinate tangent generator after
the local \(Ad'\) and \(R_2d'\) loops have been canceled, restricted to the
variables reachable from one normalized raw middle column.  A sufficient
new statement has the form

\[
 \left\|
 \frac1n\sum_{r\le Cn}
 \exp\left{2\int_0^t
 \lambda_r(\operatorname{Sym}\mathcal K(s))\,ds\right}
 \right\|_{p/2}
 \le C_Tp^2,
 \qquad p\le c_T\log n.                                               \tag{4.1}
\]

Together with (1.1) and the diffuse initial/source covariance, (4.1) would
give the desired Frobenius-response estimate.  Section 2 proves the fixed
weighted-Gaussian part of such a bound.  The unresolved part is the adaptive
off-diagonal transport: taking its operator norm loses delocalization, while
Gaussian integration by parts differentiates the response and returns the
higher-order hierarchy.

This is a narrower and potentially useful target, but (4.1) currently has
conditional status only.
