# Independent alternative route: protected rows, continuum injectivity, and a nonlinear oracle inequality

Status: first-round theoretical attempt, frozen for coordinator comparison. No milestone claim, promotion claim, experiment, or Git operation is made here. The endpoint completeness argument below is new mathematics derived from the admitted sources. The nonlinear oracle, sampling, and stopping statements have complete analytic proofs conditional on the explicitly identified Borel-law episode interface in Section 8. That interface is not silently imported from C.4.9's one-atom theorem.

## Scope and sources actually read

Scientific inputs read completely:

* `studies/nonlinear_selection_generalization/README.md`, the frozen whole-circle Fourier class and model contract.
* `docs/NOTATION.md`.
* `docs/global_nonlinear.md`, complete C.4.9, lines 12994 through the end of that section. In particular its protected-row estimate, raw gradient formula, endpoint bounds, source-tube proof, reached-curve differentiation, residual identity, and finite-GF proof were read, not only its theorem statement.
* `docs/global_nonlinear.md`, complete C.4.1, lines 3982–4207, for the one-reference transport inequality and its finite normalized version.

Process sources read: the complete `solve-math-rigorously` and `investigate-conjectures` skills, and the latter's research-contract, proof-search-orchestration, evidence-ledger, and adversarial-audit references. The supervisor's explicit scope replaces ordinary author startup. No other study, route, chat, web scientific source, maintained API, or experiment was consulted. The supervisor supplied the locator for III.F in `docs/special_data_limits.md`; that section was not read or used as an independently checked dependency in this attempt.

The contract remains the original two-hidden-layer tanh GF, Gaussian stored variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, unhalved square loss, full first rows, original fixed-mixture initialization, and actual reused action/adjoint. The proposed approximation does not replace the trained flow. It bounds that flow using an endpoint comparison space whose features and coefficients are determined without the later target trajectory.

## 1. Main result of this route

Finite-list endpoint positivity can be strengthened in a different way from a uniform kernel lower bound: the endpoint middle-gradient transform is injective on **all finite odd signed measures on the circle**. Its proof uses protected extreme first rows and the nonzero odd Fourier multipliers of `sign(cos alpha)`.

This has three useful consequences.

1. The constrained endpoint prediction space is dense in odd `L2` for every admitted whole-circle input density, even though its kernel has no positive uniform spectral gap.
2. Every nonzero odd endpoint residual produces a nonzero projected **middle** force. Thus hidden-block activity does not need to be inferred from readout activity.
3. Finite matrices built from a predetermined dense set of circle queries give an explicit target-dependent oracle. Along a source-controlled nonlinear episode, the exact moving-feature residual obeys that oracle plus an `O(tau^2)` error. This error is derived from motion of the actual feature map, rather than omitted.

The decisive unresolved implication for a complete milestone theorem is the Borel-law extension and capture interface stated in Section 8. The endpoint completeness proof and the conditional statistical analysis do not resolve that interface by themselves.

## 2. Endpoint notation and parity

Write `u_alpha=(cos alpha,sin alpha)`, let `rho=dalpha/(2 pi)`, and use the raw Hilbert space `E` and endpoint `theta_dagger` of C.4.9. All unlabeled gradients and fields in Sections 2–4 are evaluated at that endpoint. Put

\[
 H(u)=\tanh(w_\dagger\cdot u),\quad
 Z(u)=A_\dagger H(u),\quad
 \delta(u)=c_\dagger\operatorname{sech}^2 Z(u),
\]
\[
 G=(g(e_1),g(e_2)),\quad M=G^*G,\quad
 \Pi=I-GM^{-1}G^*,\quad d(u)=\Pi g(u).
 \tag{A1}
\]

The endpoint anchor Gram is positive by C.4.9.B.2. The readout is nonzero because the first anchor prediction is one. C.4.9 supplies bounded `c_dagger`, bounded action, finite `w_dagger` moments needed below, and continuous raw gradients on the circle.

Bias-free odd activations give `H(-u)=-H(u)`, `Z(-u)=-Z(u)`, `delta(-u)=delta(u)`, and `g(-u)=-g(u)`. Thus `d` and every predictor are odd. For a density `p`, write

\[
 p_s(u)=\tfrac12(p(u)+p(-u)),\qquad d\nu_s=p_s\,d\rho.
\]

An odd squared residual and its population force depend on `p` only through `p_s`. The density still satisfies `1/2<=p_s<=2` and the same Lipschitz bound. Let `H_o=L^2_odd(nu_s)`; its norm equals the actual test-error norm on odd functions. Define

\[
 T h=\int h(u)d(u)\,d\nu_s(u),\qquad
 (T^*v)(u)=\langle d(u),v\rangle_E,\qquad K=T^*T.
 \tag{A2}
\]

These bounded maps have types `T:H_o->E`, `T*:E->H_o`, and `K:H_o->H_o`. `K` is not assumed coercive.

## 3. New key estimate: injectivity on odd signed measures

**Lemma 1.** If a finite odd signed Borel measure `mu` on `S1` satisfies

\[
 \int \delta(u)\otimes H(u)\,d\mu(u)=0
 \quad\text{in }HS(H_1,H_2),
 \tag{A3}
\]

then `mu=0`.

The measure is odd in the sense that its pushforward under `u->-u` is `-mu`. This includes absolutely continuous odd measures and antisymmetrized atoms.

**Proof.** The integrand in (A3) is continuous into the Hilbert–Schmidt space and bounded there. Its integral identifies, by Fubini, with the `L2(Omega_2 x Omega_1)` kernel

\[
 (\omega_2,\omega_1)\longmapsto
 c_\dagger(\omega_2)\int
  \operatorname{sech}^2 Z(u,\omega_2)
  \tanh(w_\dagger(\omega_1)\cdot u)\,d\mu(u).
 \tag{A4}
\]

A jointly measurable representative is available from continuity into `L2` and finite simple approximations on the circle. Fubini also gives, for almost every upper coordinate, finite `Z(u,omega_2)` for `|mu|`-almost every `u`, and the even-gate identity at `|mu|`-almost every pair `u,-u`.

Choose an upper coordinate outside these null sets with `c_dagger(omega_2)!=0`; such coordinates have positive probability. Its function

\[
 a(u)=\operatorname{sech}^2 Z(u,\omega_2)
\]

is bounded, strictly positive `|mu|`-almost everywhere, and even. Hence `lambda=a mu` is a finite odd signed measure. Equation (A4) says

\[
 \int\tanh(w_\dagger(\omega_1)\cdot u)\,d\lambda(u)=0
 \quad\text{for almost every }\omega_1.
 \tag{A5}
\]

C.4.9.B.2 provides the following protected-row fact. For each vector `v` with two nonzero coordinates, and all sufficiently large `r`, there is a positive-probability event on which

\[
 |g-rv|_\infty\le1,\qquad N\le r^2,\qquad
 |w_\dagger-g|_\infty\le C_v r^2e^{-c_vr}.
 \tag{A6}
\]

Its proof uses the Gaussian box probability, the subGaussian tail of `N`, and the exact inverse-gate primitive; it does not require independence of `N` and `g`. Intersect (A6) with the full-probability set of (A5), and choose one row from the nonempty intersection for each sufficiently large integer `r`.

For every `u` with `v.u!=0`, the chosen row satisfies

\[
 \tanh(w_\dagger\cdot u)\longrightarrow\operatorname{sign}(v\cdot u).
\]

A finite signed measure has at most countably many atoms. For almost every direction of `v`, neither point perpendicular to `v` is an atom of `|lambda|`. Bounded convergence with respect to `|lambda|` therefore passes (A5) to

\[
 \int\operatorname{sign}(v\cdot u)\,d\lambda(u)=0
 \quad\text{for almost every direction of }v.
 \tag{A7}
\]

The two excluded coordinate directions have zero arc measure and do not matter here. This is an integral limit over a fixed signed measure, not an assertion about a random supremum over all queries.

For completeness the Fourier step is explicit. The complex Fourier coefficients of `s(alpha)=sign(cos alpha)` are zero at even indices and, at positive odd `j=2k+1`, are

\[
 \widehat s(j)=\widehat s(-j)
       ={2(-1)^k\over\pi(2k+1)}\ne0.
 \tag{A8}
\]

This follows by integrating `cos(j alpha)` over the two half-circles on which the sign is constant. Fubini applied to the bounded function in (A7) gives `widehat s(j) widehat lambda(j)=0`. All odd coefficients of `lambda` consequently vanish. Its even coefficients, including its mass, vanish by oddness. Hence every Fourier coefficient vanishes.

Here is the needed uniqueness argument without a density assumption on `lambda`. The Fejer kernels

\[
 F_n(\alpha)={1\over n}\left|\sum_{k=0}^{n-1}e^{ik\alpha}\right|^2
\]

are nonnegative, integrate to one against `rho`, and have integrals outside any fixed neighborhood of zero tending to zero, because `F_n(alpha)<=1/[n sin^2(alpha/2)]` there. Uniform continuity then proves `F_n*h->h` uniformly for every continuous periodic `h`. Every `F_n*h` is a trigonometric polynomial, whose integral against `lambda` is zero. Passing the uniform limit gives zero against every continuous `h`, which determines a finite signed Borel measure on the compact circle. Thus `lambda=0`. Finally strict positivity of `a` implies `mu=0`: on each set `{a>=1/k}`, multiplication by `1/a` recovers `mu`, and these sets exhaust its total variation up to a null set. This proves the lemma. ∎

**Corollary 2 (projected continuum injectivity, including the middle block).** If `h in H_o` and the middle block of `T h` is zero, then `h=0`.

**Proof.** Put

\[
 b=\int h(u)g(u)\,d\nu_s(u),\qquad \beta=M^{-1}G^*b.
\]

Since `Th=b-G beta`, its middle block is (A3) for the finite odd measure

\[
 \mu=h\nu_s-\sum_{a=1}^2\beta_a
                {\delta_{e_a}-\delta_{-e_a}\over2}.
 \tag{A9}
\]

Lemma 1 gives `mu=0`. Its absolutely continuous and atomic parts must vanish separately. Since `p_s>=1/2`, this implies `h=0` in `H_o` and `beta=0`. ∎

In particular `T` and `K` are injective. This statement does **not** give `K>=lambda I` for a positive `lambda` on the infinite-dimensional space. Indeed the continuous bounded kernel makes `K` compact, so such a lower bound would contradict infinite dimensionality: uniform finite-grid approximations of its kernel give finite-rank operator approximations, while the identity cannot have compact image of the unit ball.

## 4. An explicit finite-section approximation oracle

Choose once a dense sequence `u_1,u_2,...` on one open semicircle, excluding the two anchor lines, with distinct nonantipodal entries. For example rational angles in that semicircle can be enumerated in a fixed order. This choice is independent of every target and every trained path. Let

\[
 k_j=T^*d(u_j),\quad
 S_J=(\langle k_i,k_j\rangle_{H_o})_{i,j\le J},\quad
 D_J=(\langle d(u_i),d(u_j)\rangle_E)_{i,j\le J}.
 \tag{A10}
\]

Both matrices are defined entirely by the reference endpoint and the input density. `D_J` is positive: adding the two anchors and using C.4.9.B.2 gives independence of the projected finite list. Also `S_J` is positive. To see this, if `v=sum_j a_jd(u_j)` and `T*v=0`, continuity makes `<d(u),v>=0` on the whole circle. Evaluation at the listed points gives `||v||^2=0`, and finite-list independence gives `a=0`.

For a specified odd function `h`, set

\[
 b_J(h)=(\langle h,k_j\rangle)_{j\le J},\quad
 a_J(h)=S_J^{-1}b_J(h),\quad
 v_J(h)=\sum_{j\le J}a_{J,j}(h)d(u_j),
\]
\[
 E_J(h)^2=\|h\|_{H_o}^2-b_J(h)^TS_J^{-1}b_J(h),\quad
 B_J(h)^2=a_J(h)^TD_Ja_J(h).
 \tag{A11}
\]

Then `E_J(h)=||h-T*v_J(h)||` and `B_J(h)=||v_J(h)||`. These are ordinary finite Gram calculations; no inverse continuum operator or inaccessible trajectory coefficient is used.

Moreover `E_J(h)->0` for every `h in H_o`. Indeed a function orthogonal to every `k_j` satisfies `(Kh)(u_j)=0`; continuity and density imply `Kh=0`. Pairing with `h` gives `Th=0`, and Corollary 2 gives `h=0`. The closure of the increasing finite spans therefore has zero orthogonal complement and is all of `H_o`. The orthogonal projections have approximation error decreasing to zero.

For the frozen Fourier targets, let `q_L` be the target with only `k<=L` retained and put `h_L=F_*-q_L`. Absolute summability gives the explicit tail estimate

\[
 \|q-q_L\|_\infty\le {R\over(2L+3)^s}=:\eta_L.
 \tag{A12}
\]

For a finite target with no omitted coefficient use `eta_L=0`. Thus `(E_J(h_L),B_J(h_L),eta_L)` is an independently specified target-complexity oracle. It separates Fourier truncation, finite-section approximation, and the cost of the representing direction. No rate for `E_J` or the smallest eigenvalue of `S_J` is asserted merely from density.

## 5. Conditional nonlinear oracle estimate, retaining all evolving features

Assume the Borel-law episode interface in Section 8. For its actual constrained population path write

\[
 r_\tau=f_{\theta_\tau}-q,\quad
 d_\tau(u)=\Pi_{\theta_\tau}g_{\theta_\tau}(u),\quad
 T_\tau h=\int h(u)d_\tau(u)\,d\nu_s(u),\quad
 K_\tau=T_\tau^*T_\tau.
\]

The exact equations, by the scalar chain rule, are

\[
 \theta_\tau'=-2T_\tau r_\tau,\qquad
 r_\tau'=-2K_\tau r_\tau,\qquad
 {d\over d\tau}\|r_\tau\|^2=-4\|T_\tau r_\tau\|^2.
 \tag{A13}
\]

The projector, first rows, middle action, readout, and both hidden features in these equations all evolve.

C.4.9.C.5 provides the following reached-curve mechanism. If the total instantaneous control mass is at most `A`, its displayed derivative formulas, the uniform `L4` query bound, and actual adjunction give

\[
 \sup_u\|g_{\theta_\tau}(u)'\|_E\le C A.
\]

Differentiating the ordinary anchor Gram inverse gives the same bound for `Pi'`. Hence there are finite uniform constants `L,C_d` such that

\[
 \|T_\tau\|\le L,\quad
 \|T_\tau-T_0\|\le C_d\tau,\quad
 \|K_\tau-K_0\|\le C_K\tau,\qquad C_K=2LC_d.
 \tag{A14}
\]

This is differentiation along the reached controlled curve. It is not an ambient Hessian assumption. In extending C.5 to an integral control, Minkowski bounds the lower-row `L4` velocity by `C` times its total variation; the identical Holder product then proves the displayed estimate.

Let `z_tau` solve `z'=-2K_0z`, `z_0=r_0`. The exponential of a bounded operator is defined by its norm-convergent series. Positivity of `K_0` implies contraction, since the squared norm of each solution has derivative `-4<Tz,Tz>`. Variation of constants in (A13), followed by (A14) and risk monotonicity, gives

\[
 \|r_\tau-z_\tau\|
 \le2\int_0^\tau\|(K_s-K_0)r_s\|ds
 \le C_K\|r_0\|\tau^2.
 \tag{A15}
\]

For every `v in E`, the endpoint linear flow satisfies

\[
 \|z_\tau\|\le\|r_0-T_0^*v\|+{\|v\|\over2\sqrt\tau}.
 \tag{A16}
\]

Here is a direct proof, avoiding a spectral theorem. Let `w_tau=exp(-2tau T_0T_0*)v`. The identity `exp(-2tau K_0)T_0*=T_0*exp(-2tau T_0T_0*)` follows termwise from the exponential series. Also

\[
 (\|w_\tau\|^2)'=-4\|T_0^*w_\tau\|^2,\qquad
 (\|T_0^*w_\tau\|^2)'=-4\|T_0T_0^*w_\tau\|^2\le0.
\]

The nonincreasing second quantity is at most its average on `[0,tau]`, hence at most `||v||^2/(4tau)`. Contract the remaining initial error to obtain (A16).

Combining (A11)–(A16), for every positive episode time,

\[
 \boxed{\quad
 \|f_{\theta_\tau}-q\|_{L^2(\nu_X)}
 \le\min\left\{\|F_*-q\|_{L^2(\nu_X)},
 \inf_{J,L}\left[
 E_J(h_L)+\eta_L+{B_J(h_L)\over2\sqrt\tau}
 \right]+C_K\|F_*-q\|\tau^2\right\}.
 \quad}                                                    \tag{A17}
\]

This is a finite-episode approximation bound with a declared nonlinear floor. It is useful only when its finite-section terms beat the initial error; the formula does not promise this for every target at a source-tube-limited horizon. Its stronger unconditional short-episode improvement mechanism is next.

Put `b_tau=T_tau r_tau`. Equations (A13)–(A14) imply

\[
 \|b_\tau-b_0\|
 \le (C_d+2L^3)\|r_0\|\tau=:C_b\|r_0\|\tau.
 \tag{A18}
\]

Indeed differentiate `T_tau r_tau` along the reached curve and bound the two resulting terms. If `r_0!=0`, Corollary 2 gives `b_0!=0`, and for

\[
 0<\tau\le\min\{\tau_{ex},\|b_0\|/(2C_b\|r_0\|)\}
\]

the exact identity (A13) yields

\[
 \|r_\tau\|^2\le\|r_0\|^2-\tau\|b_0\|^2.
 \tag{A19}
\]

The target-dependent constant is the norm of one explicitly defined endpoint integral, not a future-trajectory oracle.

## 6. A robust, independently specified subfamily and upper-hidden displacement

Assume `R>0`. Let

\[
 q_0(\alpha)=\cos^3\alpha-\sin^3\alpha,\qquad
 \psi(\alpha)=\sin^2(2\alpha)(\cos\alpha+\sin\alpha).
\]

Take `q=q_0+a psi+sin^2(2alpha) z(alpha)`, where

\[
 R/4\le a\le3R/8,\qquad
 \sum_k(2k+1)^s(|z_{c,k}|+|z_{s,k}|)\le R/16.
 \tag{A20}
\]

This is inside the frozen class: its weighted coefficient sum is at most `2a+R/16<=13R/16<R`. It has genuine independent shape variation. Its relative interior is nonempty, with the fixed axes and noise restrictions unchanged. Every admitted density `p` is permitted.

The endpoint satisfies `F_*(u_2,u_1)=-F_*(u_1,u_2)`. One proof uses the finite reference flows: swapping the two columns of `W1` and negating the readout maps the reference GF to itself, with prediction `-f(u_2,u_1)`. The Gaussian initialization is invariant under that transformation. At each fixed physical time the deterministic population prediction limit therefore has this antisymmetry; reference endpoint convergence passes it to `F_*`. This uses no feature-freezing assertion.

The same antisymmetry holds for `q_0`, while `psi` is symmetric under coordinate swap. They are orthogonal in `L2(rho)`. Direct integration gives `||psi||^2=3/8`: `(cos alpha+sin alpha)^2=1+sin(2alpha)`, and the odd sine term integrates to zero against `sin^4(2alpha)`. Consequently every target in (A20) has

\[
 \|F_*-q\|_{L^2(\nu_X)}
 \ge {1\over\sqrt2}\left({R\over4}\sqrt{3/8}-{R\over16}\right)>0.
 \tag{A21}
\]

For fixed `D,R,s`, the closed density and target family used here is compact in the uniform topology. For densities this follows by choosing finite circle meshes, extracting convergent values by diagonal subsequences, and applying the common Lipschitz modulus. For targets the coefficient diagonal subsequence and the uniform tail estimate (A12) give the same conclusion. The maps `p,q -> b_0` and their middle blocks are continuous, since their integrands are uniformly bounded endpoint fields and the anchor inverse is fixed. Corollary 2 and (A21) therefore give genuine positive constants

\[
 b_*:=\min_{p,q}\|b_0\|>0,\qquad
 h_*:=\min_{p,q}\|(b_0)_H\|>0,
 \tag{A22}
\]

where the subscript `H` denotes the first-row plus middle hidden blocks. In fact the middle block alone has positive minimum. These are defined endpoint constants over a compact independently specified class; no continuum spectral gap is claimed. With a uniform bound for `||r_0||`, (A19) gives one uniform positive episode and a uniform unseen-risk gain on this whole subfamily.

To convert hidden force into upper activation displacement, keep `r_0`, the density, and

\[
 \beta=M^{-1}G^*\int r_0(u)g(u)d\nu_s(u)
\]

fixed, and define the scalar hidden contrast

\[
 O(\theta)=\int r_0(u)p_s(u)
     \langle c_\dagger,H^2_\theta(u)\rangle d\rho(u)
 -\sum_{a=1}^2\beta_a\langle c_\dagger,H^2_\theta(e_a)\rangle.
 \tag{A23}
\]

Its endpoint raw gradient is `((b_0)_H,0)`. The strong scalar chain rule and the actual velocity in (A13) give

\[
 O'(0)=-2\|(b_0)_H\|^2.
 \tag{A24}
\]

C.4.9.B.3's endpoint `L4` estimate applies with the fixed readout `c_dagger`; integrating its gradient modulus against the bounded coefficients in (A23) gives a uniform `C sqrt(||theta-theta_dagger||)` modulus. The velocity is bounded and continuous. Thus, after a uniform reduction of the episode time, `O'(tau)<=-h_*^2` throughout the robust family. This is a continuity argument for the actual finite trajectory, not the initial Taylor term used as a finite-time surrogate.

Define the whole-circle paired observation

\[
 J_2(\tau)={1\over3}\left[
 \int\|H^2_{\theta_\tau}(u)-H^2_\dagger(u)\|_2^2d\rho(u)
 +\sum_{a=1}^2\|H^2_{\theta_\tau}(e_a)-H^2_\dagger(e_a)\|_2^2\right].
\]

Two applications of Cauchy–Schwarz give

\[
 |O(\theta_\tau)-O(\theta_\dagger)|^2
 \le3\|c_\dagger\|_2^2
       (\|r_0p_s\|_{L^2(\rho)}^2+|\beta|^2)J_2(\tau).
\]

Hence, uniformly over the family,

\[
 J_2(\tau)\ge
 {h_*^4\tau^2\over
  3\|c_\dagger\|_2^2\sup_{p,q}(\|r_0p_s\|_2^2+|\beta|^2)}>0.
 \tag{A25}
\]

A fixed finite query mesh can replace the circle integral with a slightly reduced margin: the raw/action bounds give a uniform `L2` input Lipschitz constant for `H2`, hence a uniform quadrature error for its bounded squared displacement. Choosing a mesh after the theoretical positive margin is fixed requires only class/reference constants. The same mesh works for every target in the robust family.

If `R=0`, the endpoint-completeness and oracle results remain valid, and (A19) applies when `F_*!=q_0`. This route does not prove that inequality for the singleton `R=0` class; its robust-family claim is expressly for `R>0`.

## 7. Separate input sampling and centered-noise control; an available rule

Again assume the uniform episode interface of Section 8. Let `theta_tau` be the population constrained path for `(p,q)` and `hat theta_tau` the path for `m` training observations. Their initialization is the same endpoint. Evaluate the following functions only on the deterministic population path:

\[
 A_\tau(X)=r_\tau(X)d_\tau(X),\qquad
 B_\tau(X,\xi)=\xi d_\tau(X).
\]

At the same population state, the empirical-minus-population field is exactly

\[
 -2\left[(P_m-P_X)A_\tau-P_m B_\tau\right].
 \tag{A26}
\]

Set

\[
 v_X(\tau)=E\|A_\tau-EA_\tau\|_E^2,\qquad
 v_\xi(\tau)=E[\xi^2\|d_\tau(X)\|_E^2]\le\sigma^2L^2,
\]
\[
 \mathfrak a_X=\sqrt{T\int_0^T v_X(s)ds},\qquad
 \mathfrak a_\xi=\sqrt{T\int_0^T v_\xi(s)ds}\le T\sigma L.
 \tag{A27}
\]

Hilbert-space independence and zero means yield

\[
 E\left(\int_0^T\|(P_m-P_X)A_s\|ds\right)^2
       \le {\mathfrak a_X^2\over m},\qquad
 E\left(\int_0^T\|P_mB_s\|ds\right)^2
       \le {\mathfrak a_\xi^2\over m}.
 \tag{A28}
\]

Indeed the expectation of the squared norm of each centered empirical mean is its single-sample second moment divided by `m`: cross terms vanish by independence. Cauchy–Schwarz in time and integration prove (A28). Conditional centering `E[xi|X]=0` is exactly what removes the cross terms for the second mean; a bound on noise magnitude alone would not do so.

The triangle inequality in scalar `L2` and Markov's inequality show that, with probability at least `1-delta`, the integrated norm of (A26) is at most

\[
 \eta_m={2(\mathfrak a_X+\mathfrak a_\xi)\over\sqrt{m\delta}}.
 \tag{A29}
\]

For a fully class/reference bound use `mathfrak a_X<=T L sup_tau ||r_tau||_infty` and `mathfrak a_xi<=T sigma L`. These are different mechanisms with additive scales, not a joint Wasserstein distance in `(X,Y)` that obscures conditional noise cancellation.

The one-reference gradient cutoff and anchor inverse identity give, with the population path as the sole tail-bearing comparison,

\[
 D(\tau)\le\eta_m+C\int_0^\tau\omega(D(s))ds,
 \quad D(\tau)=\sup_{s\le\tau}\|\hat\theta_s-\theta_s\|_E,
 \quad\omega(z)=z\sqrt{\log(e/z)}.
\]

This holds while the states remain in the common inner tube; its existence is part of the interface. The C.4.9.C.2 calculation yields

\[
 \sup_{\tau\le T}\|\hat\theta_\tau-\theta_\tau\|_E
 \le e\exp\left[-\left(\sqrt{\log(e/\eta_m)}-CT/2\right)^2\right]
 =:\mathcal O_T(\eta_m)
 \tag{A30}
\]

for sufficiently large `m`; at zero forcing interpret the right side as zero. The estimate is `m^{-1/2+o(1)}` for fixed `delta,T`, with separate input and noise constants. Prediction risk differs by at most `C mathcal O_T(eta_m)` on the common bounded region. Applying the same argument to the hidden observable transfers its positive margin as well.

There are two available stopping choices.

* A deterministic slow time `T` chosen once below the uniform source, risk, and hidden-motion thresholds uses only the frozen class and reference constants, not the unknown target error or population force. It already gives the generalization statement (A17) plus (A30).
* For a data-based choice, retain an independent validation set of `v` observations and a finite grid `0<T_1<...<T_J<=T`, with the positive times bounded below by a fixed `T_min>0`. Include the paired reference predictor as candidate zero. Choose the candidate with least validation square loss, breaking ties toward smaller time.

Here is an elementary quantitative validation guarantee. On the common prediction bound `|f|<=B`, each validation square loss lies in `[0,M]`, where `M=(B+1)^2`. Conditional on the training data, each empirical validation risk has variance at most `M^2/v`. The union bound and Chebyshev inequality therefore give, with probability at least `1-delta_v`, simultaneous error at most

\[
 e_v=M\sqrt{(J+1)/(v\delta_v)}.
\]

The selected predictor's true excess risk is at most the minimum candidate excess risk plus `2e_v`; subtracting the common irreducible-noise risk does not alter the comparison. Together with (A30), its population comparison is at most

\[
 \min_{j\ge1}\|f_{\theta_{T_j}}-q\|^2
       +C\mathcal O_T(\eta_m)+2e_v.
 \tag{A31}
\]

Once the last two errors are smaller than half the robust gain from (A19), candidate zero cannot be selected. Every remaining candidate has the uniform hidden margin at least the bound (A25) at `T_min`, reduced by its sampling error.

This validation rule is available from observations; it never evaluates `q`, a continuum kernel eigenvalue, or an unknown oracle approximation error. At finite width, candidate zero is the paired actual reference network at the largest physical time, and the other candidates are snapshots of one actual fixed-mixture run at `T_j/epsilon`. Thus all candidates are directly available. Keeping earlier snapshots and selecting one is a stopping/output rule; it does not alter the fixed training law. The input/noise separation above concerns the training path; the displayed elementary validation penalty is intentionally a coarser distribution-free bound.

## 8. Exact remaining interface: Borel-law continuation and actual GF capture

For a complete theorem the following interface must be proved, with constants uniform over all probability laws on the full circle with `|Y|<=1`, including every empirical law:

1. A common positive `T` and canonical source-retaining strong constrained path from `theta_dagger`, with field
   `-2 Pi_theta integral (f_theta(u)-y) g_theta(u) dnu(u,y)`.
2. A common accumulated-force source tube, bounded readout, uniform passive-query Gaussian tails, positive two-anchor Gram, and the reached differentiation bounds used in (A14).
3. Original-initialization mixture continuation through `T/epsilon`, and convergence on every positive slow-time subinterval to that constrained path, retaining the exact known anchor weights.
4. Actual finite GF and the same-array paired observations converge at each fixed `epsilon` before `epsilon` tends to zero. For random training data this must hold conditionally on each fixed empirical dataset; probability and boundedness then permit averaging. Sample size increases only after these two limits.

C.4.9 proves this for its one-atom parameter rectangle. The following route to the extension is concrete, but is recorded as an obligation rather than a finished theorem in this first-round file.

* Its source-tube proof A is stated for arbitrary finite direction lists. Inspecting its pulse equations shows that update slots occur through total absolute coefficient mass; the bounds CT26–CT45 contain no cardinality factor. Verify that this remains true in the underlying fixed-program/common-carrier dependency III.F, which this attempt has not independently read.
* For a finite added law replace its single added force by the weighted sum. Bound its total variation by `2 sup|f-y|`; the anchor correction has mass at most a fixed multiple because its inverse is only two by two. The C.4.9.C residual inequalities and `theta'=epsilon V+B r'` are unchanged after this substitution. The differentiation proof C.5 uses Minkowski and total variation in place of a three-term sum.
* Quantize an arbitrary law on `S1 x [-1,1]` into finitely supported laws. C.4.1's transport inequality, with its rank identity also in HS norm, and the source-tube tails supply a common Osgood modulus in the law's `W1` distance. This should construct a Cauchy family on one carrier without dependence on support size, retaining all old sources. The common bounds must be established before passage to the limit.
* For actual finite GF at a fixed physical horizon, use a finite-law reference proxy and C.4.1's normalized one-reference transport inequality. Its proof controls changing inputs with the full first-row RMS and tails of the proxy alone. Width is sent to infinity with quadrature, cutoff, and Euler mesh fixed; subsequently remove those three approximations in the proved order. Do not take a growing finite transcript before width or assume a supremum of Gaussian queries over a dataset.

No new optimizer or source reset is needed for those steps. Nonetheless the finite-to-Borel source construction and its uniformity are a necessary bridge; equations (A13) alone do not establish them. If the coordinator proves this interface independently, Sections 3–7 supply the missing continuum approximation, input/noise separation, robust activity, and available selection bounds.

Under that interface, the final finite-network statement has exactly the authorized order: for every fixed training and validation sample size, first `n->infinity` at each fixed positive `epsilon`, then `epsilon->0`; only then send training and validation sample sizes to infinity. The positive-time finite grid makes all selection comparisons finite, and the common prediction bounds control passage of risk. No simultaneous width/epsilon/sample rate or raw-GD extension is asserted.

## 9. Audit and route disposition

| Claim | Status | Evidence and surviving restriction |
|---|---|---|
| Odd signed-measure injectivity of the endpoint middle transform | Proved from C.4.9 endpoint facts | Lemma 1, positive gate, protected rows, explicit sign Fourier transform |
| Dense constrained endpoint approximation space | Proved | Corollary 2 and finite-section orthogonal complement argument |
| Uniform continuum kernel coercivity | Not claimed; impossible for this compact operator on infinite-dimensional `H_o` | Compactness argument after Corollary 2 |
| Finite-section target oracle and Fourier tail | Proved | Explicit matrices (A10)–(A12) |
| Nonlinear finite-time oracle | Exact under the episode interface | (A13)–(A17), moving-kernel error `C_K||r_0||tau^2` |
| Strict robust endpoint force and hidden force | Proved for the independent subfamily (A20), `R>0` | Reflection symmetry, nonzero symmetric target component, injectivity, compactness |
| Finite-time unseen-risk improvement and upper-hidden displacement | Exact under the episode interface | (A18)–(A25), actual derivative continuity |
| Input/noise sampling separation and validation selection | Exact under the uniform episode interface | (A26)–(A31), elementary Hilbert variances and Osgood comparison |
| Borel-law continuation and actual finite-GF transfer | Open in this attempt | Section 8 specifies the exact uniform source/common-carrier bridge |

The main adversarial limitation is quantitative conditioning: density of the endpoint approximation space need not make the finite-section oracle small within the available short episode. This route does not turn universality into a practical sample or approximation rate. The robust risk gain is independently certified by the endpoint force and continuity; it is not claimed to follow from a favorable numerical value of the oracle. Similarly, the nonzero hidden gradient is converted into a paired activation observation by a separate scalar contrast, rather than treated as synonymous with activation motion.

Recommended registry status: **promising, with a proved distinctive key estimate and one named continuation/capture interface**. The route's main contribution is the continuum signed-measure argument. Its reopen condition for a full theorem is a complete verification of Section 8, followed by independent audit of the integrated result.
