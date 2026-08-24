# Exact Euler cancellation in the causal top predictor

## Status

This note records an exact algebraic cancellation in the fixed-mesh
transpose-reusing tensor program.  It removes the previously isolated
``projected bulk velocity'' as an independent tail obstruction.  It does not
bound the endpoint Gaussian transfer and therefore does not prove the middle
tail theorem by itself.

## 1. Divided-difference identities

Let the Euler feature-time step be (h).  At step (k), abbreviate

\[
 x_k=X_2^k,quad W_k=\Gamma _2+P_2^k,quad
 z_k=Z_3^k,quad a_k=A^k,quad d_k=d(z_k),quad b_k=a_kd_k,
\]

where (d(z)=(1+z^2)^{-1}).  Put

\[
 \rho_k=\langle x_k,x_k\rangle,qquad
 Dd_k=Dd(z_k,z_{k+1})
 ={d(z_{k+1})-d(z_k)\over z_{k+1}-z_k}.
\]

The exact Euler preactivation and readout increments are

\[
 z_{k+1}-z_k=h\{W_kV_2^k+\rho_kb_k\},
 \qquad a_{k+1}-a_k=h\atan z_k,
 \tag{1.1}
\]

and hence

\[
 hW_kV_2^k=(z_{k+1}-z_k)-h\rho_kb_k.                 \tag{1.2}
\]

The exact divided difference of the arctangent gate is

\[
 Dd(a,b)=-{a+b\over(1+a^2)(1+b^2)}.                 \tag{1.3}
\]

If

\[
 F_3^k=\atan(z_k)d_{k+1}+a_kDd_k\{W_kV_2^k+\rho_kb_k\},
 \tag{1.4}
\]

then (1.1)--(1.3) give the exact identity

\[
 \boxed{hF_3^k=b_{k+1}-b_k.}                        \tag{1.5}
\]

In particular, the apparent remainder
(h\rho_k a_k^2d_kDd_k) from replacing (W_kV_2^k) by a
preactivation increment cancels the explicit learned-row contribution in
(1.4).  No estimate is involved.

## 2. Causal-transfer recursion

Let (mathcal T_{k+1}) denote the covariance-isometric transfer from the
Gaussian forward history through step (k+1) to the corresponding
(X_2)-history.  The exact causal predictor recursion is

\[
 p_{k+1}=p_k+h\mathcal T_{k+1}F_3^k
          =p_k+\mathcal T_{k+1}(b_{k+1}-b_k).        \tag{2.1}
\]

The canonical transfers are extension-consistent: if (v) belongs to the
old Gaussian history space, then

\[
 \mathcal T_{k+1}v=\mathcal T_kv.                   \tag{2.2}
\]

Since (b_k) is an old-history variable, discrete Abel summation gives

\[
\begin{aligned}
 \sum_{k=0}^{m-1}\mathcal T_{k+1}(b_{k+1}-b_k)
 &=\mathcal T_m b_m-\mathcal T_1b_0
   -\sum_{k=1}^{m-1}(\mathcal T_{k+1}-\mathcal T_k)b_k\\
 &=\mathcal T_mb_m-\mathcal T_1b_0.                \tag{2.3}
\end{aligned}
\]

Thus (with the matching initial convention)

\[
 \boxed{p_m=\mathcal T_mb_m.}                       \tag{2.4}
\]

This is exactly the endpoint first-chaos transfer; the bulk-velocity term,
the learned-row term, and the apparent variation of the transfer do not
leave separate remainders.

## 3. What remains

The covariance isometry gives only

\[
 \|\mathcal T_mb_m\|_2\le \|b_m\|_2.               \tag{3.1}
\]

There is no generic (L^2\to\psi_1) upgrade: near-collinear bounded
arctangent histories can have normalized residuals converging to cubic or
higher Gaussian chaos.  Nor may one estimate the variation of
(mathcal T_k) off the old history: an (O(h)) residual can select an
(O(1))-different normalized direction.

Consequently the surviving question is model-specific.  In the actual
Euler orbit one must control the endpoint transfer through the coupled
static forward response.  The first nontrivial lower response contains

\[
 R_2{d'(Z_2)\over d(Z_2)}\,\delta X_2,
 \qquad
 {d'(z)\over d(z)}=-{2z\over1+z^2}=-\sin(2\atan z), \tag{3.2}
\]

whose logarithmic gate factor is bounded but whose repeated weighted
tangent has not yet been controlled.  Equation (2.4) sharpens the frontier:
the endpoint coupled response, not a missing Abel or coefficient-BV
estimate, is the sole predictor-tail obstruction.
