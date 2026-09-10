**Independent complete mathematical audit**

I found **no required mathematical corrections within the expressly stated scopes**. The three candidate verdicts are separate:

| Candidate | Verdict |
|---|---|
| `FINAL_LAST_ADDITION.md`, A–I | Clean within each part’s stated scope, including B’s unproved moment premise and the explicit limitations on its negative results. |
| `FINAL_SCOPE_ADDITION.md`, A–E | Clean within the stated initialization, formal-coefficient, conditional, and local-trajectory scopes. |
| `FINAL_IDENTITY_UNIFORM_ADDITION.md`, §§1–8 | Clean for separately fixed finite identity depth, fixed-program width limits, the subsequent local feature-time limit, and the deterministic obstruction in §8. |

These verdicts include examination of the complete supplied dependency proofs. They do not presume correctness from the dependencies’ theorem statements or their descriptions of themselves.

**Reading, isolation, and integrity**

I read every line of all five scientific inputs:

| File | Lines read |
|---|---:|
| `FINAL_LAST_ADDITION.md` | 2,229 |
| `FINAL_SCOPE_ADDITION.md` | 1,256 |
| `FINAL_IDENTITY_UNIFORM_ADDITION.md` | 1,032 |
| `FINAL_LAST_R2_DEPENDENCIES.md` | 4,861 |
| `NOTATION.md` | 98 |
| **Total** | **9,476** |

The reads used consecutive bounded, line-numbered ranges. None of the returned displays was truncated; there was no unresolved omitted display.

I also read `INPUTS.json` and the specifically required `/etc/codex/skills/solve-math-rigorously/SKILL.md`, and inspected directory metadata. I did not read other scientific files, project history, previous audits or verdicts, `EVENTS.jsonl`, `PROCESS.log`, or `PROMPT.txt`. I did not access `/home/amir/Codes/PDE`, Git, network resources, external sources, or memory. I used no delegation, experiments, simulations, or implementation tests. The only computational mathematical checks were bounded exact arithmetic. I issued no file-writing operation.

This attests to the allowed-input isolation actually observed; it does not claim that outside files were physically inaccessible or independently certify how the parent process was created.

All starting hashes matched `INPUTS.json`. The final hashes also match, as recorded below.

**Shared model and normalization audit**

`NOTATION.md`, lines 10–42 and 70–98, consistently distinguishes:

- hidden depth from sample count and width;
- first storage \(W^{(1)}\) from \(V^{(1)}=W^{(1)}/\sqrt d\);
- residual-free backward fields from residual-weighted training directions;
- tiny stored readout variance \(n^{-2}\) from order-one stored readout variance;
- physical time, feature time, actual GD step, and auxiliary proof mesh;
- same-population pairings from cross-layer operations;
- bounded initialized actions from Hilbert–Schmidt or trace-class learned increments.

The finite dependency, lines 8–213, establishes the advertised metric identities directly. In particular,
\[
\nabla_{W^{(1)}}f_a=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},
\qquad
\nabla_{W^{(\ell)}}f_a=\frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n},
\]
and the stored readout derivative is \(h_a^{(L)}/n\). Applying the stated mobilities produces the displayed updates and all kernel blocks.

For mean-square loss, the factors \(2/m\) in prediction evolution and \(4/m^2\) in dissipation are correct. The half-sum and unhalved-sum candidates explicitly change those factors. The finite global-existence proof correctly uses the nonnegative loss and integrated squared raw speed to obtain a Cauchy endpoint. The width-uniform estimates give RMS and operator bounds at fixed depth; they do not supply multiplier continuity or uniform square tails by themselves.

**LAST: separate audit of A–I**

**A — Evolving affine reference and first-order mixing, lines 19–262.**

The model is three hidden layers, unit input directions, zero population readout, all four raw blocks trained, and half-summed square loss. The first-layer Gram factor in the flow is correct.

The local affine vector field is polynomial on the first-row/Hilbert–Schmidt/readout space. Its local strong solution and smooth time expansions are justified. The Gaussian character of the affine same-layer fields follows from finite affine transcripts and strong passage to the flow, without requiring sample symmetry.

I checked the second-order changes of both action maps as well as the first field. The required initialized contractions give
\[
(d_1,d_2,d_3)=(1,3,6).
\]
The trace values \(1,2,3,2\) used for these coefficients agree with the supplied Wick proof and the displayed conditional fourth-moment computation.

The exact null decomposition retains all three nonlinear insertions. Gaussian integration by parts, combined with the exact affine null cancellation, gives
\[
N_v(t)=10m'(1)\sum_i v_i(\Gamma y)_i^3\,t^3+O(t^4).
\]
The coefficient \(10=1+3+6\), the sign \(m'(1)<0\), and the derivative coefficient \(30\) are correct. For the displayed triple,
\[
\sum_i v_i(\Gamma y)_i^3=\frac72+\frac5{\sqrt2}>0.
\]

The first-order kernel identity follows from the identically zero affine null predictor on the whole raw state space. Strong convergence of the relevant gradients suffices; the proof does not require a nonexistent general second Fréchet derivative of an \(L^2\)-valued activation.

**Clean conclusion:** initialization has an \(O(e^2)\) mixed block, whereas evaluation along the actual evolving affine reference gives a nonzero order-\(e\) mixed block at sufficiently small positive times. This does not establish a global nonlinear flow or disprove a Schur method retaining its moving coupling.

**B — Conditional sub-exponential construction, lines 265–627.**

The premise is explicitly a uniform \(Kp\) moment bound for the **actual incoming fields of reachable capped paths**, stopped on prescribed raw balls. It is not derived from energy.

The Hölder multiplier estimate has exponent \(1-1/p\). The asymmetric subtraction puts the moment requirement only on the reference factor. The backward recurrence and the four raw-block bounds are sufficient for the constant \(300KB_0^8\).

Choosing \(p=2+\log(1/D)\) produces
\[
\omega(D)=D\log(e^2/D),
\]
whose reciprocal has divergent integral at zero. The scalar comparison and its stated bootstrap restriction are correct.

The cap tail
\[
\|q-\tau_R(q)\|_2\le4K e^{-R/(4eK)}
\]
follows from the moment premise. Cap-error propagation uses capped incoming moments, not an unstated moment bound on the uncut recursion at the capped state.

The approximate-energy identity has the correct sign:
\[
\mathcal L'
=-\|F_R\|^2+\langle F_R-F,F_R\rangle.
\]
It closes the proposed displacement ball for sufficiently large caps. Direct cap-to-cap Osgood comparison then gives uniform convergence of paths and derivatives. Strong identification, Fatou, and comparison with the reference establish the claimed uniqueness and reached-state restart.

**Clean conclusion:** the global strong-flow implication is proved conditionally. Finite GF/GD identification and regression-error claims remain outside this result, as the text states.

**C — Orlicz obstruction and norm loss, lines 630–698.**

For fixed \(\varepsilon>0\),
\[
x\bigl(g(1+\varepsilon x)-1/2\bigr)/x\longrightarrow-1/2.
\]
The Gaussian integral therefore diverges for every proposed \(\psi_2\) scale below \(1/\sqrt2\). The lower bound, including multiplication by the nonlinear amplitude in the actual gate, is correct. Dominated convergence still gives convergence in every fixed finite \(L^p\).

The \(\psi_2\times\psi_2\to\psi_1\) product inequality uses Cauchy–Schwarz and needs no independence.

**Clean conclusion:** the gate is not continuous in the specified strong sub-Gaussian norm on the displayed bounded ball. This excludes the stated direct same-space contraction argument, not population existence or uniqueness.

**D — Focusing and raw-ball Hessian obstruction, lines 701–968.**

For D.1, the pulse supports, orthonormality, pointwise query bounds, and integrated derivative estimate are consistent. Alternating coefficients cancel the shared Gaussian component exactly, leaving a standard normal observation. The transported response has squared \(L^2\) norm \(\beta(t)^2\), matching the covariance-weighted derivative norm.

On an interval of probability \(1/(3N)\), its size is at least \(\beta(1)\sqrt{N/2}\). This proves the stated \(L^p\) divergence, \(\psi_1\) lower bound, and failure of uniform square-tail integrability. The causal step-factor observation correctly notes that its density coefficients grow with \(N\).

For D.2, the initialized orthogonal-input covariance, normalized indicator readout, and unit rank-one direction are valid. The first-derivative contribution is bounded, while
\[
\phi_\theta''(z)\ge4\theta/25\quad(-2\le z\le-1)
\]
makes the residual-curvature term tend to \(-\infty\). The one-dimensional differentiations are justified for each fixed indicator concentration.

**Clean conclusion:** both are valid insufficiency results. Neither construction is asserted canonically reachable.

**E — Stationary-state metric obstruction, lines 971–1280.**

The scalar transform and its inverse are globally Lipschitz because the gate lies in \([a,1]\). The transformed toy field is globally Lipschitz. The row-field bracket derivative has the stated nonzero real eigenvalues, which contradict the skew-adjoint derivative required of a Killing field vanishing at that point. The inverse-mobility Hessian-integrability calculation is also correct.

The equal-elasticity lemma follows from opposite signs of \(E(rt)-E(t)\) near zero and infinity. Its three successive applications give the exact derivative ratios needed for every stationary gradient cancellation.

The two-valued population subspaces are legitimate, and the action modifications are finite rank with the stated uniform Hilbert–Schmidt bounds. The readout is \(c_0\,1-f_p\); its norm and the two scalar moments used in the curvature calculation are correct. The stationary loss is strictly below \(3/2\).

The restricted two-valued subsystem is invariant under the full gradient flow. Its negative unit-direction Hessian values imply positive linearization eigenvalues tending to infinity. At stationary points, the derivative of any smooth metric along the flow vanishes, so positivity of the metric alone forces its differential growth constant to dominate those eigenvalues.

**Clean conclusion:** no smooth positive full-parameter metric has one finite differential one-sided-Lipschitz constant on that whole raw ball. The result is an ambient stationary-state obstruction, not a claim about reached states.

**F — Order-one Gaussian readout, lines 1282–1734.**

This theorem uses two hidden layers, one RMS-unit sample, order-one independent Gaussian endpoint coordinates, connector variance \(1/n\), the displayed endpoint-RMS/connector-Frobenius metric, full-square loss, and multiplier \(\eta\ge0\).

The transformed equations and complete raw kernel are correct:
\[
A_s=Y,\quad \Xi_s=G^*B,\quad G_s=B\otimes X,
\]
\[
K=\|Y\|_2^2+\|B\|_2^2\|X\|_2^2+\|c(\Xi)G^*B\|_2^2.
\]
The transformation changes coordinates without changing the raw optimizer.

The root tuple \((u_0,\Theta(u_0))\) satisfies the finite-program root hypothesis; it need not be jointly Gaussian. Fixed readout saturation makes the coordinate instructions meet the bounded-derivative theorem.

Trace-class completeness supports the integrated increments. Bounded activation gives the pointwise readout envelope and cap-independent primal bounds. The comparison cost \(e^{C_SM}\) is dominated by the Gaussian initial clipping tail \(C(1+M)e^{-M^2/4}\). The Gaussian-envelope Osgood argument proves uniqueness in the stated class.

The two mesh limits in F.4 have distinct valid roles: one establishes uniform square-tail control, and the other transfers the gated quadratic kernel observation. Cap removal respects that order and does not presume fourth-moment convergence of finite arrays.

The physical clock
\[
s_t=2\eta(y-F(s))
\]
has the correct full-square factor. Monotonicity \(F_s=K\ge0\) bounds its range on every finite physical horizon. The finite clock uses \(y-f_n(0)\), rather than replacing its random initial error by \(y\).

The arctangent inverse, \(E\Theta(U)^2=14/3\), scaling example, and reciprocal-positive-polynomial class satisfy the stated hypotheses.

**Clean conclusion:** global population flow and the specified compact-time GF/current-field/kernel limits hold. Exact raw GD, the full velocity bundle, and asymptotic fitting are expressly not conclusions.

**G — Equal-label sech transfer, lines 1736–1984.**

The activation derivative is exactly \(0.1\operatorname{sech}z\), with the required value, slope, curvature, and smoothness bounds. The transfer uses the actual two-sample initialization, summed loss, three hidden layers, and raw GD step \(n^{-2}\).

The Part II numerical bootstrap applies with these inequalities. The fitting floor \(25/36\), clock factor \(4\), and physical exponents \(25/9\) and \(50/9\) are correct.

The two activation-specific replacements are sufficient: the feature-separation bound exceeds \(\pi/20\), and the top gate-ratio rectangles give ratio below \(1/4\) with the stated positive lower bound for the larger backward field. They establish the forward and backward positivity arguments, including \(\rho=-1\).

The initial hidden expansion has coefficient \(s^2/2\); conversion by \(s(t)=4t+o(t)\) gives the stated \(8\), \(16\), and \(32\) coefficients.

**Clean conclusion:** the entire listed equal-label flow, finite-algorithm, observation, nonaffinity, and motion scope transfers. There is no opposite-label global result or infinite-time/width interchange.

**H — Prescribed fixed-sign controls, lines 1987–2122.**

Integrable controls and bounded spatial derivatives give the asserted absolutely continuous solution and differentiability in the initial point with the control frozen.

After reflection, the \(C_r^{-1}\) energy calculation is correct. For negative correlation, monotonicity of \(x+y\) bounds the central-strip integral by \(8Q/(1-k)\); the argument also handles flat segments. The discarded and exterior contributions have the displayed exponential bounds.

Taking \(Q=2\log(e+U)\) yields the stated, conservative exponent \(16/(1-k)\) and prefactor \(e^4\). The relative-gate inequality follows from \(\phi''/\phi'=-\tanh\).

**Clean conclusion:** the frozen-control tangent bound and its moment implication hold. They do not control feedback variations or establish the required signs or moments for trained controls.

**I — First-Euler neighborhood obstruction, lines 2125–2229.**

The proof explicitly uses an auxiliary exactly zero readout, not the actual nonzero tiny Gaussian finite readout. Its first Euler step, residual interval, and Gaussian conditional transpose law are correct.

The removed projection has vanishing normalized squared norm. The limiting conditional Gaussian component has positive variance, yielding coordinates with arbitrarily large backward values in the fixed preactivation interval.

The rank-one perturbation changes exactly one preactivation by \(A^{-1}\). The gate term gives the fixed lower contribution, while the remaining query and residual changes cost \(O(A^{-1})\) at the relevant scale. The velocity-to-state ratio grows at least linearly in \(A\).

**Clean conclusion:** the claimed width-uniform neighborhood Lipschitz estimate fails in the displayed distance, with threshold chosen before width. This is not a continuous-trajectory or nonuniqueness result.

**SCOPE: separate audit of A–E**

**A — Tanh short-time continuity and zero-label stationarity, lines 11–257.**

The order-one stored readout, three hidden layers, full-square loss, and four raw kernel terms are consistent.

At initialization, clipping the centered readout and then the intermediate reverse query correctly eliminates the expected response coefficients. Removing those clips through second-moment laws yields the stated \(s_3,s_2,s_1\) and \(K_0\).

Conditional Gaussian estimates establish the exponential-square empirical bounds and initial maxima without independence between query coordinates. The entropy/Jensen multiplier inequality
\[
n^{-1}\|vw\|^2\le L^2u\log(M_v/u)
\]
is valid. Pairing successive gate differences with fixed initial incoming fields avoids iterating logarithmic losses.

The signed feature clock and decreasing residual magnitude transfer the estimate to every deterministic \(t_n\downarrow0\). For \(y=0\), the initial prediction is \(O_{\mathbb P}(n^{-1/2})\), so a fixed physical horizon lies in a vanishing feature interval.

Both continuous balance identities for \(\Phi(u)=\tfrac12\sinh^2u\) differentiate correctly and imply the displayed inverse-gate RMS bounds.

**Clean conclusion:** the vanishing-time statements, zero-label stationary limit, and continuous balance estimates hold. They do not establish nonzero-label positive-time tails, order-one learning, or raw-GD convergence.

**B — Sin-plus-cosine initialization and formal coefficients, lines 259–413.**

The Gaussian covariance and derivative covariance both equal \(e^{\rho-1}\). Tensor-power expansion and polynomial interpolation prove strict positivity for distinct normalized inputs, including singular input Grams.

The \(J_3,J_2\) response coefficients have the correct diagonal curvature terms. Their clipped derivation meets the source theorem’s hypotheses. The Gaussian innovations and positive diagonal gate Grams prove positivity of \(R_3,R_2,R_1\) and the three hidden coefficient matrices.

The formal \(t^2\) hidden terms and doubled total label-quadratic coefficient account correctly for \(\gamma=2/m\). The finite trigonometric Gaussian formula and regression residual \(1-2/e\) are correct.

The first-Euler reverse query has the stated variance \(2(1+e^{-8})h^2\). Sending \(h\downarrow0\) at fixed \(p\), then allowing \(p\) to increase, disproves the proposed bound with one constant.

**Clean conclusion:** these are initialization and formal-coefficient results. No analytic time remainder or constructed sin-plus-cosine trajectory is claimed.

**C — Fixed-offset affine reference, lines 415–595.**

The given-space polynomial raw flow is globally well posed by its exact loss-energy identity and completeness. The initialized Grams \(G+\ell11^T\), complete kernel, augmented-Gram lower bound, and three offset balance defects are correct.

Three distinct unit inputs are affinely independent. This supports the stationary-prediction classification; for mixed binary labels the nonzero constant-prediction loss is \(4/3\).

The conditional fitting proof correctly requires both a positive raw-Gram margin and entry below \(4/3\). Its residual-length clock gives
\[
R_u=-\|\theta_u\|^2,
\]
and the nonconstant prediction component bounds \(\|q_1\|\) from below. The resulting logarithmic clock bound and subsequent exponential fitting follow.

**Clean conclusion:** global given-space affine flow is unconditional; the fitting implication retains both stated premises. Pairwise separation does not replace them.

**D — Same-array causal response lemma, lines 598–795.**

Both triangular resolvents are bounded using the actual arrays. The proof correctly avoids assigning a column-density estimate directly to \(AB\). The elimination formulas retain the bounded arctangent offset and the actual Gaussian covariance.

The \(L^2\) premise bounds the Gaussian part, and the causal discrete inequality supplies the stated \(L^p\) bounds without a smallness premise on \(\varepsilon S\).

The two-fast-eigenvalue assertion, initialized Gaussian projection recurrence, remainder bound \(9I\), and initial strong/weak estimates are valid. The residual-coordinate equations retain \(\dot L\); the constrained readout decomposition retains its orthogonal component.

**Clean conclusion:** this is an auxiliary implication plus exact initialization and coordinate identities. It does not prove response bounds for neural training or trained Schur coercivity.

**E — Actual reached-state loss of local Lipschitzness, lines 797–1256.**

The local two-cap construction applies to the sech activation for either binary label pair. Exchange and readout-sign equivariance give deterministic population predictions \(f_a=y_ag\); this is not asserted samplewise at finite width.

The temporal covariance estimate for the reverse source follows from cap-independent primal bounds. The supplied dyadic Gaussian argument bounds the supremum of the finite interpolated source path uniformly in mesh.

Regression onto the terminal reverse coordinate provides a large signed source with a controlled whole path. Independence of the forward source group then permits varying its terminal coordinate. The resulting scalar recursion stays within \(O(R+1)\) of that coordinate and has Lipschitz constant at most \(Ce^{C(R+1)}\). These facts give the claimed Gaussian lower bound for the joint event. Closed inner events allow passage through mesh and cap limits in the correct direction.

The dual first-feature vector isolates one sample under a unit rank-one middle-matrix perturbation. Boundedness of each chosen indicator direction justifies the second derivative, while bounded readout makes the last-layer scalar differentiation valid with only an \(L^2\) first variation. The remaining last-layer curvature term is uniformly bounded.

The exact full-loss identity
\[
-D^2\mathcal L[v,v]
=4(1-g)D^2g[v,v]-2\sum_a(Df_a[v])^2
\]
has the correct factors and is used only after differentiating at the base state. The two essential tails therefore yield second derivatives of both unbounded signs.

**Clean conclusion:** the raw gradient fails to be locally Lipschitz at these actual deterministic positive-time population states. The local existence, uniqueness, and restart theorem remains consistent with this result. Opposite-label global continuation and fixed-positive-time finite-width Hessian limits are not established.

**IDENTITY: audit of §§1–8**

**§§1–3, lines 3–348.**

The endpoint rescaling converts the raw metric exactly into ordinary endpoint Hilbert norms and connector Frobenius norms. Simultaneous feature-ascent Euler updates are correct and contain no loss clock.

The Fock source uses actual creation adjoints and two orthogonal rooted sectors. The supplied Gaussian-word dependency proves its rooted Gram identification for every fixed compatible word list.

Finite Euler expansion produces finitely many rooted words with polynomial coefficients in initial contractions. The variable-threshold Gaussian norm estimate and endpoint moment bounds give uniform moments for each fixed program, justifying convergence in every finite \(L^p\), including expectations.

Finite-rank singular-value observations follow from the two finite Gram matrices without inverses. Oddness of the limit follows from symmetry of the finite initialization law, not from claiming that the deterministic representative is fixed by readout negation.

**§4, lines 350–543.**

The differentiated Euler recurrence and gradient symmetry identities are correct. Along the straight initial gradient line, two learned connector insertions vanish by rooted-sector orthogonality, giving \(S_0=0\).

The return recursions retain the annihilation contribution from reuse of each connector. Their orthogonal expansions yield
\[
H_0^{\rm sc}
=2\sum_{q=1}^L(L-q+1)q^2
=\frac{L(L+1)^2(L+2)}6.
\]
Substitution gives exactly the cubic step-doubling coefficient and sign in IU6. The formulas include \(L=1\) with empty connector products.

**§5, lines 545–810.**

The derivative bounds represented by \(K_L\) are valid; the stated values \(6,27,108\) are correct.

The transported-defect argument removes the exact factor \(h^2\) before taking three derivatives. The noncommutative telescoping order is correct. All trajectories and defect interpolation points remain inside the derivative-control ball, including for negative \(h\).

The recurrences \(X_r,G_r,A_r,Z_r,T_r,H_r,W_r\) bound the respective derivatives with the stated powers of step count. They use derivatives through order four only. Summing the \(t\) transported defects gives
\[
\sup|Q_t'''|\le6C_Kt^4.
\]
Oddness removes the constant and quadratic terms of \(Q_t\), yielding the claimed \(C_Kt^4|h|^5\) remainder.

**§§6–7, lines 812–937.**

Trace-class completeness supports the Picard integral and Euler limit. The contraction, first-exit argument, signed interval \(T_L=1/(8K_L)\), and local Euler error bounds are correct.

The dyadic substitution \(h=T/(2t)\) satisfies the theorem’s radius condition. Its summable bound and tail constant agree with IU6. Identification of the scalar dyadic limit properly uses the independently constructed operator-state flow.

**§8, lines 939–1032.**

The deterministic example has the advertised energy quantities and activation distance \(n^{-1/2}\). The two bottom updates are exactly \(4h1\) and \(3h1\), so their RMS difference is \(|h|\). The concentrated readout produces the claimed instability.

**Clean conclusion for IDENTITY:** all stated results hold for separately fixed finite depth. Width is taken first at each fixed Euler program; mesh refinement then occurs in the fixed population space. No joint depth limit, global feature-time theorem, physical-loss-clock theorem, or Gaussian-typical interpretation of §8 follows.

**Complete dependency audit**

The dependency packet was audited beyond the portions invoked by particular candidates.

| Dependency portion | Lines | Finding |
|---|---:|---|
| Finite §§1–4 | 8–213 | Raw derivatives, mobilities, kernels, dissipation, finite global existence, and fixed-depth width-uniform bounds are correct. |
| Special-data II.A | 277–471 | First-field metric, antipodal endpoint, exchange symmetry, and label-mode clock are correct. |
| II.B | 473–789 | The two-query chronological response bootstrap closes without assuming the current unknown row. |
| II.C | 791–1288 | Common-space construction, two-cap removal, nonsymmetric competitors, finite physical GF/GD, and full observation transfer are justified. |
| II.D | 1292–1629 | Forward separation, persistent nonaffinity, positive backward Grams, all-layer motion, and initial quadratic coefficients are justified. |
| III.M | 1646–1911 | Normalization, raw scaling, theorem quantifiers, and observation definitions are consistent with the subsequent proofs. |
| III.F | 1913–2453 | Fixed-program Gaussian law, singular-query extension, common actions, adjoints, scalar differentiation, and fixed-cap ODE/Euler foundations are established internally. |
| III.S | 2455–2710 | Controlled source moments and derivative bounds close at every separately fixed finite depth with the stated gain condition. |
| III.G | 2712–3118 | Initialized geometry, controlled displacement, capped residual decay, total control time, and regression lower bounds are correct. |
| III.V | 3120–3579 | Population cap removal and the finite-algorithm, kernel, velocity, path-law, and probe bridges respect the necessary limit orders. |
| III.N | 3581–4146 | Initialized backward and forward innovations prove every claimed nonzero acceleration and the coefficient \(18\). |
| III.A | 4148–4510 | Function-class gain selection, failure of a broad depth-uniform margin, and the stronger infinite-dimensional class are justified. |
| Linear §2.A | 4514–4696 | Singular expansion, trace-norm completeness, ideals, trace, Hilbert–Schmidt identities, and finite-rank Gram formulas are proved. |
| Linear §9 | 4699–4861 | Gaussian norm, Wick, trace variance, rooted contraction, and Fock identification proofs are sufficient. |

Several dependency checks are particularly material to the verdicts.

First, III.F’s adaptive conditioning is justified instruction by instruction. A new query is measurable from the current transcript; conditioning its answer constrains only the queried residual Gaussian matrix factor. For nonsingular query Grams, the stated minimum-norm conditional mean satisfies both forward and transpose constraints. The removed fresh-noise projection has normalized mean square \(\operatorname{rank}(U)/n\).

Gaussian integration by parts cancels the old regression-response terms and gives the advertised source formula. Adding a fresh small independent input noise at each query resolves singular Grams. Finite-array Lipschitz comparison and covariance-square-root coupling remove that noise; no pseudoinverse continuity is used. The common generated spaces are dense enough to extend the actions, and finite transpose pairings prove genuine adjunction.

Second, Part II’s critical constants check exactly:
\[
V_*=\frac{3067}{3200},\qquad
Q_*=\frac{24829}{19200},
\]
\[
\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
+\frac3{200}Q_*^2
=\frac{71063018523}{73728000000}<\frac{97}{100}.
\]
The forward margin is \(3/2-(49/36+3/25)=17/900>0\). The two actual-query Gaussian envelopes dominate the linear-in-cap comparison exponential. Ordered observation clipping and compact \(L^2\) tails justify velocity and kernel passage; mere RMS boundedness is not substituted.

Third, III.S uses independent primal estimates before its source bootstrap. Its same-array elimination retains the offset of size \(K_\ell^{-1}\), which compensates the curvature scale \(K_\ell\). Forward response production uses only completed past reverse rows. The descending reverse sweep uses the already constructed current forward rows and current upper reverse row. The explicit \(\alpha_\ell,b_\ell\) bounds satisfy the required small-gain inequalities for all separately fixed \(L\ge2\).

Fourth, III.G does not assign gradient dissipation to the capped field. It retains the possibly nonsymmetric hidden term \(J_hU_{h,R}\), bounds its operator norm, and combines it with the readout Gram floor. This gives the residual estimate and total control time \(S/2\), with continuation slack. Nonaffinity follows from an actual initialized Gaussian regression margin and a coupled raw-preactivation displacement bound.

Fifth, III.V’s source and observation arguments distinguish expected derivative rows, pointwise derivative envelopes, and value-only truncation. The final velocity cap removal uses compact tails of the uncut reference after strong construction; it does not multiply a potentially uncontrolled cap-dependent fourth-moment constant by a cap error. Path-law convergence additionally uses the integrated-velocity interpolation inequality.

Sixth, III.N’s innovations use **uncentered input Grams** as centered source covariances. Positive conditional variances prevent cancellation in every upper sample direction. Its coherent clipping schedule supplies the expected derivative formulas for unbounded products with only the stated \(C^2\) regularity. The half-sum physical factors yield acceleration \(9\mathscr V\) and equal kernel contributions \(9t^2\|\mathscr V\|^2\), totaling \(18\).

Finally, the linear foundations are self-contained. The compact singular expansion proves the approximation-number formula and trace-norm completeness. The Wick graph count identifies precisely the matching-label, opposite-orientation noncrossing pairings; connected two-trace contributions vanish. Conditioning on independent Gaussian roots transfers trace limits to rooted contractions. The two Fock sectors encode orthogonality of entire rooted subspaces. The passing mention of `gaussian_calculus.md` is not needed: Wick’s identity is already derived from the finite Gaussian moment-generating function.

**Required corrections and clean-scope boundary**

No mathematical correction is required by this audit.

The clean verdicts preserve the documents’ explicit restrictions:

- Conditional moment, response, Gram, and loss-entry premises remain premises.
- Formal initial coefficients remain formal where no time remainder is asserted.
- Fixed-program width limits precede subsequent mesh limits.
- Compact physical horizons do not authorize growing horizons or infinite-time/width interchange.
- Fixed-depth results do not authorize \(L=L(n)\).
- Ambient-state and designed-query counterexamples do not imply canonical reachability.
- Failure of local Lipschitzness does not contradict the separately proved weaker uniqueness estimates.
- Actual adjoints, immutable sources, and full reached states remain part of the restart specification.

**Final unchanged hashes**

| File | Final SHA-256 |
|---|---|
| `FINAL_LAST_ADDITION.md` | `bb28eb597f0e6a230e90674eb379e2a901e2038f8aa1138b1e236e137c212976` |
| `FINAL_SCOPE_ADDITION.md` | `b85476dd8886365c292de1cd19463f988971d6f472800d838a8a1cd6d7b166d6` |
| `FINAL_IDENTITY_UNIFORM_ADDITION.md` | `d26113499bb36349cbb95fe7c78bedc74e694b4ae57ffcc862c7351103081bce` |
| `FINAL_LAST_R2_DEPENDENCIES.md` | `d98b98ce35bf3f2f16d55be8ded7c1d10dd4f713abb49169f07bd3b82b808753` |
| `NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

All five match the starting manifest exactly.