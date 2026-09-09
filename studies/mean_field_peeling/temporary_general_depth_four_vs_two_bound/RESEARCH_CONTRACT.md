# Research contract: four fine steps versus two coarse steps

## Canonical object

Fix a hidden depth \(L\ge1\), common hidden width \(n\), scalar input
\(1\), no biases, and activation \(\phi\).  At training time \(s\),

\[
 Z_1^s=u^s,\qquad X_1^s=\phi(Z_1^s),
\]

\[
 Z_\ell^s=\frac{W_\ell^sX_{\ell-1}^s}{\sqrt n},\qquad
 X_\ell^s=\phi(Z_\ell^s),\qquad 2\le\ell\le L,
\]

\[
 f_{n,L}^s=\frac1n(a^s)^TX_L^s.
\]

All entries of \(u^0,a^0,W_2^0,\ldots,W_L^0\) are mutually independent
standard Gaussians.  One recomputed ascent step of size \(h\) is exactly

\[
 \theta^{s+1}=\theta^s+hn\nabla f_{n,L}(\theta^s).
\]

Equivalently, with the usual cotangents \(D_\ell^s\),

\[
 a^{s+1}=a^s+hX_L^s,\qquad
 W_\ell^{s+1}=W_\ell^s+\frac h{\sqrt n}
 D_\ell^s(X_{\ell-1}^s)^T,
 \qquad Z_1^{s+1}=Z_1^s+hD_1^s.
\]

## Admissible activation class

Let \(G\sim N(0,1)\).  Assume

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,
\]

and

\[
 M_\phi=\max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty.
\]

The constant-activation case is an explicit separate branch.

## Observable, horizon, and limit order

For each fixed nonzero \(h\), define—only after proving existence—

\[
 F_{k,L}(h)=\lim_{n\to\infty}\mathbb E f_{n,L}^k(h).
\]

The target discrepancy is

\[
 \Delta_{42,L}(\eta)=F_{4,L}(\eta)-F_{2,L}(2\eta).
\]

The order of operations is inviolable:

\[
 n\to\infty\quad\text{at each fixed nonzero step},
 \qquad\text{then}\qquad \eta\to0.
\]

No finite-width Taylor coefficient may be passed through the width limit.

## Sharp target

Construct from activation data and finite Gaussian integration:

\[
 \kappa_{42,\phi,L},\qquad
 B_{\phi,42}(L)<\infty,\qquad h_{\phi,42}(L)>0,
\]

with completely explicit depth dependence, such that

\[
 |\Delta_{42,L}(\eta)-\kappa_{42,\phi,L}\eta^3|
 \le B_{\phi,42}(L)|\eta|^5,
 \qquad |\eta|\le h_{\phi,42}(L).
\]

The ideal separated form is

\[
 B_{\phi,42}(L)=G_4^{A_4(L)}b_\phi^{E_4(L)},\qquad
 h_{\phi,42}(L)=c_4G_4^{-a_4(L)}b_\phi^{-e_4(L)},
\]

where \(b_\phi\) is activation-only and
\(G_4,c_4,A_4,E_4,a_4,e_4\) are explicit numerical/depth quantities.
A completely specified terminating recursion is acceptable.

The coefficient must be a terminating nodewise Gaussian Price recursion.
Any relation to the audited two-versus-one coefficient must be proved by
an intertwining identity, not asserted from finite-width jets.

## Required bridges

1. Exact \(9(L-1)\)-action finite-width chronology through time four.
2. Adaptive row/column Gaussian conditioning with every reused-matrix
   response and empirical overlap included.
3. Pointwise fixed-step convergence and uniform integrability of the
   expected terminal output.
4. Positivity of every population time-history Gram actually inverted,
   with an explicit admissible step interval.
5. An inverse-free population DAG defined independently at coalesced
   covariance.
6. Singular-covariance \(C^5\) regularity from activation envelopes.
7. A nodewise Gaussian-integral cubic coefficient and activation-only
   fifth-derivative majorant with explicit depth factors.
8. Independent reconstruction and hostile audits of all preceding bridges.

## Forbidden substitutions and non-vacuity rules

- No abstract Gaussian program may replace the actual finite-width model.
- No output-derived supremum, continuity modulus, trained trajectory, or
  unknown limiting derivative may define a constant or radius.
- No unproved dynamic-cavity/state-evolution theorem may be invoked.
- No rank assertion may be inferred from a lower-order Gram.
- No easier architecture, frozen-feature model, or altered optimizer may
  replace the stated network.
- A fixed-\(L\), fixed-horizon theorem is not a uniform-in-time theorem.

## Claim ladder and terminal outcomes

- A: exact finite chronology and inverse-free DAG;
- B: internal \(C^5\) regularity and finite envelope compiler;
- E: identification of that DAG with the actual width-first limit;
- F: the displayed local quantitative comparison for every fixed \(L\).

The task terminates only with either a proof surviving independent audit or
an exact open/conditional statement naming every missing bridge.

## Authorization

The user authorized new theoretical analysis, new files inside this MFP
study, delegated proof search, and independent adversarial audits.  No
numerical experiment or external literature search is needed or authorized
for the central proof.
