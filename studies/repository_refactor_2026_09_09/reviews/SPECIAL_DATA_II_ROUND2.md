CLEAN

# Fresh adversarial proof audit: Part II

Theorem II.1 and its proof pass this audit. I found no mathematical gap requiring a correction in the assigned proof or in the dependencies it uses. This is a verdict about the supplied argument for the fixed two-sample, three-hidden-layer, equal-label model, with its stated initialization, clocks, convergence modes, and restart class. It is not a whole-chapter verdict or a claim about other models.

## Input identity and isolation

Exact SHA-256 hashes, identical at the initial read and the pre-write verification:

| Mathematical input | Lines | SHA-256 |
|---|---:|---|
| `/tmp/pde-special-II-round2.vHrub9/special_data_limits.md` | 6397 | `42d7acebd0e7c712a122022c42e1b92483fba7e8c6912b670e117a2a87af2c97` |
| `/tmp/pde-special-II-round2.vHrub9/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

These were the only mathematical/project inputs. I did not inspect the repository, history, other reviews, other agents, or outside mathematical sources. No experiment was performed and neither input was edited. The procedural skill read was `/etc/codex/skills/solve-math-rigorously/SKILL.md`; it supplied an audit procedure, not mathematical premises. This review was created with `apply_patch`.

## Full read coverage

All ranges below were read in full. Truncated tool displays were supplemented by overlapping reads of the omitted material. References below without a filename refer to `special_data_limits.md`.

| Range | Coverage and use |
|---|---|
| `NOTATION.md:1–98` | Entire notation contract, including raw storage, residual-free backward fields, layer types, metrics, clocks, and limit scope. |
| Chapter `1–126` | Entire opening and conventions; initialization, canonical/raw storage conversion, summed-loss physical clock, interpolation conventions, and stated scope of III.F. |
| `2087–2143` | Theorem II.1 and all its claims and quantifiers. |
| `2144–2340` | Entire II.A: finite geometry, gradient/kernel identities, singular input geometry, exchange symmetry, and label-mode clock. |
| `2341–2658` | Entire II.B: finite Euler source law, identification, formal derivative convention, bootstrap, and both query envelopes. |
| `2659–3159` | Entire II.C: common state, first-row reconstruction, capped existence, two-cap comparison, cap removal, restart, physical GF/GD, observation closure, uniform velocities, paths, and increments. |
| `3160–3498` | Entire II.D: forward separation, marginal tails and nonaffinity, backward nondegeneracy, all-layer motion, initialization closure, and quadratic expansions. |
| `3777–4103` | Entire III.F.1–7: the finite Gaussian theorem and its proof, singular regularization, scalar feedback, common spaces, and actual adjoints. |
| `4104–4278` | Entire III.F.8–10: Hilbert–Schmidt geometry, strong multiplier/curve rules, and scalar differentiability. |
| `4279–4318` | Entire III.F.11: local contraction, Euler estimate, and observation/derivative scope. |
| `6376–6397` | Entire final scope statement. |

Thus the complete required Part II range `2087–3498` and dependency range `3777–4318` were covered: 2102 chapter lines and all 98 notation lines. No other chapter range was needed. In particular, the Part III-specific capped gates and later derivative estimates mentioned in III.F.11 are not premises of Part II: II.C gives its own capped field, and II.D.5 gives its own derivative-valid truncation. Their applications elsewhere were not audited.

## 1. Model, normalization, and finite identities

**Verified:** opening `21–119`, II.A.1 `2148–2234`, and the notation contract agree.

The canonical first weight is `W^(1)=sqrt(d)V^(1)`. Its metric `||dW^(1)||_F^2/n` becomes `d||dV^(1)||_F^2/n`; therefore the first mobility in V storage is `n/d`, not `n`. Hidden matrices retain their actual `N(0,1/n)` initialization and ordinary Frobenius metric. The stored readout has entry variance `n^-2`, output normalization `1/n`, and metric `||dW^(4)||^2/n`. Its finite initial RMS is `O_P(n^-1)`, whereas its population initial value is zero.

With the residual-free convention `delta=n partial f/partial z`, differentiating one prediction gives the four differentials at `2180–2183`. Applying the inverse metric gives exactly

\[
\nabla f_a=\left(\delta_a^{(1)}x_a^T/d,
 \delta_a^{(2)}(h_a^{(1)})^T/n,
 \delta_a^{(3)}(h_a^{(2)})^T/n,h_a^{(3)}\right).
\]

The summed-loss field is `-2 sum_a r_a grad f_a`. Its first sample-coordinate update is consequently `-2 eta sum_a G_ba r_a delta_a^(1)`. The four kernel formulas in II.A.2 have the correct normalizations: the first contains `G_ab`, each middle block contains two normalized pairings, and the readout block contains one. They are actual gradient Gram matrices, so positive semidefiniteness, `dot f=-2Kr`, and `dot L=-4r^TKr` follow without an entrywise-positivity assumption.

The finite GF continuation argument is valid. On an existing solution, `||dot theta||_raw^2=-dot L`. On any subinterval `[u,v]`, its displacement is at most `sqrt((v-u)L(0))`. This makes a finite-time endpoint Cauchy; finite-dimensional local smoothness then continues the solution. The identities are not incorrectly treated as exact prediction updates for GD.

For `-1<rho<1`, the in-span first-row metric is the stated `G^-1` quadratic form. At `rho=-1`, `x_2=-x_1` forces `Z_2^(1)=-Z_1^(1)`, and the one-field metric applies. The reconstruction in `2699–2722` gives the exact original first row, preserves its frozen orthogonal component, and recovers its raw speeds. No inverse of a singular G is used. Constants may depend on a fixed rho; no angle-uniform assertion is needed.

The opening clock conversion is correct: summed loss for two samples is twice mean loss. Thus the actual step is `n^-2` in the theorem's physical time, corresponding to mean-loss step `2n^-2` and mean-loss time `2t`. The feature clock `ds/dt=4(1-g)` has the additional factor arising from `g=(f_1+f_2)/2`. It is neither the one-sample clock nor an exact finite optimizer clock. There is no nonlinear coordinate transformation in Part II.

## 2. Exchange symmetry and the role of determinism

**Verified:** II.A.2–3 (`2236–2340`) and II.C.3 (`2853–2862`).

The Householder reflection is defined because rho is strictly below one; equal input norms make it exchange the two inputs. Together with the indicated readout sign it is a linear isometry of the raw parameter metric, preserves the appropriate loss, and preserves the initialization law. Equivariance gives symmetry in law at finite width, not equality of the two finite residuals.

Part II obtains deterministic limiting scalar observations from the proved finite-program construction and subsequent flow comparison. Only then does sample exchange force equal limiting predictions and equal sample moments. This is a sufficient route to the same-label reduction; it does not need to infer samplewise equality from a random symmetric limit or assume an unproved physical symmetry. For equal negative labels, simultaneous label/readout reversal preserves all hidden equations and raw norm statements.

On the limiting same-label path, `dot theta=4(1-g)grad g` follows in the full raw metric. The manuscript postpones division by `1-g` until a feature flow has been constructed. The broader opposite-label identities in II.A are not used to claim opposite-label global existence.

## 3. Adaptive Gaussian empirical laws: the dependency was checked

**Verified:** III.F.1–7 (`3777–4103`), rather than assuming Theorem III.F.1.

### Conditioning and empirical averaging

The conditional law in III.F.3 remains valid for adaptive inputs. At each call the input is measurable from the already revealed transcript. Conditional on that transcript, the answer is a linear observation of one matrix. Induction therefore preserves the product of the conditional matrix laws and imposes precisely the revealed linear constraints. This argument does not require independence of a query from an unrevealed original matrix.

For constraints `WV=Y`, `W^TU=Q`, the displayed mean M satisfies both constraints using `U^TY=Q^TV`; it is Frobenius-orthogonal to all homogeneous solutions `P_(U-perp) K P_(V-perp)`. Isotropic Gaussian projection gives the stated residual matrix law. Applied to a new h, this gives III.F.7 with the displayed least-squares and reverse-response coefficients.

At a fixed finite transcript, removal of `P_U g` costs normalized mean square `rank(U)/n`; its multiplying variance is bounded in probability. After replacing convergent coefficients, the new answer is an old-node linear combination plus fresh independent coordinate Gaussians. Conditional variance bounds prove convergence of bounded tests. The explicit expansion of its empirical square, including the conditional variance of the cross term, proves second-moment convergence. Together these give same-layer joint Wasserstein-2 convergence; no iid assertion about trained coordinates is substituted for this calculation.

The Gaussian operator bound used here is independently justified in III.F.2: two 1/4-nets of cardinality at most `9^n`, the factor-two net approximation, and the scalar Gaussian tail at threshold five give the stated probability bound for norm ten. Its exponent is negative. Only finitely many initialized matrices are needed. The accompanying moment and independent Gaussian trace-probe identities are valid; a trace theorem is not an additional premise of the Part II response calculation.

### Source covariances and response derivatives

In the source-rule proof, orthogonality of `h_perp` to old forward inputs removes the old forward response terms from `E[q h_perp]`. Gaussian integration by parts gives

\[
E[\zeta h_\perp]=G_U E[\nabla_\zeta h_\perp].
\]

The bounded first derivatives of a fixed program make these derivatives integrable, including after conditioning on its roots and other independent source groups. The least-squares contribution cancels the old response coefficients. The remaining answer is precisely the new centered Gaussian source plus the contracted expected source derivatives. The covariance of that source is the **full input second moment**, not the variance left after subtracting a response. Its covariance with earlier sources is likewise the full corresponding input contraction.

Different oriented Gaussian source groups can be independent while actual forward and transpose answers remain dependent through their response terms. The manuscript retains those terms. It also holds previously selected deterministic coefficients and covariance parameters fixed when differentiating the formal scalar expression, as required by the proof.

### Singular Grams

The fresh-noise regularization at every call supplies a new same-orientation query direction with limiting squared orthogonal distance at least `epsilon^2`. The new noise is independent of the entire preceding transcript. This proves the positive-definiteness needed for the provisional conditioning induction at fixed epsilon.

The finite perturbed/original comparison is a fixed-length Lipschitz induction on the initialized norm event, giving RMS error `C epsilon`. To remove epsilon in the scalar law, the proof uses convergence of covariance **square roots** and convergence of the bounded formal derivatives. Its causal induction keeps the earlier coefficient list bounded, supplies a common linear-growth envelope for node values, and a bounded envelope for source derivatives. Thus both second moments and expected derivatives converge. This avoids an unjustified continuity claim for pseudoinverses at rank loss.

The width-then-epsilon triangle inequality gives full-sequence convergence in probability. The additional null-space identity in III.F.14 correctly explains why contracted corrections are independent of admissible formal extensions on a singular Gaussian support. In particular, a zero-variance source slot must not be deleted before differentiation. II.B.2 explicitly retains the zero-time slots with nonzero reverse derivatives.

### Common actions and applicability to Part II

The countable language has consistent finite marginals because any finite union of instructions is itself a finite program with the same matrices and roots. The norm-ten inequality passes to every generated input and every rational combination. It makes answer assignments linear and well-defined on L2 equivalence classes. Smooth cylinder functions give density in the generated L2 spaces, so the assignments extend to bounded actions. Passing the exact finite transpose pairing on a dense set makes the reverse actions their genuine Hilbert adjoints. No cross-width operator-norm convergence or independent reverse resampling is claimed.

The scope includes three populations, two adjacent independent Gaussian matrices, an arbitrary fixed finite bottom root tuple with the prescribed internal dependence, and the optionally augmented full Gaussian first row. Hence it includes `rho=-1`. At fixed caps and fixed Euler length, Part II's gated products have globally bounded-derivative extensions; the readout is pointwise bounded by `aS` and can be truncated outside that attained range. The finitely many empirical contractions are handled by the causal scalar-feedback comparison in III.F.6. These are the actual hypotheses of the proved theorem. No invocation has a transcript length growing with width.

## 4. Identification and quantitative two-query bootstrap

**Verified:** all of II.B (`2341–2658`).

Unrolling each matrix update gives the forward learned coefficient `(Delta/2)y_b E[H_ka H_rb]` and reverse learned coefficient `(Delta/2)y_b E[delta_ka delta_rb]`. III.F's initial-action response rule supplies the other terms of A and B in II.B.2. Forward responses involve strictly earlier reverse calls; reverse responses include the currently available forward sample calls. This matches the causal ordering of the simultaneous two-sample Euler step.

The bounds `c_-=5/6`, `a=7/6`, `epsilon=1/10`, `|phi''|<=1/5` are valid for the fixed shifted arctangent. The bootstrap order is noncircular: past U,V bound A2, then A3 and the top fields; the current V is established before the current U is used.

Specific checks:

* A single bottom reverse-source injection has size at most `Delta epsilon/2`. Multiplication by the feature gate gives `Delta/200`. The feedback coefficients give exactly the exponent in II.B.6. The absolute row sum of `G/2` is at most one, including both singular endpoint Grams allowed in this estimate.
* Past middle queries satisfy `||q2||_2<=aS/10+a=161/120`. The bottom source standard deviation is therefore at most `161/1200`. The two-sample Gaussian maximum bound has prefactor four. Jensen over time requires no temporal independence. Its exponent is bounded by `73/200+(9/200)(161/1200)^2<2/5`, so the claimed bound `E E1<6` is valid.
* Consequently `|A2|<(Delta/2)(49/36+3/50)<(3/2)Delta/2`.
* A current forward-source row has one direct derivative, not one per sample. Summing the two update samples converts `Delta/2` to Delta. This yields the middle sensitivity bound and the single reverse-source injection `A Delta/200` after the feature gate.
* The middle exponential moment has exponent `219p/400+3969p^2/1280000`. It gives `E E2<8` and `||E2||_2<7/2`. The numerical inequalities used for the latter are strict. Hence `|A3|<(Delta/2)(49/36+3/25)`, and `49/36+3/25=1333/900<3/2` supplies the required margin.
* Differentiating both the top readout history and its current gate gives the two terms in the top derivative row, bounded by `(73/300)S max T`. Gronwall yields `max T<=exp(657/800)<5/2`. Adding the learned covariance row gives `V<=73/80+147/3200=3067/3200<1`.
* The sharpened current middle query bound is `Q_*=7/40+(7/6)(3067/3200)=24829/19200`. It is available before bounding current U. Cauchy–Schwarz with the middle sensitivity bound and the learned covariance row gives

\[
U\le\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
       +\frac3{200}Q_*^2
 =\frac{71063018523}{73728000000}<\frac{97}{100}<1.
\]

The exact rational arithmetic checks. The covariance contribution has one time factor S and the gate-square factor `1/100`; there is no missing factor of two.

Each actual reverse query is its Gaussian source plus a correction of absolute value at most a. Both source variances are at most `(7/40)^2`. Without assuming independence of the correction and source, `q^2<=2 zeta^2+2a^2` and the one-dimensional Gaussian integral give the stated envelope `E exp(q^2/16)<2`. Thus both multipliers needed for cap removal are controlled, uniformly in caps and mesh.

## 5. Existence, both-cap removal, and restart

**Verified:** II.C.1–3 (`2666–2914`), with the elementary Hilbert and differentiation arguments in III.F.8–11.

Bounded activation gives the readout bound first, then the W3 bound, then the W2 bound, and finally the bottom velocity bound. This order uses `|tau_R(q)|<=|q|` and gives cap-independent primal and velocity bounds on each fixed feature interval. For the zero-readout flow, `|W4(s)|<=as` holds pointwise.

At fixed cap, the top backward difference is controlled by state distance by expanding around the reference readout, which alone has to be pointwise bounded. The middle gate difference costs R; its query difference does not. The bottom gate has one separate R cost, while its incoming query difference retains a bounded gate coefficient. Thus the total Lipschitz coefficient is `C(1+R)`, not `CR^2`. Picard iteration can be restricted to the closed continuous-path set preserving the readout bound; the integral map preserves that constraint. The primal bounds permit continuation, and the fixed-cap Euler error is width-independent on the initialized norm event.

The same expansion with a larger cap, including no cap, proves II.C.3. The two error terms are precisely the tails of the reference's actual top query and its middle-capped bottom query. No tail assumption is imposed on the comparison state. The difference of cap functions is bounded by `4(|q|-R/2)_+`; the gate expansion uses the smaller reference cap. This is why the coefficient stays linear in R uniformly in the larger cap.

The exponential envelope passes from Euler laws to each cap flow by strong convergence and Fatou. From `E exp(q^2/16)<=2`, the displayed tail calculation gives

\[
\|(|q|-R/2)_+\|_2\le8e^{-R^2/256},\qquad
e_R\le32e^{-R^2/256}=\epsilon_R.
\]

Gronwall therefore makes all caps Cauchy with error at most `CS exp(C(1+R)S)epsilon_R`. Its Gaussian decay beats every fixed linear-in-R exponential. Top stability, then the middle and bottom tail comparisons, identify the limiting **uncut** queries, backward fields, and vector field. Passing the integral equations gives a strong C1 feature flow on the full interval `[0,3/2]`.

Rank-one differences obey the same factor estimates in Hilbert–Schmidt norm. Hence the trained increments belong to the raw affine Hilbert space and the limiting field is a raw Hilbert field, not merely an operator-norm solution. The initialized actions themselves need not be Hilbert–Schmidt.

A bounded-primal uncut competitor can be compared with the same capped reference. Its possibly larger fixed constants still lose to `epsilon_R`. At a reached time, the reference's initial error is the already established cap-removal error; one further Gronwall factor does not obstruct its removal. This proves uniqueness and restart without assuming tail bounds for arbitrary competitors.

The scalar predictor is continuously Fréchet differentiable even though the L2-valued activation map need not be. The weighted scalar remainder bound in `2869–2875` (proved more generally in III.F.10) uses a fixed L2 incoming factor, truncates it, and gives `o(||v||_2)`. Downward adjunction and quadratic cross terms identify the raw gradient. Bounded multiplier continuity proves gradient continuity. Thus the uncut feature field is indeed `grad g`.

## 6. Physical fitting and global physical uniqueness

**Verified:** `2878–2914`.

The readout component gives

\[
g_s=\|\nabla g\|_{\rm raw}^2
 \ge E\left[(H_1^{(3)}+H_2^{(3)})^2/4\right]\ge25/36.
\]

Since `g(0)=0`, there is a unique crossing of level one at `s_*<=36/25<3/2`. The continuous gradient is bounded on the constructed feature interval. If B bounds `g_s`, then `1-g(s)<=B(s_*-s)`. This proves divergence of the reciprocal-clock integral at the crossing, with the correct direction of inequality. Its inverse therefore exists for every finite physical time and remains strictly below `s_*`.

The reparametrized flow is the exact summed-loss raw gradient flow. The physical residual satisfies `(1-g)_t=-4g_s(1-g)`, yielding `1-g<=exp(-25t/9)` and `L=2(1-g)^2<=2exp(-50t/9)`, with `0<=g<1`. Readout feature speed is at least `c_-`, and its physical clock is strictly positive at finite time.

Physical uniqueness is not restricted to symmetric competitors. The physical cut-loss field evaluated at the reference differs from the reference's clocked feature direction by its prediction error. Prediction is Lipschitz on the bounded primal sets. The asymmetric comparison consequently applies to an arbitrary physical competitor with an additional vanishing reference prediction error. This proves the stated full-state physical restart. No infinite-time finite-width fitting statement is inferred.

## 7. Actual finite GF and raw GD

**Verified:** II.C.4 (`2916–2985`).

The finite comparison uses the same initialized first row and hidden matrices as the actual algorithm, zero readout only in the auxiliary capped reference, and the deterministic **population** clock. The real finite readout is restored as an initial `O_P(n^-1)` discrepancy.

At fixed cap, joint Wasserstein-2 convergence and the fixed-cap L2 time modulus give uniform empirical convergence of the continuous quadratic-growth tail measurements. Predictions at each of the two samples converge to the capped population reference and differ from the uncut predictions by the cap-removal error. Splitting the actual residual against these reference predictions controls its off-mode component as well as its label-mode component. No scalar clock is assigned as an identity to the actual finite process.

For GF, the asymmetric field estimate integrates directly. For GD, each parameter and bottom sample-coordinate update is exact raw Euler. The smooth capped reference, together with continuous bounded `s''=-4g_s s'`, has local defect `C_(R,T)eta_n^2`. The resulting error is II.C.8: first width tends to infinity at fixed R, then R tends to infinity. The cap errors remain polynomial/linear-exponential multiples of `epsilon_R` and vanish in that order.

The primal stopping argument is valid. Before a first bad node, the raw velocities are bounded by the stopped primal norms and bounded gates. The step into that node overshoots by at most `C eta_n`; the same comparison is valid through that step. Its vanishing discrepancy contradicts the reserved stopping margin. This removes the stop for both algorithms.

Within a GD step, raw vectors change by `O(eta_n)` in RMS and matrices by `O(eta_n)` in operator norm. A coordinate supremum change of a recomputed preactivation is at most its Euclidean norm, hence `O(eta_n sqrt(n))`. The bounded second derivative controls gate differences. The layer-by-layer product rule then gives the stated vanishing interpolation velocity error for `eta_n=n^-2`. The right-interior-node and terminal-left conventions are consistent with that estimate. The actual growing number of GD steps is handled by deterministic comparison, not by a growing-transcript Gaussian theorem.

## 8. Full observables, uniform speeds, path laws, and increments

**Verified:** II.C.5–6 (`2987–3156`).

The observation proof does not infer uniform integrability from bounded L2 norms. At a fixed cap and finite transcript, it appends true backward probes downwards and velocity probes upwards. For each incoming P it first uses the bounded-derivative instruction `phi'(Z)tau_M(P)`. The error is bounded by a constant times `||(|P|-M/2)_+||_2`. This tail functional is Lipschitz in Wasserstein-2, so empirical convergence of the already identified input supplies convergence of the error at fixed M; its population limit vanishes as M grows. Later gates are handled with the indicated ordered caps. Bounded L2 action norms suffice throughout; an Lp operator bound for p greater than two is not assumed.

The deterministic velocity comparison II.C.o2 is valid. At an upper layer,

\[
P_\ell=\dot W^{(\ell)}H^{(\ell-1)}+W^{(\ell)}U_{\ell-1}.
\]

The P difference costs state and raw-direction discrepancies plus the preceding U difference. At a gate, truncate only the reference P. The new M multiplies the current **forward state** difference, not the preceding velocity error. Thus induction gives the claimed single `(1+M)alpha` factor and reference tail sum, with no depth-generated power of M. The downward backward-field comparison has the same structure.

Strong multiplier continuity and the curve chain rule prove continuity of the population velocity curves in L2. Their compactness on a fixed time interval gives uniform tail removal by a finite L2-net and the Lipschitz tail functional. This closes the otherwise nontrivial passage from fixed-time laws to uniform-time velocity observations.

The order of limits in II.C.6 is sufficient: fixed training cap and observation cap, width limit, mesh refinement, and observation-cap removal; then training-cap removal using the uncut compact L2 velocity curve. For actual physical GF/GD the state and direction comparison is used against the finite capped reference, and the reference tails pass through its uniform laws before the final observation cap is removed. No uncontrolled cap-dependent moment constant is multiplied by a small state error.

Second-moment joint laws yield the kernel entries and raw/hidden squared speed norms; products of converging scalar contractions are harmless. Uniform convergence of squared speeds gives their integrated energies. For preactivation paths, the coordinatewise interpolation estimate

\[
\|z-I_\pi z\|_\infty^2\le4|\pi|\int_0^T|\dot z|^2
\]

and its empirical/expected version reduce path Wasserstein-2 convergence to finite-grid joint laws and uniform integrated speed bounds. Both samples can be treated as a two-component path. Lipschitz activation transfers the conclusion to features.

For operator increments, the Hilbert–Schmidt inner product of two rank-one terms is the product of their two within-layer pairings. Continuous integrands and the already proved cross-time contraction convergence justify finite Riemann sums and mesh removal. This proves the asserted scalar norm and cross-time increment observations. It does not compare different-width operators in operator norm or pair neuron coordinates across layers. The first-row reconstruction supplies the corresponding canonical first-weight observations.

## 9. Persistent nonaffinity

**Verified:** II.D.1–2 (`3169–3278`).

The bottom displacement dominator depends only on reverse Gaussian sources, not on the bottom Gaussian root pair. Its expectation is below `1/5`. Consequently its event of being at most one has probability at least `4/5` and can be intersected independently with `G_1>=2,G_2<=-2`. The latter has positive probability at every allowed rho, including `rho=-1`. This gives a strictly positive first-layer feature-difference second moment.

Sample exchange makes the two feature diagonal moments equal. The sum mode is bounded below by positivity of phi, and the difference mode by that separation event. Thus the first feature second-moment matrix is positive definite even when the input Gram is singular.

The middle displacement dominator uses the middle reverse source group, which is independent of its forward source group. Its expectation is `483/1600<1/3`. The forward source covariance has eigenvalues between the positive first-feature lower bound and `2a^2`, giving the stated uniform positive Gaussian rectangle probability. This yields middle feature separation and a positive lower eigenvalue for the next forward source covariance.

At the top the deterministic correction is bounded by `A a epsilon S^2=63/160<2/5`; no independence of that correction from its source is required. This supplies top feature separation. The Gaussian density lower bound used for these rectangles has the correct determinant and inverse-covariance directions.

The same dominators give both unbounded marginal tails at every fixed level, uniformly over the constructed interval. Strong joint convergence transfers their closed-event lower bounds through mesh and cap removal; the Portmanteau direction used in the text is correct.

For each marginal, the L2 affine minimizer exists because `Var(Z)>0`. If its error were zero, bounded phi and unbounded support of Z would force the affine slope to be zero; strict monotonicity would then force Z constant. This is impossible. The regression expression is continuous along the L2 path, so its strictly positive value has a positive minimum on every compact interval. Uniform empirical moments and a variance bounded away from zero transfer the assertion to empirical regression errors. This establishes the claimed absolute nonaffinity for the fixed activation, without asserting a margin uniform in rho or over infinite physical time.

## 10. Strictly positive motion at every positive time

**Verified:** II.D.3–4 (`3280–3368`).

For positive feature time, the common readout is pointwise at least `c_-s`. On the top Gaussian rectangles `[4,5] x [-1/10,1/10]` and its swap, the bounded correction gives the displayed gate-ratio separation and a positive lower bound `b_0` on the larger delta. For any unit coefficient vector, choose the rectangle where its larger coefficient multiplies the larger delta. The smaller delta can cancel at most one quarter of that contribution. This gives the lower bound `9p(rho)b_0^2/32` for the top-delta second-moment matrix. Taking approximation times bounded away from zero makes this bound survive the limits.

That positive-definite matrix is the covariance of the middle reverse **source**. A Gaussian with this covariance has positive probability in every signed rectangle beyond the bounded response shift. Hence the actual middle query has positive probability in all four nonzero signed quadrants. Multiplication by the strictly positive gate preserves the signs. Choosing a quadrant aligned with any proposed nonzero constant linear combination proves that no such combination of middle deltas vanishes almost surely. Its second-moment matrix is positive definite. The same argument with its covariance as the bottom reverse-source covariance proves bottom-delta positive definiteness. Training caps are removed using the previously established strong field and second-moment convergence.

For the first hidden parameter block,

\[
K_g^{(1)}=\tfrac14\operatorname{tr}(G D_1)>0,
\]

because `D_1` is positive definite and G is positive semidefinite with trace two. This remains strict when G has rank one at `rho=-1`. For each middle block, the analogous trace product pairs a positive-definite delta moment matrix with a feature Gram matrix of positive trace. Thus every hidden raw parameter block has positive feature speed.

Nonzero parameter speed alone would not establish hidden field motion. The proof supplies the necessary additional identity:

\[
\tfrac12\sum_a E[\delta_a^{(j)}(Z_a^{(j)})']
       =\sum_{\ell\le j}K_g^{(\ell)}>0.
\]

At each layer the trained rank-one term contributes its own kernel block; adjunction of the propagated term gives the preceding-layer identity. This verifies the telescoping calculation. At least one sample velocity is therefore nonzero at each layer. Exchange symmetry of the deterministic joint derivative laws gives equal sample velocity norms, so both are nonzero. Strictly positive phi' then gives nonzero feature velocities. The positive finite-time physical clock preserves all these strict statements; it also gives strict readout motion. Initial hidden speed remains zero because the initial population readout is zero.

## 11. Initialization derivatives and quadratic motion/kernel terms

**Verified:** II.D.5 (`3370–3497`).

At initialization the top pair is nondegenerate, and `V_0=(H_1^3+H_2^3)/2>=c_-`. The same gate-ratio rectangles prove positive definiteness of the beta3 moment matrix. The first initialized transpose query has the response coefficient obtained by differentiating `V_0 D_a^3`:

\[
R^2_{ab}=E[\tfrac12D_a^3D_b^3+
                 1_{a=b}V_0\phi''(Z_a^3)].
\]

The resulting q2 is Gaussian plus a bounded correction. For the next transpose, the proof uses `D_a^2 tau_M(q_a^2)`, not the unbounded product as an unsupported bounded-derivative instruction. Its displayed derivative has a uniform `C(1+|q_a^2|)` dominator. Dominated convergence therefore identifies R1, while strong L2 input convergence identifies the source covariance. Covariance-square-root coupling and bounded action continuity identify the actual uncut answer. The finite input error is controlled in the width-then-M order. This establishes the initialized two-transpose closure empirically and on the canonical actions.

The source covariances are the beta input second moments. Bounded response shifts and positive gates transfer positive definiteness down both layers, as in the positive-time argument. The trace-product calculation consequently makes every component of `B=D_0^*V_0` nonzero, including the singular-input first block.

Let `Gamma_ell=||B_ell||^2` and `Gamma=sum Gamma_ell`. Readout integration gives `W4(s)/s -> V_0`; downward strong multiplier continuity then gives `alpha'(s)/s -> B`. Thus `alpha(s)-alpha(0)=s^2 B/2+o(s^2)` in the raw hidden norm. Only strong action on these convergent directions is needed. There is no claim of operator-norm differentiability of an L2 Nemytskii map.

The strong forward chain rule gives `V'(s)=sD_0B+o(s)` and `E[V_0D_0B]=||B||^2=Gamma`. Therefore the readout-mode kernel has quadratic coefficient Gamma, the sum of hidden-mode kernels has coefficient Gamma, and the full label-mode kernel has coefficient `2Gamma`, exactly as in II.D.5.

The analogous forward velocity expansion, paired with the telescoping identity divided by `s^2`, gives nonzero leading preactivation velocities at each layer. Symmetry makes both sample coefficients nonzero; the positive initial gates give the feature coefficients. Finally `s(t)=4t+o(t)` converts the feature displacement coefficient to `8t^2 phi'(Z_0)T`, the output-mode kernel coefficient to `16Gamma t^2`, and the full-mode coefficient to `32Gamma t^2`. These factors are consistent with the theorem's physical clock.

## Required issues and limits of the verdict

**Required issues: none.** No exact line or dependency in the audited scope needs a mathematical repair for Theorem II.1 as stated.

The verdict specifically retains the restrictions that the proof uses: fixed data and rho, fixed depth three, same labels, the fixed shifted-arctangent activation, zero *limiting* readout with the actual finite small Gaussian readout restored, and each fixed finite physical horizon. It does not assert a growing-time/width limit, uniformity over rho approaching one, an opposite-label global theorem, a convergence rate for the full width limit, or convergence of infinite-time finite-GF/GD endpoints. All path Wasserstein claims audited here are order two. Canonical actions and scalar increment observations are not cross-width operator-norm convergence.

The potentially dangerous transitions—adaptive empirical averaging, formal derivatives at singular source covariances, both reverse-query tails, linear-in-cap comparison, asymmetric restart, off-mode finite residuals, actual raw interpolation, uniform integrability for velocity observations, and the passage from parameter motion to both samples' hidden motion—have explicit arguments in the supplied text and withstand the checks above.
