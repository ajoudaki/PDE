# An exactly stalled but representable three-input configuration

This is an internally checked configuration counterexample for the scalar closure, not a generic or open-family claim. Its inputs are the supervisor's explicit assignment, the established scalar coefficient/dynamics sources already assigned to this route, and the derivations below. No other study routes or experiments were used.

Fix `0<delta<1`, write `s=sqrt(1-delta^2)`, and take

\[
u_1=(\delta,s),\qquad u_2=(-\delta,s),\qquad u_3=(0,1),
\qquad x_i=\sqrt2\,u_i,
\]
\[
(y_1,y_2,y_3)=(1,1,-1),\qquad
(p_1,p_2,p_3)=(1/4,1/4,1/2).
\]

Use exactly the assigned fixed marks
`b_1=tanh(g_1)/sqrt(nu+eta)` and
`b=tanh(sqrt(nu)Z)/sqrt(tau+eta)` on the separate populations, and the positive prescribed scalar `D`. The three directions are pairwise nonparallel: the first two have determinant `2 delta s>0`, while their determinants with the third have magnitudes `delta>0`.

**Proposition.** The canonical trajectory `w(0)=g`, `c(0)=0`, `M(0)=D` is stationary with loss `1` for all time. Nevertheless, the same fixed-mark scalar model has a finite state that interpolates all three labels. This interpolating state can have `M=D`, bounded lower increment, bounded odd readout, and the canonical root symmetry `w(-g)=-w(g)`. Its three upper feature functions are linearly independent.

**Exact stall.** At initialization,

\[
(a_1,a_2,a_3)=(A,-A,0),\qquad
A=\frac{E[\tanh(g_1)\tanh(\delta g_1+s g_2)]}
        {\sqrt{\nu+\eta}}>0.
\]

For positivity, condition on `g_1=x`. The function
`m(x)=E[tanh(delta x+sG)]` is odd and strictly increasing, because its derivative is `delta E[sech^2(delta x+sG)]>0`. Thus `tanh(x)m(x)>0` for every `x!=0`, proving `A>0`. The equality `a_2=-a_1` follows by reversing `g_1`, and `a_3=0` by independence and centering.

Consequently `H_2=-H_1` and `H_3=0`. With `c=0`, all predictions and all backward coefficients `d_i` vanish. The readout equation is therefore

\[
\dot c=2\sum_i p_i y_iH_i
=\tfrac12H_1+\tfrac12H_2-H_3=0,
\]

while the lower and middle equations vanish because `d_i=0`. Thus the initialized state is an exact stationary solution. The established uniqueness of the bounded-increment characteristic flow identifies it with the canonical trajectory on every finite horizon. Its loss is `sum_i p_i y_i^2=1` at every time.

**Independent perturbability of the three scalar features.** Define bounded vector fields

\[
v_j(g)=b_1(g)\operatorname{sech}^2(g\cdot u_j)u_j,
\qquad
w_h(g)=g+\sum_{j=1}^3h_jv_j(g),\qquad h\in\mathbb R^3,
\]

and the smooth map

\[
\mathcal A(h)_i=E_1[b_1\tanh(w_h\cdot u_i)].
\]

Its Jacobian at zero is the Gram matrix

\[
L_{ij}=E_1[v_i\cdot v_j]
=(u_i\cdot u_j)E_1[b_1^2
       \operatorname{sech}^2(g\cdot u_i)
       \operatorname{sech}^2(g\cdot u_j)].
\]

This matrix is positive definite. If `alpha^T L alpha=0`, then, since `b_1!=0` almost everywhere and the Gaussian density is positive,

\[
\sum_i\alpha_i\operatorname{sech}^2(g\cdot u_i)u_i=0
\]

almost everywhere. The left side is continuous, so it vanishes everywhere. Fix `j` and put `g=t z_j` for a unit vector `z_j` perpendicular to `u_j`. Pairwise nonparallelness gives `z_j dot u_i !=0` for `i!=j`. Letting `t->infinity` leaves precisely `alpha_j u_j=0`; hence every coefficient is zero.

For completeness, invertibility gives an actual local feature construction, not only a formal differential. Write

\[
\mathcal A(h)=\mathcal A(0)+Lh+R(h),\qquad DR(0)=0.
\]

Continuity of the derivative follows by differentiating the bounded integrands in the finite vector `h`. Choose a sufficiently small closed Euclidean ball of radius `rho` so that
`||L^{-1}|| sup_{|h|<=rho}||DR(h)||<=1/2`.
For every feature perturbation `z` with `||L^{-1}z||<=rho/2`, the map

\[
h\longmapsto L^{-1}(z-R(h))
\]

maps that ball into itself and has Lipschitz constant at most `1/2`. Its successive iterates are Cauchy, their limit lies in the closed ball, and continuity makes the limit a fixed point. Thus `mathcal A(h)=mathcal A(0)+z` exactly.

Choose a sufficiently small `epsilon>0`, also satisfying `epsilon<A`, and take

\[
z=(\varepsilon,0,\varepsilon),\qquad
a^*=(A+\varepsilon,-A,\varepsilon).
\]

The construction gives a finite `h` and corresponding `w^*=w_h` with exactly these scalar features. Each `v_j` is bounded and odd under full root reversal, because `b_1` is odd and the gate is even. Hence `w^*-g` is bounded and `w^*(-g)=-w^*(g)`. Also `v_j=0` when `g_1=0`, preserving the initialized values on that fixed-mark zero set.

**Finite exact interpolation.** Keep `M^*=D` and put

\[
H_i^*(b)=\tanh(Dba_i^*),\qquad
G_{ij}=E_2[H_i^*H_j^*].
\]

The three positive magnitudes `D(A+epsilon)`, `DA`, and `D epsilon` are distinct. The upper mark has positive density on an interval containing zero. Any linear identity among the `H_i^*` would, after absorbing the signs of `a_i^*`, give an identity among `tanh(b sigma_j)` at three distinct positive `sigma_j`. Continuity makes the identity pointwise on that interval. Its derivatives of orders `1,3,5` at zero give the Vandermonde system in `sigma_j^2`, multiplied by the nonzero factors `sigma_j` and the nonzero Taylor coefficients `1,-1/3,2/15`. Every coefficient therefore vanishes. Thus `G` is positive definite and has an ordinary finite inverse.

Define

\[
\alpha=G^{-1}(1,1,-1)^T,
\qquad c^*(b)=\sum_{j=1}^3\alpha_jH_j^*(b).
\]

This is a bounded odd upper state. Direct substitution gives

\[
f_i^*=E_2[c^*H_i^*]=(G\alpha)_i=y_i
\]

for all three inputs. All marks remain fixed, both frozen-mark marginals retain their prescribed laws, `M^*=D`, and every state coordinate is finite in the required bounded-increment class. The loss is exactly zero. ∎

The positive training loss is therefore an initialization/dynamics obstruction at this precisely balanced configuration, not a representational obstruction or a redundant third input. The third input has an independent constraint in the interpolating state, and the feature differential is onto already at initialization. The argument does not assert that the stalled configuration is open under perturbations, or that perturbed canonical trajectories also fail.

## Quantitative delay under a small weight imbalance

Keep the inputs, labels, marks, and initialized state `z_0=(g,0,D)` fixed, and replace the weights by

\[
p_\varepsilon=(1/4+\varepsilon,\,1/4-\varepsilon,\,1/2),
\qquad 0<|\varepsilon|\le1/8.
\]

Let `z_epsilon(t)` be the actual canonical gradient trajectory for this law, `F_epsilon` its vector field, and `L_epsilon` its unhalved loss. All norms of states below use the fixed population Hilbert metric

\[
\|z-z_0\|^2=\|w-g\|_2^2+\|c\|_2^2+|M-D|^2.
\]

At the common initialized state, the exact cancellation calculation now gives

\[
F_\varepsilon(z_0)=(0,4\varepsilon H_1,0),
\qquad \|F_\varepsilon(z_0)\|\le4|\varepsilon|.
\tag{S1}
\]

Here `H_1(b)=tanh(bDA)` is the same initialized feature as above. In particular the initial vector field is nonzero when `epsilon!=0`.

There are finite constants `B>0` and `C>0`, independent of `epsilon` in the displayed range, such that on the closed Hilbert ball `||z-z_0||<=1`,

\[
\|F_\varepsilon(z)-F_\varepsilon(\widetilde z)\|
\le B\|z-\widetilde z\|,
\qquad
\|f(z)-f(\widetilde z)\|_{p_\varepsilon}
\le C\|z-\widetilde z\|.
\tag{S2}
\]

These estimates concern the exact vector field. They follow directly from bounded marks, bounded tanh derivatives, and Cauchy--Schwarz, and do not require the moving lower increments to be bounded in supremum norm throughout the Hilbert ball.

Here are optional explicit constants verifying uniformity. Write

\[
B_1=(\nu+\eta)^{-1/2},\quad B_2=(\tau+\eta)^{-1/2},
\quad m=D+1,\quad S_0=B_1\sqrt{1+m^2},
\]
\[
C=\sqrt{1+B_1^2B_2^2(1+m^2)},\qquad
A_0=2B_2S_0+2B_2^2S_0^2+2B_1B_2(1+m),
\]
\[
B=2\bigl[A_0(1+C)+C^2\bigr].
\tag{S3}
\]

To check these bounds, let `J_epsilon` be the derivative of the weighted output vector `(sqrt(p_epsilon,i) f_i)_i`. On the ball one has `||c||_2<=1` and `|M|<=m`. The gradient blocks of each scalar output are `H_i`, `d_i a_i`, and `b_1 M d_i sech^2(w dot u_i)u_i`; their squared norms sum to at most `C^2`. Since the weights sum to one, `||J_epsilon||<=C`.

Directly, `||Da_i||<=B_1` and
`||Da_i(w)-Da_i(tilde w)||<=2B_1||w-tilde w||_2`, because the derivative is represented by `b_1 sech^2(w dot u_i)u_i` and `sech^2` is `2`-Lipschitz. Thus the required lower-feature regularity is `C^{1,1}`. To compute the displayed constant, one may use directional second variations along bounded directions: that of `a_i` is bounded by `2B_1`, while for `s_i=Ma_i` the first-variation bound is `S_0` and the directional second-variation bound is `2B_1(1+m)`. The directional second variation of `f_i=E_2[c tanh(bs_i)]` consists of two readout/feature cross terms, one term with `tanh''`, and one term with the directional second variation of `s_i`. Their combined bound is `A_0`. Integrating these estimates along line segments in bounded directions, and then using density and the direct derivative continuity above, gives `||J_epsilon(z)-J_epsilon(tilde z)||<=A_0||z-tilde z||` in the Hilbert norm. No twice Fréchet differentiability on the whole `L2` state space is asserted or needed. Finally the weighted residual has norm at most `1+C` on the ball, because `f(z_0)=0` and `||y||_{p_epsilon}=1`. Applying the product difference bound to the exact gradient formula `F_epsilon=-2J_epsilon^* r_epsilon` gives the constant `B` in (S3).

Fix a loss level `0<ell<1`, and choose

\[
0<r\le\min\left\{1,\frac{1-\sqrt\ell}{2C}\right\}.
\tag{S4}
\]

Define the first loss hitting time, with the infimum of an empty set understood as infinity,

\[
\tau_\varepsilon(\ell)
=\inf\{t\ge0:\mathcal L_\varepsilon(z_\varepsilon(t))\le\ell\}.
\]

**Delay bound.** The actual trajectory satisfies

\[
\tau_\varepsilon(\ell)
\ge \frac1B\log\left(1+\frac{Br}{4|\varepsilon|}\right).
\tag{S5}
\]

To prove it, every state of distance at most `r` from `z_0` obeys

\[
\sqrt{\mathcal L_\varepsilon(z)}
=\|f(z)-y\|_{p_\varepsilon}
\ge1-\|f(z)\|_{p_\varepsilon}
\ge1-Cr
\ge\frac{1+\sqrt\ell}{2}>\sqrt\ell.
\tag{S6}
\]

Thus the loss cannot hit `ell` before the first radius exit. Up to that exit, put `h(t)=||z_epsilon(t)-z_0||`. The integral equation, (S1), and (S2) give

\[
h(t)\le4|\varepsilon|t+B\int_0^t h(s)ds
\le\frac{4|\varepsilon|}{B}(e^{Bt}-1).
\tag{S7}
\]

The last inequality follows by iterating the integral inequality, or by solving its scalar comparison equation. If the first radius exit time is finite, continuity gives `h=r` there; substituting in (S7) gives (S5). If there is no radius exit, (S6) makes the hitting time infinite. This proves the bound without assuming that a hitting time or eventual interpolation exists.

For every fixed `delta` and `ell`, the right side tends to infinity as `epsilon->0`. The constants are independent of `epsilon`; the explicit bounds above are even uniform in the input directions of unit norm. This is a delay statement under weight perturbations, not an assertion about eventual fitting or an open set of perturbed input geometries.

## Consequence for a potential with a common exponential rate

Suppose a family of nonnegative potentials along these perturbed trajectories has fixed exponents `alpha>0` and `lambda>0`, independent of `epsilon`, and satisfies

\[
\mathcal L_\varepsilon(t)\le\Phi_\varepsilon(t)^\alpha,
\qquad
\Phi_\varepsilon(t)\le e^{-\lambda t}\Phi_\varepsilon(0)
\quad(t\ge0).
\tag{S8}
\]

The potential may depend on the training law. For every time strictly below the lower bound in (S5), the loss is greater than `ell`, so (S8) implies
`Phi_epsilon(0)>=ell^(1/alpha) exp(lambda t)`.
Letting `t` increase to that lower bound proves

\[
\Phi_\varepsilon(0)
\ge\ell^{1/\alpha}
\left(1+\frac{Br}{4|\varepsilon|}\right)^{\lambda/B}.
\tag{S9}
\]

The exponent is `lambda/B`, not `alpha lambda/B`: taking the `alpha`-th root of the loss domination cancels the factor `alpha` from the exponential loss rate. In particular a common positive decay rate cannot coexist with a uniformly bounded initial potential as these laws approach the balanced stalled law. At exact balance, the permanently unit loss itself excludes any finite initial potential satisfying (S8) with a positive decay rate.
