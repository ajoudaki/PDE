# Two-input cubic plus channel: frozen order-five Stieltjes protocol

## Canonical object and domain

Use the accepted exact symbolic derivatives in
`results_symbolic_order5.json` for the two-input, equal-label,
two-hidden-layer raw-cubic plus channel.  Put

\[
a(\rho)=F_+^{(1)}(0;\rho),\qquad
b(\rho)=F_+^{(3)}(0;\rho),\qquad
c(\rho)=F_+^{(5)}(0;\rho),
\]

with Gram domain \(-1\leq\rho\leq1\).  The endpoint \(\rho=-1\) is
degenerate because \(a(-1)=0\), so output-coordinate moments are defined
only on \(-1<\rho\leq1\).

Use the convention

\[
K_+(y;\rho)=F_+'(F_+^{-1}(y;\rho);\rho)
=a(\rho)+\sum_{r\geq0}(-1)^r\mu_r(\rho)y^{2r+2}.
\]

The accepted jet determines exactly

\[
\mu_0=\frac{b}{2a^2},\qquad
\mu_1=\frac{4b^2-ac}{24a^5}.
\]

It does not determine \(\mu_2\), which requires \(F_+^{(7)}(0;\rho)\).

## Decision question

Do all Stieltjes PSD conditions decidable from \(\mu_0,\mu_1\) have a
correlation-independent sign on the full nondegenerate domain?

- **Pass:** \(\mu_0(\rho)>0\) and \(\mu_1(\rho)>0\) for every
  \(-1<\rho\leq1\).
- **Fail:** either moment is negative at an exact admissible correlation.
- **Boundary:** an interior or nondegenerate endpoint zero is isolated
  exactly.
- **Inconclusive:** exact sign isolation cannot decide a numerator or
  denominator on the full domain.

## Exact gates

1. Parse the stored coefficient lists as exact rationals and reproduce all
   three requested specializations.
2. Derive the two moment formulas both by formal series reversion/composition
   and by the triangular identity \(F_+'(s)=K_+(F_+(s))\).
3. Factor every forced power of \(1+\rho\) before sign analysis.
4. Certify all remaining polynomial signs by exact factorization, Sturm root
   counts, or a positive Bernstein-coefficient certificate on \([-1,1]\).
5. Record exact values at \(\rho=0,1/2,1\).
6. Do not report \(\det H_1=\mu_0\mu_2-\mu_1^2\): it is unavailable without
   order seven.

## Budget and claim boundary

The exact symbolic audit has a two-minute and 2-GiB bound.  A pass proves
only order-five finite-prefix compatibility on the nondegenerate plus
channel.  It does not prove any higher Hankel condition, an all-order moment
sequence, a representing measure, series convergence, or a positive-time
mean-field trajectory.
