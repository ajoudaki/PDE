# Unconditional theorem at every fixed integer time

This is the strongest result currently obtained without a
horizon-uniform response-state theorem.  It preserves the width-first
limit order but its constants are not polynomial in \(t\).

## Theorem

Fix integers \(t,L\ge1\), put \(T=2t\), and assume the exact network and
weighted \(C^{12}\) activation class in `RESEARCH_CONTRACT.md`.  Define

\[
 D_T=2T+1,
\]

\[
 b_{T,0}=16,\qquad
 b_{T,s+1}=64(T+2)^2(b_{T,s}+1)^2,\qquad0\le s<T,    \tag{1.1}
\]

\[
 s_T=8(b_{T,T}+1),\qquad
 A_T^{\rm op}=64(1+D_T^{10}+32D_T^2),                 \tag{1.2}
\]

\[
 c_{T,0}=\max\{128,s_T\},\qquad
 c_{T,r+1}=A_T^{\rm op}(c_{T,r}+1)^2,\qquad0\le r<24,\tag{1.3}
\]

\[
 C_T=c_{T,24},\qquad q_T=2C_T.                        \tag{1.4}
\]

For

\[
 \mu_{D,p}(v)=\sum_{r=0}^p{p\choose r}v^{r/2}2^{r/2}
 \frac{\Gamma((D+r)/2)}{\Gamma(D/2)},                 \tag{1.5}
\]

put

\[
 g_T=2^{C_T}\mu_{D_T,C_T}(D_T^2C_T^2),\qquad
 b_\phi=\max\{2,M_\phi\}.                            \tag{1.6}
\]

The horizon-\(T\) call count and solved envelope exponents are

\[
 N_{T,L}=(2T-1)L-2T+2,                                \tag{1.7}
\]

\[
 A_{T,L}=\frac{q_T^{N_{T,L}}-1}{q_T-1},\qquad
 E_{T,L}=2Lq_T^{N_{T,L}}+C_TA_{T,L}.                  \tag{1.8}
\]

Define the explicit activation/depth/horizon envelope

\[
 \mathcal S_{T,L}=g_T^{A_{T,L}}b_\phi^{E_{T,L}}.       \tag{1.9}
\]

For the two horizons used below, put

\[
 \overline{\mathcal S}_{t,L}
 =\max\{\mathcal S_{t,L},\mathcal S_{2t,L}\}.          \tag{1.9a}
\]

Let \(\kappa_{\phi,L}=2H_L+\frac12S_L\) be the terminating marked
Gaussian coefficient construction of CUBIC_MARKED_BRIDGE.md.  Let
\(\mathcal J_3(F_{k,L})\) be the direct signed Price recursion of the
horizon-\(T\) inverse-free Gaussian DAG, evaluated at the coalesced
covariance; by definition it returns the third signed jet
\(F_{k,L}^{(3)}(0)\).  The marked temporal law proves

\[
 \kappa^{\rm dir}_{t,\phi,L}
 =\frac{\mathcal J_3(F_{2t,L})
 -8\mathcal J_3(F_{t,L})}{6}
 =t(2t-1)\kappa_{\phi,L}.                              \tag{1.10}
\]

Then the pointwise width limits \(F_{2t,L}(\eta)\) and
\(F_{t,L}(2\eta)\) exist for every fixed nonzero \(\eta\) satisfying

\[
 |\eta|\le h^{\rm fix}_{t,\phi,L}
 :=\frac1{8t\sqrt{\overline{\mathcal S}_{t,L}}}.        \tag{1.11}
\]

After taking those width limits,

\[
 \boxed{
 \left|F_{2t,L}(\eta)-F_{t,L}(2\eta)
 -t(2t-1)\kappa_{\phi,L}\eta^3\right|
 \le\overline{\mathcal S}_{t,L}|\eta|^5.}              \tag{1.12}
\]

The coefficient (1.10) is a terminating expression in finite Gaussian
activation integrals, not an output-derived derivative.

## Proof

For a horizon \(T\), the exact finite-width chronology consists of \(T\)
forward/backward sweeps and one terminal forward sweep, hence
\((2T+1)(L-1)\) predictable reused-matrix actions.
GENERAL_FIXED_H_IDENTIFICATION.md gives the parameterized action list,
inverse-free population DAG, arbitrary-horizon rank proof, compatible
ideal arrays, action-indexed good events, concentration induction, raw
exceptional-event bound, and terminal uniform integrability.  It gives
all feature Grams through time \(T\) and cotangent Grams through time
\(T-1\) on

\[
 0<|h|\le\frac1{2T\sqrt{\mathcal S_{T,L}}}.            \tag{2.1}
\]

It therefore identifies the expected finite-width output with the
inverse-free DAG at each fixed nonzero \(h\) in (2.1).  No learning-rate
derivative is used in this step.

The signed and absolute Price recursions are also stated for arbitrary
fixed \(T\).  The call count is (1.7), and solving the one-call envelope
recurrence gives exactly (1.9).  Thus both terminal outputs are \(C^5\) at
the singular covariance and their fifth derivatives are bounded by
\(\mathcal S_{T,L}\) on the compiler interval.

The sign involution makes every \(F_{k,L}\) odd.  Moreover

\[
 F_{k,L}'(0)=k\sum_{j=0}^Ld^j,\qquad
 d=\mathbb E\phi'(G)^2.                               \tag{2.2}
\]

Therefore the constant, linear, quadratic, and quartic coefficients of
\(F_{2t,L}(\eta)-F_{t,L}(2\eta)\) vanish, while (1.10) is its cubic
coefficient by CUBIC_MARKED_BRIDGE.md.  Taylor's integral remainder gives

\[
 \begin{aligned}
 &|F_{2t,L}(\eta)-F_{t,L}(2\eta)
 -t(2t-1)\kappa_{\phi,L}\eta^3|\\
 &\quad\le\frac{\mathcal S_{2t,L}+2^5\mathcal S_{t,L}}{120}
 |\eta|^5
 \le\overline{\mathcal S}_{t,L}|\eta|^5.             \tag{2.3}
 \end{aligned}
\]

The radius (1.11) puts the fine step \(\eta\) and, conservatively, the
coarse step \(2\eta\) inside their respective instances of (2.1) and
inside \(|h|\le1\).  This proves (1.12).  If
\(\phi\equiv\pm1\), both sides of the discrepancy vanish exactly.

## Limitation

The quantities \(C_T,g_T,q_T\), and hence
\(\overline{\mathcal S}_{t,L}\), grow much faster than a polynomial in
\(T=2t\).  Thus (1.12) is a theorem for every
fixed \(t\), but it does not prove the requested uniform quadratic/quartic
general-time law on a total-time window.
