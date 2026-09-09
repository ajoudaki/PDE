# Authoritative research state

## Proved result

For every fixed hidden depth \(L\ge1\) and every activation in the stated
weighted \(C^{12}\) class, first take the width limit at each fixed step.
Then

\[
 \left|F_{4,L}(\eta)-F_{2,L}(2\eta)
 -\kappa_{42,\phi,L}\eta^3\right|
 \le B_{\phi,42}(L)|\eta|^5
\]

for \(|\eta|\le h_{\phi,42}(L)\).  The authoritative proof is
`THEOREM.md`; `AUDIT.md` records three independent passes.

The coefficient is the terminating exact signed Gaussian Price recursion

\[
 \kappa_{42,\phi,L}
 =\frac{\mathcal J_3(F_{4,L})-8\mathcal J_3(F_{2,L})}{6}.
\]

It reduces at the coalesced covariance to finitely many one-dimensional
Gaussian integrals of \(\phi,\ldots,\phi^{(12)}\).  It is not defined via an
unknown output derivative.

## Explicit depth dependence

With the numerical horizon-four constants \(C_4,q_4,g_4\) in
`THEOREM.md`, let

\[
 N_{4,L}=7L-6,\qquad
 A_{4,L}=\frac{q_4^{N_{4,L}}-1}{q_4-1},
\]

\[
 E_{4,L}=2Lq_4^{N_{4,L}}+C_4A_{4,L},\qquad
 b_\phi=\max\{2,M_\phi\}.
\]

Then the audited explicit choice is

\[
 B_{\phi,42}(L)=g_4^{A_{4,L}}b_\phi^{E_{4,L}},\qquad
 h_{\phi,42}(L)=\frac1{16\sqrt{B_{\phi,42}(L)}}.
\]

At \(L=3\), \(N_{4,3}=15\),
\(A_{4,3}=(q_4^{15}-1)/(q_4-1)\), and
\(E_{4,3}=6q_4^{15}+C_4A_{4,3}\).

For every \(\varepsilon>0\), the proved corollary is

\[
 |F_{4,L}(\eta)-F_{2,L}(2\eta)|
 \le (|\kappa_{42,\phi,L}|+\varepsilon)|\eta|^3
\]

when

\[
 |\eta|\le
 \min\left\{h_{\phi,42}(L),
 \sqrt{\frac{\varepsilon}{1+B_{\phi,42}(L)}}\right\}.
\]

## Open sharpening

The identity

\[
 \kappa_{42,\phi,L}=6\kappa_{21,\phi,L}
\]

is compatible with the temporal Euler algebra and with the candidate
activation recursions, but it is open under the demanded standard.  The
missing bridge is a complete enlarged marked-history response-functor
intertwining at changing and singular Grams.  Two independent audits found
the same omission.  No proved statement above depends on it.

The compiler and rank argument are parameterized by an arbitrary fixed
horizon \(T\), which is the mechanism intended for a later general-time
theorem.  This research state makes no horizon-uniform or general-time
claim beyond the audited \(4\)-versus-\(2\) comparison.

