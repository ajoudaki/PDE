# Exact three-input classification of a vanishing initial loss slope

Status: complete analytic candidate, frozen on 2026-09-18 before comparison with other current routes. This is an internally derived study result, not promoted material. No experiment or numerical coefficient estimate is used.

Scientific inputs: `docs/observable_p1.md` in full; the model and existence statements in `docs/global_nonlinear.md` C.4.7.9.3–4 and C.4.7.10.D.3; and this study's `initialization_positivity.md` and `terminal_geometry.md` in full, with their stated source qualifications. The investigate-conjectures and solve-math-rigorously skills and research-contract and adversarial-audit references were read. No other study or current-route findings are premises.

## Contract and main statement

Use the exact canonical full order-one population closure in dimension three: its joint Gaussian-derived lower marks, prescribed ridge `eta=1/4096`, `w(0)=g`, `c(0)=0`, `M(0)=D`, the actual transpose of the evolving full matrix, all three trainable blocks, and unhalved physical square loss. Expectations are exact population expectations. There is no finite-population, quadrature, time-step, neural-width, or higher-order limit. Write `u_i=x_i/sqrt(3)` and consider

\[
 \mu=\sum_{i=1}^3p_i\delta_{(u_i,y_i)},\qquad
 u_i\in S^2,\quad p_i\ge0,\quad\sum_i p_i=1,\quad y_i\in\{-1,1\}.
 \tag{1}
\]

Zero weights compactify the actual datasets, whose weights are positive. Repeated or opposite limiting directions are retained. If actual datasets must have distinct or linearly independent inputs, the same limit classification applies.

Set `z_i=y_i u_i`, the label-oriented direction, and define

\[
 \mathcal S(\mu)=-\mathcal L_\mu'(0),\qquad
 \Delta(\mu)=\min_{1\le k\le3}
 \left\{\left|p_k-\tfrac12\right|
       +\sum_{j\ne k}p_j\|z_j+z_k\|^2\right\}.
 \tag{2}
\]

The exact classification is

\[
 \mathcal S(\mu)=0
 \quad\Longleftrightarrow\quad\Delta(\mu)=0
 \quad\Longleftrightarrow\quad
 \begin{cases}
 p_k=\tfrac12\text{ for some }k,\\
 y_j u_j=-y_k u_k\text{ whenever }j\ne k\text{ and }p_j>0.
 \end{cases}
 \tag{3}
\]

Consequently, for every sequence of positive-weight actual datasets,

\[
 \mathcal S(\mu_n)\longrightarrow0
 \quad\Longleftrightarrow\quad\Delta(\mu_n)\longrightarrow0.
 \tag{4}
\]

Labels may be fixed or vary with the sequence. Formula (2) already absorbs them into `z_i`; alternatively, their finitely many possibilities permit fixed-label subsequences. Equation (4) is an explicit geometric and weight criterion, not a restatement of feature-Gram nullity.

The proof strengthens initialized sign protection to strict coordinate monotonicity, identifies all dependencies between at most three initialized upper features, and then uses positivity of the weights. The final section distinguishes (4) from delay to one chosen loss threshold.

## Injectivity of the initialized effective map, including modulo sign

Use the scalar constants of `initialization_positivity.md`:

\[
\begin{gathered}
 \nu=E\tanh^2G,\quad\tau=E\tanh^2(\sqrt\nu Z),\quad\alpha=1-\tau,\\
 h=\tanh G,\quad k=\tanh(\sqrt\tau Z+\alpha h),\quad
 s=Ek^2,\quad\beta=Ehk,\quad\gamma=1-s,\\
 a=\sqrt{\nu+\eta},\quad b=\sqrt{s+\eta-\beta^2/(\nu+\eta)},\quad
 c_* =\sqrt{\tau+\eta},\\
 d_h=\frac{\alpha\nu}{ac_*},\qquad
 d_k=\frac{\alpha\beta\eta/(\nu+\eta)+\tau\gamma}{bc_*},\\
 K(h)=E_Z\tanh(\sqrt\tau Z+\alpha h),\qquad
 \Psi(h)=\frac{d_hh}{a}+\frac{d_k}{b}
                 \left(K(h)-\frac{\beta h}{\nu+\eta}\right).
\end{gathered}
 \tag{5}
\]

The argument of `Psi` is scalar. The Gaussian variables `G,Z` in these expectations are independent; sharing `G` in `h,k` preserves their prescribed dependence. The coefficients retain the actual reused reverse response and ridge-dependent Cholesky subtraction.

The assigned positivity source proves without a numerical premise that `Psi` is odd and

\[
 c_*\frac{\Psi(h)}h\ge
 \frac{\alpha}{\gamma}\frac{2552}{61425}>0,
 \qquad 0<h\le1.
 \tag{6}
\]

Thus `F(G)=Psi(tanh G)` is bounded, odd, and has the strict sign of `G` away from zero. No monotonicity of `Psi` is assumed. For independent standard normals `G,V`, define

\[
 T(r)=E[F(G)\tanh(rG+\sqrt{1-r^2}V)],\qquad -1\le r\le1.
 \tag{7}
\]

Dominated convergence gives continuity, including endpoints. For fixed `g`, let `m_r(g)=E_V tanh(rg+sqrt(1-r²)V)`. For `|r|<1`, differentiation followed by Gaussian integration by parts, with `X=rg+sqrt(1-r²)V`, gives

\[
 \partial_rm_r(g)
 =gE\operatorname{sech}^2X-rE\tanh''X
 =gE\operatorname{sech}^2X
   +2rE[\tanh X\operatorname{sech}^2X].
 \tag{8}
\]

Differentiation is justified on compact subintervals of `(-1,1)` by the Gaussian first moment. The integration-by-parts boundary term vanishes because the gate derivative is bounded. To determine the last expectation's sign, write `A(t)=tanh(t)sech²(t)`. This is odd and strictly positive for `t>0`. If `m>0` and `sigma>0`, then

\[
 E A(m+\sigma V)=\int_0^\infty
 A(t)\{\varphi_\sigma(t-m)-\varphi_\sigma(t+m)\}\,dt>0,
 \tag{9}
\]

since `(t-m)²<(t+m)²` for `t,m>0`. Oddness gives the negative-mean case and zero at zero mean. Consequently, when `g>0`, the second term in (8) is nonnegative for every `r` and the first is strictly positive. For `g<0`, the derivative is strictly negative. Formula (8) also bounds its absolute value by `|g|+2`, uniformly in `r`. Boundedness of `F` and the Gaussian first moment justify differentiation in (7), so

\[
 T'(r)=E[F(G)\partial_rm_r(G)]>0,
 \qquad -1<r<1.
 \tag{10}
\]

Oddness in `r` makes `T` odd. Its continuous extension is strictly increasing on the entire closed interval: between any distinct two points there is an interior subinterval on which (10) gives strictly positive increase.

In the initialized odd sector, omit only inactive constant coordinates and put `a_0(u)=E_1[b_1 tanh(g.u)] in R^6`. The canonical formula for `D` and conditioning each lower reverse noise give

\[
 \Phi(u):=Da_0(u)=(T(u_1),T(u_2),T(u_3))\in\mathbb R^3.
 \tag{11}
\]

Indeed `(G_j,g.u)` has unit marginal variances and covariance `u_j`; conditioning on `G_j` gives precisely the Gaussian representation in (7). The conditional coefficient of row `j` of `D b_1` is `F(G_j)` from (5). Thus the entire lower joint law has been respected. Strict coordinate monotonicity and oddness imply

\[
 \Phi(u)=\Phi(v)\iff u=v,\qquad
 \Phi(u)=-\Phi(v)\iff u=-v.
 \tag{12}
\]

Also `Phi(u)!=0` on the unit sphere. This proves initialized injectivity, including modulo sign. It assumes neither rotational invariance nor injectivity of the evolved map at arbitrary times.

## Exact dependencies and the full initial slope

Write

\[
 H_0(u)=\tanh(b_2\cdot\Phi(u)),\qquad
 K_0(u,v)=E_2[H_0(u)H_0(v)].
 \tag{13}
\]

The nonconstant upper coordinates are `b_{2j}=tanh(sqrt(nu) Z_j)/c_*`; their joint law has strictly positive density on `(-1/c_*,1/c_*)³`. For at most three nonzero vectors `v_i`, all linear dependencies among `tanh(b.v_i)` come from signed duplicates `v_i=+/-v_j`.

Here is a contained proof. Choose representatives `v_1,...,v_q`, `q<=3`, distinct modulo sign. A continuous almost-sure identity holds everywhere on the open cube: a nonzero value would persist on an open set of positive probability. Choose `e` outside the finitely many proper hyperplanes `e.v_i=0` and `e.(v_i+/-v_j)=0`. Such an `e` exists because the product of these nonzero linear polynomials is not the zero polynomial. Then `t_i=e.v_i` are nonzero with distinct squares. Restrict the identity to `b=t e` near zero. The first three odd Taylor coefficients of tanh, namely `1,-1/3,2/15`, give the first `q` equations

\[
 \sum_{i=1}^q A_i t_i^{2n+1}=0,\qquad 0\le n<q.
 \tag{14}
\]

Their matrix has determinant equal to a nonzero diagonal factor times `prod_{i<j}(t_j²-t_i²)`. Thus every `A_i=0`. Grouping signed duplicates proves the dependency claim, and (12) identifies those duplicates exactly with signed input duplicates.

Initially predictions are zero, `L(0)=1`, and residuals are `-y_i`. Because `c(0)=0`, both the matrix and lower velocities vanish initially, whereas the full physical readout velocity is

\[
 c'(0)=2\sum_i p_i y_i H_0(u_i).
\]

The exact full gradient-flow energy identity yields

\[
 \mathcal S(\mu)
 =4\left\|\sum_i p_i y_i H_0(u_i)\right\|_{L^2(\Omega_2)}^2
 =4\sum_{i,j}p_i p_j y_i y_jK_0(u_i,u_j).
 \tag{15}
\]

This reduction follows from the prescribed zero readout; it does not freeze hidden blocks after initialization. Input oddness gives `y_i H_0(u_i)=H_0(z_i)`.

Partition positive-weight indices by the unoriented lines of their `z_i`. In one group write `z_i=epsilon_i v`, `epsilon_i=+/-1`. The dependency result says that (15) vanishes exactly when each group satisfies

\[
 \sum_{i\text{ in group}}p_i\epsilon_i=0.
 \tag{16}
\]

Each nonempty group needs at least two active atoms, one of each sign. With at most three active atoms there can therefore be only one group. Its positive and negative masses both equal `1/2`. One of the signs has a single atom, which has weight `1/2`; every other active direction has the opposite sign. Conversely these conditions cancel the feature sum pointwise. This proves (3).

All boundary cases are included:

- With three positive limiting weights, one is `1/2`; the other two sum to `1/2` and have the same label-oriented direction, opposite to the half-weight atom.
- With two positive limiting weights, both are `1/2` and their label-oriented directions are opposite. The inactive direction and label are unrestricted.
- One active atom cannot cancel. In particular, two weights tending to zero cannot produce a vanishing slope.
- For two active atoms, equal labels require opposite raw inputs; opposite labels require equal raw inputs. Opposite raw inputs with opposite labels reinforce their initialized contributions.

Every exact zero-slope law has a stationary initialized full state. All three initial velocities vanish and uniqueness gives the constant continuation. There is also an exact loss obstruction. Choose a raw representative `v` of the active line and write `u_i=epsilon_i v`. The cancellation condition is `sum p_i epsilon_i y_i=0`. Every prediction in this bias-free architecture is odd, so its loss for this law is

\[
 \sum_i p_i(\epsilon_i f(v)-y_i)^2=1+f(v)^2\ge1.
 \tag{17}
\]

The best odd-predictor loss is already attained at initialization. No higher-order escape from that stationary state is asserted.

## Compact limits, fixed weights, and label balance

The simplex of nonnegative weights times three spheres is compact. The bounded initialized features depend continuously on direction in `L²`, by (7), (11), (13), and dominated convergence. Thus `S` and `Delta` are continuous and have the same zero set. If one tends to zero while the other does not, take a subsequence on which the latter stays bounded away from zero, then a convergent parameter subsequence; continuity contradicts the common zero set. This proves (4), including sequences oscillating between different cancellation configurations.

Equivalently, every accumulation point must be a configuration in (3); no fixed limiting direction or distinguished atom is required. On every compact region `Delta>=epsilon>0`, `S` has a strictly positive minimum. For fixed positive weights a cancellation geometry exists exactly when `max_i p_i=1/2`. Three equal weights therefore admit a uniform strictly positive initial slope over all unit directions and labels. Near-coincidence and antipodal geometry do not remove this weight obstruction.

Suppose the labels are exactly balanced:

\[
 \sum_i p_i y_i=0.
 \tag{18}
\]

At a cancellation limit, all active inputs have the form `u_i=epsilon_i v`. Combining (18) with cancellation gives separately

\[
 \sum_{\epsilon_i=+1}p_i y_i=0,\qquad
 \sum_{\epsilon_i=-1}p_i y_i=0.
 \tag{19}
\]

Each nonempty raw orientation would require at least two active atoms, one of each label. With only three atoms, both orientations cannot be nonempty. Consequently, within the balanced slice,

\[
 \mathcal S(\mu)=0
 \quad\Longleftrightarrow\quad
 \text{all positive-weight raw inputs coincide.}
 \tag{20}
\]

Label balance is a premise of (20). With all three weights positive, the singleton label necessarily has weight `1/2`; the other two have total weight `1/2`. With two active atoms, their labels are opposite and their weights are both `1/2`. An inactive third direction is unrestricted.

An explicit sequence criterion in the balanced slice is

\[
 \mathcal S(\mu_n)\to0
 \quad\Longleftrightarrow\quad
 \sum_{i<j}p_{i,n}p_{j,n}\|u_{i,n}-u_{j,n}\|^2\to0.
 \tag{21}
\]

The right-hand expression is continuous and has precisely the zero set in (20), so the compactness argument applies. If all weights stay bounded below, it is simply pairwise coalescence of all raw directions. More generally (21) remains valid whenever the label imbalance tends to zero, since all accumulation points are then balanced. Without exact or asymptotic balance, use (4).

For linearly independent actual inputs, the slope is positive at every dataset. Its asymptotic vanishing can occur only through the classified limiting degenerations. No terminal behavior has been assumed.

## Initial-slope vanishing versus a specified-threshold delay

An **asymptotically vanishing initial slope** means (4), for separately initialized systems measured in the same physical clock, with `L_n(0)=1`. This also implies finite-horizon stagnation for the full system, but is not equivalent to delay to one chosen loss threshold.

Let `V_mu(theta)` be the complete physical vector field, in the Hilbert norm

\[
 \|(\delta w,\delta c,\delta M)\|^2
 =\|\delta w\|_2^2+\|\delta c\|_2^2+\|\delta M\|_F^2.
\]

For every fixed `T`, the exact energy and contraction estimates supply common bounds over all laws (1):

\[
 \|c(t)\|_\infty\le2T,\qquad
 \|M(t)\|\le\|D\|+2T^2,\qquad 0\le t\le T.
 \tag{22}
\]

There is a common Lipschitz constant `L_T>=1` for the full vector field in this Hilbert metric on that state region. To verify the claim, at a fixed input one has `||h_1-h_1'||_2<=||w-w'||_2`. Feature-synthesis contractions give `|a-a'|<=||h_1-h_1'||_2` and bound the upper preactivation difference by a constant times `||w-w'||_2+||M-M'||_F`. Subtracting `c sech²(z)` and `c' sech²(z')` bounds its `L²` difference by `||c-c'||_2+2||c'||_infinity ||z-z'||_2`. Bounded lower features then bound the reverse action and its difference in supremum norm. The lower velocity is a bounded reverse action times a gate, whose difference is controlled in `L²`; the remaining velocities are finite contractions of the same bounded factors. Predictions and residuals satisfy the corresponding difference estimates. Summing the blocks and averaging against a probability law proves the common constant. The frozen unbounded Gaussian base occurs only inside gates: no product of unrestricted `L²` fields is used. This is a Hilbert-metric estimate, not an invalid supremum-norm continuity assertion in the varying Gaussian input.

Set `v(t)=||V_mu(theta(t))||`. The initial norm equals `sqrt(S(mu))`. The integral equation and Lipschitz estimate give

\[
 v(t)\le\sqrt{\mathcal S(\mu)}+L_T\int_0^t v(s)\,ds
       \le\sqrt{\mathcal S(\mu)}e^{L_Tt}.
\]

The last inequality follows by differentiating the scalar integral majorant after multiplication by `exp(-L_T t)`. The exact energy identity yields

\[
 0\le1-\mathcal L_\mu(t)=\int_0^t v(s)^2\,ds
 \le\mathcal S(\mu)\frac{e^{2L_Tt}-1}{2L_T},\qquad 0\le t\le T.
 \tag{23}
\]

Thus (4) implies uniform stagnation at loss one on every fixed finite interval. This conclusion uses the full evolving dynamics and its actual transpose, not a frozen-feature extrapolation of (15).

Conversely, with the common constant `L_1` through time one,

\[
 \|V_\mu(\theta(t))-V_\mu(\theta(0))\|
 \le\sqrt{\mathcal S(\mu)}(e^{L_1t}-1).
\]

Take `t_0=min(1,log(3/2)/L_1)>0`. The speed is at least `sqrt(S(mu))/2` on `[0,t_0]`, and hence

\[
 1-\mathcal L_\mu(t_0)\ge\tfrac14t_0\mathcal S(\mu).
 \tag{24}
\]

Therefore vanishing initial slope is equivalent to uniform stagnation on every fixed finite interval. Define

\[
 \tau_\mu(\delta)=\inf\{t\ge0:\mathcal L_\mu(t)\le1-\delta\},
 \qquad 0<\delta<1,
 \tag{25}
\]

where the infimum of the empty set is infinity. The same property is equivalent to `tau_{mu_n}(delta)->infinity` **for every** fixed `delta in (0,1)`. The forward implication follows from (23). Conversely, divergence for all thresholds and monotonicity of loss give `L_n(t_0)->1`, and (24) applies. No eventual attainment of any threshold is asserted.

### A single specified threshold has a strictly weaker meaning

The distinction persists with exact label balance and linearly independent actual inputs. Fix `delta in (0,1)` and choose

\[
 0<\kappa<\min\left(\tfrac12,\frac{\delta}{1+\delta}\right).
\]

Consider the limiting law

\[
 (p_1,p_2,p_3)=(\tfrac12,\tfrac12-\kappa,\kappa),\qquad
 (y_1,y_2,y_3)=(+1,-1,-1),\qquad
 (u_1,u_2,u_3)=(e_1,e_1,e_2).
 \tag{26}
\]

It is exactly label-balanced. For any predictions `A=f(e_1)`, `B=f(e_2)`, completing the square gives

\[
 \begin{split}
 \mathcal L
 &=\tfrac12(A-1)^2+(\tfrac12-\kappa)(A+1)^2+\kappa(B+1)^2\\
 &=(1-\kappa)\left(A-\frac{\kappa}{1-\kappa}\right)^2
    +\frac{1-2\kappa}{1-\kappa}+\kappa(B+1)^2\\
 &\ge1-\frac{\kappa}{1-\kappa}>1-\delta.
 \end{split}
 \tag{27}
\]

Nevertheless its initial slope is strictly positive:

\[
 \mathcal S=4\kappa^2\|H_0(e_1)-H_0(e_2)\|_2^2>0,
 \tag{28}
\]

by (12)–(14). The specified threshold is never attained despite a nonzero initial slope.

To obtain three linearly independent actual inputs, keep the positive weights and labels and replace only

\[
 u_{2,n}=\frac{e_1+\varepsilon_n e_3}{\sqrt{1+\varepsilon_n^2}},
 \qquad \varepsilon_n>0,\quad\varepsilon_n\to0.
 \tag{29}
\]

The three directions are independent for every `n`, and their slopes tend to the positive number (28). Their full trajectories and losses converge to those of (26) on each fixed interval. For the needed parameter continuity, retain the Hilbert state estimates above. Varying an input adds `||tanh(w.u)-tanh(w.v)||_2<=||w||_2 ||u-v||`, and the analogous gate bound; all other factors are bounded by (22). A common finite-time bound on `||w||_2` follows by integrating the bounded reverse-action speed from the Gaussian initial state. Thus the vector-field difference acquires only `C_T max_i||u_{i,n}-u_i||`; its integral inequality yields uniform state convergence, and the bounded observation formulas yield uniform loss convergence. The strict gap in (27) then gives `tau_{mu_n}(delta)->infinity` while `S(mu_n)` tends to a positive value.

This disproves the converse for one specified threshold even with fixed positive weights, exact label balance, and independent actual inputs. It does not assert that these perturbed datasets eventually fit or that their individual threshold times are finite.

## Scope

Equations (3)–(4), the balanced specialization (20)–(21), and the finite-horizon equivalence (23)–(25) concern precisely the stated initialized canonical order-one full closure. They do not establish terminal fitting, a terminal rate, or a universal quantitative asymptotic for diverging threshold times. The three-atom restriction matters: four atoms can carry two separately cancelling pairs on distinct unoriented lines. The proof retains initialized reverse correlation and ridge, assumes no rotational invariance, and does not identify this closure with a trained-network limit or a higher-order approximation theorem.

