# Independent constructive route: initialized three-sample rank and a trapping lemma

Status: **partial; the requested unconditional exponential theorem is not proved**.
This candidate was frozen independently before comparison with another proof
route. No numerical experiment was performed. The scientific input scope was
`docs/observable_p1.md` in full and `docs/global_nonlinear.md`, C.4.7.9 and
C.4.7.10.D.3 in full. No other scientific section or study was read. Required
research and rigorous-mathematics skills were read.

The exact model throughout is the active, sign-folded p=1 population closure:
`b1 in R4`, `b2 in R2`, full `M in R^(2x4)`, tanh, ridge `1/4096`, canonical
correlated lower marks, `w(0)=g`, `M(0)=D`, and `c(0)=0`. Both expectations
are separate population expectations. All three moving blocks and the
unhalved probability loss use the prescribed physical gradient metric.
Neither a finite population rule nor a neural-width limit is substituted.

The useful positive result is that a concrete balanced three-input geometry
has a full-rank initialized readout tangent, despite a two-mode symmetry in
its training trajectory. A complete quantitative local trapping lemma then
identifies precisely what a successful global reference argument must supply.

## 1. Exact equations and metric

For three unit inputs `u_i`, targets `y_i`, and strictly positive masses
`mu_i` summing to one, put

\[
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad
 z_i=b_2^TMa_i,\quad h_i=\tanh z_i,
 \quad f_i=E_2[c h_i],\quad r_i=f_i-y_i,
\]
\[
 d_i=E_2[b_2c\operatorname{sech}^2z_i],\qquad
 q_i=b_1^TM^Td_i.
\]

The exact velocities are

\[
 w'=-2\sum_i\mu_i r_i\operatorname{sech}^2(w\cdot u_i)q_i u_i,
 \quad c'=-2\sum_i\mu_i r_i h_i,
 \quad M'=-2\sum_i\mu_i r_i d_i a_i^T.
\]

In the Hilbert metric
\(\mathcal H=L^2(\Omega_1;\mathbb R^2)\oplus
L^2(\Omega_2)\oplus\mathbb R^{2\times4}\), the prediction gradient is

\[
 J_i=\big(\operatorname{sech}^2(w\cdot u_i)q_i u_i,
             h_i,d_i a_i^T\big).
\]

Let \(e_i=\sqrt{\mu_i}r_i\) and
\(K_{ij}=\sqrt{\mu_i\mu_j}\langle J_i,J_j\rangle_{\mathcal H}\).
Then exactly

\[
 \mathcal L=|e|^2,\qquad e'=-2Ke,\qquad
 \mathcal L'=-4e^TKe=-\|(w',c',M')\|_{\mathcal H}^2.
 \tag{1}
\]

At initialization, `c=0` makes both hidden-block components of `J_i` vanish,
so `K(0)` is precisely the weighted readout Gram. This is an identity at one
time, not a frozen-feature approximation to subsequent evolution.

## 2. A genuine balanced three-input family with initialized full rank

Consider

\[
 u_1=(\cos\theta,\sin\theta),\quad
 u_2=(\cos\theta,-\sin\theta),\quad u_3=-e_1,
 \qquad y=(1,1,-1),\qquad
 \mu=(1/4,1/4,1/2).
 \tag{2}
\]

For every sufficiently small positive `theta`, all three initialized
readout fields are linearly independent in the upper population. Therefore
`K(0)` is positive definite. In particular, these are three functionally
independent fitting constraints; none is a duplicate or an antipodal copy
of another.

Here is a proof using the exact retained contraction, including its reuse
response term. Use the scalar constants `v,s,beta,tau,alpha,gamma` from
`observable_p1.md`, write `eta=1/4096`, and put

\[
 S=\begin{pmatrix}v+\eta&\beta\\\beta&s+\eta\end{pmatrix},
 \qquad C=(\alpha v,\alpha\beta+\tau\gamma),\qquad
 c_0=\sqrt{\tau+\eta}.
\]

The notation `c_0` in this paragraph is a positive scalar normalization,
not the moving readout. Define the bounded lower scalar mark

\[
 \ell(G,Z)=c_0^{-1}CS^{-1}
       \binom{\tanh G}{\tanh(\sqrt\tau Z+\alpha\tanh G)}.
\]

If `E` is a further independent standard normal, set

\[
 T(\rho)=E\big[\ell(G,Z)
       \tanh(\rho G+\sqrt{1-\rho^2}E)\big],\qquad -1\le\rho\le1.
 \tag{3}
\]

The Cholesky algebra in the source gives exactly

\[
 (Da_0(u))_j=T(u_j),\qquad |u|=1.
 \tag{4}
\]

Indeed `D a_0` contains the contraction `C S^{-1}` on each coordinate
pair, while `(G_j,g dot u)` is a standard Gaussian pair with correlation
`u_j`. The `Z_j` integration in (3) retains the prescribed dependence of
the reverse mark on `G_j`; it is not an independent resampling of the two
lower feature coordinates.

`T` is odd and continuous on `[-1,1]`. It is real analytic on `(-1,1)`:
first integrate out `Z`, obtaining a bounded function of `G`; for a
Gaussian pair with correlation `rho`, its density is

\[
 {1\over2\pi\sqrt{1-\rho^2}}
 \exp\!\left[-{g^2-2\rho gx+x^2\over2(1-\rho^2)}\right].
\]

Around each real `rho` strictly between `-1` and `1`, this density extends
holomorphically to a complex disk and is bounded there by a constant times
`exp[-a(g^2+x^2)]` for some `a>0`. This follows by continuity of the real
part of its quadratic matrix and positivity at the disk center. Integrating
against the two bounded functions proves the stated analyticity, by
dominated complex differentiation.

Moreover `T(1)>0`. With `Delta=det S>0`, direct multiplication yields

\[
 c_0\Delta T(1)
 =\alpha v\{vs-\beta^2+v\eta\}
       +(\alpha\beta+\tau\gamma)\beta\eta>0.
 \tag{5}
\]

Here `vs-beta^2>=0`, `alpha,v,eta>0`, and `beta>0`: conditional on
`G`, the mean of `tanh(sqrt(tau) Z+alpha tanh G)` is strictly increasing,
odd, and has the sign of `tanh G`. Thus its product with `tanh G` has
strictly positive expectation. No sign assertion about the separate entries
of `C S^{-1}` was needed.

Analyticity and (5) imply that `T` is not identically zero. Its Taylor
series at zero has a first nonzero coefficient, so `T(rho)` is nonzero
for every sufficiently small positive `rho`. Continuity at one likewise
makes `T(rho)>0` for all `rho` sufficiently close to one. Consequently,
for all sufficiently small `theta>0`,

\[
 A=T(\cos\theta)\ne0,\qquad B=T(\sin\theta)\ne0,
 \qquad C_*=T(1)>0.
\]

The initialized upper fields in (2), expressed in upper coordinates
`(x,y)=b2`, are

\[
 \tanh(Ax+By),\quad\tanh(Ax-By),\quad-\tanh(C_*x).
 \tag{6}
\]

The upper mark law has a strictly positive density on the square
`(-1/c_0,1/c_0)^2`. An almost-everywhere linear relation among (6) would,
by continuity, hold throughout this square. At `x=0` it first implies
that the coefficients of the first two terms agree. Differentiating the
relation twice in `y` at `y=0` gives
`2 lambda B^2 tanh''(Ax)=0` for all `x` in the square. Since `A B !=0`,
this forces `lambda=0`, and the third coefficient then vanishes too.
This proves the strict Gram positivity.

This conclusion is open under perturbation of all three input directions
and all positive masses: the fields are continuous in the inputs in `L2`,
and the smallest eigenvalue of the finite Gram is continuous. Labels stay
exactly `(1,1,-1)`. Label balance can be preserved by imposing
`mu_1+mu_2=mu_3=1/2` while varying the positive masses. The radius obtained
here is an initial-rank radius only; it is not an all-time convergence
radius. The small-angle threshold is defined solely by the frozen Gaussian
integral (3), but no useful numerical value is claimed.

For the exactly symmetric law (2), reflection across the first coordinate
axis forces `f_1=f_2` along training. This does not invalidate the rank
calculation: arbitrary infinitesimal readout variations include an
antisymmetric direction that distinguishes samples 1 and 2. Symmetry of
the reached training trajectory does not imply degeneracy of its full
three-sample tangent.

## 3. A complete finite-state trapping estimate

This lemma is conditional on a reached finite state. It is not an
initialization theorem and is not offered as a replacement for data-only
hypotheses.

Let a reached state `theta_*=(w_*,c_*,M_*)` have
`kappa=lambda_min K(theta_*)>0`. Use the stronger distance

\[
 d_X(\theta,\theta_*)=
   \|w-w_*\|_\infty+\|c-c_*\|_\infty+\|M-M_*\|_F.
\]

Put

\[
 B_1=\mathop{\rm ess\,sup}|b_1|,\quad
 C=\|c_*\|_\infty+1,\quad m=\|M_*\|_{\rm op}+1,
 \quad D_1=1+2C(1+m),
\]
\[
 j_0=1+C+mC,\qquad
 j_1=(C+mD_1+2mC)+(D_1+C)+(1+m),
\]
\[
 L_K=2j_0j_1,\quad V=2(1+C+B_1mC),\quad
 R=\min\{1,\kappa/(2L_K)\}.
 \tag{7}
\]

If

\[
 \sqrt{\mathcal L(\theta_*)}\le {\kappa R\over 2V},
 \tag{8}
\]

then the actual, unchanged full dynamics starting at this state satisfy

\[
 d_X(\theta(t),\theta_*)\le R/2,\qquad
 \mathcal L(\theta(t))\le
       \mathcal L(\theta_*)e^{-2\kappa t}\quad(t\ge0).
 \tag{9}
\]

Thus the ordinary current-state loss itself is an exponentially decreasing
loss-controlling potential on this reached basin. No future norm or kernel
bound is assumed in this lemma; its future bounds are proved from (8).

Proof. The normalized feature maps have operator norms at most one, so
`|a_i|<=1`, `|d_i|<=C`, and `||q_i||_2<=m C` throughout the unit `X` ball.
For two states there at distance `delta`, subtraction of the forward and
backward formulas gives

\[
 |\delta a_i|\le\delta,\quad
 \|\delta z_i\|_2\le(1+m)\delta,\quad
 |\delta d_i|\le D_1\delta,\quad
 \|\delta q_i\|_2\le(C+mD_1)\delta.
\]

The upper gate is 2-Lipschitz and the readouts are bounded by `C`.
Subtracting the three components of `J_i`, using the supremum difference
of the lower fields for its lower gate, therefore gives

\[
 \|J_i\|_{\mathcal H}\le j_0,\qquad
 \|J_i-\widetilde J_i\|_{\mathcal H}\le j_1\delta.
\]

The weighted Jacobian has operator norm bounded by `j_0` and its difference
by `j_1 delta`, because the masses sum to one. Subtracting its two Gram
products proves `||K-K_*||op<=L_K d_X`. Hence `K>=kappa I/2` in the
radius-`R` ball. Equation (1) then gives
`L(t)<=L_* exp(-2 kappa t)` up to first exit.

The exact velocities satisfy

\[
 \|c'\|_\infty\le2\sqrt{\mathcal L},\qquad
 \|M'\|_F\le2C\sqrt{\mathcal L},\qquad
 \|w'\|_\infty\le2B_1mC\sqrt{\mathcal L}.
\]

Consequently the total `X` displacement up to any first exit is at most

\[
 V\int_0^t\sqrt{\mathcal L_*}e^{-\kappa s}\,ds
 \le V\sqrt{\mathcal L_*}/\kappa\le R/2.
\]

Continuity rules out first exit. The fixed-order global existence theorem
in the supplied source permits continuation for every finite time, proving
(9). It also follows that the state has a finite `X` limit and zero loss.

## 4. What remains missing for exact unit labels

The geometry in (2) proves initialized full tangent rank, but
`L(0)=1`. The trapping hypothesis (8) does not follow. With the deliberately
safe initial choices `C=1` and `m=3` (the source gives `||D||op<=2`),
one gets `j_0=7`, `j_1=48`, and `L_K=672`. Also `kappa<=1` because the
initialized kernel is a readout Gram of features bounded by one. Thus the
right side of (8) is much smaller than one. This invalidates this particular
initial small-movement argument; it is not an obstruction to convergence
of the actual flow.

A successful completion needs one of the following additional proved
facts, obtained from the prescribed initialization and the chosen data:

1. A global residual-sensitive coercivity estimate along the symmetric
   reference, strong enough to enter (8), together with a positive full
   three-sample tangent at its limiting state.
2. Direct entrance into (8) at a finite time established analytically from
   data-only bounds, with explicit retained lower bounds on the full
   three-sample tangent.
3. A different state potential whose derivative avoids requiring uniform
   Gram conditioning and which controls all three residuals, including the
   antisymmetric mode introduced by nonsymmetric data perturbations.

The existing fixed-order energy identity provides global finite-time
existence and `L<=1`, but only polynomial-in-time norm bounds. It gives none
of these three missing statements. Initial Gram positivity, the
two-mode symmetry reduction, and finite-time continuous dependence cannot
by themselves be promoted to an all-time unit-label result. A proof only
for a small label amplitude would satisfy a different problem and is not
used here.

The intended reference-to-open-family route is logically sound if an
independent argument supplies exponential reference fitting and an endpoint
with positive full three-sample tangent. Then a late finite time has a
strict version of (8); finite-time continuous dependence transfers it to
nearby data, and the trapping proof supplies the entire subsequent tail.
The missing reference theorem, rather than open-basin perturbation after
it, is the decisive unresolved step of this route.
