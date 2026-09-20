# Class centers, scatter, and the moving lower geometry

Scoped theoretical route, 2026-09-18. Scientific inputs: the supervisor's model specification only. No other study, prior route, numerical experiment, or external source was consulted. The required research and rigorous-math skills and their research-contract/adversarial-audit references were read.

The requested all-time, data-only exponential potential is **not proved** by this route. The positive results are exact class-coordinate equations, an unconditional accumulated lower bound on hidden label contrast, positive definiteness of the first-layer metric at every bounded-displacement state for nonparallel inputs, a strict-saddle classification of finite nonoptimal critical points in that regime, and exact initial-stall classification. Two rigorous stress tests show why positive contrast and monotone within-class collapse do not close the argument.

## 1. Contract and notation

Write `u_i=x_i/sqrt(2)`, so `|u_i|=1`, and retain the supplied population model, initialization, physical gradient metric, and squared loss. No layer is frozen or replaced. The target is a current-state functional whose coefficients and finite initial value follow from the input data, and whose exponential decrease controls the actual loss for all time outside an explicitly identified exceptional data set. Future trajectory bounds, a posteriori smallest-kernel eigenvalues, and an integrated future loss are not admissible substitutes.

The general identities below require only the supplied finite-horizon regularity. Results invoking a nonsingular first-layer geometry assume the explicit input condition

\[
 u_i\ne\pm u_j\qquad(i\ne j).
\tag{1}
\]

This excludes duplicated or antipodal sample directions; it does not freeze feature learning. Let

\[
 \Phi_i(g)=\tanh(w(g)\cdot u_i),\quad
 z_i=Ma_i,\quad H_i(b)=\tanh(bz_i),\quad b=b_2(Z).
\]

The law of `b` has positive density on an interval about zero. Set

\[
 H_i'(b)=b\operatorname{sech}^2(bz_i),\qquad
 H_i''(b)=b^2\tanh''(bz_i),\qquad d_i=\langle c,H_i'\rangle.
\]

Primes on `H_i` mean derivatives with respect to `z_i`, not `b`. All second-layer brackets use the given Gaussian law of `Z`.

## 2. Exact class centers and scatter at both layers

For any triple `V_i` in a real Hilbert space define

\[
 V_+=qV_1+(1-q)V_2,\quad
 V_0=\frac{V_++V_3}{2},\quad
 V_\Delta=\frac{V_+-V_3}{2},\quad V_s=V_1-V_2.
\tag{2}
\]

The positive-class variance identity is

\[
 q\|V_1-V_+\|^2+(1-q)\|V_2-V_+\|^2
 =q(1-q)\|V_s\|^2.
\tag{3}
\]

Apply (2) first to `Phi_i` in `L^2(g)`, then to the scalars `a_i=<b_1,Phi_i>`, and finally to `H_i` in `L^2(Z)`. The first-layer scalar centers are exactly the `b_1` projections of the corresponding first-layer field centers. Nonlinearity means the second-layer class center is

\[
 H_+=q\tanh(bMa_1)+(1-q)\tanh(bMa_2),
\]

and generally is not `tanh(bM a_+)`. Thus passing through the second activation does not commute with taking class means.

For the second layer write

\[
 k=H_0,\qquad h=H_\Delta,\qquad s=H_s,
 \qquad \kappa=\frac{q(1-q)}2,
\]

and define

\[
 f_0=\langle c,k\rangle,\qquad
 m=\langle c,h\rangle,\qquad
 \rho=\langle c,s\rangle.
\]

The exact loss and readout flow become

\[
 L=f_0^2+(m-1)^2+\kappa\rho^2,
\tag{4}
\]

\[
 \dot c=-2\{f_0 k+(m-1)h+\kappa\rho s\}.
\tag{5}
\]

To check (4), decompose the two positive residuals around
`r_+=q r_1+(1-q)r_2=f_+-1`; their contribution is
`[r_+^2+q(1-q)(f_1-f_2)^2]/2`. Adding `r_3^2/2`, and using
`r_+=f_0+(m-1)` and `r_3=f_0-(m-1)`, gives (4).
Equation (5) follows by the same linear decomposition of `sum p_i r_i H_i`.

This makes the two nuisance directions explicit: the common class center `k` and the positive-class scatter `s`. Their contributions can cancel the label-contrast contribution in (5).

## 3. Full lower geometry, including its motion

Let `P=diag(p_1,p_2,p_3)`, `D=diag(d_1,d_2,d_3)`, and let

\[
 K_{ij}=(u_i\cdot u_j)\,
 \mathbb E_1[b_1^2\operatorname{sech}^2(w\cdot u_i)
                         \operatorname{sech}^2(w\cdot u_j)].
\tag{6}
\]

This is the Gram matrix of the differentials of the three scalar lower features. Direct differentiation gives

\[
 \dot a=-2MKDPr,\qquad
 \dot M=-2a^TDPr.
\tag{7}
\]

Consequently, the actual preactivations `z=Ma` obey

\[
 \dot z=-2SDPr,\qquad S=M^2K+aa^T.
\tag{8}
\]

Both lower-layer motions contribute: the `aa^T` term is the trainable scalar `M`, while `M^2K` is the trainable field `w`.

Let `R_ij=<H_i,H_j>`. The full output derivative is

\[
 \dot f=-2(R+DSD)Pr.
\tag{9}
\]

For the class transformation use

\[
 T=\begin{pmatrix}
 q/2&(1-q)/2&1/2\\
 q/2&(1-q)/2&-1/2\\
 1&-1&0
 \end{pmatrix},\qquad
 W=\operatorname{diag}(1,1,\kappa).
\]

It is invertible for `0<q<1`, and `P=T^TWT`. Let

\[
 a_c=Ta,\quad S_c=TST^T=M^2(TKT^T)+a_ca_c^T,
 \quad B=TDT^{-1}.
\]

The full class-coordinate Gram is

\[
 G=TRT^T+B S_c B^T.
\tag{10}
\]

Here `TRT^T` is the Gram matrix of `(k,h,s)`. Unless all `d_i` coincide, `B` mixes class-center and scatter directions. With

\[
 e=Tr=(f_0,m-1,\rho)^T,\quad
 v=W^{1/2}e,\quad A=W^{1/2}GW^{1/2},
\]

the residual evolution is exactly

\[
 \dot v=-2Av,\qquad L=\|v\|^2.
\tag{11}
\]

Changing to class coordinates therefore exposes the geometry but does not remove the lower metric or the nonlinear mixing.

### The metric derivative cannot be omitted

Where `A` is positive definite, the natural inverse-metric quantity has derivative

\[
 \frac d{dt}(v^TA^{-1}v)
 =-4L-v^TA^{-1}\dot A A^{-1}v.
\tag{12}
\]

The second term has no established sign. The exact constituents of that term include

\[
 \dot S=2M\dot M K+M^2\dot K+\dot a a^T+a\dot a^T,
\tag{13}
\]

\[
 \dot K_{ij}=(u_i\cdot u_j)\mathbb E_1\left[
 b_1^2\left\{
 \tanh''(w\cdot u_i)(\dot w\cdot u_i)
                         \operatorname{sech}^2(w\cdot u_j)
 +\operatorname{sech}^2(w\cdot u_i)
       \tanh''(w\cdot u_j)(\dot w\cdot u_j)
 \right\}\right],
\tag{14}
\]

\[
 \dot R_{ij}=\dot z_i\langle H_i',H_j\rangle
             +\dot z_j\langle H_i,H_j'\rangle,
 \qquad
 \dot d_i=\langle\dot c,H_i'\rangle
                 +\dot z_i\langle c,H_i''\rangle.
\tag{15}
\]

These identities display the precise obstruction to treating the class metric as fixed. In particular, `tanh''` changes sign. The equations do not imply a Loewner-sign bound on `dot A`, and no such bound along the initialized flow was proved here.

## 4. A genuine unconditional contrast bound

Let

\[
 Q=\sum_i p_i f_i^2,\qquad \mathcal D=1-L.
\]

Balanced labels give

\[
 L=1-2\sum_i p_i y_i f_i+Q,
 \qquad \sum_i p_i y_i f_i=m.
\]

Therefore

\[
 \langle c,h\rangle=m=\frac{\mathcal D+Q}{2}.
\tag{16}
\]

If the initialization is nonstalled, `dot c(0) != 0`; continuity and the energy identity give `L(t)<1` for every `t>0`. Thus `mathcal D(t)>0`. Since `M=0` would force all predictions to vanish and `L=1`, continuity gives

\[
 M(t)>0\quad\text{at every finite time.}
\tag{17}
\]

This is not a uniform positive lower bound as `t` tends to infinity.

Moreover `c(0)=0`, Cauchy--Schwarz in time, and physical energy dissipation yield

\[
 \|c(t)\|^2\le t\int_0^t\|\dot c(s)\|^2ds
 \le t\mathcal D(t).
\tag{18}
\]

Combining (16)--(18) gives the data-unconditional accumulated contrast bound

\[
 \|h(t)\|^2\ge\frac{\mathcal D(t)}{4t},\qquad t>0.
\tag{19}
\]

For any global nonstalled solution and any fixed `t_0>0`, monotonicity of `mathcal D` implies

\[
 \int_{t_0}^{\infty}\|h(t)\|^2dt=\infty.
\tag{20}
\]

In fact finite total readout speed implies `||c(t)||=o(sqrt(t))`: split the time integral at `T`, bound the tail by
`sqrt(t-T)(int_T^infty ||dot c||^2)^{1/2}`, divide by `sqrt(t)`, let `t` tend to infinity, then let `T` tend to infinity.

The same argument rules out rapid collapse of the trainable scalar factor. Put
`B_1=E|b_1|` and `B_2=(E b_2^2)^{1/2}`. The feature bound `|a_i|<=B_1`, the inequality `|tanh(v)|<=|v|`, and Cauchy--Schwarz imply

\[
 \sqrt Q\le M B_1B_2\|c\|.
\]

The triangle inequality in the weighted sample norm gives `sqrt Q>=1-sqrt L`. Hence

\[
 M(t)^2\ge
 \frac{\mathcal D(t)}{B_1^2B_2^2(1+\sqrt{L(t)})^2t}
 \ge\frac{\mathcal D(t)}{4B_1^2B_2^2t}.
\tag{20a}
\]

Consequently `int_{t_0}^infinity M(t)^2dt=infinity` on every global nonstalled flow. This still does not control the matrix `K` in the product `M^2K`.

The missing implication is not persistence of label contrast. It is coercive control of the nuisance cancellation in (5). Section 7 supplies a stationary counterexample to making that implication from contrast alone.

## 5. First-layer metric is nonsingular at every finite bounded-displacement state

Assume (1), and assume `||w-g||_infty <= B < infinity`. Then

\[
 K\succ0.
\tag{21}
\]

This does not need continuity, invertibility, or a density formula for the map `g -> w(g)`.

To prove it, suppose `beta^T K beta=0`. Its integrand is nonnegative, hence

\[
 \sum_i\beta_i\operatorname{sech}^2(w(g)\cdot u_i)u_i=0
\tag{22}
\]

for almost every `g` outside the zero-measure set `b_1(g)=0`. Fix `i`, and choose a unit `v_i` perpendicular to `u_i`. On the unit ball centered at `R v_i`,

\[
 |w\cdot u_i|\le B+1,\qquad
 |w\cdot u_j|\ge R|v_i\cdot u_j|-B-1\quad(j\ne i).
\]

All `|v_i dot u_j|` are positive by (1). The `i`th term in (22) has norm at least `|beta_i|sech^2(B+1)`; the sum of the other term norms tends uniformly to zero as `R` tends to infinity. Every such ball has positive Gaussian measure. Equation (22) therefore forces `beta_i=0`. Repeat for all three indices.

The proof even gives an explicit positive lower bound in terms of the current `B` and the input angles, by taking `R` large enough that the two unwanted `sech^2` terms are at most one sixth of `sech^2(B+1)`. The Gaussian mass of the distant ball then enters the bound. That lower bound deteriorates with `B`; replacing it by an unknown all-time displacement bound would violate the requested contract.

## 6. Finite nonoptimal critical points are strict saddles

Under (1), bounded displacement, and `M != 0`, every critical point with `L>0` has a strictly negative Hessian direction in the physical parameter space.

The differential `J_a:delta w -> delta a` is surjective because `J_a J_a^*=K` is positive definite. At a critical point, (7) gives `r_i d_i=0` for every `i`. Choose an index `i` with `r_i != 0`.

The analytic function `H_i'(b)=b sech^2(z_i b)` does not belong to the span of the finitely many `H_j(b)=tanh(z_j b)`. For `z_i=0`, this follows because `b` is unbounded on the real line while all such `tanh` combinations are bounded. For `z_i != 0`, analyticity extends any proposed equality from the support interval of `b` to all real `b`. Grouping the right side by distinct positive absolute frequencies, compare the smallest surviving exponential as `b -> +infinity`. Frequencies below `|z_i|` must have zero coefficients. A frequency at `|z_i|` contributes a constant multiple of `exp(-2|z_i|b)`, while the left side has leading term `4b exp(-2|z_i|b)`. Larger frequencies decay faster. None can produce the factor `b`, proving the claim.

Hence there exists `delta c` orthogonal to every `H_j` but satisfying
`<delta c,H_i'> != 0`; take the orthogonal projection of `H_i'` onto the orthogonal complement of their span. The pure `delta c` Hessian is zero. Choose a bounded `delta w=J_a^*K^{-1}e_i`, so `delta a=e_i`. The mixed Hessian equals

\[
 \nabla^2L[(\delta w,0,0),(0,\delta c,0)]
 =2p_i r_iM\langle\delta c,H_i'\rangle\ne0.
\tag{23}
\]

If `xi=(delta w,0,0)` and `zeta=(0,delta c,0)`, then

\[
 \nabla^2L[\xi+\lambda\zeta,\xi+\lambda\zeta]
 =\nabla^2L[\xi,\xi]
    +2\lambda\nabla^2L[\xi,\zeta].
\]

Choosing the sign and magnitude of `lambda` makes this negative. This is a strict-saddle result, not a proof that the specified deterministic initialization avoids all stable manifolds or asymptotic escape to degeneracy.

## 7. Positive class contrast does not exclude stalled states below the initial loss

Fix `M>0` and choose `a_1=a_3=s>0`, `a_2=t>0`, with `s != t`. Write `H_s=tanh(bMs)` and `H_t=tanh(bMt)`, with `H_s'=b sech^2(bMs)`. These three functions are linearly independent: the two value functions are independent by their first and third Taylor coefficients, and the derivative is outside their span by the argument in Section 6.

There is therefore a finite-norm readout satisfying

\[
 \langle c,H_s\rangle=\frac{q-1}{q+1},\qquad
 \langle c,H_t\rangle=1,\qquad
 \langle c,H_s'\rangle=0.
\tag{24}
\]

For example solve the invertible three-function Gram system in their span. Then

\[
 r_1=-\frac2{q+1},\quad r_2=0,\quad
 r_3=\frac{2q}{q+1},\qquad
 p_1r_1+p_3r_3=0.
\]

Thus `dot c=0`. Also `d_1=d_3=0`, and `r_2=0`, so `dot w=dot M=0`. Nevertheless

\[
 L=\frac{2q}{1+q}<1,\qquad
 h=\frac{1-q}{2}(H_t-H_s)\ne0.
\tag{25}
\]

These states obey the energy-gap/contrast identities, have finite readout norm and strictly positive contrast, and still do not learn. Their strict-saddle nature does not alter that counterexample to a contrast-only coercivity claim.

### The lower triples in this example are realizable

For completeness, sufficiently small triples `(s,t,s)` can be realized by measurable bounded-displacement fields under (1). Define
`F(v)=(tanh(v dot u_1),tanh(v dot u_2),tanh(v dot u_3))`.
Its values span `R^3`: if `beta dot F(v)=0` for all `v`, send `v=R v_i+a u_i` to infinity, where `v_i` is perpendicular to `u_i`. The limit has the form `beta_i tanh(a)+constant=0` for every real `a`, so `beta_i=0`.

Choose finitely many values spanning `R^3` and their negatives. Their centrally symmetric convex hull contains a ball about zero. On a large bounded Gaussian region `Omega`, partition the nonatomic measure `|b_1|d gamma` into prescribed convex-combination weights. On each part set `w(g)=sign(b_1(g))v_k`. The contribution to `a` is then
`(int_Omega |b_1|d gamma) sum lambda_k F(v_k)`.
Outside `Omega` put `w(g)=g`. Its contribution tends to zero as `Omega` increases, while the central convex hull retains a ball of fixed positive radius. Consequently any sufficiently small prescribed triple is attainable. The resulting displacement is bounded because only a bounded region is changed and only finitely many finite vectors `v_k` are used.

This does not assert reachability of these saddles from the prescribed initialization. It shows exactly why positive contrast and bounded readout norm, by themselves, cannot give the missing theorem.

## 8. Prescribed-initialization stress test: both hidden scatters increase

Take the genuine three-input data

\[
 u_1=(s_0,\gamma),\qquad u_2=(-s_0,\gamma),\qquad u_3=(0,-1),
 \quad s_0,\gamma>0,\quad s_0^2+\gamma^2=1,
\tag{26}
\]

and `q != 1/2`. These inputs are pairwise nonparallel. At initialization

\[
 a_1=A_0>0,\quad a_2=-A_0,\quad a_3=0.
\]

Let

\[
 \epsilon=2q-1,\quad H=\tanh(bM_0A_0),\quad
 B_0=\mathbb E[bH\operatorname{sech}^2(bM_0A_0)]>0,
 \quad C_0=\mathbb E[bH]>0.
\]

Then

\[
 \dot c(0)=\epsilon H,\quad
 \dot d_1(0)=\dot d_2(0)=\epsilon B_0,\quad
 \dot d_3(0)=\epsilon C_0.
\tag{27}
\]

The hidden parameters have zero first derivative at zero. Reflection of `g_1` gives
`K_11=K_22`, `K_12=K_21`, and `K_13=K_23`. Differentiating (7),

\[
 (a_1-a_2)''(0)=M_0\epsilon^2(K_{11}-K_{12})B_0>0,
\tag{28}
\]

\[
 M''(0)=\epsilon^2A_0B_0,
\tag{29}
\]

\[
 (z_1-z_2)''(0)
 =\epsilon^2B_0\{M_0^2(K_{11}-K_{12})+2A_0^2\}>0.
\tag{30}
\]

The strict inequality `K_11-K_12>0` follows from positive definiteness, or directly from half the squared norm of the difference of the two lower feature gradients.

The full first-layer fields also have increasing scatter. At initialization put
`v_i(g)=sech^2(g dot u_i)u_i`. Directly differentiating the field flow gives

\[
 \ddot w(0)=M_0\epsilon b_1
 \{B_0(qv_1+(1-q)v_2)-C_0v_3\}.
\]

In the second derivative of `||Phi_1-Phi_2||^2`, reflection `g_1 -> -g_1` cancels the terms involving `v_1+v_2` and `v_3`. The remaining term is

\[
 \left.\frac{d^2}{dt^2}\|\Phi_1-\Phi_2\|^2\right|_{0}
 =M_0\epsilon^2B_0\,
 \mathbb E_1[b_1(\Phi_1-\Phi_2)\|v_1-v_2\|^2]>0.
\tag{31}
\]

Indeed `Phi_1-Phi_2` has the sign of `g_1`, as does `b_1`, and the remaining squared factor is positive on a set of positive measure.

For the second layer, `H_1-H_2=2H`, `dot z_i(0)=0`, and

\[
 \left.\frac{d^2}{dt^2}\|H_1-H_2\|^2\right|_{0}
 =4B_0(z_1-z_2)''(0)>0.
\tag{32}
\]

Meanwhile `dot L(0)=-epsilon^2||H||^2<0`. Multiplying (31) and (32) by `q(1-q)` gives the positive-class within-class variance derivatives. Thus the actual prescribed flow initially increases within-positive-class scatter in both hidden layers while decreasing loss. A proof based on monotone class collapse is false even on these simple nonsingular three-input data. At `q=1/2`, the same geometry becomes exactly stalled, as classified next.

## 9. Complete classification of initial stalls

Let `alpha_i=a_i(0)`. Since `M_0>0` and `c(0)=0`, the initial state is stalled exactly when

\[
 q\tanh(bM_0\alpha_1)+(1-q)\tanh(bM_0\alpha_2)
 -\tanh(bM_0\alpha_3)=0
\tag{33}
\]

almost everywhere. For up to three distinct positive frequencies, the corresponding `tanh` functions are independent: their Taylor coefficients of degrees `1,3,5` yield a Vandermonde matrix after removing the nonzero frequency factors. Analyticity transfers almost-everywhere equality on the mark interval to equality of these coefficients.

Group the nonzero `alpha_i` by absolute value and use oddness. A singleton nonzero group cannot cancel. If all three absolute values coincide and are nonzero, cancellation requires

\[
 q\operatorname{sgn}(\alpha_1)
 +(1-q)\operatorname{sgn}(\alpha_2)
 =\operatorname{sgn}(\alpha_3),
\]

which, since `0<q<1`, requires all three signs to agree. If exactly two entries are nonzero, cancellation is possible only when the negative-class entry is zero, the two positive entries have opposite signs, and `q=1/2`. A single nonzero entry cannot cancel. Thus the exact complete classification is

\[
 \boxed{\alpha_1=\alpha_2=\alpha_3}
 \quad\text{or}\quad
 \boxed{q=\tfrac12,\ \alpha_2=-\alpha_1,\ \alpha_3=0}.
\tag{34}
\]

These are data conditions. To express them directly in input coordinates, let

\[
 F(\rho)=\mathbb E[\tanh(G)\tanh(\rho G+\sqrt{1-\rho^2}Y)],
\]

where `G,Y` are independent standard Gaussians. Then
`alpha_i=F((u_i)_1)/sqrt(nu+eta)`. The function `F` is odd and strictly increasing. For `|rho|<1`, differentiating and integrating by parts separately in `G` and `Y` cancels the derivative-of-`sech^2` terms and gives

\[
 F'(\rho)=\mathbb E[
 \operatorname{sech}^2(G)
 \operatorname{sech}^2(\rho G+\sqrt{1-\rho^2}Y)]>0.
\]

Boundedness justifies differentiation away from the endpoints and continuity at the endpoints. Thus (34) is equivalent to equality of all three first input coordinates, or `q=1/2`, opposite first coordinates of the two positive inputs, and zero first coordinate of the negative input. For three distinct points on the circle, the first alternative is impossible because a fixed first coordinate admits at most two circle points. The second alternative remains possible with no antipodal pair.

## 10. Exact remaining obligation

The demonstrated contrast persistence (19)--(20), finite-time lower-metric nonsingularity, positive `M`, and strict-saddle classification do not establish an all-time decay rate. Three issues remain logically separate:

1. **Nuisance cancellation:** obtain coercivity for the coupled common-center/contrast/scatter residual, not only a norm lower bound for `h`. The stalled construction (24)--(25) prevents inferring this from contrast alone.
2. **Reachability and escape:** show that the deterministic initialized flow outside (34) cannot approach the stable manifold of a nonoptimal saddle or lose coercivity through unbounded parameters. A generic-random-initialization saddle-avoidance statement would not apply to this fixed population initialization without a new verified argument.
3. **Moving-metric compensation:** exhibit an explicit current-state correction controlling the last term of (12), with a finite initial value and constants determined by the data. Merely assuming a future lower bound on `A`, `S`, or a readout norm would replace the requested theorem.

The strongest unresolved step in this route is the third one coupled to the first: a coercive balance law for the actual nonlinear mixing `B S_c B^T` that compensates its motion and remains effective as signed scalar features collide. No such balance law was established. The exact calculations above rule out neither the existence of a more singular current-state potential nor global convergence from all nonstalled prescribed data.
