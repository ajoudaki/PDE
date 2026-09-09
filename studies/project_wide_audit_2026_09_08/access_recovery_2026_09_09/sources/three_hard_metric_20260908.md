# Testing an activation-adapted metric: an exact full-L3 obstruction on raw balls

2026-09-08. Theory only; no experiments or old proof-file edits.

## Conclusion

A scalar activation-coordinate transform can indeed remove the troublesome incoming-field multiplier in a one-coordinate toy system. However, for correlated sample rows no common rowwise isometric straightening exists. More strongly, **for every fixed `0<theta<=1/2` and `0<delta<=1/4`, the actual three-hidden-layer model has exact stationary states in one fixed raw-radius ball whose finite-dimensional restricted GF linearization has arbitrarily large positive eigenvalues.**

This rules out a raw-ball semiconvexity bound for the loss and a raw-ball one-sided-Lipschitz bound for the GF in any smooth positive Riemannian metric, even one involving all parameter blocks. The fixed radius may depend on theta and delta but does not depend on the growing eigenvalue. The construction respects the original initialized-action affine space: only finite-rank changes of the canonical initialized actions are used.

These stationary states are not asserted reachable from canonical initialization. Thus the result excludes a blanket energy-ball metric argument; it does not disprove the desired global GF/population theorem or exclude a stronger reachable-state argument.

## 1. The useful scalar transform and its limitation

Write `phi(z)=a z+e atan z`, with `a=1-e`, `0<e<=1/2`, and `g=phi'`.
Then `a<=g<=1`. In the toy system

\[
 x'=g(x)A^*y,\qquad y'=A\phi(x),
\]

set `v=T(x)`, where

\[
 T(x)=\int_0^x\frac{ds}{g(s)}.
\]

Both T and its inverse act as globally Lipschitz maps on L2. The curve chain rule gives

\[
 v'=A^*y,\qquad y'=A\phi(T^{-1}(v)).
\]

The last coordinate map has derivative `g(T^-1(v))^2`, bounded by one. Thus the transformed toy system is a globally Lipschitz Hilbert ODE. This is a real cancellation, not merely a formal coordinate analogy.

For normalized sample directions u_i, the actual bottom row is driven by the vector fields

\[
 X_i(w)=g(u_i\cdot w)u_i.
\]

For two nonparallel, nonorthogonal directions with correlation rho,

\[
 [X_i,X_j]
 =\rho\{g_i g_j' u_j-g_jg_i'u_i\}.
\]

At w=0 the bracket vanishes, but its derivative is

\[
 D[X_i,X_j](0)
 =\rho\phi'''(0)(u_j u_j^T-u_i u_i^T)
 =-2e\rho(u_j u_j^T-u_i u_i^T).                       \tag{1}
\]

On their two-dimensional span its eigenvalues are
`+/- 2e |rho| sqrt(1-rho^2)`, both nonzero.
If all X_i were Killing fields for one smooth positive metric, their bracket would also be Killing. A Killing field vanishing at a point has a skew-adjoint derivative in that point's inner product: its linearized local flow preserves that inner product. Such a derivative cannot have a nonzero real eigenvalue. Equation (1) is therefore a contradiction.

This excludes a common rowwise metric which exactly cancels arbitrary incoming controls. It applies in particular to the equilateral admissible triple. It does not assume that actual GF supplies arbitrary controls or claim that a state-dependent full-parameter metric has already been excluded; the stronger construction below addresses the latter possibility on raw balls.

For a full-rank sample Gram Gamma, another manifestation appears in feature coordinates h=phi(z). The mobility is `D Gamma D`, with `D=diag(g(z_i))`. Its inverse has entries

\[
 M_{ij}(h)=\frac{(\Gamma^{-1})_{ij}}{g(z_i)g(z_j)}.
\]

For i!=j, `partial_{h_j} M_{ii}=0`, whereas

\[
 \partial_{h_i}M_{ij}
 =-\frac{(\Gamma^{-1})_{ij}\phi''(z_i)}{g(z_i)^3g(z_j)}.
\]

Thus this inverse metric is not the Hessian of a potential whenever an off-diagonal inverse-Gram entry is nonzero. A direct separable mirror/Bregman transplant of the scalar transform fails its Hessian integrability condition.

## 2. An elementary equal-elasticity lemma

For z>0 define

\[
 E(z)=\frac{\phi(z)}{z g(z)}.
\]

For every fixed r in (0,1), there is a finite t>0 with

\[
 E(rt)=E(t).                                             \tag{2}
\]

Indeed, Taylor expansion at zero gives

\[
 E(z)=1+\frac{2e}{3}z^2+O(z^4),
\]

so `E(rt)-E(t)<0` for small t>0. At infinity,

\[
 E(z)=1+\frac{e\pi}{2az}+O(z^{-2}),
\]

so the difference is positive for large t. Continuity proves (2).
All expansions have fixed positive a and e; no uniform t-bound is asserted.

At such a pair put

\[
 r_{new}=\frac{\phi(rt)}{\phi(t)}.
\]

Strict positivity, monotonicity, and strict concavity of phi on (0,infinity) imply
`r<r_new<1`. Equality of elasticities gives the exact useful identity

\[
 \frac{g(rt)}{g(t)}=\frac{r_{new}}r.                    \tag{3}
\]

## 3. Three scales and an exact nonzero-loss stationary pattern

Fix `0<delta<=1/4`, put `c=1-delta`, `s=sqrt(1-c^2)`, and choose

\[
 u_+=(c,s),\qquad u_0=(1,0),\qquad u_-=(c,-s),
 \qquad y=(1,-1,1).
\]

These obey the closed pairwise absolute-separation condition, as already proved in the geometry note. Use the preceding lemma three times:

1. Choose t_1 with `E(c t_1)=E(t_1)` and define
   `r_1=phi(c t_1)/phi(t_1)`.
2. Choose t_2 with `E(r_1 t_2)=E(t_2)`, define
   `lambda=t_2/phi(t_1)>0`, and
   `r_2=phi(r_1 t_2)/phi(t_2)`.
3. Choose t_3 with `E(r_2 t_3)=E(t_3)`, define
   `mu=t_3/phi(t_2)>0`, and
   `r_3=phi(r_2 t_3)/phi(t_3)`.

All quantities are fixed and finite for the chosen e and delta, and
`c<r_1<r_2<r_3<1`. Define the scalar composition

\[
 F(z)=\phi(\mu\phi(\lambda\phi(z))),\qquad H=\phi(t_3).
\]

Then

\[
 F(c t_1)=r_3H,\quad F(t_1)=H,\quad
 \frac{F'(c t_1)}{F'(t_1)}=\frac{r_3}{c}.               \tag{4}
\]

The derivative ratio follows by multiplying (3) at the three layers.
Also F is strictly increasing and strictly concave for z>0; direct differentiation of the composition makes every contribution to F'' negative.

Choose the mean readout

\[
 c_0=\frac{2r_3-1}{H(1+2r_3^2)}.
\]

The prediction vector from a constant neuron feature pattern is
`f=c_0 H(r_3,1,r_3)`. Its residual is exactly

\[
 r=f-y=\kappa(1,-2r_3,1),\qquad
 \kappa=-\frac{1+r_3}{1+2r_3^2}<0.                     \tag{5}
\]

For this residual, all the following contractions vanish:

\[
 \sum_i r_i h_i^3=0,\qquad
 \sum_i r_i g(z_i^3)h_i^2=0,
\]
\[
 \sum_i r_i g(z_i^3)g(z_i^2)h_i^1=0,
\]
\[
 \sum_i r_i g(z_i^3)g(z_i^2)g(z_i^1)u_i=0.             \tag{6}
\]

Here the sample values are the three scalar layer pairs just constructed. The side/center ratio of the first scalar product in the second expression is
`r_2 [g(r_2 t_3)/g(t_3)]=r_3`. For the next it is
`r_1 [g(r_1 t_2)/g(t_2)] [g(r_2 t_3)/g(t_3)]=r_3`.
The last vector identity follows from `u_++u_-=2c u_0` and the product derivative ratio `r_3/c` in (4). This proves every cancellation in (6).

## 4. Realization inside the original canonical raw state space

Let p in (0,1/2) tend to zero. On each canonical neuron probability space choose an event of probability p and define the normalized centered two-valued field

\[
 f_p=\frac{1_E-p}{\sqrt{p(1-p)}}.
\]

It has mean zero and L2 norm one. Each canonical space is nonatomic because it includes a Gaussian root; events of the prescribed probability exist. Let P_l be the orthogonal projection onto
`span{1,f_p}` in layer l. The identical two values and probabilities identify these two-dimensional spaces isometrically, including their pointwise multiplication algebras.

Let U_21 and U_32 denote the partial isometries mapping the respective orthonormal bases `(1,f_p)` to `(1,f_p)`. Starting from the actual canonical bounded initialized actions A_0 and B_0, set

\[
 A_p=(I-P_2)A_0(I-P_1)+\lambda U_{21},
\]
\[
 B_p=(I-P_3)B_0(I-P_2)+\mu U_{32}.                     \tag{7}
\]

These changes are finite-rank and hence Hilbert--Schmidt. Since initialized norms are at most 10,

\[
 \|A_p-A_0\|_{HS}\le\sqrt2(30+\lambda),\qquad
 \|B_p-B_0\|_{HS}\le\sqrt2(30+\mu).                    \tag{8}
\]

For example expand the first difference as
`-P_2 A_0-A_0 P_1+P_2 A_0 P_1+lambda U_21`; each of the first three terms has HS norm at most `10sqrt(2)`. The complement blocks in (7) remain the original actions. Their actual adjoints are used throughout.

Choose the first-layer parameter to be the constant map
`sqrt(d)w=t_1 u_0`, and choose the readout

\[
 C_p=c_0\,1-f_p.                                        \tag{9}
\]

All sample features are constant on each neuron space, with the values in Section 3. The prediction depends only on the mean c_0 and is independent of p. The readout has norm `sqrt(c_0^2+1)`, also independent of p.
The raw squared distance from canonical initialization is bounded uniformly in p by

\[
 d+t_1^2+2(30+\lambda)^2+2(30+\mu)^2+c_0^2+1.           \tag{10}
\]

The first term follows from the centered identity-covariance Gaussian initial first map. We may fix d=2 throughout.

Every one of these states is an **exact stationary point of the original full GF**. Indeed, its backward fields are respectively

\[
 b_i^3=g(z_i^3)C_p,\quad
 b_i^2=\mu g(z_i^2)g(z_i^3)C_p,\quad
 b_i^1=\lambda\mu g(z_i^1)g(z_i^2)g(z_i^3)C_p,
\]

with the corresponding copies of C_p on each neuron space. Substituting these into every raw gradient block gives precisely the four cancellations (6). No hidden block is frozen or removed in this calculation. The residual (5) is nonzero. These stationary states even belong to the
initial loss sublevel: their loss is

\[
 L_{crit}=\frac{(1+r_3)^2}{1+2r_3^2}<\frac32=L(0),
\]

where the strict inequality follows from `(2r_3-1)^2>0`. Thus adding
only loss sublevel control does not remove the construction.

## 5. Unbounded negative loss curvature at those stationary states

Let

\[
 v_p=1_E/\sqrt p
\]

on the first layer, and vary only the first parameter by
`sqrt(d) Delta w=v_p e_2`. This direction has raw norm one and belongs to `span{1,f_p}`.
Keep A_p,B_p,C_p fixed along this variation. Since the two-valued algebra is closed under every coordinate activation and the restricted actions are lambda and mu times its identity, the sample predictor along this curve is exactly

\[
 f_i(\epsilon)=E\left[C_p F(t_1u_i\cdot u_0+
                           \epsilon v_p u_i\cdot e_2)\right].
\]

Consequently its loss second derivative at zero is

\[
 L''(0)
 =\sum_i\left[F'(t_1u_i\cdot u_0)(u_i\cdot e_2)E(C_pv_p)\right]^2
 +E(C_pv_p^2)\sum_i r_i F''(t_1u_i\cdot u_0)(u_i\cdot e_2)^2.
\]

The exact scalar moments are

\[
 E(C_pv_p)=c_0\sqrt p-\sqrt{1-p},\qquad
 E(C_pv_p^2)=c_0-\sqrt{(1-p)/p}.
\]

The center sample's perpendicular projection vanishes. The two side contributions give

\[
 K_*:=\sum_i r_i F''(t_1u_i\cdot u_0)(u_i\cdot e_2)^2
 =2\kappa s^2 F''(ct_1)>0.                              \tag{11}
\]

Strict positivity uses kappa<0, s>0, and F''(ct_1)<0. Therefore

\[
 L''(0)
 \le2s^2F'(ct_1)^2(|c_0|+1)^2
 +K_*\left[c_0-\sqrt{(1-p)/p}\right]
 \longrightarrow-\infty.                              \tag{12}
\]

This is a unit-direction Hessian calculation at an exact stationary point, not an estimate at an arbitrary noncritical state.

## 6. Consequence for full-parameter metrics

For each fixed p, allow all first-layer coordinates in the two-dimensional algebra, all 2-by-2 learned action blocks between these algebras, and all readout coordinates there; keep the complement blocks from (7) fixed. This is an invariant finite-dimensional submanifold of the exact GF: activations remain two-valued, backward fields stay in the same subspaces, and rank-one updates stay in the corresponding action blocks.

On this finite-dimensional submanifold the loss and vector field are smooth. At the stationary state, (12) shows that its selfadjoint loss Hessian has a negative eigenvalue tending to minus infinity. Hence the restricted GF linearization has a positive eigenvalue tending to plus infinity, although all states lie in the one fixed raw ball (10).

Suppose a smooth positive Riemannian metric on the full parameter state space made the GF one-sided Lipschitz on that ball with one finite constant L_B. Restrict it to this invariant submanifold. At a stationary point the derivative-of-metric-along-flow term is zero. For an eigenvector of the linearized GF with positive eigenvalue lambda_p, the metric quadratic growth is exactly `2lambda_p` times its squared metric norm. The one-sided bound therefore requires `lambda_p<=L_B`, a contradiction as p tends to zero.

This argument allows metric cross terms between every parameter block. Uniform equivalence to the raw metric is not needed for the eigenvalue contradiction; positivity on each restricted tangent space already suffices. Smoothness is used only for the usual differential one-sided-Lipschitz formulation.

## 7. Implication for the proof search

The scalar transform is valid but cannot be promoted to a uniform full-state metric argument by bounded positivity of phi' alone. Correlations obstruct rowwise Killing cancellation, and the exact stationary family obstructs global raw-ball semiconvexity or full-parameter one-sided-Lipschitz estimates.

The construction does not prove that these states are reached from canonical Gaussian initialization. It therefore leaves open a metric, entropy, or source-tail estimate using a genuinely stronger reachable-state invariant. The Osgood module in `three_hard_energy_20260908.md` remains available if that invariant yields uniform sub-exponential incoming moments. Neither the present obstruction nor that conditional module is a completed unconditional three-input theorem.
