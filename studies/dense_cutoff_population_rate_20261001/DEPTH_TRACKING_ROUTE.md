# Arbitrary-depth tracking from a finite dense carrier envelope

2026-10-03. Scoped deterministic proof extension. This note proves an
implication from the actual dense carrier maximum to the actual autonomous
residual-RMS Legendre closure at the same width. It does **not** prove the
probability of the carrier envelope. The proof is complete within the
stated deterministic hypotheses; independent reconstruction is pending.

The improvement over directly substituting a zero tail into the final
estimate of `paper/proof_tracking.tex` is that zero tail can be used earlier.
The square-root feedback disappears, and only one exponential stability
factor is needed. A dense backward history, recorded in the closure's own
clock and multiplied by the closure's residual direction, supplies the
second projection factor. No clipping is needed even in this proof.

Inputs: complete current `paper/main.tex` and every included mathematical
file (`results.tex`, `proof_alltime.tex`, `proof_tracking.tex`,
`proof_finite_time.tex`, `comparison_appendix.tex`, `sphere_appendix.tex`);
`docs/index.qmd`, `docs/notation.qmd`; own-study
`NONORTHOGONAL_DIRECT_ROUTE.md`, `NONORTHOGONAL_CHECK.md`,
`Q_ORDER_RESULT.md`, and `Q_ORDER_POSITIVE_ROUTE.md`. Required canonical
notation/neural conventions, rigorous-proof and conjecture-investigation
skills and the shared process instructions were applied. No new sibling
route was read. No experiment, manuscript edit, or Git write was performed.

## 1. Model and deterministic hypotheses

Fix depth $L\ge2$, input dimension $d$, and training pairs

\[
(x_a,y_a)\in\mathbb R^d\times\mathbb R,\qquad
v_a=x_a/\sqrt d,\qquad a=1,\ldots,m.
\]

Neither normalization nor orthogonality of the inputs is required. The
inputs, depth and sample count are fixed as width varies. For each hidden
layer choose a scalar activation $\phi_\ell\in C^1(\mathbb R)$ such that

\[
|\phi_\ell(0)|\le a_*,\quad
\|\phi_\ell'\|_\infty\le s_*,\quad
|\phi_\ell'(u)-\phi_\ell'(v)|\le j_*|u-v|.
\tag{1}
\]

The finite constants in (1) are independent of width. The activation
values need not be bounded. Put $W^{(1)}\in\mathbb R^{n\times d}$,
$W^{(\ell)}\in\mathbb R^{n\times n}$ for $2\le\ell\le L$, and
$w\in\mathbb R^n$. The canonical model is

\[
z_a^{(1)}=W^{(1)}v_a,\quad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\quad
f_a=\frac{w^\top h_a^{(L)}}n,
\]
\[
r_a=f_a-y_a,\qquad
\rho=\left(\frac1m\sum_a r_a^2\right)^{1/2},\qquad
\mathcal L=\rho^2,\qquad
Y=\left(\frac1m\sum_a y_a^2\right)^{1/2}.
\]

Define the full backward carriers and backward responses by

\[
k_a^{(L)}=w,\quad
k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}
\quad(\ell<L),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
\tag{2}
\]

The dense vector field $F$ uses block mobilities
$(n,1,\ldots,1,n)$:

\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\quad
\dot W^{(\ell)}=-\frac2{mn}\sum_a
r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},
\quad
\dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\tag{3}
\]

Use zero initial readout and the same initialization in both systems.
Fix an initialization satisfying the paper's event $\mathcal G_n$:
fixed hidden operator bounds, first-preactivation RMS bounds, a full
first-weight Frobenius bound $\|W_0^{(1)}\|_F/\sqrt n\le C_0$, and
the initial readout-feature Gram bound

\[
\Gamma_w(0)=H_L(0)^\top H_L(0)/(mn)\succeq\lambda I_m,
\qquad\lambda>0.
\tag{4}
\]

No randomness is needed after fixing this initialization. For canonical
independent Gaussian initialization, the paper proves that such events
have probability tending to one if the limiting feature Gram has a
strictly positive gap. That initialization fact does not by itself prove
the trained carrier envelope below.

For every integer $q\ge1$, the comparison path is exactly the paper's
autonomous learning-speed closure. Its own clock is
$\dot{\widehat\tau}=\widehat\rho$, $\widehat\tau(0)=1$. It stores
Legendre moments of $\widehat h_a^{(\ell-1)}$ and

\[
\widehat b_a^{(\ell)}=\widehat c_a\widehat\delta_a^{(\ell)},
\qquad \widehat c_a=\widehat r_a/\widehat\rho.
\]

The forward prefix is constant and the backward prefix zero. With
$p_j(1)=1$ the shifted Legendre polynomials, its exact reconstruction is

\[
\widehat W^{(\ell)}=W_0^{(\ell)}-
\frac2{mn\widehat\tau}\sum_{a,j<q}(2j+1)
\bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
\tag{5}
\]

Each moment obeys

\[
\dot M_j=S-\frac{\widehat\rho}{\widehat\tau}
\left(jM_j+\sum_{i<j}(2i+1)M_i\right),
\tag{6}
\]

where $S=\widehat\rho\widehat h_a^{(\ell-1)}$ or
$S=\widehat r_a\widehat\delta_a^{(\ell)}$. The first layer and readout
use (3) at the reconstructed state. Thus no division by residual RMS
occurs in the algorithm. Division below only describes histories on
nonstationary paths. If $Y=0$, both paths are stationary and the theorem
is immediate; hence take $0<Y\le Y_*$ below.

For sufficiently small $Y_*$, depending on (1), (4), the fixed depth
and inputs, the deterministic fitting portion of `proof_alltime.tex`
proves simultaneously for the dense path and all closure orders:

\[
\begin{gathered}
\rho_j(t)\le Ye^{-\kappa t},\qquad
\int_t^\infty\rho_j(s)\,ds\le\rho_j(t)/\kappa,
\qquad j\in\{D,q\},\\
\max_{\ell\ge2}\|W_j^{(\ell)}(t)\|_{\rm op}\le C,
\quad\max_{\ell,a}\frac{\|h_{j,a}^{(\ell)}\|_2}{\sqrt n}\le C,
\quad\max_{\ell,a}\frac{\|\delta_{j,a}^{(\ell)}\|_2}{\sqrt n}\le CY,\\
\frac{\|\dot W_j^{(1)}\|_F}{\sqrt n}
+\sum_{\ell=2}^L\|\dot W_j^{(\ell)}\|_F\le CY\rho_j,
\quad \frac{\|\dot w_j\|_2}{\sqrt n}\le C\rho_j,\\
\max_{\ell,a}\frac{\|\dot z_{j,a}^{(\ell)}\|_2+
\|\dot h_{j,a}^{(\ell)}\|_2}{\sqrt n}\le CY\rho_j,
\qquad \|\dot{\widehat c}\|_m\le C.
\end{gathered}
\tag{7}
\]

Here $\|u\|_m^2=m^{-1}\sum_a u_a^2$. Both paths exist globally;
their physical limits exist. Their residuals stay positive on each finite
time interval when $Y>0$. These facts are proved before comparison, using
the exact defect identity and all-order forward regularity, so invoking
them is not a comparison bootstrap. The closure tangent Gram has a
positive gap and fixed upper bound. All constants in the remainder of
this note may depend on these fixed data and $Y_*$, but not on
$n,q,t,M$. The sharper factor $Y$ in a stability exponent is retained
where useful.

Assume the actual dense path has the deterministic all-layer envelope

\[
\sup_{t\ge0}\max_{\ell,a}\|k_{D,a}^{(\ell)}(t)\|_\infty\le M,
\qquad M\ge0.
\tag{8}
\]

This is an input to the theorem, never an algorithmic cutoff.

## 2. Deterministic theorem

There are constants $C,K,c_*>0$ with the following property. Set

\[
A_M=C e^{K M}\ge1.
\tag{9}
\]

One can retain $K=C_1Y$ with $C_1$ independent of
$0<Y\le Y_*$. If

\[
q\ge c_*(1+M)A_M,
\tag{10}
\]

then the actual unclipped closure satisfies

\[
D_{n,q}:=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_{n,D}(t))
\le C A_M\frac{1+M+\sqrt{\log(e+q)}}{q^2},
\tag{11}
\]

where

\[
d_n(\widehat\theta,\theta_D)=
\frac{\|\widehat W^{(1)}-W_D^{(1)}\|_F}{\sqrt n}
+\sum_{\ell=2}^L\|\widehat W^{(\ell)}-W_D^{(\ell)}\|_F
+\frac{\|\widehat w-w_D\|_2}{\sqrt n}.
\]

All statements hold simultaneously for every order satisfying (10) on
the same deterministic initialized trajectory. The corresponding
whole-input estimate, for every fixed probability law $\mu$ with
finite second moment, is

\[
\left(\int\sup_{t\ge0}
|\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|^2d\mu(x)\right)^{1/2}
\le C_\mu A_M\frac{1+M+\sqrt{\log(e+q)}}{q^2}.
\tag{12}
\]

The time supremum includes the fitted endpoint. A fixed bounded query
set has the corresponding uniform absolute prediction estimate.

### 2.1 Exact defect and forward projection factor

At a current clock endpoint $A=\widehat\tau(t)$, let $\Pi_q^A$
be orthogonal projection onto polynomials of degree below $q$ in
$L^2(0,A;\mathbb R^n)$. Differentiating (5)–(6) gives

\[
\dot{\widehat\theta}=F(\widehat\theta)+E,\qquad E_1=E_w=0,
\quad
E_\ell=\frac{2\widehat\rho}{mn}\sum_a
(\widehat b_a^{(\ell)}-\widehat b_a^{(\ell)*})
(\widehat h_a^{(\ell-1)}-\widehat h_a^{(\ell-1)*})^\top.
\tag{13}
\]

A star evaluates the projected history at its current right endpoint.
For any inserted history $u$, its projection energy satisfies

\[
\frac d{dt}\|(I-\Pi_q^A)u\|_{L^2(0,A)}^2
=\widehat\rho(t)\|u(t)-u^*(t)\|_2^2.
\]

The derivative of the projected polynomial pairs to zero with the
orthogonal residual, proving this identity; every initial projection
error is zero. The rank-one Frobenius identity and Cauchy–Schwarz thus give

\[
\int_0^t\|E_\ell(s)\|_Fds
\le\frac2m\sum_a
\frac{\|(I-\Pi_q^A)\widehat b_a^{(\ell)}\|_{L^2}}{\sqrt n}
\frac{\|(I-\Pi_q^A)\widehat h_a^{(\ell-1)}\|_{L^2}}{\sqrt n}.
\tag{14}
\]

The weighted Legendre inequality used below is

\[
\|(I-\Pi_q^A)u\|_{L^2}^2
\le\frac1{q(q+1)}\int_0^A\xi(A-\xi)\|u'(\xi)\|_2^2d\xi.
\tag{15}
\]

It follows by expanding in normalized Legendre eigenfunctions of
$-\partial_\xi[\xi(A-\xi)\partial_\xi]$, whose eigenvalues are
$j(j+1)$, then applying Bessel to the weighted derivatives. It holds
componentwise for every $H^1$ history. From (7), division by the
positive clock speed gives $\|\partial_\xi\widehat h\|_2/\sqrt n\le CY$.
It vanishes on the prefix; the physical clock mass is at most $CY$.
Consequently (15) gives, uniformly in $A\le1+Y/\kappa$,

\[
\frac{\|(I-\Pi_q^A)\widehat h_a^{(\ell-1)}\|_{L^2}}{\sqrt n}
\le CY^{3/2}/q\le C/q.
\tag{16}
\]

### 2.2 Stability using the dense envelope

Forward subtraction gives

\[
\max_{\ell,a}\frac{\|\widehat z_a^{(\ell)}-z_{D,a}^{(\ell)}\|_2
+\|\widehat h_a^{(\ell)}-h_{D,a}^{(\ell)}\|_2}{\sqrt n}
\le C d_n(t).
\tag{17}
\]

Indeed, a hidden link subtracts as
$(\widehat W-W_D)h_D+\widehat W(\widehat h-h_D)$, and (7)
controls the two multipliers. A gate difference times a dense carrier is
bounded using (1), (8) by $j_*M\|\widehat z-z_D\|_2$. The rest of
the backward difference uses bounded gates and bounded operators. Thus
downward induction gives

\[
\max_{\ell,a}\frac{\|\widehat\delta_a^{(\ell)}-
\delta_{D,a}^{(\ell)}\|_2}{\sqrt n}
\le C(1+M)d_n(t).
\tag{18}
\]

The new $M$-contributions add through fixed depth: an already formed
backward difference is propagated by a bounded gate and operator, not
multiplied by another $M$.

Let $e_E=\sum_{\ell=2}^L\|E_\ell\|_F$ and
$\epsilon(t)=\int_0^t e_E(s)ds$. Expanding each gradient-product Gram
using (17)–(18) yields
$\|\widehat\Gamma-\Gamma_D\|_{\rm op}\le C(1+M)d_n(t)$.
For $u=\widehat r-r_D$, exact residual subtraction gives

\[
\dot u=-2\widehat\Gamma u
-2(\widehat\Gamma-\Gamma_D)r_D+\widehat J E.
\]

The gap in (7) and $\|\widehat J E\|_m\le CY e_E\le C e_E$
imply

\[
D^+\|u\|_m\le-\lambda_1\|u\|_m
+C(1+M)\rho_Dd_n+C e_E,
\]

with fixed $\lambda_1>0$. Regularizing the norm by
$(\|u\|_m^2+\eta^2)^{1/2}$ justifies the inequality at $u=0$.
Since $u(0)=0$, integration and discarding its nonnegative terminal
norm give

\[
\int_0^t\|u\|_m ds\le C(1+M)\int_0^t\rho_Dd_n ds+C\epsilon(t).
\tag{19}
\]

Subtract (3), expanding each product into its residual, backward and
forward differences, and add the defect. Equations (17)–(19) imply

\[
d_n(t)\le C\epsilon(t)+C(1+M)\int_0^t\rho_D(s)d_n(s)ds.
\]

On a fixed terminal interval replace $\epsilon(s)$ by its terminal
value and integrate the scalar inequality. Since
$\int_0^\infty\rho_D\le Y/\kappa$,

\[
D_{n,q}\le A_M\epsilon,\qquad
\epsilon=\int_0^\infty e_E(s)ds,\qquad
A_M\le C e^{C_1YM}.
\tag{20}
\]

The coarse defect estimate and (7) make $D_{n,q},\epsilon$ finite
before this comparison. Equation (20) is the zero-tail specialization
of the paper's damping argument, reconstructed here without any tail term.

### 2.3 A dense backward history in the closure clock

Differentiate the dense backward recursion almost everywhere. Lipschitz
continuity of $\phi_\ell'$ gives

\[
\left\|\frac d{dt}\phi_\ell'(z_{D,a}^{(\ell)})
\odot k_{D,a}^{(\ell)}\right\|_2/\sqrt n
\le j_*M\|\dot z_{D,a}^{(\ell)}\|_2/\sqrt n
\le C M Y\rho_D.
\]

At the top the other term is a bounded gate times $\dot w_D$. At a
lower layer it is a bounded gate times

\[
\dot W_D^{(\ell+1)\top}\delta_{D,a}^{(\ell+1)}
+W_D^{(\ell+1)\top}\dot\delta_{D,a}^{(\ell+1)}.
\]

The first has normalized norm at most $CY^2\rho_D$; the second
propagates the derivative through a bounded operator. Fixed-depth
induction therefore proves

\[
\max_{\ell,a}\|\dot\delta_{D,a}^{(\ell)}\|_2/\sqrt n
\le C(1+M)\rho_D.
\tag{21}
\]

This step uses no derivative of a gate beyond its global Lipschitz
constant. Lipschitz functions of absolutely continuous finite-dimensional
paths are absolutely continuous and satisfy the asserted chain inequality
almost everywhere, so classical second derivatives are unnecessary.

Define the auxiliary physical-time path

\[
\widetilde b_a^{(\ell)}(t)
=\widehat c_a(t)\delta_{D,a}^{(\ell)}(t).
\tag{22}
\]

It is placed at $\xi=\widehat\tau(t)$, with zero prefix. It is only
a proof history; it is not inserted into (5)–(6). Since $m$ is fixed,
$|\widehat c_a|+|\dot{\widehat c}_a|\le C$. Equations (7), (21) give

\[
\|\widetilde b_a^{(\ell)}\|_2/\sqrt n\le CY,
\qquad
\|\dot{\widetilde b}_a^{(\ell)}\|_2/\sqrt n
\le C[Y+(1+M)\rho_D].
\tag{23}
\]

For $T\ge0$, freeze (22) after physical time $T$, keeping the
unfrozen history if the current terminal time is below $T$. Denote the
resulting clock history by $\widetilde b_{a,T}^{(\ell)}$. Both its
prefix join and its freeze join are continuous: the former uses $w_D(0)=0$.
On every finite interval before freezing the closure residual is positive,
so this history belongs to $H^1(0,A;\mathbb R^n)$.

The remaining closure clock mass after $T$ is at most
$Y e^{-\kappa T}/\kappa$. From (23),

\[
\|\widetilde b_a^{(\ell)}-
\widetilde b_{a,T}^{(\ell)}\|_{L^2(0,A)}/\sqrt n
\le C e^{-\kappa T/2}.
\tag{24}
\]

For $s\le\min(t,T)$, the upper endpoint $A=\widehat\tau(t)$
satisfies

\[
A-\widehat\tau(s)
\le\int_s^\infty\widehat\rho(u)du
\le\widehat\rho(s)/\kappa.
\]

Change variables $d\xi=\widehat\rho(s)ds$ in the weighted energy:

\[
\begin{aligned}
\frac1n\int_0^A\xi(A-\xi)
\|\partial_\xi\widetilde b_{a,T}^{(\ell)}\|_2^2d\xi
&=\frac1n\int_0^{\min(t,T)}
\frac{\widehat\tau(s)[A-\widehat\tau(s)]}{\widehat\rho(s)}
\|\dot{\widetilde b}_a^{(\ell)}(s)\|_2^2ds\\
&\le C\int_0^{\min(t,T)}[Y+(1+M)\rho_D(s)]^2ds\\
&\le C[T+(1+M)^2].
\end{aligned}
\tag{25}
\]

The final line uses $2uv\le u^2+v^2$ and
$\int_0^\infty\rho_D^2\le Y^2/(2\kappa)$. There is no ratio of
dense to closure residuals: the inverse closure clock speed canceled
against its own remaining clock mass before the dense derivative was
estimated. This is the reason histories from the two systems can be
paired without synchronizing their clocks.

Equations (15), (24), (25), and contraction of $I-\Pi_q^A$ imply

\[
\|(I-\Pi_q^A)\widetilde b_a^{(\ell)}\|_{L^2}/\sqrt n
\le C\left[\frac{1+M+\sqrt T}{q}+e^{-\kappa T/2}\right].
\tag{26}
\]

The actual and auxiliary histories use exactly the same closure residual
direction and clock. Thus (18) gives directly

\[
\begin{aligned}
\|\widehat b_a^{(\ell)}-\widetilde b_a^{(\ell)}\|_{L^2(0,A)}/\sqrt n
&\le C(1+M)\left(\int_0^t\widehat\rho(s)d_n(s)^2ds\right)^{1/2}\\
&\le C(1+M)D_{n,q}.
\end{aligned}
\tag{27}
\]

Again no residual comparison is used. Applying $I-\Pi_q^A$, whose
operator norm is one, preserves this estimate.

### 2.4 Source, absorption, and whole-input transfer

Use (16), (26), (27) in (14), sum the finitely many hidden links, and
increase the terminal time to infinity. The left side increases to the
absolute accumulated defect, while the right side is uniform. Hence

\[
\epsilon\le C\left[
\frac{1+M+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q
+\frac{(1+M)D_{n,q}}q\right].
\tag{28}
\]

Choose $T=2\log q/\kappa$, including $T=0$ at $q=1$. Then

\[
\epsilon\le C\frac{1+M+\sqrt{\log(e+q)}}{q^2}
+\frac{C(1+M)A_M}q\epsilon
\]

by (20). Choosing $c_*$ large enough in (10) makes the final
coefficient at most $1/2$. Absorption and another use of (20) prove
(11). This is an actual source-and-comparison proof at arbitrary fixed
depth. It does not assume the independent two-layer source bound survives.

For any query $x\in\mathbb R^d$, the first-layer full Frobenius bound
and (7) imply $\|W^{(1)}(t)\|_F/\sqrt n\le C$ on both paths.
Linear activation growth from (1), followed by forward subtraction through
bounded operators and slopes, gives

\[
\|h_j^{(\ell)}(t,x)\|_2/\sqrt n
\le C(1+\|x\|_2/\sqrt d),
\qquad
|\widehat f(t,x)-f_D(t,x)|
\le C(1+\|x\|_2/\sqrt d)d_n(t).
\tag{29}
\]

The readout identity is expanded into a readout difference and a feature
difference to obtain the second inequality. Taking the time supremum
before the $L^2(\mu)$ norm proves (12), with

\[
C_\mu=C\left(\int(1+\|x\|_2/\sqrt d)^2d\mu(x)\right)^{1/2}<\infty.
\]

This controls fidelity to the trained dense predictor, not its error
against unseen labels. No dense-to-population bias enters.

## 3. Why the square-root feedback is absent

With a nonzero dense carrier tail, the paper bounds the history mismatch
using an integral $\int\widehat\rho H_n(M,t)^2dt$. Replacing its clock
weight by the dense residual introduces
$Q_r=\int\|\widehat r-r_D\|_m dt$, and taking a square root gives
the term $q^{-1}\sqrt{Z_n+Q_r}$. Absorbing it produces an $A_M^2/q^2$
contribution.

Under (8), $H_n(M,t)=0$ at **every** time. Its weighted integral is
exactly zero under either clock. Equation (27) retains that information;
there is no $Q_r$ term to estimate. Setting $Z_n=0$ only in the
paper's final, already weakened bound leaves an avoidable $\sqrt{Q_r}$.
The earlier pointwise simplification, or equivalently the dense proxy
(22), removes it. The order threshold (10) remains and must be checked.

## 4. Explicit sufficient memory orders

Suppose $M_n\ge0$ is a deterministic envelope for (8) on events
$\Omega_n\subseteq\mathcal G_n$. Constants below do not depend on
the realized initialization within those events. A general sufficient
order is

\[
q_n=\left\lceil C\max\left\{
(1+M_n)e^{K M_n},\quad
n^{1/4}e^{K M_n/2}
[1+M_n+\sqrt{\log(e+n)}]^{1/2}
\right\}\right\rceil.
\tag{30}
\]

The first term enforces (10). For this choice,
$\log(e+q_n)\le C[1+M_n+\log(e+n)]$, hence

\[
1+M_n+\sqrt{\log(e+q_n)}
\le C[1+M_n+\sqrt{\log(e+n)}].
\]

The second term in (30), substituted in (11)–(12), therefore gives

\[
D_{n,q_n}\le Cn^{-1/2},\qquad
\mathcal E_\mu(\widehat f_{n,q_n},f_{n,D})\le C_\mu n^{-1/2}
\quad\text{on }\Omega_n.
\tag{31}
\]

This is a deterministic implication for arbitrary $M_n$, including the
elementary envelope $M_n=CY\sqrt n$ from the RMS tube. That elementary
choice gives no compression.

Write $N_n=\log(e+n)$. If $M_n\le cN_n^\beta$, the following
more explicit schedules result.

* **Bounded carrier maximum $(\beta=0)$.**
  $q_n=\lceil Cn^{1/4}N_n^{1/4}\rceil$ suffices. The logarithmic
  factor compensates for the endpoint-history freeze estimate.

* **Sublogarithmic maximum $(0<\beta<1)$.** For any fixed
  $a>Kc/2$,
  \[
  q_n=\left\lceil n^{1/4}e^{aN_n^\beta}\right\rceil
  =n^{1/4+o(1)}
  \tag{32}
  \]
  suffices for all large $n$. The surplus exponential absorbs the
  factor $N_n^{\max(\beta,1/2)}$, and
  $q_n/[(1+M_n)e^{KM_n}]\to\infty$ because the positive
  $\frac14\log n$ dominates every $O(N_n^\beta)$ term.
  At the exact exponential coefficient $a=Kc/2$, the explicit
  polynomial correction
  \[
  q_n=\left\lceil Cn^{1/4}e^{(Kc/2)N_n^\beta}
  N_n^{\max(\beta/2,1/4)}\right\rceil
  \tag{33}
  \]
  also suffices.

* **Gaussian-scale maximum $(\beta=1/2)$.** In particular,
  $q_n=\lceil n^{1/4}e^{a\sqrt{N_n}}\rceil$, $a>Kc/2$, gives
  strict root-width error at arbitrary fixed depth. The absorption
  threshold grows only as $e^{O(\sqrt{\log n})}\sqrt{\log n}$,
  below this chosen order. Neither a squared stability amplification nor
  an independent source bound is required.

* **Logarithmic maximum $(\beta=1)$.** Put $\alpha=Kc$.
  A sufficient schedule is
  \[
  q_n=\left\lceil C\max\{n^\alpha\log(e+n),
  n^{1/4+\alpha/2}[\log(e+n)]^{1/2}\}\right\rceil.
  \tag{34}
  \]
  Its power is $\max\{\alpha,1/4+\alpha/2\}$. For example,
  $\alpha=1/10$ gives $n^{3/10}\sqrt{\log n}$;
  $\alpha=1/2$ gives $n^{1/2}\log n$; and $\alpha=3/4$ gives
  $n^{3/4}\log n$. This schedule is sublinear for $\alpha<1$,
  but at fixed positive $\alpha$ does not reach $n^{1/4+o(1)}$.

* **Superlogarithmic power $(\beta>1)$.** With a fixed positive
  coefficient $Kc$, (30) is eventually dominated by its absorption
  term $N_n^\beta e^{KcN_n^\beta}$. This particular maximum-based
  estimate supplies no sublinear memory order. It is not a lower bound
  on the true approximation error or on other stability arguments.

For (32), or any $M_n=o(\log n)$, the moving-state count is

\[
2(L-1)mnq_n+n(d+1)+O(1)=n^{5/4+o(1)}
\]

at fixed $L,m,d$. The $L-1$ initialized $n\times n$ matrices
remain stored and used exactly. There is no total-storage or runtime
compression claim. If $\Pr(\Omega_n)\to1$ has separately been proved,
(31) holds at any fixed confidence for all sufficiently large widths;
the theorem itself does not supply that probability input.

## 5. An integrated-envelope refinement

The global maximum can be weakened in the deterministic proof. Define
the actual dense maximum profile

\[
M(t)=\max_{\ell,a}\|k_{D,a}^{(\ell)}(t)\|_\infty,
\]

and the finite quantities

\[
\begin{aligned}
\mathcal A&=C\exp\left\{C\int_0^\infty
\rho_D(t)[1+M(t)]dt\right\},\\
B_2&=\left(Y\int_0^\infty e^{-\kappa t}[1+M(t)]^2dt\right)^{1/2},\\
B_3&=\left(\int_0^\infty[1+M(t)]^2\rho_D(t)^2dt\right)^{1/2}.
\end{aligned}
\tag{35}
\]

At finite width the RMS physical tube makes them finite. The same
derivation gives $D\le\mathcal A\epsilon$, replaces (25) by
$C(T+B_3^2)$, and replaces (27) by $CB_2D$. Therefore

\[
q\ge C\mathcal A B_2
\quad\Longrightarrow\quad
D_{n,q}\le C\mathcal A
\frac{1+B_3+\sqrt{\log(e+q)}}{q^2}.
\tag{36}
\]

This can exploit small activity when large carrier coordinates occur.
An averaged neuron moment alone does not justify replacing $M(t)$
in (35): (18) multiplies an arbitrary parameter-induced gate difference
by the dense carrier coordinate. Controlling that product by an averaged
carrier norm would require an additional localization or response
estimate. No such estimate is silently assumed in (36).

## 6. Activation, data, and claim boundaries

The deterministic theorem uses exactly (1), not bounded activation values,
analyticity, oddness, a strictly positive derivative, or a classical
third derivative. Zero readout ensures the backward prefix joins
continuously; it is part of the theorem. ReLU and leaky ReLU do not meet
(1), whereas bounded smooth activations and the paper's bounded-slope,
Lipschitz-derivative unbounded activations are admissible when their
initial feature Gram has the required gap. A proof of a finite trained
carrier maximum can impose additional regularity or boundedness; that
would limit the final probabilistic theorem, not this deterministic step.

The fitting input is the feature-Gram gap, not invertibility of the raw
input Gram. Under independent Gaussian initialization one sufficient
criterion is nonzero, pairwise nonproportional inputs, nonpolynomial first
activation and nonconstant later activations in (1), as proved in
`proof_alltime.tex`. Linearly independent inputs and nonconstant
activations are another sufficient criterion. These are sufficient
conditions, not an exhaustive characterization. Compatible exact
symmetries may permit a weighted quotient, but neither that quotient nor
clock changes for incompatible labels are used here.

Constants may depend on the actual fixed dataset and its positive gap;
there is no uniform result over colliding data or increasing depth/sample
count. The result compares the dense and closure systems at the same
physical time with their original clocks. Both are unclipped. Neither
the auxiliary history nor the numerical envelope $M$ modifies the
algorithm or requires additional stored closure coordinates. The remaining
probabilistic obligation for a near-quarter-order theorem is a proved
sublogarithmic actual dense all-layer maximum (or sufficient integrated
envelopes in (35)) on events of the claimed confidence.
