# Identity depth-2/depth-3 order-eleven Stieltjes audit: frozen protocol

## Canonical object and convention

Use only the accepted exact derivatives in `RESULTS.json` for the raw
identity activation, equal hidden widths, one input of Gram one, independent
standard-Gaussian initialization, unit metric on every parameter block, and
the width-first limit at each fixed derivative order.  The input SHA-256 is

`6acac5edc920a02b68ea0d0f53f9fac675cacdca5a750309b51654b8fc1d19c3`.

For each hidden depth \(H\in\{2,3\}\), use the project convention

\[
 K_H(y)=F_H'\!\left(F_H^{-1}(y)\right)
 =F_H'(0)+\sum_{r\ge0}(-1)^r\mu_{r,H}y^{2r+2}.
\]

Equivalently,

\[
 {K_H(\sqrt{x})-F_H'(0)\over x}
 =\sum_{r\ge0}(-1)^r\mu_{r,H}x^r.
\]

No finite-width extrapolation, activation/depth substitution, or
positive-time interpretation is admissible.

## Available information and stopping rule

The exact odd feature derivatives through \(F_H^{(11)}(0)\) determine exactly

\[
 \mu_{0,H},\mu_{1,H},\mu_{2,H},\mu_{3,H},\mu_{4,H}.
\]

Stop there.  In particular, \(\mu_{5,H}\) and the shifted matrix
\(H_{2,H}^+\) require \(F_H^{(13)}(0)\) and will not be estimated.

Two exact moment transformations must agree:

1. rational series reversion followed by composition;
2. the triangular coefficient identity \(F_H'(t)=K_H(F_H(t))\).

## Complete accessible PSD audit

For a Stieltjes moment sequence, every ordinary and shifted Hankel matrix

\[
 H_d=(\mu_{i+j})_{i,j=0}^d,
 \qquad H_d^+=(\mu_{i+j+1})_{i,j=0}^d
\]

is positive semidefinite.  The complete matrices determined by five moments
are

\[
 H_0,\ H_1,\ H_2,\ H_0^+,\ H_1^+.
\]

Every nonempty principal minor of all five matrices will be evaluated in
exact rational arithmetic.  After removing duplicates, the ten distinct PSD
inequalities are the five moment signs,

\[
 \mu_0,\mu_1,\mu_2,\mu_3,\mu_4\ge0,
\]

the four distinct principal \(2\times2\) inequalities,

\[
\begin{aligned}
 \mu_0\mu_2-\mu_1^2&\ge0,&
 \mu_1\mu_3-\mu_2^2&\ge0,\\
 \mu_0\mu_4-\mu_2^2&\ge0,&
 \mu_2\mu_4-\mu_3^2&\ge0,
\end{aligned}
\]

and

\[
 \det H_2\ge0.
\]

## Complete accessible Hankel total-positivity diagnostics

For completeness, enumerate every distinct square minor of the infinite
Hankel array whose entries require no moment beyond \(\mu_4\).  In addition
to the PSD principal minors above, the three distinct cross minors are

\[
\begin{aligned}
 \mu_0\mu_3-\mu_1\mu_2&\ge0,\\
 \mu_0\mu_4-\mu_1\mu_3&\ge0,\\
 \mu_1\mu_4-\mu_2\mu_3&\ge0.
\end{aligned}
\]

Thus all five moment signs, all seven distinct accessible \(2\times2\)
Hankel minors, and the single accessible \(3\times3\) determinant are
reported.

## Decision rule and validity gates

- **Finite-order compatible:** all accessible principal minors are
  nonnegative.  If every one is strictly positive, all five accessible
  matrices are positive definite.
- **Finite-order violation:** at least one exact principal minor is negative.
- **Inconclusive computation:** the two moment transformations disagree, an
  input/parity gate fails, or the audit exceeds 60 seconds or 512 MiB.

The three cross-minor signs are reported separately as stronger
total-positivity diagnostics.

## Claim boundary

Passing means compatibility with every Stieltjes/Hankel condition decidable
from the order-eleven identity jets.  It does not prove that an unknown
infinite continuation is a Stieltjes moment sequence, construct a representing
measure, establish convergence of the formal series, or imply positive-time
mean-field dynamics.
