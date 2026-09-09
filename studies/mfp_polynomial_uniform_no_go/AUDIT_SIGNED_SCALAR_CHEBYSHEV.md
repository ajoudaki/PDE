# Hostile audit of the signed scalar Chebyshev theorem

## Verdict

**PASS for the frozen scalar theorem, after one notation correction.**  The
translation which removes the degree-\((d-1)\) coefficient is an exact
conjugacy, the noncentral Gaussian tail estimate is sufficient, and the
Gaussian factorial gain is of order \(t d^{2t}\) in the logarithm while the
Chebyshev penalty is only order \(d^{2t}\).  The argument therefore proves
both displayed scalar suprema.

The theorem does not prove the corresponding statement for the full
two-hidden-layer width-first OMFP output.  Its final audit boundary states
this correctly.

## 1. Translation and the odd-degree coefficient

Put

\[
 \mu=\frac{c_{d-1}}{dc_d},\qquad Y=Z+\mu,qquad
 \widetilde P(y)=P(y-\mu).
\]

The coefficient of \(y^{d-1}\) in \(\widetilde P\) is

\[
 c_{d-1}-dc_d\mu=0.
\]

Moreover,

\[
\begin{aligned}
 A^+&=A+hP(Z)=A+h\widetilde P(Y),\\
 Y^+&=Z^++\mu=Y+hA\widetilde P'(Y).
\end{aligned}
\]

Thus this is an exact coordinate conjugacy, not an approximation.  It changes
only the initialization law to \(Y_0\sim N(\mu,1)\), independent of the
standard \(A_0\).  It also preserves the observable exactly:
\(A P(Z)=A\widetilde P(Y)\).

Let \(r=d^{N-1}\), \(s=d^N\).  After time one the top coefficients are
\(P(Y_0)\) and \(A_0P'(Y_0)\), and every later top branch uses the leading
monomial.  Hence the top output is a positive constant times

\[
 P(Y_0)^r\{A_0P'(Y_0)\}^s.
\]

For odd \(d\), \(s\) is odd, so its expectation vanishes through the
independent centered factor \(\mathbb EA_0^s=0\).

At one lower \(h\)-degree, a later identity choice loses
\(\delta_k-\delta_{k-1}=d^{k-1}\ge d\) powers for \(k\ge2\).  At the second
update, a lower activation monomial of degree \(j\) loses \(d-j\) powers.
The only possible one-power loss is \(j=d-1\), whose coefficient was removed
by the translation.  Terminal lower monomials lose at least two powers as
well.  Therefore the two first-step identity choices listed in formula (7)
are exhaustive.

The first expectation in (7) must use the same shifted variable \(Y\) as the
second.  The source draft wrote \(G\) there while subsequently declaring only
\(Y\sim N(\mu,1)\).  This was a notation-level but mathematically material
ambiguity and has been corrected to

\[
 \mathbb E[P(Y)^{r-1}P'(Y)^s].
\]

An independent exact expansion gives the same coefficient.  In the original
untranslated coordinates it contains an additional degree-\((d-1)\) branch;
after translation that branch vanishes, while the shift of the Gaussian law
reproduces its numerical contribution exactly.  The script
`../temporary_quadratic_l2_order5/audit_general_polynomial_chebyshev.py`
checks this identity over \(\mathbb Q\) for a signed cubic at \(N=2\), as
well as the even-degree top formulas for signed quadratic and quartic cases.

## 2. Noncentral tail estimate

For \(K\ge R^2\), the interval

\[
 I_K=[\sqrt K,\sqrt K+K^{-1/2}]
\]

lies in \(\{|x|\ge R\}\), has length \(K^{-1/2}\), and satisfies
\(x^K\ge K^{K/2}\).  If \(Y\sim N(\mu,1)\), then on this interval

\[
 e^{-(x-\mu)^2/2}
 \ge
 \exp\!\left[-\frac12
 (\sqrt K+K^{-1/2}+|\mu|)^2\right].
\]

Integration proves (11) exactly.  No symmetry or centering of \(Y\) is used.

The coefficient bounds in (8) imply (9), since for \(|x|\ge1\),

\[
 \sum_{j<d}|c_j||x|^j\le C_0|x|^{d-1},\qquad
 \sum_{1\le j<d}j|c_j||x|^{j-1}\le C_1|x|^{d-2}.
\]

For odd \(d\), the leading monomial of \(P\) has the sign of \(x\), and
that of \(P'\) is positive on both tails.  The half-leading bounds therefore
also prove (10).

In (7), \(r-1\) and \(s-1\) are even.  Thus the first tail integrand has
the sign of \(P'\), and the second has the sign of \(xP(x)\); both are
nonnegative outside \([-R,R]\).  Their raw Gaussian powers are

\[
 d(r-1)+(d-1)s=ds-d=d(s-1)
\]

and

\[
 1+dr+(d-1)(s-1)=ds-d+2,
\]

which verifies (14).  The compact-region estimates (15) follow by taking
the probability of that region to be at most one.

The logarithm of either tail lower bound is

\[
 \frac d2s\log s+O_P(s),
\]

whereas each compact bound has logarithm \(O_P(s)\).  Hence an
activation-defined finite \(N_P\) exists after which both signed expectations
are positive.  To avoid an implicit monotonicity claim, the theorem now
defines \(N_P\) as the least index after which the explicit inequalities hold
for every later \(N\).  Nonemptiness follows from the displayed logarithmic
difference.  If a closed numerical upper bound is desired, replace the
\(O_P(s)\) terms by the explicit coefficient logarithms in (9), (11), and
(15), then require \(\log s\) to exceed their resulting constant; this is a
finite coefficient-only computation.

## 3. Chebyshev constant and growth

Under \(x=H(y+1)/2\), a leading coefficient \(a_m\) becomes
\(a_m(H/2)^m\).  The leading coefficient of \(T_m\) is \(2^{m-1}\), so

\[
 \|R\|_{L^\infty[0,H]}
 \ge 2^{1-2m}|a_m|H^m.
\]

Thus the factor in (3) is correct.

At the fine horizon \(N=2t\), put \(s=d^{2t}\).  The two Gaussian moments
in the retained coefficient have total order

\[
 (d+1)s+O_d(1).
\]

Their factorial contribution, divided by \(s\), is
\((d+1)t\log d+O_d(1)\).  Since

\[
 k_{2t}=\frac{d+1}{d-1}s+O_d(1),
\]

the interval factor contributes
\(-\frac{d+1}{d-1}\log t+O_{P,\rho}(1)\), and Chebyshev contributes only a
constant times \(s\).  This verifies (18) and proves that the lower bound in
(17) tends to infinity.  Also \(k_{2t}>m_t\) for all sufficiently large
\(t\), so the coarse polynomial cannot alter this coefficient.

## 4. Cubic subtraction

At order three, an \(N\)-fold Euler composition contains at most three
selected update placements.  There are at most \(N^3\) placements and only
a finite list of derivative trees, involving Gaussian integrals of the fixed
polynomial and its first three derivatives.  This proves
\(|\kappa_t|\le K_P(2t)^3\) with activation-only \(K_P<\infty\).

If \(h_t\) maximizes \(|D_t|\) on \([0,\rho/t]\), then for large \(t\),
\(h_t>0\), because \(D_t(0)=0\) while the maximum diverges.  Moreover,

\[
 |D_t(h_t)-\kappa_th_t^3|
 \ge |D_t(h_t)|-8K_P\rho^3\longrightarrow\infty,
\]

and

\[
 t^4h_t^5\le\rho^5/t.
\]

This proves (2).

## Final boundary

No finite-width or full-network inequality is inferred.  With signed lower
coefficients, deletion of the bottom update is not coefficientwise monotone.
Chebyshev controls cancellation among \(h\)-coefficients of the scalar
polynomial, but it supplies neither that missing deletion comparison nor a
width-first leading-coefficient theorem for the full reused-matrix DAG.
