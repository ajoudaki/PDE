# Raw-sine depth-2 derivatives through order five: frozen protocol

## Canonical model

Fix one input, two hidden layers of equal width \(n\), standard Gaussian
initialization, input Gram one, and the raw activation

\[
\phi(x)=\sin x
\]

at both hidden layers.  Write

\[
X_j=\sin U_j,
\qquad
Z_i=\frac1{\sqrt n}\sum_jW_{ij}X_j,
\qquad
f_n=\frac1n\sum_iA_i\sin Z_i.
\]

All three parameter blocks \((A,W,U)\) train with unit Euclidean metric,

\[
D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad
F^{(r)}(0)=\lim_{n\to\infty}D_n^rf_n.
\]

The limit is width first at each fixed order.  No normalization of \(\sin x\),
unit-Gram quotient, frozen-feature substitution, or finite-width
extrapolation is allowed.  In particular, the second hidden preactivation has
variance

\[
Q_1=E[\sin^2G]=\frac{1-e^{-2}}2,
\qquad G\sim N(0,1).
\]

## Scope

Compute the complete jet through order five:

\[
F(0),F'(0),F''(0),F^{(3)}(0),F^{(4)}(0),F^{(5)}(0).
\]

This is the first three potentially nonzero derivatives.  Readout reflection
must give exact zeros at orders zero, two, and four.  Orders seven and nine
are outside the frozen scope because the currently audited
activation-generic normal form stops at order five.

## Evaluation routes

The order-five Gaussian program has already eliminated every auxiliary
Gaussian and retained only one-dimensional atoms

\[
E_{G\sim N(0,Q_\ell)}
\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.
\]

For sine, each atom is a finite Fourier sum because

\[
\phi^{(r)}(x)=\sin(x+r\pi/2).
\]

If the product has Fourier coefficients \(c_m\), then

\[
E[e^{imG}]=e^{-m^2Q_\ell/2},
\qquad
E\prod_r\phi^{(r)}(G)^{\nu_r}
=\sum_m c_m e^{-m^2Q_\ell/2}.
\]

Thus no polynomial or Hermite truncation of the activation is used.

Two independently frozen coefficient representations must agree:

1. the primary dependency-first arithmetic DAG
   `LAYER_SEPARATED_ABC_NORMAL_FORM.txt`, SHA-256
   `5219b3558aec52a2065b93ba7d6ce0e350ee930c2048518fcd012ba61f605ec9`;
2. the independent expanded layer-tagged coefficient map
   `independent_layer_tagged_coefficient_map.json`, SHA-256
   `52832afc4f9e1cf27f5b8465f2f5373bcb3e9f5c56b0686c9366162da2e17c11`.

Both are evaluated by closed finite Fourier sums at 80 and 120 decimal
digits.  As an evaluator-level control, Gauss--Hermite quadrature at orders 64
and 96 must reproduce the Fourier values within \(10^{-10}\) for
\(F'(0),F^{(3)}(0)\) and within \(10^{-7}\) for \(F^{(5)}(0)\).

## Frozen validation gates

1. The earlier audited raw-sine values are reproduced:

   \[
   F'(0)=1,
   \qquad
   F^{(3)}(0)=-1.88699982730593\ldots.
   \]

2. The primary and independent order-five maps agree to at least 60 decimal
   digits at every nonzero derivative.
3. Repeating the finite-Fourier evaluation at 80 and 120 digits changes no
   reported 60-digit prefix.
4. The two quadrature orders satisfy the frozen tolerances.
5. Orders zero, two, and four vanish exactly by readout parity.

A failed gate makes the computation inconclusive rather than changing an
accepted lower-order result.

## Resource and claim boundary

- Maximum derivative order: five.
- Hard audit bound: 60 seconds and 2 GiB.
- The result concerns formal width-first derivatives only.  It does not imply
  convergence of the Taylor series, positive-time existence, a Stieltjes
  representation, or equal efficiency at arbitrarily high order.
