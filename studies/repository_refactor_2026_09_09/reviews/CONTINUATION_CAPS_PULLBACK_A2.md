# Independent complete review A2

**Verdict: CLEAN. No required correction was found in the supplied candidate.**

This is a fresh, isolated review of `/tmp/pde_continuation_review_a2`, identified by its `INPUTS.json`. I read all eleven supplied files in full (2,501 lines), including all code and tests, and checked their mathematical dependencies. All eleven supplied tests passed. Independent bounded checks passed 267 exact rational coefficient comparisons, the finite mobility/kernel/energy identities, and three cap-dissipation checks. Every supplied file's SHA-256 was verified against the manifest before and after the review and was unchanged.

The conclusion concerns the statements actually supplied: global capped dynamics on given Hilbert spaces; cap removal and strong uniqueness conditional on quantitative exponential tails; exact finite Euler coefficients with a fixed-order remainder; and a conditional finite-dimensional tube estimate. It does not certify the exponential-tail premise, construct a Gaussian action space, identify a finite-width limit, or establish any empirical training conclusion.

## Scope and method

- Candidate inputs were read only. No checkout files, studies, history, previous reports, or other tasks were inspected, and no review work was delegated.
- Applied `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md` as requested. The required references read were `research-contract.md`, `adversarial-audit.md`, `evidence-ledger.md`, and `decisive-experiments.md` in the latter skill's `references` directory. A bounded review does not require the multi-route proof-search reference.
- The analysis used the supplied definitions and proofs, with direct derivations of the needed estimates. No unverified specialized external theorem or source was used. The elementary Gaussian and Hilbert-space facts needed here are derived in the supplied dependencies.
- The computation was deterministic and bounded. The supplied certificate test was run as part of the required eleven tests; the independent polynomial checks stopped at degree six. There was no sampling, training campaign, large-order extension, or width sweep.
- Review artifacts are outside the candidate: `/tmp/pde_caps_pullback_A2_before.json`, `/tmp/pde_caps_pullback_A2_after.json`, `/tmp/pde_caps_pullback_A2_check_plan.md`, `/tmp/pde_caps_pullback_A2_checks.py`, and this report.

## Full-read ledger

Every interval in this ledger was read completely, rather than sampled or inferred from tests.

| Supplied file | Lines read | Role and completed audit |
|---|---:|---|
| `code/NUMERICAL_CONTRACT.md` | 1–91 | Finite coordinate, loss, mobility, callback, numerical-range, and ownership contract |
| `code/pde/__init__.py` | 1–26 | Imports and public exports; exact operations correctly used through their module |
| `code/pde/exact_calculus.py` | 1–249 | Both Euler APIs, all arithmetic helpers, reversion, determinant, forest key, and fixed certificate |
| `code/pde/finite_network.py` | 1–363 | Input validation, forward/backward evaluation, all gradient/velocity/kernel factors, simultaneous GD, numerical caveats |
| `code/pde/gaussian_moments.py` | 1–114 | Rational validation, singular PSD cases, Wick recurrence, cache scope |
| `code/tests/test_exact_calculus.py` | 1–217 | Every helper and all eleven test methods; exact expectations and independence of checks |
| `docs/NOTATION.md` | 1–98 | State types, normalization, residual-free backward fields, mobilities, clocks, scope |
| `docs/finite_dynamics.md` | 1–214 | Derivatives, kernel blocks, dissipation, finite global existence, width-dependent and width-independent bounds |
| `docs/gaussian_dependencies.md` | 1–346 | Gaussian recurrence/PSD proof, forest expectation factorization, formal certificate and its restricted interpretation |
| `docs/given_space_caps.md` | 1–417 | Every definition, estimate, global capped-flow proof, conditional continuation and uniqueness proof |
| `docs/loss_pullback.md` | 1–366 | Every regularity condition, noncommuting word identity, temporal coefficient, cubic formula, remainder and tube estimate |

Total: **11 files, 2,501 lines**. `INPUTS.json` was also read and used to verify provenance.

## Mathematical claim ledger

| Claim | Status within the supplied scope | Critical assumptions retained |
|---|---|---|
| All given-space fields are defined, continuous and bounded on state balls | Verified | Probability-space L2 spaces; bounded given operator with its genuine adjoint; HS increments; the specified activation |
| Loss chain rule along C1 Hilbert-state curves | Verified | Strong curves and bounded continuous activation derivative; no unsupported global Frechet differentiability assertion |
| Theorem 12.1: unique global capped strong solution | Verified | Fixed cap R; stated initial state with zero readout; common radial cap on the three incoming sample fields |
| Theorem 12.2: cap removal and uniform strong field/kernel convergence | Verified conditionally | Uniform exponential L2 tails (12.17), for every compact horizon |
| Theorem 12.2: uniqueness against arbitrary strong competitors and restart at reached states | Verified conditionally | The constructed reference has inherited exponential tails; competitors are bounded on their compact intervals |
| Finite Euler word identities and temporal table | Verified | Fixed finite order, sufficient Cj regularity, and a common local step interval |
| Fixed-N integral remainder through degree five | Verified | C6 scalar paired map, supplied by C6 u,v; P in C7 is a sufficient gradient-field condition |
| Generic and full-square-loss cubic formulas | Verified | Euclidean coordinates after the constant mobility change; arbitrary residual; separately stated C3 predictor condition |
| Convex-tube comparison and dyadic Cauchy conclusion | Verified conditionally | Uniform derivative/field bounds and inclusion of all relevant hybrid and intermediate states |
| Gaussian action construction, tail proof, finite-width GF/GD identification, increasing-order convergence | Not asserted or established | The candidate explicitly leaves these separate |

## Detailed audit of `given_space_caps.md`

### Spaces, differentiation and metric

Lines 24–67 consistently distinguish the bounded base operator from its Hilbert–Schmidt increment. The state norm is the direct-sum Hilbert norm with ordinary HS pairing. The displayed rank-one norm and pairing identities follow from Parseval and Cauchy–Schwarz; they give the correct gradient in the middle block. Neither finite-dimensionality nor a Hilbert–Schmidt base operator is silently assumed.

The initialization is an element of the stated state space. The additional three first-preactivation norm conditions do not substitute for membership in that space. Coincident inputs and a singular input Gram cause no problem: only the three unit vectors and their pairings are used, never a Gram inverse.

For the displayed activation, `|phi| <= 1 + |z|`, `3/4 <= phi' <= 1`, and `|phi''| <= 1/2` are valid. Consequently the forward maps and residuals are Lipschitz on each bounded state ball. Each backward product is an L2 field because its gate is bounded. Equation (12.6) correctly proves continuity of a gate times an L2 amplitude by a subsequence/dominated-convergence argument; it does not claim an unavailable L2 product Lipschitz estimate.

The chain-rule proof at lines 117–137 is sufficient. A continuous L2 velocity admits jointly measurable time-integral representatives that are absolutely continuous pointwise almost everywhere. The scalar chain rule, followed by (12.6), identifies a continuous L2 derivative. Bounded-operator product differentiation, the genuine adjoint, and the HS rank-one pairing then yield (12.7). Thus the energy calculations have the required chain rule even without using Frechet differentiability of the activation map on an entire L2 ball.

### Global capped existence and dissipation

The cutoff in (12.8) is smooth, coincides with the identity near zero, and is bounded by `min(|input|, 2R)`. Its scalar derivative and radial/tangential eigenvalues lie in `[0,1]`; integration along segments proves the stated Lipschitz constants. The function chi is positive and at most one. The tail defect inequalities (12.9) are valid, including their zero cases.

The auxiliary top cap with `M = 1 + 2RT` makes the extended field Lipschitz on state balls. The gate estimates have the claimed linear growth in R: the top gate contributes `O(M)`, while the lower radial cap's input Lipschitz constant is one and its bounded output contributes `O(R)`. These contributions add; they do not multiply. Expanding residual, operator, and rank-one differences verifies the remaining blocks. The field norm itself has a cap-independent bound on each fixed state ball.

The short-time integral-map construction takes place in a complete continuous-path space. The readout equation gives `|W3(t)| <= 2Rt`, so the auxiliary top cap is inactive on the constructed path before T. It therefore solves the original capped equations. The same pointwise bound holds for any strong solution with this initialization, allowing the extension's uniqueness to identify all such solutions.

Equation (12.16) uses exactly one common scalar chi multiplying the entire first-row gradient. This is essential when sample directions cancel, and the supplied radial cap has exactly that property. Since `chi^2 <= chi`, each capped block dissipates at least the squared norm of its actual velocity. Integrating gives the loss bound and the path displacement `sqrt(3t/2)`, with `E0 = 3/2` from three labels of magnitude one and zero initial readout.

The global continuation argument does not invoke compactness of a Hilbert ball. The energy estimate confines the solution to a fixed ball; the bounded field makes it Cauchy at any finite maximal endpoint; completeness gives a limiting state. Strong L2 convergence preserves the readout bound by an almost-sure subsequence, and the same locally Lipschitz extension continues the solution. Horizons agree by uniqueness. The uniform true-field bounds then follow from the cap-independent energy ball.

### Conditional cap removal and uniqueness

The moment/tail argument at lines 281–305 is correct. Assumption (12.17) gives an exponential probability tail for the readout direction and hence `||g3||_j <= D_T j`. Since the readout starts at zero and `|tau_R(g3)| <= |g3|`, Minkowski yields `||W3(t)||_j <= T D_T j`. Choosing integer `j` proportional to the amplitude in Markov's inequality gives an exponential probability tail. The tail integral identity then gives the L2 exponential tail (12.19), after decreasing the rate to absorb polynomial factors. Constants can cover small thresholds uniformly.

Equation (12.20) correctly uses a tail only on one reference amplitude. Applying it first to the reference readout controls the top-gate difference. Operator and residual differences retain a single cutoff factor. At the lower gate the incoming difference is multiplied by a bounded gate, and only the other summand uses the reference P tail. This verifies `K(1+L)s + K exp(-cL)` in (12.21), with no hidden L-squared factor. Optimizing L gives the increasing logarithmic modulus (12.22) on the chosen distance range.

The defect bound (12.23) is valid: the middle block has no defect, the first block uses Cauchy–Schwarz over three unit input vectors, and the readout defect is exactly controlled by its stated tail. For any real cap pair `R' >= R`, both defects are bounded by an exponential in R.

The scalar comparison in (12.24)–(12.25) yields uniform Cauchy convergence. A positive majorant starts at delta, its forcing is at most `Y log(B/Y)` within the comparison range, and integration gives the stated fractional-power bound. For large R this bound stays inside that range on the entire fixed horizon, closing the first-exit argument. It applies to the full real-indexed cap family, rather than only a selected sequence.

Uniform convergence of continuous field maps along these paths is justified by compactness of the time interval and continuity at the limiting path, not by compactness of a state ball. The integral equations pass to the continuous true field. All named L2 fields converge strongly and uniformly, and Cauchy–Schwarz gives the three raw kernel limits in (12.18). The exact limit energy identity follows from (12.7).

Fatou's lemma at threshold a/2 transfers the tails to the limit at every time with common constants. A time-dependent almost-sure subsequence is sufficient for these pointwise-in-time bounds. The logarithmic comparison therefore applies with the limit as reference and any strong competitor on its bounded compact path. Sending the positive majorant's initial value to zero proves uniqueness without assuming tails for the competitor. The same argument applies from a reached state, while the already constructed global curve supplies continuation existence. This establishes exactly the stated restart domain.

### Clocks and limits

The half-sum loss E and mean loss L satisfy `L = 2E/3`; the mean-loss flow is the E-flow evaluated at `2t/3`. The statement about capped time rescaling explicitly scales the entire capped field, which is the condition needed. No transformation of raw GD is inferred. The theorem is on the given operator spaces and its constants are compact-horizon constants. The text correctly does not infer exponential tails from bounded L2 norms or identify this model with initialized finite neural networks.

## Detailed audit of `loss_pullback.md`

### Mobility coordinates, domains and finite words

The raw mobility matrix is the one in the notation and finite-dynamics dependencies. With `theta = D^(1/2) x`, the chain rule gives `grad_x L = D^(1/2) grad_theta L`; hence simultaneous raw GD becomes exactly `x+ = x - eta grad_x L`. The linear change preserves Euler updates. For the full one-sample square loss, `v = -2 r grad f`, including the moving residual. A batch mean loss uses its full gradient and the stated mean factor. The step eta and the count N are kept separate from physical time and feature time.

For every fixed N, continuity gives a local interval of positive and negative step arguments on which the finite iterates remain in the open domain. Finite composition is C6 under the stated assumptions. This is enough for the scalar integral remainder. The generic order-j identity needs only finite-order derivatives; no analytic assumption is used.

The operator `T_k` differentiates only the observable in its inner definition; an outer operator differentiates the resulting field dependence as well. Thus `T_1^2 u = D^2u[v,v] + Du[Dv v]`, with the moving-field term correctly retained. The positive-composition recurrence partitions by the first part and terminates by decreasing total order.

For fixed M, `(I+B_eta)^M` is a binomial identity in the single pullback-difference operator. It does not assume commutativity of different T operators. Differentiating at a finite target order j selects positive compositions and gives weight `binom(M,q)` for each word of length q. Intermediate derivatives use at most j derivatives of u and j-1 of v. A common neighborhood for the finitely many compositions is available locally, so there is no operator-domain or infinite-series assumption hidden in this calculation.

Subtracting M=N, step 2 eta from M=2N, step eta gives `Q_(j,q)(N) = binom(2N,q) - 2^j binom(N,q)`. The zero and first coefficients vanish. The degree-j term cancels in the q=j row; every other row already has degree at most j-1. Every displayed entry through degree five agrees with this formula.

The remainder in (9.P13) has the correct coefficient `eta^6/5!` and weight `(1-s)^5`. Its derivative is the sixth derivative with respect to the scalar step argument. The text explicitly restricts this identity to fixed N and does not infer uniform remainder control.

### Cubic coefficients and the full square loss

Summing the cubic Euler increments gives the three state terms in (9.P16): `M v`, `binom(M,2) Dv v`, and the two cubic coefficients `binom(M,3)` and `M(M-1)(2M-1)/12`. Pairing the fine and coarse paths leaves the coefficients in (9.P17). In the gradient case the Hessian symmetry gives `Du[a] = -T_P`, `Du[b2] = -S_P`, `Du[b3] = -U_P`, and `D^2u[v,a] = -S_P`. Consequently (9.P15), including its sign and factor one-half, is correct.

For `P = -r^2`, direct differentiation gives `b = -2rg`, `H_P b = 4rK g + 4r^2 H_f g`, and the stated T_P and S_P. The third derivative gives `U_P = 16r^4 U + 48r^3 K B`. Combining `4S_P+U_P` produces exactly the coefficient 11 on `r^3 K B` in (9.P21). The additional C3 predictor assumption is explicitly present; smoothness of the squared loss alone is not being used to infer predictor smoothness.

All residual powers and normalizations agree for arbitrary labels and arbitrary supplied states. If r or g vanishes, the vector field is zero at that state and the entire Euler sequence remains fixed. For an affine predictor, the residual recurrence gives the displayed exact powers and checks both low-order coefficients. The independent bivariate cubic checks below also agree exactly for nonzero arbitrary residuals.

### Tube bound and its boundary

The convex set contains all hybrid macro-step compositions and intermediate fine-step states. This is sufficient for every segment and pair of states used in the mean-value and propagation estimates. The local defect is exactly `eta [v(x+eta v(x))-v(x)]` and is bounded by `L_T M_T eta^2`. Each fine macro-step has Lipschitz factor at most `(1+eta L_T)^2` on the relevant pairs. Telescoping the N+1 hybrid endpoints produces the geometric sum and exponential bound in (9.P24).

The observable derivative bound gives (9.P25), including `T^2/(4N)` and `exp(L_T T)`. Zero values of any bound require no division and are covered. Uniform constants over the stated dyadic refinements give a summable series of successive differences and hence terminal state and observable Cauchy convergence. This is the conditional conclusion stated; the document does not assert arbitrary-partition convergence, a population theorem, or a common width-uniform tube.

The fixed-order degree cancellation makes each fixed coefficient term O(1/N) at eta=T/(2N). The explicit warning that this does not bound the remainder or justify increasing-order summation is correct and necessary.

## Code and dependency audit

`euler_pullback_words` validates both arguments before its zero-order cases. Exact Python nonnegative integers are accepted; booleans, floats and Fractions are rejected. The finite stack reaches each positive composition once and limits its length to the number of steps. Every returned nonzero weight is precisely the Fraction of `comb(steps, length)`. The empty-word/zero-step cases and fresh dictionary ownership agree with the documented contract. The exponential composition count and tuple-storage qualification are accurate; large integer bit lengths are not hidden by the cost statement.

`paired_euler_weights` starts from the constant binomial polynomial and multiplies by `(N-q+1)/q` exactly. Its degree-k coefficient multiplier is `2^k - 2^order`, which implements the required substitution and paired subtraction. Omitting the potential degree-order entry is justified by cancellation. Return shapes, exact Fraction values, zero-order behavior, immutability, and O(order-squared) rational-operation/storage costs agree with the contract. Neither routine evaluates derivatives, mutates input, draws samples, persists a cache, or writes files.

The remaining exact arithmetic is also consistent with its supplied proofs. Series reversion has a nonzero linear pivot and zero constant; its truncated Horner compositions are used with zero-constant inner series. Determinant elimination tracks row-swap signs and handles singular and empty matrices. Forest union-find rejects precisely duplicates/cycles in the allowed bipartite graph, and the all-roots canonical key correctly preserves decorations and repeated components. The fixed certificate regenerates the stated monomial derivatives, formal inverse, kernel coefficients, shifted determinant and negative polynomial witness. The provided tests check its numerical values by a separate determinant route and direct witness evaluation.

The Gaussian moment validator handles rational symmetric PSD matrices, including zero pivots and singular covariance. Its degree recurrence terminates, and all arguments are validated even for zero or odd total degree. The local cache is cleared. The forest factorization proof counts Gaussian pairings and quotient vertices consistently, including component merging, odd-edge components and isolated vertices. It establishes an expectation limit only. The quadratic certificate's frozen first block, order-one readout, auxiliary feature-ascent clock and formal-series status are explicitly separated from the canonical model; the moment obstruction is not promoted into nonexistence of a nonlinear training limit.

The finite network and `finite_dynamics.md` agree on input division by sqrt(d), stored hidden matrices, readout division by n, residual-free backward arrays, loss factor 2/m, and endpoint versus middle mobilities. Gradients and kernel blocks use ordinary Euclidean/Frobenius pairings. GD uses simultaneous contractions from the original state. The constant mobility coordinate change in the pullback document therefore matches the executable finite API.

The finite global-flow proof uses nonnegative loss, the weighted energy identity and a finite-dimensional Cauchy endpoint argument; arbitrary C2 activations suffice there. Its separate width-uniform field bounds require bounded activation derivatives and controlled initial norms as stated. The finite Gaussian initialization bounds and net argument retain the proper width and depth qualifications. The implementation's finite float64 checks, private activation callback copies, fresh GD arrays, and documented intermediate-overflow caveats are consistent with the scope of a numerical reference implementation.

## Validation executed

Environment: Python 3.10.12, NumPy 1.26.4. Both commands used the candidate alone on PYTHONPATH and disabled bytecode writes.

### Required supplied tests

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde_continuation_review_a2/code python -B -m unittest discover -s /tmp/pde_continuation_review_a2/code/tests -p test_exact_calculus.py -v
Ran 11 tests in 0.178s
OK
```

The eleven methods cover the certificate, Euler domains/ownership, displayed temporal polynomials, nonlinear scalar differential words, independent active-slot enumeration, forest components/decorations, invalid graphs, relabelling, rational determinants, invalid rational inputs, and two-direction series reversion.

### Independent bounded checks

The independent plan was written before executing the independent script. Its pass rule was exact rational equality for coefficient checks, discrepancy below 1e-7 for the finite directional derivative checks, and 1e-12 roundoff tolerance for the cap-dissipation sanity check. The script had a 60-second limit and completed in approximately half a second without retries or failed branches.

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde_continuation_review_a2/code timeout 60s python -B /tmp/pde_caps_pullback_A2_checks.py
status: PASS
exact_word_comparisons: 24
exact_paired_comparisons: 15
exact_temporal_evaluations: 210
exact_cubic_coefficient_comparisons: 18
finite_output_max_abs_error: 6.368836014125634e-12
finite_loss_abs_error: 6.405899248551616e-11
finite_energy_abs_error: 8.673617379884035e-19
cap_dissipation_cases: 3
```

The word comparison used an independently implemented sparse bivariate derivative algebra and direct truncated Euler substitution, with `v(x,y) = (1+xy, x^2-y)`, `u(x,y) = x^3+xy+2y^2`, and state `(1/3,-2/5)`. It checked orders zero through five for 0, 1, 2 and 4 updates; paired comparisons used N=1,2,3. Temporal rows were evaluated at N=0 through 9, through order six, and compared directly with integer binomial values.

The cubic loss check used `f(x,y) = x^3/3 + xy + y^2 + 2x` at the same state, labels `7/4,-1,0`, and N=1,2,3. Its gradient, Hessian and third-derivative contractions were computed separately from direct loss-Euler composition. Both coefficients agreed exactly in every case.

The finite identity check used one fixed two-layer, width-two network, three samples including a duplicated input, and nonunit block multipliers `(0.7,1.3,1.1)`. It verified raw gradients versus velocities, the linear mobility coordinate change, one simultaneous GD update and independent returned arrays, output/kernel contraction, weighted loss dissipation, and kernel positive semidefiniteness. These are local identity checks, not training or population evidence.

The cap sanity check used a three-atom probability space, cancelling sample directions, the displayed smooth cutoff and R=1,2,4. It checked `E' <= -||velocity||^2`. Quadrature only supplied cutoff values for this finite check; the analytic proof relies directly on `0 <= chi <= 1` and does not depend on quadrature.

## Required corrections and remaining obligations

**Required corrections: none.** No formula, domain, metric, clock, normalization, code-contract or proof gap requiring repair was found.

The substantive limits are already stated in the candidate and are not defects in these theorems: the exponential-tail premise remains an assumption; the Hilbert spaces and base operator are supplied; canonical Gaussian-space construction and finite-width GF/raw-GD identification remain separate; fixed-order Euler algebra does not imply a uniform analytic remainder; and the tube inclusion is conditional. The tests support the finite code and coefficients only.

## Provenance and before/after hashes

The SHA-256 of the read `INPUTS.json` is `a73ff4662dc7acc075afdb9aa353581f3f6caa6f5e37ea096ff6f9c078e76c1d`. The following table records the identical before and after hash for each supplied file; both copies also match the manifest. Separate machine-readable before and after records are retained at the paths listed above.

| File | SHA-256 before = after = manifest |
|---|---|
| `code/NUMERICAL_CONTRACT.md` | `3791adea2ec3a4713a265ab1aa2b00e9993b51a957415060bebc88fe2399de22` |
| `code/pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/exact_calculus.py` | `d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tests/test_exact_calculus.py` | `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `docs/gaussian_dependencies.md` | `e52365e7ed2afaf3d48272b913caf60e1aa59f55d846019527f84ae15592cf84` |
| `docs/given_space_caps.md` | `cdda914e481b46d51366a5d80661cd192b0f319d6507bc8b29eba69d87f9f95d` |
| `docs/loss_pullback.md` | `dccefe204d607ad778a09e9a2c98ced0fbcb50a75cba869c44df9d9f652108ea` |
