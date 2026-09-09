# Research state: general-time step doubling

## Requested theorem

For

\[
 \Delta_{t,L}(\eta)=F_{2t,L}(\eta)-F_{t,L}(2\eta),
\]

the sharp candidate is

\[
 \left|\Delta_{t,L}(\eta)
 -t(2t-1)\kappa_{\phi,L}\eta^3\right|
 \le B_{\phi,L}t^4|\eta|^5,
 \qquad |\eta|\le\frac{h_{\phi,L}}t.                  \tag{R.1}
\]

The powers \(t^2\) and \(t^4\) cannot in general be lowered.

## Proved

### Coupled abstract theorem

For any autonomous Euler population state whose mixed-schedule output
has

\[
 \sup_{\|\delta\|_1\le\rho}
 \|D_\delta^5\mathcal F_m\|_{(\ell^1)^5}\le Q
\]

uniformly in the schedule length, oddness gives

\[
 \left|\Delta_t(\eta)-[\eta^3]\Delta_t\,\eta^3\right|
 \le\frac83Qt^4|\eta|^5,\qquad2t|\eta|\le\rho.
                                                               \tag{R.2}
\]

The proof and a terminating Bell-polynomial construction of \(Q\) from
derivative envelopes are in ABSTRACT_STEP_DOUBLING.md.

### Actual one-hidden-layer network

For \(L=1\), (R.1) is unconditional with

\[
 B_{\phi,1}=\frac83Q_{\phi,1},\qquad
 h_{\phi,1}=\frac1{24M_\phi},
\]

where \(Q_{\phi,1}\) is the explicit two-Gaussian integral and finite
recursion in SCALAR_QUANTITATIVE_THEOREM.md.  Its coefficient is

\[
 \begin{aligned}
 \kappa_{\phi,1}
 ={}&\frac32\mathbb E[
 \phi'(G)^3\phi'''(G)+
 \phi(G)\phi'(G)^2\phi''(G)]\\
 &+2\mathbb E[
 \phi'(G)^4+\phi(G)^2\phi'(G)^2+
 2\phi(G)\phi'(G)^2\phi''(G)+
 3\phi'(G)^2\phi''(G)^2].
 \end{aligned}
                                                               \tag{R.3}
\]

### Exact cubic law at every depth

For every finite \(L,t\),

\[
 [\eta^3]\Delta_{t,L}
 =t(2t-1)\kappa_{\phi,L},                              \tag{R.4}
\]

where

\[
 \kappa_{\phi,L}=2H_L+\frac12S_L
\]

is defined by the terminating marked Gaussian compiler in
CUBIC_MARKED_BRIDGE.md.  The proof includes the full marked
\(\rho/\sigma\) convolutions, singular causal adjoint, substitution
naturality, and a lexicographic temporal-action-multiindex induction.
It was repaired after two adversarial objections and then passed both
re-audits.  The older compact nine-moment reduction is not claimed.

## Conditional sharp general-depth theorem

If the actual width-first reused-matrix DAG admits the restartable
population response state and the horizon-uniform schedule envelope
specified in SHARP_CONJECTURE.md, then

\[
 B_{\phi,L}=\frac83Q_{\phi,L},\qquad
 h_{\phi,L}=\frac{\rho_{\phi,L}}2
\]

give (R.1).  The coefficient is the already proved
\(\kappa_{\phi,L}\) in (R.4); only the uniform remainder bridge is
conditional.

## Current boundary

For \(L\ge2\), (R.1) is not yet an unconditional theorem.  The sole
remaining substantive bridge is a common restartable mixed-schedule
object with total-time Gram stability and a fifth schedule derivative
bound independent of the history length.  The fixed-\((t,L)\) theorem
is recorded separately in FIXED_T_THEOREM.md; it already has the exact
quadratic coefficient (R.4), but its explicit envelope grows
super-polynomially in \(t\) and therefore is not a substitute for
(R.1).
