# Dissipative approximations and a conditional continuation theorem at two hidden layers

2026-09-08. This report proves a partial result. **It does not prove the requested global Gaussian-initialized training limit.** The exponential tail premise in Theorem 2 is unproved for the approximations in Theorem 1. Nor does this report claim a finite-width limit from its population statements. These boundaries are part of the statements to be reviewed.

The practical activation is fixed throughout:

\[
\phi(s)=\frac34(1+s)+\frac14\tanh s.
\tag{1}
\]

It satisfies `|phi(s)|<=1+|s|`, `3/4<=phi'(s)<=1`, and `|phi''(s)|<=1/2`. No amplitude is chosen as a function of training time or input separation.

## 1. Complete analytic setting

Let `(Omega_j,P_j)`, `j=1,2`, be probability spaces with separable real Hilbert spaces `H_j=L2(Omega_j,P_j)`. Fix a bounded linear operator `A0:H1->H2`, always paired with its genuine Hilbert adjoint `A0*`. The operator `A0` need not be Hilbert–Schmidt. This is an explicit analytic hypothesis, not a construction of the initialized Gaussian action. The results below apply to that action if it has already been constructed on such spaces.

Fix unit vectors `u_1,u_2,u_3` in `R^d`, labels `y_i in {-1,1}`, and `w0 in L2(Omega1;R^d)` with `||w0 dot u_i||2=1`. The vectors need not be independent or separated. A standard Gaussian `w0` meets the norm hypothesis. The state and its norm are

\[
\Theta=(w,U,C)\in\mathcal H
=L^2(\Omega_1;\mathbb R^d)\oplus\mathrm{HS}(H_1,H_2)\oplus H_2,
\qquad
\|\Theta\|_{\mathcal H}^2=\|w\|_2^2+\|U\|_{\rm HS}^2+\|C\|_2^2.
\]

Initially `Theta0=(w0,0,0)`. Put `A=A0+U` and define

\[
\begin{split}
z_i&=w\cdot u_i,&h_i&=\phi(z_i),&v_i&=Ah_i,&k_i&=\phi(v_i),\\
f_i&=\langle C,k_i\rangle,&r_i&=f_i-y_i,&E&=\tfrac12\sum_i r_i^2,\\
b_i&=C\phi'(v_i),&q_i&=A^*b_i,&p_i&=r_iq_i,&P&=(\sum_i p_i^2)^{1/2}.
\end{split}
\tag{2}
\]

Products of scalar fields are pointwise on their stated layer. The operator `b tensor h` means `a -> b <h,a>` and has Hilbert–Schmidt norm `||b||2 ||h||2`. Define the true directions

\[
g_w=\sum_i\phi'(z_i)p_i u_i,
\qquad g_U=\sum_i r_i b_i\otimes h_i,
\qquad g_C=\sum_i r_i k_i,
\qquad F(\Theta)=-(g_w,g_U,g_C).
\tag{3}
\]

A strong solution means a `C1` curve in `H` satisfying its displayed equation in `H`. Every field in (2) belongs to `L2`. On each bounded state ball, all their `L2` norms, all residuals, and all three norms in (3) have bounds depending only on the ball, `||A0||`, and the fixed data. Indeed `||U||op<=||U||HS`, activations grow at most linearly, and their derivatives are bounded. Forward fields and residuals are Lipschitz on these balls; backward fields are continuous there but are not asserted to be Lipschitz.

Here is the continuity fact used repeatedly. If `a_n->a` in `L2`, `z_n->z` in `L2`, and `m` is bounded and continuous, then

\[
a_nm(z_n)\longrightarrow am(z)\quad\hbox{in }L^2.
\tag{4}
\]

The term `(a_n-a)m(z_n)` tends to zero by boundedness. For the remaining term, every subsequence has a further subsequence on which `z_n->z` almost surely; dominated convergence against `|a|²` applies. If convergence of the whole sequence failed, this subsequence property would give a contradiction. Equation (4), operator continuity, and the rank-one inequality prove the asserted continuity of all backward fields and `F`.

For every strong curve the exact loss chain rule is

\[
E'=\langle g_w,\dot w\rangle
+\langle g_U,\dot U\rangle_{\rm HS}
+\langle g_C,\dot C\rangle.
\tag{5}
\]

To justify it without asserting Fréchet differentiability of a nonlinear `L2` Nemytskii map, choose coordinatewise absolutely continuous versions of its preactivation paths. Such versions follow from their Bochner integral representations and Fubini's theorem. The scalar chain rule gives `hdot_i=phi'(z_i) zdot_i`; its right side is `L2`-continuous by (4) with the continuous velocity as the incoming field. Then `vdot_i=Udot h_i+A hdot_i`, and `kdot_i=phi'(v_i) vdot_i`. Differentiate `<C,k_i>`, use the genuine adjoint, multiply by `r_i`, and sum to obtain (5).

## 2. A smooth cap

Choose a smooth nonincreasing function `eta:[0,infinity)->[0,1]` equal to one on `[0,1]` and zero on `[2,infinity)`. For example, on `(1,2)` use

\[
\eta(s)=\frac{\rho(2-s)}{\rho(2-s)+\rho(s-1)},
\qquad \rho(t)=\begin{cases}e^{-1/t},&t>0,\\0,&t\le0,\end{cases}
\]

and use the stated constants elsewhere. For `R>=1` define

\[
\tau_R(s)=\operatorname{sgn}(s)R\int_0^{|s|/R}\eta(a)\,da,
\qquad
\chi_R(s)=\begin{cases}\tau_R(s)/s,&s\ne0,\\1,&s=0,\end{cases}
\qquad
H_R(p)=\chi_R(|p|)p\quad(p\in\mathbb R^3).
\tag{6}
\]

The maps `tau_R,H_R` are smooth and 1-Lipschitz; they equal the identity inside the radius `R` ball and have magnitude at most `min(input magnitude,2R)`. Also `0<chi_R<=1`. For `H_R`, its radial Jacobian eigenvalue is `tau_R'(|p|)` and its two tangential eigenvalues are `tau_R(|p|)/|p|`, all in `[0,1]`; integrating its Jacobian along a segment proves the Lipschitz bound. Smoothness at zero follows since the map is the identity there. In particular

\[
|p-H_R(p)|\le |p|\mathbf1_{|p|>R},
\qquad |s-\tau_R(s)|\le |s|\mathbf1_{|s|>R}.
\tag{7}
\]

## 3. Unconditional approximation theorem

**Theorem 1.** For every `R>=1`, the equations

\[
\dot w_R=-\sum_i\phi'(z_{R,i})H_R(p_R)_i u_i
          =-\chi_R(P_R)g_{w,R},
\qquad
\dot U_R=-g_{U,R},
\qquad
\dot C_R=-\tau_R(g_{C,R}),
\tag{8}
\]

started from `Theta0`, have a unique global strong solution. Uniqueness here is among strong solutions of (8) with the same initial state. They obey

\[
E_R(t)+\int_0^t\|\dot\Theta_R(s)\|_{\mathcal H}^2ds\le E_0=3/2,
\qquad
\|\Theta_R(t)-\Theta_0\|_{\mathcal H}\le\sqrt{tE_0},
\qquad |C_R(t)|\le2Rt\quad\hbox{a.e.}
\tag{9}
\]

On `[0,T]`, all true field `L2` norms and `||F(Theta_R)||` are bounded uniformly in `R`. These approximations are dissipative modifications of the raw gradient, not the true raw gradient flow at finite `R`.

**Proof.** Fix `T<infinity` and set `M=1+2RT`. Temporarily replace `C` in `b_i` by `tau_M(C)` and compute `q_i,p_i` from that replacement. Use these replacements in the first two equations of (8). Keep the actual forward predictions, residuals and readout equation. This gives an autonomous extension on all of `H`.

On a state ball the extended top gate satisfies

\[
\|\tau_M(C)\phi'(v_i)-\tau_M(\bar C)\phi'(\bar v_i)\|_2
\le\|C-\bar C\|_2+M\|v_i-\bar v_i\|_2.
\tag{10}
\]

Apply `A*` and use its operator norm, with `||A-bar A||op<=||U-bar U||HS`, to compare the extended `q_i`. The residual-weighted fields satisfy

\[
\|p_i-\bar p_i\|_2
\le |r_i|\|q_i-\bar q_i\|_2
   +|r_i-\bar r_i|\|\bar q_i\|_2.
\tag{11}
\]

For the lower gate, the cap is used before estimating the multiplier:

\[
\|\phi'(z_i)H_R(p)_i-\phi'(\bar z_i)H_R(\bar p)_i\|_2
\le\|p-\bar p\|_{L^2(\mathbb R^3)}+R\|z_i-\bar z_i\|_2.
\tag{12}
\]

The rank-one inequality

\[
\|b\otimes h-\bar b\otimes\bar h\|_{\rm HS}
\le\|b-\bar b\|_2\|h\|_2+\|\bar b\|_2\|h-\bar h\|_2
\tag{13}
\]

controls the matrix direction. The readout cap is 1-Lipschitz. Equations (10)–(13) and forward Lipschitzness give a Lipschitz constant `K_{B,T}(1+R)` on a state ball of radius `B`. There is no product of the two cap sizes: the incoming-argument Lipschitz constant of `H_R` is one.

The extension's field norm on that ball has a bound independent of `R,M`, since each cap decreases magnitude, bounded gates multiply only `L2` fields, and operator/rank-one norms have the bounds already given. Picard iteration on a short interval now constructs a unique strong solution: choose the interval so its length times the field bound preserves a closed path ball and its length times the Lipschitz constant is less than one. The path space is complete and the integral map is a contraction.

The readout integral equation yields `|C(t)|<=2Rt<M` throughout its existence interval before `T`. Thus the auxiliary top cap is inactive there. Substituting (8) into (5) gives

\[
E'=-\int\chi_R(P)|g_w|^2-\|g_U\|_{\rm HS}^2
    -\int\chi_R(g_C)|g_C|^2
\le-\|\dot\Theta_R\|_{\mathcal H}^2,
\tag{14}
\]

because `chi_R²<=chi_R`. The same scalar cap multiplies the entire first-row gradient, which is essential for (14). Integrating and applying Cauchy–Schwarz in time proves (9).

If the maximal extension ended before `T`, (9) would keep it in a fixed state ball. The bounded field norm makes it Cauchy at that endpoint. The endpoint has `|C|<=2RT` a.e., since this property is closed under strong `L2` convergence. Local existence for the same extension continues the path, a contradiction. Different choices of `T` yield identical paths on overlaps: their readouts are bounded on each overlap, so (10)–(13), with one sufficiently large common `M`, and the integral contraction/iteration argument give uniqueness. Every strong solution of (8) itself has the pointwise readout bound and so belongs to the same extended equation on each compact interval. This proves the stated uniqueness and global construction. The final uniform true-field bounds follow from (9) and the ball bounds in Section 1. ∎

## 4. A conditional theorem that removes the caps

**Theorem 2.** In addition to the setting of Theorem 1, assume the following unproved premise: for every `T<infinity` there are finite `K_T,c_T>0` such that, for every `R>=1`, `0<=t<=T`, and `a>=1`,

\[
\|P_R(t)\mathbf1_{P_R(t)>a}\|_2
+\|g_{C,R}(t)\mathbf1_{|g_{C,R}(t)|>a}\|_2
\le K_T e^{-c_T a}.
\tag{15}
\]

Then `Theta_R` converges in `C([0,T];H)` for every finite `T` to one global strong solution of the true equation `Thetadot=F(Theta)`. Every true field in (2) converges uniformly in `L2` on that interval, and each of the three kernel matrices

\[
\Gamma_{ij}\langle d_i,d_j\rangle,
\qquad \langle b_i,b_j\rangle\langle h_i,h_j\rangle,
\qquad \langle k_i,k_j\rangle,
\quad d_i=\phi'(z_i)q_i,\quad\Gamma_{ij}=u_i\cdot u_j
\tag{16}
\]

converges uniformly. The limit has the true energy identity. It is unique against bounded-state strong competitors from the same initial state, and restarts uniquely from every reached state. These are assertions on the given population spaces. They do not identify finite Gaussian arrays with those spaces or prove a finite-width GF/GD limit.

**Proof.** We first obtain readout tails from the second term of (15). That term implies a uniform exponential probability tail for `|g_C|` on `[0,T]`: for `a>=1`, Markov's inequality on the event `|g_C|>a` gives a bound `K_T² a^{-2} exp(-2c_Ta)`. Enlarging its constants covers `0<=a<1`. The layer-cake identity

\[
\mathbb E|X|^m=m\int_0^\infty a^{m-1}\mathbb P(|X|>a)\,da
\]

therefore gives `||g_C||_m<=D_T m` for integers `m>=2`. Here the integral of `a^{m-1}exp(-ca)` equals `(m-1)! c^{-m}`, by repeated integration by parts, and `m!<=m^m`. Since `|tau_R(g_C)|<=|g_C|`, the readout integral equation and Minkowski's inequality imply

\[
\sup_{R,t\le T}\|C_R(t)\|_m\le T D_Tm\quad(m\ge2).
\tag{17}
\]

Choose an integer `m` proportional to `a` in Markov's inequality; for example `m=floor(a/(eTD_T))` when this is at least two. This gives a uniform exponential probability tail for `C_R`. Integrating that tail, using

\[
\mathbb E[X^2\mathbf1_{|X|>a}]
=a^2\mathbb P(|X|>a)+\int_a^\infty2s\mathbb P(|X|>s)\,ds,
\]

and absorbing the polynomial factors into a smaller exponential rate proves

\[
\sup_{R,t\le T}\|C_R(t)\mathbf1_{|C_R(t)|>a}\|_2
\le D'_T e^{-c'_T a},\qquad a\ge1.
\tag{18}
\]

We next prove an Osgood modulus, including its orientation. For a bounded Lipschitz scalar `m`, any fixed incoming field `a`, any `z,bar z`, and cutoff `L>=1`,

\[
\|a(m(z)-m(\bar z))\|_2
\le \operatorname{Lip}(m)L\|z-\bar z\|_2
   +2\|m\|_\infty\|a\mathbf1_{|a|>L}\|_2.
\tag{19}
\]

This follows by splitting into `|a|<=L` and its complement and applying the triangle inequality. For states `Theta,bar Theta` on a common bounded ball, split

\[
b_i-\bar b_i=(C-\bar C)\phi'(v_i)
+\bar C[\phi'(v_i)-\phi'(\bar v_i)].
\tag{20}
\]

Equation (19) uses tails only of the reference `bar C`. Forward differences have already been bounded linearly by the state distance. The genuine adjoint and (11) next compare `q_i,p_i`. Finally split

\[
g_w-\bar g_w
=\sum_i\bigl[\phi'(z_i)(p_i-\bar p_i)
+\bar p_i(\phi'(z_i)-\phi'(\bar z_i))\bigr]u_i.
\tag{21}
\]

Use (19) again, this time with reference incoming `bar p_i`, whose tail is bounded by that of `bar P`. Equations (13), (20) also handle the matrix direction; the readout direction uses only forward differences. Crucially, the first term of (21) does not multiply the already obtained `p` difference by another `L`. Thus, if the reference state has tails (15), (18), the true field satisfies, with `s=||Theta-bar Theta||`,

\[
\|F(\Theta)-F(\bar\Theta)\|\le K(1+L)s+K e^{-cL}.
\tag{22}
\]

Constants here and below can depend on `T` and the common state ball, but not on its approximating indices. Taking `L=max(1,c^{-1}log(1/s))` for `0<s<1`, and using bounded field norms for larger distances, gives

\[
\|F(\Theta)-F(\bar\Theta)\|
\le a_T s\log(B_T/s).
\tag{23}
\]

Choose `B_T` larger than `e` times the diameter of the comparison ball and large enough to absorb constants. The right side is increasing on the relevant distance range. At `s=0` it is interpreted as zero. The modulus also holds between any two approximants, because either can be the reference.

By (7), (8), and (15), their true-direction defects satisfy

\[
\|\dot\Theta_R-F(\Theta_R)\|
\le\sqrt3\|P_R\mathbf1_{P_R>R}\|_2
   +\|g_{C,R}\mathbf1_{|g_{C,R}|>R}\|_2
\le K e^{-cR}.
\tag{24}
\]

Consequently, for `S>=R`, the absolutely continuous distance between the two approximants satisfies the integral version of

\[
s'\le a_T s\log(B_T/s)+\delta_R,
\qquad s(0)=0,\qquad \delta_R=K' e^{-cR}.
\tag{25}
\]

An elementary scalar comparison proves convergence without invoking an external uniqueness theorem. Let `Y(0)=delta_R` and `Y'=a_T Y log(B_T/Y)+delta_R`. While in the bounded comparison range, `Y>=delta_R` and `log(B_T/Y)>=1`, so

\[
Y'\le(a_T+1)Y\log(B_T/Y),
\qquad
Y(t)\le B_T(\delta_R/B_T)^{\exp(-(a_T+1)t)}.
\tag{26}
\]

The bound follows by differentiating `log(B_T/Y)`. The usual first-crossing argument for scalar integral inequalities, or its strictly larger initial-value version followed by a limit, gives `s<=Y`. A first-exit argument with (26) ensures the comparison stays in range for all sufficiently large `R` on `[0,T]`. Thus `Theta_R` is uniformly Cauchy there.

The state limit is continuous. Continuity of each true field and of `F`, proved in Section 1, gives uniform convergence of their paths as well, even though `R` ranges over real values. To check this, take any sequence `R_n->infinity`. The union of the images of `Theta_{R_n}` and the limit path has compact closure in `H`: for any positive accuracy, uniform convergence places all sufficiently late paths within that accuracy of the compact limit image, and the finitely many earlier path images are compact. Completeness gives compactness from this total boundedness. Each field map is uniformly continuous on this compact closure. If uniform field convergence failed for the full family, a sequence of cap values tending to infinity witnessing that failure would contradict this argument. Equations (24) and the integral equations therefore pass to

\[
\Theta(t)=\Theta_0+\int_0^tF(\Theta(s))\,ds.
\tag{27}
\]

It is a strong solution because the integrand is continuous. The same argument gives uniform strong convergence of all fields, including `d_i`, by (4), and then of (16) by Cauchy–Schwarz. The exact energy identity follows directly from (5), rather than by asserting convergence of dissipations without proof.

The limit inherits exponential squared-amplitude tails for `C` and `P`: strong `L2` convergence implies convergence in probability, and an almost-sure subsequence with threshold `a/2` and Fatou's lemma bounds its tail above `a` by the uniform approximating tail above `a/2`. Constants may change. Compare any bounded-state strong competitor with this reference limit using (19)–(23); no tails of the competitor are needed. Its distance satisfies (25) with zero forcing. Apply the scalar majorant argument with arbitrary positive initial majorant and zero forcing, then let that initial value tend to zero. The distance is identically zero. On overlapping horizons the same uniqueness identifies the constructed limits. At any reached time, the already constructed global curve supplies a continuation; uniqueness from that reached state follows by this identical comparison on its next compact interval, using the reference curve's tails there. This proves the restart statement and the theorem. ∎

## 5. What remains unproved

Theorem 1 removes a loss-dissipation obstruction in a particular approximation scheme. It does not imply (15). Bounded `L2` norms alone do not imply uniform square-integrability: on a nonatomic probability space the fields `a_n=sqrt(n) 1_(0,1/n)` have norm one, with that norm entirely above each fixed amplitude cutoff for all sufficiently large `n`.

This example is not a trajectory or a counterexample to the desired theorem. The unresolved question is whether the actual approximations (8), with the Gaussian-program initialized action and physical residual feedback, avoid such concentration with enough quantitative control, or admit a different direct comparison argument. A proof of that assertion must retain the same matrix action and its adjoint and all their adapted returns.

Even after that question is answered, a finite-width theorem must explicitly identify the initialized action from finite Gaussian programs, retain the actual small random finite readout, compare the actual finite GF and simultaneous raw GD with step `n^-2`, and transfer the requested field path, kernel, velocity and second-moment observations. None of these additional bridges is asserted here. The full practical fixed-depth problem remains open in this report.
