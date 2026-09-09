# Independent complete review B2: finite reductions and positive-metric Taylor obstruction

**Verdict: CLEAN. No required corrections found in the supplied version.**

This verdict covers the complete frozen packet at `/tmp/pde_continuation_review_b2`, not a checkout or another version. The finite QI/IQ/QQ identities, differentiated RMS construction, and their finite physical-flow existence proofs are correct under their stated scopes. The positive-metric Stieltjes obstruction and canonical prescribed-Taylor non-Cauchy result follow from the supplied finite-order algebra and estimates. Their separation from positive-time population identification is maintained. The implementation agrees with those finite formulas within its stated float64 contract. All 20 supplied tests and the additional bounded deterministic checks passed.

## Scope, independence, and full-read coverage

I read every line of all 15 payload files (3,622 lines), plus the 77-line `INPUTS.json`. No checkout, study artifact, history, prior review, other task, external source, or delegated review was consulted. No packet file was changed, created, or removed. The only written artifacts are this report and uniquely named B2 diagnostics/hash records outside the packet.

I applied `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`. Required references read: `research-contract.md`, `evidence-ledger.md`, `adversarial-audit.md`, and `decisive-experiments.md`. The task was treated as a bounded proof/code assessment with explicitly authorized tests, not an experimental research campaign or proof search.

| Fully read file | Lines | Audit coverage |
|---|---:|---|
| `docs/NOTATION.md` | 98 | Stored weights, residual, norm, metric, initialization, clocks, limit scope |
| `docs/finite_dynamics.md` | 214 | Backpropagation, kernel blocks, energy, global existence, width bounds, Gaussian initial event |
| `docs/finite_reductions.md` | 434 | Every argument in Sections 5–7, including Lax similarity, orientation witness, RMS lift and continuation |
| `docs/gaussian_dependencies.md` | 346 | Gaussian recurrence/PSD validation, full forest factorization, exact boundary certificate and interfaces |
| `docs/loss_pullback.md` | 366 | Every argument in Section 9, operator words, temporal table, remainders, cubic loss formula, convex-tube bound |
| `docs/positive_metric_taylor.md` | 496 | Every argument in Section 10, derivative rewrites, moments, positive metric, factorial bound and prescribed loss family |
| `code/NUMERICAL_CONTRACT.md` | 91 | Numerical scope, storage, callbacks, initialization, normalization and raw GD |
| `code/API_ADDITIONS.md` | 118 | Complete reductions and Euler-word API/formula/scope/complexity descriptions |
| `code/pde/__init__.py` | 26 | Imports/exports and package dependencies |
| `code/pde/finite_network.py` | 363 | Full finite reference implementation, validation, callbacks, scaling, gradients, kernels and simultaneous updates |
| `code/pde/finite_reductions.py` | 251 | Every evaluator, parameter/argument validation, all returned fields and ownership |
| `code/pde/gaussian_moments.py` | 114 | Rational validation, singular PSD test and locally memoized moment recurrence |
| `code/pde/exact_calculus.py` | 249 | Every exact primitive, recurrence, certificate, graph key and ownership |
| `code/tests/test_finite_reductions.py` | 239 | All nine tests and helpers, independence and tolerances |
| `code/tests/test_exact_calculus.py` | 217 | All eleven tests and helpers, independent constructions and exact witnesses |
| `INPUTS.json` | 77 | All 15 hashes, byte counts and line counts checked |

## Scientific findings

### Finite metric, QI/IQ/QQ, and Lax reductions: verified

The fixed datum is `x=1`, dimension one, one sample, two width-`n` hidden layers. The middle matrix `B` is already stored with its width scaling. The inverse of the parameter metric `||du||²/n + ||dB||² + ||da||²/n` multiplies endpoint gradients by `n`. Direct differentiation of the three outputs reproduces every row of (10), all three squared metric norms in (11), and the physical identities `dot f=-2rK`, `dot L=-4r²K`. The residual is absent from all backward fields and raw kernels. The label is arbitrary, and the prime is a vector field rather than an assumed globally invertible clock.

The isometries divide neuron vectors by `sqrt(n)` while preserving numerical middle-matrix entries. In QI, `Q'=QS` and `JS=-SJ` give `L'=[L,S]`; in IQ, `P'=2SP` gives `L'=2[L,S]`. The specified blocks recover the correctly normalized `q`, `z`, scalar norms and current quadratic forms. The physical multipliers and signs in the similarity proof are correct: `U'=-FU`, `V'=VF` imply `(VLU)'=0`. Self-adjointness is not required.

The QI witness is raw-realizable: the Householder matrix fixes `h`, maps the two readouts into each other, and conjugates the signed Gram matrices. The outputs are both `1/3`, while total kernels are `68/9` and `28/3`, differing by `16/9`. A common nonzero residual produces different output velocities. This excludes the proposed spectrum-plus-current-`h`-plus-output state; it does not exclude the full operators. Both QQ row and column balances differentiate to zero with their stated coefficients. No width-independent scalar reduction is claimed.

### Differentiated RMS and finite continuation: verified

For `N_epsilon(x)=x/sigma`, its differential is `sigma^-1(I-NN^T/n)`. The radial eigenvalue is `epsilon/sigma²`; the matrices called `Pi` are positive definite for positive epsilon and are not asserted to be projectors. Transferring these symmetric derivatives backward gives exactly `c`, `b`, `q_tilde`, all three ascent blocks and kernel terms in (23)–(26). Every normalizing denominator is differentiated.

The field equations (27)–(28), contraction `h^Tq/n=2 epsilon f/beta²`, and signed balance drifts (30) check directly. In particular the row drift generally survives the formal epsilon-zero evaluation; the API and theorem correctly require positive epsilon. Recovering `alpha` from `h` requires the stated strict RMS domain `rho_h<1`, and `h>=0` makes `A_h` positive semidefinite. The reconstructed raw square has exactly that normalizer. Arbitrary choices of the nonzero raw signs yield the same locally unique reduced future; zero coordinates remain zero. The restart claim is confined to states with a finite raw lift, and the source matrix still scales with width.

All four finite architectures have smooth losses. The nonnegative squared loss gives the exact weighted energy identity, hence a square-root time modulus for the parameters. At fixed width the metric is equivalent to Euclidean distance, so any finite maximal endpoint has a finite limit and local continuation. This establishes global physical flow without assuming global feature ascent, a width limit, bounded coordinate maxima, or arbitrary-step GD stability. The general finite-dynamics dependency uses the same argument correctly. Its additional width bounds are conditional on bounded activation derivatives and initial normalized/operator bounds; it does not apply that bounded-derivative conclusion to the raw square without qualification.

### Annealed derivative forests and positive-metric obstruction: verified

In the independent primitives `(u,g,a)`, the change `B=g/sqrt(n)` gives the mobility `n beta` in the `g` block. Formula (10.1) has normalization `n^-2`. Differentiation gives all three primitive rules (10.3), with degree six. The row, column and edge rewrites include the correct factors `p`, `8 alpha q`, `2 beta`. Fresh abstract vertices are summed without distinct-label restrictions, so coincident numerical labels do not remove product-rule contributions. A bridge removal increases the component count by one; every rewrite increases `e/2+r` by one, as required.

For each Gaussian edge pairing, endpoint identifications give a multigraph with `v<=b+c<=b+r`. Additional numerical label coincidences lose a power of `n`; fixed decorations have bounded Gaussian moments. Leading terms cannot pair across original components, yielding exactly the component factorization, also for isolated vertices and odd-edge components. Thus each fixed-order annealed derivative exists, with nonnegative polynomial mobility coefficients. Primitive degree `7+5k` proves the claimed even-order vanishing. This is a fixed-order expectation theorem, not concentration or a trajectory theorem.

The frozen-row reduction and its conditional Gaussian moment limit in (7.C1)–(7.C5) are complete dependencies for the certificate. The displayed derivatives, six rational moments, determinant and polynomial witness regenerate exactly. Formal reversion depends rationally on finitely many coefficients and only divides by powers of the nonzero first coefficient. Hence the negative witness remains negative for some strictly positive first mobility, with the other two blocks training. The proof supplies an existential neighborhood of the frozen boundary; it appropriately leaves the unit metric's Stieltjes status undecided. A negative value on `lambda p(lambda)^2` contradicts a nonnegative measure on `[0,infinity)` because the needed moments through degree five are finite. No analytic convergence or positive-time population interpretation is inserted.

### Canonical factorial lower bound and prescribed loss family: verified

Every block derivation preserves the cone of polynomials with nonnegative coefficients in the independent primitives. Noncommuting ordered-word expansion therefore justifies the annealed comparison against the frozen-first-block word; it does not compare trajectories. Conditioning on the first layer and using `q_n -> 3` with uniformly bounded fixed moments justifies the finite-order frozen limit.

The invariant ray `z=sqrt(2q)a` reduces to `a'=2qa²` and evaluates the homogeneous polynomial coefficient exactly as `(2q)^(k+1) binom(k+2,2)`. Its use is solely at initialization. For odd `k`, even Gaussian moments dominate `m!4^-m(2q)^v` termwise, including zero exponents. This yields (10.13) with `m=(k+3)/2`. The elementary factorial estimate proves that the odd coefficient roots diverge; positivity then gives divergence of every positive-argument partial sum.

For each prescribed polynomial, strict monotonicity produces a unique positive root at output one. The reciprocal residual-clock integral diverges there, giving a unique global clock whose output increases to one and never reaches it at finite time. Translation of that polynomial solves the source PDE and its complete finite coefficient ODE. For every fixed level below one, the hitting time tends to zero. The losses therefore have pointwise limit one at initialization and zero at every positive time. Uniform Cauchy behavior on any `[0,T]`, `T>0`, would give a continuous limit and is impossible. The truncated uniform metric triangle inequality also correctly excludes the stated iterated common-target shadowing claim, even without an identified target limit.

The order of limits and claim boundary are explicit and valid: fixed derivative order, width, then prescribed Taylor order. This does not establish an actual network step loss, analyze a coupled `M(n)`, or exclude signed/non-Taylor descriptions.

### Exact loss-pullback dependency: verified

The linear metric-coordinate change preserves raw loss GD and the moving residual. Powers of the single exact pullback difference yield the binomial operator-word coefficients without commuting distinct differential operators. The finite recursion includes differentiation of each inner state-dependent vector field. The entire displayed temporal table, the highest-degree cancellation, the fixed-`N` integral remainder, and the generic cubic formula check. The separate predictor regularity assumption suffices for the one-sample specialization. The affine and stationary cases have the asserted coefficients and behavior.

The convex-tube estimate explicitly includes all hybrid states and fine intermediate states needed by the telescoping argument. Its local defect, propagation factor and scalar derivative bound yield (9.P24)–(9.P25). Fixed-order cancellation is not promoted to a uniform remainder or neural limit. The word/weight APIs implement only the claimed finite rational combinatorics.

## Code and numerical contract

The reductions return the documented values and raw-storage ascent/physical velocities. RMS remains a widthwise architecture distinct from a scalar callback. All required arguments are checked; epsilon is strictly positive, models are explicitly restricted, parameters are revalidated, and labels are finite real scalars. Returned arrays do not borrow input storage; fixed dataclass fields do not imply immutable contents. QQ balance zeros are exact analytic identities, separately checked against raw differentiation. The IQ Lax generator includes its factor two.

The finite core's forward scaling, residual-free backward recursion, mean-loss factors, endpoint/middle mobilities, and raw simultaneous GD all agree with the proof conventions. Exact Gaussian and combinatorial routines use their declared finite rational domains; singular PSD covariance is handled without an inverse or tolerance. Forest keys preserve colors and component multiplicity and reject cycles/duplicates.

The numerical declarations are appropriately limited. The reductions use ordinary float64 contractions, reject evaluated nonfinite required quantities, can underflow, and do not inherit the core's specialized scaled products. The core itself does not promise recovery from arbitrary unrepresentable matrix contractions. No certified rounding or arbitrary-range claim is made. The stated reductions/Lax/combinatorial operation and storage bounds match the implementations, with rational bit-size and recursion limitations stated.

## Executed checks

Environment: Python 3.10.12, NumPy 1.26.4. Bytecode output was disabled to preserve the packet.

Supplied suite command:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde_continuation_review_b2/code python -m unittest discover -s /tmp/pde_continuation_review_b2/code/tests -v
```

Result: **20 tests passed**, 0 failures/errors, reported runtime 0.285 seconds. This includes the prescribed order-13 certificate regeneration, not a new high-order campaign. Exact comparisons use rational equality; finite differences and finite core comparisons use the tolerances visible in the fully read tests.

Additional checks were bounded before execution in `/tmp/pde_finite_taylor_B2_diagnostics.py` and run with the same bytecode/PYTHONPATH settings. No training, trajectory integration, sampling campaign, adaptive search or generated dataset was performed.

1. Complex-step differentiation of direct output definitions for QI, IQ, QQ and RMS (epsilon 0.07 and 1.4), fixed widths 1, 2 and 4, including zero and signed coordinates: **175 parameter-coordinate comparisons passed**, maximum absolute discrepancy **2.220446049250313e-16**, against a predeclared `3e-12` absolute/relative threshold.
2. Independent exact multivariate monomial differentiation in the Gaussian primitives, widths 1 and 2, orders 0–3: all coefficient-cone and parity checks passed. Canonical derivative lists were `[0,1455,0,25604087040]` and `[0,783,0,3605283360]`. First derivatives agree with the separately derived finite identity `E D_(1,1,n) f_n = 111 + 1344/n`; the frozen identity is `63 + 672/n`. In particular the canonical limiting first coefficient is 111, consistent with the theorem's sufficient lower bound 63.
3. Exact invariant-ray coefficient and Gaussian lower-bound checks at `q=1/2,3`, odd orders 1, 3, 5 and 7: all passed as rational comparisons.
4. Pairwise independent returned Lax storage and separation from raw parameter arrays: passed for QI and IQ. Required overflowing square rejection: passed for mixed, RMS and QI Lax calls.

The first-derivative identity follows directly: conditional Gaussian contraction gives first/middle/readout expectations `48+672/n`, `36+384/n`, `27+288/n`; their sum is `111+1344/n`. These checks support the stated formulas at their tested scope. The forest and nonconvergence conclusions rest on the audited proofs, not numerical extrapolation.

## Integrity record

Before/after hashes were independently recomputed over every packet file. All 16 were identical, and all 15 payload entries matched `INPUTS.json` in SHA-256, bytes and lines. There were no extra/missing files after execution. Separate records: `/tmp/pde_finite_taylor_B2_before.json` and `/tmp/pde_finite_taylor_B2_after.json`.

The table below records each SHA-256; **the value is identical before and after**.

| File | Before = after SHA-256 |
|---|---|
| `INPUTS.json` | `6ab215441c7a0837d2d5e27c824ec03d002b818d8d934ff492ddc243cc9bd55f` |
| `code/API_ADDITIONS.md` | `eb0a736a1419ff9c1e8011d6a2fd0c5d63a9b8be7d09f321010106ec6b9cf0de` |
| `code/NUMERICAL_CONTRACT.md` | `3791adea2ec3a4713a265ab1aa2b00e9993b51a957415060bebc88fe2399de22` |
| `code/pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/exact_calculus.py` | `d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_reductions.py` | `b74b7da576e75749417dce2662e04c110f6028f09b724cfa1d295f1055c99225` |
| `code/pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tests/test_exact_calculus.py` | `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242` |
| `code/tests/test_finite_reductions.py` | `bd0063b5d7865cdb9f9b13e7bbea9118379a9baf2cb28845989ffbdd77935a9e` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `docs/finite_reductions.md` | `5c422cb6bed3ce0816853cccd78d49a85f1fd3c8ca9718528584e15dc725427f` |
| `docs/gaussian_dependencies.md` | `e52365e7ed2afaf3d48272b913caf60e1aa59f55d846019527f84ae15592cf84` |
| `docs/loss_pullback.md` | `dccefe204d607ad778a09e9a2c98ced0fbcb50a75cba869c44df9d9f652108ea` |
| `docs/positive_metric_taylor.md` | `bfe815697f0a7a6e090d3e48bcf72cdf357e2cc9fbeb837007ce636010b667b8` |

No required repairs or unresolved dependencies remain for the claims reviewed in this supplied packet. The stated exclusions above are scope boundaries, not defects.
