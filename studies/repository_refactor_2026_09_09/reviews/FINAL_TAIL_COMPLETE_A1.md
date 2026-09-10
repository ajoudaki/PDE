**All three candidates pass the mathematical audit within their stated scopes.** I found no substantive mathematical error or unresolved specialized dependency. There is one wording correction in the long dependency: it reverses the comparison between two input assumptions. That correction does not change a theorem or its proof.

The separate verdicts are:

| Candidate | Verdict |
|---|---|
| **LAST A–I** — `FINAL_LAST_ADDITION.md` | Pass. Positive, conditional and negative results are justified, with the initialization and reachability distinctions stated below. |
| **SCOPE A–E** — `FINAL_SCOPE_ADDITION.md` | Pass. The formal, conditional, vanishing-time and actual positive-time conclusions remain distinct. |
| **SHALLOW** — `FINAL_SHALLOW_RATE_ADDITION.md` | Pass. The quantitative continuous-flow rates follow from the fully checked shallow characteristic dependency. |

## Required correction

In [FINAL_LAST_DEPENDENCIES.md:1656](/tmp/pde_final_tail_a_a8d7_3gt/FINAL_LAST_DEPENDENCIES.md:1656), replace:

> “The stronger one-sided condition (III.M.1) is sufficient”

with:

> “The weaker one-sided assumption (III.M.1) is sufficient.”

The two-sided restriction
\[
-1+\delta<G_{ij}<1-\delta
\]
implies the one-sided restriction \(G_{ij}\le1-\delta\), not conversely. For example, an antipodal pair together with a perpendicular third unit vector satisfies the one-sided restriction for \(0<\delta<1\), while the antipodal correlation violates the two-sided restriction. The theorem under the one-sided assumption is therefore **more general**, while its assumption is **weaker**.

The displayed hypothesis and the geometric proof use the correct one-sided restriction throughout. This is a wording correction, not a gap in the result.

## Complete dependency audit

### Shared notation and finite model

I checked all 98 lines of `NOTATION.md` and lines 8–213 of the long dependency.

The normalization is internally consistent:

- The stored first matrix uses \(W^{(1)}x/\sqrt d\); the alternate storage \(V^{(1)}=W^{(1)}/\sqrt d\) produces the metric \(d\|dV^{(1)}\|_F^2/n\).
- The stored readout appears as \(C^Th/n\).
- The backward vectors are residual-free and satisfy \(\delta^{(\ell)}=n\,\partial f/\partial z^{(\ell)}\).
- The first/readout mobilities are \(n\kappa_\ell\), while middle-matrix mobilities are \(\kappa_\ell\).
- The rank-one population operator \(U\otimes V\) corresponds to \(uv^T/n\), whose ordinary finite Frobenius norm matches the Hilbert–Schmidt norm under normalized vector pairings.

The gradient formulas, all kernel blocks, their positive semidefiniteness, and
\[
\dot f=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr
=-\|D^{-1/2}\dot\theta\|^2
\]
have the correct factors.

The global finite-GF proof is valid even without bounded activations: nonnegative loss and the energy identity give a Cauchy parameter endpoint at any hypothetical finite escape time. Local Lipschitzness then permits continuation. This does not establish global GD stability, and the text does not claim it.

The width-uniform RMS bounds require bounded activation derivatives, fixed depth, bounded initial operator/RMS norms and bounded initial loss. The forward/backward inductions verify precisely those hypotheses. The Gaussian net argument supplies the required initial event without invoking a sharp spectral-edge theorem.

### Complete special-data Part II

I checked lines 219–1629, including all of II.A–II.D.

**Finite geometry and symmetry.** The four raw kernel matrices and summed-loss factor are correct. The \(G^{-1}\) first-field metric is used only for \(-1<\rho<1\); the antipodal endpoint uses the preserved subspace \((Z,-Z)\). Input reflection is a raw-metric isometry. Finite exchange symmetry is correctly an equality in law, becoming an equality of deterministic limiting predictions only after the finite-program limit.

The label-mode feature field has the required factor \(1/2\), and the summed-loss clock is
\[
\frac{ds}{dt}=4(1-g).
\]
The actual finite residual pair is not assigned this clock.

**Two-query response estimate.** The scalar laws retain both samples, every current transpose response and all zero-variance formal slots. The forward coefficients are constructed before the current reverse coefficients that depend on them. Thus the induction does not assume its own unknown current-row bound.

I checked the sensitivity recurrences, Gaussian exponential estimates and numerical margins. In particular,
\[
\frac{49}{36}+\frac3{25}=\frac{1333}{900}<\frac32,
\]
and the stated bounds
\[
V_*\le\frac{3067}{3200}<1,\qquad
U_*\le\frac{71063018523}{73728000000}<0.97
\]
close the induction. The exponential-square query bound uses a bounded response correction, not independence of that correction from its Gaussian source.

**Construction and approximation.** At fixed caps, the bounded readout and clipped products satisfy the finite-program hypotheses. The asymmetric field comparison costs \(C(1+R)\), rather than a power \(R^L\). Only the reference requires tail control. Its error
\[
e^{CR}\,e^{-R^2/256}\longrightarrow0
\]
is sufficient for strong cap removal, uniqueness against bounded-primal competitors and restart from reached states.

The scalar predictor is continuously Fréchet differentiable even though an \(L^2\)-valued activation map need not be. The weighted Taylor-remainder argument and strong multiplier continuity justify this distinction.

For equal labels,
\[
g_s\ge25/36
\]
forces a crossing \(g(s_*)=1\) before \(36/25<3/2\). Bounded \(g_s\) makes the physical-time integral diverge at that crossing. This proves global physical flow and the stated exponential population fitting rates.

The finite GF/GD comparison controls the off-mode residual explicitly. Raw GD is simultaneous Euler in raw parameters. Stopping includes the first possible overshooting node. The stated \(n^{-2}\) step makes the recomputed within-step velocity errors vanish.

**Observables.** The ordered observation clipping, compact \(L^2\) reference tails and separate mesh/cap limits justify the backward and velocity laws, uniform squared speeds, kernel entries and integrated energies. Fixed-grid joint laws plus
\[
\|z-I_\pi z\|_\infty^2
\le4|\pi|\int_0^T|\dot z|^2
\]
supply the claimed \(\mathcal W_2\) path laws. Rank-one cross-time contractions justify increment norms without comparing operators across widths.

**Nonaffinity and motion.** The independent displacement dominators and Gaussian rectangles give forward separation and unbounded marginal support. Bounded strictly monotone activation then excludes an almost-sure affine fit. The backward rectangle and signed-quadrant arguments establish positive-definite backward second-moment matrices. The trace-product and telescoping identities prove every claimed positive hidden speed, including \(\rho=-1\).

The initialized transpose formulas are justified by derivative-valid clipping. The expansion
\[
K_g(s)=\|V_0\|^2+2\Gamma s^2+o(s^2)
\]
and its physical coefficient \(32\Gamma t^2\) have the correct clock factors.

### Complete special-data Part III

I checked lines 1635–4510, including III.M, III.F, III.S, III.G, III.V, III.N and III.A, whether or not a particular candidate invokes each part.

**Model and normalization.** The half-summed loss has coefficient one in the raw updates. The normalization changes hidden fields only:
\[
f_i=a^LF_i,\qquad \nabla_{\rm raw}f_i=a^L\nabla_{\rm raw}F_i.
\]
It does not rescale stored readout or replace the raw metric. The true backward scaling and all \(a^{2L}\) kernel factors are consistent.

**Finite Gaussian foundation, III.F.**

- Adaptive conditioning is justified instruction by instruction. Conditioning on one matrix answer updates only that matrix’s residual Gaussian factor.
- The displayed conditional mean satisfies both forward and reverse constraints and is orthogonal to the homogeneous constraint space.
- The removed Gaussian projection has normalized mean-square size \(\operatorname{rank}(U)/n\).
- Conditional averaging establishes weak convergence and second moments; the supplied transport argument upgrades them to \(\mathcal W_2\).
- Gaussian integration by parts cancels the regression terms and produces the stated source-response formulas.
- Source covariances are full input second moments. Independence belongs to oriented source groups, not to matrix answers and adaptive inputs.
- Singular queries are handled by fresh input perturbations, same-array Lipschitz comparison and continuity of finite covariance square roots. No continuity of pseudoinverses is assumed.
- Expected derivative convergence follows from continuous bounded first derivatives at a fixed transcript; it is not inferred from value convergence alone.
- Causal scalar feedback is restored through convergent contractions and bounded RMS norms.
- The countable generated construction supplies dense domains, bounded actions and genuine adjoints. The density argument and passage of transpose pairings are sufficient.
- Hilbert–Schmidt completeness, rank-one identities, strong multiplier continuity and curve chain rules support the state construction.
- The scalar predictor and scalar feature-energy differentiability proofs control weighted remainders without asserting an invalid ambient Nemytskii derivative.

These arguments establish the foundation internally.

**Controlled source bounds, III.S.** The independent primal bootstrap closes before the response induction uses it. The Gaussian-part elimination uses the actual frozen coefficient arrays, retaining the offset term. The moment absorption and source-derivative recurrences include current reverse returns.

The chosen boxes have sufficient slack: the bounds on \(\alpha_\ell S\), \(\alpha_\ell Sb_\ell\) and \(\alpha_\ell SM_{\rm src,\ell}\) support the exponential estimates and both production inequalities. The chronological forward-then-backward construction avoids circular current-row assumptions. These are marginal moment bounds; no temporal independence or random time-maximum estimate is silently used.

**Geometry, clock and nonaffinity, III.G.** The proof of
\[
G+\mathbf1\mathbf1^T\succeq\delta^2I/4
\]
works at singular input Grams. Gaussian constant/linear projection gives the initialized Gram floor. Boundedness of \(\psi\), through integration by parts, makes the layerwise losses summable.

The controlled displacement, forward perturbation and hidden-response estimates have the correct powers of \(a\) and \(32\). The selected gain makes the top Gram perturbation and possibly nonsymmetric capped hidden contribution smaller than \(\lambda/4\). Consequently the capped residual estimate is valid without treating the capped field as a gradient.

The total control clock stays below \(S/2\), closing continuation. The bounded-control approximation is in \(L^1\), rather than unjustified pointwise sampling of measurable controls.

The affine-regression stability inequality follows from the optimal slope bound \(|c_X|\le1\). The finite-interval Gaussian density estimate and the selected gain preserve the stated all-time nonaffinity margin.

**Population, finite algorithms and observables, III.V.** The one-cap-factor recursion, reference-only tails and strong derivative convergence justify uncut existence and uniqueness. Fixed-cap primal events precede the probe arguments that use them. Gaussian probes correctly bound expected derivative rows, and the subsequent recurrences bound pointwise source rows.

The ascending velocity-query proof supplies its derivative-valid extension through nested clipping. The descending true-backward proof requires only the established second-moment tails. Uniform-time limits use the correct order of width, mesh, training cap and observation threshold. Raw-GD directions remain preceding-node directions, with hidden quantities recomputed along interpolation. The full path, kernel, velocity and integrated-energy claims follow in their stated topologies.

**Initial motion, III.N.** The forward Grams are positive definite under the augmented-input argument. At the top, nonconstancy of bounded \(\psi\) forces \(\phi''\not\equiv0\), which is enough for strict backward-Gram positivity. Conditional Gaussian covariance propagates this positivity downward.

The upper-layer innovation variance is regression against the original feature span without an intercept; its conditional-variance lower bounds are valid for that exact span. The coherent clipping program proves the required reverse and added-forward formulas before removing the clips. The raw hidden acceleration is \(9\mathscr V\), and the total kernel coefficient is
\[
18\|\mathscr V\|_{\rm hidden}^2.
\]

**Activation classes, III.A.** The common interval-margin gain, compact-support obstruction to depth-uniform nonaffinity, distinct-tail-limit argument and open \(C_b^2\) ball construction all check out. The arctangent-center derivative maximum is correct. Disjoint translated bumps establish infinitely many independent directions. Uniform class constants do not imply uniform finite-width convergence over the class.

### Complete linear dependencies

I checked lines 4514–4861.

The compact singular expansion, approximation-number formula, trace-norm triangle inequality and completeness proof are sufficient. The ideal inequality, trace cyclicity and Hilbert–Schmidt statements follow from absolutely convergent singular expansions. The finite-Gram singular-value formula uses partial isometries and remains valid at singular Grams. The rank-\(m\) approximation inequality controls the full trace-norm tail.

The Gaussian-word proof establishes Wick’s identity internally. Its index count gives \(n^{v-k-1}\); only tree quotients survive, and these correspond exactly to matching-label, opposite-transpose noncrossing pairings. The creation/annihilation construction realizes those pairings. Connected two-trace diagrams give vanishing variance. Independent Gaussian-root quadratic/bilinear calculations then prove the rooted laws. The orthogonal direct sum supplies orthogonality of entire rooted subspaces.

The reference to `gaussian_calculus.md` is redundant: the immediately preceding moment-generating-function proof supplies the needed identity. I did not access that file or rely on its contents.

## LAST A–I: findings and scope

### A — Trained-affine strong/weak mixing

**Pass.** The reference is the actual all-block affine flow with zero readout and half-summed loss. Its polynomial Hilbert-space field supports the local smooth expansions.

The hidden parameter changes and trained variance coefficients
\[
(d_1,d_2,d_3)=(1,3,6)
\]
retain both trained matrix increments. The needed trace values \(1,2,3,2\) are justified by the checked word dependency and uniform integrability.

The exact null decomposition \(v^Tf_e=eN_{v,e}\) holds on the entire raw state space. Gaussian integration by parts at the evolving affine state gives
\[
N_v(t)=10m'(1)\sum_i v_i(\Gamma y)_i^3t^3+O(t^4).
\]
For the displayed triple the cubic contraction is \(7/2+5/\sqrt2>0\). The null-row gradient identity therefore proves order-\(e\) mixed coupling at sufficiently small positive reference times, despite order-\(e^2\) initialization.

This is not an unproved nonlinear trajectory comparison or a refutation of a correctly scaled Schur argument.

### B — Conditional sub-exponential construction

**Pass as a conditional theorem.** Hölder’s estimate yields the one-reference modulus
\[
D\log(e^2/D),
\]
whose reciprocal diverges at zero. The backward and raw-block bounds have sufficient constants.

The cap-error estimate uses actual capped incoming fields. Approximate energy, rather than a false capped-gradient identity, prevents escape from the chosen radius. The Osgood comparison makes cap states and derivatives Cauchy; Fatou transfers the assumed moments to the limit and supports uniqueness and reached-state restart.

The required cap-uniform \(Kp\) moment premise is not proved here. Neither finite GF/GD identification nor nonaffinity follows from this implication alone.

### C — Strong Gaussian-norm obstruction

**Pass.** For every positive perturbation size,
\[
x\bigl[g(1+\varepsilon x)-1/2\bigr]/x\longrightarrow-1/2
\]
in the tails, making the exponential-square integral infinite below the stated threshold. Thus the gate fails continuity in the ordinary strong \(\psi_2\) norm, while converging in every fixed finite \(L^p\).

The \(\psi_2\times\psi_2\to\psi_1\) product estimate is valid without independence. Its loss of exponent does not close a same-space contraction. The conclusion concerns this norm-based method, not population nonexistence.

### D — Signed-response focusing and raw-ball Hessian curvature

**Pass.** The pulse construction preserves the instantaneous three-query Gram \(I\), bounded values and uniform temporal \(H^1(L^2)\) norms. Its whitened Gaussian observation is causal. Transport cancels the common baseline and produces the normalized trigonometric sum.

The interval near \(x=1/2\) proves divergence of every fixed \(L^p\), \(p>2\), and of the \(\psi_1\) norm, as well as failure of uniform square-tail integrability. The time-step representation does not supply a bounded response density.

The separate raw-state construction has unit raw displacement and a unit rank-one test direction. Its negative residual curvature grows as \(\varepsilon^{-1/2}\), while the positive predictor-gradient term remains bounded. Both constructions explicitly lack canonical reachability claims.

### E — Stationary-state metric obstruction

**Pass.** The scalar transform is valid for the prescribed toy system. The row-field bracket has nonzero real linearization eigenvalues, excluding simultaneous Killing-field cancellation. The inverse feature metric fails the displayed Hessian integrability condition when an inverse-Gram off-diagonal entry is nonzero.

The equal-elasticity lemma follows from opposite signs of the small- and large-scale differences. Applying it three times gives every stationary cancellation. The modified initialized actions differ by finite-rank operators of uniformly bounded Hilbert–Schmidt norm. The resulting states are exact full-gradient stationary points with nonzero loss below \(3/2\).

The two-valued submanifold is invariant. Unit-direction curvature tends to \(-\infty\), so the restricted GF linearization has eigenvalues tending to \(+\infty\). At a stationary point the derivative-of-metric-along-flow term vanishes; any smooth positive metric must therefore have a differential one-sided bound at least as large as those eigenvalues. Uniform metric equivalence is unnecessary.

The obstruction applies to the common ambient ball, not to the canonical trajectory.

### F — Global two-hidden-layer Gaussian-readout flow

**Pass.** This is the distinct order-one stored-readout model, with one sample, bounded activation, positive tame gate and full-square flow with multiplier \(\eta\).

The natural coordinate satisfies \(\iota'=c\), \(\psi'=c^2\), and preserves the original optimizer. All three raw kernel terms are correct. The non-Gaussian root tuple \((u_0,\Theta(u_0))\) is permitted by the finite-program theorem.

Trace-class rank-one integrals, bounded readout increments and Gaussian initial tails establish global feature flow on both signs of feature time. The Gaussian-envelope Osgood modulus supports uniqueness in the stated class. The two mesh limits provide square-tail control before passing the kernel multiplier.

The physical clock uses the true finite initial error \(y-f_n(0)\), and converges on every fixed physical horizon. The arctangent and reciprocal-polynomial examples meet the hypotheses.

No raw-GD theorem, full hidden-velocity bundle or asymptotic fitting result is established here.

### G — Equal-label sech-gate transfer

**Pass.** The new activation satisfies every value, slope and curvature bound used by II.B–II.C. The two formula-dependent substitutions—feature separation and top gate-ratio rectangles—are proved explicitly.

Consequently the global equal-label flow, fitting rates, raw GF/GD approximation, observables, nonaffinity and positive motion transfer. The initialized transpose argument separately verifies the quadratic feature and kernel coefficients.

The result includes the antipodal endpoint and either equal-label sign. It supplies no opposite-label global theorem.

### H — Fixed-sign prescribed controls

**Pass.** Integrable controls and bounded spatial derivatives justify the characteristic and its initial-state derivative. Reflection converts the sign premise into nonnegative controls with correlation \(r=\rho s_1s_2\).

The \(C_r^{-1}\) energy identity, truncated potential and monotone sum coordinate bound the adverse energy integral. The treatment of flat boundary-level segments is valid. The choice \(Q=2\log(e+U)\) gives the claimed polynomial estimate.

The random-control consequence requires the displayed moment of \(U\). These are frozen-control derivatives; feedback-induced control variations are outside the result.

### I — First-Euler neighborhood obstruction

**Pass.** The construction uses an exactly zero-readout auxiliary initialization and a fixed proof step. Gaussian conditioning gives the actual transpose answer with a nonzero innovation. Joint empirical convergence supplies arbitrarily large query coordinates on the required gate interval.

The rank-one perturbation changes one second-layer preactivation by \(A^{-1}\), has norm \(O((A\sqrt n)^{-1})\), and creates a velocity difference bounded below by \(O(n^{-1/2})\). Residual and reverse-field changes have the smaller controlled errors. The Lipschitz ratio grows linearly in \(A\).

The threshold is chosen before width tends to infinity. This excludes the stated width-uniform neighborhood estimate; it does not establish continuous-trajectory failure or nonuniqueness.

## SCOPE A–E: findings and scope

### A — Tanh vanishing-time continuity

**Pass.** Order-one readout is retained. The initialization reverse-response coefficients vanish after the stated centered clipping, giving the correct \(s_j\) and \(K_0\).

Conditional Gaussian bounds supply the initial exponential-square averages and maxima. The entropy/Jensen multiplier inequality transfers these initial tails through the backward chain without iterating logarithms. The residual clock then proves continuity for every deterministic \(t_n\downarrow0\).

For \(y=0\), the initial residual is \(O_{\mathbb P}(n^{-1/2})\), so every fixed physical horizon occupies a vanishing feature interval. This proves the stationary limiting conclusion.

Both tanh balance identities and the inverse-gate RMS bound are correct. Those bounds do not imply uniform square tails of the ungated query, as the stated static example demonstrates. No fixed-positive-time nonzero-label theorem follows.

### B — Sin-plus-cosine initialization and formal coefficients

**Pass.** Product-to-sum identities give the exponential covariance map with unit diagonal. Tensor powers and polynomial interpolation prove positive definiteness for distinct inputs, including singular input Grams.

Both transpose-response matrices \(J_3,J_2\) have the correct signs from \(\phi''=-\phi\). The unbounded intermediate product is justified by derivative-valid clipping. The innovation and tensor-product arguments prove strict positivity of all \(R_j\) and hidden kernel coefficient matrices.

The total formal label-kernel coefficient includes the equal readout contribution, giving the factor two. The trigonometric Gaussian formula and \(1-2/e\) regression error are correct.

These are initialization and formal coefficient identities, not analytic trajectory expansions. The separate one-node Gaussian calculation correctly disproves the proposed uniform \(Kh\,e^{Khp}\) bound.

### C — Fixed-offset affine reference

**Pass.** This is a given-space polynomial Hilbert ODE, with arbitrary bounded initialized actions and half-summed loss. Energy gives global existence and strong continuation.

The canonical initial Grams \(G+\ell\mathbf1\mathbf1^T\), full kernel and augmented-Gram lower bound are correct. The offset terms produce exactly the displayed balance defects; only the compressed balances are invariant.

The stationary prediction classification follows from the raw stationarity equations and affine independence of three distinct unit inputs. The mixed-label loss threshold is \(4/3\).

The fitting result requires both positive raw input Gram and entry below that threshold. The residual-length clock gives the logarithmic bound and a finite strong endpoint; a positive kernel floor then yields physical-time exponential fitting. Neither hypothesis follows from pairwise separation alone.

### D — Same-array Gaussian values and residual coordinates

**Pass as an auxiliary implication.** Both \(AB\) and \(BA\) are strictly causal. The inverse row bounds remain valid when old columns of \(B\) concentrate; the proof does not incorrectly give \(AB\) a column-density bound.

Exact elimination at the same arrays gives the Gaussian parts and nonlinear remainders. Actual second-moment bounds control their Gaussian variances, and the discrete Volterra inequality gives the stated \(C\sqrt p\) estimates without a smallness assumption.

The three-input eigenvalue statement, initialized Gaussian projection recursion and order-\(\varepsilon^2\) mixed-block bounds are correct. The transformed residual equation retains \(\dot L\). The readout projection identity retains the offset and moving orthogonal subspace.

This lemma does not prove its response bounds or capped second-moment premises, nor a trained Schur floor.

### E — Actual positive-time failure of raw-Hilbert local Lipschitzness

**Pass.** Unlike the ambient counterexamples in LAST, this result concerns reached local population states.

The sech substitution satisfies the Part-II local construction hypotheses for either label pair. Symmetry gives \(f_a=y_ag\) at the base trajectory; the physical clock is positive on the selected short interval.

The top-delta increment estimate produces a Gaussian source-path bound uniform in mesh and cap. Regression on the terminal reverse source gives a large query while controlling the entire reverse path. Independently regressing the forward source leaves its terminal residual exactly zero. The bounded correction and Lipschitz dependence on that scalar source put the terminal preactivation in any prescribed positive-length interval with the claimed Gaussian lower bound.

Only positive scalar variances are inverted. The closed inner event permits both limit passages. No independence between the evolved preactivation and query is asserted.

The feature-Gram dual isolates one sample under a unit rank-one perturbation. Individually bounded directions justify the second directional derivative. Bounded readout controls the top curvature term without an \(L^4\) requirement on its propagated direction. The middle multiplier has both unbounded signs, while squared first predictor derivatives remain uniformly bounded.

The summed-loss identity
\[
-D^2\mathcal L[v,v]
=4(1-g)D^2g[v,v]-2\sum_a(Df_a[v])^2
\]
therefore proves unbounded curvature of both signs and failure of local Lipschitzness of the raw gradient. This is compatible with the separately established local strong existence and uniqueness. No opposite-label global continuation or finite-width positive-time Hessian limit is claimed.

## SHALLOW: complete verdict

**Pass.** I checked all 215 dependency lines and all 161 candidate lines.

The dependency proves global feature characteristics on both signs of time under \(C^2\) activation with bounded first and second derivatives and linear growth. Its quadratic observable envelopes and cubic derivative envelopes justify differentiation under expectation. The monotone predictor gives the global physical clock for any label and \(\kappa\ge0\).

The uniform empirical argument uses finite nets and an integrable random Lipschitz envelope. Its fourth-moment calculation supplies almost-sure convergence under the nested iid coupling, and hence the intrinsic convergence in probability. Restart retains the full marked pair and its consistency relation, not merely \((f,K,r)\).

For the quantitative candidate:

- The integral identity for the empirical predictor error gives second and fourth supremum moments of orders \(n^{-1}\) and \(n^{-2}\).
- On \(|F_n(0)|\le1\), both clocks lie in a deterministic compact interval, so deterministic-clock stability transfers those rates.
- On the complementary event, actual residual monotonicity bounds the output error by \(4|F_n(0)|\). This avoids uncontrolled random-clock growth.
- The loss estimate follows from the output’s second and fourth moments.
- For bounded \(\phi\), explicit characteristic displacement bounds and the eighth-moment sample-mean estimate give the particle-path rate. Exchangeability then gives joint convergence of any fixed finite particle family to independent limiting paths.

Thus the asserted output, variance and loss rates hold for the stated possibly linearly growing activations. The particle-path rate additionally requires bounded activation. All conclusions concern fixed-horizon continuous GF; there is no raw-GD, kernel-rate, growing-depth or fitting conclusion.

## Reading, isolation and integrity attestation

I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and **every line of all six scientific inputs**, including both complete dependencies. Numbered bounded reads covered every scientific line; no truncated scientific output was left unresolved.

| Scientific input | Lines |
|---|---:|
| `FINAL_LAST_ADDITION.md` | 2,229 |
| `FINAL_SCOPE_ADDITION.md` | 1,256 |
| `FINAL_SHALLOW_RATE_ADDITION.md` | 161 |
| `FINAL_LAST_DEPENDENCIES.md` | 4,861 |
| `FINAL_SHALLOW_RATE_DEPENDENCIES.md` | 215 |
| `NOTATION.md` | 98 |
| **Total** | **8,820** |

Scientific content reads were restricted to those six files. I also read `INPUTS.json`, the explicitly required skill, and directory-entry metadata. I did not read logs, events, prompts, history, prior audits, reviews, verdicts or other scientific files. I did not access `/home/amir/Codes/PDE`, Git, network resources or external sources. I used no memory, delegation, experiments, simulations or implementation tests. All tool operations were read-only; no files were written or modified.

The final SHA-256 hashes match all six exact starting hashes in `INPUTS.json`:

```text
FINAL_LAST_ADDITION.md
bb28eb597f0e6a230e90674eb379e2a901e2038f8aa1138b1e236e137c212976

FINAL_SCOPE_ADDITION.md
b85476dd8886365c292de1cd19463f988971d6f472800d838a8a1cd6d7b166d6

FINAL_SHALLOW_RATE_ADDITION.md
0adf42cdd2cfa3328a7e21f6e72eb4a9a2f5311a4da05edff3b71130564d11b8

FINAL_LAST_DEPENDENCIES.md
e27b438b599b7e8554f05cca455e9b20913ac06bea5342cb845151e0b8e8aecf

FINAL_SHALLOW_RATE_DEPENDENCIES.md
ec3f238c98356de7ee4311e7cdaff5da6cfca359cf0612b1472cb98165830f35

NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
```