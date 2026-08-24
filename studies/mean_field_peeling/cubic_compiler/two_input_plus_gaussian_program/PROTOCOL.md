# Two-input raw-cubic plus-channel kernel: frozen local protocol

## Canonical model and input geometry

Fix two deterministic unit-RMS inputs with correlation

\[
Q(\rho)=\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},
\qquad -1\leq\rho\leq1.
\]

For two equal-width hidden layers and raw cubic activation at both layers,
write, for examples \(r\in\{1,2\}\),

\[
X_r=U_r^3,
\qquad
Z_r=n^{-1/2}WX_r,
\qquad
G_r=Z_r^3,
\qquad
f_r=n^{-1}A^\top G_r.
\]

At initialization, \((U_1,U_2)\) is centered Gaussian with covariance
\(Q(\rho)\); \(A,W\) have independent standard-Gaussian entries.  All
three parameter blocks train with the same unit Euclidean metric as in the
one-input cubic program.  The matrix \(Q(\rho)\) is used both in the
initialization law and in the bottom-layer gradient metric.  Omitting its
second occurrence changes the model.

For equal labels \((1,1)\), define the exchange-symmetric output and feature
direction

\[
g=\frac{f_1+f_2}{2},
\qquad
D_+=n\nabla g\mathbin\cdot\nabla,
\qquad
F_+^{(k)}(0;\rho)=\lim_{n\to\infty}E[D_+^kg].
\]

The width limit is taken first at every fixed derivative order.  No
finite-width extrapolation, independent-matrix replacement, NTK freezing,
or omission of cross-example responses is allowed.

## Exact loss-flow object

For a general two-output state, the instantaneous object is the tangent
kernel matrix

\[
\Theta_{rs}=n\nabla f_r\mathbin\cdot\nabla f_s.
\]

In the deterministic width-first/formal reduction, exchange symmetry starts
at \(f_1=f_2=0\) and preserves the plus channel \(f_1=f_2=g\).  On this
channel,

\[
K_+(g;\rho)=n\|\nabla g\|^2
=\frac{\Theta_{11}+\Theta_{12}}2.
\]

If \(F_+'(0;\rho)\ne0\), its formal output-coordinate representation is

\[
K_+(y;\rho)
=F_+'\!\left(F_+^{-1}(y;\rho);\rho\right).
\]

For the natural average squared loss

\[
\mathcal L=\frac12\left[(f_1-1)^2+(f_2-1)^2\right]
=(1-g)^2
\]

and learning-rate multiplier \(\eta\), the exact symmetric-channel equations
are

\[
\dot g=2\eta(1-g)K_+(g;\rho),
\qquad
\dot{\mathcal L}=-4\eta K_+(g;\rho)\mathcal L.
\]

This is exactly the restriction of the genuine two-example MSE gradient, not
a surrogate loss.  The scalar reduction is licensed by equal labels and the
exchange-symmetric width-first/formal trajectory.  It is not an exact scalar
closure for an individual finite random network, where generally
\(f_1\ne f_2\) and \(\Theta_{11}\ne\Theta_{22}\), nor for arbitrary
two-output trajectories; those require the full matrix \(\Theta\).

Readout reflection makes \(F_+\) odd and \(K_+\) even.  Thus
\(K_+'(0;\rho)=0\); the first informative kernel derivative is
\(K_+''(0;\rho)\).

## Two-example feature-ascent recurrence

Put

\[
B_r=A\odot Z_r^2,
\qquad
R_r=n^{-1/2}W^\top B_r.
\]

The exact feature-ascent flow is

\[
\dot A=\frac{G_1+G_2}{2},
\]

\[
\dot W=\frac3{2\sqrt n}\sum_{q=1}^2B_qX_q^\top,
\]

\[
\dot U_r=\frac92\sum_{q=1}^2
Q_{rq}(\rho)\,U_q^2\odot R_q.
\]

Integrating \(W\) gives

\[
Z_r(t)=n^{-1/2}W_0X_r(t)
+\frac32\sum_q\int_0^t
B_q(s)\langle X_q(s),X_r(t)\rangle_n\,ds,
\]

\[
R_r(t)=n^{-1/2}W_0^\top B_r(t)
+\frac32\sum_q\int_0^t
X_q(s)\langle B_q(s),B_r(t)\rangle_n\,ds.
\]

For sample-indexed Gaussian innovations, exact detransposition is

\[
E[\eta_{r,k}\eta_{q,j}]=E[X_{r,k}X_{q,j}],
\]

\[
\widehat Z_{r,k}=\eta_{r,k}
+\sum_{q=1}^2\sum_{j<k}
E[\partial_{\xi_{q,j}}X_{r,k}]B_{q,j},
\]

\[
E[\xi_{r,k}\xi_{q,j}]=E[B_{r,k}B_{q,j}],
\]

\[
\widehat R_{r,k}=\xi_{r,k}
+\sum_{q=1}^2\sum_{j\leq k}
E[\partial_{\eta_{q,j}}B_{r,k}]X_{q,j}.
\]

Every coefficient and covariance is retained as an exact rational polynomial
in \(\rho\), and every Gaussian expectation is evaluated by exact Wick
recurrence.

## Primary target and precommitted gates

Compute the exact polynomial jets

\[
F_+'(0;\rho),\qquad F_+^{(3)}(0;\rho),
\]

then report

\[
K_+(0;\rho)=F_+'(0;\rho),
\qquad K_+'(0;\rho)=0,
\qquad
K_+''(0;\rho)=\frac{F_+^{(3)}(0;\rho)}{F_+'(0;\rho)^2}.
\]

The run is accepted only if all gates pass:

1. ordinary-Taylor and derivative-normalized recurrences agree exactly;
2. every even feature derivative through order three vanishes exactly;
3. the direct initialization block audit gives, with
   \(c(\rho)=9\rho+6\rho^3\),

   \[
   \begin{aligned}
   F_+'(0;\rho)={}&\frac12(50625+2025c+6c^3)\\
   &+\frac92\{10125+c(225+2c^2)\}\\
   &+\frac{81}{2}\{2025+\rho(1+2\rho^2)(225+2c^2)\};
   \end{aligned}
   \]

4. at \(\rho=1\), both jets equal the accepted one-input cubic values
   \(305775\) and \(154118008098000\);
5. at \(\rho=-1\), the plus direction is exactly degenerate and both jets
   vanish;
6. exchange of the two inputs leaves every output polynomial unchanged;
7. exact polynomial coefficients are reproduced by independent rational
   evaluations at unused holdout correlations.

## Resource and claim boundary

- Maximum feature order: three.
- Maximum two minutes and 2 GiB per exact coefficient route.
- Resource exhaustion or a failed gate is inconclusive.
- The result determines only the local kernel value and curvature at output
  zero.  It does not prove positive-time existence, global invertibility,
  arbitrary-order closure, or a scalar reduction away from the invariant
  equal-label plus channel.
- At \(\rho=-1\), \(F_+'(0)=0\), so the output-coordinate inverse and
  \(K_+''(0)\) are not defined even though the feature jets have a well-defined
  degenerate limit.
