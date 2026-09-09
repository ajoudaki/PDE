# Uniform near-identity OMFP remainder: frozen contract

Date: 25 August 2026.

## Canonical target

Use the already proved pointwise fixed-step, width-first OMFP DAG for the
same scalar-input, two-hidden-layer, mean-field feature-ascent network.  For
each fixed finite schedule, take width to infinity first.  Only the resulting
population DAG may subsequently be differentiated in the common step or
studied as the number of steps grows.

For

\[
 \psi_\alpha(x)=
 \frac{x+\alpha\varphi(x)}{\|G+\alpha\varphi(G)\|_2},
 \qquad
 \|\varphi^{(r)}\|_\infty\le MA^r r!,
 \qquad \varphi''\not\equiv0,
\]

and

\[
 \Delta_t(\eta)=F_{2t}(\eta)-F_t(2\eta),
\]

the requested theorem is the existence of explicitly computable
\(\alpha_0,\rho,C>0\), depending only on \((M,A)\) and numerical Gaussian
constants, such that

\[
 |\Delta_t(\eta)-\kappa_t\eta^3|
 \le Ct^4|\eta|^5
\]

for every integer \(t\ge1\), every \(0<|\alpha|\le\alpha_0\), and every
\(|\eta|\le\rho/t\).

## Required proof architecture

The requested witness is a single reachable-source norm

\[
 \|V\|_{\mathfrak X}
 =\sum_{m\ge0}w_m\|\mathcal D^mV\|_{p_m},
\]

with positive explicit weights and ordinary finite-moment norms, together
with quantitative same-space closure under the exact network operations.
In particular, the proof must establish, rather than assume, a same-space
one-step tangent estimate with multiplier \(1+C_0|\eta|\).

## Non-resolutions

The following do not prove the target: fixed-horizon continuity in
\(\alpha\); a finite source ledger; ambient Fréchet smoothness on an
\(L^2\)-ball; independent Taylor bounds for the two outputs; finite-width
Taylor expansion; output-defined constants; or a Banach/analytic norm whose
closure estimate is itself equivalent to the desired stability theorem.

## Terminal outcomes

1. A complete proof with explicit constants which survives independent and
   adversarial reconstruction; or
2. a rigorous contradiction showing that the requested theorem or required
   norm architecture cannot hold as stated.  Failure of this particular
   norm architecture does not by itself falsify the scalar remainder
   conjecture; those claim levels must remain separate.

