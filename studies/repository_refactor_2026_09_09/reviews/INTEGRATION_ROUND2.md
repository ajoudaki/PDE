# Frozen library integration audit

**Verdict: CLEAN — for the integration, notation, dependency-interface, and implementation-equation scope specified below.**

Required findings: **none**. One optional local notation refinement is recorded in §8. I found no concrete incompatibility requiring a change to the supplied library. This is not a claim that 17,224 chapter lines have received an independent, line-by-line proof certification.

Audit date: 2026-09-09. Immutable input root: `/tmp/pde-integration-round2.vG0oUu`.

## 1. Isolation, method, and meaning of the verdict

The only mathematical/project inputs used were the supplied `docs/`, `code/`, `Makefile`, and `requirements.txt`. No original repository, studies, data, history, chats, other reviews, agents, external papers, or web sources were consulted. No prior verdict was used. No input was edited; no installation or experiment was performed. The sole delivered edit is this report.

The audit followed definitions and equations through the actual arguments supporting their interfaces, not just chapter summaries or dependency headings. In particular, Gaussian source identification, singular-Gram handling, response estimates, removal of cutoffs, raw-gradient identification, physical-clock conversion, and velocity-observable extensions were checked where the conclusions need them. Specialized mathematical imports were not accepted on the strength of a citation: the supplied proof and its hypotheses were checked at the consuming interface.

“Self-contained” here means that the specialized results needed by these chapters are supplied in the book. It does not mean that the book reconstructs foundational analysis and probability from axioms. Standard background such as Fubini, dominated convergence, finite-dimensional spectral calculus, and disintegration/countable probability-kernel construction is still used. For example, continuous-depth §7 explicitly states the disintegration input to its Wasserstein completeness argument. I did not classify these background tools as missing network-limit theorems.

The verdict covers the actual stated, restricted theorems. It does **not** extend them to arbitrary correlated dense data, joint dense-network depth/width limits, growing training programs or time horizons, arbitrary population restart states, projected population dynamics, or observables/topologies not proved in the relevant chapter.

## 2. Read coverage

Every line of every listed input was read. The three requested guides were read fully, as were all eight chapters, all implementation files, all tests, and the boundary checker. The 21 files contain 18,853 lines; the eight mathematical chapters account for 17,224 of them.

| Input | Lines | Textual coverage |
| --- | ---: | --- |
| [docs/NOTATION.md](/tmp/pde-integration-round2.vG0oUu/docs/NOTATION.md:1) | 98 | Full |
| [docs/README.md](/tmp/pde-integration-round2.vG0oUu/docs/README.md:1) | 85 | Full |
| [docs/finite_dynamics.md](/tmp/pde-integration-round2.vG0oUu/docs/finite_dynamics.md:1) | 214 | Full |
| [docs/gaussian_calculus.md](/tmp/pde-integration-round2.vG0oUu/docs/gaussian_calculus.md:1) | 1,812 | Full |
| [docs/arctan_limits.md](/tmp/pde-integration-round2.vG0oUu/docs/arctan_limits.md:1) | 3,117 | Full |
| [docs/global_nonlinear.md](/tmp/pde-integration-round2.vG0oUu/docs/global_nonlinear.md:1) | 1,796 | Full |
| [docs/special_data_limits.md](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:1) | 6,398 | Full, including all three parts and appendix |
| [docs/finite_optimization_and_controls.md](/tmp/pde-integration-round2.vG0oUu/docs/finite_optimization_and_controls.md:1) | 1,231 | Full |
| [docs/linear_dynamics.md](/tmp/pde-integration-round2.vG0oUu/docs/linear_dynamics.md:1) | 1,166 | Full |
| [docs/continuous_depth.md](/tmp/pde-integration-round2.vG0oUu/docs/continuous_depth.md:1) | 1,490 | Full |
| [code/README.md](/tmp/pde-integration-round2.vG0oUu/code/README.md:1) | 165 | Full |
| [code/pde/__init__.py](/tmp/pde-integration-round2.vG0oUu/code/pde/__init__.py:1) | 26 | Full |
| [code/pde/finite_network.py](/tmp/pde-integration-round2.vG0oUu/code/pde/finite_network.py:1) | 363 | Full |
| [code/pde/gaussian_moments.py](/tmp/pde-integration-round2.vG0oUu/code/pde/gaussian_moments.py:1) | 114 | Full |
| [code/tests/test_finite_network.py](/tmp/pde-integration-round2.vG0oUu/code/tests/test_finite_network.py:1) | 297 | Full |
| [code/tests/test_gaussian_moments.py](/tmp/pde-integration-round2.vG0oUu/code/tests/test_gaussian_moments.py:1) | 110 | Full |
| [code/tests/test_library_boundary.py](/tmp/pde-integration-round2.vG0oUu/code/tests/test_library_boundary.py:1) | 58 | Full |
| [code/tests/test_numerical_contract.py](/tmp/pde-integration-round2.vG0oUu/code/tests/test_numerical_contract.py:1) | 202 | Full |
| [code/tools/check_library.py](/tmp/pde-integration-round2.vG0oUu/code/tools/check_library.py:1) | 100 | Full |
| [Makefile](/tmp/pde-integration-round2.vG0oUu/Makefile:1) | 9 | Full |
| [requirements.txt](/tmp/pde-integration-round2.vG0oUu/requirements.txt:1) | 2 | Full |

**Interface-only textual reads: none.** This should not be confused with proof-verification depth. Mathematical checking was integration-focused: every chapter's theorem/conventions/dependency interfaces were examined, and the supporting proofs were checked for the hypotheses, conclusions, constants, limit orders, and types needed at those interfaces. I did not independently rederive every combinatorial enumeration, every numerical constant, or every inequality in the full text. There was no formal proof assistant or exhaustive symbolic verification.

The detailed checks below identify what was actually tested conceptually. They are evidence for the scoped verdict, rather than a claim that passing tests certifies the mathematical chapters.

## 3. Canonical notation, normalization, and clocks

The shared conventions in [NOTATION](/tmp/pde-integration-round2.vG0oUu/docs/NOTATION.md:1) agree with the finite identities and implementation:

- `L` is hidden depth, `m` sample count, `d` input dimension, and `n` hidden width. The first stored matrix has entry variance 1, middle matrices variance `1/n`, and the canonical small stored readout variance `1/n²`.
- The first input contraction includes `1/sqrt(d)`; middle forward actions have no additional `1/sqrt(n)`; the final prediction has `1/n`. A Gaussian matrix already stored at variance `1/n` is not divided by `sqrt(n)` a second time.
- Residuals are `r=f-y`; backward fields `delta=n df/dz` exclude residuals. Under mean-square loss, block mobilities are `(n kappa_1, kappa_2, ..., kappa_L, n kappa_out)`.
- Population layers have distinct typed Hilbert spaces. Transpose reuse becomes the genuine adjoint on those spaces. A population rank-one action `v tensor h` corresponds to the finite matrix `v h^T/n`; it is not an unnormalized outer product. Finite Euclidean, RMS, Frobenius, and operator norms are distinguished.
- Initialization is not silently changed to exactly zero finite readout. Zero readout is a population initial value or an explicitly separate deterministic finite case. Where a proof starts from a zero-readout reference, the actual nonzero Gaussian readout is retained and compared.

The general finite algebra gives

\[
\dot f=-\frac{2}{m}Kr,\qquad
\dot{\mathcal L}=-\frac{4}{m^2}r^TKr,
\]

with `K` including the declared block mobilities. The code's mean-loss gradients, velocities, and kernel blocks have precisely these factors. The linear chapter instead explicitly places its common mobility multiplier outside its unit-mobility kernel; this is a stated convention, not a missing factor.

The apparently different loss and acceleration constants in the special-data parts are consistent after conversion:

| Setting | Physical loss | Same-mobility speed relative to mean-square convention | Actual GD/clock scope |
| --- | --- | --- | --- |
| Canonical dense chapters/code | `(1/m) sum r_i²` | 1 | Chapter-specific GD hypotheses |
| Special data I and II, `m=2` | `sum r_i²` | 2 | Raw step `n^-2`; mean-loss implementation would use step `2 n^-2` |
| Special data III, `m=3` | `(1/2) sum r_i²` | `3/2` | Raw step `n^-2`; mean-loss implementation would use step `(3/2)n^-2` |
| Continuous-depth particle model | `(1/(2m)) sum r_i²` | `1/2` | Exact gradient flow only; architectural mesh `1/L` is not a training step |

Evidence: [special-data conventions, lines 1–125](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:1), [continuous-depth assumptions/clocks, lines 28–102](/tmp/pde-integration-round2.vG0oUu/docs/continuous_depth.md:28), and [finite implementation, lines 261–363](/tmp/pde-integration-round2.vG0oUu/code/pde/finite_network.py:261).

The first-row replacement `V^(1)=W^(1)/sqrt(d)` in special data has the corresponding raw metric factor `d`; it is not an unannounced mobility change. In Part III, `K_ell=a^(ell-1)`, `Y^ell=Z^ell/K_ell`, and `X^ell=H^ell/a^ell` normalize **fields only**. The stored middle matrices and readout remain unchanged. Consequently `f=a^L F`, every raw predictor-gradient block acquires `a^L`, and the raw kernel acquires `a^(2L)`. The true backward relation `delta_i^ell=a^(L-ell+1)d_i^ell` is consistent with every layer. These identities are stated together and used consistently in [III.M, lines 3638–3709](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:3638).

Ordinary arctangent uses the primitive `F(z)=z+z³/3`; the shifted/scaled arctangent uses `10F`. Those transformed continuous identities are not passed off as exact transformed-coordinate GD updates. The raw-GD proofs retain the cubic update defect.

## 4. Chapter interfaces and dependency checks

### 4.1 Finite dynamics and finite optimization

[Finite dynamics](/tmp/pde-integration-round2.vG0oUu/docs/finite_dynamics.md:1) supplies the general finite differentiation, kernel, and dissipation identities. Its finite-time continuation uses finite-dimensional local existence plus finite energy and a Cauchy endpoint argument. Its fixed-depth norm estimates and Gaussian initial matrix bound are proved there; they do not assert that a population action is bounded on arbitrary `L^p`, or that unbounded coordinate multiplication is harmless. The final warning at lines 209–214 correctly limits reuse of the RMS estimates.

[Finite optimization](/tmp/pde-integration-round2.vG0oUu/docs/finite_optimization_and_controls.md:19) is restricted to `L=3`, `m=d=1`, target 1, ordinary arctangent, and finite width. I checked the following actual dependency chain:

- Lemma 2.1 supplies the feature-flow action and positive readout acceleration used by Theorem 3.1. The small, nonzero stored-readout case has its own explicit size threshold and initial noncollapse assumptions; it is not inferred from the zero-readout case by a qualitative appeal to continuity over infinite time.
- Theorem 4.1 establishes raw-GD coercivity through its own positive-step path bounds, exact directional identity, remainder control, and extended-prefix induction (§4.1–§4.4). It does not assume residual positivity in order to prove it, or import finite-time GF convergence as a proof of an infinite GD endpoint.
- The metric-projection theorem proves its energy inequality, positive-definiteness/noncollapse, continuation, and physical clock inside §§5–6. The integrated middle-equation defect in §7.1 is an `L^1` defect against bounded tests, not a state-stability theorem.
- Eventual exactness in [§7.2, lines 1032–1063](/tmp/pde-integration-round2.vG0oUu/docs/finite_optimization_and_controls.md:1032) requires `R >= C(S)sqrt(n)` at **fixed width**. The argument checks feasibility of the canonical backward vector and uniqueness of the metric minimizer. It does not supply a width-independent cap, a projected GD theorem, or interchange of width and cap limits.
- The Gaussian event and width thresholds in §8 verify the initial assumptions actually needed by the finite results. The finite GF and GD endpoints are not claimed to coincide.

Thus finite fitting and finite projected continuation do not fill the missing global uncut ordinary-arctangent population theorem. This restriction agrees with the chapter's [dependency/scope section, lines 1202–1231](/tmp/pde-integration-round2.vG0oUu/docs/finite_optimization_and_controls.md:1202) and the book overview.

### 4.2 Gaussian calculus: the current fixed-program theorem

The theorem in [gaussian_calculus §5.1, lines 262–318](/tmp/pde-integration-round2.vG0oUu/docs/gaussian_calculus.md:262) is a **fixed finite program**: fixed `L`, fixed update count `N`, and fixed nonzero update parameter `h`; one scalar input; order-one stored readout; and the stated `C²`, growth, derivative, and normalization hypotheses on the activation. Its update is an output-ascent program, not the small-readout loss-gradient training flow. Negative `h` is allowed; `h=0` is not silently included in a rank proof requiring nonzero forcing. Constant and affine cases receive their own treatment.

I followed the program chronology and full adaptive conditioning, not just a Wick-moment slogan. The important proof interfaces are:

1. The matrix-call count includes terminal forward calls. Both forward and transpose source groups are retained in the inverse-free construction (§§5.2–5.6, lines 351–885). Reused-column response paths are not dropped.
2. Rank is proved for the claimed program, with the constant/affine exceptions handled separately (§5.7, lines 886–1116). This is a fixed-program gap, not a gap uniform in growing `N` or vanishing `h`.
3. The predictable stopping argument supplies the high-moment/error estimates needed before removing stopping (§5.9, lines 1170–1547). The terminal raw polynomial bound and uniform integrability are supplied in §5.10, lines 1548–1718.
4. Claims about regression coefficients concern the specified extended predictable coefficients, not unrestricted moments of raw inverses on singular or ill-conditioned events.

The resulting expected terminal output and finite mixed-coordinate moment conclusions are supported at this interface. They are not imported as a theorem for `N=N_n -> infinity`, a continuous-time training limit, a width-dependent step, or an unrestricted population `L^p` action. The later obstruction examples likewise do not establish that a PDE representation is necessary.

### 4.3 Ordinary arctangent and shifted global nonlinear dynamics

[Arctangent limits](/tmp/pde-integration-round2.vG0oUu/docs/arctan_limits.md:1) separates three materially different results:

- The two-hidden-layer, one-sample theorem is global on each fixed physical-time compact interval, with the stated `eta_n sqrt(n) -> 0` condition. Its transformed `L²` comparison, bounded reference readout, countably generated action space, raw Euler defects, and observation tails are actually provided in §1. It establishes initial positive-time hidden motion/nonaffinity, not an unrestricted later-time persistence or fitting theorem.
- The three-hidden-layer, one-sample **uncut** theorem is local, with explicit positive `S_0,T_0`, and raw step `n^-2` (§2). Its finite-program source law is proved in §3, local response envelope in §5, and asymmetric comparison/cutoff removal in §6. The lemma at lines 1876–1899 is used with the source and tail hypotheses established in those sections. The `exp(CR-cR²)` comparison closes precisely on the supplied local interval.
- The globally continued fixed-cap feature-time family in §4 is auxiliary. Its global existence is not uncut loss-gradient continuation or fitting. Likewise, §7's scalar raw-gradient differentiability is not local Lipschitzness of the entire uncut gradient field in ambient `L²`.

At the velocity interface, the argument does not apply a Gaussian theorem with bounded derivatives directly to an unbounded product: extra truncations and actual action estimates precede passing to the limit. In §8, the initial transpose computations include the current return terms and full second moments. The lower positive bounds and the physical `2t²` preactivation displacement / `8t²` total-kernel correction are consistent with the one-sample mean-loss clock. Evidence: [§§5–6](/tmp/pde-integration-round2.vG0oUu/docs/arctan_limits.md:1487), [raw-gradient discussion](/tmp/pde-integration-round2.vG0oUu/docs/arctan_limits.md:2547), and [initial-motion proof](/tmp/pde-integration-round2.vG0oUu/docs/arctan_limits.md:2716).

[Global nonlinear dynamics](/tmp/pde-integration-round2.vG0oUu/docs/global_nonlinear.md:1) instead uses `phi(z)=1+arctan(z)/10`, fixed `L>=3`, one scalar sample/target 1, and small stored readout. This architectural/activation change is explicit. Its positive activation bound `5/6`, upper bound `7/6`, derivative bound `1/10`, and primitive `10F` are not borrowed from ordinary arctangent.

The decisive global proof chain was checked: finite Gaussian source identification and singular perturbation (§3); all-depth current upper-return equations (§4); generated `L²` actions and comparison with only one power of the cutoff parameter (§5); chronological response bounds through feature time `3/2` (§6); and cutoff removal against sub-Gaussian reference tails (§7). The response induction includes current upper responses before lower responses; it does not invoke the fixed-program theorem with a growing instruction count.

The positive readout kernel bound `25/36` makes the target feature time at most `36/25 < 3/2`. The clock argument in [§9, lines 1132–1259](/tmp/pde-integration-round2.vG0oUu/docs/global_nonlinear.md:1132) then supports all finite physical times and the stated fitting rate. Raw GD and recomputed velocity observations have their own compact-time stopping and product-truncation arguments (§§10–11). Persistence of nonaffinity and activity of every hidden layer at positive times is proved separately in §12; it is not deduced from a nonzero initial Taylor coefficient alone. The statements remain fixed-depth/fixed-horizon width limits even where a response bound happens to be depth-uniform.

### 4.4 Linear dynamics: reuse scope and closure claims

[Linear dynamics](/tmp/pde-integration-round2.vG0oUu/docs/linear_dynamics.md:15) has exactly three hidden layers, identity activation, one scalar input and arbitrary scalar target, and **order-one** stored endpoint/readout coordinates. Its embedded variables `W^(1)/sqrt(n)` and `W^(4)/sqrt(n)` are proof-space representations, not the small-readout model. The initial limiting unit kernel is 4. These facts are not transferred to the canonical tiny-readout nonlinear initialization.

The initialization limit uses the chapter's **own** fixed-word Gaussian lemma ([§2, lines 144–368](/tmp/pde-integration-round2.vG0oUu/docs/linear_dynamics.md:144)): Gaussian pairings, the surviving quotient graphs, root contractions, and variance control. I checked that this is the lemma used by the cyclic operator construction. There is no dependency on the Gaussian chapter's output-ascent trajectory theorem, hence no unverified substitution of different readout, update, or activation hypotheses.

The cyclic representation has trace-class increments and rank-at-most-four cubic field. Local trace-norm stability and the finite-energy endpoint estimate give the stated global flow (§3). Here restart genuinely covers the stated cyclic trace-class affine state space, a broader domain than merely the reached-state restart of the nonlinear generated-action constructions. The fitting proof uses its own endpoint norm/kernel inequalities; target zero gives the stationary limiting initial trajectory.

For the width/GD result (§4), common finite rooted-word Gram matrices, continuity of positive square roots even at singular Grams, and a dimension-independent Euler estimate are supplied. This supports every positive `eta_n -> 0` at fixed compact time without an additional width-rate condition. The observations are the declared rooted-word contractions and finite-rank/Schatten quantities. The theorem does not assert a neuron-coordinate law or operator-norm convergence between unrelated width spaces.

The obstruction in §§5–6 is restricted to uniform bounded-degree complete contractions, the specified polynomial differential/readout structure (or analytic structure near zero), and an open state-domain requirement. The graph argument and the surviving long-path monomial test this restricted interface. It is not a theorem that no finite nonlinear encoding of a single Gaussian-initialized orbit can exist. [§7, lines 1059–1166](/tmp/pde-integration-round2.vG0oUu/docs/linear_dynamics.md:1059) explicitly supplies unrestricted future-profile encoding and a width-one exception. No overclaim about all finite-dimensional closures or all fields was found.

### 4.5 Continuous depth is a separate architecture

[Continuous depth](/tmp/pde-integration-round2.vG0oUu/docs/continuous_depth.md:28) concerns scalar residual particle features averaged within each layer, with no trainable dense hidden matrices and no separate trained readout. Its assumptions A1–A2 apply to the raw parameterized feature `Phi(theta,z)`: uniform forward growth and uniform parameter/derivative regularity on bounded state strips. They are not assumptions automatically satisfied by arbitrary dense-network activations or arbitrary reparameterizations.

The proof supplies width/depth-independent state and sensitivity bounds (§5), discrete-depth population stability (§6), completeness and characteristic flow on the depth-integrated Wasserstein profile space (§7), a canonical continuous depth representative for constant initialization (§8), and width convergence under exactly a finite first moment (§9). In particular, the width error is the **average** empirical `W_1` error across layers, not the layer maximum. This is what permits arbitrary joint width/depth sequences without a hidden maximum-over-depth concentration requirement.

Restart covers the full declared profile space. Pointwise sampling in the depth consistency estimate uses the canonical continuous representative, not arbitrary representatives of an almost-everywhere equivalence class. The `O_T(1/L)` consistency proof uses constant-in-depth initialization; it is not asserted for every restart profile. Evidence: [Theorem 4.1](/tmp/pde-integration-round2.vG0oUu/docs/continuous_depth.md:329), [profile construction](/tmp/pde-integration-round2.vG0oUu/docs/continuous_depth.md:639), and [representative/limit proofs](/tmp/pde-integration-round2.vG0oUu/docs/continuous_depth.md:842).

The differentiable output/dissipation readouts in §10 remain valid on the full restart domain by bounded derivatives and velocities. Nonzero individual gradients do not preclude sample cancellation: the chapter correctly requires positive total dissipation energy for strict loss decrease. It does not infer fitting or a positive kernel floor from A1–A2. The finite linear-moment obstruction in §12 is proved by finite-support linear relations and is explicitly not an obstruction to arbitrary nonlinear encodings. No GD, ReLU, general unbounded-weight polynomial, or dense Gaussian ResNet theorem is claimed.

## 5. Special-data audit: all three parts

### 5.1 Part I: ordinary arctangent, two opposite labels

Scope: `L=2`, labels `(+1,-1)`, and only the two correlations `rho=0` or `rho=-1`. The feature transformation relies on these special geometries. The proof does not cancel the cross-sample gate ratios for arbitrary intermediate correlations.

The [theorem and strong-flow construction, lines 272–679](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:272) establish global fixed-compact-time limits and reached-state restart in the declared transformed/action state. The raw first-row reconstruction preserves the component orthogonal to the data span. At `rho=-1`, the first projection is one-dimensional; no inverse of the singular two-column Gram is used.

The Gaussian and response arguments in [I.3, lines 680–1342](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:680) actually provide the stronger finite-moment input needed here. They use coordinate Gaussian/conditional-mean estimates, not an assumed bounded initialized action on arbitrary `L^p`. Response coefficients are extracted with an actual independently perturbed finite program, followed by the stated limit order; a transverse derivative is not inferred from values on singular support. The Gaussian-plus-bounded descriptions do not require Gaussianity of a path supremum or independence across training times.

The observation proof in I.4 distinguishes all finite `W_p` moments for the stated joint base-field paths from the second-moment/`W_2` velocity and probe assertions. The latter require additional tail estimates before action reuse. Population sample-exchange symmetry is not asserted as exact symmetry of every finite realization; the antiparallel case has its separate exact structural relation.

At [I.5, initial-motion calculation, lines 1836–1960](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:1836), the top hidden layer is layer 2 and the readout is layer 3 throughout. With `hat W^3=(H_1^2-H_2^2)/2`, the reverse source covariance is the full second moment of `hat delta`, not its centered covariance. For orthogonal inputs, the finite two-column feature Gram tends to `mu_0 I`; for antiparallel inputs the proof uses the one surviving column with positive `mu_0`.

The orthogonal first-layer and matrix velocities carry the required sample factor `1/2`. The antiparallel reduction uses its one-column formula instead of double counting. In feature time the hidden displacement is second order; the sum-loss clock has `s'=4(1-f_1)`, hence `s=4t+o(t)`. The hidden and readout kernel contributions each produce the same positive feature-time quadratic coefficient. Their sum gives the stated physical coefficient `32 d_* t²`. The return terms and actual adjunction are used to prove positivity, rather than assuming all correction coefficients have a sign.

The all-positive-time hidden activity and nonaffinity conclusions have separate support/adjunction arguments. Fitting is **not** concluded: `0<f_1<1` and positive instantaneous kernel do not establish divergence of its time integral. The final scope section preserves this distinction.

### 5.2 Part II: shifted arctangent, two equal labels

Scope: `L=3`, `phi=1+arctan/10`, two equal labels (either sign), and `-1<=rho<1`. The lower activation bound is the explicitly named `c_-=5/6`, upper bound `a=7/6`; neither is a silent reassignment of sample count. The first-layer data Gram is inverted only for `rho>-1`; the antiparallel endpoint is handled on the one-dimensional projection space.

The forward import of III.F is legitimate, but needed checking. At [lines 2429–2441](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:2429), Part II uses the generic finite-program result proved in [III.F, lines 3778–4319](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:3778). That result is stated/proved for a finite adjacent-matrix program and a finite tuple of iid-per-population roots, allowing dependence inside each tuple. It is not restricted by its placement in Part III to exactly three input samples or to Part III's activation. Part II has independent initialized matrices, admissible two-sample root tuples (including the singular endpoint), causal finite feedback, and fixed-cap `C¹` maps with bounded first derivatives. Its readout is bounded on the feature interval; where a globally bounded-derivative map is required, the proof truncates outside the attained readout range. Thus the imported hypotheses really match.

The source equations retain all past-time/sample slots and current upper responses, with full uncentered Grams. The response bootstrap in II.B counts the two sample weights correctly: a factor `Delta/2` summed over two samples gives `Delta`, not `2 Delta`. Both displayed response bounds are below the prescribed threshold, giving the required exponential-square tails through feature time `3/2`.

II.C then uses actual common generated actions, an asymmetric single-cutoff comparison, and those tails to remove the caps. It proves raw-gradient identification and reached-state restart. Exchange symmetry is imposed on the limiting law, not fabricated for the finite trajectory. Finite trajectories with small off-symmetry errors are compared to the symmetric reference instead of being assigned an exact scalar clock.

For the limiting equal-label prediction `g=y(f_1+f_2)/2`, the clock is `s'=4(1-g)`. The positive readout floor gives `s_*<=36/25<3/2`; the stated residual and sum-loss rates are respectively `exp(-25t/9)` and `2 exp(-50t/9)`. This global fitting proof does not extend to opposite labels.

The velocity and backward-observable interface in II.C.5–II.C.6 explicitly inserts nested clips before applying III.F to unbounded products. The relevant source derivatives have integrable envelopes, covariance-square-root couplings identify their limits, and actual bounded actions transfer the errors. Ordinary `W_2` convergence alone is not used to pass an expected derivative of an unbounded map.

The [activity and initial-motion proof, lines 3101–3500](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:3101) establishes positive pair Grams even at `rho=-1`: shifted features are not opposite, and the support argument is not an invalid appeal to a nonsingular initial input Gram. Full reverse-source covariance propagates positivity. The initial `R^2` and `R^1` terms occur at their correct layers and include the next-layer return and the curvature term. Unbounded lower-layer derivatives are handled by the supplied truncation/envelope argument.

The initial hidden field displacement is `s² B/2 = 8t² B+o(t²)` because `s~4t`. Readout and hidden kernel contributions each give `16 Gamma t²`, hence total coefficient `32 Gamma`. All three hidden blocks occur with positive contributions. Persistence for every positive time is separately established; it is not inferred merely from this expansion.

### 5.3 Part III: one nonaffine activation for all separately fixed finite depths

Scope: three normalized inputs with pairwise `G_ij<=1-delta`, `delta>0`; binary labels; fixed `L>=2`; and

\[
\phi(z)=a(1+z)+e\psi(z),\qquad 0<e\le1,
\]

with the declared nonconstant `C_b²` perturbation. The chosen gain depends on `delta,psi`, not on depth, input dimension, the particular admitted triple, or the time horizon. The model is unbounded-activation and does **not** inherit the positive activation floor from Part II. Its positive basic bound is the slope `alpha=a-e>0`.

The [model/theorem interface, lines 3500–3777](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:3500) consistently separates raw fields, normalized fields, raw backward observations, and temporarily capped update fields. Each true raw kernel block has the correct adjacent-layer feature pairing and normalization. No top-layer symbol is reused as a hidden matrix index, and no depth factor is missing from the raw clock/kernel conversion.

The geometric and positivity steps in [III.G, lines 4577–4986](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:4577) were checked at the hypotheses they use:

- The three-point argument proves a lower bound for `G+11^T` even when `G` itself is singular. It uses the three-sample geometry and is not advertised for arbitrary batch size.
- Initial feature-Gram positivity uses constant/linear Gaussian projections. Summable depth losses, including the integration-by-parts bound on the perturbation's expected derivative, are what preserve the quantitative normalized Gram floor. Merely iterating the coarse lower slope bound would not establish that floor.
- Controlled primal displacements keep the top normalized Gram at least `3 lambda/4`, with `lambda=delta²/16`. The hidden term in the capped residual equation is a product of a true Jacobian and a capped update direction; it can be nonsymmetric. The proof bounds its operator norm by `lambda/4`, rather than wrongly declaring it positive semidefinite.
- The resulting residual decay controls total feature/control length, closing the global continuation argument. The raw half-sum rate is `||r(t)|| <= sqrt(3) exp(-lambda a^(2L)t/2)`, and loss at most `(3/2) exp(-lambda a^(2L)t)`.

The proof behind the generic Gaussian import III.F was read, including adaptive conditioning, full second-moment source terms, independent jitter before matrix reuse, the Schur lower bound at fixed jitter, fixed-program perturbation control, and removal via covariance square roots and bounded continuous derivative expectations. The derivative hypothesis is genuinely bounded-first-derivative `C¹`; it does not cover arbitrary raw reverse-product maps by itself.

That gap is supplied, rather than ignored, by [III.V, lines 4987–5445](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:4987): Gaussian probes identify response rows at the correct chronological slot; nested product truncations precede source-derivative limits; integrable envelopes and Gaussian tails control their removal; actual action norms propagate the errors. For velocity observations the cap order is fixed outer observation cap, width/mesh limits, removal of the dynamical cap, and then removal of the observation cap. True backward observations have their separate descending construction. The proof does not confuse the capped training direction with the actual raw gradient/kernel.

Raw scalar predictor Fréchet differentiability is established by a dual remainder estimate. Only the needed strong multiplier/curve chain rules are used for coordinatewise activation on `L²`; a false ambient Nemytskii Fréchet differentiability assertion is not imported. Restart is from every reached state in the stated bounded-primal strong class, with the inherited action structure, not from an arbitrary replacement collection of Gaussian fields.

The [initial-motion proof III.N, lines 5446–6012](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:5446) also handles every layer, including the `L=2` boundary:

- The separate initial statement only needs its stated `a>=2` slope condition and nonconstant perturbation, not a depth-dependent affine-comparison premise.
- Top source-Gram positivity uses full Gaussian support and nontrivial curvature. Lower reverse fields include both curvature and next-layer return terms. Return coefficients need not be positive; the proof obtains positivity from independent conditional Gaussian variance and genuine adjunction instead.
- Nonzero raw hidden-block motion does not by itself prove each sample's upper hidden field moves. The additional forward query isolates a fresh component outside the old feature span and provides the strictly positive variance lower bound needed for that stronger conclusion. The descending reverse/ascending forward truncation schedule in III.N.4 verifies the imported Gaussian hypotheses.
- With `p=y/3` and `H=sum_i p_i H_i^L`, the half-sum loss gives readout velocity `3H`, `delta(t)/t -> 3 beta`, hidden parameter velocity divided by `t` tending to `9 V`, and hidden field velocity divided by `t` tending to `9 U` or `9 T`. Thus raw hidden displacement is `(9/2)t² V+o(t²)`.
- The label-direction kernel `p^T K p` receives `9t² ||V||²` from readout change and another `9t² ||V||²` from the hidden blocks. The coefficient is therefore **18**, not the Part I/II coefficient 32. This concerns the specified directional kernel and its own definitions, not a universal entrywise matrix expansion.

The initial accelerations are nonzero for every declared hidden block/sample/layer. Part III does **not** claim every-later-time hidden activity. Its all-time nonaffinity bound `e² c_psi/(16 a^(L-1))` is positive at each separately fixed depth but is not depth-uniform. The appendix [III.A, lines 6013–6398](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:6013) proves why the broad nonconstant `C_b²` class cannot support a depth-uniform margin, then gives an additional uniform Gaussian regression-margin hypothesis and a concrete open class that can. The regression-distance stability argument, compactly supported counterexample mechanism, and open neighborhood construction support precisely those distinctions. There is no uniform-in-width theorem over an infinite activation class, no joint depth/width limit, and no positive margin uniform as `e -> 0`.

## 6. Cross-chapter claim boundaries

The interfaces above support the following differences; they should not be erased when reusing a result.

| Topic | Established scope | Unjustified extension avoided by the supplied text |
| --- | --- | --- |
| Dense model/depth | Each nonlinear/linear theorem's specified fixed hidden depth or every separately fixed depth | Joint dense depth/width theorem |
| Data | One sample; the explicit two-sample angle/label cases; or the admitted three-sample geometry | Arbitrary correlated dense batches |
| Readout | Small stored readout for canonical nonlinear limits; order-one readout in Gaussian program/linear benchmark | Treating these initializations as interchangeable |
| Gaussian reuse | Fixed-program source identification plus separately proved mesh/cap stability where needed | Substituting a fixed-program theorem for a growing training transcript |
| Restart | Inherited reached action states for nonlinear constructions; stated cyclic affine space for linear flow; whole profile space for continuous depth | Arbitrary-state nonlinear restart without the action/regularity class |
| Observations/topology | Chapter-specific `L²`, `W_p`, path `W_2`, rooted-word/Schatten, or depth-averaged `W_1` statements | Turning all statements into a common neuron-path or operator-norm theorem |
| Fitting | Proved finite optimization, shifted global nonlinear, special II/III, and the stated linear setting | Ordinary-arctangent special I or general continuous-depth fitting |
| Nonaffinity | Initial interval, all times, fixed-depth positive margin, or stronger-class depth-uniform margin as individually proved | Inferring persistence/uniformity from one initial coefficient |
| Activity | All-positive-time in global shifted and special I/II settings; initial acceleration only in special III | Initial motion implies perpetual motion |
| Auxiliary dynamics | Fixed-cap feature flow and finite metric projection under their own equations | Treating either as the global uncut population gradient flow |

The overview [docs/README, lines 33–49 and 74–77](/tmp/pde-integration-round2.vG0oUu/docs/README.md:33) and [special-data final scope, lines 6377–6398](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:6377) are consistent with these actual proof boundaries. In particular, no missing general correlated dense theorem is concealed by reuse of the scalar particle benchmark or of finite-width fitting.

## 7. Implementation, self-containment, and bounded checks

The code advertises a finite-network reference implementation and finite Gaussian polynomial moments, not a simulator of all the population/action-space, projected, or continuous-depth theorems. That claim matches what is implemented.

In [finite_network.py](/tmp/pde-integration-round2.vG0oUu/code/pde/finite_network.py:156), initialization, forward propagation, and residual-free backpropagation match the stored matrix conventions. The first contraction, all middle transposes, and final readout normalization were checked. Mean-loss raw gradients and metric velocities are separate operations. The simultaneous GD update evaluates all right-hand sides at the old state; it does not sequentially update layers or discretize a transformed primitive. Layer kernel formulas agree with the raw Jacobian/mobility contractions, including input Gram `X^T X/d`, normalized hidden products, and the readout block.

The numerical contract is also narrower than exact real arithmetic, as documented. Scalar-factor combination uses mantissa/exponent handling to avoid avoidable intermediate over/underflow, but raw matrix contractions remain ordinary float64 operations. Public results are checked for finiteness, including overflowed loss and total-kernel results, and mutable parameter/input shapes are validated. This is not a guarantee against rounding or underflow. Stable arctangent/tanh derivatives, zero-step behavior, callback copies, and simultaneous-state use agree with the documentation and tests. For custom activations, coordinatewise behavior, the actual derivative, and the required regularity remain caller obligations, not runtime-certified properties. “Exact raw GD” denotes the update formula, not an arbitrary-precision promise.

In [gaussian_moments.py](/tmp/pde-integration-round2.vG0oUu/code/pde/gaussian_moments.py:1), the exact rational PSD check handles zero Schur pivots by checking the remaining row, and the Wick recursion removes one leg with the correct multiplicities. Validation also occurs for moment requests whose final value is trivially zero or one. This is a finite Gaussian-moment routine, not an implementation or independent certification of the adaptive Gaussian-program theorem.

The supplied tests were inspected before execution. They cover finite-difference raw gradients, independently computed output-Jacobian kernels, the energy identity, simultaneous updates, deterministic seeded storage scales, correlated/repeated/conflicting samples, exact Gaussian moments and singular PSD cases, input/numerical contracts, and boundary-checker fixtures. The finite-network numerical cases exercise depths 1–3; arbitrary-depth loop correctness was inspected, not experimentally exhaustively tested.

Bounded validation performed:

```text
Working directory: /tmp/pde-integration-round2.vG0oUu
Command: timeout 60s make check
Runtime: Python 3.10.12; NumPy 1.26.4
Boundary check: passed, 19 docs/code files
Unit tests: 52 passed, 0 failed; reported test time 0.159 s
Process exit status: 0
```

The boundary count excludes the separate Makefile and requirements file; it is consistent with the 21-file audit inventory. The checker was itself read: its link/import/tree checks are useful self-containment evidence, not a mathematical theorem verifier. No dependency installation was needed. No experiment, training sweep, or unbounded test was run.

All 21 input hashes matched their initial values after the check. This confirms byte preservation of the audited input files; it is not merely a claim that no intentional source edit was made.

## 8. Findings and optional refinement

### Required findings

**None identified.** In particular, I did not find an unverified specialized theorem import, a clock/readout/depth substitution, a missing layer factor in the requested special-data initial-motion interfaces, an unsupported transfer of all-time activity, or an implementation-equation mismatch requiring correction.

### Optional O1 — give a local regression remainder a non-residual letter

At [special_data_limits.md:5508](/tmp/pde-integration-round2.vG0oUu/docs/special_data_limits.md:5508), `r_i = phi(Z_i)-mu_s-b_s Z_i` denotes the local Gaussian regression remainder. The canonical residual elsewhere is `r_i=f_i-y_i` ([NOTATION.md:31](/tmp/pde-integration-round2.vG0oUu/docs/NOTATION.md:31)). The remainder is explicitly defined and used locally in the subsequent Gram decomposition, so I found no mistaken sign, derivative, or training-residual substitution. The notation policy permits explicitly typed local auxiliaries; this is therefore **not** a required correction. Renaming it to a regression-specific symbol would make that proof slightly easier to scan across chapters.

No inputs were changed to implement this suggestion.

## 9. Immutable SHA-256 manifest

These are the exact audited bytes, recorded before bounded validation and confirmed unchanged afterward. Paths below are relative to the immutable input root. The generated report is intentionally not included in its own input manifest.

```text
740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
f7d3d22e48aac6ed90d4b041c317b10ecf99a538e02e09cf5183fd46d25af95a  docs/README.md
19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead  docs/arctan_limits.md
0930e1b2a4c219749cd1994ffb657093aea0a103b2d4a414c21bd697604d5362  docs/continuous_depth.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
a12a4f2541dd989a01920541f07ce8f80058b88d3e19db65c4b376c1fcf6653e  docs/finite_optimization_and_controls.md
cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e  docs/gaussian_calculus.md
becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95  docs/global_nonlinear.md
36988f8175a433264671e1d980df752c8c52b34e1802de1c3d560d3ed3d8f41b  docs/linear_dynamics.md
e491ea163cf325ced50a3f1d19ab79cf9f84df85977ad644b68f4c96775e36ea  docs/special_data_limits.md
0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6  code/tools/check_library.py
```
