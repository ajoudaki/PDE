# Independent complete review B2

**Verdict: CLEAN. No required correction was found in the supplied candidate.**

This is a fresh, complete review of `/tmp/pde_continuation_review_a2`, identified by its `INPUTS.json`: 11 supplied files, 2,501 lines. All files were read in full, including the two primary proof chapters, their supplied mathematical dependencies, every supplied implementation, and the entire test file. No checkout, study directory, history, prior report, other task's findings, or delegated review was used. The candidate was not edited. Before/after SHA-256 values, byte counts, and line counts agree with each other and with the manifest for all 11 files.

The requested `solve-math-rigorously` and `investigate-conjectures` skills were read. Relevant investigation references read in full were `research-contract.md`, `evidence-ledger.md`, `adversarial-audit.md`, and `decisive-experiments.md`. The audit used direct derivations, the supplied source, the 11 supplied tests, and a fixed set of independent deterministic checks. It did not require an external theorem lookup, train a model, conduct a high-order campaign, or infer a population limit from code.

**Full-read ledger**

All ranges below were read completely; split tool reads covered the complete indicated ranges without relying on truncated output.

| Supplied file | Fully read lines | Audit role |
|---|---:|---|
| `code/NUMERICAL_CONTRACT.md` | 1–91 | Finite model, API, normalization, numerical limitations |
| `code/pde/__init__.py` | 1–26 | Package exports and import dependencies |
| `code/pde/exact_calculus.py` | 1–249 | Both Euler APIs; all other exact primitives and certificate |
| `code/pde/finite_network.py` | 1–363 | Forward/backward equations, gradients, raw mobility, GD, kernels, validation |
| `code/pde/gaussian_moments.py` | 1–114 | Rational covariance validation and Wick recurrence |
| `code/tests/test_exact_calculus.py` | 1–217 | All 11 tests and independent helper implementations |
| `docs/NOTATION.md` | 1–98 | Shared coordinates, metrics, residuals, initializations, clocks |
| `docs/finite_dynamics.md` | 1–214 | Exact finite derivatives, kernels, dissipation, global existence, width bounds |
| `docs/gaussian_dependencies.md` | 1–346 | Gaussian moments, forest factorization, formal initialization certificate |
| `docs/given_space_caps.md` | 1–417 | Global given-space capped flow and conditional uncapped continuation |
| `docs/loss_pullback.md` | 1–366 | Exact finite Euler words, complete temporal table, cubic loss and tube bounds |

**Research contract and claim ledger**

| Claim | Reviewed conclusion | Limits that remain explicit |
|---|---|---|
| Theorem 12.1 | The proof establishes a unique global strong capped solution on the stated separable L2/HS state space, with the stated dissipative bounds. | Initial operator spaces and the bounded operator with its genuine adjoint are supplied; this constructs no Gaussian action. |
| Theorem 12.2 | The stated uniform exponential square-tail premise implies full-family strong convergence, a global strong uncapped solution, field/kernel convergence, the exact energy identity, uniqueness against arbitrary strong competitors, and restart uniqueness on the reached curve. | The quantitative tail premise is an assumption, not a consequence established by Theorem 12.1. |
| Equations 9.P7–9.P13 | Exact finite Taylor coefficients and the fixed-N sixth-derivative integral remainder follow under the displayed regularity/domain assumptions. | No infinite series convergence or N-uniform remainder is asserted. |
| Equations 9.P15–9.P21 | The generic gradient-loss cubic and the arbitrary-residual full-square specialization are correct. | Predictor C3 regularity is separately stated; the residual moves in every actual raw Euler update. |
| Equations 9.P24–9.P25 | The convex-tube hypotheses imply the stated paired Euler bounds and dyadic terminal Cauchy conclusions. | Inclusion of all hybrid/intermediate states and uniform bounds are assumed. No population, arbitrary-partition, or width-uniform conclusion follows. |
| Exact APIs | Implementations meet the displayed input, output, ordering, rational arithmetic, ownership and finite-complexity contracts. | They enumerate coefficients; they do not evaluate derivatives or network expectations. |
| Supplied dependencies | No required correction was found in their stated finite identities, Gaussian algebra, formal certificate or supporting implementation. | Their deliberately distinct initialization, metric, probability mode and formal-series scopes remain distinct. |

**Proof audit: given-space caps**

- Lines 15–20 correctly distinguish the half-sum energy E from the three-sample mean squared loss: the latter is 2E/3, so the uncapped gradient field is multiplied by 2/3 and its solution is the E-flow at time 2t/3. The capped time rescaling is asserted only when the entire capped field is scaled. No discrete raw-GD equivalence is inferred.
- Lines 24–67 provide the needed state and operator types. The fixed middle action is bounded with its actual adjoint, while only the trained increment is HS. The Hilbert–Schmidt completeness, operator bound and rank-one pairing are valid. The initial state is specified in the Hilbert state space. No inversion or nonsingularity of the sample Gram is used.
- Lines 69–115 have valid layerwise products. Bounded activation gates put backward fields in L2; forward fields and scalar residuals are Lipschitz on bounded state balls. The product-continuity lemma is valid by a fixed L2 multiplier, an almost-sure subsubsequence and dominated convergence. It yields continuity without incorrectly asserting local Lipschitzness of the full uncapped field on an L2 ball.
- Lines 117–137 correctly prove the loss chain rule along C1 Hilbert curves. Integrable velocity gives coordinatewise absolutely continuous representatives; the bounded continuous gate and the product lemma make the differentiated activation velocity continuous in L2. The operator-product derivative and genuine-adjoint/HS rank-one identity then give precisely the displayed three pairings. No false global Fréchet differentiability claim for a Nemytskii activation is needed.
- Lines 141–162 define genuine smooth caps. The scalar derivative is between zero and one; radial and tangential eigenvalues give the vector 1-Lipschitz bound. Both maps equal the identity near zero, reduce magnitude, and obey the displayed tail-defect bound. The scalar multiplier is positive, even when its signed scalar input is negative.
- Lines 183–230 correctly introduce a fixed auxiliary top cap to obtain a locally Lipschitz autonomous extension. The top-gate multiplier contributes M, and the lower cap contributes R; the vector cap's input Lipschitz constant is one, so no product RM is introduced. Since M=1+2RT, the ball-wise Lipschitz constant is of the claimed form. Explicit field-norm bounds on bounded balls are independent of both cap sizes.
- Lines 231–252 establish that the auxiliary top cap stays inactive before T. The readout integral supplies the pointwise 2Rt bound. The common first-row scalar cap multiplies the full gradient, so the energy identity remains valid under cancellation between sample directions. The inequality is exactly chi squared ≤ chi. E(0)=3/2 follows from the zero readout and the three unit-magnitude labels. Energy, time Cauchy–Schwarz, completeness and local extension establish global existence and uniqueness, including all strong solutions of the actual capped equation.
- Lines 281–304 validly convert the assumed uniform square tails of g3 into uniform integer Lp bounds, use the readout integral and Minkowski, choose p proportional to the threshold in Markov's inequality, and recover exponential square tails for the readout. Small thresholds and polynomial prefactors are absorbed by enlarged constants and a smaller positive rate. No Gaussian distribution is assumed.
- Lines 307–348 provide the crucial one-sided comparison. The top gate uses only the reference readout tail. The lower gate uses the reference residual-weighted incoming P tail; the already estimated incoming difference is multiplied by a bounded gate. Thus the estimate is K(1+L)s+K exp(-cL), with one cutoff factor, not a squared cutoff factor. Optimizing L gives an increasing Osgood modulus s log(B/s). This estimate needs tail bounds only for the reference state, not for an arbitrary competitor.
- Lines 350–382 correctly bound the capped defect by the P and g3 tails. The factor sqrt(3) follows from the three unit input vectors, and the HS component has no cap defect. The positive scalar majorant, logarithmic substitution and first-exit comparison yield a bound tending to zero uniformly on each compact time interval. This makes the entire real-indexed cap family Cauchy, rather than merely constructing a convergent subsequence.
- Lines 384–407 correctly pass field maps along uniformly convergent paths by continuity and compactness of the time interval; no compactness of a bounded Hilbert ball is assumed. The limiting integral equation has a continuous integrand and hence a C1 solution. L2 convergence and Cauchy–Schwarz give all three true raw kernel blocks. Fatou at half the threshold passes both needed tail bounds to the limit uniformly in time even though subsequences may depend on time. The one-sided modulus then proves uniqueness against any strong competitor on a common compact interval, and the same argument proves restart uniqueness at reached states. The global reference curve supplies those continuations.
- Lines 409–417 correctly state the remaining gap. The norm-one shrinking-support example disproves the inference from L2 boundedness to uniform square tails but is not presented as a trained-path counterexample. Neither a finite-width identification nor persistent nonlinear feature motion is claimed.

**Proof audit: finite loss pullback**

- Lines 11–42 use ordinary flattened Euclidean/Frobenius parameters and the actual positive-definite raw mobility matrix. The linear substitution x=D^(-1/2) theta transforms simultaneous raw GD exactly into Euler for minus the full squared-loss gradient. For one sample v=-2r grad f; there is no missing half-loss, sample, width or mobility factor. The general fixed-batch observation is valid with P equal to minus the mean loss.
- Lines 44–56 state an open finite-dimensional domain and a fixed-N step interval containing zero on which all needed iterates exist. Finite composition is C6; P in C7 is a sufficient loss-potential assumption. Negative small steps cause no issue for the local Taylor identity.
- Lines 60–123 define the frozen-direction operator correctly. Outer operators differentiate the state dependence of inner fields. The composition recurrence enumerates every positive ordered composition once. The binomial formula is for the single exact operator P_eta-I and does not require the T_k to commute. Differentiating the finite products yields exactly the indicated words, with the regularity required for each finite total degree. M=0 and order zero are handled separately.
- Lines 125–155 give the correct coefficient binom(2N,q)-2^j binom(N,q), with cancellation of the degree-j term when q=j. Every displayed rational polynomial through degree five is correct. The cancellation is termwise and does not presume a neural identity between word values.
- Lines 157–169 contain the correctly normalized integral remainder: eta^6/5! times the weighted integral of the sixth derivative. The entire segment lies in the step interval. This is an exact fixed-N identity and supplies no uniform-in-N derivative bound.
- Lines 173–217 give the correct direct cubic Euler state expansion. The paired cubic is 2N(N-1) Du[b2] + N(2N-1) Du[b3]/2 + 2N^2 D2u[v,a]; substituting u=-P and v=grad P gives exactly -N T_P eta^2 - N(2N-1)(4S_P+U_P)eta^3/2.
- Lines 219–263 separately require predictor C3 for its invariants. The full-square substitutions give T_P=-8r^2 K^2-8r^3 B, S_P=16r^2 K^3+32r^3 KB+16r^4 S, and U_P=16r^4 U+48r^3 KB. They reproduce the coefficient 11 on r^3 KB in 9.P21. Zero residual or zero predictor gradient is an exact stationary Euler state. The affine closed form has the displayed exponents and agrees with the quadratic/cubic coefficients.
- Lines 267–316 include the hybrid macro-step and intermediate fine states needed by the telescoping proof. Convexity supplies all derivative-estimate segments. The local defect is LM eta^2, fine macro-step amplification is (1+eta L)^2, and summation gives LM N eta^2 exp(2LNeta); the scalar bound adds R. Zero constants and eta=0 remain valid. Uniform assumptions across dyadic refinements make the terminal differences summable. The conclusion is Cauchy convergence in finite dimensions, not an unstated population theorem or a claim that a limit must remain in a nonclosed tube.
- Lines 318–324 correctly prevent promotion of fixed-order N-degree cancellation into a summed series, uniform remainder, or verified tube assumption.

**Code and dependency audit**

`euler_pullback_words` validates both arguments before handling zero order, rejects non-Python integers and booleans as documented, returns fresh dictionaries, reaches every positive composition of permitted length exactly once, and emits exact Fraction binomial weights. Dead prefixes at the step limit are not emitted; zero weights are absent. Empty-word and zero-step behavior is correct. The documented exponential composition count and O(j 2^j) tuple construction/storage upper bound are appropriate finite arithmetic bounds, with unbounded integer bit lengths explicitly acknowledged.

`paired_euler_weights` recursively constructs binom(N,q) by multiplying by (N-q+1)/q, then scales its degree-k coefficient by 2^k-2^order. Omitting the final degree-order coefficient is correct because it vanishes. The zero/first orders, row order, increasing power order, exact Fraction types and immutable output match the chapter. The O(j^2) arithmetic/storage statement is appropriate. Neither Euler API retains a cache, mutates arguments, writes files, or performs derivatives or Gaussian expectations.

The rest of `exact_calculus.py` was also audited: rational input checks, series reversion recurrence, exact determinant pivoting, colored bipartite forest validation/canonicalization, and the fixed quadratic certificate agree with their supplied proofs. The Gaussian moment implementation uses an exact Schur-complement PSD check, including singular zero pivots, and the correct degree-reducing Wick recurrence. Its memoization is local and cleared. The forest leading-factorization proof keeps neuron populations separate and counts collision losses correctly; it asserts expectations only. The quadratic certificate uses the explicitly different frozen-first-block feature metric and order-one stored readout, proves fixed-order annealed initialization derivatives, and treats the inverse series as formal. The negative shifted-moment witness is a finite representation obstruction over that stated scope.

The finite network implementation matches the shared equations: first input division by sqrt(d), no additional hidden width factor, readout division by n, residual-free backward derivatives, mean-square loss, endpoint mobilities n*kappa and middle mobilities kappa. Gradients, all three block types, simultaneous raw GD and the weighted energy identity have the required factors. The supplied numerical contract accurately limits float64 guarantees, including possible intermediate contraction overflow/underflow. Callback inputs and returned arrays are isolated as documented; zero-step GD returns independent parameter copies after structural validation. No additional export of the two exact-calculus functions is required: their documented interface is the `pde.exact_calculus` module.

The finite-dynamics existence proof uses finite-dimensional local Lipschitzness and the nonnegative-loss energy estimate to preclude finite-time escape. Its width bounds require bounded activation derivatives and the stated initial norms, and its Gaussian initial-event argument uses fixed depth and explicit net/tail bounds. It does not identify a nonlinear population trajectory.

**Executed validation**

Environment: Python 3.10.12; NumPy 1.26.4. Candidate imports used `PYTHONDONTWRITEBYTECODE=1`; no cache files or other files were added to the candidate.

Supplied test command:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde_continuation_review_a2/code python -m unittest discover -s /tmp/pde_continuation_review_a2/code/tests -p 'test_exact_calculus.py' -v
```

Result: exit status 0, **11 tests passed**, reported test runtime 0.185 seconds. The executed cases covered all displayed certificate integers/fractions and the independent determinant/witness, Euler argument domains and ownership, every displayed temporal polynomial, nonlinear scalar direct Euler versus differential words through degree six, independent active-slot enumeration, all forest tests, both-direction formal reversion, determinant edge cases, and invalid rational inputs.

Independent check script: `/tmp/pde_caps_pullback_B2_checks.py`.

SHA-256: `7807b5c4fe90ce973f9fa2a2533c4e9b2072aae3a7a545eda1c42e63ce900f56`.

Its finite scope and pass rules were written before execution: exact rational equality for a two-dimensional moving square-loss polynomial through degree five with N=1,2,3, temporal weights through degree six, and numerical finite-metric checks with absolute tolerance 2e-8. The selected predictor was

```text
f(x,z) = 1/5 + x + 2z + xz + x^2/3 + z^3/4,
y = -2/7,  (x0,z0) = (1/3,-2/5).
```

Its residual and B,S,U invariants are all nonzero. The script evaluates multivariable T_k via the partial-derivative multinomial formula and direct Euler composition via independently truncated univariate step polynomials. This exercises moving fields and cross-coordinate derivatives beyond the supplied scalar test. The finite-network diagnostic uses n=d=2, m=3, duplicate inputs and unequal positive mobilities; its independent centered-difference predictor Jacobian determines all block kernels as J D J^T. The cap diagnostic uses unequal atomic probabilities on the two layers, the actual weighted adjoint, and the actual HS metric sum p2_i/p1_j times U_ij^2; it checks the chain rule and prescribed common-row/readout cap dissipation. Scalar cap integration uses fixed 64-point Gauss–Legendre quadrature. These numerical diagnostics are finite consistency checks, not proofs of the infinite-dimensional theorem or its tail premise.

Command:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde_continuation_review_a2/code python /tmp/pde_caps_pullback_B2_checks.py
```

Result: exit status 0, all fixed checks passed:

```text
PASS 2D moving square-loss Euler: 36 exact word/paired coefficient comparisons plus 6 exact cubic-invariant comparisons; nonzero r,B,S,U.
PASS temporal weights: 147 exact evaluations through degree six.
PASS finite raw mobilities/gradients/all three kernels/energy/GD simultaneity, n=d=2, m=3, duplicate inputs, unequal positive mobilities.
PASS given unequal-probability L2/HS chain rule, genuine adjoint, common-row cap dissipation, readout bound; finite-state diagnostic only.
```

There were no failed or excluded runs, no tuning after results, and no further computational branch. The supplied order-thirteen fixed certificate was regenerated only by the expressly requested supplied test suite.

**Integrity record**

All 11 supplied files matched the manifest before review and were unchanged after all reads and checks. The next table gives the common before/after SHA-256; byte and line counts also matched at both checks. The final directory inventory contains exactly `INPUTS.json` and the 11 supplied files.

| File | Bytes | Lines | Before = after SHA-256 |
|---|---:|---:|---|
| `code/NUMERICAL_CONTRACT.md` | 4890 | 91 | `3791adea2ec3a4713a265ab1aa2b00e9993b51a957415060bebc88fe2399de22` |
| `code/pde/__init__.py` | 611 | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/exact_calculus.py` | 10108 | 249 | `d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3` |
| `code/pde/finite_network.py` | 15525 | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 4464 | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tests/test_exact_calculus.py` | 10214 | 217 | `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242` |
| `docs/NOTATION.md` | 5110 | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | 8355 | 214 | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `docs/gaussian_dependencies.md` | 17119 | 346 | `e52365e7ed2afaf3d48272b913caf60e1aa59f55d846019527f84ae15592cf84` |
| `docs/given_space_caps.md` | 18663 | 417 | `cdda914e481b46d51366a5d80661cd192b0f319d6507bc8b29eba69d87f9f95d` |
| `docs/loss_pullback.md` | 16049 | 366 | `dccefe204d607ad778a09e9a2c98ced0fbcb50a75cba869c44df9d9f652108ea` |

The supplied manifest's SHA-256 at final verification was `a73ff4662dc7acc075afdb9aa353581f3f6caa6f5e37ea096ff6f9c078e76c1d`. Machine-readable verification records are `/tmp/pde_caps_pullback_B2_before.json` and `/tmp/pde_caps_pullback_B2_after.json`.

**Required repairs: none.** CLEAN applies to the supplied statements under their actual assumptions and to the audited code contracts. It does not certify the unproved exponential-tail premise, construct Gaussian action spaces, identify a finite-width GF/GD population limit, promote a formal coefficient calculation to an analytic trajectory, or supply an empirical learning claim.
