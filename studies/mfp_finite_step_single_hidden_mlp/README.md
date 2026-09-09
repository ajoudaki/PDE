# One finite μP step in a one-hidden-layer MLP

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

**Status:** exact calculation for one input and one simultaneous
feature-ascent step. No small-learning-rate approximation is used.

## Model

Fix one input $x\in\mathbb R^d$ and define

$$
q=\frac{\|x\|^2}{d}.
$$

The width-$n$ network is

$$
z_i=\frac{w_i^\top x}{\sqrt d},
\qquad
f_n(x)=\frac1n\sum_{i=1}^n a_i\phi(z_i).
$$

At initialization,

$$
w_i\sim N(0,I_d),
\qquad
a_i\sim N(0,1),
$$

independently across neurons and parameter blocks. Hence
$z_i\sim N(0,q)$ and $a_i$ is independent of $z_i$.

## One simultaneous step

Take one explicit μP feature-ascent step

$$
(a,w)^+=(a,w)+\eta n\nabla_{a,w}f_n(x).
$$

Both gradients are evaluated at the old parameters. Since

$$
\frac{\partial f_n}{\partial a_i}
=\frac1n\phi(z_i),
\qquad
\nabla_{w_i}f_n
=\frac1n a_i\phi'(z_i)\frac{x}{\sqrt d},
$$

the exact updates are

$$
a_i^+=a_i+\eta\phi(z_i),
$$

$$
w_i^+=w_i+\eta a_i\phi'(z_i)\frac{x}{\sqrt d}.
$$

Therefore the new preactivation at the same input is

$$
z_i^+
=\frac{(w_i^+)^\top x}{\sqrt d}
=z_i+\eta q\,a_i\phi'(z_i).
$$

The post-step output is thus exactly

$$
f_n^+(x)
=\frac1n\sum_{i=1}^n
\left(a_i+\eta\phi(z_i)\right)
\phi\!\left(z_i+\eta q\,a_i\phi'(z_i)\right).
$$

## Expected output and mean-field limit

Let

$$
A\sim N(0,1),
\qquad
Z\sim N(0,q),
\qquad
A\perp Z.
$$

Then, for every finite width $n$,

$$
F_\eta
:=\mathbb E[f_n^+(x)]
=
\mathbb E\!\left[
\left(A+\eta\phi(Z)\right)
\phi\!\left(Z+\eta qA\phi'(Z)\right)
\right].
$$

This is already the exact finite-$n$ expectation. If the integrand is
integrable, the iid strong law also gives

$$
f_n^+(x)\longrightarrow F_\eta
\qquad\text{almost surely as }n\to\infty.
$$

No covariance replacement or Taylor expansion in $\eta$ is required.

## Gaussian computational DAG

Define

$$
Z_\eta=Z+\eta qA\phi'(Z).
$$

The complete width-independent DAG is

$$
(A,Z)
\longrightarrow
\bigl(\phi(Z),\phi'(Z)\bigr)
\longrightarrow
\bigl(A+\eta\phi(Z),Z_\eta\bigr)
\longrightarrow
\left(A+\eta\phi(Z)\right)\phi(Z_\eta)
\longrightarrow
\mathbb E.
$$

Under the usual Gaussian integration-by-parts assumptions,

$$
\mathbb E\!\left[A\phi(Z_\eta)\mid Z\right]
=\eta q\phi'(Z)
\mathbb E\!\left[\phi'(Z_\eta)\mid Z\right].
$$

Consequently the same answer has the compact cross-kernel form

$$
F_\eta
=
\eta\,\mathbb E\!\left[
\phi(Z)\phi(Z_\eta)
+q\phi'(Z)\phi'(Z_\eta)
\right].
$$

This is a two-Gaussian normal form, but it is not generally a finite product
of initialization moments: the activation is evaluated at the shifted
variable $Z_\eta$.

## Connection with initialization derivatives

At small $\eta$,

$$
F_\eta
=
\eta\,\mathbb E\!\left[
\phi(Z)^2+q\phi'(Z)^2
\right]
+O(\eta^3).
$$

The coefficient of $\eta$ is the usual initialization tangent kernel.
Higher powers here are coefficients of the one-step Euler map, not
derivatives of the continuous feature-ascent flow.

For example, if $\phi(z)=z$,

$$
F_\eta=2\eta q.
$$

If $\phi(z)=z^2$,

$$
F_\eta=7\eta q^2+12\eta^3q^4.
$$

At $q=1$, continuous feature ascent instead begins
$7t+160t^3+\cdots$. Thus one finite Euler step cannot be obtained by simply
evaluating the continuous-flow initialization jet at $t=\eta$.

## Scope

- One fixed input and the output at that same input.
- One simultaneous feature-ascent step.
- Arbitrary finite $\eta$ for which the displayed expectation exists.
- The raw expectation only needs the derivative used in the update.
  The integration-by-parts form needs the corresponding additional
  differentiability and integrability.
- A second step evolves the non-Gaussian pushforward law of $(A,Z)$ and is a
  separate calculation.

finite_step_dag.py evaluates both expectation formulas by Gauss--Hermite
quadrature. test_finite_step_dag.py checks their equality and the constant,
linear, and quadratic controls.
