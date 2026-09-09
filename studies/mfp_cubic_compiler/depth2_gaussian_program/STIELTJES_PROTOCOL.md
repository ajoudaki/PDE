# Raw-cubic depth-2 order-nine Stieltjes audit: frozen protocol

## Canonical object and convention

Use only the accepted raw-cubic, equal-width, two-hidden-layer feature jet in
`results_order9.json`, with

\[
K(y)=F'\!\left(F^{-1}(y)\right),
\qquad
K(y)=F'(0)+\sum_{r\ge0}(-1)^r\mu_r y^{2r+2}.
\]

Equivalently,

\[
R(x)=\frac{K(\sqrt{x})-F'(0)}{x}
=\sum_{r\ge0}(-1)^r\mu_r x^r.
\]

The model remains the raw activation \(x^3\), standard Gaussian
initialization, input Gram one, unit metric on all parameter blocks, and the
width-first limit at every fixed derivative order.  No activation
normalization, depth substitution, finite-width extrapolation, or
positive-time interpretation is admissible.

The frozen derivative input has SHA-256
`6ef10c12960929bc95437eb44407b8e84c6b4e4f3b10b4e8416ad8666bd56979`.

## Available information and stopping rule

The odd derivatives through \(F^{(9)}(0)\) determine exactly
\(\mu_0,\mu_1,\mu_2,\mu_3\).  Stop there:

- \(\mu_4\) and the ordinary \(3\times3\) matrix \(H_2\) require
  \(F^{(11)}(0)\);
- \(\mu_5\) and the shifted \(3\times3\) matrix \(H_2^+\) require
  \(F^{(13)}(0)\).

No unavailable moment or matrix entry will be estimated from a trend.

## Exact Stieltjes decision objects

For a Stieltjes moment sequence, every ordinary and shifted Hankel matrix

\[
H_d=(\mu_{i+j})_{i,j=0}^d,
\qquad
H_d^+=(\mu_{i+j+1})_{i,j=0}^d
\]

must be positive semidefinite.  The complete accessible list is

\[
H_0=[\mu_0],
\qquad
H_0^+=[\mu_1],
\]

\[
H_1=\begin{pmatrix}\mu_0&\mu_1\\\mu_1&\mu_2\end{pmatrix},
\qquad
H_1^+=\begin{pmatrix}\mu_1&\mu_2\\\mu_2&\mu_3\end{pmatrix}.
\]

Every nonempty principal minor is evaluated in exact rational arithmetic.
The six unique scalar PSD conditions are therefore

\[
\mu_0,\mu_1,\mu_2,\mu_3\ge0,
\]

\[
\Delta_1=\mu_0\mu_2-\mu_1^2\ge0,
\qquad
\Delta_1^+=\mu_1\mu_3-\mu_2^2\ge0.
\]

For completeness, also evaluate the remaining distinct \(2\times2\) minor
of the accessible infinite Hankel corner,

\[
\Delta_{\rm cross}=\mu_0\mu_3-\mu_1\mu_2\ge0.
\]

This total-positivity check is redundant once the two consecutive Hankel
determinants and moment signs pass, but it is an additional exact diagnostic.

## Competing outcomes and numerical gates

- **Finite-order compatible:** every accessible principal minor is
  nonnegative.  Strict positivity classifies all four matrices as positive
  definite.
- **Finite-order violation:** at least one exact principal minor is negative;
  that minor is a finite-order counter-witness for the cubic jet.
- **Inconclusive computation:** either exact moment route disagrees, the
  input or source hash changes, the derivative parity gate fails, or the
  audit exceeds 60 seconds or 512 MiB.

Moment route A performs exact rational series reversion and composition.
Moment route B solves the triangular identity

\[
F'(t)=K(F(t))
\]

coefficient by coefficient without constructing \(F^{-1}\).  They must
agree exactly.

## Claim boundary

Passing establishes compatibility only with every Stieltjes/Hankel condition
decidable from the cubic jet through order nine.  It does not prove that the
unknown infinite sequence is a Stieltjes moment sequence, construct a measure
for all orders, establish formal-series convergence, or identify a
positive-time mean-field trajectory.
