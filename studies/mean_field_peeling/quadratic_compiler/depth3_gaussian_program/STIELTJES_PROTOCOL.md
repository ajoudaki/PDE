# Depth-3 order-nine Stieltjes audit: frozen protocol

## Canonical object and convention

Use only the accepted raw-quadratic, equal-width, three-hidden-layer feature
jet in `results_order9.json`, with

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

No unit-Gram normalization, depth-2 coefficient, activation rescaling,
finite-width extrapolation, or positive-time interpretation is admissible.
The limit remains width first at each fixed derivative order.

## Available information and stopping rule

The odd derivatives through (F^{(9)}(0)) determine exactly
(\mu_0,\mu_1,\mu_2,\mu_3).  Stop there.  In particular:

- (\mu_4) requires (F^{(11)}(0));
- the ordinary (3\times3) matrix (H_2) requires (\mu_4);
- the shifted (3\times3) matrix (H_2^+) requires (\mu_5), hence
  (F^{(13)}(0)).

No unavailable entry will be estimated, bounded, or inferred from a trend.

## Exact decision objects

For a Stieltjes moment sequence, every ordinary and shifted Hankel matrix

\[
H_d=(\mu_{i+j})_{i,j=0}^d,
\qquad
H_d^+=(\mu_{i+j+1})_{i,j=0}^d
\]

must be positive semidefinite.  The complete accessible list is

\[
H_0=[\mu_0],
\quad H_0^+=[\mu_1],
\quad
H_1=\begin{pmatrix}\mu_0&\mu_1\\\mu_1&\mu_2\end{pmatrix},
\quad
H_1^+=\begin{pmatrix}\mu_1&\mu_2\\\mu_2&\mu_3\end{pmatrix}.
\]

Every nonempty principal minor of each accessible matrix will be evaluated
in exact rational arithmetic.  Thus the explicit scalar checks are

\[
\mu_0,\mu_1,\mu_2,\mu_3\ge0,
\qquad
\Delta_1=\mu_0\mu_2-\mu_1^2\ge0,
\qquad
\Delta_1^+=\mu_1\mu_3-\mu_2^2\ge0.
\]

Strict positivity of both leading principal minors of a (2\times2)
symmetric matrix certifies positive definiteness by Sylvester's criterion.

## Competing outcomes and gates

- **Compatible outcome:** all accessible principal minors are nonnegative.
  Strictly positive minors classify all four matrices as positive definite.
- **Violation:** at least one exact principal minor is negative.  Its
  corresponding polynomial vector is a finite-order Stieltjes
  counter-witness for this depth-3 jet.
- **Inconclusive computation:** the two moment transformations disagree, an
  input SHA-256 gate fails, an even-power/parity gate fails, or exact
  arithmetic does not terminate inside 60 seconds and 512 MiB.

Moment route A performs direct exact series reversion and composition.
Moment route B solves the triangular identity (F'(t)=K(F(t))) coefficient
by coefficient without constructing (F^{-1}).  They must agree exactly.

## Claim boundary

Passing proves only compatibility with every Stieltjes Hankel condition
decidable from (F^{(9)}(0)).  It does not prove the all-order conjecture,
existence of a representing measure for the full unknown sequence,
convergence of the formal series, or identification with a positive-time
mean-field trajectory.
