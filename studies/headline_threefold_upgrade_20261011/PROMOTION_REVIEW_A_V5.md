# Independent scientific promotion review A — frozen version 5

**Verdict: PASS for the stated theory and exact-real algorithm-complexity addition.** No required scientific correction or missing scientific input remains in this review. This is not approval to integrate, a whole-book integration review, an empirical reproduction, or a finite-precision certification.

## Role, independence, and input identity

Reviewer: `/root/promotion_science_a_v5`. I am distinct from the three named authors/assemblers and the relevance selector. I received the neutral version-5 assignment in a fresh context, without author discussion, prior versions, study history, prior verdicts, or another reviewer's findings. I did not request an author's explanation. I did not read the study README, source notes, other studies, archived book, producer implementations, or other review reports. No reviewer delegation was used.

Scientific inputs were exclusively the five frozen files below in `data/generated/headline_threefold_upgrade_20261011/promotion_v5/`. Process inputs were the assignment, `RESEARCH_WORKFLOW.md`, the rigorous-math skill, the canonical-notation skill, and its neural-response-memory reference. The initial wildcard line-count/hash command exposed other frozen file names, lengths, and hashes only; their scientific contents were not read.

| Input | SHA-256 |
|---|---|
| `docs/08b-trajectory-compression.qmd` | `7363ea5815ed592ce33b0b4b2185539358348f21f3e3b264caa68620a2d5f460` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `chapter.diff` | `76f17ece3582b944a78c9e6e1282f56d99194e1460074ac7dc1aad8e6e506816` |
| `inputs.sha256.json` | `c6c5c124dafb8f42f61beba15e527226f9abaa7862acfcdb78361b93b15bc483` |
| Neutral assignment outside packet | `ba74aee8bacdc9fa591a0816fc3fbcd085b368b04bea1b088ff873faec9e52cd` |

The manifest deliberately distinguishes the established chapter from the proposed chapter. The frozen chapter matches its `proposed/docs/08b-trajectory-compression.qmd` entry. Independently reversing all nine supplied diff hunks, using only the frozen candidate and diff, produces SHA-256 `405c8e0a4d99d8b5bebcb4c13d5534317050aa0a10d33b0476b9d90c9cc5bdf5`, exactly its established-chapter entry. This establishes the two identities without consulting an earlier version. Every context/addition line of every diff hunk matched the candidate.

## Complete reading record

I read all 7,954 lines of the candidate, including unchanged proof bodies. The principal consecutive reads were lines 1–850, 851–1750, 1751–2650, 2651–3550, 3551–4450, 4451–5350, 5351–6250, 6251–7150, and 7151–7954. The 6251–7150 response was truncated around the angular-domain/quadrature passage; separate reads of 6680–6735 and 6730–6810 restored that passage. No unread chapter interval remains.

I read the complete 260-line index and 98-line notation contract. I read the complete 3,007-line diff in intervals 1–1050, 1051–1550, 1551–2150, 2151–2600, and 2601–3007. The first interval's truncated middle was reread at 350–620. The full hash manifest was reread after its initial combined output was truncated. The promotion-process text was repaired by rereading workflow lines 175–300 through EOF. Both required skills and the linked neural-network reference were read completely.

These reads covered the original fitting and signed-stability arguments; the complete cavity, trace, budget, and analytic-domain proof; both Legendre estimates; both dense-fluctuation proofs; sparse selection, corrected dynamics, and comparison; initialized-jet continuation; sphere and panel approximation; all numerical setup, sampler, and cost proofs; nonlinear-learning certificates; and final assembly. The unchanged nonlinear-learning section was read even though the new polynomial-width theorem explicitly excludes quantitative onset for those additional certificates.

The only external chapter link relevant to the opening comparison is Chapter 7's separately scoped storage theorem. Neither new proof uses it. The index's literature links are orientation only. I found no additional cross-chapter scientific proof input requiring retrieval. Elementary finite-dimensional Gaussian conditioning, spectral decompositions, Cauchy estimates, polynomial orthogonality, and the stated classical density/continuity facts suffice for the arguments inspected here.

## Scope and model checks

The reference is the finite nonlinear network with independent first entries of variance one, hidden entries of variance `1/n`, and exactly zero stored readout. Its loss is the sample mean of squared residuals, and the mobility factors are `(n,1,...,1,n)`. Thus in the ordinary Euclidean coordinates

\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},W^{(L+1)}/\sqrt n)
\]

the field is `-2/m` times the sum of residual-weighted prediction gradients. The normalization in the displayed gradient blocks, hidden outer products, and initial derivative `2/(mn)` is consistent. Residuals never enter the definition of the backward derivative.

The allowed activations have linear growth; bounded activation values are not assumed. Bounded strip derivative and Cauchy's estimate supply the smaller-strip second and third derivative bounds used in the proofs. A positive uncentered final population Gram gap is assumed, not inferred from arbitrary data. Intermediate Grams may be singular. No whitening, input-rank condition, or label sign enters the new claims. The small-label restriction is retained throughout.

Legendre and Harmonic promise the whole sphere; Taylor promises only a finite panel declared before initialization. Its exact input-span reduction preserves normalized inner products, first-layer Gaussian laws, and all panel predictions. The passive inputs add source vectors but no residuals, labels, or rows of the training Gram inverse. The norm includes every physical time and the parameter-limit endpoint. The denominator is actual independent-run variability, witnessed at positive training time; the training endpoint itself has no such lower bound.

All probability statements remain at one individual width for fixed deterministic problem data. The new explicit sufficient widths expose problem-parameter dependence but do not claim one event over infinitely many independently initialized widths. Counts are real coordinates and primitive exact-real operations. Setup constants in the four-row table may depend on the whole fixed problem; the retained-state constants have the narrower dependence stated in the chapter.

## Finite-width probability and actual dense separation

### Initialization and the finite source event: PASS

Locations: lines 242–532, 533–2326, and 3290–4065.

I reconstructed the fitting bootstrap from the readout Gram contribution. With `lambda=gamma/m` and residual RMS `rho`, the stopped energy inequality is

\[
-(\rho^2)'=\|\dot\theta\|^2\ge\lambda\rho^2.
\]

Integrating `||theta'||²/rho` and `rho` gives tail length at most `2 rho(t)/sqrt(lambda)`. Hidden velocities contain both residual and readout factors. Their integrated changes are therefore quadratic in the label size, which closes the feature and Gram margins under the displayed cap. Bounded parameters at finite width give global continuation; finite length gives an actual parameter limit. This supplies endpoints independently of source approximation.

For quantitative initialization, Gaussian concentration is applied to empirical norms of one feature or the sum/difference of two features. Their Lipschitz constants are proportional to `n^(-1/2)`, even for singular covariance pairs. Polarization then bounds each covariance error. Shrinking to common marginal standard deviations and integrating the correlation derivative controls the population covariance map without dividing by a marginal variance. The recursions for RMS and covariance errors give the stated `e_0` margin. The sphere net enters logarithmically through `d log(1+2/h_0)`, so its exponential cardinality does not produce an exponential width in `d`.

The cavity proof's independence is substantive. Each coefficient path is stopped and extended using its own retained initialization before a deleted Gaussian root is integrated. The normalized hidden variables use `S=16Y/lambda`; the normalized prediction is the scaled readout paired with features, so no inverse-label derivative is introduced. First-layer incoming rows enter deleted scalar controls, rather than an incorrectly normalized retained reverse port. I checked this against the retained equation and the endpoint exceptions at the top layer.

Differentiating that equation produces the residual-change port, the forward Hessian port, and the reverse lower-Jacobian port. In the nonlinear remainder, localized products contribute `d_0 N`, `d_0 u_0`, and `u_0²`, while matrix cross terms contribute `(N+u_0)²/sqrt(n)`. With the stated stops these give the leading exponent `-0.08`; multiplying by the propagator and finite envelope leaves `-0.07875`, strictly below the nonlinear stop exponent `-0.04`. This is a strict first-exit improvement, not a presumption that the linearization remains valid.

I checked that the exponential variational factor spends the label allowance before the confidence moment order is chosen. The residual-Hessian coefficient of `log n` is bounded by `1/4000`; no growing confidence parameter occurs in that exponent. The Schatten trace calculation uses rank at most `n` for each forward/Hessian factor, not the full parameter-space dimension. Reciprocal exponents sum to one, so the trace normalization is `1/n`. The three leading nonzero contractions and the small residual-change trace are retained; adaptive substitution is performed only after the uniform Gaussian bounds. It is not legitimate to call the actual adaptive inserted variation centered Gaussian, and the candidate does not do so.

The finite endpoint grid addresses a possible independence failure. Grid points are clamped only at the cavity's own stop. The uniform family also includes deterministic prefix levels. Only afterwards is a full-network common prefix selected. The canonical contours lie in that prefix, and interpolation uses the actual analytic solution along a short retracted segment. Thus the proof never conditions a deleted root on survival of the full path.

The numerical exponent ledger is internally consistent: `A ell^16 <= n^(1/1000)` follows at the supplied `(A/rho)^40000` gate by taking logarithms. Control entropy is below `n^.627`; the endpoint, map, and deletion union cost is below `n^.65`; Gaussian tails are bounded by `exp(-n^.78)`. Their difference supplies the stated superpolynomial exceptional event. For the confidence budget, `u` grows only logarithmically in `mL/rho`. Distinct roots have independent complete common-cavity references conditional on that cavity. Singleton/common-cavity correction moments are bounded at order proportional to `u`; repeated indices are charged by the partition count and the coordinate weight bound. The resulting `e 16^u` moment yields `emL(64e²)^(-u) <= rho/4`.

The simultaneous rectangle/panel failure allocation fits `rho`: initialization is shared, and the other three allowances are counted twice. Each underlying bound is strict, so the displayed upper allocations summing to `rho` cause no missing probability margin. Carrier and response tails after `T` use deterministic fitting and reference-anchored subtraction, hence require no new event.

### Capped Taylor geometry: PASS

The cap is used as written, without waiting for it to become inactive. For

\[
h(t)=\frac{\log(1+2\mathcal K r_n e^{\lambda t/4})}{2\mathcal K},
\]

one has `h' <= lambda/(8 K) <= 1/8`. The disk radius `h(t)/(2(1+d_h))` remains inside the vertically fibered domain, including negative real corners. Along vertical pieces, integrating the residual bound gives activity at most `Y r_n`. Freezing the real symmetric negative-Gram generator gives a unitary imaginary-time base; the integrated generator difference, not complex positivity, bounds its perturbation.

The panel count comes from integrating `1/h` and splitting where `2 K r_n exp(lambda t/4)=1`. The reciprocal cap contributes both `lambda^(-1) sqrt(log(e+ell))` and `B_n sqrt(log(e+ell))`. The latter's label-dependent part is bounded using

\[
[\log(e+\ell)]^{3/2}\le4\sqrt\ell.
\]

Consequently the count has exactly a `(Y/lambda)² sqrt(ell)` term and a `lambda^(-1) log(e+ell)` term. There is no confidence factor in the radius/count coefficient and no extra logarithmic storage power.

### Quantitative dense lower bound: PASS

Locations: lines 2943–3210 and 4066–4226.

The innovation proof is distributional geometry, not a recursive network CLT. For final feature vector `U`, put `c=Qy`. The squared area of `c` and `U` is bounded by `||U(U^T y)-c||² ||U||²`. Splitting the latter norm at a radius and optimizing yields the displayed variance bound. For `Q >= g I`, the two spectral bounds use `x in [g,tr(Q)-(m-1)g]`; multiplying them before dividing by `||Qy||²` yields a positive variance in at least one coordinate. The nonzero label and `m>=2` are essential and stated.

For the finite version I checked the Fourier majorant directly. Symmetrization gives characteristic-function modulus at most `exp(-sigma² t²/4)` up to `3 sigma²/(8 M_3)`. The Gaussian majorant of an interval is integrable, yielding `3h/sigma` plus the stated exponentially small tail. This bound is uniform in the interval center. Conditioning on lower layers and the entire second run therefore allows the second run and conditional mean to be arbitrary measurable shifts. The maximizing training index is chosen measurably from the conditional covariance; a fixed deterministic maximizing index is not needed in this finite argument.

Conditional sixth moments give `M_3²/sigma_0^6 <= 2^30 m^6 X^96 gamma^(-12)`. The factors of `Y` cancel here. The derivative-to-trajectory estimate uses the training rectangle of radius proportional to `1/(u X^100(1+lambda)sqrt(ell))`, a degree proportional to `ell`, and the bounded analytic difference. Hence the resulting coefficient is weaker than the earlier asymptotic coefficient but polynomially controlled. The third lower-width gate dominates the `n^(-2)` analytic remainder. No assumption of independence between this derivative event and the source event is used.

## Legendre, Taylor, and retained-state transfer

### Third-order Legendre estimate and polynomial ratio: PASS

Locations: lines 2327–2942 and 4227–4464.

I checked the growing-interval moment identity, including the constant forward prefix and zero backward prefix. Differentiating the projected bilinear pairing gives the exact physical defect as the product of the two endpoint projection errors. The growing-projection energy identity integrates each squared endpoint error to the final squared history tail; there is no missing boundary term from the prefix.

The order-independent fitting argument is needed before discrepancy bootstrap. It bounds feature-history derivative energy independently of `q`, then combines the `sqrt(q)` endpoint-kernel bound with the `1/sqrt(q)` forward endpoint error. Thus the physical defect is controlled without an order-dependent stability constant, and each finite-order model fits and has parameter/moment limits.

The new estimate separates the accumulated physical feature defect from its history. For the corrected history `g`, activity differentiation gives `g_tau=a` and `g_tautau=a_dot/rho_hat`. The prefix derivative is zero because the initialized readout is zero. In the Legendre Sturm–Liouville operator, the factor `(A-tau)` cancels the apparent inverse residual through `(A-tau)/rho_hat <=4/lambda`. Two integrations by parts therefore give an order-`q^(-2)` forward tail. The physical defect enters this tail additively as `P d_T`.

The backward history retains its order-`q^(-1)` freezing estimate. On the discrepancy bootstrap and with `q<=sqrt(n)`, its additional discrepancy term is absorbed into that order. Multiplying the two final tail bounds in the exact defect identity gives

\[
d_T\lesssim \frac{Y P^3\ell^2}{q^3}
       +\frac{Y P^3\ell}{q}d_T.
\]

The `q>=4P³ ell` gate absorbs the second term. Signed stability uses only dense reference carriers in changed gates, so its exponent is proportional to `(Y/lambda)² sqrt(ell)` and is bounded by `n^(1/64)` under the fixed small-label cap. With `q>=n^(1/4)`, the resulting discrepancy scales as `Y ell² n^(-47/64)`, improving the bootstrap after the structural gate. Whole-sphere output subtraction is real and deterministic; no whole-sphere complex event is required for this new Legendre result.

Dividing by the finite dense lower bound gives exponent `-15/64` and logarithm power `9/2`. Absorbing `7/64` into that logarithm leaves `n^(-1/8)`, which explains the eighth power of inverse requested relative tolerance. This is the substantive improvement over the old logarithmic ratio estimate. All structural gates are fixed powers of exposed parameters; none uses `Y^(-1)` for Legendre.

### Exact metric, corrected optimizer, and endpoints: PASS

Locations: lines 4589–5495.

The barrier selector uses at most `9r` rank-one updates. Its lower potential also ensures the shifted lower inverse exists. After rescaling the diagonal weights, `I <= P^T D P <=4I`. The corrected metric satisfies `P^T M P=I` and `D/4<=M<=D`; coordinate gates therefore have operator bound twice their maximum value. The metric is not assumed diagonal, and the selected dynamics are correctly stated as prescribed directions, not gradient flow of the corrected readout.

The initial exact additions reproduce the training forward pass and Gram. The selected energy identity follows by expanding the squared norm of each velocity in its stated metric. Its corrected readout remains bounded because it is an orthogonal component plus the minimum-norm training fit. The small-label fitting bootstrap is independent of source accuracy. It gives integrable selected velocities, an actual fitted limit, and explicit output tails.

For comparison I checked the exact readout-deficit decomposition and the cancellation in `zeta=z_readout+T_C e`: the `2 V_C e` term cancels because `T_C Q_C=V_C`. The dissipative norm inequality for `p=T_C e` controls the integral of the deficit discrepancy without a bare physical-time exponential. Source pair errors use the exact source isometry plus mass bound and are never differentiated. Initialized forward/reverse approximation pairs must use the same matrix applied to the same approximant; both numerical constructions satisfy this stronger condition. These facts justify the source-to-runtime comparison through the fitted endpoint.

### Taylor width and count: PASS

Locations: lines 4465–4588 and 5754–5892.

On each half-radius disk, Taylor coefficient error sums geometrically. Exact initialized images are controlled in Euclidean norm using operator norm eight. The source dimension includes constants, exact initialized training additions, and reduced first-layer columns. Squaring the panel count only after preserving its `(Y/lambda)²` term gives `(Y/lambda)^4 ell³` and `lambda^(-2)ell²[log(e+ell)]²`. The inverse-label gate is used to simplify the coefficient degree; the exact degree displays the logarithm of inverse tolerance before that simplification. It is not needed for normalized source probability.

The endpoint tail gate is label-independent after dividing by `Y`, since `ne^(-8ell)<=n^(-7)`. Absolute error `Y/n` divided by the lower fluctuation gives `ell^(5/2)/sqrt(n)`, and the stated fourth power of inverse relative tolerance suffices after logarithm absorption. Final probability allocation uses a union bound, not independence. Thus the assembled polynomial statement preserves the intended domain and full trajectory norm.

## Four numerical initializers

### Numerical source routine, activation backend, and restart induction: PASS

Locations: lines 5893–6422.

The approximate path has an integrated defect against the original dense field. Let `E` be its parameter discrepancy and `z` its prediction discrepancy in sample RMS. Retaining the negative square yields

\[
\tfrac12(E^2)'\le-2z^2+2(C^{\rm r}+J^{\rm r})zE^2
          +2J^{\rm r}\rho E^2+E\|d_u\|.
\]

Maximizing the quadratic in `z` gives the cubic discrepancy inequality printed in the candidate. The integral of `rho`, not the length `T`, controls its linear exponential. The explicit small integrated-defect tolerance closes the cubic bootstrap. This avoids a width-dependent ambient Lipschitz exponent over the full physical horizon.

The complex moving balls are derived from RMS forward/backward subtraction and conversion to coordinate bounds. Their radius contains `1/sqrt(n)` and keeps preactivation imaginary parts strictly inside the half-strip. Cauchy's estimate is therefore applied in a genuine complex neighborhood of the computed restart, not merely along a known real path.

The activation polynomial is built from finitely many real value calls. I checked the two ellipse heights, the spare disk radius, the Chebyshev tail and discrete alias sums, and the derivative-error conversion by Cauchy. The polynomial is used only for disposable source computation. Exact initialized training features and the final autonomous model use the original activation. No original high-order activation derivatives are algorithmic inputs.

On each numerical panel, the moving-error contraction has factor at most `1/4`; the local polynomial-field solution remains inside the smaller moving ball. The numerical order makes both the derivative truncation defect and activation-field defect integrable to at most `e_d` over the whole horizon. Applying the real signed estimate to the already constructed prefix produces the next anchor's required `b_n/8` accuracy. This is a finite induction beginning at the exact initialization and does not test an unknown dense trajectory or require panel rejection.

The source-error decomposition contains four terms: analytic source-tail truncation, activation substitution, evaluation on the truncated rather than exact local polynomial-field trajectory, and discrepancy from the dense trajectory. Each is bounded by `epsilon_v/64` in Euclidean norm, giving the advertised `epsilon_v/16`. Passive-query coordinates may cost two factors of `sqrt(n)` in the source Lipschitz bound; the source and order prescriptions explicitly pay `n^(3/2)` after converting to Euclidean source norm. That cost affects logarithmic degree only.

At fixed problem parameters, `A_n,L_n,M_c=O(sqrt(ell))`, inverse moving-ball radius is `O(sqrt(n ell))`, and all inverse tolerance logarithms are `O(ell)`. The activation ellipse gap is order `1/sqrt(ell)`. Hence `J,D=O(ell^(3/2))` and `K=O(ell)` follow from the finite formulas, including the dependence on very small fixed positive labels.

### Taylor numerical nodes and compatibility with polynomial width: PASS

Locations: lines 6423–6588 (continuing through the Taylor rank/degree calculation).

The setup uses exactly the capped source domain from the finite probability theorem. Its uniform restart disk has radius `h(0)/4`, smaller than every certified disk. Since `2 K r_cap<=1`, `h(0)>=r_cap/2`; its inverse is `O(sqrt(ell))` at fixed parameters, whether or not the cap is active. There is no imported uncapped eventual event.

Interpolation at real Chebyshev roots has operator norm at most `2K_s+1`. Exact-source analytic tails are bounded separately for base and initialized image, while approximate node errors are Euclidean and the image operation costs eight. Interpolation and the initialized map commute exactly. The nodal degree differs from the initialized-jet degree, but the candidate proves `K_s+1<=8ell` at the same displayed polynomial count gate. The transfer tolerance is no smaller than the conservative width-theorem tolerance and the same endpoint gate suffices. Thus this implementation does not silently add a qualitative width qualification to Taylor accuracy/storage.

### Harmonic quadrature and retained count: PASS

Locations: lines 5496–5753 and the Harmonic setup passage ending at 6745.

The spatial harmonic estimate follows by tangent-circle averaging and the positive-coefficient Gegenbauer generating function. Time coefficients use a Fourier contour in the Chebyshev angle. Weighted lattice counting gives the total coefficient count with the factorial denominator. For `d=1` the sphere is the two-point set and the time-only construction is handled separately.

The numerical quadrature is positive. Its polar weights are the integrals of the cosine-root interpolating basis; their positivity follows from the telescoping sum of `1/(4k²-1)`. Periodic trapezoids and polar polynomial integration have the stated geometric analytic errors. Complex rotations keep all angles jointly inside the intrinsic query tube; the Jacobian and harmonic polynomial factors are included in the integrand envelope. Nodal errors are multiplied by the total spatial mass bound and harmonic suprema before summing modes.

Only global coefficient vectors are source generators. Local numerical panels are streamed into those coefficients and do not multiply the retained rank. Computing exact initialized images after coefficient accumulation preserves pairing. The factor `alpha^(-1)` still contains `(Y/lambda)²` before squaring, so the retained Harmonic label factor remains fourth order. Harmonic's separate eventual source qualification is not replaced by an unsupported polynomial gate.

### Adaptive Gaussian law and final-array coupling: PASS

Locations: lines 6746–6989.

For stored orthonormal input bases `V,U` and replies `Y=WV,R=W^T U`, the conditional mean is

\[
A=YV^T+UR^T(I-VV^T),
\]

and the remaining law is `(I-UU^T)G(I-VV^T)`. The constraints and Frobenius orthogonality determine this kernel. A fresh forward direction removes exactly one right rank-one component from the residual; its innovation and remaining matrix have zero cross-covariance. Joint Gaussianity proves independence even at singular ranks. Transpose queries are the left-sided version. A dependent or zero query is already determined; full opposite rank makes the innovation zero. The per-layer product kernel persists when layers and directions are adaptively chosen from the transcript. Completion at the bounded stopping time therefore has the ordinary independent Gaussian matrix law.

I separately checked the deterministic query inventory: exact initialized training actions; constant-anchor actions for all required jet orders and directions; initialized images of source nodes/global coefficients; and final initialized basis images after orthogonalization. No norm or entry test on the hidden matrix is used. Random actual rank is replaced by its deterministic bound when specifying the request budget. A fresh reduced first matrix has a Gaussian completion on the unused input complement. Under this completion coupling, coefficient induction and panel induction produce identical explicit/implicit source lists, selections, metrics, and final mixers. This compares to one actual dense reference and does not claim to recover an arbitrary supplied matrix from an entry seed.

### Full operation and peak-memory ledgers: PASS

Locations: lines 6990–7384.

The hidden jet coefficient at order `s` is a sum of outer products with denominator `s`. Grouping the integrated increment gives at most `mK` outer products per panel. Cached inner products reduce the current-panel action convolution to `O(m b' K²(n+K))`; storing a full `K`-tuple of dense matrices is unnecessary. Earlier-panel factors have `b mK` columns and are explicitly charged in both their actions and memory. The numerical rank statement concerns the finite computed anchor, not the continuous dense flow.

The selector cost is `O(L n r³)`: `9r` steps, each charging both a small inverse and all `n` row tests. Source orthogonalization, final basis-image queries, metric composition, initial training Gram construction, and evaluator scratch are all present. The metric inverse formula follows by decomposing into the source span and its complement and passes the independent algebra check below. The input reduction is charged as `O(dM²)` plus the supplied first-matrix projection when applicable. Exact initialized original activation calls remain separate from the polynomial approximation calls.

With `ell=log(en)`, put `a_d=3d/2+1`. Harmonic has `r,R,q,Q=O(ell^a_d)` and spatial sizes `O(ell^(3(d-1)/2))`. Its implicit sampler costs `n ell^(2a_d)` and selector `n ell^(3a_d)`; the latter dominates the other width-proportional terms for every `d>=1`. Peak memory is `n ell^a_d`. The supplied-matrix leading term is `n² ell^a_d`, eventually dominating `n ell^(3a_d)` for each fixed problem, with `O(n²)` peak memory.

Taylor has source rank `O(ell^(3/2))` but matrix requests `O(ell^(5/2))`. The latter distinction is necessary. The sampler, accumulated factors, and activation composition each cost `O(n ell^5)`; selection costs `O(n ell^(9/2))`. Live transcripts, factors, and polynomial-composition scratch fit `O(n ell^(5/2))`. The supplied-matrix leading term is `O(n² ell^(5/2))` with `O(n²)` peak memory. These derive all four table entries from their full parameter formulas, rather than treating rank as a proxy for setup work.

The disposable continuation covers `T=32ell/lambda` in physical time. The short list of numerical panels does not mean a short physical prefix. The Euler comparison explicitly includes its step `h`; it makes no necessity or optimality claim about Euler accuracy. No empirical producer or maintained numerical API is newly claimed, so an empirical reproduction is inapplicable to this addition.

## Unchanged final sections and edge cases

I also read the nonlinear-learning arguments at lines 7385–7906. Their extra nonaffineness and nonparallel-input assumptions are not imported into the new compression claims. The positive covariance-series support, finite-query forward/reverse conditioning, inverse-mobility acceleration energies, adjoint telescoping, and cubic frozen-kernel departure are consistent with the zero-readout scaling. The new width theorem properly declines to quantify their separate onset. The final assembly at lines 7907–7954 uses the actual dense lower event and a union bound and includes endpoint existence in its failure convention.

Boundary attacks included `p=0`; `d=1` and `d=2` harmonic conventions; singular input/intermediate covariance; duplicate passive queries; arbitrarily small fixed positive `Y`; the excluded stationary `Y=0` ratio case; exact residual zeros; a zero or dependent Gaussian query; empty and full query ranks; and accidental numerical source-rank deficiency. None requires a new unstated assumption. The candidate selects the actual computed source span and bounds its rank by generator count, so approximate generators need not preserve an accidental rank deficiency of exact generators.

## Executed checks and their limits

The independent deterministic script and retained output are:

- `data/generated/headline_threefold_upgrade_20261011/review_a_v5/checks.py`
- `data/generated/headline_threefold_upgrade_20261011/review_a_v5/checks.log`

Command, run from `/home/amir/Codes/PDE`:

```sh
python data/generated/headline_threefold_upgrade_20261011/review_a_v5/checks.py | tee data/generated/headline_threefold_upgrade_20261011/review_a_v5/checks.log
```

The script completed with `ALL_DETERMINISTIC_CHECKS_PASS` and the tool reported exit status zero. Results:

| Check | Outcome |
|---|---|
| Three scientific input hashes and complete reverse diff | Exact match; nine hunks; baseline hash reproduced |
| Positive Fejer weights and polynomial exactness, orders 1–64 | Maximum numerical discrepancy `1.9736816347926123e-15` |
| Source metric, inverse, exact isometry, and metric sandwich | Maximum identity discrepancy `7.092979727600255e-16` |
| Gaussian conditional mean/remainder identities at all ranks 0–5 | Maximum discrepancy zero |
| Cached jet actions versus direct polynomial convolution | Maximum discrepancy `1.4936523181711914e-15` |
| Scalar logarithm inequalities and cost exponent domination | Passed the stated deterministic sample checks |

These are finite algebraic diagnostics, not evidence for a stochastic training campaign or substitutes for the derivations above. They use deterministic arrays; no external data, author implementation, or random empirical result is involved. The Gaussian *law* conclusion rests on the conditional-kernel proof, not on the finite matrix identity test. The all-parameter logarithm conclusions rest on analytic maximization; the finite grid merely checks arithmetic mistakes.

At completion, all five frozen input hashes were recomputed and remained identical to the table above. The check script hash is `89632c696031ae6a83c208f319e016a67c6a79bf3a8753d94d1400cf9273aa30`; its log hash is `b26ce6fe0dfb910d4ab09b3c90ca57b70190131f468f33922cbe7b704366a564`. The final scoped whitespace check reported no errors.

Other actual commands included the interval `sed`/complete `cat` reads recorded above, `wc -l`, `sha256sum`, targeted `rg -n` for report locations, and metadata-only `git rev-parse HEAD`, `git diff --name-only`, and `git diff --cached --name-only`. The observed HEAD before writing was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`; unrelated dirty-path metadata was preserved. I made no Git-index changes and edited only this report and the assigned scratch script/log.

## Component verdicts and completion

| Component | Verdict |
|---|---|
| Model, domain, confidence, and complete-trajectory contract | PASS |
| Unchanged fitting/source/selection dependencies used by the additions | PASS |
| Finite source probability and capped panel geometry | PASS |
| Actual dense lower comparison and inverse-tolerance dependence | PASS |
| Improved Legendre error at original moving-state order | PASS |
| Taylor polynomial width and retained count | PASS |
| Numerical source routine, activation approximation, and restarts | PASS |
| Exact pairing and selected all-time/endpoint transfer | PASS |
| Adaptive forward/transpose Gaussian law and final-array coupling | PASS |
| Supplied Harmonic work and peak storage | PASS |
| Supplied Taylor work and peak storage | PASS |
| Implicit Harmonic work and peak storage | PASS |
| Implicit Taylor work and peak storage | PASS |
| Taylor numerical-setup compatibility with its quantitative width | PASS |

There are no unresolved scientific objections, refuted claims, missing inputs, or required editorial corrections in this review. I have completed the assigned full reading, repaired the identified output truncations, independently reconstructed the requested transitions, recorded concrete attacks and checks, and supplied exact input identity. The PASS applies only to this frozen candidate and its stated qualifications. Separate integration review, edition validation, and approval remain outside this scientific review's authority.
