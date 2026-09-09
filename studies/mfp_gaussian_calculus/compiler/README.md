# Generic first-Stieltjes compiler: symbolic base

This directory is an isolated implementation track for the two-hidden-layer,
one-input base case. It does not modify or generalize the audited quadratic
decorated-forest compiler.

## Frozen model

For one input with (q_0=\|x\|^2/d_0), the scalarized initialization is

\[
U_j\sim N(0,q_0),\qquad H_j=\phi(U_j),\qquad
Z_i=\frac1{\sqrt n}\sum_jW_{ij}H_j,
\qquad
f_n=\frac1n\sum_i a_i\phi(Z_i).
\]

All raw parameters are independent standard Gaussians and
(D_n=n\nabla f_n\cdot\nabla). Scalarizing the first raw matrix produces the
metric factor (q_0) in the (U) coordinate. The derivative order is formed
at finite width before (n\to\infty).

`normal_form.py` represents a coefficient as a finite scalar DAG. Its only
nonalgebraic leaves are literal atoms

\[
\mathbb E_{X\sim N(0,\Sigma)}
\prod_s\phi^{(r_s)}(X_{i_s}),
\]

with the full covariance matrix stored in the node. Covariance entries may
depend on earlier atoms, giving a finite layerwise DAG without concealing
random response variables. `evaluate_polynomial` contracts every such atom
exactly by Isserlis recursion.

## Established initialization coefficient

`l2_b1_base.py` emits

\[
\begin{aligned}
q_1&=\mathbb E_{U\sim N(0,q_0)}[\phi(U)^2],
&d_1&=\mathbb E_{U\sim N(0,q_0)}[\phi'(U)^2],\\
q_2&=\mathbb E_{Z\sim N(0,q_1)}[\phi(Z)^2],
&d_2&=\mathbb E_{Z\sim N(0,q_1)}[\phi'(Z)^2],
\end{aligned}
\]

and the exact initialization NTK limit

\[
A=F'(0)=q_2+q_1d_2+q_0d_1d_2.
\]

The exact polynomial gates are

| activation, (q_0=1) | (A) |
|---|---:|
| (phi(x)=2) | (4) |
| (phi(x)=x) | (3) |
| (phi(x)=x^2) | (111) |

## Independent finite-width oracle

`finite_width_jet.py` propagates ordinary Taylor coefficients of the exact
finite-width feature-ascent ODE through order three for a supplied derivative
oracle. It requires only (phi,\phi',\phi'',\phi'''). It is not a mean-field
proof and performs no Gaussian replacement.

For the linear activation and (q_0=1), a separate exact finite-width Wick
calculation gives

\[
\mathbb E[D_n^3f_n]=48+\frac{60}{n},\qquad
\lim_{n\to\infty}\mathbb E[D_n^3f_n]=48.
\]

Indeed, writing (g=a^TWu) and (f=n^{-3/2}g),

\[
D_n^3f_n=n^{-3}\left(4\|H_gp_g\|^2+2T_g[p_g,p_g,p_g]\right).
\]

Exact Gaussian contraction gives

\[
\mathbb E\|H_gp_g\|^2=12n^3+12n^2,
\quad
T_g[p_g,p_g,p_g]=6g^2,
\quad
\mathbb E[g^2]=n^2,
\]

which proves the displayed (48+60/n) identity. For the quadratic activation,
the generic finite-width oracle agrees seed-by-seed with the pre-existing
quadratic reference implementation, and the required mean-field regression is

\[
A=111,\qquad F'''(0)=1\,685\,184.
\]

`finite_width_contraction.py` is a second, independent finite-width route. It
evaluates equation (3.10) of `PEELING_AND_PROBABILITY_LEDGER.md` directly from
the initialization vectors and matrix. It neither imports nor reproduces the
Taylor-series propagation in `finite_width_jet.py`. Seedwise tests compare the
two exact encodings for widths 1, 2, 5, and 9; seeds 0, 3, and 17; and linear,
affine, quadratic, cubic, sine, and tanh activations. Additional tests at
`q0=0.25` and `q0=2.5` audit every input-metric power. All comparisons pass at
floating-point roundoff.

## Audited correction normal form

The IR and independent finite-width oracle are complete.
`l2_b1_correction.py` emits the literal normal form for
\(C=F'''(0)\). It contains the complete inventory of seventeen unique
one-dimensional Gaussian atoms, uses derivatives only through \(\phi'''\),
and contains no unnamed fresh or response field. Its compact labels are
finite-DAG common subexpressions and expand entirely into literal atoms.

The formula is an executable exact mean-field coefficient under the
polynomially-smooth activation envelope.  The line-by-line response/equality
audit and the almost-sure/\(L^p\) finite-width bridge are recorded in
`PEELING_AND_PROBABILITY_LEDGER.md`; the weaker finite-order regularity tier is
spelled out there and in `PROBABILISTIC_BRIDGE_AUDIT.md`.  Its special-case
contractions below are exact:

1. constant: (C=0);
2. linear: (C=48) at (q_0=1), including the exact finite-width
   (48+60/n) audit;
3. quadratic: (C=1\,685\,184) at (q_0=1), matched both to exact MFP and to
   the independent finite-width jet implementation.
