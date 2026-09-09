# Isolated finite-calculus integration audit

Audit date: 2026-09-09. Input root: `/tmp/pde-code-integration.G88LB0QB`.

**Verdict: CLEAN within the read and execution scope below. Required corrections: none identified.**

The finite-network implementation, moving physical-flow jets, rational Gaussian moments, forest keys, formal reversion and fixed rational certificate agree with their documented interfaces and the mathematical dependencies reviewed here. All **73 authorized supplied tests passed**, and all four runnable examples in `code/README.md` succeeded. This conclusion also rests on direct source-level reasoning, detailed below; passing tests alone was not treated as proof.

This is a code/API/reproduction/integration assessment of the specified snapshot. It is not a whole-book proof certificate, an audit of the unreviewed population theorems, or a certification of all possible float64 inputs.

## 1. Isolation, exclusions and input integrity

Evidence was confined to the named input snapshot, the permitted Python/NumPy runtime, and temporary audit/test outputs. No other project, studies, history, prior review, agent, external skill file, or internet source was consulted. No installation, build, export, training run, random experiment, new numerical search, or custom numerical experiment was performed. The only seeded draws executed were those already present in the supplied small tests and the guide's width-eight example.

No input file was edited. SHA-256 was recorded before execution and recomputed after the tests and guide examples. All 18 in-scope whole-file hashes matched. The initial symlink inventory found no symlinks in the snapshot. These checks establish the identity and stability of the reviewed bytes; they make no comparison to another checkout or to an alleged earlier mathematical version. File-copy permission-preservation warnings are not evidence of a mathematical change.

The report directory `/tmp/pde-integration-audit.qYsrLMlP` was independently created with `mktemp -d` under `/tmp`; its verified mode is `0700`, owned by the current user. It is outside the input snapshot. The boundary tests created and cleaned up their own small synthetic fixtures underneath this directory using `TMPDIR`.

The user's scope correction excluded **`code/tests/test_book_exporter.py` and the whole `code/tools/book_pdf/` subtree**. Before that correction, their names, line counts and initial file hashes had been collected as inventory metadata. Their contents were never inspected or displayed, and they were not imported, executed, or used as evidence for this verdict. No further reads of those files were made after the correction. Their incidental presence is an exclusion, not a defect.

`Makefile` was read as a nine-line ancillary file, but no Make target was executed. The guide's broad `unittest discover` command was not executed because it would include the excluded exporter test. The six authorized modules were explicitly enumerated instead. Likewise, `check_library.main()` was not run on the entire snapshot: its recursive scan would read the excluded exporter files and the unreviewed portions of the calculus chapter. Its implementation was read in full, its supplied synthetic-fixture tests were executed, and the actual in-scope imports and the links in the reviewed prose were assessed directly.

## 2. Exact read scope

All line numbers below are one-based and inclusive in the hashed snapshot. “Full” means every line was inspected, not only definitions, search hits, or test names.

| File | Read scope |
| --- | --- |
| `code/README.md` | Full, lines 1–271 |
| `code/pde/__init__.py` | Full, lines 1–26 |
| `code/pde/finite_network.py` | Full, lines 1–363 |
| `code/pde/finite_jets.py` | Full, lines 1–176 |
| `code/pde/gaussian_moments.py` | Full, lines 1–114 |
| `code/pde/exact_calculus.py` | Full, lines 1–191 |
| `code/tools/check_library.py` | Full, lines 1–100 |
| `code/tests/test_finite_network.py` | Full, lines 1–297 |
| `code/tests/test_finite_jets.py` | Full, lines 1–296 |
| `code/tests/test_gaussian_moments.py` | Full, lines 1–110 |
| `code/tests/test_exact_calculus.py` | Full, lines 1–122 |
| `code/tests/test_numerical_contract.py` | Full, lines 1–202 |
| `code/tests/test_library_boundary.py` | Full, lines 1–58 |
| `docs/NOTATION.md` | Full, lines 1–98 |
| `docs/finite_dynamics.md` | Full, lines 1–214 |
| `docs/gaussian_calculus.md` | Section 4 in full, lines 195–254; Section 7 in full, lines 1816–2431 |
| `Makefile` | Full, lines 1–9; read only |
| `requirements.txt` | Full, lines 1–2 |

Gaussian calculus lines **1–194 and 255–1815 were not substantively read or reaudited**. A heading-only inventory covered the chapter, and whole-file hashing covered its bytes; neither is a substantive review of those unread ranges. Section 4 supplies the Gaussian integration-by-parts/Wick recurrence, including singular covariance, and the exact Schur-complement validation proof used by this audit. Section 7's finite-flow, forest and certificate arguments were read in their entirety. Its references to other population results were not treated as dependencies that establish those other results. No additional Sections 1–6 proof dependency was needed for the bounded claims assessed here.

## 3. Execution and reproducibility

Observed environment:

- Python `3.10.12 (main, Jun 22 2026, 18:55:27) [GCC 11.4.0]`.
- NumPy `1.26.4`, matching `requirements.txt`.
- `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`.
- Python `-I -B`: isolated interpreter startup and no bytecode writes; only the input's `code/` and `code/tests/` directories were explicitly prepended for the tests.
- `TMPDIR=/tmp/pde-integration-audit.qYsrLMlP`.

Runtime diagnostics confirmed that `pde`, `pde.finite_jets`, and `pde.exact_calculus` loaded from this exact input root. Source inspection resolves the other relative package imports to the same root. No installed copy of `pde` was used as the implementation under test.

The effective test invocation was the following, preceded in the same interpreter by version and module-location printouts:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
TMPDIR=/tmp/pde-integration-audit.qYsrLMlP python -I -B -c '
import sys, unittest
sys.path[:0] = [
    "/tmp/pde-code-integration.G88LB0QB/code",
    "/tmp/pde-code-integration.G88LB0QB/code/tests",
]
unittest.main(module=None, argv=[
    "authorized-tests", "-v",
    "test_finite_network", "test_finite_jets",
    "test_gaussian_moments", "test_exact_calculus",
    "test_numerical_contract", "test_library_boundary",
])'
```

| Authorized module | Tests | Result |
| --- | ---: | --- |
| `test_finite_network` | 15 | PASS |
| `test_finite_jets` | 14 | PASS |
| `test_gaussian_moments` | 11 | PASS |
| `test_exact_calculus` | 7 | PASS |
| `test_numerical_contract` | 21 | PASS |
| `test_library_boundary` | 5 | PASS |
| Total | **73** | **PASS** |

The actual unittest summary was `Ran 73 tests in 0.241s`, followed by `OK`; process exit status was zero. No tests were skipped and no failures or errors were reported. This is one permitted-runtime run, not a cross-platform or cross-version test matrix.

### Guide examples

The executable bodies at README lines 97–106, 141–146, 179–189 and 253 were run with the same isolated Python/NumPy environment, explicitly adding only this snapshot's `code/` directory. The fixed certificate one-liner was executed as its equivalent Python statements. No example values, seeds, dimensions, activations or assertions were changed. Descriptive `text` fences are equations, not additional executable examples.

The finite-network example printed:

```text
[ 0.00585987 -0.00357566 -0.00585987]
[[ 0.08579212  0.05179866 -0.08579212]
 [ 0.05179866  0.0781826  -0.05179866]
 [-0.08579212 -0.05179866  0.08579212]]
0.7410221085761991 0.7398799811970899
```

Both exact Gaussian assertions passed: the values are `56/9` and `3`. The moving-flow example printed ordinary coefficients followed by physical derivatives:

```text
[0.23145472 0.62056291 0.26424555 0.17584787]
[0.23145472 0.62056291 0.5284911  1.05508723]
```

The exact certificate printed:

```text
-86245462994269879146938487857152/200150589172828762588730609071155193161975
-673792679642733430835456936384/329714727520793070279653295504327135
```

These agree with Section 7 equations (7.C10) and (7.C11). All example execution exited successfully. Rounded NumPy display values above are observations of this run, not exact-real values or a promise of identical last bits on every platform. The loss decrease in this example is not a general step-size theorem.

## 4. Finite-network API and proof normalization

Sources: [finite_network.py](/tmp/pde-code-integration.G88LB0QB/code/pde/finite_network.py:15), [notation contract](/tmp/pde-code-integration.G88LB0QB/docs/NOTATION.md:8), [finite dynamics](/tmp/pde-code-integration.G88LB0QB/docs/finite_dynamics.md:9), and [guide API](/tmp/pde-code-integration.G88LB0QB/code/README.md:39).

The shape and storage contract is implemented consistently: `(n,d)` first weights, equal-width `(n,n)` hidden matrices, `(n,)` readout, and `(d,m)` inputs with a nonempty batch. Any positive hidden depth is supported by the loops, including depth one with no middle blocks. Constructor conversion, evaluation-time validation, nonfinite rejection, label shape, activation sequence length, positive mobilities and nonnegative finite GD steps match the stated interface. The tests exercise depths one through three; the arbitrary-depth conclusion additionally follows from inspection of the uniform layer loops, rather than exhaustive testing at every depth.

The first preactivation is the raw product divided by `sqrt(d)`, each subsequent hidden action uses the stored matrix directly, and the output divides by `n`. There is no extra hidden `1/sqrt(n)`, Gram inversion, whitening or normalization of supplied samples. Initialization draws first weights at standard deviation one, hidden entries at `1/sqrt(n)`, then readout at `1/n`, exactly in that order from a locally seeded generator. Thus the stored-readout variance is `1/n²`, not `1/n`.

Direct differentiation gives residual-free `delta_l = n * partial f / partial z_l`. Multiplying its outer products by the loss derivative `2r/m` gives:

| Block | Loss gradient | Physical velocity after mobility |
| --- | --- | --- |
| First | `2/(mn sqrt(d)) sum_a r_a delta1_a x_a.T` | `-2 kappa1/(m sqrt(d)) sum_a r_a delta1_a x_a.T` |
| Hidden, `l >= 2` | `2/(mn) sum_a r_a delta_l,a h_(l-1),a.T` | `-2 kappa_l/(mn) sum_a r_a delta_l,a h_(l-1),a.T` |
| Readout | `2/(mn) sum_a r_a hL_a` | `-2 kappa_(L+1)/m sum_a r_a hL_a` |

These are the quantities assembled by `_loss_contractions`, `loss_gradients` and `_physical_blocks`; the endpoint factors cancel exactly as in the finite-dynamics proof. `gd_step` obtains every raw contraction from the original state before constructing any updated block. It is simultaneous raw GD, with the documented lack of an arbitrary-step loss-decrease guarantee.

For each sample pair, the first kernel block is `kappa1 * (x_a.T x_b/d) * (delta1_a.T delta1_b/n)`, a middle block is `kappa_l * (h_a.T h_b/n) * (delta_a.T delta_b/n)`, and the last block is `kappa_last * hL_a.T hL_b/n`. Those factors and signs match `kernel_blocks`. They contain neither residuals nor `2/m`. Consequently the real-arithmetic identities are `f_dot = -2Kr/m` and `loss_dot = -4 r.T K r/m² = -sum ||velocity_block||² / mobility_block`. The numeric Jacobian and dissipation tests check these identities through separate differentiation routes.

I also inspected the full finite-dynamics existence and norm arguments. The weighted energy identity bounds increments by `sqrt((t-s) loss(0))`; positive fixed finite-dimensional mobilities give a finite endpoint limit and local continuation, proving the stated global finite-width forward flow result. Bounded activation derivatives then close the stated forward/backward RMS induction on fixed horizons. The initialization argument uses fixed-depth Gaussian moment bounds and the explicit sphere-net tail bound. These statements have the specified hypotheses and do not assert GD stability, depth-uniform estimates, or population identification.

## 5. Moving physical-flow jets

Sources: [finite_jets.py](/tmp/pde-code-integration.G88LB0QB/code/pde/finite_jets.py:26) and [Section 7.1](/tmp/pde-code-integration.G88LB0QB/docs/gaussian_calculus.md:1818).

The implementation enforces exactly two hidden layers, one sample, one shared activation derivative callback, orders zero through three, and three positive mobility multipliers. It uses the existing raw `Parameters` storage. The narrow contract is stated prominently in both the guide and module; it is not advertised as arbitrary-depth or arbitrary-order differentiation.

The recurrence matches (J4)–(J8) term by term:

- `_convolve` includes every split of the requested ordinary coefficient under a bilinear product.
- `_compose` uses `phi' z2 + phi'' z1²/2` at degree two and `phi' z3 + phi'' z1 z2 + phi''' z1³/6` at degree three.
- The second forward action convolves the moving middle matrix with the moving first hidden field. The reverse action explicitly uses each moving middle coefficient's transpose; it does not substitute a fixed or independent matrix.
- Residual coefficients subtract the label only at degree zero. Their positive degrees enter all subsequent physical updates.
- Each next parameter coefficient divides its physical RHS coefficient by `k+1`, with first/middle/readout normalizers `1/sqrt(d)`, `1/n`, and `1` respectively.

The dependency order is triangular: weights through degree `k` determine the degree-`k` forward fields, then backward fields, then weights at `k+1`. The terminal forward degree stops before any unused backward or residual computation. For order three, the RHS needs only degree two, so the callback is requested only through derivative three. Order zero validates all argument structure and computes only values.

The mathematical regularity statement is sufficient: a C3 activation makes the physical vector field C2, yielding a local C3 parameter solution and C3 forward fields. This justifies the finite Taylor coefficients with a little-o remainder, without assuming a fourth derivative or an analytic expansion. The documented lack of an `O(t^(R+1))`, width-uniform or positive-time approximation theorem is appropriate.

The physical/feature clock calculation also checks. With `b=-2r(0)` and feature derivative notation, `s''=-2bF'` and `s'''=-2b²F''+4b(F')²`; substitution gives `f'''=b³F'''-8b²F'F''+4b(F')³`, agreeing with (J11). The moving residual in the implementation supplies these terms. The special input factor `G11=x.T x/d` in first-preactivation feature dynamics is consistent with the raw first matrix; it is not an extra tunable mobility.

Returned shapes, factorial conversion, derivative request prefixes and ownership match the guide. Inputs, labels and rates are copied for this computation; initial parameter coefficients are copied into new storage. Callback inputs and immediate returned values are also copied. Mutable result arrays are not a promise that stored fields will automatically recompute if the user later edits a returned coefficient.

## 6. Independent derivative oracles: precise labels

The following distinctions are material to the verdict. None of these finite checks alone establishes an infinite-width theorem or certified floating error bound.

| Supplied check | What is independently checked | What it shares or does not establish |
| --- | --- | --- |
| Loss coordinate differences, `test_finite_network.py:96` | Every coordinate of every raw gradient block at the supplied depths | Uses the production scalar loss/forward evaluator, not a separate implementation of the predictor |
| Output coordinate differences, `test_finite_network.py:110` | Each mobility-weighted kernel block against `J.T D J` | Uses production forward values; it does not reuse the analytic kernel or analytic gradient to form its reference |
| Directional loss/output differences, `test_finite_network.py:132` | The connection between the physical RHS, kernel and weighted dissipation | Uses the existing production forward/loss and RHS; first directional derivatives need only the initial velocity |
| Linear, cubic and constant-flow solutions, `test_finite_jets.py:74` | Closed-form moving trajectories and their ordinary coefficients | Small special cases, not coverage of every activation or state |
| Parameter acceleration and jerk, `test_finite_jets.py:117` | `theta''=V'V` and `theta'''=V''[V,V]+V'(V'V)` from differences of the existing physical RHS | Independent of the jet propagation recurrence, but shares the existing RHS, basic helpers and activation functions; finite-difference tolerances apply |
| Forward fields along a parameter polynomial, `test_finite_jets.py:136` | Composition of forward fields with the returned parameter polynomial | **A composition/consistency check**, not an independent oracle for that polynomial's physical dynamics |
| First-order jet/RHS/kernel comparisons, `test_finite_jets.py:53` | Integration and normalization of the two APIs | Shared finite-network identities; not by itself a third-derivative oracle |

The hand-solvable tests have substantive discriminatory value: the linear equal-weight case gives `f(t)=(1+8t)^(-3/4)` with coefficients `[1,-6,42,-308]`, while a frozen initial parameter direction gives a degree-two coefficient of `12`. The cubic example uses unequal mobilities to preserve equal weights and exercises all activation derivatives through order three. The constant-activation case has an exponentially changing residual, so it detects omission of the physical clock terms.

The guide's actual wording, “independent derivative checks against the existing physical RHS,” is supported by this appropriately limited meaning of independence. It does not label the forward-field polynomial check as an independently generated flow trajectory. No correction to the oracle descriptions is required.

## 7. Floating range, validation and ownership

Sources: [finite arithmetic helpers](/tmp/pde-code-integration.G88LB0QB/code/pde/finite_network.py:31), [numerical-contract tests](/tmp/pde-code-integration.G88LB0QB/code/tests/test_numerical_contract.py:13), and [Section 7 numerical contract](/tmp/pde-code-integration.G88LB0QB/docs/gaussian_calculus.md:2107).

The documented improvements are present: tanh derivatives use an exponential expression instead of subtracting a rounded squared tanh from one; arctan derivatives use a reciprocal branch beyond absolute value one; mean square evaluation scales residuals; and `_scaled_product` combines finite factors via mantissas and exponents before restoring magnitude. GD includes its step directly in that product and can combine an increment with the stored weight before restoring a common exponent. Thus neither flow nor GD requires a separately representable normalized loss gradient, and GD need not first produce a representable standalone velocity. The supplied extreme-range tests exercise these particular properties, including subnormal raw contractions and cancellation with an otherwise unrepresentable increment.

The guarantee is deliberately bounded. Raw matrix products, elementwise residual/backward contractions, Gram products, convolution sums and composition powers still operate in float64. They can overflow before later normalization or underflow before a large mobility could restore a result. Already lost information is not recovered by `_scaled_product`. Built-in activation derivatives can themselves underflow outside representable range. Summation/cancellation and final subnormal rounding remain ordinary floating-point behavior. A real-arithmetic result can be representable even when an intermediate computation is not; the package does not promise success in every such case.

Detected nonfinite evaluated quantities are rejected through validation; underflow to a finite zero is not diagnosed as an error. Kernel positive semidefiniteness is a real-arithmetic statement and is not enforced by a numerical projection. Loss and total kernel overflow are rejected rather than silently returned as infinity. Requested output derivative factorial conversion is separately validated. The guide and Section 7 expressly disclose these limits, so their presence does not contradict a broader claimed range guarantee.

Callbacks receive private copies and have their results copied immediately, including when they reuse buffers. The ordinary `Parameters` constructor intentionally can share float64 storage with caller arrays, and evaluation revalidates the mutable state; the guide says so. Updates return new arrays. A zero GD step returns independent copies after structural argument validation without calling activation functions. Semantic correctness of derivative callbacks, coordinatewise behavior and C2/C3 regularity remain caller responsibilities; shape validation is not presented as certifying them.

## 8. Exact Gaussian moments and forest logic

Sources: [gaussian_moments.py](/tmp/pde-code-integration.G88LB0QB/code/pde/gaussian_moments.py:23), [Section 4](/tmp/pde-code-integration.G88LB0QB/docs/gaussian_calculus.md:195), [forest implementation](/tmp/pde-code-integration.G88LB0QB/code/pde/exact_calculus.py:88), and [forest proof](/tmp/pde-code-integration.G88LB0QB/docs/gaussian_calculus.md:2157).

The moment implementation selects an occupied coordinate, removes one leg, and pairs that leg with each remaining coordinate with its remaining multiplicity and covariance entry. Each recursive term lowers total degree by two. Zero total degree gives one and odd total degree gives zero, only after all validation. Exact Schur complements handle a positive pivot, while a zero pivot requires a zero remaining row; negative pivots and asymmetric matrices are rejected. This is the singular-covariance integration-by-parts recurrence and PSD argument in Section 4, with no approximate tolerance or illicit inverse at a zero pivot.

Fractions remain exact throughout. Inputs are not mutated. The recursive cache is local and cleared in `finally`; there is no retained cross-call coefficient table. The finite rational operation/state bounds do not bound rational bit size, recursion overhead or practical feasible degree. The small-order positioning is appropriate; the tests use explicit closed forms, singular/zero cases and exact near-boundary invalid covariances, not a sampling estimate of a moment.

For `forest_key`, union/find rejects precisely the edge additions that connect vertices already in the same component, covering duplicates and cycles after color/index validation. Rooted keys preserve the root color and sorted multiset of child keys. Induction gives equality exactly for rooted color-preserving isomorphism; taking the minimum over all roots gives the unrooted equivalence; sorting components preserves their multiplicities. This proves the intended invariant beyond the tested five-vertex relabelings. It is not an evaluator of arbitrary forest coefficients.

I also checked the separate leading expectation factorization argument. For `e=2p` Gaussian edge factors, a pairing quotient with `v` vertices and `c` components satisfies `v<=p+c` and `c<=r`. After normalization by `n^(-p-r)`, only `v=p+r` can survive. Pairings joining original components have fewer than `r` quotient components and vanish at leading order. The remaining componentwise pairings and decoration factors multiply; extra label coincidences lose at least one free label. Fixed graph sizes and finite Gaussian decoration moments justify the error counting. Odd-edge components and isolated vertices are handled by the same reasoning. This proves the stated expectation factorization, not concentration, a trained-coordinate independence claim, or an unimplemented compiler.

## 9. Exact certificate versus its probability interpretation

Sources: [certificate implementation](/tmp/pde-code-integration.G88LB0QB/code/pde/exact_calculus.py:143), [Section 7.2 certificate proof](/tmp/pde-code-integration.G88LB0QB/docs/gaussian_calculus.md:2240), and [exact certificate tests](/tmp/pde-code-integration.G88LB0QB/code/tests/test_exact_calculus.py:93).

There are three distinct models/objects here:

| Object | Initialization/state and clock | Scope |
| --- | --- | --- |
| Finite-network API | Arbitrary finite state; supplied initializer has stored-readout variance `1/n²`; positive mobilities; physical loss flow/GD | General finite depth and batch |
| Moving jet API | Arbitrary supplied finite state; positive mobilities; physical loss-flow coefficients | Two hidden layers, one sample, orders 0–3 |
| Fixed quadratic certificate | Order-one standard-normal stored readout; frozen first block; feature ascent | Exact formal initialization-derivative coefficients and a particular moment obstruction |

The last object is separately specified. It does not need zero mobility to be accepted by the positive-mobility numerical APIs, and its order-thirteen formal calculation is not a claim that `flow_jet` supports order thirteen.

**Probability argument.** For the certificate, `q_n = mean(u_j^4)` is constant along the frozen-first-block feature flow. Conditional on the first-layer variables, the initial `(a_i,z_i)` are independent with law `N(0,1) x N(0,q_n)`. The reduced feature derivative operator is `D_q = z² partial_a + 2qaz partial_z`. Substituting `z=sqrt(q) xi` gives a factor `q` in this operator and in `az²`, so the conditional expectation of derivative order `k` is `c_k q_n^(k+1)`. The displayed variance and moment bounds imply convergence of each required expectation to its value at `q=3`.

Thus (7.C1)–(7.C5) justify **limits of expectations of each fixed-order initialization derivative** (the stated annealed interpretation). This argument is logically separate from running exact arithmetic. It is not evidence for convergence of whole trajectories, interchange of an infinite Taylor series with a width limit, or a positive-time population solution. Those stronger conclusions are not needed or claimed here.

**Algebraic regeneration.** The implementation begins with the single polynomial `az²`, applies `D = z² partial_a + 6az partial_z` in sparse monomial form, and evaluates independent Gaussian moments with variances one and three. It generates derivatives zero through thirteen from that recurrence; the large displayed derivative integers are not embedded in production code. In particular `D(az²)=z^4+12a²z²`, giving `d1=27+36=63`, and parity forces every even derivative to vanish.

Dividing by factorials gives ordinary coefficients of the formal `F`. `revert_series` determines each inverse coefficient because its only new linear contribution is `a1*b_k`; production Horner composition computes the remaining known coefficient. The inverse has the same truncation length. Differentiation and composition give `K=F'(F^(-1))` through degree twelve, enough for all six `mu_j=(-1)^j [y^(2j+2)]K`. These are formal-series coefficients whose proposed moment interpretation is being tested, not automatically Gaussian moments or probabilities. Rational elimination tracks row-swap signs and exact pivots, including singular matrices and the empty determinant.

The returned witness solves the leading two-by-two shifted system, whose positive determinant is explicitly checked. The negative shifted determinant and negative witness value reproduced above agree with the chapter. For any nonnegative measure on `[0,infinity)` representing these six moments, the witness sum would equal `integral lambda * p(lambda)^2 dnu >= 0`, contradicting its exact negative value. This is the correct moment obstruction; it is not a contradiction to the existence of the underlying Gaussian initialization.

**Independence of arithmetic checks.** Tests verify all displayed derivatives, six moments and witness fractions. A Leibniz-permutation determinant independently checks the elimination result. Separate schoolbook-power composition checks both directions of reversion on supplied small series, rather than reusing production Horner composition. A direct quadratic-form calculation from the displayed witness checks the negative value. The high-order derivative reference list is a set of expected constants, not a second independently implemented high-order derivative compiler; source-level verification of the monomial recurrence and the probability derivation supplies the additional reasoning. The guide does not promise such a second compiler.

The rejection applies to a representation required uniformly over metrics including this **zero first-block mobility** model. It does not establish the same rejection for strictly positive first mobility, resolve the canonical unit-metric all-order problem, or refute a positive-time feature-learning limit. README lines 264–271 and Section 7 lines 2380–2387 state these restrictions. No correction of that claim boundary is needed.

## 10. Imports, boundary checker and integration

Sources: [package exports](/tmp/pde-code-integration.G88LB0QB/code/pde/__init__.py:1) and [boundary checker](/tmp/pde-code-integration.G88LB0QB/code/tools/check_library.py:24).

The package implementation imports only NumPy, the standard library and explicitly present sibling modules. `finite_jets` uses a small set of private finite-network helpers inside this same package; this is visible internal coupling and has been checked against their current definitions. Exact calculus uses only the standard library in its own source. Gaussian moments likewise uses only the standard library in its module, while importing through the public `pde` package also initializes its NumPy finite-network API, exactly as the README explains.

Top-level exports match the guide. `flow_jet` and the exact-calculus functions are intentionally imported from their submodules. There is no advertised packaging/install command that is needed for the guide; adding the snapshot's `code/` directory is sufficient and was reproduced. No model weights, retained coefficient arrays, generated data, historical artifacts or other local project files are opened by these APIs. Only the explicitly seeded initializer draws weights.

The six authorized tests depend only on the same package, NumPy and standard-library helpers. The boundary tests load the checker by a path resolved inside this snapshot and create synthetic local fixtures. No excluded exporter module is imported transitively by them.

The checker parses ordinary Python imports and Markdown links after removing code/math lookalikes; it rejects the tested missing modules, undeclared packages, broken links and symlinks. It calls itself a structural check, correctly. It is not a general dynamic-import or security verifier, nor a mathematics verifier. Inspection found no dynamic-import escape or external local dependency in the target package. The relative file links in the fully reviewed guide/notation/finite-dynamics material resolve inside the supplied `docs/` and `code/` boundary. A full-tree checker result is deliberately **not claimed**, for the exclusion reasons in Section 1.

## 11. Required corrections and residual limits

**Required corrections: none identified.** No in-scope failing test, broken guide example, inconsistent public interface, wrong normalization, false independent-oracle label, illicit probability inference, or missing external local implementation dependency was found.

The following are scope limits, not unresolved required corrections:

- Gaussian calculus outside Sections 4 and 7, and all exporter content, remain substantively unread and unreviewed.
- Finite-difference references have truncation/roundoff error and share the existing forward/RHS evaluator as described; they are not formal verification.
- Tests cover small supplied cases on Python 3.10.12 / NumPy 1.26.4, not every parameter, degree, platform or runtime version.
- Extreme float64 intermediate overflow/underflow, derivative callback semantics, recursion limits and growing exact rational cost retain the documented restrictions.
- No concentration, all-order moment representation, whole-book population theorem, or positive-time identification conclusion is inferred from the finite arithmetic checks.

These limits define the CLEAN verdict rather than expanding it beyond the requested integration audit.

## 12. SHA-256 manifest

Paths are relative to `/tmp/pde-code-integration.G88LB0QB`. Each whole-file digest below matched both the initial and post-execution checks. For the partially read calculus chapter, a whole-file digest identifies the snapshot; it does not imply that the whole chapter was substantively reviewed. Excluded exporter digests are intentionally omitted from this report's evidence manifest.

```text
740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt
b563a8a4fcebbb5fb634057f6cf09d32475462670002c8fbad0502f5c06482e0  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2  code/pde/finite_jets.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
482a45deb3e5fb721acdd0ae97654f9f5db57da145e0902d9ff1b24f01c8fc41  code/pde/exact_calculus.py
7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6  code/tools/check_library.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a  code/tests/test_finite_jets.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
b4a7f5795def064e53b2e7a849637d29dcaa0bad403e8e8ff893863b8468a439  code/tests/test_exact_calculus.py
c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
8bfcc0250b744e779f1be702ee62f55e43e56bde9f9d6fdc9a631861d5eef1f0  docs/gaussian_calculus.md
```

For exact identification of the substantively read calculus extracts, these additional SHA-256 values were calculated over the original line bytes, including their line endings, using `sed -n '195,254p'` and `sed -n '1816,2431p'` respectively:

```text
e3ae87e118aa93a8cd58f21869dfd678cdaecc7d9b1efb27942c47bc7b2cca7d  docs/gaussian_calculus.md lines 195–254 (Section 4)
da526195a3d3d256486f455ce1a6147c886aa8cc3b4b316b786facbb7c0e188e  docs/gaussian_calculus.md lines 1816–2431 (Section 7)
```
