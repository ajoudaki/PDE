# Internal check of the order-two/three tanh bounds

This is a bounded internal cross-check, not an isolated review or a promotion
approval. Authorized scientific inputs were the complete TANH_LOWER_ROUTE.md,
Sections 1 and 4 of TANH_UPPER_ROUTE.md, and the maintained notation. I did
not inspect the upper route's conditional growing-order theorem or re-audit
the coordinatewise analytic route. The canonical-notation, rigorous-mathematics,
and research-audit instructions were applied. No experiment or external
source was used.

Rechecked source hashes:

- TANH_LOWER_ROUTE.md:
  53463b440ab0d9fba6a8e7e4c4a41a4b2942747f40dcfb6bc20e91f6ccfb19a1.
- TANH_UPPER_ROUTE.md:
  66057d8fc64e246e8b03b6c5824d0928c664072a199e3bd4f0ac439c621e8885.

**Verdict:** the requested two-sided order-two/three bound is verified for
the assigned scope. The lower author corrected the remainder coefficient
identified in the initial check, and the amended proof preserves both final
constants. No blocking issue remains in the checked statement. An explicit
sufficient joint width threshold is derived below. This status does not
extend to a growing-order theorem or a promotion review.

## Checked statement

Use the two-hidden-layer tanh network, zero initial readout, independent
Gaussian weights, mobilities $(n,1,n)$, and half-mean squared loss in the two
source notes. Let $m\ge2$, let the inputs be arbitrary fixed unit vectors, put
$Y=\|y\|_2/\sqrt m$, and let $\gamma>0$ be the smallest eigenvalue of the
population second-layer feature Gram. Set

\[
\lambda=\gamma/m,\qquad 0<Y\le\lambda/64.
\]

All these quantities are fixed independently of width. For $q=2$ or $3$,
let $f^{(q)}$ be the frozen-top NTH initialized from the same network.
For every $0<\delta<1$, the sufficient condition

\[
n\ge247808\,\lambda^{-4}\log\frac{10m^2}{\delta}
\tag{A}
\]

gives the joint event, with probability at least $1-\delta$, on which the
dense and frozen-order flows exist globally, their predictions have limits,
and

\[
\frac{Y^3\lambda^8}{384\cdot10^{15}}
\ \le\
\sup_{t\in[0,\infty]}\sup_{v\in\mathcal X}
|f^{(q)}(t,v)-f(t,v)|
\ \le\
7300\,\frac{Y^3}{\lambda^3}.
\tag{B}
\]

Here $\mathcal X$ is either the full unit input sphere or any declared finite
panel containing all training inputs. The upper bound on a finite panel
follows from the sphere bound. The lower bound uses a training input and a
strictly positive time. The fitted endpoint is included.

Condition (A) is deliberately loose. It does not impose an $n$-dependent
label restriction. Statement (B) is a fixed-order result and gives no
growing-order accuracy or storage law.

## Amended lower remainder verified

Equation (10) of the corrected lower route asserts

\[
\|u(t)-tH_y(t)\|_2/\sqrt n
\le B^2Y^3t^3/3+Yt^2/2,\qquad B^2=82.
\]

The factor $1/3$ is correct. Its displayed justification uses
$\|\dot H_y(\tau)\|_2/\sqrt n\le B^2Y^3\tau$, which yields exactly

\[
\begin{aligned}
\int_0^t\frac{\|H_y(s)-H_y(t)\|_2}{\sqrt n}\,ds
&\le B^2Y^3\int_0^t\int_s^t\tau\,d\tau\,ds\\
&=B^2Y^3\int_0^t\tau^2\,d\tau\\
&=\frac{B^2}{3}Y^3t^3.
\end{aligned}
\tag{C}
\]

The previous version had $1/6$ at this step. The amended version uses
$E=1/2+B^2/3$ and $C_E=2B^2(E+1)=14186/3$, which are correct on
$0\le t\le1$ when $Y\le1$. Its sharper short-time estimate is also valid:
$E_{\rm eff}(t)=1/2+(B^2/3)Y^2t\le1$ for $t\le3/(2B^2)$.

For the requested final bound, it is enough to work on

\[
0\le t\le T_0=\lambda^2/10^5.
\]

The lower argument only needs $Y\le1$, which the present label condition
implies. Since $T_0\le10^{-5}$, (C) gives

\[
\frac{\|u(t)-tH_y(t)\|_2}{\sqrt n}
\le Yt^2\left(\frac12+\frac{82}{3}Y^2t\right)
\le Yt^2.
\tag{D}
\]

Use the local bound $E_{\rm eff}\le1$, giving error coefficient at most
$2B^2(1+1)=328$ on this interval.
All subsequent lower estimates then hold because

\[
T_0\le T_A,\qquad
T_0\le\frac{a}{328}=\frac{\lambda^2}{10496},\qquad
T_0\le\frac{a}{4C_K}=\frac{\lambda^2}{20992},
\]

where $a=\lambda^2/32$ and $C_K=164$. The displayed formula for
$T_A=\min\{1,\sqrt{\lambda/(510\sqrt2)}\}$ also exceeds $T_0$.
Consequently the lower proof yields

\[
\max_a|f_a(T_0)-f_a^{(q)}(T_0)|
\ge\frac{a}{12}Y^3T_0^3
=\frac{Y^3\lambda^8}{384\cdot10^{15}}.
\]

The amended standalone interval statement takes
$T=\min\{T_A,3/(2B^2),a/(4B^2),a/(4C_K)\}$ and use (D) with
$Y\le1$ on that interval. This includes $T_0$, so the amended proof establishes
the original final constant. No stronger label assumption is needed: the
early-time argument uses $Y\le1$, already implied by the original combined
condition $Y\le\lambda/64$.

## Checks of the lower argument

The Gaussian Poincare step is valid. The scalar
$\psi(G)=H(Q^{(1)1/2}G)|H(Q^{(1)1/2}G)|$ is bounded, odd, and continuously
differentiable with bounded gradient. Its mean is zero, and

\[
\mathbb E\psi^2=\mathbb EH^4,\qquad
\mathbb E\|\nabla\psi\|_2^2
=4\mathbb E[H^2d^\top Q^{(1)}d].
\]

The interpolation proof in the note establishes the required Poincare
inequality, including singular $Q^{(1)}$ by the square-root representation.
Since $\|c\|_2^2=1/m$, the final-Gram gap indeed gives
$\mathbb EH^2\ge\gamma/m=\lambda$, and hence
$a_0=\lambda^2/4$ in its equation (5).

The covariance-interpolation constant $22$ also checks out. For
$D=d^\top Qd$ and $\|c\|_1\le1$,

\[
|H|\le1,\quad
\sum_i|\partial_iH|\le1,\quad
\sum_{ij}|\partial_{ij}H|\le2,\quad
\sum_i|\partial_iD|\le4,\quad
\sum_{ij}|\partial_{ij}D|\le20.
\]

The Hessian entrywise sum for $H^2D$ is therefore at most
$6+16+20=42$. Covariance interpolation costs at most
$21\|Q-Q'\|_{\max}$; the direct change of $Q$ costs at most
$\|Q-Q'\|_{\max}$. Positive semidefinite covariance paths with entries
bounded by one preserve these estimates. Adding a vanishing diagonal
regularization justifies singular endpoints without changing the limiting
bound.

The two Hoeffding bounds and the Gaussian operator-net bound therefore give
the stated lower initialization failure probability

\[
2e^{-\alpha n}
+2m^2e^{-n\lambda^4/247808}
+e^{-n\lambda^4/128},
\qquad \alpha=8-2\log9>0.
\tag{E}
\]

In the deterministic time argument, the norm bounds in equation (8), the
three-factor estimate for $A^{(2)}$, the positivity of the hidden-kernel
contribution, and the operator estimate
$\|K(t)-K(0)\|_{\rm op}\le mC_KY^2t^2$ are consistent with the mobility
normalization. The Duhamel formula has the correct sign and factor $1/m$.
Its scalar integrand remainder is bounded by
$m^2C_KY^4ts^2$: the propagator difference contributes $t-s$ and replacing
$y-f(s)$ by $y$ contributes $s$. Their sum is $t$. After dividing by
$m^2$ and integrating, the lower constant is $a/12$, as claimed.

Freezing the initially zero third tensor does exactly freeze the second
tensor. Thus the order-three prediction agrees with the order-two prediction;
the argument is about the surrogate's own residual at the same physical time.

## Checks of the upper argument

The real-flow bootstrap uses the correct mobility norm

\[
\|\dot\theta\|_{\rm par}^2
=\|\dot W^{(1)}\|_F^2/n+
 \|\dot W^{(2)}\|_F^2+\|\dot u\|_2^2/n
=-\rho\dot\rho.
\]

Before either stop, the feature Gram gap gives
$\rho(t)\le Ye^{-\lambda t/4}$. Cauchy--Schwarz then bounds the complete
parameter length by $2Y/\sqrt\lambda$. The two hidden displacements in
equation (24) follow, and their forward propagation gives the uniform sphere
feature displacement

\[
D_h=584Y^2/\lambda^{3/2}.
\]

The label assumption implies
$D_h\le(584/4096)\sqrt\lambda$. This strictly improves the feature stop,
since $1/\sqrt2-584/4096>1/2$, and also strictly improves the hidden
operator stop. The global continuation, fitting, and finite parameter length
claims follow at fixed width.

The kernel displacement estimate

\[
D\le1496Y^2/\lambda^{3/2}
\]

correctly includes both hidden blocks with the stated mobilities. The
constant-kernel propagator calculation gives training RMS error at most
$DY/\lambda$; the maximum of
$e^{-\lambda t/4}-e^{-\lambda t/2}$ is $1/4$.

The sphere argument correctly handles the part of the readout difference
orthogonal to the initialized training-feature span. In particular, it does
not infer a sphere error bound directly from the training error. Its
perpendicular bound is $4D_hY/\lambda$, while the initialized Gram gap
controls the parallel component by

\[
\sqrt{2/\lambda}\left(DY/\lambda+2D_hY/\sqrt\lambda\right).
\]

Adding the output's current-versus-initial feature difference gives

\[
(3504+2664\sqrt2)Y^3/\lambda^3
<7300Y^3/\lambda^3.
\]

The finite parameter length and the exponentially decaying frozen residual
also justify the endpoint and uniform sphere limits. The note appropriately
states that evaluating arbitrary new sphere inputs requires an initialized
query-feature evaluator, whose possible dense storage cannot be omitted.

## Explicit probability for the upper initialization event

Let $\mathcal T(Q)_{ab}=\mathbb E[\tanh Z_a\tanh Z_b]$ for $Z\sim N(0,Q)$.
For $a\ne b$, the scalar integrand has two pure second derivatives bounded
by $2$ and two mixed derivatives bounded by $1$; their absolute sum is at
most $6$. For $a=b$, the second derivative of $\tanh^2z_a$ is also bounded
by $6$. Gaussian covariance interpolation therefore gives, including
singular endpoints,

\[
\|\mathcal T(Q)-\mathcal T(Q')\|_{\max}
\le3\|Q-Q'\|_{\max}.
\tag{F}
\]

The first-layer empirical Gram $Q_n$ has independent bounded row
contributions. Hoeffding gives

\[
\Pr\{\|Q_n-Q^{(1)}\|_{\max}>\lambda/12\}
\le2m^2e^{-n\lambda^2/288}.
\]

Conditional on that first layer, the second-layer feature rows are
independent and their products lie in $[-1,1]$. Thus

\[
\Pr\{\|K_2(0)-\mathcal T(Q_n)\|_{\max}>\lambda/4\mid Q_n\}
\le2m^2e^{-n\lambda^2/32}.
\]

On the intersection, (F) gives
$\|K_2(0)-Q^{(2)}\|_{\max}\le\lambda/2=\gamma/(2m)$.
Since a symmetric $m\times m$ matrix has operator norm at most $m$ times
its largest entry magnitude, $K_2(0)\succeq\gamma I_m/2$.
Combining with the operator-net event gives upper-event failure at most

\[
2e^{-\alpha n}
+2m^2e^{-n\lambda^2/288}
+2m^2e^{-n\lambda^2/32}.
\tag{G}
\]

In particular, $n\ge288\lambda^{-2}\log(6m^2/\delta)$ suffices for the
upper event alone.

The operator event is common to (E) and (G), so the joint failure bound is

\[
2e^{-\alpha n}
+2m^2e^{-n\lambda^4/247808}
+e^{-n\lambda^4/128}
+2m^2e^{-n\lambda^2/288}
+2m^2e^{-n\lambda^2/32}.
\]

Under (A), every exponential is at most $\delta/(10m^2)$; here
$0<\lambda\le1$ and $\alpha>1$ suffice for the comparisons.
The prefactors sum to $3+6m^2\le10m^2$, proving the promised confidence.

## Scope of the conclusion

The source-proof coefficient correction is incorporated and verified at the
hash recorded above. The corrected argument establishes exactly the requested
two-sided constants for $q=2,3$, with the explicit width condition (A) and the
original fixed label range $0<Y\le\lambda/64$. No blocking issue remains in
the assigned statements. This check does not validate growing-order
convergence, nonconvergence, a dense-variability rate, or a width-dependent
storage lower bound. Those are unresolved beyond this check's scope; the
fixed-order theorem does not resolve the user's growing-order task.
