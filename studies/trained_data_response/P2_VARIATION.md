# P2 variation: clock forcing, compact tangent families, and a conditional uniform remainder

Frozen independent author result, 2026-09-11. Input scope was the supervisor's self-contained prompt only, plus the required rigorous-math and conjecture-investigation process instructions. No scientific files, other attempts, experiments, or Git history were consulted. This document is an internally derived conditional result, not a promotion or an unconditional proof of the neural assertion.

## Result and remaining obligation

There is a route to the requested uniform first-order expansion that does not assume ambient Hilbert-space Fréchet differentiability, does not assume that the fixed Gaussian-limit operator acts boundedly on any (L^p) other than (L^2), and does not assume an (O(\varepsilon)) bound on normalized nonlinear state deviations.

The route uses the scalar clock

\[
 g(s)=\int_0^s\cosh^2 r\,dr=\frac{s}{2}+\frac{\sinh(2s)}4,
 \qquad \psi=g^{-1},\qquad \psi'(X)=\operatorname{sech}^2(\psi(X)).
 \tag{1}
\]

It proves the uniform nonlinear remainder conditional on **uniform square integrability of the actual perturbed clock forcing**. This is a tail condition on an explicit neural quantity, before any division by \(\varepsilon\). It simultaneously gives a uniform forcing bound, continuity of that forcing along the perturbed trajectories, and compactness of the reference linear-response family. The proof then tests Taylor expansion only on that compact family of linear responses.

The decisive unresolved neural estimate is (UI) below, uniformly over all contaminating Borel probability laws. Reference-only Gaussian tails and the already-known bounded reference propagator do not verify it.

## Exact contract

Let \(H_i=L^2(\Omega_i)\), with both underlying measures probability measures. The fixed operator \(A_0:H_1\to H_2\) has norm at most \(10\); every transpose below is its actual Hilbert-space adjoint. Let \(T\le40\), and take \(Y\ge1\), so that the reference law

\[
 \mu_*={1\over2}\delta_{(e_1,1)}+{1\over2}\delta_{(e_2,-1)}
\]

belongs to the specified input-label domain. For every Borel probability law \(\nu\) on \(S^1\times[-Y,Y]\), write \(\mu_{\varepsilon,\nu}=(1-\varepsilon)\mu_*+\varepsilon\nu\), \(0\le\varepsilon\le\varepsilon_0\le1\).

The physical state is \(\theta=(w,K,c)\in L^2(\Omega_1;\mathbb R^2)\times\mathrm{HS}(H_1,H_2)\times H_2\), initially \(w=(G_1,G_2)\) a standard Gaussian pair and \(K=c=0\). Put \(A=A_0+K\), \(q=\operatorname{sech}^2\), and, for an input \(u\),

\[
 z_{1,u}=w\cdot u,quad h_{1,u}=\tanh z_{1,u},\quad
 z_{2,u}=Ah_{1,u},\quad h_{2,u}=\tanh z_{2,u},
\]
\[
 f_u=\langle c,h_{2,u}\rangle,quad
 d_u=cq(z_{2,u}),\quad p_u=A^*d_u,quad r_{u,y}=f_u-y.
\]

The flow is the physical flow in the assignment, with factor \(-2\) in each law integral. For a rank-one operator, \(a\otimes b\) means \(v\mapsto a\langle b,v\rangle\), from \(H_1\) to \(H_2\).

For the conditional theorem, assume that strong physical solutions \(\theta_{\varepsilon,\nu}\) on \([0,T]\) exist, with common initialization. Here a strong solution is an absolutely continuous curve in the displayed physical Hilbert space satisfying the stated vector-field equation almost everywhere. The theorem applies to every family of such solutions satisfying (UI); it does not establish their existence from the supplied reference solution. Standard strong measurability of the feature and law integrals is understood. No uniqueness assumption about the perturbed physical flow is needed for the conclusion.

The target norms are the physical Hilbert norm and the uniform prediction norm over \(t\in[0,T]\) and \(u\in S^1\). The result concerns the infinite-width flow and its exact linear response. It does not exchange width and perturbation limits; the supplied fixed-law finite-width derivative convergence is only an identification input, if needed.

## The additional tail estimate

Define, on each actual trajectory,

\[
 Z_{\varepsilon,\nu;j,u}(t)
 =u_j\cosh^2(w_{\varepsilon,\nu;j}(t))
   q(w_{\varepsilon,\nu}(t)\cdot u)
   p_{\varepsilon,\nu;u}(t)
 \quad\text{on }\Omega_1.
 \tag{2}
\]

The factor \(u_j\) is included: at the other reference axis the corresponding clock forcing is zero. The single additional regularity hypothesis is

\[
 \lim_{R\to\infty}
 \sup_{\substack{0\le\varepsilon\le\varepsilon_0,\ \nu,\ 0\le t\le T\\
                  u\in S^1,\ j=1,2}}
 \int_{\Omega_1}|Z_{\varepsilon,\nu;j,u}(t)|^2
          \mathbf1_{\{|Z_{\varepsilon,\nu;j,u}(t)|>R\}}=0.
 \tag{UI}
\]

For \(\varepsilon=0\), the state is the given reference state and is independent of \(\nu\). (UI) asserts that the quantities in (2) exist as measurable functions and have uniformly integrable squares. In particular their \(L^2\) norms are uniformly bounded: choose \(R\) making the tail at most one and use \(\|Z\|_2^2\le R^2+1\).

A more familiar, stronger sufficient hypothesis is: for some \(\delta>0\),

\[
 \sup_{\varepsilon,\nu,t,u,j}
 \|Z_{\varepsilon,\nu;j,u}(t)\|_{2+\delta}<\infty.
 \tag{M}
\]

Indeed the tail in (UI) is at most \(R^{-\delta}\sup\|Z\|_{2+\delta}^{2+\delta}\). For example, if \(p=2+\delta\), uniform bounds on

\[
 \mathbb E e^{4p|w_j|}\quad\text{and}\quad
 \mathbb E|p_u|^{2p}
 \tag{3}
\]

imply (M), by \(q\le1\), \(\cosh^2 s\le e^{2|s|}\), and Cauchy–Schwarz. These are additional **joint reachable-state estimates**, not consequences of \(\|A_0\|_{2\to2}\le10\). No claim is made here that the neural flow satisfies (3).

## Conditional theorem

Under the stated strong-solution assumption and (UI), the clock state

\[
 x_{\varepsilon,\nu}=(X_{\varepsilon,\nu},K_{\varepsilon,\nu},c_{\varepsilon,\nu}),
 \qquad X_j=g(w_j),
 \tag{4}
\]

is absolutely continuous in

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)\times\mathrm{HS}(H_1,H_2)\times H_2.
\]

Let \(x_*=x_{0,\nu}\), and let \(R_\nu\) be the exact clock linear response to \(\nu-\mu_*\), initialized at zero. Then

\[
 \sup_\nu\sup_{t\le T}
 \|x_{\varepsilon,\nu}(t)-x_*(t)-\varepsilon R_\nu(t)\|_{\mathcal H}
       =o(\varepsilon).
 \tag{5}
\]

The physical response is

\[
 \dot w_{\nu,j}=q(w_{*,j})R_{\nu,X,j},\qquad
 \dot K_\nu=R_{\nu,K},\qquad \dot c_\nu=R_{\nu,c}.
 \tag{6}
\]

With \(\dot\theta_\nu\) defined by (6),

\[
 \sup_\nu\sup_{t\le T}
 \|\theta_{\varepsilon,\nu}(t)-\theta_*(t)-\varepsilon\dot\theta_\nu(t)\|
       =o(\varepsilon),
 \tag{7}
\]
\[
 \sup_\nu\sup_{t\le T}\sup_{u\in S^1}
 |f_{\varepsilon,\nu;u}(t)-f_{*;u}(t)-\varepsilon\dot f_{\nu;u}(t)|
       =o(\varepsilon).
 \tag{8}
\]

All small-o statements are uniform over the indicated Borel laws. Constants may depend on \(T,Y,A_0\), the common initialization through its clock \(L^2\) norm, and the uniform bound/modulus in (UI), but never on \(\nu\).

## Proof

### 1. Bounds available without the tail hypothesis

Since \(\|h_{1,u}\|_2,\|h_{2,u}\|_2\le1\),

\[
 |f_u|\le\|c\|_2,quad \|d_u\|_2\le\|c\|_2,quad
 \|p_u\|_2\le(10+\|K\|_{\mathrm{HS}})\|c\|_2.
\]

The \(c\) equation gives \(\|c(t)\|_2\le2\int_0^t(\|c(s)\|_2+Y)\,ds\), hence

\[
 \|c(t)\|_2\le Y(e^{2t}-1).
 \tag{9}
\]

Its pointwise integral formula, using \(|h_{2,u}|\le1\), gives the same bound for \(\|c(t)\|_\infty\). This pointwise bound holds for every law, not just the reference law. Set \(M=Y(e^{2T}-1)\) and \(B=2T(M+Y)M\). The \(K\) equation yields

\[
 \sup_{t\le T}\|K(t)\|_{\mathrm{HS}}\le B,
 \qquad
 \sup_{t\le T}\|w(t)-w(0)\|_2
 \le2T(M+Y)(10+B)M.
 \tag{10}
\]

These estimates need neither a loss-energy identity nor an \(L^p\) bound for \(A_0\). Their constants are large, but finite for the required horizon.

### 2. Exact clock equation

For the reference axes, \(g'(w_j)q(w_j)=1\), so the transformed reference field is

\[
 F_0(x)_{X,j}=-r_jp_j,
 \quad F_0(x)_K=-\sum_{j=1}^2r_jd_j\otimes h_{1,j},
 \quad F_0(x)_c=-\sum_{j=1}^2r_jh_{2,j}.
 \tag{11}
\]

Here \(j\) denotes input \(e_j\), with label \(1\) for \(j=1\) and \(-1\) for \(j=2\); in evaluating the field from \(x\), use \(w_j=\psi(X_j)\).

For an arbitrary law define

\[
 Q_\nu(x)_{X,j}=-2\int r_{u,y}Z_{j,u}(x)\,d\nu(u,y),
\]
\[
 Q_\nu(x)_K=-2\int r_{u,y}d_u\otimes h_{1,u}\,d\nu,
 \qquad Q_\nu(x)_c=-2\int r_{u,y}h_{2,u}\,d\nu,
\]

and \(B_\nu(x)=Q_\nu(x)-F_0(x)\). The exact equation is

\[
 x_{\varepsilon,\nu}'=F_0(x_{\varepsilon,\nu})
                         +\varepsilon B_\nu(x_{\varepsilon,\nu}).
 \tag{12}
\]

The clock is legitimate under (UI). A physical strong solution has, after choosing representatives, pointwise absolutely continuous \(w_j(t,\omega)\) for almost every \(\omega\). Apply the scalar chain rule to \(g(w_j)\). Equations (9)–(10) and (UI) bound the resulting right-hand side of (12) in \(L^1([0,T];H_1)\). Also \(g(G_j)\in L^2\), because Gaussian random variables have finite exponential moments \(\mathbb E e^{a|G_j|}\) for every finite \(a\). The pointwise integral identity consequently identifies \(X_j\) with an absolutely continuous \(H_1\)-valued curve. This argument does not assume beforehand that applying the unbounded map \(g\) preserves the physical \(L^2\) state space.

### 3. Lipschitz comparison for the reference field

On sets with bounded \(\|K\|_{\mathrm{HS}}\), \(\|c\|_2\), and with **at least one of the two compared \(c\) endpoints bounded in \(L^\infty\)**, there is a uniform constant \(L\) such that

\[
 \|F_0(x)-F_0(\widetilde x)\|_{\mathcal H}
       \le L\|x-\widetilde x\|_{\mathcal H}.
 \tag{13}
\]

To check this carefully, \(\psi\) is 1-Lipschitz, so

\[
 \|\Delta h_{1,u}\|_2\le\|\Delta X\|_2,
 \qquad
 \|\Delta z_{2,u}\|_2\le(10+B)\|\Delta X\|_2+\|\Delta K\|_{\mathrm{HS}}.
\]

If \(\|c\|_\infty\le M\), factor the backward difference as

\[
 cq(z_2)-\widetilde c q(\widetilde z_2)
    =(c-\widetilde c)q(\widetilde z_2)
      +c\{q(z_2)-q(\widetilde z_2)\}.
\]

Because \(|q'|\le2\), its \(L^2\) norm is at most
\(\|\Delta c\|_2+2M\|\Delta z_2\|_2\). Further,

\[
 |\Delta f_u|\le\|\Delta c\|_2+M\|\Delta z_{2,u}\|_2,
\]
\[
 \|\Delta p_u\|_2
 \le(10+B)\|\Delta d_u\|_2+C\|\Delta K\|_{\mathrm{HS}}.
\]

In the scalar prediction estimate, a bound on the appropriate \(c\) endpoint in \(L^2\) would already suffice. Substitution in (11), with
\(\|a\otimes b\|_{\mathrm{HS}}=\|a\|_2\|b\|_2\), proves (13). The clock \(X\) component contains no product \(p_j\Delta X_j\).

By (UI), (9), and (10), \(B_\nu(x_{\varepsilon,\nu})\) is uniformly bounded in \(\mathcal H\). Comparison of (12) with the reference equation, followed by the integral inequality \(v(t)\le a+L\int_0^tv(s)ds\Rightarrow v(t)\le ae^{Lt}\), now gives

\[
 \sup_{\nu,t\le T}\|x_{\varepsilon,\nu}(t)-x_*(t)\|_{\mathcal H}
       \le C_T\varepsilon.
 \tag{14}
\]

This is a derived estimate, not an extra reachable-deviation assumption.

### 4. Tail control gives uniform continuity of the contamination source

The relevant consequence of (UI) is

\[
 \sup_{\nu,t\le T,u\in S^1,j}
 \|Z_j(x_{\varepsilon,\nu}(t),u)-Z_j(x_*(t),u)\|_2\longrightarrow0.
 \tag{15}
\]

Here is the complete compactness argument. If (15) failed, choose a sequence \(\varepsilon_n\to0\), laws \(\nu_n\), times \(t_n\), and inputs \(u_n\) along which its left-hand difference stays bounded away from zero. Pass to a subsequence with \(t_n\to t\) and \(u_n\to u\). By (14) and reference continuity,
\(x_{\varepsilon_n,\nu_n}(t_n)\to x_*(t)\) in \(\mathcal H\).

The feature fields converge strongly in \(L^2\): for the first layer use the Lipschitz property of \(\psi\) and
\(\|(u_n-u)\cdot w_*\|_2\le|u_n-u|\|w_*\|_2\); then use boundedness of \(A_0\), convergence of \(K\), and the backward difference estimate in Step 3. In particular \(p_{u_n}(x_n)\to p_u(x_*)\) in \(L^2\). The scalar functions
\(u_{n,j}\cosh^2(\psi(X_{n,j}))q(\psi(X_n)\cdot u_n)\) converge in measure to their reference limits, because their finite-dimensional defining functions are continuous. Their products with \(p_{u_n}(x_n)\) therefore converge in measure to \(Z_j(x_*(t),u)\).

Uniformly integrable squares turn this convergence in measure into \(L^2\) convergence. Explicitly, for every \(\eta>0\), split the square of the difference into the event on which it is at most \(\eta^2\), whose integral is at most \(\eta^2\), and its complement, whose probability tends to zero. Uniform integrability makes the integral on the complement small uniformly; then send \(\eta\to0\). This also applies to the reference sequence \((t_n,u_n)\), because \(\varepsilon=0\) is included in (UI). The triangle inequality contradicts the selected failure of (15).

The remaining components of \(Q_\nu\) have ordinary strong continuity by the estimates in Step 3. Residuals are uniformly bounded and their differences tend to zero uniformly by (14). Integration against any probability law cannot exceed the supremum over its inputs. Thus

\[
 \sup_{\nu,t\le T}
 \|B_\nu(x_{\varepsilon,\nu}(t))-B_\nu(x_*(t))\|_{\mathcal H}
       \longrightarrow0.
 \tag{16}
\]

### 5. The reference response family is compact

The same reasoning, with \(\varepsilon=0\), proves joint strong continuity of

\[
 (t,u,y)\longmapsto Q_{\delta_{(u,y)}}(x_*(t))
\]

on the compact set \([0,T]\times S^1\times[-Y,Y]\). Equivalently the map

\[
 (u,y)\longmapsto b_{u,y}(\cdot)
 :=Q_{\delta_{(u,y)}}(x_*(\cdot))-F_0(x_*(\cdot))
 \tag{17}
\]

is continuous into \(C([0,T];\mathcal H)\), and its image is compact. Every forcing
\(b_\nu(t)=B_\nu(x_*(t))\) is the Bochner average \(\int b_{u,y}\,d\nu\). The set of such averages is contained in the closed convex hull of the compact image in (17), and that closed convex hull is compact. To verify the last fact, cover the image by finitely many balls of radius \(\eta\); every convex combination is within \(\eta\) of the convex hull of their finitely many centers. That latter hull is compact in a finite-dimensional space. This proves total boundedness, and completeness supplies compactness after closure.

Let \(L(t)\) be the bounded clock linearization in Step 6. Its homogeneous propagator is the one in the prompt, or can be obtained from the integral equation for this bounded, strongly continuous family. With \(\sup_{0\le s\le t\le T}\|U(t,s)\|\le M_T\),

\[
 R_\nu(t)=\int_0^tU(t,s)b_\nu(s)\,ds,
 \qquad \|R_\nu\|_{C_t\mathcal H}\le M_TT\|b_\nu\|_{C_t\mathcal H}.
 \tag{18}
\]

This is a bounded linear map between the indicated continuous-curve spaces. It maps the relatively compact forcing family to a relatively compact family of response curves. Consequently

\[
 \{R_\nu(t):\nu\text{ a Borel probability law},\ 0\le t\le T\}
 \quad\text{has compact closure in }\mathcal H.
 \tag{19}
\]

Evaluation over a compact set of continuous curves and compact time preserves compactness. Compactness is stronger than the supplied response norm bound and is the feature needed below.

### 6. Taylor expansion only along compact direction sets

The elementary Nemytskii fact used here is the following. If \(a\) is any measurable base field and \(v\) varies in a relatively compact subset of \(L^2\), and a scalar (or finite-dimensional vector) function \(N\) has bounded Lipschitz first derivative, then

\[
 \sup_{a,v}
 \left\|\frac{N(a+\varepsilon v)-N(a)}{\varepsilon}-N'(a)v\right\|_2
       \longrightarrow0,
 \tag{20}
\]

where the supremum in \(a\) ranges over any bases for which the expressions make sense. To prove this, on \(|v|\le R\) the pointwise remainder divided by \(\varepsilon\) is at most \(C\varepsilon R|v|\). On \(|v|>R\) it is at most \(C|v|\). Compact subsets of \(L^2\) have uniformly integrable squares: approximate them by a finite \(L^2\) net and use the absolute continuity of finitely many integrals. First choose \(R\) to control the tail, then \(\varepsilon\) to control the bounded part. This proves (20), without any ambient Fréchet assertion.

For completeness the actual linearization is explicit. At a reference clock state take a direction \(v=(V,J,b)\in\mathcal H\), and define

\[
 \eta w_j=q(w_j)V_j,
 \qquad \eta h_{1,u}=q(z_{1,u})\,u\cdot\eta w,
\]
\[
 \eta z_{2,u}=A\eta h_{1,u}+Jh_{1,u},\qquad
 \eta h_{2,u}=q(z_{2,u})\eta z_{2,u},
\]
\[
 \eta f_u=\langle b,h_{2,u}\rangle+\langle c,\eta h_{2,u}\rangle,
\]
\[
 \eta d_u=bq(z_{2,u})+cq'(z_{2,u})\eta z_{2,u},
 \qquad \eta p_u=A^*\eta d_u+J^*d_u.
 \tag{21}
\]

Then

\[
 (Lv)_{X,j}=-(\eta f_j)p_j-r_j\eta p_j,
\]
\[
 (Lv)_K=-\sum_j\left[(\eta f_j)d_j\otimes h_{1,j}
       +r_j\eta d_j\otimes h_{1,j}
       +r_jd_j\otimes\eta h_{1,j}\right],
\]
\[
 (Lv)_c=-\sum_j\left[(\eta f_j)h_{2,j}+r_j\eta h_{2,j}\right].
 \tag{22}
\]

All maps in (21)–(22) are bounded on \(\mathcal H\), uniformly over reference times: the sole multiplication by an unconstrained \(\eta z_2\) has coefficient \(cq'(z_2)\in L^\infty\); no \(p_jV_j\) occurs. Strong continuity of \(L(t)\) follows from reference continuity, uniform boundedness of these multipliers, and dominated convergence after applying them to a fixed \(L^2\) direction. A uniformly bounded strongly continuous operator family has its unique integral-equation propagator, obtained by the convergent iterated-integral series, whose norm is at most \(e^{T\sup\|L(t)\|}\). Thus (18) is also justified without importing an unverified propagator theorem.

Apply (20) to \(\psi\), to \(X\mapsto\tanh(u\cdot\psi(X))\), and to \(\tanh z_2\) and \(q(z_2)\). The first two functions have bounded Lipschitz first derivatives uniformly over \(u\in S^1\): \(|\psi'|\le1\), \(\psi''=q'(\psi)q(\psi)\) is bounded, and \(u\) has unit norm. Continuous bounded linear maps preserve relative compactness, as do the reference-time dependent maps here, since \(K(t)\) is norm continuous. Bilinear terms such as \(J\Delta h_1\) have the expected \(O(\varepsilon^2)\) bound.

There is one potentially problematic product in \(d_u\). After dividing its remainder by \(\varepsilon\), the cross term is

\[
 b\{q(z_{2,u}^{\mathrm{new}})-q(z_{2,u})\}.
 \tag{23}
\]

The bracket is bounded and tends to zero in measure uniformly, since its \(L^2\) norm is \(O(\varepsilon)\). The \(b\) directions lie in a compact subset of \(L^2\), so their squares are uniformly integrable. The same small-event split as in Step 4 makes (23) tend to zero in \(L^2\), uniformly. The other activation Taylor residual in \(d_u\) is multiplied by reference \(c\), which is bounded in \(L^\infty\). Products in \(f_u\) are scalar pairings; products in \(K\) are rank-one Hilbert–Schmidt products, so Cauchy–Schwarz controls them without multiplying two arbitrary \(L^2\) fields pointwise.

It follows that for every relatively compact direction set \(\mathcal C\subset\mathcal H\),

\[
 \sup_{t\le T,v\in\mathcal C}
 \|F_0(x_*(t)+\varepsilon v)-F_0(x_*(t))-\varepsilon L(t)v\|_{\mathcal H}
       =o(\varepsilon).
 \tag{24}
\]

The same proof gives the corresponding Taylor expansion of the prediction, uniformly over \(u\in S^1\). Notice that (24) is never asserted for the entire bounded \(L^2\) ball.

### 7. Compare the actual curve with the linear-response curve

Set \(\widetilde x_{\varepsilon,\nu}=x_*+\varepsilon R_\nu\). By (19) and (24),

\[
 \rho_{\varepsilon,\nu}(t)
 :=F_0(\widetilde x_{\varepsilon,\nu}(t))-F_0(x_*(t))
      -\varepsilon L(t)R_\nu(t)
\]

satisfies \(\sup_{\nu,t}\|\rho_{\varepsilon,\nu}(t)\|=o(\varepsilon)\). Subtract the response equation from (12), with \(e=x_{\varepsilon,\nu}-\widetilde x_{\varepsilon,\nu}\):

\[
 e'=F_0(x_{\varepsilon,\nu})-F_0(\widetilde x_{\varepsilon,\nu})
   +\varepsilon\{B_\nu(x_{\varepsilon,\nu})-B_\nu(x_*)\}
   +\rho_{\varepsilon,\nu},\qquad e(0)=0.
 \tag{25}
\]

In applying (13), the actual curve has the uniform \(c\) pointwise bound (9). The approximate curve need only have bounded \(K\) and \(c\) in their Hilbert norms; it is not assumed to have a pointwise bounded response \(R_{\nu,c}\). Thus the comparison does not reintroduce an unproved \(L^\infty\) tangent bound. Equations (13), (16), and (25), followed by the integral inequality used in Step 3, prove (5).

Finally \(w=\psi(X)\) is Lipschitz, and (20) on the compact response directions gives (6)–(7). The prediction is Lipschitz in the clock state on the relevant bounded sets, and its compact-direction Taylor formula from Step 6 gives (8). The linear system (21)–(22), forced by \(B_\nu(x_*)\), is exactly the differentiated clock equation, so uniqueness identifies it with the supplied exact clock response whenever that response uses this clock (or its fixed affine recentering). If the supplied clock is represented differently, the corresponding coordinate identification must be verified separately; this proof already defines its own exact response explicitly.

## Hostile checks and claim status

1. **Why the clock matters.** In physical coordinates, differentiating the first-layer backward factor creates \(q'(w_j)p_j\Delta w_j\), which need not be in \(L^2\). Equation (11) removes this multiplier from the reference field exactly. An arbitrary-input component remains multiplied by \(\varepsilon\), but its clock force must still satisfy (UI).

2. **Why mere bounded response is insufficient.** A bounded family in \(L^2\) need not have uniformly integrable squares, and bounded linear-response curves do not by themselves justify (24). Step 5 derives the required compactness from continuity of the atom-forcing family on the compact input-label set. Its continuity uses the tail condition, not merely the known response bound.

3. **Why bare force boundedness is insufficient for this proof.** Replacing (UI) by \(\sup\|Z\|_2<\infty\) proves (14), but does not prove (15). Concentrating products can converge in measure while retaining their \(L^2\) mass. Such concentration would leave an \(O(\varepsilon)\), rather than \(o(\varepsilon)\), contamination-source error in (25).

4. **The missing estimate is not supplied by \(L^2\) operator bounds.** Even if \(w\) is exactly Gaussian, \(p\in L^2\) need not imply \(\cosh^2(w_j)q(w\cdot u)p\in L^2\). For an elementary diagnostic, take independent standard Gaussians \(G,H\), choose \(u=(1,1)/\sqrt2\), and take \(p(G)=e^{G^2/4}/(1+|G|)\). Then \(p\in L^2\), since its squared Gaussian-weighted density is proportional to \((1+|G|)^{-2}\). On \(|H|\le1\), \(G\to+\infty\), the extra squared clock factor grows at least as a positive constant times \(e^{(4-2\sqrt2)G}\); the weighted product is not in \(L^2\). This is a functional-analytic check on a proposed inference, not a counterexample using the prescribed Gaussian-limit action or its reachable neural states.

5. **Reference tails do not propagate automatically.** The prompt's Gaussian reference backward tails may help verify the \(\varepsilon=0\) portion of (UI), together with appropriate reference-clock moments. They give no stated uniform tail estimate on \(Z_{\varepsilon,\nu}\) for arbitrary contaminating laws. Correlations between the fixed action, trained activations, and backward vectors must be retained when proving that estimate.

6. **No width-limit interchange.** The proof never infers nonlinear differentiability from convergence of finite-width right derivatives. A finite-width route to (UI) would need a width-uniform tail estimate, compatibility of the clock states with the width limit, and an existence/identification argument for the perturbed flow. Those are additional obligations.

7. **No hidden differentiability assumption.** (UI) is a tail bound on unnormalized, explicit forcing fields. The first-order bound (14), compactness (19), and remainder (5) are derived. The theorem does assume existence of perturbed strong solutions, separately from the differentiability conclusion.

Status: the conditional theorem and its reduction are proved in this independent derivation; the original uniform nonlinear theorem remains open under the supplied assumptions alone. The route should be classified as **conditional, with a concrete reachable-tail bottleneck**. Its next mathematical obligation is to prove (UI), or a sufficient estimate such as (M), for all \(0\le\varepsilon\le\varepsilon_0\), all Borel \(\nu\), and \(t\le40\), while also supplying the perturbed strong-solution family if it is not already available.
