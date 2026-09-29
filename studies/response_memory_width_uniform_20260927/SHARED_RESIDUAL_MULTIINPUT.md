# Shared dense residuals with evolving outer weights

Scope of Sections 1--6: two hidden tanh layers, canonical mobilities and finite training inputs. This note uses only `paper/main.tex`, `paper/comparison_appendix.tex`, and `docs/notation.qmd` as scientific inputs. Those sections concern an externally supplied middle operator reconstructed from **dense** histories. Sections 7--8 check a subsequently authorized, stronger oracle: its own histories and reconstructed matrices evolve, while dense residuals and dense backpropagation gates are supplied externally. That stronger construction works at every fixed finite depth and for arbitrary fixed finite data.

**Result.** A width-uniform outer-weight and prediction bound follows from an operator approximation bound when the nonzero training directions are pairwise orthogonal (with repetitions and sign reversals allowed). This includes the one-sample case. For arbitrary correlated inputs, sharing the residual leaves a potentially unbounded first-layer curvature multiplier. The calculations below do not settle uniform stability of the actual dense-history Legendre oracle in that case. They identify an exact obstruction to extending the scalar coordinate cancellation through a common change of variables or a common invariant metric. This is not a counterexample to that oracle.

There is also a separate, unconditional approximation result: at two hidden layers and exactly zero readout, the external dense-history middle reconstruction has a width-uniform `P^{-2}` Hilbert--Schmidt/Frobenius error on every fixed horizon, conditional only on a width-uniform initialized operator bound and fixed data. This matrix result does not settle the remaining outer-weight feedback problem.

## 1. Equations and width-independent bounds

Write

\[
q_a=x_a/\sqrt d,\quad G_{ab}=q_a^Tq_b,\quad
U=W^{(1)},\quad M=W^{(2)},\quad
s(z)=\operatorname{sech}^2z,
\]

and use the following response notation for the dense flow:

\[
z_a=Uq_a,\quad h_a=\tanh z_a,\quad
v_a=Mh_a,\quad k_a=\tanh v_a,
\quad d_a=w\odot s(v_a),\quad b_a=M^Td_a.
\]

Thus the first-layer backward response is `s(z_a) ⊙ b_a`; the symbol `b_a` in this note is the backpassed top response, not the residual-weighted history denoted by that letter in the paper's proof appendix.

Let

\[
c_a(t)=-2r_a^{\rm D}(t)/m,\qquad
C(t)=\sum_a|c_a(t)|,\qquad R(t)=\int_0^t C(u)\,du.
\]

The two systems have identical initial outer weights and satisfy

\[
\dot U=\sum_a c_a[s(z_a)\odot b_a]q_a^T,
\qquad \dot w=\sum_a c_a k_a,
\tag{1}
\]

with `(U,M,w)` replaced by `(bar U,A_P,bar w)` for the oracle. All oracle responses are its own responses, but `c_a` is shared. Suppose

\[
\sup_{t\le T}\|A_P(t)-M(t)\|_{\rm op}\le\varepsilon,
\qquad
\sup_{t\le T}\max(\|A_P(t)\|_{\rm op},\|M(t)\|_{\rm op})\le K.
\tag{2}
\]

Because `|tanh|≤1`, both readouts obey the pointwise bound

\[
\|w(t)\|_\infty,\ \|\bar w(t)\|_\infty
\le\|w(0)\|_\infty+R(t)\le B.
\tag{3}
\]

Dense loss decreases, so `C(t)≤2 rho_D(t)≤2 rho_D(0)`. These bounds, the assumed operator bound, and `(1)` also bound the outer velocities in normalized Frobenius/Euclidean norm independently of width. At each finite width they prevent escape on `[0,T]`; smooth dependence on the outer variables gives the usual continuation for a continuous supplied `A_P`.

The operator bounds in `(2)` need not be separately postulated for the external dense-history reconstruction. Put

\[
S=\int_0^T\rho_{\rm D}(t)\,dt,\qquad \tau_T=1+S,
\qquad B=\|w(0)\|_\infty+2S.
\]

The canonical middle update and normalized rank-one identity give

\[
\|M(t)\|_{\rm op}
\le\|M(0)\|_{\rm op}
+\|w(0)\|_\infty R(T)+\tfrac12 R(T)^2.
\tag{4}
\]

For the dense clock `xi=1+int rho_D`, let `eta_a=(r_a/rho_D)d_a` after the prefix, and set `eta_a=0`, `h_a=h_a(0)` on `[0,1]`. The external reconstruction is

\[
A_P=M(0)-\frac2{nm}\sum_a\int_0^{\tau(t)}
(\Pi_P\eta_a)(\Pi_Ph_a)^T\,d\xi.
\tag{5}
\]

Here `Pi_P` is the componentwise orthogonal projection on degree `<P` polynomials on the current history interval. Projection contraction and Cauchy--Schwarz give

\[
\|A_P-M(0)\|_{\rm op}
\le 2\left(\frac1m\sum_a\int\frac{\|\eta_a\|_2^2}{n}\,d\xi\right)^{1/2}
\left(\frac1m\sum_a\int\frac{\|h_a\|_2^2}{n}\,d\xi\right)^{1/2}
\le2B\sqrt{S(1+S)}.
\tag{6}
\]

In the last step, `sum_a(r_a/rho_D)^2=m`, the residual-weighted history has zero prefix, and `|h_a|≤1`. Thus a uniform bound on the initialized operator produces a common `K` in `(2)` independently of `P,n`. For Gaussian initialization this remains a deterministic statement on the event where the initialized operator has the selected bound; no probabilistic conclusion is asserted here.

## 2. The exact term that survives residual sharing

Let `L_s=sup |s'|=4/(3 sqrt 3)`. For any input `a`, define the ordinary RMS preactivation and readout errors

\[
e_{z,a}=\|\bar z_a-z_a\|_2/\sqrt n,
\qquad e_w=\|\bar w-w\|_2/\sqrt n.
\]

Bounded/Lipschitz tanh, `(2)`, and `(3)` imply

\[
\frac{\|\bar v_a-v_a\|_2}{\sqrt n}
\le K e_{z,a}+\varepsilon,
\]

\[
\frac{\|\bar d_a-d_a\|_2}{\sqrt n}
\le e_w+L_sB(Ke_{z,a}+\varepsilon),
\]

and hence

\[
\frac{\|\bar b_a-b_a\|_2}{\sqrt n}
\le Ke_w+L_sK^2B e_{z,a}
+B(1+L_sK)\varepsilon.
\tag{7}
\]

This backward estimate is width-independent. The top gate is harmless because its multiplying readout is bounded pointwise. But subtracting the first-layer equations also produces

\[
[s(\bar z_a)-s(z_a)]\odot b_a.
\tag{8}
\]

An estimate proportional to `e_{z,a}` would use `||b_a||_infty`, while the present hypotheses give only `||b_a||_2/sqrt n≤KB`. Multiplication by a vector has Euclidean operator norm equal to its largest absolute coordinate. Consequently an RMS bound on `b_a` alone does not justify a width-uniform Lipschitz bound for `(8)`.

There is also an informative sign issue. Treat the middle operator as supplied, and write the outer state in the canonical normalized Hilbert metric. The shared-residual equation is the negative gradient of the time-dependent function

\[
\frac2m\sum_a r_a^{\rm D}(t)f_a(U,w;A_P(t)).
\]

Its state derivative contains only the residual-weighted Hessians of the predictions. In the corresponding own-residual loss gradient, differentiation also gives the positive-semidefinite Gram term `2/m sum_a Df_a ⊗ Df_a` in the Hessian, whose contribution to the flow is dissipative. Sharing the residual removes that term; it does **not** remove the first-layer residual-curvature multiplier underlying `(8)`. This observation alone does not imply instability.

## 3. Complete stability result for orthogonal training directions

Assume first that all nonzero `q_a` are pairwise orthogonal, and set `g_a=||q_a||_2^2>0`. Zero inputs can be omitted: with this bias-free odd network they produce zero prediction and zero parameter update. Let `X=max_a ||q_a||_2`.

Use the exact scalar transformation

\[
F(z)=\int_0^z\cosh^2u\,du=\frac z2+\frac{\sinh(2z)}4,
\qquad F'(z)s(z)=1,\qquad F'(z)\ge1.
\tag{9}
\]

Orthogonality gives `dot z_a=g_a c_a s(z_a) ⊙ b_a`; therefore

\[
\frac d{dt}\frac{F(\bar z_a)-F(z_a)}{\sqrt{g_a}}
=\sqrt{g_a}c_a(\bar b_a-b_a).
\tag{10}
\]

All scalar applications in `(9)--(10)` are coordinatewise. Define

\[
e_U=\left(\sum_a\frac{\|F(\bar z_a)-F(z_a)\|_2^2}{ng_a}\right)^{1/2},
\qquad E=e_U+e_w.
\]

The inverse of `F` is globally 1-Lipschitz. Moreover both first-layer updates lie in the span of the `q_a`, and their initial weights agree. Expanding their difference in this orthogonal basis gives

\[
\frac{\|\bar U-U\|_F^2}{n}
=\sum_a\frac{\|\bar z_a-z_a\|_2^2}{ng_a}
\le e_U^2,
\qquad e_{z,a}\le\sqrt{g_a}e_U\le Xe_U.
\tag{11}
\]

Taking upper norm derivatives in `(10)`, using `(7)`, and using
`(sum_a g_a c_a^2)^{1/2}≤XC` yields

\[
D^+e_U\le XC\,[Ke_w+L_sK^2BXe_U+B(1+L_sK)\varepsilon].
\]

Similarly the readout equations give

\[
D^+e_w\le C(KXe_U+\varepsilon).
\]

Consequently, with

\[
L=KX+L_sK^2BX^2,\qquad H=1+XB(1+L_sK),
\]

\[
D^+E\le C(t)[LE+H\varepsilon],\qquad E(0)=0.
\]

Multiplying the scalar integral inequality by the integrating factor, or iterating it, gives the explicit estimate

\[
\sup_{t\le T}
\left(\frac{\|\bar U-U\|_F}{\sqrt n}
+\frac{\|\bar w-w\|_2}{\sqrt n}\right)
\le H R(T)e^{LR(T)}\varepsilon.
\tag{12}
\]

No initial bound on `F(z_a)` is needed: the transformed difference starts at zero, and `(10)` bounds that difference directly. In particular `(12)` does not introduce an exponential-moment condition on Gaussian first-layer initializations.

For any training or test input `q=x/sqrt d` with `||q||_2≤X_test`, the forward bounds give

\[
|\bar f(t,x)-f(t,x)|
\le e_w+B\left(\varepsilon+KX_{\rm test}\frac{\|\bar U-U\|_F}{\sqrt n}\right)
\le(1+BKX_{\rm test})E+B\varepsilon.
\tag{13}
\]

Thus `(12)` controls predictions uniformly on every bounded input set. Its constants depend on the fixed data, horizon, initial readout bound and initialized operator bound, and not on width.

If the nonzero inputs are repetitions or sign reversals of pairwise orthogonal representatives, the same result applies after grouping. Tanh is odd and `s` is even, so a sample with `q_a=epsilon_a q_j`, `epsilon_a in {−1,1}`, contributes the common response with coefficient `epsilon_a c_a`. The grouped absolute coefficient sum is at most the original `C`. This covers the one-sample case and sign-repeated copies without changing the estimate.

## 4. What fails in the same transformation for correlated inputs

For general `G`, the exact first-preactivation equation is

\[
\dot z_a=\sum_bG_{ab}c_b\,s(z_b)\odot b_b.
\]

The componentwise transformation `(9)` gives

\[
\frac d{dt}F(z_a)
=\sum_bG_{ab}c_b\,\frac{s(z_b)}{s(z_a)}\odot b_b.
\tag{14}
\]

The diagonal contribution cancels its gate, but the cross-sample ratios remain. Their differences multiply the same uncontrolled `b_b`. Neither invertibility nor diagonalization of `G` removes them, because the gates act separately on the original sample preactivations. For example, replacing `z` by `G^{-1}z` when `G` is invertible moves the coupled nonlinear gates into the coordinate relation instead of eliminating them.

A local geometric computation makes the obstruction to a *common exact cancellation* precise. For a single neuron row `u in R^d`, define

\[
X_a(u)=s(u\cdot q_a)q_a.
\]

With the convention `[X_a,X_b]=DX_b X_a−DX_a X_b`, direct differentiation gives

\[
[X_a,X_b](u)
=2G_{ab}s(u\cdot q_a)s(u\cdot q_b)
\bigl[\tanh(u\cdot q_a)q_a-\tanh(u\cdot q_b)q_b\bigr].
\tag{15}
\]

In particular,

\[
[X_a,X_b](0)=0,\qquad
D[X_a,X_b](0)=2G_{ab}(q_aq_a^T-q_bq_b^T).
\tag{16}
\]

When `G_ab≠0` and `q_b≠±q_a`, the derivative in `(16)` is a nonzero symmetric matrix. A smooth coordinate map sending every `X_a` to a constant vector field would send every bracket to zero, contradicting `(15)--(16)`. Thus the simultaneous scalar flattening is unavailable for genuinely correlated distinct directions.

The obstruction also rules out a smooth common positive-definite metric in which every sample flow is an isometry. Indeed, if `L_{X_a}g=0` for every `a`, then commuting these identities gives `L_[X_a,X_b]g=0`. At a zero of the bracket this requires

\[
D[X_a,X_b](0)^Tg(0)+g(0)D[X_a,X_b](0)=0.
\]

For an eigenvector of the nonzero symmetric matrix in `(16)` with eigenvalue `lambda≠0`, this equation says `2 lambda v^Tg(0)v=0`, contradicting positive definiteness. The same argument applies to an invariant two-point energy with a smooth positive-definite quadratic expansion on the diagonal.

The coefficients in the actual network are **not arbitrary controls**: they are `c_a(t)b_ai(t)` and are linked to the same operator, readout and dense residual. Equations `(15)--(16)` consequently do not prove a network instability or a Legendre-oracle counterexample. They rule out two exact cancellation strategies that would work for arbitrary signed coefficients. A successful general proof could exploit the remaining network coupling, a metric involving additional variables, probabilistic structure, or a weaker continuity estimate.

## 5. Dense-history matrix accuracy at zero readout

This section verifies the separate matrix premise `(2)` at an explicit rate, for arbitrary fixed finite data and `w(0)=0`. Put `X=max ||q_a||_2`, and choose width-independent upper bounds `B,K` as in `(3)--(6)`. Only the dense flow is differentiated here.

If `rho_D(0)=0`, zero readout implies all labels are zero and both flows are stationary, so all errors vanish. Assume otherwise. The dense canonical tangent kernel has entries

\[
\mathcal K_{ab}
=\frac{k_a^Tk_b}{n}
+\frac{d_a^Td_b}{n}\frac{h_a^Th_b}{n}
+G_{ab}\frac{[s(z_a)\odot b_a]^T[s(z_b)\odot b_b]}{n}.
\]

Its entries have magnitude at most

\[
\kappa=1+B^2+X^2K^2B^2,
\]

so its spectral norm is at most `m kappa`. Because `dot r=−(2/m) mathcal K r`,

\[
\rho_{\rm D}(t)\ge\mu:=\rho_{\rm D}(0)e^{-2\kappa T}>0.
\tag{17}
\]

This follows by the differential inequality `dot rho≥−2 kappa rho`; positive semidefiniteness gives the complementary loss monotonicity. All constants are independent of width when the labels and initialized operator bound are fixed.

Primes below denote differentiation in the dense clock `xi`, after the prefix. Cauchy--Schwarz over the samples gives

\[
\frac{\|h_a'\|_2}{\sqrt n}\le H_1:=2X^2KB,
\qquad \|M'\|_{\rm op}\le2B,
\qquad \|w'\|_\infty\le2.
\tag{18}
\]

For example,
`z_a'=−(2/m)sum_b(r_b/rho)G_ab[s(z_b)⊙b_b]`, and
`sum_b |r_b/rho|/m≤1`, `|G_ab|≤X^2`, and `||b_b||_2/sqrt n≤KB` yield the first bound. The product rule then gives

\[
\frac{\|v_a'\|_2}{\sqrt n}
\le2B+KH_1=2B(1+X^2K^2),
\]

\[
\frac{\|d_a'\|_2}{\sqrt n}
\le D_2:=2+2L_sB^2(1+X^2K^2).
\tag{19}
\]

For `u=r/rho`, differentiation in physical time gives

\[
\dot u=\left(I-\frac{uu^T}{m}\right)\frac{\dot r}{\rho},
\qquad \|\dot u\|_2\le2\kappa\sqrt m.
\]

Combining `(17)` with `eta_a=u_a d_a` and Minkowski in the product sample/neuronal space yields

\[
\left(\frac1m\sum_a\frac{\|\eta_a'\|_2^2}{n}\right)^{1/2}
\le H_2:=\frac{2\kappa B}{\mu}+D_2.
\tag{20}
\]

The histories are continuous across the prefix endpoint: `h_a` starts from its prefix value, and `eta_a(1+)=0` because `w(0)=0`. Thus they are `H^1` on the complete history interval, with zero derivative on the prefix. Applying the paper's Hilbert-valued Legendre tail estimate separately to the two histories gives

\[
\left(\frac1m\sum_a\int\frac{\|(I-\Pi_P)h_a\|_2^2}{n}\,d\xi\right)^{1/2}
\le\frac{\tau_T\sqrt S\,H_1}{2\sqrt{P(P+1)}},
\]

\[
\left(\frac1m\sum_a\int\frac{\|(I-\Pi_P)\eta_a\|_2^2}{n}\,d\xi\right)^{1/2}
\le\frac{\tau_T\sqrt S\,H_2}{2\sqrt{P(P+1)}}.
\]

Orthogonality removes the cross terms between projected and residual histories, so `(5)` and the exact dense history identity imply

\[
A_P-M
=\frac2{nm}\sum_a\int
[(I-\Pi_P)\eta_a][(I-\Pi_P)h_a]^T\,d\xi.
\]

The Frobenius norm of a normalized rank-one matrix is the product of the two RMS norms. Cauchy--Schwarz in time and samples therefore proves

\[
\sup_{t\le T}\|A_P(t)-M(t)\|_F
\le\frac{\tau_T^2 S H_1H_2}{2P(P+1)}.
\tag{21}
\]

In particular the same bound holds in operator norm. All constants in `(21)` are independent of width. They can be large in `T`, notably through `mu^{-1}`; no uniform-in-time claim is made.

Without exactly zero initial readout, the zero backward prefix can create a jump at `xi=1`, so `(20)` on the physical part does not establish `H^1` on the full interval. One still obtains a width-uniform `P^{-1}` matrix bound by combining the forward tail with the residual-weighted history mass:

\[
\sup_{t\le T}\|A_P-M\|_F
\le\frac{\tau_T S B H_1}{\sqrt{P(P+1)}}.
\tag{22}
\]

No sharper nonzero-readout rate is claimed here.

## 6. What has and has not been resolved

For exactly zero readout and training directions that are pairwise orthogonal up to repetitions/sign reversals, `(12)--(13)` combined with `(21)` prove width-uniform `O_T(P^{-2})` outer-weight RMS and bounded-test-input prediction error for the external dense-history oracle with shared residuals and the original dense learning-speed clock.

For arbitrary finite correlated data, `(21)` proves the same matrix reconstruction rate, and `(7)` controls the backpassed top-response difference in terms of the first-preactivation error. The remaining step is to control the first-layer gate term `(8)` along the coupled paths. Sharing residuals has not removed it. The Lie-bracket argument rules out a direct common exact flattening or invariant-metric replacement, while leaving other proofs open. Neither failure of a generic Lipschitz estimate nor the geometric obstruction is presented as a counterexample to the actual Legendre reconstruction.

## 7. Verification of the stronger dense-gate oracle

Now allow any fixed number `L≥2` of hidden layers. The oracle receives

\[
r_a^{\rm D}(t),\quad \rho_{\rm D}(t),\quad
D_{\ell,a}^{\rm D}(t)=\operatorname{diag}s(z_{\ell,a}^{\rm D}(t)),
\qquad 1\le\ell\le L.
\]

Its forward responses are its own nonlinear responses. Its backward recursion is instead

\[
\widehat\delta_{L,a}=D_{L,a}^{\rm D}\widehat w,
\qquad
\widehat\delta_{\ell,a}
=D_{\ell,a}^{\rm D}\widehat W_{\ell+1}^T\widehat\delta_{\ell+1,a}.
\tag{23}
\]

The old moment equations record these responses multiplied by `r_D/rho_D` and the oracle's own forward responses, in the supplied clock `tau=1+int rho_D`. The outer weights follow the canonical equations with supplied residual and `(23)`.

This is an explicitly forced, generally non-gradient system: `(23)` need not be the derivative of its own forward map. That causes no defect-identity problem. Differentiating the moment reconstruction uses only its recorded forward/backward signals and the orthogonal projection algebra. It gives exactly

\[
\dot{\widehat W}_\ell
=-\frac2{nm}\sum_a r_a^{\rm D}\widehat\delta_{\ell,a}
\widehat h_{\ell-1,a}^T+E_\ell,
\]

\[
E_\ell=\frac{2\rho_{\rm D}}{nm}\sum_a
(b_{\ell,a}-b_{\ell,a}^*)(h_{\ell-1,a}-h_{\ell-1,a}^*)^T,
\quad b_{\ell,a}=(r_a^{\rm D}/\rho_{\rm D})\widehat\delta_{\ell,a}.
\tag{24}
\]

Stars are current projection values at the history endpoint. No derivative of a supplied gate occurs in `(24)` or in the estimates below.

Here are explicit bounds sufficient for continuation and the defect estimate. Put `S=int_0^T rho_D`, `tau_T=1+S`, `B=||w(0)||_2/sqrt n+2S`, and choose the bounds recursively from the output backwards:

\[
\beta_L=B,\qquad
K_\ell=\|W_\ell(0)\|_{\rm op}
+2\sqrt{\tau_T S}\,\beta_\ell,\qquad
\beta_{\ell-1}=K_\ell\beta_\ell
\quad(\ell=L,\ldots,2).
\tag{25}
\]

Readout integration gives its RMS bound. Projection contraction gives the middle operator bound, exactly as in `(6)`. The gate operator norms are at most one, so `(23)` supplies the next backward bound. This top-down recursion is not circular. The dense matrices and responses obey the same upper bounds, since their exact history integrals are bounded by `2S beta_l≤2sqrt(tau_T S) beta_l`.

For clarity, a direct version of the forward-variation recursion is as follows. Primes mean differentiation in the supplied clock, and put

\[
Z_\ell=\frac1m\sum_a\int_1^{\tau(T)}
\frac{\|h_{\ell,a}'\|_2^2}{n}\,d\xi.
\]

Then

\[
Z_1\le4X^4\beta_1^2S.
\tag{26}
\]

The endpoint projection map on degree `<P` has norm `P/sqrt(tau)`. Consequently the sample-averaged RMS of `b_l−b_l^*` is at most `(P+1)beta_l`. The projection-energy identity and the Legendre tail estimate in the paper therefore imply

\[
\int_1^{\tau(T)}\left\|E_\ell/\rho_{\rm D}\right\|_F^2d\xi
\le4(P+1)^2\beta_\ell^2
\frac{\tau_T^2Z_{\ell-1}}{4P(P+1)}
\le2\beta_\ell^2\tau_T^2Z_{\ell-1}.
\tag{27}
\]

The forward derivative is the sum of the canonical middle velocity times `h`, the defect velocity times `h`, and `W h'`. Using `|tanh'|≤1`, `||h||_2/sqrt n≤1`, and the squared norm bound by three times the sum of the three squared norms gives

\[
Z_\ell\le12\beta_\ell^2S
+(6\beta_\ell^2\tau_T^2+3K_\ell^2)Z_{\ell-1},
\qquad 2\le\ell\le L.
\tag{28}
\]

All constants are independent of `P,n`. Finally, the projection-energy identity applied to both histories, Cauchy--Schwarz, the mass bound on `b_l`, and the forward Legendre tail give

\[
\int_0^T\sum_{\ell=2}^L\|E_\ell\|_Fdt
\le\frac{\tau_T}{\sqrt{P(P+1)}}
\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}}.
\tag{29}
\]

This proof uses neither derivatives of the gates nor smoothness of the backward histories. At each fixed width and order, `(25)` bounds all responses and moment insertions, while `tau≥1` keeps the triangular moment equations regular. First-layer velocities are bounded in normalized Frobenius norm. These bounds prevent finite-time escape and give continuation through the prescribed horizon.

It remains to check stability, which is now straightforward for a substantive reason: the two systems use exactly the same backward gates. Compare states with the metric

\[
d=\frac{\|\Delta W_1\|_F}{\sqrt n}
+\sum_{\ell=2}^L\|\Delta W_\ell\|_F
+\frac{\|\Delta w\|_2}{\sqrt n}.
\tag{30}
\]

For each input, let `a_l` be forward RMS difference and `b_l` backward RMS difference. The exact estimates are

\[
a_1\le Xe_1,\qquad a_\ell\le K_\ell a_{\ell-1}+e_\ell,
\]

\[
b_L\le e_w,\qquad
b_\ell\le K_{\ell+1}b_{\ell+1}+\beta_{\ell+1}e_{\ell+1}.
\tag{31}
\]

Here `e_1,e_l,e_w` are the corresponding terms in `(30)`; all bounds hold uniformly over samples. The canonical block-velocity differences are bounded respectively by

\[
2\rho_{\rm D}Xb_1,\qquad
2\rho_{\rm D}(b_\ell+\beta_\ell a_{\ell-1}),\qquad
2\rho_{\rm D}a_L.
\]

Thus they sum to at most `L_F rho_D d`, for a constant `L_F` obtained from the finite recursions `(31)`. The dense path solves the same supplied-gate vector field with zero defect. Integrating the difference and iterating the scalar integral inequality gives

\[
\sup_{t\le T}d(t)
\le e^{L_FS}\int_0^T\sum_{\ell=2}^L\|E_\ell\|_Fdt
=O_T(P^{-1}),
\tag{32}
\]

uniformly in width. The usual forward recursion transfers this to predictions on every bounded input set. This confirms the supervisor's proposed oracle proof without assuming a Lipschitz estimate for changing nonlinear gates.

## 8. Exact remainder when the oracle's own gates are restored

Consider now a moment reconstruction using its own forward and backward responses but retaining the supplied dense residual and dense clock. The same bounds `(25)--(29)` still hold, since they use only gate operator norms and forward derivatives. Stability is the remaining issue.

At the current state, let `delta_l^self` denote the backward response using its own gates, and `delta_l^Dgate` the response using the supplied dense gates on the **same** weights. Define

\[
q_{L,a}=w,\qquad
q_{\ell,a}=W_{\ell+1}^T\delta_{\ell+1,a}^{\rm self}\quad(\ell<L),
\]

\[
\Gamma_{\ell,a}
=(D_{\ell,a}^{\rm self}-D_{\ell,a}^{\rm D})q_{\ell,a},
\qquad \gamma_{\ell,a}=\|\Gamma_{\ell,a}\|_2/\sqrt n.
\tag{33}
\]

Subtracting the two backward recursions gives the exact triangular identity

\[
\delta_{\ell,a}^{\rm self}-\delta_{\ell,a}^{\rm Dgate}
=\Gamma_{\ell,a}
+D_{\ell,a}^{\rm D}W_{\ell+1}^T
(\delta_{\ell+1,a}^{\rm self}-\delta_{\ell+1,a}^{\rm Dgate}).
\]

Therefore

\[
g_{\ell,a}:=\frac{\|\delta_{\ell,a}^{\rm self}
-\delta_{\ell,a}^{\rm Dgate}\|_2}{\sqrt n}
\le\sum_{j=\ell}^L
\left(\prod_{k=\ell+1}^{j}K_k\right)\gamma_{j,a}.
\tag{34}
\]

An empty product equals one. Gate restoration changes no readout velocity. Its first-layer and middle-layer velocity changes, summed in `(30)`, are bounded by

\[
\mathcal R_{\rm gate}(t)
=\frac2m\sum_a|r_a^{\rm D}(t)|
\left[Xg_{1,a}(t)+\sum_{\ell=2}^Lg_{\ell,a}(t)\right].
\tag{35}
\]

Combining the supplied-gate stability estimate with this additive forcing yields the precise comparison bound

\[
\sup_{t\le T}d(t)
\le e^{L_FS}\left[
\frac{\tau_T}{\sqrt{P(P+1)}}
\sum_{\ell=2}^L\beta_\ell\sqrt{SZ_{\ell-1}}
+\int_0^T\mathcal R_{\rm gate}(t)dt\right].
\tag{36}
\]

For tanh and uniformly bounded initial readout, its pointwise bound `(3)` makes the top remainder harmless:

\[
\gamma_{L,a}\le L_sB_\infty
\|z_{L,a}^{\rm self}-z_{L,a}^{\rm D}\|_2/\sqrt n.
\]

At lower layers, `(33)` multiplies the gate difference by a backpassed vector with only an RMS bound. This is exactly the unresolved product seen in `(8)`, now isolated at each depth. A bound of the form `mathcal R_gate≤rho_D L_gate d`, proved from additional structure rather than postulated, would close `(36)` by another scalar stability estimate. Equation `(36)` by itself does not supply that bound.

Restoring the oracle's own residual is a different, controlled error under these operator/readout bounds. At a fixed state, with frozen supplied gates, replacing `r_D` by `r_self` changes the total canonical velocity by at most

\[
2\left(\frac1m\sum_a|r_a^{\rm self}-r_a^{\rm D}|^2\right)^{1/2}
\left[X\beta_1+\sum_{\ell=2}^L\beta_\ell+1\right].
\tag{37}
\]

The forward recursion bounds the residual RMS difference by a constant times `(30)`, so `(37)` only changes the stability coefficient. If the clock is also restored, its own projection-defect bound must be used; the algebraic gate remainder `(33)--(35)` is unchanged. This distinguishes the genuinely unresolved gate product from residual feedback and from the independent approximation defect.
