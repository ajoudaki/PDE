# Transverse Curvature No-Go for Finite-Moment Gate Calculi

## Claim

For depth three with arctangent activation, mobility flattening and exact
paired-edge integration cancel the active rank-one part of the dangerous
gate response.  They do not cancel a transverse curvature operator generated
by movement of the lower feature.  Uniform normalized energy, matrix
operator norms, and any one fixed `L^p` bound on the hidden response do not
control this operator.  Consequently no response-cutoff-uniform stability
theorem can be based on only those certificates.

This is a deterministic witness against a proposed calculus, not a
counterexample to convergence from Gaussian initialization.

## 1. The uncancelled operator

For `d(z)=(1+z^2)^(-1)`, the exact middle preactivation dynamics is

\[
 \dot z_2=K_1b_2,
 \qquad
 K_1=q_1I+G_1D_1^2G_1^*,
 \qquad
 b_2=D_2r_2.
\tag{1}
\]

In a variation with `delta r_2=0`, the gate curvature contains

\[
 K_1\operatorname{diag}(d'(z_2)r_2)\,\delta z_2.
\tag{2}
\]

The mobility coordinate removes the part of (2) proportional to `q_1I`.
The paired-edge identity does not remove

\[
 \boxed{
 G_1D_1^2G_1^*
 \operatorname{diag}(d'(z_2)r_2).
 }
\tag{3}
\]

This is the curvature of transport in directions transverse to the current
lower feature.

## 2. Exact bounded-certificate witness

Fix a finite `p>=2`, choose a set `S=S_+ union S_-` of density `epsilon`
with equal halves, and put

\[
 R=\epsilon^{-1/p},
 \qquad r_2=R1_S.
\]

Then

\[
 \|r_2\|_{p,n}=1,
 \qquad
 \|r_2\|_{2,n}=\epsilon^{1/2-1/p}\le1.
\tag{4}
\]

Take a fixed `z_0>0` and set `z_2=z_0` on `S_+`, `z_2=-z_0` on `S_-`,
and zero elsewhere.  Let `v` be a normalized, mean-zero vector supported on
`S_-`, so that `v` is orthogonal to both `1_S` and `z_2`.  Choose a lower
feature with `q_1=||x_1||_n^2` comparable to `epsilon`, and a normalized
`y` orthogonal to `x_1`, supported where `u=0`.  Define

\[
 G_1=\frac{z_2\otimes_nx_1}{q_1}+v\otimes_ny.
\tag{5}
\]

Then `G_1x_1=z_2`, `||G_1||_op<=C`, and, because the two relevant
contractions vanish,

\[
 G_1^*b_2=0.
\tag{6}
\]

The upper response can be realized with the same matrix in both orientations.
Let

\[
 t=\epsilon^{-1/2}1_S,
 \qquad G_2=t\otimes_nt,
 \qquad A=r_2.
\tag{7}
\]

Balanced oddness gives `G_2 atan(z_2)=0`; hence `z_3=0`, `b_3=A`, and

\[
 G_2^*b_3=r_2
\tag{8}
\]

exactly.  Also `||G_2||_op=1` and `||A||_(p,n)=1`.

Perturb only the lower mobility coordinate by

\[
 \delta w_1=a y.
\]

On the support of `y`, `u=0`, so `delta x_1=ay` and

\[
 \delta z_2=aG_1y=av.
\]

The balance choices give `delta z_3=delta r_2=0`.  On `S_-`,
`d'(-z_0)=c_0>0`, so

\[
 \delta b_2=c_0Ra v,
 \qquad
 \delta r_1=G_1^*\delta b_2=c_0Ra y.
\]

Therefore

\[
 \boxed{
 \delta\dot w_1=c_0R\,\delta w_1.
 }
\tag{9}
\]

Every certificate in (4)--(8) stays bounded while the variational rate
`c_0 epsilon^(-1/p)` diverges.

This is not merely instantaneous.  The active drift has size

\[
 q_1b_2=O(\epsilon R)=O(\epsilon^{1-1/p}),
\]

and rank-one learning along `x_1` leaves the transverse action `G_1y=v`
unchanged.  Thus the configuration persists on an order-one short interval
and the exact variational amplification is exponential in `R`.

## 3. Consequences for machinery design

1. A finite list of fixed moments cannot replace a projective tail class.
   For any largest tracked `p`, (4) passes the certificate while (9) defeats
   stability.
2. Exact forward/transpose source reuse does not remove the witness; (7)--(8)
   use one tied matrix.
3. Higher-order splitting does not cure exact instability.  A first-order
   block has factor `1+h c_0R+o(hR)`; the exact flow has `exp(h c_0R)`.
4. A lower bound on the current feature norm would remove the particular
   small-`q_1` persistence mechanism, but would still need a transverse
   decorrelation estimate.  Such a lower bound is not part of the general
   architecture.
5. A successful reachable-state theory must control a genuinely transverse
   object, for example

   \[
   \int_0^T
   \left\|
   G_{1,\perp}^*
   \operatorname{diag}(d'(z_2)r_2)
   G_{1,\perp}
   \right\|_{op}dt,
   \tag{10}
   \]

   or prove an all-order tail/decorrelation theorem that implies (10).

Equation (10) is sharper than a bare `r_2` moment bound: it records the
alignment between rare response mass and the transverse singular directions
that actually drive instability.  Conversely, assuming (10) without a
recursive verification rule would simply rename the hard problem.

## 4. Disposition

The gate-resolved increment identity remains exact and useful.  The proposed
completion from energy plus a finite moment hierarchy is falsified.  The
remaining plausible version must be probabilistic and reachable-set
specific, and it must propagate either a full Orlicz envelope together with
transverse decorrelation or a direct integrated-curvature certificate.
