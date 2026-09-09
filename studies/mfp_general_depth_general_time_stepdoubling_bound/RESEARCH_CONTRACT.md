# Research contract: general-time step doubling

## Canonical model and limit order

Use exactly the depth-\(L\), width-\(n\), scalar-input network and the
recomputed mean-field gradient-ascent update from the audited
four-versus-two study.  For each fixed integer \(k\ge1\) and each fixed
nonzero step \(h\), first prove and take

\[
 F_{k,L}(h)=\lim_{n\to\infty}\mathbb E f_{n,L}^{k}(h).
\]

Only after this pointwise width limit may \(h\to0\) be studied.  No
finite-width learning-rate jet may be passed through the width limit.

Assume

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,
\]

\[
 M_\phi=\max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty.
\]

The constant-activation case remains a separate exact branch.

## Target discrepancy and sharp quantifiers

For integers \(t,L\ge1\), define

\[
 \Delta_{t,L}(\eta)=F_{2t,L}(\eta)-F_{t,L}(2\eta).
\]

The strongest intended theorem has activation/depth quantities
\(\kappa_{\phi,L},B_{\phi,L},h_{\phi,L}\), computable solely from Gaussian
activation integrals or a stated weighted derivative envelope, such that

\[
 \left|\Delta_{t,L}(\eta)
 -t(2t-1)\kappa_{\phi,L}\eta^3\right|
 \le B_{\phi,L}\,P_4(t)|\eta|^5                       \tag{C.1}
\]

for every integer \(t\ge1\) and

\[
 |\eta|\le \frac{h_{\phi,L}}{t}.                       \tag{C.2}
\]

Here \(P_4\) must be an explicit nonnegative polynomial of degree at most
four.  The depth dependence in \(\kappa_{\phi,L},B_{\phi,L},h_{\phi,L}\)
must itself be explicit, preferably as powers of activation-only bases.
No hidden constant may depend on \(t\), an output trajectory, or an
unknown continuity modulus.

The normalization in (C.1) is chosen so that
\(\kappa_{\phi,L}=\kappa_{21,\phi,L}\) if the expected temporal
intertwining is valid.

## Required bridges

1. Pointwise fixed-step identification of the actual finite-width network
   with the horizon-\(2t\) inverse-free Gaussian DAG for every fixed
   \((t,L)\).
2. Singular-covariance \(C^5\) regularity after the width limit.
3. A complete enlarged marked-history response-functor intertwining
   through order three, including every differentiated \(\rho\)- and
   \(\sigma\)-response and its binomial convolution.
4. The exact quadratic cubic coefficient
   \(t(2t-1)\kappa_{\phi,L}\), reduced to Gaussian activation integrals.
5. A coupled step-doubling fifth-order estimate.  Bounding
   \(F_{2t}^{(5)}\) and \(F_t^{(5)}\) separately by \(O(t^5)\) is
   insufficient; the proof must expose the cancellation yielding
   \(P_4(t)=O(t^4)\).
6. An explicit activation/depth envelope valid on the total-time window
   \(|t\eta|\le h_{\phi,L}\).
7. Independent hostile reconstruction of every bridge.

## Forbidden substitutions

- No easier architecture, frozen-feature dynamics, or altered optimizer.
- No reversal of the width-first limit order.
- No coefficient defined as an unknown output derivative.
- No output-derived supremum, trajectory modulus, or existential radius.
- No unproved dynamic-cavity, state-evolution, marked-response, or
  modified-equation theorem.
- No separate fifth-derivative triangle bound advertised as an
  \(O(t^4)\) coupled remainder.
- No fixed-\(t\) statement presented as uniform in \(t\).

## Terminal outcomes

The study ends with either (i) a proof of (C.1)--(C.2) surviving
independent audits, or (ii) the strongest audited fixed-\((t,L)\) theorem
together with an exact statement of every missing bridge.  A conditional
Euler-algebra formula is not a proof of the width-first theorem.
