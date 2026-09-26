# Scoped check of the trace and fixed-path-span bounds

Date: 2026-09-22. This is a prompt-only arithmetic and logical check of the
supervisor's supplied lemma, not an independent creative research attempt,
promotion review, or verification of a population construction. The supplied
gradient equations and loss dissipation are premises. No earlier study,
repository scientific input, external source, experiment, or Git operation
was used. The required rigorous-math skill was applied. A prompt-only scoped
subagent checked the covariance factorization separately; that check used
only the Hilbert-space lemma stated below.

**Verdict:** the proposed trace bound, the two pointwise SVD bounds, and the
fixed lower-span bound are valid. The fixed-span estimate holds in
Hilbert--Schmidt norm, uniformly along the given finite-horizon path.
All are existence estimates for a specified trajectory. They do not by
themselves construct an autonomous compressed solver or establish its cost.

## 1. Setup and trace bound

Let the two population feature spaces be real Hilbert spaces
\(\mathcal H_1,\mathcal H_2\), with probability population measures. Write
\(a\otimes b:\mathcal H_1\to\mathcal H_2\) for the map
\(z\mapsto a\langle b,z\rangle\). Assume the supplied flow exists on
\([0,T]\), with the strong measurability needed for the displayed integrals.
The population \(L^2\) spaces can be taken separable; equivalently, it
suffices to restrict to the separable closed spans of the strongly
measurable feature fields. These are regularity requirements for the
integrals, not an existence proof for the flow.

For training input \(x\), set
\[
 \delta(t,x)=c(t)\operatorname{sech}^2 Z_2(t,x),\qquad
 h(t,x)=H_1(t,x),\qquad R=\sqrt{2L(0)}.
\]
Loss dissipation gives \(\|r(t,\cdot)\|_{L^2(\mu)}\le R\).
The zero initial readout and \(|H_2|\le1\) imply, for almost every upper
population coordinate,
\[
 |c(t)|
 \le\int_0^t\mathbb E_\mu|r(s,x)|\,ds
 \le Rt.
\]
Since the population measures are probability measures,
\(\|h(t,x)\|_2\le1\) and \(\|\delta(t,x)\|_2\le Rt\).
Define the actual nonnegative accumulated weight
\[
 A(t)=\int_0^t\mathbb E_\mu
       \bigl[|r(s,x)|\,\|\delta(s,x)\|_2\,\|h(s,x)\|_2\bigr]\,ds.
\]
Then
\[
 A(t)\le\int_0^t R^2s\,ds=\frac{R^2t^2}{2}.
\]
The trace norm of a rank-one operator is
\(\|a\otimes b\|_1=\|a\|_2\|b\|_2\). Thus the supplied middle-increment
equation integrates in trace norm and gives
\[
 K(t)=-\int_0^t\mathbb E_\mu[r(s,x)\delta(s,x)\otimes h(s,x)]\,ds,
 \qquad
 \|K(t)\|_1\le A(t)\le A(T)\le\frac{R^2T^2}{2}.
\]
Here \(K(0)=0\). The bounded initial operator \(W_0\) is relevant to the
assumed flow but is not needed in these norm estimates. The estimates
concern the increment \(K(t)\), not the full operator \(W_0+K(t)\).

## 2. SVD truncation at each time

Fix \(t\) and let \(s_1(t)\ge s_2(t)\ge\cdots\ge0\) be the singular
values of \(K(t)\), padded by zeros when its rank is finite. Trace-class
compactness gives a singular-value decomposition, with
\(\sum_j s_j(t)=\|K(t)\|_1\le A(t)\).
Let \(K_P(t)\) retain its first \(P\) terms, where \(P\ge0\) is an integer.
Then
\[
 \|K(t)-K_P(t)\|_{\rm op}=s_{P+1}(t)
 \le\frac{A(t)}{P+1},
\]
because the first \(P+1\) singular values are each at least
\(s_{P+1}(t)\). Also
\[
 \begin{aligned}
 \|K(t)-K_P(t)\|_{\rm HS}^2
 &=\sum_{j>P}s_j(t)^2\\
 &\le s_{P+1}(t)\sum_{j>P}s_j(t)
 \le\frac{A(t)^2}{P+1}.
 \end{aligned}
\]
Replacing \(A(t)\) by \(A(T)\) makes both bounds uniform in
\(0\le t\le T\), but the retained singular subspaces may depend on \(t\).

## 3. One lower span for the entire path

The proposed covariance supplies a stronger quantifier: one lower span
works for every time on this particular path up to \(T\).
Define a positive measure on \([0,T]\times\mathcal X\) by
\[
 d\nu(s,x)=|r(s,x)|\,\|\delta(s,x)\|_2\,\|h(s,x)\|_2
             \,ds\,d\mu(x).
\]
Its mass is \(A(T)\). On the set of positive weight, define the unit fields
\[
 u(s,x)=-\operatorname{sign}(r(s,x))
             \frac{\delta(s,x)}{\|\delta(s,x)\|_2},\qquad
 v(s,x)=\frac{h(s,x)}{\|h(s,x)\|_2}.
\]
Set them to zero on the zero-weight set; no division there is needed.
Then
\[
 K(t)=\int_{s\le t}u\otimes v\,d\nu,
 \qquad C_1=\int v\otimes v\,d\nu.
\]
The covariance is positive and trace class. For an orthonormal basis,
Tonelli's theorem and Parseval's identity give
\(\operatorname{tr}C_1=\int\|v\|_2^2d\nu=A(T)\).
Let \(\lambda_j\) denote its decreasing eigenvalues, and let \(\Pi_P\)
be a projector onto \(P\) largest-eigenvalue directions. If its rank or
the ambient dimension is less than \(P\), retain all positive directions;
the projector has rank at most \(P\), and subsequent eigenvalues are zero.
Put \(Q=I-\Pi_P\).

Factor the increment through \(L^2(\nu)\):
\[
 Vz=\langle v,z\rangle,\qquad
 U_tg=\int_{s\le t}u g\,d\nu,
 \qquad K(t)=U_tV.
\]
We have \(V^*V=C_1\), so
\[
 \|VQ\|_{\rm op}^2=\|QC_1Q\|_{\rm op}=\lambda_{P+1}.
\]
For an upper-space orthonormal basis \((e_j)\),
\[
 \|U_t\|_{\rm HS}^2
 =\sum_j\|U_t^*e_j\|_{L^2(\nu)}^2
 =\int_{s\le t}\sum_j|\langle u,e_j\rangle|^2d\nu
 =A(t).
\]
The composition inequality required here follows directly from the same
basis calculation:
\[
 \begin{aligned}
 \|U_tVQ\|_{\rm HS}^2
 &=\sum_j\|QV^*U_t^*e_j\|_2^2\\
 &\le\|VQ\|_{\rm op}^2\sum_j\|U_t^*e_j\|_2^2
 =A(t)\lambda_{P+1}.
 \end{aligned}
\]
Finally \((P+1)\lambda_{P+1}\le\operatorname{tr}C_1=A(T)\), proving
\[
 \sup_{0\le t\le T}\|K(t)-K(t)\Pi_P\|_{\rm HS}
 \le\frac{A(T)}{\sqrt{P+1}}
 \le\frac{R^2T^2}{2\sqrt{P+1}}.
\]
The same bound holds in operator norm. A useful stronger pointwise form is
\(\|K(t)Q\|_{\rm HS}^2\le A(t)\lambda_{P+1}\).
Using \(C_1(t)=\int_{s\le t}v\otimes v\,d\nu\) in the factorization
also gives \(\|K(t)Q\|_{\rm HS}^2\le A(t)\|QC_1(t)Q\|_{\rm op}\).

## 4. Scope and norm traps

- The covariance span depends on the full trajectory and horizon \(T\).
  “One span” means one span for this path, not one fixed span for every
  training law, label choice, or time horizon.
- The covariance guarantee is a right-projection guarantee. The range of
  \(K(t)\Pi_P\) may vary with \(t\); a fixed upper span or a fixed small
  coefficient matrix has not been constructed here.
- The \(A(T)/(P+1)\) operator estimate belongs to a separate SVD chosen
  at each time. The covariance-span argument supplies
  \(A(T)/\sqrt{P+1}\) in both norms; it does not justify transferring the
  stronger SVD operator rate to this fixed span.
- A loose bound through the covariance tail trace would not yield the
  stated rate. The factorization above uses the largest omitted covariance
  eigenvalue and the Hilbert--Schmidt norm of the other factor.
- The bounds are finite-horizon statements. Loss monotonicity alone does
  not establish \(A(\infty)<\infty\). If that extra condition were known,
  the same measure-factorization proof would apply on \([0,\infty)\).
- The probability normalization, half-loss convention, exact zero initial
  readout, and use of the learned increment matter to the constants.
  If \(R=0\), all weights in \(\nu\) vanish and every bound is zero.
- No bound here quantifies an evolving compressed model's error relative
  to the dense flow. Rank approximation of a known trajectory and stable
  approximation by an autonomous evolution are different conclusions.

No correction to the proposed inequalities is required. The needed
correction is to qualify the word “universal”: the covariance span is
uniform over time on one specified path, and is defined using that path.
