# Independent complete audit A3

**Verdict:** No mathematical correction required for the claims as explicitly stated and scoped in the supplied packet. This is a clean audit of the finite controls, conditional analytic results, auxiliary Gaussian recursion, clipped comparison, and exact transcript law. It is not a certification of an uncut population limit or of any conclusion the packet identifies as unresolved.

## Inputs, isolation, and complete read coverage

Audit date: 2026-09-10. The only scientific inputs were the following exact files:

| Input | SHA-256 | Read coverage |
|---|---|---|
| `studies/repository_refactor_2026_09_09/FINAL_CONTROLS_ADDITION.md` | `426fab7e5fda6c8e31747d5cddb3501892577fb26bec762c910c6680cf1e0dc2` | All 4,308 lines, 1–4308 |
| `studies/repository_refactor_2026_09_09/reviews/FINAL_CONTROLS_DEPENDENCIES.md` | `e36cf31741b43271b66b1c21469fcba2dfff6cb170e1a55ac9070cab2465d1e4` | All 245 lines, 1–245 |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | All 98 lines, 1–98 |

Total coverage: **4,651 of 4,651 lines**. The addition was read in consecutive, nonoverlapping blocks 1–600, 601–1200, 1201–1800, 1801–2400, 2401–3000, 3001–3600, and 3601–4308; the other two inputs were read in full. Subsequent searches only located references within those inputs. This was a complete audit, not a sampled audit.

I read the required solve-math-rigorously skill and checked applicable ancestor instruction-file paths. I consulted no other project scientific documents, reviews, verdicts, source audits, Git data, history, or external references. No delegation or training was performed. Only this report was written; the input hashes were checked again at completion.

## Claim and proof coverage

Line references below refer to the addition unless another input is named.

| Material | Audit result |
|---|---|
| S, lines 9–387 | The rescaled Euclidean gradient, all five hidden Hessian contributions, mixed readout blocks, and Frobenius constant agree. The resolvent proof handles repeated singular values and arbitrary transported isometric subspaces. The physical Jacobian includes the required clock term `−2bbᵀ/n`. Gaussian event constants and polynomial primal continuation bounds agree. The log-spectrum estimates do not imply normalized trace control. |
| I, lines 388–859 | The conditional reused-matrix law retains both its regression mean and orthogonal projection. The projection error is at most `H²/n` in expected normalized squared norm. Random denominators, their null-event conventions, fourth moments, quadratic-growth tests, convergence in probability and in L¹, and strict positivity of `c_*` are justified. |
| C, lines 860–1284 | The actual trained-query derivative includes the trained top-matrix term and the readout/preactivation derivative term. Its explicit remainder gives the asserted `s³` error, with the tiny initial readout retained. Probability and unrestricted moment estimates support the stated expectation bounds. The positive-fraction argument is correct on each fixed interval `[a,s₀]`, after a width threshold depending on `a`. It concerns scalar coefficients, not Hessian eigenvalues. |
| E, lines 1285–1717 | The moderate-sine normalization and derivative bounds agree. Raw gradient normalization, all displayed field/Lipschitz coefficients, and the `11000√n B⁹` bound agree. The GD stopping induction closes at step `n⁻²`. The weak path-measure tightness statement has the stated limitation. On specified population action spaces, the weighted scalar Taylor argument establishes the needed C¹ loss despite the stronger activation-map differentiability issue; energy then proves strong endpoints for existing solutions. No local existence or uniqueness is inferred there. |
| Q2, lines 1718–2047 | Frozen covariance identities, strict reverse suffix, repeated-query Cholesky formulas, effective-rank estimates, integer choices, integrated maxima and query maxima agree. The direct-noise dimensions and powers of `m` agree. The distinction between actual temporal bounds for the top histories and cap-dependent bounds for the lower backward history is retained. |
| Q3, lines 2048–2202 | The supplied inverse-Jensen, relative-entropy, variational trace-concavity, conditional exponential, stopping, and dilation arguments establish the stated rectangular Freedman bound. Its specialized concentration dependency is proved within the packet. |
| Q4, lines 2203–2429 | The row/column reveal order makes the two increments conditionally centered. The exact Gram decomposition includes both regularization residuals. Predictable rank stopping and symmetric truncation preserve the required martingale structure. The two variation bounds are `2R_ω I_n` and `2R_θ I_m`; truncation and Freedman failures sum to the declared allowance. |
| Q5, lines 2430–3266 | The noisy warmup, every pre-step memory update, and both interacting filtrations are fully specified and causal. The first pass uses only the automatic rank ceiling `n`. The resulting state bounds precede the slow-history proof. The separate warmup column is correctly retained. Rank compression gives exponent `11/12`; the second unconditional localized pass gives error exponent `−1/24` with the stated logarithms. The total failure allowance is `p₀(n)+5n⁻²`. |
| Q6, lines 3267–3671 | The integrated reference and strict pre-step discrete memory are consistent. All primal bounds can be independent of the cap. The three filters are controlled in feedforward order by geometric sums, giving a filter error of order `ε`, without an exponential in `1/ε`. Reference quadrature and slow-state Gronwall prove the claimed clipped comparison. |
| Q7, lines 3672–3824 | Each relevant time-regularity and state-difference estimate introduces at most one factor `1+R`. Consequently the extracted constant has the form `C(1+R)exp(C(1+R))`. The application correctly uses `b=2B_n` and includes warmup errors. `R_n=o(log n)` yields the stated `n^(−1/24+o(1))` rate for the two width-dependent clipped systems. |
| G, lines 3825–4308 | All forward, reverse, and cross covariances agree at deterministic histories. The positive-definite sequential-conditioning lemma then proves equality for adaptive transcripts, jointly for both matrices and the non-matrix roots. The conditional innovation covariance and learned-memory coordinate bound agree. The final bounded-Lipschitz comparison follows from the Q7 coupling and exact transcript equality. |
| Dependency, lines 1–245 | The four initial actions, exact retained memories, converse reconstruction, supplied-path mesh, integration-by-parts continuity estimates, and the three negative examples agree. The dependency expressly avoids the causal, stability, and derivative conclusions that its supplied-path estimate cannot support. |
| Notation, lines 1–98 | Width factors, stored-readout scaling, residual placement, raw mobilities, finite transposes versus population adjoints, and feature/physical/proof clocks remain consistent. The distinct moderate-sine two-sample model is declared explicitly. |

## Critical dependency and scope checks

The adaptive argument does not apply a frozen Gaussian isometry to an adaptive path. In Q4/Q5, each matrix's enlarged initial sigma-field contains the other matrix's primitive arrays, not an independently declared realized transcript. Its own fresh row and then fresh column remain independent of the corresponding past. The second rank pass bounds an intersection event unconditionally and is not conditioned on the first pass.

In G, the cross-covariance calculation uses `b_(l,k)=ω_l/√n` when `l<k` and `a_(l,k)=θ_k` when `l≥k`. The strict reverse triangle also removes the proposed Lambda cross term. The subsequent Gaussian posterior induction applies to measurable causal linear observations; it does not assert that the adaptive stacked output is jointly Gaussian. It therefore supports the coupled replacement law, while correctly excluding the original hidden matrices as jointly retained coordinates.

As a bounded deterministic arithmetic check, I formed the coefficient matrices of both Gaussian rules for four explicit finite examples, including `n=1`, repeated dimension constraints, and `K>n`. Their full covariance discrepancies were at most `4.45×10⁻¹⁶`, consistent with rounding. This was not simulation and was not used in place of the general covariance and conditioning proofs.

The closed packet supplies the specialized matrix-concentration and adaptive Gaussian-conditioning arguments used downstream. The projection argument in Q5.50 also supplies an internal direct justification of the effective-rank compression principle used in Q2.

The limitations are mathematically consequential and are respected throughout: squared-log control is not amplitude control; weak path-law tightness is not W₂ compactness; a strong endpoint for an existing population path is not a restart theorem; growing caps do not remove clipping; and innovation tails do not control the unbounded predictable mean of the full middle query. The final bounded-Lipschitz transfer does not transfer conditional laws, discontinuous tail indicators, or unbounded tests. No uncut population construction, uniqueness, autonomous restart, physical-clock comparison, exact raw-GD population convergence, or kernel/velocity convergence is established by this packet.

**Disposition:** clean within the stated scopes; no substantiated correction or missing specialized dependency found.
