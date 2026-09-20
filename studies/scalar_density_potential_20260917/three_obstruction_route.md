# Three-input stationary obstructions and a conditional convergence bridge

This is a bounded independent theory route. Scientific inputs were the supervisor's scalar equations, the coefficient target in `docs/observable_p1.md`, and the finite equations/existence discussion in C.4.7.10.C.1/C.3 of `docs/global_nonlinear.md`. No study proofs or other routes were read. No numerical experiments were run. These are internally derived partial results, not established repository theory.

The concrete conclusions are: positive stationary losses have a discrete gap of at least the smallest sample weight; under a nonzero middle weight and full lower support, every non-interpolating stationary state has a direction of strictly negative second variation; and entry below that loss gap implies fitting if the readout norm remains bounded. No bound on the middle scalar or lower state is needed for the last conditional result. None of these statements proves avoidance of saddles or excludes readout escape from the prescribed initialization.

## 1. Setup and exact dissipation

Write `u_i=x_i/sqrt(2)`, with three unit directions, positive weights `p_i` summing to one, and labels `y_i` in `{−1,+1}`. Directions are pairwise distinct and non-antipodal when this is explicitly required below. Put

\[
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad s_i=M a_i,
 \quad H_i(b)=\tanh(b s_i),
\]
\[
 f_i=E_2[cH_i],\quad d_i=E_2[bc\operatorname{sech}^2(bs_i)],
 \quad r_i=f_i-y_i,\quad L=\sum_i p_i r_i^2.
\]

The marks are those in the assignment: `b_1=tanh(g_1)/sqrt(nu+eta)`, `b=tanh(sqrt(nu)Z)/sqrt(tau+eta)`, with the stated Gaussian roots and positive `M(0)=D`. In particular, both marks are bounded, `b_1` is nonzero almost surely, and the upper mark has a positive density throughout an interval containing zero.

For the Hilbert metric `L²(lower;R²) ⊕ L²(upper) ⊕ R`, prediction gradients are

\[
 \nabla_w f_i=M d_i A_i,
 \qquad A_i(g)=b_1(g)\operatorname{sech}^2(w(g)\cdot u_i)u_i,
\]
\[
 \nabla_c f_i=H_i,\qquad \partial_M f_i=d_i a_i.
\]

Consequently the assigned flow satisfies

\[
 \dot L=-\|\dot w\|_2^2-\|\dot c\|_2^2-|\dot M|^2
 =-4r^T P K P r,
 \qquad K_{ij}=\langle\nabla f_i,\nabla f_j\rangle.
 \tag{1}
\]

All differentiations used below are justified along bounded perturbations by bounded tanh derivatives and dominated convergence. The state itself can have `w,c` in `L²`; bounded perturbations suffice for the negative-second-variation conclusions.

## 2. Upper feature independence, including the derivative direction

For positive, pairwise distinct numbers `t_j`, the functions `tanh(t_j b)` are linearly independent on the upper population. Moreover, for every real `s`,

\[
 \psi_s(b)=b\operatorname{sech}^2(sb)
 \notin\operatorname{span}\{\tanh(t_j b):j\}.
 \tag{2}
\]

Here the collection may include `|s|`; the claim is still valid. To prove it, write the Taylor expansion

\[
 \tanh z=\sum_{n\ge0}(-1)^n q_n z^{2n+1},\qquad q_n>0.
\]

Indeed `q_0=1`, and comparison in `tanh'=1−tanh²` gives

\[
 (2n+1)q_n=\sum_{j+k=n-1}q_jq_k>0\quad(n\ge1).
\]

An almost-sure linear relation is an identity on the interval where the upper density is positive, by continuity, so its Taylor coefficients vanish. Independence of the tanh functions reduces to

\[
 \sum_j v_j t_j^{2n+1}=0\quad(n\ge0).
\]

Dividing by the largest `t_j^{2n}` and sending `n` to infinity eliminates its coefficient; induction eliminates all coefficients. A putative representation of `psi_s` gives instead

\[
 (2n+1)s^{2n}=\sum_j v_jt_j^{2n+1}.
 \tag{3}
\]

For `s≠0`, coefficients at scales larger than `|s|` are first eliminated by the same argument. Division by `|s|^{2n}` then leaves a left side growing linearly in `n` and a bounded right side, a contradiction. For `s=0`, the equations for `n≥1` eliminate every coefficient, contradicting the equation for `n=0`. This proves (2).

The initialized readout Gram is therefore positive definite whenever the three initialized `a_i` are nonzero and their absolute values are pairwise distinct. This statement concerns the Gram at initialization, not a uniform lower bound along training.

## 3. Full lower support at every finite time

For every finite `T`, the bounded-mark estimates from the stated equations give bounds of the form

\[
 \sup_{t\le T}\|c(t)\|_\infty\le2T,
 \quad\sup_{t\le T}|M(t)|<\infty,
 \quad\sup_{t\le T,g}|w_t(g)-g|<\infty.
 \tag{4}
\]

The last estimate uses `dot w=−2 sum p_i r_i b_1 M d_i sech²(w·u_i)u_i`, the bounded marks, `sum p_i|r_i|≤sqrt(L)≤1`, and `|d_i|≤||b||∞||c||∞`. The dependence of the finite-time ODE on `g` is continuous: `b_1(g)` and the initial condition `w_0(g)=g` are continuous, and the vector field has locally uniform Lipschitz constants in `w` on each finite time interval. Thus `g↦w_t(g)` is continuous with bounded displacement from the identity.

Such a map is onto. For a target `z`, write `w_t(g)=g+v(g)` with `|v|≤C`. The continuous map `g↦z−v(g)` maps the closed Euclidean ball centered at `z` of radius `C` into itself. The finite-dimensional Brouwer fixed-point theorem applies to this nonempty compact convex ball and gives a fixed point, equivalently `w_t(g)=z`.

Every nonempty open set of `w` values therefore has a nonempty open preimage in `g`, of positive Gaussian measure. It follows that the law of `w_t` has full support. Correlation of `b_1` with `g_1` does not spoil the argument: `b_1=0` only on the Gaussian-null hyperplane `g_1=0`. In particular,

\[
 E_1[b_1^2\mathbf1_{\{w_t\in U\}}]>0
 \quad\text{for every nonempty open }U\subset\mathbb R^2.
 \tag{5}
\]

This is a finite-time statement. A merely `L²` limit of `w_t` as `t→∞` need not inherit the stated continuity or support property. A limit with uniform convergence of bounded increments does inherit them.

## 4. Independence of the three lower feature derivatives

Suppose (5) holds for a given state and the three directions are pairwise non-antipodal. Then the three `A_i` in Section 1 are linearly independent in lower `L²`.

If `sum_i v_i A_i=0` almost surely, (5) and continuity in the current `w` imply

\[
 \sum_i v_i\operatorname{sech}^2(z\cdot u_i)u_i=0
 \quad\text{for every }z\in\mathbb R^2.
 \tag{6}
\]

Fix `k` and take a unit vector `v` perpendicular to `u_k`. Because no other direction is parallel to `u_k`, `v·u_i≠0` for `i≠k`. Setting `z=Rv` in (6) and sending `R→∞` leaves exactly `v_k u_k=0`. Repeating this for each `k` proves independence.

The matrix `J_{ij}=E_1[A_i·A_j]` is therefore positive definite. Thus the map

\[
 \delta w\longmapsto (\delta a_i)_i
 =(E_1[A_i\cdot\delta w])_i
 \tag{7}
\]

is onto `R³`. Explicit bounded right inverses are linear combinations of the bounded fields `A_i`, with coefficients given by `J^{-1}`.

At any stationary state with `M≠0`, lower stationarity and this independence imply

\[
 r_i d_i=0\qquad\text{for each }i.
 \tag{8}
\]

Thus collision of upper features by itself is not enough for a stationary obstruction.

## 5. Discrete stationary-loss classification

This section needs only readout stationarity, `sum_i p_i r_i H_i=0`. It does **not** require lower full support, non-antipodal inputs, or lower stationarity.

If `M=0`, all predictions vanish and `L=1`. For `M≠0`, group the indices with nonzero `s_i` into classes `C` with the same absolute value `t_C=|s_i|>0`. Set

\[
 Z=\{i:s_i=0\},\quad \sigma_i=\operatorname{sign}s_i,
 \quad P_C=\sum_{i\in C}p_i,
 \quad P_C^\pm=\sum_{i\in C:\,\sigma_i y_i=\pm1}p_i.
\]

Writing `F_C=E_2[c tanh(t_C b)]`, one has `f_i=σ_iF_C` on `C`, while `f_i=0` on `Z`. The independence in Section 2 makes readout stationarity equivalent to

\[
 0=\sum_{i\in C}p_i\sigma_i r_i
 =P_CF_C-\sum_{i\in C}p_i\sigma_i y_i,
\]

for every nonzero class. Therefore

\[
 F_C=\frac{P_C^+-P_C^-}{P_C},\qquad
 L=P_Z+\sum_C\frac{4P_C^+P_C^-}{P_C},
 \quad P_Z=\sum_{i\in Z}p_i.
 \tag{9}
\]

For three samples, every stationary loss belongs to the following finite set, with distinct indices in each expression:

\[
 \left\{0,1,\ p_i,\ p_i+p_j,
 \frac{4p_ip_j}{p_i+p_j},
 \ p_i+\frac{4p_jp_k}{p_j+p_k},
 \ 4p_i(1-p_i)\right\}.
 \tag{10}
\]

This is an inclusion: no claim is made that every listed value is realized by an actual stationary scalar-model state, still less by the initialized flow.

In particular, with `p_min=min_i p_i`,

\[
 L>0\text{ at a readout-stationary state}
 \quad\Longrightarrow\quad L\ge p_{\min}.
 \tag{11}
\]

If `Z` is nonempty this follows from `P_Z≥p_min`. Otherwise a positive summand in (9) has both `P_C^+,P_C^-≥p_min`, and

\[
 \frac{4AB}{A+B}\ge2\min(A,B)\ge2p_{\min}.
\]

At `M=0`, full stationarity specifically requires

\[
 E_2[bc]\sum_i p_i y_i a_i=0;
\]

the other block velocities already vanish. If `M≠0` and all `a_i=0`, readout and middle velocities vanish; under (5) and non-antipodal directions, lower stationarity is equivalent to `E_2[bc]=0`. Both cases have loss one.

If the initialized Gram is positive definite, (1) gives

\[
 \dot L(0)=-4\left\|\sum_i p_i y_iH_i(0)\right\|_2^2<0.
\]

Hence `L(t)<1` for every `t>0`. A finite stationary state with `M=0`, or with all `a_i=0`, cannot be a finite-time endpoint or a strong bounded limit of this trajectory.

## 6. Every non-interpolating regular stationary state is a strict saddle

Assume `M≠0`, (5), pairwise non-antipodal directions, and full stationarity. If some `r_k≠0`, (8) gives `d_k=0`.

Let `V=span{H_1,H_2,H_3}` in upper `L²`, and define

\[
 h=\psi_{s_k}-\operatorname{Proj}_V\psi_{s_k}.
\]

Section 2 proves `h≠0`; all these functions are bounded. Moreover

\[
 E_2[hH_i]=0\quad\text{for all }i,
 \qquad E_2[h\psi_{s_k}]=\|h\|_2^2>0.
 \tag{12}
\]

Use (7) to choose a bounded lower perturbation `v` with

\[
 D a_i[v]=\delta_{ik}.
\]

Consider the bounded state perturbation

\[
 \delta\theta_\lambda=(\lambda v,h,0).
\]

Every first prediction variation vanishes: the readout part vanishes by (12), and the lower part is `λM d_i δ_ik=0`. For second variations, the term involving `D²a_i[v,v]` in `D²f_i` is multiplied in `D²L` by `r_i d_i=0`. Thus direct differentiation yields

\[
 D^2L[\delta\theta_\lambda,\delta\theta_\lambda]
 =C\lambda^2+4\lambda M p_k r_k\|h\|_2^2,
 \tag{13}
\]

where the finite constant is explicitly

\[
 C=2p_k r_k M^2 E_2[c b^2\tanh''(b s_k)].
\]

Choose the sign of `λ` opposite to the nonzero linear coefficient, and then choose `|λ|>0` small enough. Equation (13) is strictly negative. Along this bounded affine perturbation, the loss is twice continuously differentiable, its first derivative is zero at stationarity, and its second derivative is negative. Therefore the stationary state is not a local minimum and has a direction of strictly negative second variation.

This does not show that the prescribed initialized trajectory avoids its stable set. The nonzero-`M` hypothesis must not be dropped from the strict-saddle statement. For example, at `M=0,c=0` with `S=sum_i p_i y_i a_i=0`, the state is stationary and the entire loss Hessian is zero: the only potentially nonzero second prediction variation contributing to the loss is a middle/readout cross term proportional to `S`. Such states exist with full lower support: take `w=g`, equal-weight directions `(cos(theta),±sin(theta))` with opposite labels, and a third direction `e_2` with either label and the remaining positive weight, where `0<theta<pi/2`. The paired initial `a_i` coincide and the third is zero. By (7), choose a lower perturbation making `D S[v]>0`. Along `M=epsilon,c=epsilon b,w=g+epsilon v`, the signed target pairing of predictions is `epsilon³ E[b²]D S[v]+O(epsilon⁴)`, while squared predictions contribute `O(epsilon⁴)`. Thus the loss is below one for sufficiently small positive `epsilon`, despite the zero Hessian at the stationary state. These loss-one states are separately excluded as bounded limits after initial loss decrease.

## 7. Fitting below the gap under readout boundedness

Suppose at some finite `t_0`,

\[
 L(t_0)<p_{\min},\qquad
 \sup_{t\ge t_0}\|c(t)\|_2<\infty.
 \tag{14}
\]

Then `L(t)→0`. No boundedness or compactness assumption on `w(t)` or `M(t)` is needed for this conditional assertion.

Indeed `L` decreases to a limit `L_infty`. Dissipation gives an integrable `||dot c||²`, so there are times `t_n→∞` with `||dot c(t_n)||_2→0`. Pass to a subsequence on which every `s_i(t_n)=M(t_n)a_i(t_n)` converges in the compact extended real line. Boundedness of the readout sequence in its Hilbert space supplies a further weakly convergent subsequence `c(t_n) ⇀ c_*`. This uses the sequential weak compactness of bounded sets in a Hilbert space; its sole required hypothesis here is the bound in (14).

For a finite limit `s_{i,*}`, `H_i(t_n)` converges to `tanh(bs_{i,*})`. For an infinite limit, it converges almost everywhere to `sign(s_{i,*})sign(b)`. The upper law has no atom at zero, and all features have absolute value at most one, so dominated convergence gives strong `L²` convergence in both cases. Denote the limiting feature by `H_{i,*}`. Hence

\[
 E_2[c(t_n)H_i(t_n)]\longrightarrow E_2[c_*H_{i,*}].
\]

The feature difference is controlled in `L²` against the bounded readout norm, and the remaining pairing converges by weak convergence. Therefore residuals converge, and `dot c(t_n)→0` yields

\[
 \sum_i p_i r_{i,*}H_{i,*}=0.
\]

The functions consisting of `sign(b)` and any finite collection of `tanh(t_jb)` with distinct positive finite `t_j` are linearly independent on the upper population. Indeed an almost-sure relation is a continuous identity on the positive part of the upper interval; taking `b↓0` first forces the coefficient of `sign(b)` to vanish, after which Section 2 applies. Therefore the proof of (9) applies unchanged to this limiting tuple, with all infinite scales collected into one extra nonzero class with the appropriate signs. No actual finite lower state or finite middle scalar realizing that tuple is required. Thus either `L_infty=0` or `L_infty≥p_min`. The latter contradicts `L_infty≤L(t_0)<p_min`, proving fitting.

The missing hypothesis is exactly the readout bound in (14). The energy identity alone gives finite integrated squared speed, not a uniform bound on the readout norm. This proof also gives no exponential rate when limiting upper features collide or saturate. In particular, after entry below the gap, non-fitting would require an unbounded readout norm; escape of `M` or `w` alone cannot explain it.

## 8. What these results do and do not settle

* Proved: generic initialized upper Grams are positive when initialized feature magnitudes are distinct and nonzero; finite-time lower support survives the correlation of `b_1` with its Gaussian coordinate; upper critical losses have the gap (11); regular suboptimal stationary states have negative second variation; and (14) implies fitting.
* Not proved: a compatible generic triple reaches a suboptimal stationary state; a trajectory starting at the prescribed initializer avoids every strict saddle; or boundedness in (14) follows from the scalar equations.
* Also not proved: an arbitrary near-symmetric non-antipodal triple has an all-time exponential fitting potential. A finite-time entry argument combined with the discrete gap still needs a non-escape theorem, and an exponential conclusion needs a suitable kernel or equivalent coercivity estimate after entry.

Formal stationary examples or vanishing instantaneous Gram eigenvalues are therefore not actual-flow counterexamples. Conversely, initial positive definiteness is not an all-time coercivity proof.
