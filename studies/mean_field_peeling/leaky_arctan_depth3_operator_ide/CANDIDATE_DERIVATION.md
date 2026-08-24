# Provisional leaky-arctangent derivation

Status: exact finite algebra and compact physical-time bounds; activation
selection and the continuous width theorem are not yet frozen.

Fix `0 < alpha < 1`, put `beta=1-alpha`, and define

\[
\phi(x)=\alpha x+\beta\arctan x,
\qquad
d(x)=\phi'(x)=\frac{1+\alpha x^2}{1+x^2}.
\]

Then

\[
\alpha\le d(x)\le1,
\qquad
d'(x)=-\frac{2\beta x}{(1+x^2)^2},
\qquad
|\phi(x)|\le |x|.
\tag{1}
\]

## 1. Natural coordinate

The unique normalized natural coordinate is

\[
\Theta_\alpha(x)
=\int_0^x\frac{ds}{d(s)}
=\frac{x}{\alpha}
-\frac{1-\alpha}{\alpha\sqrt\alpha}
 \arctan(\sqrt\alpha x).
\tag{2}
\]

Indeed

\[
\Theta_\alpha'(x)=\frac{1+x^2}{1+\alpha x^2}
=\frac1{d(x)}.
\]

Consequently

\[
1\le\Theta_\alpha'(x)\le\alpha^{-1}.
\tag{3}
\]

Thus `Theta_alpha` is a global bi-Lipschitz diffeomorphism.  If
`iota_alpha=Theta_alpha^{-1}` and

\[
\Psi_\alpha(r)=\phi(\iota_\alpha(r)),
\qquad c_\alpha(r)=d(\iota_\alpha(r)),
\]

then

\[
\iota_\alpha'(r)=c_\alpha(r),
\qquad
\Psi_\alpha'(r)=c_\alpha(r)^2,
\qquad
\alpha\le c_\alpha\le1.
\tag{4}
\]

Both the transformed Gaussian seed `Theta_alpha(U)` and its inverse maps are
globally Lipschitz up to a fixed linear factor; in particular they are
pseudo-Lipschitz finite-program maps.

## 2. Exact finite feature flow

Put `r=Theta_alpha(u)` and define

\[
\begin{aligned}
X_1&=\Psi_\alpha(r),&Z_2&=G_1X_1,&X_2&=\phi(Z_2),\\
Z_3&=G_2X_2,&X_3&=\phi(Z_3),&f_n&=\langle A,X_3\rangle_n,\\
B_3&=A d(Z_3),&R_2&=G_2^*B_3,&B_2&=d(Z_2)R_2,\\
Q_1&=G_1^*B_2.&&&&
\end{aligned}
\tag{5}
\]

For `(b tensor x)v=b<x,v>_n=n^{-1}b x^T v`, feature ascent is exactly

\[
A'=X_3,
\qquad r'=Q_1,
\qquad G_1'=B_2\otimes X_1,
\qquad G_2'=B_3\otimes X_2.
\tag{6}
\]

The raw feature kernel is

\[
K_n=f_n'
=\|X_3\|_2^2
+\|B_3\|_2^2\|X_2\|_2^2
+\|B_2\|_2^2\|X_1\|_2^2
+\|d(u)Q_1\|_2^2.
\tag{7}
\]

Physical MSE flow multiplies every right-hand side in (6) by `2 eta e`,
where `e=y-f_n`, and

\[
\dot e=-2\eta eK_n,
\qquad
\dot{\mathcal L}=-4\eta e^2K_n,
\qquad \mathcal L=e^2.
\tag{8}
\]

## 3. Exact one-time operator candidate

On the joint pointed Gaussian source, retain two immutable actions with actual
adjoints,

\[
\Gamma_1:H_1\to H_2,
\qquad
\Gamma_2:H_2\to H_3,
\]

and the current state

\[
(A,r,P_1,P_2,e),
\qquad
P_\ell\in\mathfrak S_1,
\qquad
G_\ell=\Gamma_\ell+P_\ell.
\tag{9}
\]

Reconstruct (5) from the present state and solve

\[
\begin{aligned}
\dot A&=2\eta eX_3,&
\dot r&=2\eta eQ_1,\\
\dot P_1&=2\eta eB_2\otimes X_1,&
\dot P_2&=2\eta eB_3\otimes X_2,\\
\dot e&=-2\eta eK.
\end{aligned}
\tag{10}
\]

This is algebraically autonomous, restartable, and O(1)-species.  It has one
time coordinate and no response/history object.  Algebraic correctness does
not yet establish well-posedness or finite-width identification.

## 4. Compact physical-time energy bounds

Let `theta=(A,u,G1,G2)` in the declared product metric.  Since
`dot theta=2 eta e grad f`,

\[
\|\dot\theta\|^2=4\eta^2e^2K_n
=-\eta\dot{\mathcal L}.
\tag{11}
\]

Hence, for every finite `T`,

\[
\int_0^T\|\dot\theta(t)\|^2dt
\le\eta\mathcal L(0),
\qquad
\|\theta(t)-\theta(0)\|
\le\sqrt{\eta T\mathcal L(0)}.
\tag{12}
\]

For each matrix block the instantaneous gradient is rank one, and its
Frobenius and trace norms agree.  Therefore the learned perturbations satisfy

\[
\|P_\ell(t)\|_1
\le\int_0^t\|\dot G_\ell(s)\|_Fds
\le\sqrt{\eta T\mathcal L(0)}.
\tag{13}
\]

On the standard high-probability initialization event this yields uniform in
width compact-time bounds for

\[
\|A\|_2,\ \|u\|_2,\ \|P_\ell\|_1,\ \|G_\ell\|_{op}.
\tag{14}
\]

Using (1), all forward and backward fields are then bounded in normalized
`L2`:

\[
\begin{aligned}
\|X_1\|_2&\le\|u\|_2,\\
\|X_2\|_2&\le\|G_1\|_{op}\|u\|_2,\\
\|X_3\|_2&\le\|G_2\|_{op}\|G_1\|_{op}\|u\|_2,\\
\|B_3\|_2&\le\|A\|_2,\\
\|R_2\|_2&\le\|G_2\|_{op}\|A\|_2,\\
\|B_2\|_2&\le\|G_2\|_{op}\|A\|_2,\\
\|Q_1\|_2&\le\|G_1\|_{op}\|G_2\|_{op}\|A\|_2.
\end{aligned}
\tag{15}
\]

Thus neither the finite physical flow nor the algebraic candidate can escape
in the displayed state norms on a compact horizon.  These estimates do not
by themselves give square uniform integrability or continuity of nonlinear
products on bare `L2` balls.

## 5. What the derivative floor repairs—and what it does not yet repair

The exact norm equivalences

\[
\|A\|_2\le\alpha^{-1}\|B_3\|_2,
\quad
\|R_2\|_2\le\alpha^{-1}\|B_2\|_2,
\quad
\|Q_1\|_2\le\alpha^{-1}\|d(u)Q_1\|_2
\tag{16}
\]

remove the vanishing-derivative hiding mechanism of pure arctangent.  They
also make every natural-coordinate fiber norm uniformly equivalent to the
physical `L2` norm and bound every conjugation by `d` or `d^{-1}` by a fixed
power of `alpha^{-1}`.

However, a direct difference still contains, for example,

\[
A\{d(Z_3)-d(\widetilde Z_3)\},
\qquad
R_2\{d(Z_2)-d(\widetilde Z_2)\}.
\tag{17}
\]

An arbitrary `L2` multiplier times an `L2` difference need not lie in `L2`.
Therefore (16) eliminates a specific depth-three obstruction but does not,
without a reachable-state tail or cancellation estimate, prove S3--S6.

