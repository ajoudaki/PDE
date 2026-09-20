# Bounded audit of `three_generic_route.md`, sections 4–6

Only the frozen sections 4–6 were read. The supplied scalar model and initialized mark law were the other scientific inputs. This audit did not inspect other parts of that route, expand the research program, or run numerical experiments.

**Verdict:** the bounded-subsequence convergence proposition, the small-gradient escape construction, and the finite local exponential certificate are mathematically valid within their stated scopes. There is one regularity qualification: on the Hilbert `L²` state space, the displayed `D²a_i` should mean bounded directional second variations, rather than an unqualified claim of twice Fréchet differentiability. The required `C^{1,1}` property and the exact stated Lipschitz constant follow directly from first-derivative difference estimates, supplied below. Thus this qualification does not weaken the certificate.

## 1. Bounded readout subsequences

The unit-interval argument is valid. Given bounded `||c(t_n)||_2` with `t_n→∞`, total finite dissipation implies

\[
 e_n=\int_{t_n}^{t_n+1}\|\dot c\|_2^2\,dt\longrightarrow0.
\]

A point `t_n'` with squared speed at most `2e_n` exists; if `e_n=0`, the speed is zero almost everywhere on the interval. Cauchy–Schwarz bounds the change in readout by `sqrt(e_n)`. This supplies both bounded readout norms and vanishing readout gradients along the same sequence, which is the essential alignment of the two hypotheses.

Compactification of each scalar feature parameter is legitimate. The limits at infinite parameter are `±sign(b)`, and the upper law has no atom at zero. Bounded convergence therefore gives convergence in upper `L²`. Residuals have convergent subsequences because each obeys `p_i r_i²≤1`.

Bounded readout norm preserves all zero-feature and signed-equal-feature relations in the outputs by Cauchy–Schwarz. No weak subsequence of the readout, compactness of the lower state, or boundedness of `M` is needed. The asserted independence of finite positive-scale tanh features together with `sign(b)` is correct: continuity makes a putative relation an identity on the positive part of the mark interval, the limit at zero eliminates the sign coefficient, and independence of distinct finite tanh scales handles the rest.

For completeness, the limiting readout stationarity gives, on each nonzero equal-magnitude class `C`,

\[
 F_C=\frac{\sum_{i\in C}p_i\sigma_i y_i}{\sum_{i\in C}p_i},
 \qquad
 L_\infty=P_Z+\sum_C\frac{4P_C^+P_C^-}{P_C}.
\]

Here `sigma_i` is the feature sign within its class and `P_Z` is the weight of zero limiting features. Infinite parameters form one additional nonzero class. A positive term is at least `p_min`: a zero-feature contribution is at least `p_min`, while a mixed-sign class contributes at least `2p_min`. Thus the below-gap contradiction is valid. The proposition proves exactly that positive limiting loss below the gap forces `||c(t)||_2→∞`, rather than merely an unbounded subsequence.

The bound on readout growth is also correct:

\[
 \frac{d}{dt}\|c\|_2^2
 =4(\langle y,f\rangle_p-\|f\|_p^2)
 =1-4\|f-y/2\|_p^2\le1.
\]

Starting from `c(0)=0`, it gives `||c(t)||_2²≤t`, which does not close the bounded-subsequence hypothesis.

## 2. Escape construction

The three geometric thresholds are correct. With the prescribed angles, `V_q·u_1` is positive everywhere, `V_q·u_2` changes sign when `S=4/5`, and `V_q·u_3` changes sign when `S=2/5`. Solving `S(z)=(1+tanh z)/2` gives respectively `z=log 2` and `z=(1/2)log(2/3)`, exactly as stated.

The lower state has all claimed properties:

* `w_R−g` is bounded by `R` for each finite `R`.
* `w_R(-g)=-w_R(g)` because the angular factor depends on `g_2²`.
* It fixes roots with `g_1=0`.
* Each lower gate tends to zero almost everywhere, since its exceptional sign-change levels have Gaussian measure zero.

Independence of the two Gaussian coordinates therefore gives the three stated positive, distinct limiting features for sufficiently large finite `q`. Their positive weighted variance proves `ell_q>0`; convergence of all three features to the common value `kappa` as `q→∞` proves `ell_q→0`. A fixed `q` with `0<ell_q<p_min` consequently exists.

The scaling estimates are correct and uniform across the three inputs:

\[
 f_{i,R}=\alpha_R a_{i,R}+O(R^{-2}),\qquad
 d_{i,R}=R\alpha_R+O(R^{-1}).
\]

Since `sum_i p_i(alpha_R a_{i,R}−1)a_{i,R}=0`, the actual residuals satisfy `sum_i p_i r_{i,R}a_{i,R}=O(R^{-2})`. Expanding the actual vector field, rather than a surrogate loss, then gives

\[
 \|\dot c\|_2=O(R^{-3}),\qquad |\dot M|=O(R^{-1}).
\]

For the lower block, the coefficients remain bounded and the gates vanish almost everywhere, so dominated convergence gives `||dot w||_2→0`. The state norms and strictly positive but degenerating individual readout Grams are as stated. This is a valid failure of a general Palais–Smale compactness assertion and of a uniform positive PL constant on the entire below-gap state set. It is not an actual-flow counterexample.

The all-positive labels in the written construction are not an obstacle to the mixed-label interpretation specified in this audit assignment. Replace only `(u_3,y_3)` by `(-u_3,-1)`. Then `a_3,H_3,f_3,r_3` all change sign, whereas `d_3` and the lower gates do not. Every term in all three block velocities and in the loss is unchanged. With weights `(1/4,1/4,1/2)`, the two label classes have equal total weight. The resulting three directions remain pairwise nonparallel and non-antipodal.

## 3. Hilbert regularity and the explicit local constant

The local certificate needs a continuously Fréchet differentiable output map with locally Lipschitz derivative. It does not need a twice continuously Fréchet differentiable map on `L²`.

Set `B_1=||b_1||_infinity`, `B_2=||b||_infinity`. For each input,

\[
 Da_i(w)[v]=E_1[b_1\operatorname{sech}^2(w\cdot u_i)(v\cdot u_i)].
\]

Taylor's theorem and `|tanh''|≤2` give the uniform remainder bound

\[
 |a_i(w+v)-a_i(w)-Da_i(w)[v]|\le B_1\|v\|_2^2.
\]

This proves Fréchet differentiability. The first-derivative difference satisfies

\[
 \|Da_i(w)-Da_i(\widetilde w)\|\le2B_1\|w-\widetilde w\|_2.
 \tag{A1}
\]

Thus `a_i` is `C^{1,1}` on lower `L²`. A bounded formula for directional second variations also exists, but does not generally imply that `Da_i` is Fréchet differentiable on `L²`: perturbations supported on progressively smaller sets can keep fixed amplitude while their `L²` norms vanish. The route's integration-over-bounded-directions explanation is sufficient in substance; labeling the second variations explicitly avoids an unnecessary stronger regularity assertion.

Here is a direct proof of the stated constant without second Fréchet derivatives. On the radius-`rho` ball, write

\[
 C=\|c_T\|_2+\rho,\qquad m=|M_T|+\rho,
 \qquad S_0=B_1\sqrt{1+m^2}.
\]

For `s_i=M a_i`,

\[
 \|Ds_i\|\le S_0,\qquad
 \|Ds_i(z)-Ds_i(\widetilde z)\|
 \le 2B_1(1+m)\|z-\widetilde z\|.
 \tag{A2}
\]

Indeed `Ds_i[v]=M Da_i[v_w]+a_i v_M`. Subtracting this formula at two states, using (A1), `|a_i|≤B_1`, and `|a_i−a_i_tilde|≤B_1||w−w_tilde||_2`, proves (A2). The ball is convex, so the bound on `Ds_i` also gives `|s_i−s_i_tilde|≤S_0||z−z_tilde||`.

Put `psi_s=b sech²(bs)`. Then

\[
 \|H_s-H_t\|_2\le B_2|s-t|,
 \quad\|\psi_s\|_2\le B_2,
 \quad\|\psi_s-\psi_t\|_2\le2B_2^2|s-t|.
\]

The output derivative is

\[
 Df_i(z)[v]=\langle v_c,H_{s_i}\rangle
           +\langle c,\psi_{s_i}\rangle Ds_i(z)[v].
\]

Subtracting at two states and using (A2) yields exactly

\[
 \|Df_i(z)-Df_i(\widetilde z)\|
 \le A\|z-\widetilde z\|,
\]
\[
 A=2B_2S_0+2B_2^2CS_0^2+2B_1B_2C(1+m).
 \tag{A3}
\]

The first term is the sum of the readout-feature change and the change of the readout coefficient in the second term; the other two terms control the change in `psi_s` and in `Ds_i`. Since `sum_i p_i=1`, stacking `sqrt(p_i)Df_i` leaves the same operator-norm bound. This fully verifies the claimed `A` for the stated Hilbert ball, with no bound on the Gaussian root or pointwise bound on readout perturbations.

## 4. Local exponential and state convergence constants

For `J` the weighted output derivative, `lambda_T=lambda_min(J_TJ_T^*)>0`, and `A rho≤sqrt(lambda_T)/2`, the triangle inequality gives

\[
 \|J(z)^*v\|\ge\frac{\sqrt{\lambda_T}}2\|v\|
\]

throughout the ball. Since `grad L=2J^*(sqrt(p_i)r_i)_i`,

\[
 \|\nabla L\|\ge\sqrt{\lambda_T}\sqrt L,
 \qquad \dot L\le-\lambda_T L.
\]

The path-length estimate in the route follows exactly by integrating `−dot L/||grad L||`. The strict condition `2sqrt(L(T))/sqrt(lambda_T)<rho` excludes first exit, and the tail estimate gives

\[
 \|z(t)-z_\infty\|
 \le\frac{2\sqrt{L(T)}}{\sqrt{\lambda_T}}
       e^{-\lambda_T(t-T)/2}.
\]

The zero-loss case is correctly separated. Continuity of the output map gives interpolation at the limit. All factors of two agree with the unhalved square-loss convention.

The certificate remains conditional on a finite state satisfying its inequalities. Neither initial Gram positivity nor the below-gap convergence proposition proves that such a state is reached by the prescribed initialized trajectory.
