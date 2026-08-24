# Audit: full Hessian, curvature spectra, and column forcing

## Verdict

In the original preactivation coordinate \(u\), the feature flow is exact
gradient ascent and its complete tangent generator is the self-adjoint
Hessian of the predictor.  The three potentially unbounded curvature
multipliers are controlled pointwise by

\[
 |K_1|\le |C_1|,\qquad |K_2|\le |B_2|,\qquad
 |K_3|\le |B_3|,
\]

where \(C_1=D_1Q_1=u'\).  This corrects any formulation that mistakenly sets
\(u'=Q_1\); the natural coordinate satisfies \(r'=Q_1\), while
\(u'=D_1Q_1\).

The self-adjoint structure does not by itself close the response theorem.
An empirical \(\psi_1\) curvature profile permits isolated
\(\log n\)-sized positive curvature.  Log-majorization then gives only a
power-law singular-value profile, and a Schatten-\(p\) estimate with
\(p\asymp\log n\) is uniform only on intervals of length
\(O(1/\log n)\).  The canonical transpose forcing is exactly aligned with
the eigenvector of an isolated one-coordinate middle-curvature summand.

This is a sharp counterexample to any deterministic proof whose only inputs
are empirical \(\psi_1\) profiles, bulk operator norms, and the generic
Hessian block structure.  It is not a reachable-flow counterexample:
curvature-spike persistence, domination over the other Hessian blocks, and
observability at \(D_{\xi_j}B_3\) remain unproved.

## Exact normalized tangent

Use normalized vector inner products and ordinary Frobenius matrix inner
products.  Thus

\[
 b\otimes_nx=n^{-1}bx^\top.
\]

For a standard-Gaussian column
\(\Gamma_{2,:,j}=n^{-1/2}\xi_j\) and direction \(h\), its direct matrix
variation is

\[
 S_j(h)=n^{-1/2}he_j^\top.
\]

Write

\[
 a=D_{\xi_j}A[h],\quad v=D_{\xi_j}u[h],\quad
 H_\ell=D_{\xi_j}P_\ell[h].
\]

With \(D_\ell=\operatorname{diag}d(Z_\ell)\) and

\[
\begin{aligned}
K_1&=\operatorname{diag}(d'(u)Q_1),\\
K_2&=\operatorname{diag}(d'(Z_2)R_2),\\
K_3&=\operatorname{diag}(d'(Z_3)A),
\end{aligned}
\]

the exact differentiated graph is

\[
\begin{aligned}
x_1&=D_1v,\\
z_2&=H_1X_1+G_1x_1,&x_2&=D_2z_2,\\
z_3&=(H_2+S_j(h))X_2+G_2x_2,&x_3&=D_3z_3,\\
b_3&=D_3a+K_3z_3,\\
r_2&=(H_2+S_j(h))^*B_3+G_2^*b_3,\\
b_2&=D_2r_2+K_2z_2,\\
q_1&=H_1^*B_2+G_1^*b_2.
\end{aligned}
\]

The memory ODE is

\[
\begin{aligned}
a'&=x_3,\\
v'&=K_1v+D_1q_1,\\
H_1'&=n^{-1}(b_2X_1^\top+B_2x_1^\top),\\
H_2'&=n^{-1}(b_3X_2^\top+B_3x_2^\top).
\end{aligned}
\]

Because

\[
K_1=\operatorname{diag}\{(d'/d)(u)C_1\},\quad
K_2=\operatorname{diag}\{(d'/d)(Z_2)B_2\},\quad
K_3=\operatorname{diag}\{(d'/d)(Z_3)B_3\}
\]

and \(|d'/d|\le1\), the displayed curvature bounds follow.

The complete system is

\[
Y'=\nabla^2f(\theta(t))Y,\qquad
Y(0)=(0,0,0,S_j(h)),
\]

on the vector/matrix parameter Hilbert space.  Hence the generator is
self-adjoint.  Passing to \(r\) is an exact time-dependent gauge
\(v=D_1D_{\xi_j}r[h]\); the resulting fixed \(r\)-metric generator need not
be self-adjoint, and its connection term is precisely \(K_1\).

## Exact isolated-curvature alignment

Let the parameter-to-middle-preactivation Jacobian be

\[
 \mathcal J_2(a,v,H_1,H_2)=G_1D_1v+H_1X_1.
\]

Its adjoint is

\[
 \mathcal J_2^\dagger z
 =(0,D_1G_1^*z,n^{-1}zX_1^\top,0).
\]

The middle curvature block of the Hessian is exactly

\[
 \mathcal K_2=\mathcal J_2^\dagger K_2\mathcal J_2.
\]

The direct transpose variation is

\[
 S_j(h)^*B_3=n^{-1/2}(B_3^\top h)e_j.
\]

After the \(D_2\) gate, its induced parameter forcing contains

\[
 \mathfrak f_j^{\rm tr}(h)
 =\frac{d(Z_{2,j})B_3^\top h}{\sqrt n}
   \mathcal J_2^\dagger e_j.
\]

If the isolated curvature is \(K_2=k_je_je_j^\top\), then
\(s_j=\mathcal J_2^\dagger e_j\) is its eigenvector and the forcing is
parallel to it.  Under the normalized metric,

\[
 \mathcal K_2s_j
 =n k_j\|s_j\|_{\mathcal H}^2s_j,
\]

and typically \(n\|s_j\|_{\mathcal H}^2\asymp1\).

## Sharp limitation of empirical spectral profiles

An empirical \(\psi_1\) moment bound

\[
 \left(n^{-1}\sum_i|b_i|^p\right)^{1/p}\le Kp,
 \qquad p\le\log n,
\]

implies only the order-statistic estimate

\[
 |b|_{(r)}\le CK\{1+\log(n/r)\}.
\]

Finite-sum Ky Fan inequalities applied to the exact Hessian blocks therefore
give at best

\[
 \lambda_r^+(\nabla^2f)
 \le C\{1+\log(Cn/r)\}.
\]

Exterior-power log-majorization for the propagator \(U(t,s)\) yields

\[
 s_k(U(t,s))
 \le C_\tau(Cn/k)^{CK\tau},\qquad \tau=t-s.
\]

Its normalized Schatten-\(q\) profile is uniformly summable only if

\[
 CK\tau q<1.
\]

Thus \(q\asymp\log n\) forces \(\tau=O(1/\log n)\).  Splitting time into such
intervals does not reset the Malliavin response, so persistent stretching
multiplies across the pieces.

The estimate is sharp under its abstract hypotheses.  The vector

\[
 k^{(n)}=(K\log n,0,\ldots,0)
\]

has uniformly bounded empirical \(\psi_1\) norm.  In the frozen isolated
model

\[
 \mathcal J_2^\dagger\operatorname{diag}(k^{(n)})\mathcal J_2
\]

the aligned source in column one grows as
\(n^{cKt}/\log n\), provided the remaining Hessian is only \(O(1)\).  One
such column already destroys an empirical \(p=\log n\) response profile.

## Surviving requirement

A successful spectral proof must use a property absent from empirical
curvature profiles: for example, a bound on time-integrated positive
curvature along the source-reachable direction, rapid residence-time decay
of large gate curvature, signed rotation away from the spike, or a
target-output observability estimate.  Any such statement has to be proved
from the canonical arctan dynamics; it cannot be inferred from \(\psi_1\)
tails alone.
