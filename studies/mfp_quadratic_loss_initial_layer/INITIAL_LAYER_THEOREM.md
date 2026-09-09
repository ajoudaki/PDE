# Width-first quadratic loss Euler has an instantaneous initial layer

## Theorem

Consider the same one-input, two-hidden-layer network, with

\[
 \phi(x)=q x^2,  q=3^{-1/2}, 
 \mathbb E\phi(G)^2=1.
\]

Let $F_k^{h}$ be the deterministic width-first output after $k$
recomputed half-square-loss gradient steps of size $h>0$,

\[
 \theta^{k+1}
 =\theta^k+h(1-f(\theta^k))g(\theta^k), 
 g=n\nabla f,  y=1.
\tag{1.1}
\]

Fix a physical horizon $T>0$, put $h_N=T/N$, and let

\[
 \tau_N(\delta)
 =h_N\min\{k\ge0:F_k^{h_N}\ge\delta\}, 
 0<\delta<1.
\tag{1.2}
\]

Then

\[
 \boxed{\tau_N(\delta)\longrightarrow0}
\tag{1.3}
\]

for every $0<\delta<1$.  In particular, the piecewise-linear predictor
interpolants cannot converge uniformly on any interval $[0,T]$ to a
continuous function having the initialization value $F(0)=0$.  The
corresponding interpolated losses

\[
 \ell_N(s)={1\over2}\{1-\overline F_N(s)\}^2
\]

cannot converge uniformly to a continuous loss curve with
$\ell(0)=1/2$.

Thus the width-first Euler meshes do **not** have the requested classical
compact-time gradient-flow limit.  The obstruction is an all-source-order
initial layer, not a finite Taylor coefficient.

The theorem does not assert that $F_N^{T/N}$, or its terminal loss, fails
to converge at one fixed $T>0$.  Nor does it prove that

\[
 \ell_{2t}(h)-\ell_t(2h)
\]

stays away from zero at their common terminal time.  Both meshes could in
principle converge after the same discontinuous initial layer.  The
post-hitting dynamics contains negative effective feature steps and is not
ordered by the argument below.

## 1. Exact finite-width network

At width $n$, initialize $a_i,u_j,W_{ij}$ independently as standard
Gaussians and put

\[
 H_j=q u_j^2, 
 z_i={1\over\sqrt n}\sum_jW_{ij}H_j, 
 Y_i=qz_i^2, 
 f_n={1\over n}\sum_i a_iY_i.
\tag{2.1}
\]

With

\[
 C_i=2q a_i z_i, 
 b_j={1\over\sqrt n}\sum_iW_{ij}C_i,
\]

one deterministic feature-ascent step of size $s$ is exactly

\[
\begin{aligned}
 a_i^+&=a_i+s qz_i^2,\\
 W_{ij}^+&=W_{ij}+{s\over\sqrt n}C_iH_j,\\
 u_j^+&=u_j+2qs\,b_ju_j.
\end{aligned}
\tag{2.2}
\]

One loss step is (2.2) with the random effective step

\[
 s_{k,n}=h(1-f_{k,n}).
\tag{2.3}
\]

## 2. Deterministic schedules are coefficientwise monotone

For a deterministic schedule
$\mathbf s=(s_0,\ldots,s_{m-1})$, let
$\mathcal F_{m,n}(\mathbf s)=\mathbb E f_{m,n}$ for the feature updates
(2.2).

Treat every raw initialization coordinate and every $s_j$ as a formal
indeterminate.  Every coordinate on the right of (2.1)--(2.2) is a
polynomial with nonnegative coefficients.  Induction on the steps therefore
shows that the terminal output is a polynomial with nonnegative formal
coefficients in

\[
 (a_i,u_j,W_{ij},s_0,\ldots,s_{m-1}).
\]

The expectation of an initialization monomial is zero if some independent
Gaussian exponent is odd and is a positive product of double factorials
otherwise.  Hence

\[
 \mathcal F_{m,n}(\mathbf s)
\]

is a polynomial with nonnegative coefficients in the schedule variables.
Consequently, for deterministic schedules

\[
 0\le s_j\le\widetilde s_j (0\le j<m),
\]

one has

\[
 \mathcal F_{m,n}(\mathbf s)
 \le \mathcal F_{m,n}(\widetilde{\mathbf s}).
\tag{3.1}
\]

The fixed-schedule quadratic width theorem gives the limit of each side at
every fixed $m$ and schedule.  Passing to the limit preserves (3.1):

\[
 \mathcal F_m(\mathbf s)
 \le\mathcal F_m(\widetilde{\mathbf s}).
\tag{3.2}
\]

This proof uses formal coefficient positivity before Gaussian expectation;
it does not assume that the raw Gaussian coordinates themselves are
positive.

## 3. The adaptive residual schedule becomes deterministic width first

Fix $m$ and $h$.  The loss recursion has the width-first representation

\[
 F_k^h=\mathcal F_k(s_0,\ldots,s_{k-1}), 
 s_k=h(1-F_k^h).
\tag{4.1}
\]

Here every $s_k$ is deterministic.  To prove (4.1), induct on $k$.
At initialization, $f_{0,n}\to0$ in every finite $L^p$, so
$s_{0,n}\to h$.  Suppose the complete history through time $k$
converges in every finite moment and $f_{k,n}\to F_k^h$.  Multiplication
by

\[
 s_{k,n}=h(1-f_{k,n})
\]

adds only one scalar polynomial gate to the fixed-horizon quadratic
chronology.  The quadratic mixed-moment inequalities and the finite
moment-order tower therefore give convergence of the next forward,
backward, Gram, response, and output bundles in every fixed $L^p$.
Their limiting update is (2.2) with
$s_k=h(1-F_k^h)$.  This proves the induction.

No estimate uniform in $m$ is used here.  Width is taken to infinity for
each separately fixed finite schedule, exactly in the required order.

Until the first time $F_k^h\ge\delta$, (4.1) gives

\[
 s_k>(1-\delta)h>0.
\tag{4.2}
\]

## 4. Constant-step quadratic feature ascent diverges

The established all-order quadratic theorem states that, for every fixed
$\rho>0$,

\[
 \mathcal F_{2t}
 \left({\rho\over t},\ldots,{\rho\over t}\right)
 \longrightarrow+\infty.
\tag{5.1}
\]

Its proof retains a positive Wick term whose Gaussian degree grows as
$4^t$; it is not a Taylor truncation.  The activation in the present
theorem is exactly the $p=0,q=3^{-1/2}$ member covered by (5.1).

## 5. Proof of the initial layer

Fix $0<\delta<1$ and an arbitrary $0<\varepsilon<T$.  Let

\[
 t_N=\left\lfloor{\varepsilon\over2h_N}\right\rfloor.
\]

Then $t_N\to\infty$, $2t_Nh_N\le\varepsilon$, and
$t_Nh_N\to\varepsilon/2$.  Choose

\[
 \rho_*={(1-\delta)\varepsilon\over4}>0.
\tag{6.1}
\]

For all sufficiently large $N$,

\[
 {\rho_*\over t_N}\le(1-\delta)h_N.
\tag{6.2}
\]

Suppose, toward a contradiction, that

\[
 F_k^{h_N}<\delta,  0\le k\le2t_N.
\tag{6.3}
\]

Equations (4.1)--(4.2) make the adaptive loss trajectory a deterministic
feature trajectory whose first $2t_N$ steps all obey

\[
 s_k\ge(1-\delta)h_N\ge{\rho_*\over t_N}.
\]

Schedule monotonicity (3.2) therefore yields

\[
 F_{2t_N}^{h_N}
 \ge
 \mathcal F_{2t_N}
 \left({\rho_*\over t_N},\ldots,{\rho_*\over t_N}\right).
\tag{6.4}
\]

The right side tends to $+\infty$ by (5.1), contradicting (6.3).
Thus, for all large $N$, the first hitting time is at most
$2t_Nh_N\le\varepsilon$.  Since $\varepsilon>0$ was arbitrary,
(1.3) follows.

Let $\overline F_N$ be the piecewise-linear interpolation of the grid
outputs.  At the first hit, the preceding grid value is below $\delta$
and the new value is at least $\delta$.  Hence there is
$r_N\le\tau_N(\delta)$ with

\[
 \overline F_N(r_N)=\delta,  r_N\to0.
\]

If $\overline F_N\to F$ uniformly and $F$ were continuous with
$F(0)=0$, then

\[
 \delta=\overline F_N(r_N)\longrightarrow F(0)=0,
\]

a contradiction.  At the same times,

\[
 \ell_N(r_N)={1\over2}(1-\delta)^2
 \ne{1\over2}=\ell_N(0),
\]

which proves the loss assertion.

## 6. What remains open about the terminal paired discrepancy

The comparison uses only the pre-hitting region $F<\delta<1$, where all
effective feature steps are nonnegative.  If a step overshoots the label,
then $1-F<0$; coefficientwise schedule monotonicity no longer applies.
The theorem therefore gives no endpoint lower bound for

\[
 \left|\ell_{2t}(h)-\ell_t(2h)\right|.
\]

In particular, an instantaneous-layer scenario in which both meshes settle
to the same target loss for every fixed positive time is compatible with
the theorem, although it is not a classical gradient flow because it is
discontinuous at initialization.  Proving or refuting terminal paired-loss
convergence requires a post-hitting signed-schedule analysis not supplied
by the positive-polynomial feature theorem.
