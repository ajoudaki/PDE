# Exact-hash adversarial audit of the offset-arctangent global theorem

**Overall status: PASS.** The three-file package proves the stated changed-activation theorem, with its stated probability, observation, solution-class, and finite-physical-time quantifiers. I found no remaining fatal gap or unresolved mathematical premise in that theorem. This is a proof audit, not a claim that every sentence is maximally expanded. Below I supply the intermediate verifications needed to assess the compressed passages, and distinguish the theorem's actual scope from stronger statements it does not claim.

## 1. Scope and immutable identification

The audit was performed in fresh context. I read the requested skill at `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely, followed by the entirety of exactly these three mathematical files. Their hashes were checked against the request and matched:

| Label | File | SHA256 |
| --- | --- | --- |
| G | `/tmp/l3-activation-design-oaGjWO/OFFSET_ARCTAN_GLOBAL_THEOREM.md` | `d50b7708b767f20010437e48a716366ac32b5dd6db6e6e12beb94cd1d15897e5` |
| B | `/tmp/l3-activation-design-oaGjWO/OFFSET_ARCTAN_RESPONSE_BOOTSTRAP.md` | `65579a94f883f1b9f9240430039f334f5b3b663599cd7ab16bb15c35f7bacc43` |
| L | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |

Locations below are one-based line numbers in these exact versions. G has 822 lines, B 273, and L 2321. I did not read other reviews, worker notes, source tasks, repository material, or the separate files named in L's historical references. The relevant arguments are included in L itself and were audited there. No simulation, agent, external search, or source/repository mutation was used. The candidate and both dependencies were left unchanged.

The authorized activation is the single fixed function

\[
\phi(z)=1+\frac{\arctan z}{10}.
\]

The audit retains the initialization, raw GD, time scale, recomputed raw interpolation, observables, and autonomous restart requirements in G. It does not substitute the original unshifted activation, an order-one initial readout, a frozen-feature approximation, or a transformed Euler algorithm for the actual GD.

The mathematical chain checked is: finite adaptive Gaussian identification, common bounded actions with adjoints, fixed-clip flows, mesh- and clip-uniform response control, removal of clipping, raw gradient structure and uniqueness, the global physical clock, actual-GD transfer, joint observations and path laws, and nontriviality at later times. The local arctangent theorem in L is not treated as authority for this chain; its underlying generic arguments are checked below.

## 2. Model, scaling, and activation adaptation — PASS

**Locations:** G 24–69, 119–130; L 217–242, 299, 420–447.

The normalized finite vector inner product is \(u^Tv/n\), and the matrix variation norm is ordinary Frobenius norm. With these conventions the raw gradient of the predictor is exactly

\[
(\delta^{(1)},\ \delta^{(2)}(h^{(1)})^T/n,
\ \delta^{(3)}(h^{(2)})^T/n,\ h^{(3)}).
\]

Thus the factors of \(n\), the residual factor \(-2r\), and all four kernel normalizations in G (2), (4) are consistent. The rescaled readout has coordinate variance \(n^{-2}\); its normalized norm is \(O_{\mathbb P}(n^{-1})\). Replacing it by zero is justified only inside comparisons that explicitly estimate this discrepancy.

The activation bounds used by the proof hold globally:

\[
\frac56<\phi<\frac76,
\qquad \phi'(z)=\frac1{10(1+z^2)}>0,
\qquad |\phi''|\le\frac15.
\]

In particular \(\pi<10/3\) suffices for the deliberately loose bounds on \(\phi\). For
\(F(z)=10(z+z^3/3)\), one has \(F'=1/\phi'\),
\((F^{-1})'=\phi'\circ F^{-1}\), and
\(\chi'=(\phi'\circ F^{-1})^2\). Hence the asserted Lipschitz constants \(1/10\) and \(1/100\) are valid. The polynomial root tuple \((Z_0,F(Z_0))\) has every finite moment. Its treatment as a root tuple avoids making a false global Lipschitz claim about \(F\).

At fixed clipping and program length, the middle product has bounded second factor. The readout is pointwise bounded because it is a sum of bounded features. Smooth extension of its product map outside a larger interval preserves both actual values and their derivatives along the scalar program. This verifies the bounded-first-derivative coordinate hypotheses used in L. The adapted Gaussian proof needs uncentered second moments, bounded coordinate derivatives, and root integrability; it does not need oddness, zero mean of the activation, or the old numerical value of \(\phi'\).

## 3. Adaptive finite-program Gaussian proof — PASS

**Locations:** L 297–402, 404–447; G 132–201.

### Conditioning and both matrix orientations

For old queries \(WV=Y\), \(W^TU=Q\), the conditional mean in L (1) satisfies both constraints: the first term accounts for the action on \(\operatorname{span}V\), and the second supplies the remaining transpose constraints on its perpendicular complement. The unexplored part is

\[
P_{U^\perp}\widetilde W P_{V^\perp}.
\]

This yields L (2), with variance factor \(\|h_\perp\|^2/n\). The dropped projection of a fresh standard Gaussian has expected normalized squared norm \(\operatorname{rank}(U)/n\). Its variance multiplier is bounded in probability at fixed program length. Thus the projection error vanishes in the required normalized norm.

Adaptive interleaving of the two independent matrices does not invalidate this conditioning. Given the existing transcript, the next input is fixed. Observing the next answer imposes a linear constraint on just the queried conditional residual. The other residual's conditional law and independence are retained. This is a sequential argument; it does not assume that a trained input is independent of its matrix.

With positive limiting query Grams, the coefficient limits follow from joint second-moment convergence of previous variables. After dropping the finite-rank projection, bounded-test conditional averaging and Gaussian second-moment estimates give joint weak convergence and convergence of second moments. For example, the normalized pairing of a known vector with the fresh Gaussian has conditional variance \(\|v\|_n^2/n\). The resulting empirical convergence is in \(\mathcal W_2\). It does not require reused coordinate tuples to be iid.

### Identification of the response

In L 335–375, the correction in each old transpose output is a linear combination of old forward inputs. It therefore disappears in its pairing with \(h_\perp\). Writing \(\Gamma_U=(\mathbb E u_su_t)\), the remaining pairing satisfies

\[
\mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp],
\qquad
\mathbb E[\zeta h_\perp]
=\Gamma_U\mathbb E\nabla_\zeta h_\perp.
\]

Gaussian integration by parts applies because the finite coordinate expression has bounded first derivatives and at most linear growth in its finite inputs, with integrable roots. Other source groups and roots can be conditioned upon. The inverse Gram in the conditional mean then cancels \(\Gamma_U\). Substituting the previous forward decompositions cancels the derivatives of the least-squares projection and leaves

\[
(Wh)_{\rm lim}=\xi_h+\sum_s u_s\mathbb E\partial_{\zeta_s}h.
\]

The new source is the linear projection of old same-orientation sources plus a fresh Gaussian innovation. Its covariance with old sources is \(\mathbb E[h v_r]\), and its variance is \(\mathbb E h^2\). Independence of distinct source groups is preserved in this induction. This independence describes the source representation, not independence of a matrix from its transpose or of a response shift from its source.

Derivatives are of the full finite coordinate expression, holding deterministic coefficients fixed. Therefore derivative paths involving the other matrix are retained. No derivative of a covariance square root or population coefficient selection is required or appropriate here.

### Singular query Grams

L 379–402 supplies an effective removal argument rather than assuming pseudoinverse continuity. Each new query is perturbed by its own independent \(\epsilon\)-Gaussian input. Its limiting squared distance from the old same-direction input span has a contribution at least \(\epsilon^2\), so the fixed-length perturbed proof has positive Grams.

At finite width, induction through the fixed Lipschitz program, with bounded initial operator norms and finitely many bounded normalized noise norms, gives an \(O(\epsilon)\) discrepancy. The constant is allowed to depend on the finite program.

On the scalar side the recursion is causal and contains expected source derivatives, not inverse Grams. Inductively its earlier coefficients remain bounded and converge as \(\epsilon\to0\). Covariance square roots are continuous on positive semidefinite matrices; bounded derivatives and finite root moments then pass the next source law, second moments, and expected derivatives to the limit. Keeping the auxiliary root slots with coefficient zero at \(\epsilon=0\) gives precisely the unperturbed formal program. This also explains why formal derivatives remain meaningful at a singular law. The contracted response is insensitive to covariance-null directions, as L 394–402 verifies.

There is no need for a estimate uniform in the number of queries at this stage. The later mesh limit uses deterministic clipped-flow stability, not a growing Gaussian-program theorem.

### Actual empirical feedback and current-time returns

The learned terms are exactly the rank-one sums in L 406–418. Freezing their contractions is causal: a forward contraction uses already available forward input coordinates; a transpose contraction uses the already computed backward input. The fixed oracle's contractions converge by its joint \(\mathcal W_2\) laws. Cauchy–Schwarz and finite induction then compare the actual empirical-feedback program with that oracle. This discharges the identification premise of B; it is not an additional training assumption.

At time \(k\), the call order is forward through matrix 2, forward through matrix 3, transpose through matrix 3, transpose through matrix 2. Consequently the forward responses use \(s<k\), but the transpose responses include \(s=k\). In particular the package correctly includes

\[
b^{(3)}_{kk}=\mathbb E[W^{(4)}_k\phi''(Z^{(3)}_k)],
\]
\[
b^{(2)}_{kk}
=\mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
+b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)].
\]

The latter second term is essential and is present in both the identification and the estimate in B. The learned-rank contribution at the current time is correctly absent because the stored matrix only contains updates with index less than \(k\).

## 4. Common population spaces, actions, and adjoints — PASS

**Locations:** L 470–547; G 204–219.

The countable family is closed under finite unions, rational linear combinations, both directions of both matrices, and a dense family of bounded smooth coordinate maps. Joint empirical limits of finite unions are consistent because they are limits of the same finite-width calculations. Their countable product construction gives the three generated probability spaces.

The stated Gaussian matrix bound is sufficient: a \(1/4\)-net with at most \(9^n\) points gives

\[
\mathbb P(\|W\|_{\rm op}>10)
\le2\,9^{2n}e^{-100n/8}\longrightarrow0.
\]

Indeed, a norm exceeding 10 forces a net bilinear form exceeding 5, whose Gaussian variance is \(1/n\). Passing finite inequalities to limiting second moments proves the bound on each generated probe combination. Zero input norm forces zero output norm, so the assignment is well-defined on equivalence classes and linear. The node span is dense in generated \(L^2\): finite-coordinate measurable functions are dense, bounded continuous functions approximate them in the finite-coordinate laws, and compact approximation and clipping bring them into the specified countable family.

Both orientations consequently extend as bounded actions. Finite transpose identities pass to the limit in scalar inner products, and density proves adjunction on the whole generated spaces. This does not require a joint coordinate pairing between distinct layers. The scalar contractions on either side of adjunction are each calculated on their own layer.

Real coefficients and additional fixed Lipschitz probes can be approximated using compact truncation and propagated normalized-norm errors. The operator bounds control each subsequent action. Thus the construction supports the claimed observation class and all clipped programs on common spaces; it is not merely a separate probability space for each mesh.

## 5. Fixed-clip existence and width limits — PASS

**Locations:** G 221–265; L 549–719, 1159–1255.

The rank-one action has both operator and Hilbert–Schmidt norm \(\|U\|_2\|V\|_2\), matching the finite action \(uv^T/n\). Integrating the readout, then matrix 3, then matrix 2 gives G (6); bounded activation and gates suffice. The first-coordinate velocity is bounded by the product of the two operator bounds and the readout bound. The same estimates apply to positive-step Euler prefixes. No clipped gradient identity is used.

The forward difference estimates use Lipschitz \(F^{-1}\), \(\chi\), and \(\phi\). The top backward difference can be expanded with the reference readout multiplying the gate difference. Hence G (7) needs a pointwise bound only for the reference readout; a normalized \(L^2\) bound suffices for the other readout.

The middle clipped gate difference costs \(C R\) times the state discrepancy, and all other terms cost \(C\) times that discrepancy. Picard iteration is valid on the complete closed set of paths imposing the pointwise readout bound: that condition survives \(L^2\) convergence and is preserved by integration of the readout equation. The primal estimates provide continuation for each fixed clip. The bounded velocity and Lipschitz field give a local Euler defect \(O_{R,S}(\Delta^2)\), followed by global error \(O_{R,S}(\Delta)\).

Combining that deterministic, width-uniform comparison with fixed-program convergence proves fixed-clip flow convergence. The references used later have exactly zero initial readout, so the reference pointwise bound is available. The actual small random readout is subsequently restored by an asymmetric comparison. There is no hidden need for a width-uniform supremum estimate on an arbitrary nonzero readout.

## 6. Numerical response closure on feature time 3/2 — PASS

**Locations:** all of B, especially 98–251; G 269–287.

I checked the entire coefficient induction, not only the terminal estimate. All estimates are uniform in the mesh and clip under the displayed scalar-system premise, now discharged by Sections 2–3 of this audit.

For the bottom forward response, \(|\chi'|\le1/100\) and the past-row bound give

\[
|\partial_{\zeta^{(1)}_s}H^{(1)}_j|
\le\frac\Delta{100}e^{S/100},
\quad
|a^{(2)}_{js}|
\le\Delta\left(\frac{49}{36}+\frac{e^{S/100}}{100}\right)
<\frac32\Delta.
\]

For the middle response the coefficient of a preactivation derivative is
\(|q^{(2)}_r|/5+V_r/100\). The second summand includes the current same-time return within row \(r\). Summing source derivatives gives a direct term 1 for the \(\xi^{(2)}\) derivatives and a single direct term at most \(A\Delta/10\) for a \(\zeta^{(2)}_s\) derivative. Discrete Gronwall therefore gives B (3) and the envelope \(E_j\).

The Gaussian variance is at most \((aS/10)^2\). Jensen's inequality over times, rather than independence over times, gives

\[
\mathbb E E_j^p
\le2\exp\left(\frac{219p}{400}
+\frac{3969p^2}{1280000}\right).
\]

For \(p=1,2\), dividing the exponent by \(p\) gives a number below \(3/5\). Thus \(\|E_j\|_1<4\) and \(\|E_j\|_2<3\). These imply

\[
|a^{(3)}_{js}|\le\Delta(49/36+3/50)<(3/2)\Delta.
\]

At the top, differentiating both the accumulated readout and the gate yields the factor
\(1/100+a/5=73/300\). Hence

\[
\max_{v\le j}T_v\le e^{657/800}<5/2,
\]
\[
V_k\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}<1.
\]

This uses only past backward rows. It is therefore available before estimating the current middle field. Minkowski gives
\(\|q^{(2)}_k\|_2\le7/40+7/6=161/120=:Q\), with no independence assumption about the response shift. Finally, Cauchy–Schwarz, the middle derivative envelope, and the learned covariance term give

\[
U_k\le3(Q/5+1/100)+\frac{3Q^2}{200}
=\frac{2482563}{2880000}<\frac9{10}.
\]

The induction closes in the stated causal order; it never assumes the current \(U_k\) in proving the current \(V_k\) or \(U_k\). The zero-readout base case gives \(U_0=V_0=0\), including the zero-variance source slots under the formal-derivative convention.

Consequently \(q^{(2)}_k\) is a centered Gaussian of variance at most \((7/40)^2\) plus a shift of absolute value at most \(7/6\). This gives B (1), hence a uniform exponential-square moment after enlarging \(K\). Fixed-clip Euler convergence and Fatou pass that moment to every clipped flow time. A different almost-sure subsequence at different times is harmless: the conclusion is a deterministic expectation bound with the same constant for every time, not a bound on the supremum of a Gaussian path.

## 7. Removal of clipping and feature-time uniqueness/restart — PASS

**Locations:** G 289–362; L 1257–1501.

The three-term identity at G 295–299 is exact. In particular the gate-difference term uses \(\tau_R(q_B)\), whose absolute value is at most \(2R\), and the discrepancy of the two clips is evaluated at the reference field \(q_B\). It is zero for \(|q_B|\le R\), and elsewhere is bounded by \(2|q_B|\), including when \(R'=\infty\).

Since \(|q|\mathbf1_{|q|>R}\le2(|q|-R/2)_+\), this gives separately

\[
\|\delta^{(2)}_{R'}(A)-\delta^{(2)}_R(B)\|_2
\le C(1+R)d(A,B)+C\|b_R(q_B)\|_2,
\]

and, by bounded actions and rank-one estimates, G (10) for the full field. The constant is independent of \(R'\).

The exponential-square moment implies

\[
\mathbb E[q^2\mathbf1_{|q|>u}]
\le4K^2e^{-u^2/(2K^2)},
\qquad
\|b_R(q)\|_2\le2Ke^{-R^2/(16K^2)}.
\]

Thus the \(e^{C(1+R)S}\) loss in Gronwall is dominated by the Gaussian decay in \(R\). The clipped states are Cauchy uniformly on the full feature interval. The same inequality evaluated at their limit proves uniform convergence of the actual uncut vector field to the clipped fields; the extra factor \(1+R\) still vanishes against the error bound. This validates the integral equation and its continuous velocity, rather than merely constructing a limit of trajectories.

For an arbitrary competing bounded-primal integral solution, exactly the same inequality uses only its primal bounds. Its own tail distribution never enters. Its bound changes \(C\), but any fixed exponential \(e^{CR}\) is still dominated by \(e^{-cR^2}\). This proves uniqueness. At a reached state, the initial comparison discrepancy is already of that same form, and multiplication by a second Gronwall exponential still tends to zero. Restart uniqueness is therefore established on the constructed feature interval.

For finite width, the fixed-clip \(\mathcal W_2\) convergence applies to the continuous quadratic-growth measurement \(b_R^2\). The reference \(q^{(2)}\) is uniformly Lipschitz in time by G (7) and the primal velocity bounds. Since \(b_R\) is 1-Lipschitz, a finite time net proves G (13). Finite exponential moments or tail indicators are not needed. The asymmetric comparison restores the prescribed small readout and proves G (14). Finite uncut existence on this interval follows from smooth finite-dimensional equations and the same primal bounds.

## 8. Raw gradient structure and all finite physical times — PASS

**Locations:** G 364–444; L 1748–1914.

Trained increments are integrals of continuous rank-one velocities, so they are Hilbert–Schmidt. The rank-one difference inequality holds in that norm as well, and therefore identifies the same increments after cutoff removal.

The scalar Taylor argument is adequate for Fréchet differentiability of the predictor in the raw affine Hilbert space. For a fixed backward factor \(B\in L^2\), truncating \(B\) bounds the remainder by

\[
CR\|v\|_2^2+C\|B\mathbf1_{|B|>R}\|_2\|v\|_2=o(\|v\|_2).
\]

Forward variations are \(O(\|d\theta\|)\) in \(L^2\); terms containing both a matrix change and a feature change are quadratic because \(\|dW\|_{\rm op}\le\|dW\|_{\rm HS}\). Expanding the scalar output backwards thus gives the displayed raw gradient. Bounded gates multiply converging fixed \(L^2\) factors continuously by truncation, which proves continuity of the gradient. This avoids an invalid Fréchet derivative claim for a nonlinear Nemytskii map from all of \(L^2\) into itself.

The chain rule for \(F^{-1}\) along the constructed curve gives \((Z^{(1)})'=\phi'(Z^{(1)})q^{(1)}\), so feature time is raw gradient ascent of \(f\). Consequently

\[
f'=\sum_{\ell=1}^4K^{(\ell)},
\qquad K^{(4)}\ge25/36.
\]

All four summands are continuous and bounded. Since \(f(0)=0\) and \(f(3/2)\ge25/24>1\), the unique root satisfies
\(0<s_*\le36/25<3/2\). For the scalar clock \(s'=2(1-f(s))\), set \(B_* =\sup_{[0,s_*]}f'\). Before reaching the root,

\[
(s_*-s)'\ge-2B_*(s_*-s),
\qquad s_*-s(t)\ge s_*e^{-2B_*t}>0.
\]

Local scalar Lipschitz existence, this nonattainment estimate, and boundedness of the interval give a unique clock for all finite physical times. The feature interval established above therefore covers every finite physical horizon. No clipped predictor monotonicity or response estimate at arbitrarily large feature time is required.

### Competing raw solutions, not only transformed solutions

G 430–444 also closes the raw-solution issue. For a continuous bounded-primal raw integral solution, bounded gates and operator continuity make the backward fields continuous in \(L^2\). Its rank-one matrix integral equation lifts its increments to Hilbert–Schmidt integrals. The raw scalar chain rule therefore applies to this competitor as well and gives

\[
\frac d{dt}(1-f)=-2(1-f)\sum_\ell K^{(\ell)}.
\]

The kernel is bounded on each compact competing interval by its primal bounds. A positive initial \(1-f\) consequently cannot vanish there. Coordinate absolute continuity and the ordinary scalar chain rule give

\[
F(Z^{(1)}(t))=F(Z^{(1)}(t_0))
+\int_{t_0}^t2(1-f(u))q^{(1)}(u)\,du.
\]

The right side is an \(L^2\) identity; membership of the transformed coordinate need not be separately assumed for a raw competitor. Its increasing feature clock permits the asymmetric uniqueness comparison up to a first attempted exit. Scalar-clock uniqueness then identifies the clock and excludes that exit at finite time. Starting at any reached state preserves positivity of \(1-f\) and the transformed \(L^2\) state. Thus autonomous raw restartability follows in precisely the stated bounded-primal integral-solution class.

## 9. Actual raw GD, interpolation, and full sequences — PASS

**Locations:** G 446–539; corresponding local bridge in L 1503–1668.

G does not identify transformed Euler with raw GD. The exact cubic correction in G (17) has the correct factors of 10:

\[
F(z+\alpha\phi'(z)q)-F(z)
=\alpha q+10\alpha^2z\phi'(z)^2q^2
+\frac{10}{3}\alpha^3\phi'(z)^3q^3.
\]

With \(\|q^{(1)}\|_2\le C\sqrt n\), the inequalities
\(\|q^2\|_2\le\|q\|_2^2\) and
\(\|q^3\|_2\le\|q\|_2^3\), together with bounded \(|z|\phi'(z)^2\), give normalized error
\(C(\alpha^2\sqrt n+\alpha^3n)\). On any positive prefix with bounded total feature time and \(\max\alpha\le C\eta_n\), the sum is

\[
O(\eta_n\sqrt n+\eta_n^2n)
=O(n^{-3/2}+n^{-3})\longrightarrow0.
\]

No unproved higher-coordinate moment is used.

The positive-prefix argument is properly stopped before assuming convergence. For fixed physical \(T\), the population residual on \([0,T+1]\) has a positive minimum \(\rho\). Before the stated stopping node, the raw updates have positive feature increments, so the primal bounds hold inductively. These bound the predictor and hence the increment by \(C\eta_n\). The first stopping endpoint still lies inside the proven feature interval, allowing the comparison through that endpoint.

The clipped-reference local error, asymmetric stability, and cubic correction give G (19). The random partition requires no independent-tail estimate: the time-Lipschitz reference tail norm gives its Riemann-sum bound pathwise. The population predictor is Lipschitz in feature time, so scalar Gronwall gives G (20) uniformly through the stopping node. The limiting clock remains at least \(3/100\) below the stopping clock threshold, and the limiting prediction at least \(\rho/2\) below the stopping prediction threshold. Both premature stopping alternatives are thereby excluded with probability tending to one.

Applying the same cubic identity to each fractional raw step controls the prescribed interpolation. For the other parameter blocks interpolation is already linear. Finite GF is identified by its feature flow and scalar clock; its root is below \(3/2\) with probability tending to one because \(f_n(0)\to0\) and \(df_n/ds\ge25/36\). Both actual algorithms are compared to the same finite clipped reference at nearby clocks, which proves the stated same-width state comparison.

The limit is a full-sequence convergence in probability: for a desired error, one first fixes a large clip so the deterministic Gaussian-tail comparison error is small, then fixes a fine mesh, then takes all sufficiently large widths using the fixed-program convergence. Every error estimate has this order of limits. The Fatou subsequences used for moment bounds do not select a subsequence of widths for the final theorem. Joint comparisons on the shared initialization give joint GF/GD convergence as well.

## 10. Observations, velocities, kernels, and path laws — PASS

**Locations:** G 87–109, 541–592; L 1489–1501, 1696–1737.

The state metric directly controls fixed Lipschitz probe programs. Gate-containing backward quantities need the additional argument in the package: the exact middle comparison controls \(\delta^{(2)}\), and the bounded reverse action then controls \(q^{(1)}\). Their finite joint laws converge uniformly in \(\mathcal W_2\).

Multiplication by a bounded continuous gate is continuous for such laws even though it is not globally Lipschitz jointly in an unbounded second factor. To see the required uniform statement, clip the second factor at a fixed level. The resulting operation is approximable by bounded Lipschitz coordinate maps. The discarded normalized \(L^2\) error is bounded by its squared tail. The limiting continuous \(L^2\) path has compact time image and therefore uniformly integrable squared tails; uniform \(\mathcal W_2\) convergence gives the corresponding asymptotic finite uniform tail control in probability. After a bounded operator call the input truncation error is multiplied by at most the operator bound. This proves the observation assertion inductively through any fixed finite named program.

The three formulas G (21) follow by the product rule and rank-one action. In particular the bottom gate occurs twice in the matrix-2 propagation term, and the middle gate occurs once in the matrix-3 propagation term; these powers are correct. They give continuous \(L^2\) velocities and uniformly convergent finite joint velocity laws. The four kernel blocks follow from second moments and their products; predictor, residual, and loss follow from the same joint contractions.

For clarity, the GD interpolation argument does not require uniform coordinatewise smallness of every velocity. On a step, write \(\lambda_k=2(1-f_{n,k})\). The raw first velocity is \(\lambda_k\phi'(z^{(1)}_k)q^{(1)}_k\). Differentiating a recomputed feature inserts its current gate. The difference from the left-node expression is a gate difference times this left-node field. Truncating that field controls the difference by the normalized preactivation step; its remaining tail is uniformly small by the preceding paragraph. Differentiating the next preactivation gives

\[
\dot z^{(2)}(t)
=\lambda_k\delta^{(2)}_k\langle h^{(1)}_k,h^{(1)}(t)\rangle_n
+W^{(2)}(t)[\phi'(z^{(1)}(t))\dot z^{(1)}(t)].
\]

The contraction and matrix changes are small in the established norms, and the remaining gate product is handled by that same truncation. At the next layer repeat with the already established left-node layer-2 velocity, whose squared tails are controlled by its joint-law convergence. This proves the asserted uniform velocity discrepancy without using interpolation-velocity convergence as its own premise. The right-node and terminal-left conventions cause only one-step errors. Uniform convergence of squared speeds then gives convergence of their integrals.

For the path-law statement, measurable \(L^2\) velocities have integrable squared norm over the compact interval. Fubini and integration give almost surely absolutely continuous coordinate versions, with finite expected squared supremum norm. For every such scalar path,

\[
\|z-I_\pi z\|_\infty^2
\le4|\pi|\int_0^T|\dot z|^2.
\]

Applying this bound in empirical average and in expectation controls both finite and population path-to-grid interpolation errors. On a fixed grid, joint \(\mathcal W_2\) convergence of time coordinates implies \(\mathcal W_2\) convergence of their linear path interpolants. Letting the grid size tend to zero proves the claimed \(\mathcal W_2(C([0,T]))\) convergence. Bounded Lipschitz \(\phi\) then transfers it to feature paths. This step uses joint time laws, which the finite-program/common-space construction supplies.

## 11. Initial feature learning and nonconstant kernel — PASS

**Locations:** G 594–710; L 1919–2300 for the underlying expansion method.

The initial forward variances are the full second moments

\[
m_\ell=1+\frac1{100}\mathbb E[\arctan(\sqrt{m_{\ell-1}}G)^2]>1.
\]

The cross term vanishes only by the initial centered Gaussian symmetry; the activation is not centered thereafter.

For the first initial transpose, conditioning on the forward query gives the response \(c_3H^{(2)}_0\) and Gaussian innovation variance \(\mathbb E[(B^{(3)})^2]\). There is no subtraction of the response variance. The displayed coefficient

\[
c_3=\frac1{100m_2}\mathbb E\frac{Z^{(3)}_0\arctan Z^{(3)}_0}{1+(Z^{(3)}_0)^2}>0
\]

is correct: the offset term in \(\mathbb E[Z\phi(Z)\phi'(Z)]\) is odd and integrates to zero initially. The remaining integrand is strictly positive off zero. For the second transpose, conditioning additionally on the entire independent third-layer matrix fixes \(B^{(2)}\) without exposing the residual of matrix 2. This validates the next innovation and the factor \(c_3\) in \(c_2\). It proves strictly positive \(\gamma_1,\gamma_2,\gamma_3\).

Strong continuity and the readout integral give \(W^{(4)}(s)/s\to H^{(3)}_0\), and successive bounded-gate multiplications and actions give \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\). The exact velocity equations then give the second-order state and feature expansions in G. Adjunction yields

\[
\mathbb E[B^{(2)}V^{(2)}]=\gamma_1+\gamma_2>0,
\qquad
\mathbb E[B^{(3)}V^{(3)}]=\Gamma>0.
\]

Thus the leading velocity and feature coefficients are nonzero in all layers. The rank-one matrix expansions are nonzero in Hilbert–Schmidt norm as well.

Expansion of the fourth kernel gives \(m_3+\Gamma s^2+o(s^2)\), while the first three kernels sum to \(\Gamma s^2+o(s^2)\). Since \(s(t)=2t+o(t)\), the total physical kernel is

\[
m_3+8\Gamma t^2+o(t^2),\qquad \Gamma>0.
\]

The physical feature velocity is \(4t\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t)\), giving the claimed \(16/3\) coefficient for the small-horizon squared-speed integral. These are width-independent nonzero limits for the fixed activation, rather than effects vanishing with width.

## 12. Strict nonlinearity and absence of later freezing — PASS

**Locations:** G 712–816.

### Two-sided unbounded hidden support at every reached time

The forward sources have standard deviations between \(m=5/6\) and \(a=7/6\), since their variances are uncentered activation second moments. The response bounds already proved give the following valid dominating errors:

\[
|Z^{(3)}_k-\xi^{(3)}_k|\le\frac{63}{160},
\]
\[
|Z^{(2)}_k-\xi^{(2)}_k|
\le\frac{A\Delta}{10}\sum_{j<k}(|\zeta^{(2)}_j|+a),
\quad \mathbb E R_{2,k}\le\frac{483}{1600},
\]
\[
|X^{(1)}_k-F(Z^{(1)}_0)|
\le\Delta\sum_{j<k}|\zeta^{(1)}_j|+aS,
\quad \mathbb E R_{1,k}\le\frac{1561}{800}<2.
\]

At the top the bound is deterministic and needs no independence of the correction. In the middle, the dominating variable depends only on the backward source group and is independent of the forward source. Markov at threshold 1 therefore gives the multiplier \(1117/1600\) in G (24). At the bottom the dominating variable is independent of the initial root, and Markov at threshold 4 gives a probability greater than \(1/2\). Monotonicity and oddness of \(F\) give the threshold in G (25). The actual corrections need not be independent of the corresponding forward variable or root; only these dominating variables need the independence just verified.

The bounds are uniform in clipping, mesh, and time index. They pass to the flows because the upper and lower half-lines are closed: if \(\mu_j\Rightarrow\mu\), then \(\mu(C)\ge\limsup_j\mu_j(C)\). The Portmanteau direction used in G is correct. Thus both tails remain nonempty arbitrarily far out at every reached time.

### Positive affine-approximation error

Every preactivation is in \(L^2\) and has positive variance. The affine span of \(1,Z\) is a finite-dimensional closed subspace of \(L^2\), so its least-squares minimum is attained and equals G (26). If this minimum were zero, bounded \(\phi(Z)\) and unbounded support of \(Z\) would force zero slope. Strict monotonicity of \(\phi\) would then force \(Z\) to be constant, a contradiction.

The required moments are continuous along the \(L^2\) paths. Thus both the variance denominator and the positive least-squares error have positive minima on each compact physical interval, for each layer and hence simultaneously for the three layers. Uniform joint second-moment convergence passes this lower bound to finite empirical least-squares errors with probability tending to one. This is a rigorous obstruction to effective affine behavior at later times, not just a statement about the activation formula at initialization.

### Nonzero hidden velocities at every positive finite physical time

For every \(s>0\), the readout satisfies \(W^{(4)}(s)\ge ms\) pointwise, so strict positivity of \(\phi'\) gives \(\|\delta^{(3)}(s)\|_2>0\). Along sufficiently accurate fixed-mesh clipped approximations at that time, the Gaussian variance \(\mathbb E[(\delta^{(3)}_k)^2]\) therefore has a common positive lower bound. The approximation can be taken first in mesh for fixed clip and then in clip; all response-shift bounds are uniform in those choices.

Since \(|q^{(2)}_k-\zeta^{(2)}_k|\le a\), a positive Gaussian variance lower bound supplies nonzero arbitrarily distant tails for \(q^{(2)}(s)\) after the same closed-half-line argument. Hence \(\delta^{(2)}(s)\ne0\). Its converging second moment in turn gives a positive lower bound for the \(\zeta^{(1)}\) variance. The bounded bottom response shift then implies \(q^{(1)}(s)\) is unbounded in law and \(\delta^{(1)}(s)\ne0\). This is a sequential positivity argument; no positivity of a lower layer is assumed to prove itself.

Finally,

\[
\mathbb E[\delta^{(2)}(Z^{(2)})']=K^{(2)}+K^{(1)}>0,
\]
\[
\mathbb E[\delta^{(3)}(Z^{(3)})']=K^{(3)}+K^{(2)}+K^{(1)}>0.
\]

Together with \((Z^{(1)})'=\delta^{(1)}\), these prove nonzero preactivation velocities in all layers. A strictly positive gate cannot annihilate a nonzero \(L^2\) variable, so all feature velocities are nonzero as well. The physical multiplier \(2(1-f)\) is strictly positive at every finite physical time. This excludes later freezing throughout the claimed interval, rather than relying only on the small-time expansions.

## 13. Remaining gaps and limits of the verdict

**Remaining fatal gaps: none found. Remaining conditional mathematical premises for the stated theorem: none found.** No repair or counterexample is required for acceptance of this exact package.

The following distinctions are limits of the asserted theorem, not defects or proposed replacements:

- The result concerns the fixed shifted activation. L's old short-horizon numerical constants and its unshifted-activation positivity argument are not imported unchanged. B supplies the new horizon, and G supplies the corrected initial symmetry calculation and later-time arguments.
- Convergence across widths is convergence of the specified joint empirical action laws, including their second moments. Operator-norm convergence is asserted only for comparisons on the same finite spaces or the same constructed population spaces.
- Uniqueness and restart concern continuous bounded-primal integral solutions on the common generated spaces, with the specified initial or reached state. The argument covers raw competitors in that class. It does not claim arbitrary-state global existence or uniqueness across unrelated realizations of population spaces.
- Initial hidden velocities vanish because the limiting initial readout is zero. The proved second-order onset and the nonzero velocities at every positive finite time satisfy the feature-learning claim. Strict affine-approximation error also holds at initialization.
- The total kernel is proved nonconstant. Global monotonicity of that kernel, or a uniform positive lower bound on hidden speeds as physical time tends to infinity, is not asserted or needed.
- Every fixed finite physical horizon is covered. No interchange between infinite training time and infinite width is proved.

**Final verdict: PASS for the complete theorem at the three hashes listed above.** The generic adaptation, both reused transposes and current-time returns, common actions and adjoints, numerical response closure, removal of clipping, raw uniqueness/restart, actual GD and interpolation, full-sequence measured/path/velocity/kernel convergence, and finite-time nonlinearity and nonfreezing all have valid supporting arguments in the permitted package.
