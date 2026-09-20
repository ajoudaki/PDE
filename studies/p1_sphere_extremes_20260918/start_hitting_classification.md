# Exact slow-onset classification for three weighted sphere inputs

Status: independent analytic derivation, frozen before comparison with other
routes. This is an internally derived theorem for the exact canonical
`d=3,p=1` population closure. No experiment, quadrature, or finite-population
approximation was used. No assertion about a general-dimensional trained
network limit or a terminal fitting rate is made.

## Scope and contract

Scientific inputs read: `docs/observable_p1.md` completely;
`docs/global_nonlinear.md` C.4.7.9.3--4 and the model, dictionary, equations,
energy and existence portions of C.4.7.10.D.3; and this study's
`early_delay.md`, `necessary_potential_growth.md`, and
`initialization_positivity.md` completely. The investigate-conjectures skill,
its research-contract and adversarial-audit references, and the
solve-math-rigorously skill were applied. No other study or another route's
current findings were read.

Write `u=x/sqrt(3)` and let

\[
 \mu=\sum_{i=1}^3p_i\delta_{(u_i,y_i)},\qquad
 u_i\in S^2,\quad y_i\in\{-1,1\},\quad p_i\ge0,\quad\sum_i p_i=1.
 \tag{1}
\]

Actual family members may be restricted to strictly positive weights and
linearly independent inputs. Zero weights, coincidences and antipodal
coincidences are included in the compactification, not asserted to be
genuine three-independent-input examples. The theorem allows arbitrary
binary label masses; a sharper description for balanced labels appears below.

Let `K` be the set of laws (1), with repeated atoms identified as laws. Equip
it with the transportation distance

\[
 d(\mu,\nu)=\inf_\pi\int (|u-v|+|y-z|)\,d\pi(u,y,v,z).
 \tag{2}
\]

For finite laws the infimum is over nonnegative coupling matrices with the
specified row and column sums. The compact parameter space
`Delta_2 x (S^2)^3 x {+1,-1}^3` maps continuously into this metric space:
match common atom masses, and transport the unmatched mass at cost at most
four. Therefore `K` is compact, including zero-weight limits.

The fixed initialized mark spaces, ridge `eta=1/4096`, and every correlation
within the lower `(b1,g)` law are those of the exact source. Use the invariant
active features `b1 in R6`, `b2 in R3`, and the complete evolving `3 x 6`
matrix. Put `theta=(w,c,M)`, `theta0=(g,0,D)`, and

\[
 \begin{gathered}
 a_\theta(u)=E_1[b_1\tanh(w\cdot u)],\qquad
 H_\theta(u)=\tanh(b_2^TMa_\theta(u)),\qquad
 f_\theta(u)=E_2[cH_\theta(u)],\\
 d_\theta(u)=E_2[b_2c(1-H_\theta(u)^2)],\qquad
 Q_\theta(u)=b_1^TM^Td_\theta(u),\qquad r=f_\theta-y.
 \end{gathered}
 \tag{3}
\]

The physical equations train all three blocks:

\[
 \begin{split}
 w'&=-2\int r\,\operatorname{sech}^2(w\cdot u)Q_\theta(u)u\,d\mu,\\
 c'&=-2\int rH_\theta(u)\,d\mu,\\
 M'&=-2\int r d_\theta(u)a_\theta(u)^T\,d\mu.
 \end{split}
 \tag{4}
\]

The raw norm is the sum-of-squares norm of the two population `L2` spaces
and the matrix Frobenius space. All times are physical GF times; no state
block is frozen and no time rescaling is substituted.

Define the exact initialized signed feature, its size, and the stationary
data set by

\[
 m_0(\mu)=\int yH_{\theta_0}(u)\,d\mu\in L^2(\Omega_2),\qquad
 s(\mu)=\|m_0(\mu)\|_2,\qquad
 Z=\{\mu\in K:m_0(\mu)=0\}.
 \tag{5}
\]

Let `rho(mu)=dist(mu,Z)`. A family has **slow onset** if

\[
 \text{for every }T<\infty,\qquad
 \sup_{0\le t\le T}|\mathcal L_{\mu_\varepsilon}(t)-1|\longrightarrow0.
 \tag{6}
\]

The family parameter tends to zero; the same statements apply to arbitrary
sequences. This is a compact-horizon definition, with the horizon fixed
before taking the data limit. For `0<delta<1`, define

\[
 \tau_\delta(\mu)=\inf\{t\ge0:\mathcal L_\mu(t)\le1-\delta\},
 \qquad\inf\varnothing=\infty.
 \tag{7}
\]

## The classification

For any family in `K`, the following are equivalent:

1. Slow onset in the sense (6).
2. `tau_delta(mu_epsilon) -> infinity` for **every** fixed
   `delta in (0,1)`.
3. `s(mu_epsilon) -> 0`, equivalently
   `-L_mu_epsilon'(0) -> 0`.
4. `rho(mu_epsilon) -> 0`.
5. Every convergent subsequence of data has its limit in `Z`.
6. For every fixed `T`, the complete raw state satisfies
   `sup_{t<=T} ||theta_mu_epsilon(t)-theta0||raw -> 0`.

Here `Z` has an exact finite geometric description. Ignore zero-weight
slots and group the remaining inputs into antipodal classes. In each class
choose a representative `v`, and write `u_i=sigma_i v`, `sigma_i in {+1,-1}`.
Then

\[
 \mu\in Z
 \quad\Longleftrightarrow\quad
 \sum_{i\text{ in each class}}p_i y_i\sigma_i=0.
 \tag{8}
\]

In particular, with three positive weights, all three directions must lie
in one antipodal class and their effective signed label masses must balance.
With exactly two positive weights, they must both be `1/2`, in one
antipodal class, with opposite effective signed labels. A single positive
weight cannot belong to `Z`. Each law in `Z` has the stronger property

\[
 \int yH_\theta(u)\,d\mu=0\quad\text{for every state }\theta,
 \qquad
 \mathcal L_\mu(\theta)=1+\int f_\theta(u)^2\,d\mu\ge1.
 \tag{9}
\]

Thus the stationary set in this three-input problem is an exact data
cancellation set, not a set identified only by an accidental small derivative.

The proof has three ingredients: the initialized ridge features distinguish
different antipodal classes, finite-time flow depends continuously on the
data, and the gradient energy controls the path near the cancellation set.

## Initialized features distinguish antipodal classes

The complete scalar proof in `initialization_positivity.md` supplies an odd
function `Psi` with `Psi(h)>0` for `h>0`, and the exact identity

\[
 V(u):=Da_{\theta_0}(u)=(T(u_1),T(u_2),T(u_3)),
 \quad
 T(r)=E[\Psi(\tanh G)\tanh(rG+\sqrt{1-r^2}N)],
 \tag{10}
\]

where `G,N` are independent standard Gaussians and endpoint values are by
continuity. This is a conditional expectation within the full canonical
joint law, not a replacement by independent lower features.

We need, and can prove, more than the sign of `T`: it is strictly increasing
on `[-1,1]`. For `g>0`, set

\[
 F_r(g)=E_N\tanh(rg+\sqrt{1-r^2}N),\qquad -1<r<1.
\]

Differentiating and integrating by parts in `N` gives

\[
 \partial_rF_r(g)
 =gE\phi'(rg+\sqrt{1-r^2}N)
   -rE\phi''(rg+\sqrt{1-r^2}N),\qquad\phi=\tanh.
 \tag{11}
\]

The integration boundary term is zero because `phi'` is bounded. If
`sigma>0`, then `E phi''(m+sigma N)` has strictly the opposite sign to
`m!=0`: pair the positive and negative integration variables to obtain

\[
 E\phi''(m+\sigma N)
 =\int_0^\infty\phi''(z)
    [\varphi_\sigma(z-m)-\varphi_\sigma(z+m)]\,dz.
 \tag{12}
\]

For `m>0`, the bracket is positive and `phi''(z)<0` for `z>0`; the negative
case follows by oddness. Consequently both terms in (11) are nonnegative
for `g>0`, and the first is strictly positive. The derivative is odd in `g`.
The bound `|partial_r F_r(g)|<=|g|+2` justifies differentiating (10) under
expectation. Since `Psi(tanh g)` has the sign of `g`, (11) gives
`T'(r)>0`. Dominated convergence gives continuity at both endpoints and
therefore strict monotonicity on the closed interval. Also `T` is odd.

It follows that `V` is nonzero on `S2` and

\[
 V(u)=V(v)\Longleftrightarrow u=v,
 \qquad V(u)=-V(v)\Longleftrightarrow u=-v.
 \tag{13}
\]

The upper mark `b2` has independent coordinates
`tanh(sqrt(nu) Z_j)/sqrt(tau+eta)` and a strictly positive density on the
open cube `(-1/sqrt(tau+eta),1/sqrt(tau+eta))^3`. Hence an `L2` identity
among the continuous functions `tanh(b2 dot V(u))` holds pointwise on that
cube.

Take `k<=3` nonzero vectors `v_j`, no two equal up to sign. The functions
`tanh(b dot v_j)` are linearly independent on this cube. To verify this,
choose a vector `q` outside the finitely many hyperplanes

\[
 q\cdot v_j=0,\qquad q\cdot(v_i-v_j)=0,
 \qquad q\cdot(v_i+v_j)=0.
\]

Such a vector exists: each proper hyperplane has zero three-dimensional
volume (solve for one coordinate and integrate its singleton sections),
so their finite union cannot contain a ball. The numbers `a_j=q dot v_j`
are nonzero and have distinct squares. Restricting a claimed linear
relation to `b=tq` for small `t` and comparing the first `k` odd Taylor
coefficients of

\[
 \tanh x=x-x^3/3+2x^5/15+O(x^7)
\]

gives `sum_j alpha_j a_j^(2l+1)=0`, `l=0,...,k-1`. The Vandermonde matrix
in the distinct numbers `a_j^2` is invertible: a polynomial of degree
at most `k-1` with these `k` distinct roots is zero, which proves its
transpose has trivial kernel. Thus `alpha_j a_j=0` for each `j`, and
all coefficients vanish.

Apply this to the distinct antipodal classes of `V(u_i)`, using (13).
The coefficient of each representative ridge feature is exactly the sum
in (8). This proves (8). Every singleton class with positive mass has a
nonzero coefficient; with at most three positive slots this also proves
the support descriptions following (8).

For every state, `a_theta(-u)=-a_theta(u)`, so
`H_theta(-u)=-H_theta(u)` and `f_theta(-u)=-f_theta(u)`. The cancellations
in (8) therefore persist for these features at every state. Expanding the
square loss proves (9). At initialization the only possibly nonzero
velocity is the readout velocity, and

\[
 F_\mu(\theta_0)=(0,2m_0(\mu),0),\qquad
 -\mathcal L_\mu'(0)=4s(\mu)^2.
 \tag{14}
\]

Unique existence consequently makes `theta0` stationary exactly for
`mu in Z`.

## Existence, energy, and finite-time dependence on the data

Write `d_*=||D||op` and `K_l=ess sup |b_l|<infinity`. Ridge normalization
gives `||U_l||op<=1` for `U_l v=b_l dot v`. In particular

\[
 |a_\theta(u)|\le1,\quad |d_\theta(u)|\le\|c\|_2,
 \quad\|H_\theta(u)-H_\theta(v)\|_2
       \le\|M\|_{op}\|w\|_2|u-v|.
 \tag{15}
\]

The bounded-feature contraction argument in the supplied model applies in
these fixed dimensions, with `w-g,c` bounded and `M` finite. Direct
differentiation in the declared metric gives

\[
 \mathcal L_\mu(t)+\int_0^t\|\theta_\mu'(s)\|_{raw}^2\,ds=1,
 \qquad
 R_\mu(t)^2:=\|\theta_\mu(t)-\theta_0\|_{raw}^2
       \le t[1-\mathcal L_\mu(t)]\le t.
 \tag{16}
\]

For continuation, `int |r| dmu<=1`, so `||c||infinity<=2t` and
`||M-D||F<=2t^2`. Also
`||w'||infinity<=4t K1(d_*+2t^2)`. These bounds prevent finite-time escape
in the local-existence space, give Cauchy endpoints, and allow repeated
local continuation. Hence every law in `K`, including its boundary, has
a unique solution through every finite time. The same proof uses the
current full state on restart.

For completeness, the flow is uniformly continuous, indeed Lipschitz,
in (2) on each fixed horizon in the raw norm. Here is a direct estimate
that avoids any assumption that unrestricted `L2` functions form an algebra.
On the ball `||theta-theta0||raw<=R`, put

\[
 B=d_*+R,\quad C=R,\quad W=\sqrt3+R,\quad J=1+C.
\]

For two states in this ball let `e_w,e_c,e_M` be their three component
distances and set

\[
 Z_1=B e_w+e_M,\quad
 F_1=e_c+CZ_1,\quad D_1=e_c+2CK_2Z_1.
\]

Contraction, the bounded feature envelope, and
`Lip(phi)<=1`, `Lip(phi')<=2` give, uniformly in the input,

\[
 \begin{gathered}
 |\Delta a|\le e_w,\quad
 \|\Delta H\|_2\le Z_1,\quad
 \|\Delta z\|_\infty\le K_2Z_1,\quad
 |\Delta f|\le F_1,\quad |\Delta d|\le D_1,\\
 \|Q\|_\infty\le K_1BC,\qquad
 \|\Delta Q\|_\infty\le K_1(Ce_M+BD_1).
 \end{gathered}
 \tag{17}
\]

Subtracting the products in (4) then yields

\[
 \begin{split}
 \|\Delta F_c\|_2&\le2(F_1+JZ_1),\\
 \|\Delta F_M\|_F&\le2(CF_1+JD_1+JC e_w),\\
 \|\Delta F_w\|_2&\le
 2K_1[BCF_1+J(2BCe_w+Ce_M+BD_1)].
 \end{split}
 \tag{18}
\]

Thus a finite constant `L_R>0`, independent of the data, satisfies

\[
 \|F_\mu(\theta)-F_\mu(\widetilde\theta)\|_{raw}
       \le L_R\|\theta-\widetilde\theta\|_{raw}.
 \tag{19}
\]

For example, sum the right sides of (18), bound each coefficient
distance by their sum, and use
`e_w+e_c+e_M<=sqrt(3)||theta-tilde theta||raw` to obtain such a constant.
In particular, (19) is not based on multiplication of two unbounded
population variables: all gate multipliers involving `Q` are bounded.

There is also a finite `A_R` with

\[
 \|F_\mu(\theta)-F_\nu(\theta)\|_{raw}\le A_R d(\mu,\nu).
 \tag{20}
\]

An explicit way to check every input multiplier in (20) is to put

\[
 P=\max(CBW,1),\quad Q_*=K_1BC,\quad
 Q_u=2K_1K_2B^2CW.
\]

The residual is `P`-Lipschitz in the cost (2); `a,H,d,Q` have input
Lipschitz constants respectively `W,BW,2CK2BW,Q_u`, with the last
one measured in the supremum norm. The lower gate has input `L2`
Lipschitz constant `2W`. The three integrands in (4) therefore have
Lipschitz constants bounded by

\[
 \begin{split}
 A_c&=2(P+JBW),\\
 A_M&=2[PC+J(2CK_2BW)+JCW],\\
 A_w&=2[PQ_*+J(2WQ_*+Q_u+Q_*)].
 \end{split}
 \tag{21}
\]

Integrating their differences against a coupling proves (20) with
`A_R=A_c+A_M+A_w`. This includes label changes and vanishing atom masses.

Both reached states stay in the ball `R=sqrt(T)` by (16). Combining
(19)--(20) with their integral equations, and integrating the scalar
inequality after multiplying by `exp(-L_R t)`, gives

\[
 \sup_{0\le t\le T}
 \|\theta_\mu(t)-\theta_\nu(t)\|_{raw}
 \le A_R\frac{e^{L_RT}-1}{L_R}\,d(\mu,\nu).
 \tag{22}
\]

The same bounds prove uniform loss continuity. At fixed input, (17)
controls the prediction difference, and the difference of squared
residuals is at most `2J` times the residual difference. At fixed state,
the squared residual is `2JP`-Lipschitz in (2). Consequently a finite
`C_T` satisfies

\[
 \sup_{t\le T}|\mathcal L_\mu(t)-\mathcal L_\nu(t)|
       \le C_Td(\mu,\nu).
 \tag{23}
\]

These estimates concern the actual complete flow. The constants may grow
with `T`; no all-time data stability is asserted.

## Proof of the equivalences and initial-feature estimates

The initial map is Lipschitz in the data. In fact (15) at initialization
gives, using the same coupling argument,

\[
 \|m_0(\mu)-m_0(\nu)\|_2
       \le \Lambda_0d(\mu,\nu),\qquad \Lambda_0=\max(d_*\sqrt3,1).
 \tag{24}
\]

Thus `Z` is compact and nonempty, and the distance to it is attained.
For any `a>0` for which the set is nonempty, compactness gives

\[
 \kappa(a):=\min_{\mu\in K:\rho(\mu)\ge a}s(\mu)>0,
 \qquad s(\mu)\le \Lambda_0\rho(\mu).
 \tag{25}
\]

The strict lower bound holds because a minimizer with value zero would
belong to `Z`, contradicting its distance at least `a`. Hence statements
3, 4 and 5 are equivalent. This uses compactness of data, not compactness
of a bounded set in the raw infinite-dimensional state space.

Statement 4 implies 6 by (22), choosing a nearest law in `Z`, whose
initialized trajectory is constant. Statement 6 implies 1 because
`|f_theta(u)|<=||c||2` and

\[
 |\mathcal L_\mu(\theta)-1|
 \le2\|c\|_2+\|c\|_2^2.
\]

Conversely, 1 implies 6 directly from (16). To obtain 1 implies 5, take
any convergent subsequence with limit `mu_*`. By (23), its limiting loss
equals `L_mu_*` on each compact interval. Under 1 this loss is identically
one, so (14) gives `m0(mu_*)=0`. This completes the dynamical equivalences.

For statements 1 and 2, loss is continuous, starts at one, and is
nonincreasing. If 1 holds, then for any fixed `delta,T`, eventually
`L(T)>1-delta`, so `tau_delta>T`. If 1 fails, there are `T>0`, `eta>0`
and a subsequence with `1-L(T)>=eta`. Choosing any fixed
`delta in (0,min(eta,1))` gives `tau_delta<=T` on that subsequence.
This proves the equivalence with **all** fixed drop thresholds. Checking
only one threshold does not prove 1.

One can also quantify the relation to the initial feature without relying
on subsequence arguments. Fix `T>0` and take `R=sqrt(T)` in (19). The
integral equation and (14) give

\[
 R_\mu(t)\le2s(\mu)\frac{e^{L_Rt}-1}{L_R},\qquad
 \|\theta_\mu'(t)\|_{raw}\le2s(\mu)e^{L_Rt}.
\]

Consequently

\[
 1-\mathcal L_\mu(t)
 \le\frac{2s(\mu)^2}{L_R}(e^{2L_Rt}-1),\qquad 0\le t\le T.
 \tag{26}
\]

For a uniform converse near time zero, use the radius-one ball, on which
the trajectory stays through time one by (16), and set
`t0=min(1,log(3/2)/L_1)>0`. For `0<=t<=t0`,

\[
 \|\theta_\mu'(t)-\theta_\mu'(0)\|_{raw}
 \le2s(\mu)(e^{L_1t}-1)\le s(\mu).
\]

The reverse triangle inequality and (14) show that the speed is at least
`s(mu)` there. Energy gives

\[
 1-\mathcal L_\mu(t)\ge s(\mu)^2t,
       \qquad 0\le t\le t_0.
 \tag{27}
\]

Equations (26)--(27) are the finite-time justification for using vanishing
initial slope in this compact family. An initial-slope observation by
itself, without these uniform estimates, would not justify a hitting-time
claim or a power-law delay exponent.

## A quantitative delay in distance to the cancellation set

The geometric identification of `Z` gives a stronger estimate than (22).
For any `r>0`, put

\[
 \Lambda_r=\max\{(d_*+r)(\sqrt3+r),1\}.
 \tag{28}
\]

Choose a nearest `nu in Z`. On `R_mu(t)<=r`, (9), (15) and coupling imply

\[
 \left\|m_\mu(\theta):=\int yH_\theta(u)\,d\mu\right\|_2
 =\|m_\mu(\theta)-m_\nu(\theta)\|_2
 \le \Lambda_r\rho(\mu).
 \tag{29}
\]

Expanding loss at the actual reached state and using (16) gives

\[
 \begin{split}
 0\le1-\mathcal L_\mu(t)
 &=2\langle c,m_\mu(\theta)\rangle_2-\int f_\theta(u)^2d\mu\\
 &\le2\Lambda_r\rho(\mu)R_\mu(t),\\
 R_\mu(t)^2&\le t[1-\mathcal L_\mu(t)].
 \end{split}
 \tag{30}
\]

Dividing only when `R_mu(t)>0` yields

\[
 R_\mu(t)\le2\Lambda_r\rho(\mu)t,\qquad
 1-\mathcal L_\mu(t)\le4\Lambda_r^2\rho(\mu)^2t.
 \tag{31}
\]

A first exit `R_mu(t_*)=r` must satisfy
`t_*>=r/(2 Lambda_r rho(mu))`. Continuity therefore validates (31) throughout

\[
 0\le t\le\frac{r}{2\Lambda_r\rho(\mu)}.
 \tag{32}
\]

If `rho(mu)=0`, the trajectory is stationary and these time bounds mean
all finite times. If `2r Lambda_r rho(mu)<delta`, loss cannot drop by `delta`
while the state is in this ball, by (30). Thus

\[
 \tau_\delta(\mu)\ge\frac{r}{2\Lambda_r\rho(\mu)}.
 \tag{33}
\]

In particular, with fixed `r=1`, approaching `Z` gives a lower bound of
order `rho^-1` for every fixed loss-drop threshold and a loss-deficit
bound of order `rho^2 t` through times of order `rho^-1`.
This is a universal lower bound, not a matching asymptotic rate. A family
may have additional centered-difference cancellation: the sharper
`epsilon^-2` result in `early_delay.md` remains useful, and is not
replaced by an initial-slope exponent or a claim that (33) is optimal.

## Balanced-label specialization, including vanishing weights

Suppose throughout that `p1+p2=p3=1/2` and the labels are `(+,+,-)`.
In the compact balanced class, (8) reduces exactly to

\[
 Z_{bal}=\{\tfrac12\delta_{(v,+1)}+
                \tfrac12\delta_{(v,-1)}:v\in S^2\}.
 \tag{34}
\]

Indeed the negative-label slot has weight `1/2`. Cancellation forces
every positive-weight positive-label slot into its antipodal class.
Since their weights sum to `1/2`, equality in the signed sum forces them
to have the same input direction as the negative-label slot, rather than
its negative. The argument allows one positive-label mass to vanish.

The distance to (34) is exactly

\[
 \rho_{bal}(\mu)=\min_{v\in S^2}\sum_i p_i|u_i-v|.
 \tag{35}
\]

For a target law in (34), all target directions equal `v`, so every
coupling pays the displayed input cost. Matching labels is possible
because the masses are balanced and adds zero label cost, proving (35).

All equivalences and bounds above hold with `K` replaced by its compact
balanced subclass, `Z` by (34), and `rho` by (35). Thus slow onset for
balanced three-input data means precisely that the weighted input radius
in (35) tends to zero. If all three masses are bounded below, this is
equivalent to the three input directions approaching one another. If a
positive-label mass vanishes, its direction need not approach the other
two. Requiring unweighted collapse of all three slots would be false.

## Why one deep hitting time can diverge without slow onset

Consider the strictly positive, balanced, linearly independent family

\[
 \begin{array}{c|c|c}
 u_1=e_1&p_1=1/4&y_1=+1\\
 u_2=e_2&p_2=1/4&y_2=+1\\
 u_3=\sqrt{1-\varepsilon^2}e_1+\varepsilon e_3
       &p_3=1/2&y_3=-1
 \end{array}\qquad 0<\varepsilon<1.
 \tag{36}
\]

The determinant of these input rows is `epsilon`. Its limit has a
contradictory pair at `e1`, but retains the independent positive input
at `e2`. For every state, that limiting loss is

\[
 \mathcal L_*(\theta)
 =\tfrac34(f_\theta(e_1)+\tfrac13)^2
  +\tfrac14(f_\theta(e_2)-1)^2+\tfrac23\ge\tfrac23.
 \tag{37}
\]

Its initialized signed feature is

\[
 m_0(\mu_*)=\tfrac14[H_{\theta_0}(e_2)-H_{\theta_0}(e_1)]\ne0.
 \tag{38}
\]

For example the two features are independent, centered, nonconstant
functions of the first and second upper marks, respectively, because
`T(1)>0`; their difference has positive squared norm. Thus
`L_*'(0)<0`. At a fixed sufficiently small positive time the limiting
loss is strictly below one, and (23) transfers a definite initial loss
decrease to (36). This family is not a slow-onset family.

Nevertheless, for every fixed `ell<2/3`, (23) and (37) show that the
hitting times of `L<=ell` tend to infinity. On any fixed horizon the
limit stays at least `2/3`, leaving a strict margin over `ell`.
The limiting loss itself is nonincreasing, drops strictly at first, and
has a limit in `[2/3,1)`. It therefore has a positive-loss plateau. No
claim is needed that this plateau equals the lower bound `2/3`.

This example establishes the distinction even under positive weights,
balanced labels, and independent inputs for every positive family
parameter. Divergence of one deep hitting time identifies neither the
start of learning nor the eventual fitting behavior of a fixed positive
member. The quantifier over **every** fixed positive loss drop in the
classification is essential.

## Claim boundary

The exact result is a necessary-and-sufficient compact-horizon
classification, with a geometric stationary set and quantitative lower
delay bounds. It includes zero limiting masses and preserves the full
trained dynamics. The proof supplies all state/data continuity needed
to pass to compact data limits; it does not exchange the data limit with
the infinite-time limit.

No upper hitting-time estimate, eventual full fitting for general
three-input data, terminal exponential rate, or optimal distance exponent
is established here. The plateau counterexample concerns a degenerate
limiting data law, not an asserted positive-loss limit for its genuine
three-input approximants. These boundaries are compatible with both
`early_delay.md` and `necessary_potential_growth.md`.
