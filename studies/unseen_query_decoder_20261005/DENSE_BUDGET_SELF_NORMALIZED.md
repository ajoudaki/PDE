# Cross-moment concentration on an empirical Gram event

2026-10-06. Scoped author lemma. The proposed self-normalized mechanism is
valid. It needs only a population second-moment bound and an upper bound
on the **raw empirical second moment**. It does not need bounded whitened
coordinates or a covariance-relative sub-Gaussian law. An upper bound on
the covariance centered at the sample mean is not a substitute.

For the vector cross moment below, the explicit conclusion is

\[
 \Pr\!\left\{
 \left\|\frac1n\sum_{i=1}^nU_iG_i-\mathbb E[UG]\right\|_2>r,
 \quad\frac1n\sum_{i=1}^nU_iU_i^T\preceq2I_R
 \right\}
 \le2\cdot5^R\exp\!\left(-\frac{nr^2}{24B^2}\right),
 \tag{1}
\]

when the pairs \((U_i,G_i)\) are iid, \(U_i\in\mathbb R^R\),
\(\mathbb E[UU^T]\preceq I_R\), and \(|G|\le B\) almost surely.
Equality \(\mathbb E[UU^T]=I_R\), as in the assignment, is sufficient.
The event involving the empirical Gram must still be supplied or controlled
by the neural application. Equation (1) does not establish its probability.

## 1. The scalar inequality with exact constants

Let \(X_1,\ldots,X_n\) be iid real random variables with mean
\(m=\mathbb EX\) and \(\mathbb EX^2\le B^2\), where \(B>0\).
For every \(C\ge0\) and \(t>0\),

\[
 \Pr\!\left\{
 \left|\frac1n\sum_iX_i-m\right|>t,
 \quad\frac1n\sum_iX_i^2\le CB^2
 \right\}
 \le2\exp\!\left(-\frac{nt^2}{2(C+1)B^2}\right).
 \tag{2}
\]

There is no restriction to small \(t\) and no fourth moment assumption.
If \(B=0\), all variables are zero almost surely and the conclusion is
trivial, interpreted separately.

Define the odd function

\[
 \psi(u)=\operatorname{sgn}(u)\log(1+|u|+u^2/2),\qquad\psi(0)=0.
 \tag{3}
\]

It satisfies, for every real \(u\),

\[
 e^{\psi(u)}\le1+u+u^2/2,\qquad
 e^{-\psi(u)}\le1-u+u^2/2,\qquad
                         |\psi(u)-u|\le u^2/2.
 \tag{4}
\]

For \(u\ge0\), the first exponential identity is equality. The second
follows from
\((1+u+u^2/2)(1-u+u^2/2)=1+u^4/4\ge1\).
Both quadratic factors are positive. Oddness supplies the negative case.
Also \(1+u+u^2/2\le e^u\), so \(\psi(u)\le u\).
For the lower bound,
\(\psi(u)\ge\log(1+u)\ge u-u^2/2\); the derivative of the last
difference is \(u^2/(1+u)\ge0\), and the difference vanishes at zero.
Oddness again gives the absolute bound for negative arguments.

For every real \(\lambda\), (4), the second-moment hypothesis, and
\(1+v\le e^v\) give

\[
 \mathbb E e^{\psi(\lambda X)}
 \le1+\lambda m+\lambda^2B^2/2
 \le\exp(\lambda m+\lambda^2B^2/2).
 \tag{5}
\]

In particular, independence yields

\[
 \mathbb E\exp\!\left\{\sum_i\psi(\lambda X_i)-n\lambda m\right\}
                      \le\exp(n\lambda^2B^2/2).
 \tag{6}
\]

Fix \(\lambda>0\). On the upper-deviation event in (2), (4) implies

\[
 \sum_i\psi(\lambda X_i)-n\lambda m
 \ge\lambda\sum_i(X_i-m)-\frac{\lambda^2}{2}\sum_iX_i^2
 >n\lambda t-\frac{n\lambda^2CB^2}{2}.
 \tag{7}
\]

Exponential Markov and (6) bound the probability of this event by
\(\exp[-n\lambda t+n\lambda^2(C+1)B^2/2]\).
Choose \(\lambda=t/[(C+1)B^2]\). This proves the upper-tail bound
with exponent \(-nt^2/[2(C+1)B^2]\). Apply the same argument to
\(-X_i\) for the lower tail and add the two probabilities. This proves
(2).

The proof uses an uncentered second moment in (5)--(7), so it incurs no
extra constant for converting the empirical second moment into a centered
one. The auxiliary function \(\psi\) is a proof device. The estimator
in (2) is the ordinary empirical mean, not a replacement robust estimator.

## 2. Exactly which centering is permitted

If instead one knows
\(\mathbb E(X-m)^2\le V^2\), apply (2) to \(X-m\). For every
\(C\ge0\),

\[
 \Pr\!\left\{
 |\bar X-m|>t,\quad
 \frac1n\sum_i(X_i-m)^2\le CV^2\right\}
       \le2\exp\!\left(-\frac{nt^2}{2(C+1)V^2}\right).
 \tag{8}
\]

Here the empirical centering is at the fixed **population mean** \(m\).
If only the raw bound in (2) is available, then

\[
 \left[\frac1n\sum_i(X_i-m)^2\right]^{1/2}
 \le\left[\frac1n\sum_iX_i^2\right]^{1/2}+|m|
 \le(\sqrt C+1)B.
 \tag{9}
\]

The first inequality is the triangle inequality in \(\mathbb R^n\),
and \(|m|\le B\) follows from Cauchy--Schwarz. Thus centering first
would also give a valid but weaker version of (2). The direct proof avoids
that loss.

The sample-centered empirical variance
\(n^{-1}\sum_i(X_i-\bar X)^2\) cannot replace the empirical second
moment in (8). The exact identity is

\[
 \frac1n\sum_i(X_i-m)^2
 =\frac1n\sum_i(X_i-\bar X)^2+(\bar X-m)^2.
 \tag{10}
\]

The missing term is precisely the deviation one is trying to control.
For a concrete failure, let \(X\) be zero with probability \(1-p\)
and equal to \(p^{-1/2}\) with probability \(p\). Then
\(\mathbb EX^2=1\), \(m=\sqrt p\), and the event that all \(n\)
samples equal \(p^{-1/2}\) has probability \(p^n\). Its sample-centered
variance is zero, while its mean error is \(p^{-1/2}-\sqrt p\).
Taking \(t=(p^{-1/2}-\sqrt p)/2\) shows that no fixed constants in
a proposed bound \(2\exp(-c n t^2)\) can hold as \(p\downarrow0\):
the proposed right side decays like \(\exp(-c'n/p)\), faster than
\(p^n\). This issue is independent of neural structure.

## 3. Vector cross moments on a Gram event

Let \(U\in\mathbb R^R\), \(R\ge1\), and scalar \(G\) satisfy
the hypotheses above (1). Write

\[
 M_n=\frac1n\sum_iU_iG_i,\qquad m=\mathbb E[UG],\qquad
 \mathcal E_C=\left\{\frac1n\sum_iU_iU_i^T\preceq CI_R\right\}.
 \tag{11}
\]

Both \(M_n\) and \(m\) are vectors in \(\mathbb R^R\). The mean
exists because every coordinate of \(U\) has a finite second moment.
For any deterministic unit vector \(a\), set \(X=a^TUG\). Then

\[
 \mathbb EX^2\le B^2\mathbb E(a^TU)^2\le B^2,\qquad
 \frac1n\sum_i(a^TU_iG_i)^2
 \le B^2a^T\left(\frac1n\sum_iU_iU_i^T\right)a\le CB^2
                    \quad\hbox{on }\mathcal E_C.
 \tag{12}
\]

There is a Euclidean \(1/2\)-net \(\mathcal N\) of the unit sphere
with at most \(5^R\) points. To construct it, take a maximal
\(1/2\)-separated set; the disjoint open balls of radius \(1/4\)
around its points lie in the radius-\(5/4\) ball, so comparison of their
volumes bounds the cardinality. Maximality gives the covering property.
For every vector \(v\), choose a net point within \(1/2\) of
\(v/\|v\|\). Cauchy--Schwarz then gives
\(\|v\|\le2\max_{a\in\mathcal N}|a^Tv|\).

Apply (2) and (12) at each net point and take a union. For every \(r>0\),

\[
 \Pr\{\|M_n-m\|>r,\ \mathcal E_C\}
 \le2\cdot5^R\exp\!\left(-\frac{nr^2}{8(C+1)B^2}\right).
 \tag{13}
\]

Setting \(C=2\) proves (1). Equivalently, for every \(s>0\),

\[
 \Pr\!\left\{
 \|M_n-m\|>
 B\sqrt{\frac{8(C+1)}n\,[R\log5+\log2+s]},\quad\mathcal E_C
 \right\}\le e^{-s}.
 \tag{14}
\]

Thus the scale is \(B\sqrt{(R+s)/n}\) with the displayed constants,
without any upper bound on \(\|U\|\) and without exponential moments
of its coordinates. The \(5^R\)-point net is proof-only.

## 4. Posterior transfer and all-prefix quantifiers

Fix a retained prefix \(c\). Under the prior, the rows have product law
\(\mu^{\otimes n}\). Let \(\pi_c\) be their posterior and suppose

\[
                    D(\pi_c\Vert\mu^{\otimes n})\le K.
 \tag{15}
\]

The functions \(U\) and \(G\) may depend on \(c\), an unseen sphere
input and time. For each such fixed choice, assume the prior second-moment
and bounded-factor hypotheses of Section 3. These choices are deterministic
when applying the prior calculation; no independence under the posterior
is assumed.

For an event with prior probability at most \(e^{-s}\), binary relative
entropy gives posterior probability at most \((K+\log2)/s\).
Indeed if its posterior and prior probabilities are \(q\) and \(p\),
data processing for the indicator gives
\(K\ge q\log(1/p)-\log2\): the binary entropy is at most \(\log2\)
and \(-(1-q)\log(1-p)\ge0\). The case \(p=0\) has posterior
probability zero by finite relative entropy.

For any \(0<\rho<1\), take \(s=(K+\log2)/\rho\) in (14).
The result is the conditional bound

\[
 \pi_c\!\left\{
 \|M_n-m\|>
 B\sqrt{\frac{8(C+1)}n
   \left[R\log5+\log2+\frac{K+\log2}{\rho}\right]},
 \quad\mathcal E_C\right\}\le\rho.
 \tag{16}
\]

If one separately proves \(\pi_c(\mathcal E_C^c)\le\rho_C\),
then the norm bound in (16) holds with posterior probability at least
\(1-\rho-\rho_C\). Alternatively, conditioning the posterior itself
on \(\mathcal E_C\) gives conditional failure at most
\(\rho/\pi_c(\mathcal E_C)\), not automatically \(\rho\).

The information input supplies one training event on which (15) holds
at **every acquired prefix** with \(K=H/\alpha\). On that event,
(16) holds for every deterministic choice of row functions satisfying its
hypotheses, including every unseen query and physical time. This statement
has no union over queries: it is a pointwise consequence of the common
entropy bound on each posterior measure. It does not assert that one
posterior row realization satisfies all such query inequalities at once.
As in the existing robust-center argument, uniform deterministic decoding
uses the conditional mass statements separately at each query on the same
training event. Fresh iid query row coordinates can be appended to the
prior and posterior as in the information input without changing relative
entropy.

For a finite set of \(q\) vector tests, union their prior exceptional
events before applying entropy. With common bounds and dimensions at most
\(R\), replace \(\log2\) in the square brackets of (16) by
\(\log(2q)\). Each exceptional event is intersected with its own Gram
event. A simultaneous un-intersected conclusion additionally needs a
posterior bound on the union of their Gram failures. Adaptive query
recursions still require the same comparison at deterministic reference
arguments and a valid propagation bound; this lemma does not justify
plugging random query summaries into fixed-function concentration.

An expectation version is also available. Define
\(V=\|M_n-m\|\mathbf1_{\mathcal E_C}\). Integrating (13) gives

\[
 \mathbb E_{\mu^{\otimes n}}
      \exp\!\left(\frac{nV^2}{16(C+1)B^2}\right)
                         \le1+2\cdot5^R\le3\cdot5^R.
 \tag{17}
\]

For verification, use
\(\mathbb Ee^{aV^2}=1+\int_0^\infty a e^{at}
\Pr(V^2>t)\,dt\) with
\(a=n/[16(C+1)B^2]\); (13) bounds the integral by
\(2\cdot5^R\int_0^\infty a e^{-at}dt\).
The entropy inequality applied to that exponential then yields

\[
 \mathbb E_{\pi_c}
      [\|M_n-m\|^2\mathbf1_{\mathcal E_C}]
 \le\frac{16(C+1)B^2}{n}[K+R\log5+\log3].
 \tag{18}
\]

Cauchy--Schwarz supplies the corresponding first-moment bound. This is
an expectation restricted to the Gram event; it is not a bound for the
full posterior discrepancy unless the complement is also controlled.

## 5. What is and is not supplied for the neural route

The proposed replacement of covariance-relative sub-Gaussianity is valid
for this cross-moment estimate: finite population second moments and a
usable empirical Gram upper event suffice. In particular the result
accommodates arbitrarily large whitened coordinates along small covariance
directions. It does not insert an inverse covariance eigenvalue into (13).

The empirical Gram event is essential. Its high probability does not
follow from \(\mathbb E[UU^T]\preceq I\) uniformly over admissible
row laws. For example, in dimension one let
\(U=\pm\sqrt{3n}\), each with probability \(1/(6n)\), and let
\(U=0\) otherwise. Then \(\mathbb EU^2=1\), but one nonzero sample
already makes \(n^{-1}\sum_iU_i^2\ge3\). Consequently
\(\Pr(\mathcal E_2)=(1-1/(3n))^n\to e^{-1/3}\), not one.
This width-dependent family rules out a uniform high-confidence deduction
from the second moment alone.

For the physical application one must therefore identify how the retained
Gram information, its noise and its finite precision enforce
\(\mathcal E_C\) under the relevant posterior. The bound is on the raw
Gram of the precise whitened variables used in the cross moment. Replacing
it by a sample-centered covariance or by the Gram of differently centered
features requires an additional argument. The bounded multiplier \(G\),
or a justified truncation with its error, must also be supplied; this note
does not strengthen the original activation assumptions.

Finally, (1) is a statistical comparison for the original iid row array
intersected with a Gram event. It does not automatically replace the
sub-Gaussian assumption in an unconditional finite-seed numerical sampler:
that sampler would need its own empirical-Gram event and its probability,
or a different counted numerical integration argument. Physical propagation,
adaptive summaries and rounded-prefix stability also remain separate.

Status: the proposed scalar and vector self-normalized inequalities,
their posterior-entropy transfer, and their centering qualifications are
proved above. Scientific inputs were the supervisor's explicit prompt and
the previously authorized five complete notes used for
`DENSE_BUDGET_SAMPLING.md`. Required skills were already read and remain
current; the authorized canonical-notation fallback remains in effect.
Only this new assigned note was written. No experiment, external source,
other study, or Git operation was used.
