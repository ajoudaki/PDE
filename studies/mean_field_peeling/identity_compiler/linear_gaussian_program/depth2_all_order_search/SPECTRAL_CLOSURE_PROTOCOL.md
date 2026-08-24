# Depth-two identity spectral-closure audit

Status: frozen before the spectral recursion was evaluated, 20 August 2026.

## Independent route

Starting from the finite-width characteristic flow

\[
x'=By,\quad y'=B^Tx,\quad B'=xy^T,
\]

use the exact invariant `C=BB^T-xx^T` to derive

\[
x''=(C+\|x\|^2+\|y\|^2)x.
\]

At iid Gaussian initialization, norm balance gives a deterministic common
limit `r(t)=lim ||x(t)||^2=lim ||y(t)||^2`, and hence the scalar potential
is `2r(t)`.  The initial spectral measures relative to `x(0)` and
`x'(0)=B(0)y(0)` must be derived by a Wishart limit and a rank-one resolvent
identity, not fit from the accepted feature coefficients.

The resulting spectral fixed-point recursion is evaluated through the
coefficient needed for `F^(81)(0)`.  It must reproduce every exact derivative
and every output-kernel moment in `RESULTS.json`.  No coefficient from that
file may enter the spectral recursion itself.

Agreement proves an algebraically independent all-fixed-order *formal
closure*.  It does not by itself give an elementary closed form for `F` or
`K`, convergence at positive time, or all-order Stieltjes positivity.

