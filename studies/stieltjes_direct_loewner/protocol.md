# Prespecified direct Loewner test

Frozen before inspecting any newly simulated observable values on 2026-08-12.

## Canonical simulation

Only the stated one-sample, two-hidden-layer quadratic feature-ascent system is used:

\[
z_i=n^{-1/2}\sum_jW_{ij}u_j^2,\qquad
f=n^{-1}\sum_i a_i z_i^2,
\]

\[
\dot a_i=z_i^2,\qquad
\dot W_{ij}=2n^{-1/2}a_i z_i u_j^2,\qquad
\dot u_j=4u_jn^{-1/2}\sum_i a_i z_iW_{ij}.
\]

All initial coordinates are independent standard Gaussians. The observable is

\[
K_n=n\lVert\nabla f\rVert_2^2
=\frac1n\sum_i z_i^4
+\frac4{n^2}\left(\sum_i a_i^2z_i^2\right)\left(\sum_j u_j^4\right)
+\frac{16}{n^2}\sum_j u_j^2\left(\sum_i a_i z_iW_{ij}\right)^2.
\]

Its infinite-width initial expectation is the stipulated value \(27+36+48=111\).

## Frozen design

- Evaluation points: \(x=(0.0004,0.0016,0.0036,0.0064)\), hence
  \(y=\sqrt x=(0.02,0.04,0.06,0.08)\).
- Widths: \(n=(64,128,256)\).
- Independent base seeds/antithetic pairs: respectively \((96,64,32)\).
- Seed base: `2026081201`. For common coupling, each seed first generates
  width-256 arrays and each smaller width takes their leading coordinates and
  leading principal matrix.
- Each base draw is simulated with both \(a(0)\) and \(-a(0)\), sharing
  \(W(0),u(0)\). Their average equals a forward/backward-time symmetrization
  and cancels finite-sample odd powers of \(y\).
- Primary integrator: fixed-step classical RK4 with \(h=0.001\); all output
  times are exact step endpoints.
- Numerical check: the first eight base seeds at each width are rerun with
  \(h=0.0005\).
- Each pair is centered by its own common \(K_n(0)\):
  \(R_{n,r}(x)=[K_{n,r}(\sqrt x)-K_{n,r}(0)]/x\). Thus the random finite-width
  offset from 111 is removed explicitly. The raw \(K_n(0)-111\) is retained.
- Loewner diagonals use an analytic directional derivative \(\dot K_n\), not
  a finite difference. With \(R'=\dot K/(2y^3)-[K(y)-K(0)]/y^4\),
  \(A_{ii}=-R'(x_i)\) and \(B_{ii}=R(x_i)+x_iR'(x_i)\).

## Frozen inference rule

For every width and each of \(A,B\), the first half of the base seeds is a
discovery sample. Its smallest-eigenvalue eigenvector is frozen. The second
half is the confirmation sample, on which the scalar quadratic form is tested.
A negative direction is called statistically confirmed only if its one-sided
Student-t upper confidence bound is below zero after Bonferroni correction at
familywise level 0.01 over the six width-by-matrix tests. Full-sample minimum
eigenvalues are descriptive only.

The numerical validity check compares primary and half-step matrices on the
same eight pairs. We report absolute and relative differences and their size
relative to the confirmation standard error. Nonfinite trajectories or a
step-size discrepancy comparable to statistical uncertainty make the result
inconclusive.

Conditioning diagnostics are the minimum eigenvalue divided by trace and
spectral norm, the two-lowest-eigenvalue gap, and bootstrap angles of the
minimum-eigenvector estimate. A negative result at finite width is empirical
evidence about the intended limit, never a proof about that limit.

## Positive controls

At the identical \(x\)-points, construct exact normalized Stieltjes transforms
from:

- two atoms: weights \((0.6,0.4)\), nodes \((10,100)\);
- three atoms: weights \((0.5,0.3,0.2)\), nodes \((5,40,160)\).

Their Loewner matrices are positive semidefinite and have ranks at most two
and three. They check signs, diagonals, and expected floating-point behavior
near a rank boundary; they are not fitted evidence for the target model.
