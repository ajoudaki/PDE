# Collaborative check of the direct energy-stability route

2026-10-03. Scoped internal mathematical reconstruction of the complete
`GENERAL_DATA_STABILITY_ROUTE.md`, using its definitions and the supplied
general-data source estimate in `NONORTHOGONAL_DIRECT_ROUTE.md`. This is a
collaborative check, not an independent promotion review. The current
canonical-notation skill, neural-response reference, and rigorous-math skill
were applied. No experiments, Git operations, manuscript edits, or other
studies were used.

Checked source hashes:

```text
015efebaff428647bcc90353804f9652b1a7e222b88a5ad8566dd2f0c4f62583  GENERAL_DATA_STABILITY_ROUTE.md
5619965ad3ea85c186385951d07f59f3fe7e01c0f52b5b7710de65ba38896522  NONORTHOGONAL_DIRECT_ROUTE.md
```

**Verdict:** the prediction-Hessian estimate, endpoint-residual energy
identity, deterministic integrating-factor bound, and conditional root-width
schedule are correct as stated. No substantive mathematical objection was
found. The spatial-distribution hypothesis remains unproved; this is not an
unconditional general-data tracking theorem.

## 1. Hessian reconstruction and its normalization

Use the source's two-tanh network, canonical mobilities \((n,1,n)\), and
parameter discrepancy \(\Delta\theta=(\Delta A,\Delta W,\Delta w)\).
Its squared mobility norm and first-layer row fourth-moment quantity are
\[
e^2=n^{-1}\|\Delta A\|_F^2+\|\Delta W\|_F^2
+n^{-1}\|\Delta w\|_2^2,
\qquad
A_4^2=\left(n^{-1}\sum_i\|\Delta A_{i,:}\|_2^4\right)^{1/2}.
\]
On the straight segment \(\theta_s=\theta_D+s\Delta\theta\), put
\(\eta_a=\Delta A v_a\) and
\(u_s=\Delta W h_{a,s}^{(1)}+
W_s[g(z_{a,s}^{(1)})\odot\eta_a]\), with
\(g=\operatorname{sech}^2\). Differentiating the second preactivation gives
\[
\partial_s^2z_{a,s}^{(2)}
=2\Delta W[g(z_{a,s}^{(1)})\odot\eta_a]
+W_s[g'(z_{a,s}^{(1)})\odot\eta_a^2].
\]
Substitution in the twice differentiated prediction gives exactly the four
terms in source equation (7), including its factors of two and its factor
\(1/n\) in every term.

The segment inherits the hidden operator and readout coordinate bounds by
convexity. Consequently
\(\|\Delta w\|_2\le\sqrt n e\),
\(\|u_s\|_2+\|\eta_a\|_2\le C\sqrt n e\), and
\(\|\delta_{a,s}^{(2)}\|_2+\|k_{a,s}^{(1)}\|_2\le CY\sqrt n\).
The first three Hessian terms are therefore bounded by
\(Ce^2\), \(CYe^2\), and \(CYe^2\), respectively. The first term
indeed has no factor of \(Y\): its readout factor is the discrepancy
\(\Delta w\), not the small current readout.

For the last term, normalized Cauchy--Schwarz gives
\[
\frac1n\left|\sum_i k_{a,s,i}^{(1)}
g'(z_{a,s,i}^{(1)})\eta_{a,i}^2\right|
\le C\frac{\|k_{a,s}^{(1)}\|_2}{\sqrt n}
\left(\frac1n\sum_i|\eta_{a,i}|^4\right)^{1/2}
\le CY\|v_a\|_2^2 A_4^2.
\]
Thus the source's bound \(C(e^2+YA_4^2)\) is correctly normalized and
uses only the carrier RMS. Replacing \(A_4^2\) by \(e^2\) without another
assumption is unjustified. The always-valid inequality is
\[
A_4^2\le n^{-1/2}\sum_i\|\Delta A_{i,:}\|_2^2
\le\sqrt n e^2.
\]

## 2. Exact energy identity

Write \(d_a=\widehat f_a-f_{D,a}\), and let the source's remainders be
\[
R_{0,a}=d_a-Df_a(\theta_D)[\Delta\theta],\qquad
R_{1,a}=Df_a(\widehat\theta)[\Delta\theta]-d_a.
\]
For \(F_a(s)=f_a(\theta_s)\), direct integration gives
\[
R_{0,a}=\int_0^1(1-s)F_a''(s)ds,\qquad
R_{1,a}=\int_0^1sF_a''(s)ds.
\]
Gradient flow in the mobility inner product and the fact that only the hidden
matrix defect is nonzero imply
\[
\begin{aligned}
\frac12(e^2)'&=
-\frac2m\sum_a\widehat r_a(d_a+R_{1,a})
+\frac2m\sum_a r_{D,a}(d_a-R_{0,a})
+\langle\Delta W,E_2\rangle_F\\
&=-2\|d\|_m^2
-\frac2m\sum_a(\widehat r_aR_{1,a}+r_{D,a}R_{0,a})
+\langle\Delta W,E_2\rangle_F.
\end{aligned}
\]
This verifies source equation (10), with both signs and both residuals at
their actual trajectory endpoints. Weighted sample Cauchy--Schwarz and the
Hessian bound give its equation (11). No residual on the straight parameter
segment is substituted, and the damping term is nonpositive with the claimed
coefficient.

## 3. Integrating factor, including zero discrepancy

Define \(A_4^2/e^2=0\) where \(e=0\). This definition causes no loss:
then \(\Delta\theta=0\), so \(A_4=0\). Let
\[
a(t)=C(\rho_D(t)+\widehat\rho(t))
\left(1+Y\frac{A_4(t)^2}{e(t)^2}\right),
\qquad b(t)=\|E_2(t)\|_F.
\]
At each fixed width,
\(a(t)\le C(\rho_D+\widehat\rho)(1+Y\sqrt n)\), so \(a\) is
integrable by the supplied fitting theorem. Equation (11) gives
\(\tfrac12(e^2)'\le ae^2+eb\). To handle all zero crossings, set
\(e_\varepsilon=(e^2+\varepsilon^2)^{1/2}\). Then almost everywhere
\[
e_\varepsilon'\le a e_\varepsilon+b,
\qquad e_\varepsilon(0)=\varepsilon.
\]
Multiplying by \(\exp(-\int_0^t a)\), integrating, and taking
\(\varepsilon\downarrow0\) proves
\[
\sup_t e(t)\le
\exp\left(\int_0^\infty a(t)dt\right)
\int_0^\infty b(t)dt.
\]
The source's quantity
\(K_{n,q}=\int_0^\infty Y(\rho_D+\widehat\rho)A_4^2/e^2\,dt\)
therefore gives exactly
\[
\sup_t d_n(\widehat\theta,\theta_D)
\le C\exp(CY+CK_{n,q})\epsilon_q,
\]
using \(d_n\le\sqrt3 e\). This also checks that the deterministic bound
is meaningful before assuming a width-uniform bound on \(K_{n,q}\).

## 4. Order schedule, probability, and scope

For
\(q_n=\lceil n^{1/4}[\log(e+n)]^{1/4}\rceil\), one has
\(q_n=o(n)\), \(q_n^2\ge n^{1/2}[\log(e+n)]^{1/2}\), and
\(\log(e+q_n)\le C\log(e+n)\). Hence
\[
q_n^{-2}\sqrt{\log(e+q_n)}\le Cn^{-1/2}.
\]
Combining the supplied source estimate with a width-uniform high-probability
bound on \(K_{n,q_n}\) proves the claimed strict root-width parameter
tracking. The known forward comparison then transfers it to the stated
whole-input observables. No population discrepancy is added. The evolving
state count and unchanged quadratic fixed mixer storage are correctly stated.

The source correctly distinguishes its assumptions from proved facts:
neither row-spread control nor the weighted expectation of \(K_{n,q_n}\)
is established. Exchangeability, bounded RMS, low matrix rank, and temporal
projection orthogonality do not imply those assertions. Its localized
rank-one example verifies this limitation without claiming to be a reachable
Gaussian training path.

One scope clarification would improve presentation: “general input geometry”
still retains the manuscript's positive initial readout-feature-Gram
hypothesis and corresponding high-probability event \(\mathcal G_n\).
The conditional statement already enforces this through its equation (16),
so it is mathematically correct. It should not be read as covering every
normalized dataset with inconsistent duplicate or antipodal labels; for such
data the full Gram event can be empty and the original residual need not
decay. This is an applicability qualification, not a flaw in the conditional
energy theorem.
