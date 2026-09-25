# Current-interval orthogonal derivative-memory closure

Status: a first-principles autonomous candidate, frozen before its simulations. Allowed scientific input was the supervisor's assignment, clarifications, and this route's previous rational-bin note. No external framework, source, experiment, or other study was consulted. Fix the pseudolength **eta=1** in the proposed experiments; retain it symbolically below to explain the construction.

## 1. Object and sole approximation

Keep the actual initialized Gaussian operator `W0` and its transpose. Keep the original current nonlinear forward/backward responses at `What2=W0+K/n`. Write `h_a=h1_a`, `delta_a=delta2_a`,

\[
 \rho=(M^{-1}\textstyle\sum_a r_a^2)^{1/2},\qquad
 \dot s=\rho,\quad s(0)=0,\qquad L=\eta+s,
 \qquad u_a=r_a\delta_a/\rho.
\]

The exact source to be represented is

\[
 K_*(s)=-\frac2M\sum_a\int_0^s u_a(\alpha)h_a(\alpha)^T\,d\alpha.
\]

The construction stores finitely many **exact history coefficients of its own evolving responses**. No closure or truncation enters their equations. Its sole approximation is replacing the cross moment above by the cross moment of finitely projected histories. This is a global projection on the full current activity interval, not a Taylor expansion in time, and no response dictionary is frozen or freely trained.

## 2. Pseudohistory and orthogonal polynomials

On the extended interval `0<=tau<=L`, define histories by

\[
 \widetilde h_a(\tau)=
 \begin{cases}h_a(0),&0\le\tau<\eta,\\
 h_a(\tau-\eta),&\eta\le\tau\le L,
 \end{cases}
 \quad
 \widetilde u_a(\tau)=
 \begin{cases}0,&0\le\tau<\eta,\\
 u_a(\tau-\eta),&\eta\le\tau\le L.
 \end{cases}
\]

The prefix contributes exactly zero to the target cross integral. Thus eta can remain fixed as order grows; it creates no persistent approximation bias. The source history has a known jump at `tau=eta`; the first-layer history is continuous there.

Let `ell_k` be shifted Legendre polynomials on `[0,1]`, defined constructively by

\[
 \ell_0(x)=1,\quad \ell_1(x)=2x-1,\qquad
 (k+1)\ell_{k+1}(x)=(2k+1)(2x-1)\ell_k(x)-k\ell_{k-1}(x).
\]

They obey

\[
 \int_0^1\ell_k\ell_j\,dx=\frac{\mathbf1_{k=j}}{2k+1},
 \quad \ell_k(1)=1,\quad |\ell_k(x)|\le1,
\]

and the exact dilation identity

\[
 x\ell'_k(x)=k\ell_k(x)+\sum_{j<k}(2j+1)\ell_j(x).
\]

These identities follow from the displayed recurrence and differentiation; alternatively orthogonality follows by repeated integration by parts from `ell_k(x)=(k!)^{-1} d^k/dx^k [x^k(x-1)^k]`. All basis coefficients are specified before observing the trajectory.

## 3. Practical autonomous moment equations

For `k=0,...,P-1`, store neuron vectors

\[
 U_{ak}=\int_0^L\widetilde u_a(\tau)\ell_k(\tau/L)\,d\tau,
 \qquad
 H_{ak}=\int_0^L\widetilde h_a(\tau)\ell_k(\tau/L)\,d\tau.
\]

Differentiating the moving interval and using the dilation identity gives the closed exact moment equations

\[
\boxed{
 \dot U_{ak}=r_a\delta_a-
   \frac\rho L\left(kU_{ak}+\sum_{j<k}(2j+1)U_{aj}\right),}
\]

\[
\boxed{
 \dot H_{ak}=\rho h_a-
   \frac\rho L\left(kH_{ak}+\sum_{j<k}(2j+1)H_{aj}\right).}
\]

Initialize `U_ak=0`, `H_a0=eta h_a(0)`, and `H_ak=0` for `k>0`. All coefficients are rational functions of current state. Prefix sums evaluate the triangular transport in linear, rather than quadratic, work in `P`. The terms proportional to `rho/L` are exactly the transport induced by interval dilation; they are not selected damping rates.

Set

\[
\boxed{
 K=-\frac{2}{ML}\sum_{a,k<P}(2k+1)U_{ak}H_{ak}^T,
 \qquad\widehat W_2=W_0+K/n.}
\]

This is the inner product of the two orthogonal projections. The rank is at most `MP`. Forward and transpose actions both use this same matrix. Current first-layer weights and readout obey the specified original gradient equations.

## 4. Exact derivative-memory interpretation and source correction

Define polynomial primitives

\[
 q_0(x)=x,\qquad
 q_k(x)=\frac{\ell_{k+1}(x)-\ell_{k-1}(x)}{2(2k+1)}\quad(k\ge1).
\]

Then `q'_k=ell_k`, `q_k(0)=0`, and `q_k(1)=1_{k=0}`. Define genuine weighted derivative memories on the **actual** activity history:

\[
 J^h_{ak}=\int_0^s q_k((\eta+\alpha)/L)\,dh_a(\alpha),
 \qquad
 J^u_{ak}=\int_0^s q_k((\eta+\alpha)/L)\,du_a(\alpha).
\]

For differentiable responses these are ordinary integrals against `h'_a(alpha)` and `u'_a(alpha)`. Bounded-variation responses admit the displayed Stieltjes interpretation. Integration by parts gives exactly

\[
\boxed{H_{ak}=L\big(\mathbf1_{k=0}h_a-J^h_{ak}\big),}
\]

\[
\boxed{U_{ak}=L\big(\mathbf1_{k=0}u_a-u_a(0)q_k(\eta/L)-J^u_{ak}\big).}
\]

Both derivative memories start at zero. The known initial-response term `u_a(0) q_k(eta/L)` is essential: it accounts for the empty source prefix. Omitting it changes the initialization and introduces a false learned increment.

For an explicit rational ODE in these derivative coordinates, let `T^H_ak=(k+1)H_ak+sum_{j<k}(2j+1)H_aj`, and similarly define `T^U`. Then

\[
 \dot J^h_{ak}=\mathbf1_{k=0}\dot h_a-\rho h_a/L
                              +\rho T^H_{ak}/L^2,
\]

\[
 \dot J^u_{ak}=\mathbf1_{k=0}\dot u_a
       +u_a(0)\frac{\rho\eta}{L^2}\ell_k(\eta/L)
       -r_a\delta_a/L+\rho T^U_{ak}/L^2.
\]

These equations and the reconstruction above give the requested derivative-moment population state. They are an exact change of coordinates of the practical raw-moment system, not a different approximation. For numerical evolution the raw `U,H` coordinates avoid cancellation and unnecessary division by small rho.

## 5. Initial consistency and the exact defect

Define projected endpoint responses

\[
 u^P_a=L^{-1}\sum_{k<P}(2k+1)U_{ak},\qquad
 h^P_a=L^{-1}\sum_{k<P}(2k+1)H_{ak}.
\]

Differentiating the cross-moment reconstruction and collecting its diagonal and triangular terms yields

\[
 \dot K=-\frac{2\rho}{M}\sum_a
       \big[u_a(h^P_a)^T+u^P_a h_a^T-u^P_a(h^P_a)^T\big].
\]

The exact difference from the original gradient at the surrogate's current state is therefore

\[
\boxed{
 E_2:=\dot{\widehat W}_2+
   \frac{2}{nM}\sum_a r_a\delta_a h_a^T
 =\frac{2\rho}{nM}\sum_a
          (u_a-u^P_a)(h_a-h^P_a)^T.}
\]

At initialization `K=0`, `h^P_a=h_a(0)`, and `u^P_a=0`, so `E2(0)=0` and the original initial middle-layer derivative is exactly reproduced at every `P>=1`.

For implementation without forming `u=r delta/rho`, evaluate the derivative as

\[
 \dot K=-\frac2M\sum_a
 \big[r_a\delta_a(h^P_a)^T+\rho u^P_a(h_a-h^P_a)^T\big].
\]

This also gives a convenient independent algebraic check against differentiating the factor reconstruction directly.

## 6. Exact rational response lift and evaluation order

The training responses can be stored with their exact tanh differential equations:

\[
 \dot h^1_a=(1-(h^1_a)^2)\odot(\dot W_1x_a/\sqrt d),
\]

\[
 \dot h^2_a=(1-(h^2_a)^2)\odot
       (\dot K h^1_a/n+\widehat W_2\dot h^1_a).
\]

Initialize them using the actual tanh forward pass. Compute raw moment derivatives and `Kdot` first; then `h2dot`, output derivatives, and `rhodot=mean(r fdot)/rho`. Only afterward, if using derivative coordinates, compute

\[
 \dot u_a=(\dot f_a\delta_a+r_a\dot\delta_a)/\rho
                     -u_a\dot\rho/\rho.
\]

For a linear scalar readout, `delta2=W3 odot (1-h2^2)`, so its derivative is explicit and polynomial in the lifted states and their already computed derivatives. This order has no implicit loop.

The system is autonomous and rational on `rho>0,L>=eta`. The zero-initial-loss case is stationary. Consistent initialization preserves both `rho^2=mean(r^2)` and activation consistency exactly; numerical drift in either is a validity diagnostic. Readout and layer normalizations must follow the original model.

## 7. A derived hierarchy estimate

Use `||z||_n=||z||_2/sqrt(n)`. Suppose the current trajectory satisfies:

- finite total activity `s_infinity<=S`;
- `h_a` is Lipschitz in activity, with constant `H` in neuron norm;
- the extended source response `utilde_a` has total variation at most `V` in that norm, including its known initial jump.

The third assumption is additional: bounded source amplitude and finite activity do not imply bounded variation of `u=r delta/rho`. Changes of residual direction near zero residual can be important. These hypotheses are required uniformly over the tested hierarchy if a uniform convergence statement is intended.

For any bounded-variation history `g`, the endpoint projection error has the exact identity

\[
 g(L)-g^P(L)=\frac12\int_0^L
  [\ell_P(\tau/L)+\ell_{P-1}(\tau/L)]\,dg(\tau).
\]

Indeed the endpoint projection kernel is `sum_{k<P}(2k+1)ell_k=(ell'_P+ell'_{P-1})/2`. Integrate by parts: the polynomial sum is two at the right endpoint and zero at the left. At a jump, use the right endpoint value and include the corresponding atom in `dg`.

Consequently,

\[
 \|u_a-u^P_a\|_n\le V,
\]

and Cauchy--Schwarz plus Legendre orthogonality gives

\[
 \|h_a-h^P_a\|_n
 \le\frac{LH}{2}\left((2P+1)^{-1/2}+(2P-1)^{-1/2}\right)
 \le\frac{LH}{\sqrt{2P-1}}.
\]

The virtual constant prefix preserves this Lipschitz bound. Using the exact defect identity,

\[
\boxed{
 \|E_2(t)\|_F\le c_P\rho(t),\qquad
 c_P=\frac{2VH(\eta+S)}{\sqrt{2P-1}}\longrightarrow0.}
\]

Thus `integral ||E2||_F dt <= c_P S`. This conservative estimate needs no Taylor analyticity radius, no assumed low-rank dense increment, and no small-defect hypothesis. It derives small defect from named regularity bounds. Smoother histories may admit better rates; none is claimed here.

## 8. Conditional all-time convergence and limits

For a fixed width and bounded smooth dynamics, the preceding source estimate implies convergence on each compact physical-time interval. An all-time guarantee additionally follows under a common forward region with:

1. a gradient loss-decay bound `L_loss_dot<=-2 gamma L_loss`, where `L_loss=rho^2`, for the original vector field;
2. a perturbation-to-loss estimate `|extra loss derivative|<=C_L rho ||E2||_F`;
3. an original parameter-velocity bound `||theta_dot||<=C_V rho` and controlled norm conversion for `E2`;
4. uniform source regularity and justified forward containment of the approximate as well as exact flow.

For large enough `P`, `C_L c_P<=gamma` gives closure decay `L_loss_dot<=-gamma L_loss`. Hence `rho<=rho(0)exp(-gamma t/2)`, the closure's total activity is at most `2rho(0)/gamma`, and parameter tails after time `T` are uniformly exponentially small. Apply the source bound up to a proposed activity cap larger than this number; the decay estimate prevents reaching that cap. Compact-time convergence followed by this uniform tail estimate proves all-time convergence. This is a conditional result with an explicit order of limits.

A gradient/geometry theorem for all compatible inputs has not been proved. Width-independent state efficiency also requires the stability, source-variation, activity, and normalization constants to remain uniform with width. The assumption about source variation is a particularly useful diagnostic target; neither good small-order accuracy nor an internal pass establishes it.

## 9. Cost, practical interpretation, and remaining risks

The additional history state is `2nMP` scalars; two clocks add two scalars. Including first-layer weights, readout, and stored training responses gives `2nMP+nd+n+2nM+2`, up to cached outputs. The derivative-coordinate formulation additionally retains the initial source vector per input, which is computable from initialization. Rank is at most `MP`; correction matvecs and transpose matvecs cost `O(nMP)` per vector. Retaining W0 still entails its dense operator cost.

The full current interval expands with learning activity. It does not spend most of its resolution near activity zero through a fixed compactification. That may improve efficiency on large-activity histories, but it is a motivation, not a proven comparison at small P. Endpoint projection can overshoot and the defect can increase loss; the projection itself is not a positivity or descent guarantee.

With eta=1, the raw triangular transport has diagonal rates `k rho/L`, avoiding the large `eta^-1` startup factors of vanishing-pseudomass bins. Triangular coupling and endpoint sums can still become poorly conditioned at high order. Solver refinement, activation/rho invariant checks, and direct comparison of the two Kdot formulas are needed before interpreting an order trend.

Both this route and the previous bin route were specified before their results. No empirical success, failure, efficiency guarantee, or established-material promotion is claimed here.
