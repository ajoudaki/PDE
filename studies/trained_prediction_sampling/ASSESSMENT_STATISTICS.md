# Scoped independent sampling assessment

Date: 2026-09-12. Assessor: independent sampling/statistics subagent.

**Finding:** I found no material mathematical defect in the implication from the explicitly stated analytic inputs below to the candidate's actual influence, sampling expansion, Hilbert CLT, width-first bridge, and mean-square strengthening. The exact requested A–C and secondary formulas follow **conditionally on those inputs**. This is a scoped assessment, not acceptance of the entire neural theorem or of its upstream source construction.

## Scope, inputs, and integrity

I read the entire 1,552-line `proposal_C4_8_v2.md`, all of `docs/NOTATION.md` and `docs/README.md`, and exactly `docs/global_nonlinear.md` lines 8976–9187. I applied the `solve-math-rigorously` skill. I did not read the study README, history, earlier reviews, other studies, or other assessors' findings. I did not run the supplied sampling checks, train a model, fetch additional scientific inputs, or use Git. The supervisor supplied only the original A–C and secondary target formulas after my initial candidate reading.

The following SHA-256 values agreed before and after the scientific reading and audit:

| Input | SHA-256 |
|---|---|
| `studies/trained_prediction_sampling/proposal_C4_8_v2.md` | `98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| `docs/global_nonlinear.md` | `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226` |

The last hash is an integrity check of the file, not a claim to have read beyond the assigned excerpt. Only this assessment report was written.

## Analytic inputs on which the neural conclusions depend

1. **Actual deterministic value map.** C.4.7 supplies the prescribed neural population flow, with no random environment outside its expectations, and a bounded, whole-circle, supremum-norm-valued, Wasserstein-continuous endpoint map `F` on `U_Y`. For every fixed finite law in the analytic region, its exact population raw Euler endpoints converge to `F` in this norm. C.4.7.NG and NL directly support boundedness and law continuity in the assigned statement; the population-program approximation is also described there.
2. **Uniform finite-program responses.** C.4.8.S1/P7 holds in a neighborhood containing the closed law ball of radius `3 δ_Y/4`, with common finite constants `L,M` and a positive maximum-step threshold. The derivative bounds must be uniform over atom count, minimum positive mass, covariance rank, passive input, and Euler step count. They include continuous one-sided extensions at zero masses, linear first mass responses, and second mixed responses on admissible probability rectangles. The value algorithms and their derivatives must be those of the actual retained neural action construction.
3. **Actual finite-width value convergence.** C.4.7.NW1 holds at every separately fixed finite law in `U_Y`, for the actual random Gaussian initialized finite GF. The initialization is independent of sampling. The assigned canonical theorem states a stronger whole-circle, whole-time assertion than the endpoint `H` convergence required here.

Input 2 is the specific neural-response lemma treated conditionally in this assessment. I read its proof and checked the statistical requirements against its exact quantifiers and formulas. I did not independently validate the complete III.F action construction, C.4.7.N-cap, or all proofs behind C.4.7, which are outside the assigned scientific inputs. Thus a defect in the exact source representation or its uniform cap would invalidate the neural application without invalidating the abstract sampling lemma. These are explicit dependencies, not additional probabilistic regularity assumptions silently imposed on the sampling law.

The candidate's separate all-finite-law existence and measurability argument, P18, was checked directly below. It need not be added as an unproved analytic premise.

## Interface from finite responses to Borel-law influence

The passage in C.4.8.2 is sufficient under inputs 1–2.

* **One common neighborhood.** The choice `δ'_Y=δ_Y/4` is positive and strictly smaller than `δ_Y`. For `Q` in the closed ball of radius `δ_Y/2`, contamination of size at most `min(1/2,δ_Y/(4D_Y))` moves a law by at most `δ_Y/4` in Wasserstein distance. Thus all forward quotients used to define the influence remain inside the stated larger analytic region. The constants needed for this step are independent of the atom `z` and base law in this closed ball.
* **Derivative convergence does not assume differentiation commutes with a limit.** The finite Taylor remainder is `2M ε²`, since `||δ_z−λ||_TV≤2`. Each finite derivative is within `2M ε` of the corresponding forward quotient. Comparing two vanishing meshes and using value convergence at the two fixed laws yields a limsup difference at most `4M ε`. Taking `ε↓0` makes the finite derivatives Cauchy in the complete supremum-norm output space. This proves an actual derivative, rather than merely a formal tangent equation.
* **Nonatomic laws.** For finite laws the quotient difference is bounded by `2M(ε+η)` uniformly in the law and atom. Finite laws are dense in the compact closed Wasserstein ball; quantization with a vanishing inward mixture handles its boundary. Continuity of `F` transfers the bound to every law. Consequently the quotients converge uniformly on the compact law/atom product. Their limit is jointly continuous and bounded. No empirical convergence in total variation is used.
* **Centering and integrability.** Finite centering follows from linearity because `Σ p_a(δ_{z_a}−λ)=0`. Uniform atom continuity and norm convergence of Banach-valued integrals under weak convergence pass this to arbitrary laws. The circle's continuous-function space is separable, as is `H`, so the bounded continuous field is Bochner measurable and square integrable. Continuity as a function with values in the supremum-norm output space also supplies the claimed jointly continuous atom/input representative.
* **General signed directions and replacements.** Common quantization contracts total variation and preserves the probability property of all laws on a segment or rectangle. It therefore transfers the finite derivative formula and mixed difference inequality with their stated constants. If a signed direction `η` admits a segment of length `a>0`, the law `Q+aη` is a valid probability measure; rescaling the mixture derivative gives the derivative along `η`. At interior points, positive and negative directions give matching two-sided derivatives. Joint continuity makes these derivatives continuous along the segment, justifying the fundamental theorem of calculus. The rectangle's compact image lies a positive distance inside the open ball, so its finite approximants remain admissible.

Zero-mass atom additions are essential to the first item of the requested contract. They are explicitly included in S1/P7 and used in P8, rather than inferred from derivative estimates restricted to strictly positive masses. Similarly, uniformity in support size and small weights is essential for the Borel completion, and the candidate explicitly supplies it as part of input 2. A theorem with only a separately finite-support constant would not suffice.

The dynamics characterization P13 retains the entire displayed finite response recursion before taking its mesh and quantization limits. It includes residual feedback, both changing source covariances, both action orientations, and the learned middle increment through the coefficient/contraction recursions. Its identification with genuine dynamics is conditional on the exact source representation in input 2. The statistical argument does not substitute an arbitrary endpoint derivative or a frozen-feature model for that representation.

## Independent check of the Hilbert sampling lemma

I checked C.4.8.3 as a standalone theorem under its own R1–R4. These hypotheses are sufficient as written.

### Taylor estimate and localization

R3 applied to collinear increments `(b−a)η` and `hη`, divided by `h` and followed by `h↓0`, gives

`||f'(b)−f'(a)|| ≤ M(b−a)||η||_TV²`.

First-derivative continuity covers segment endpoints. Integration gives R9 with the factor `M/2`. Combining this estimate on a contamination segment of length `τ` with the bounded value map gives R10, namely `||I_Q(z)||≤2B/τ+2Mτ`. Thus the local integrability needed subsequently is derived, not assumed through an unstated global atom bound.

For the finite continuous partition of unity, the two quantization costs sum to `4ε`, and unmatched discrete mass is half the coordinate `l¹` discrepancy. This gives R11. With `ε=r_loc/16` and `b=r_loc/(2DN)`, the support of the cutoff lies within distance `r_loc/2` from the sampling law. The first kernel of the product is correctly centered in R13.

The four-term product identity R14 is algebraically correct. Its cross terms are controlled using the first TV derivative bound, and the last term uses the smooth scalar cutoff's second derivative. The cover/grid argument extends the mixed difference bound globally: the buffer ball and complement of the cutoff support cover the whole parameter rectangle, each sufficiently small cell lies in one member, and summing the mixed differences telescopes. The edge products scale by each cell's two side lengths, whose products sum to one. Vanishing cutoff derivatives and the uniform local kernel bound also justify the global first-segment calculus across the support boundary.

For each test in `[0,1]`, the centered log moment-generating function bound `λ²/8` yields the tail `2 exp(−m b²/2)` at threshold `b/2`. The union bound R16 is correct. Its constants may depend on the separately fixed sampling law and localization radius; no uniform-law or sample-rate assertion requires otherwise.

### Bias, replacement, and first projection

The bias telescoping laws retain at least `1/m` of the original sampling law until the next observation is added. Therefore every Taylor segment is a probability segment even when the sampling law is nonatomic. The first-order term has conditional mean zero; the `2M_*/m²` remainder summed over `m` observations gives `||b_m||≤2M_*/m`.

The Hilbert-valued Hoeffding components in R18 are the usual inclusion–exclusion projections, and their orthogonality follows by integrating out a coordinate in the symmetric difference of the index sets. A double replacement kills exactly the components not containing both replaced indices. For a component containing both, its four copies are pairwise orthogonal and have equal squared norm. Hence the factor four in R19 is correct. Distinct components remain orthogonal after the replacement operation by the same conditioning argument.

Each replacement edge has TV norm at most `2/m`. The rectangle is a probability rectangle for every pair of observed indices, including duplicate observations. Consequently

`||D_ij T_m||≤4M_*/m²`,

and

`E||R_m^H||²≤(1/4) binom(m,2)·16M_*²/m⁴≤2M_*²/m²`.

The base law `Q_m=μ/m+Σ_{j=2}^m δ_{Z_j}/m` in R21 is particularly important: it makes replacement of its remaining `μ/m` by `δ_z/m` admissible for **every** `z`. Centering the Taylor remainder costs at most `4M_*/m` after multiplication by `m`, as stated. Wasserstein convergence of `Q_m` to `μ`, R4 with the fixed reference law `μ`, and the bounded global kernel give the required convergence in expected `L²(μ;H)`. No diagonal evaluation of an uncontrolled random kernel and no total-variation empirical convergence are used here.

The exact orthogonality identity R23 is correct. Its first two terms are bounded by `6M_*²/m`; the third is the first-projection error, which tends to zero without any quantitative continuity modulus. Thus the proof establishes the stronger `m E||r_m||²→0`, not merely an in-probability expansion.

### Gaussian limit and covariance

The covariance is a positive self-adjoint trace-class operator because Tonelli and Parseval give trace `E||I_μ(Z)||²`. The Gaussian series is well-defined in `L²(H)`, allowing zero covariance, finite rank, or infinite rank. The finite-dimensional characteristic-function proof needs only centered finite variance, and the projection tail is uniformly controlled by the corresponding tail second moment of the influence. Approximation of bounded Lipschitz tests by these projections proves the Hilbert weak limit.

R24 gives the covariance for every finite collection of arbitrary `H` spatial tests. R25 is also well-defined: the `L²` norm of the rank-one spatial kernel equals `||I_μ(z)||_H²`, which is integrable. In the actual neural application the stronger continuous influence makes P16 a continuous kernel on the input product. None of these arguments assumes positive rank or diagonal covariance. A point-evaluation CLT or a continuous-function-space CLT is not needed for the requested contract and is not inferred from the Hilbert CLT.

The claim about a possible independent residual environment is correctly qualified in the abstract lemma. The actual model explicitly says its population endpoint is deterministic, so the requested unconditional limit is Gaussian with a deterministic covariance rather than an unacknowledged Gaussian mixture.

## Mean-square extension and width-first bridge

The cutoff and the specified zero extension agree on a finite-test neighborhood of `μ`. Both are bounded, and the complement has exponentially small probability. Thus their squared difference, multiplied by `m`, tends to zero. This justifies P4 for exactly the zero extension P3, even though P3 need not be continuous across the boundary of `U_Y`.

For `S_m=m^{-1}Σ I_μ(Z_i)`, centering and independence give `E||S_m||²=Tr(Σ_μ)/m`. The cross term obeys

`m|E〈S_m,r_m〉|≤sqrt(Tr Σ_μ) sqrt(m E||r_m||²)→0`.

The squared remainder has the same vanishing scaled expectation. Therefore P17 is the exact requested trace-over-sample-size expansion. It concerns the population endpoint extension and does not claim a finite-width moment expansion.

I also checked the exceptional-law finite GF argument. Bounded tanh gates give the displayed readout norm differential bound. Its finite-horizon bound then controls the Frobenius norm of the middle increment by integration. The spectral norm of the initial middle matrix plus that Frobenius increment controls the first-row derivative. For a fixed finite initialized array all three parameter blocks stay finite on finite horizons. The smooth finite-dimensional vector field therefore continues globally in time. Smooth local dependence, extended over the finite horizon using these bounds, gives a measurable continuous-input prediction and hence an `H`-valued sample statistic. This argument includes arbitrary finite empirical laws outside `U_Y` and the actual random initial readout.

At fixed sample count, conditioning on each good empirical law allows C.4.7.NW1 to be applied with the correct initialization law. Convergence in initialization probability implies convergence of the expectation of `min(2,sqrt(m)·error)` to zero. It is bounded by two, so dominated convergence over samples gives P19. This does not require convergence uniformly in the empirical law. On the bad event the difference of bounded Lipschitz test values is at most two, giving P20. The exponentially vanishing bad-event probability and the population Hilbert CLT then establish precisely `lim_m limsup_n d_BL=0`.

The bridge makes no illegitimate interchange of sample and width limits, needs no convergence theorem on bad empirical laws, and does not infer a `sqrt(m)`-accurate simultaneous width/sample rate from ordinary width convergence.

## Exact target disposition

| Requested target | Candidate formulas | Scoped conclusion |
|---|---|---|
| A: actual centered measurable square-integrable influence in `H`, identified by full trained dynamics | P2, P8–P13 | Follows under inputs 1–2; the candidate proves the stronger supremum-norm derivative. Actual-action identification remains conditional on the upstream source input. |
| B: empirical expansion with `sqrt(m)||r_m||→0` in probability | P3–P4, R23, P14 | Follows under inputs 1–2; the remainder is in fact small in scaled mean square. |
| C: covariance, arbitrary spatial tests, Hilbert Gaussian limit | P5, P15–P16, R24 | Follows under inputs 1–2, with degenerate covariance permitted. |
| C: actual finite-network width-first distributional bridge | P6, P18–P20 | Follows under inputs 1–3 and the independently checked finite-GF existence/measurability argument. |
| Secondary: scaled remainder mean square and trace-over-`m` error | P4, P17 | Follows for the specified bounded population endpoint extension. |

There is no material objection to report in the audited sampling layer or its stated conditional interfaces. This conclusion supplies neither full acceptance of the neural source/cap lemma nor a promotion decision. Uniform-law rates, simultaneous fluctuation-scale width/sample limits, finite-network tangent convergence away from the reference, a continuous-function-space CLT, and a claim that feature learning improves generalization are outside the requested and established conclusions here.
