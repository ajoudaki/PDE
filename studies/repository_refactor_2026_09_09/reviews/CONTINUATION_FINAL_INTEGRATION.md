# Scientific integration review

**Verdict: CLEAN within the explicitly bounded integration scope below.** No required correction was found. This is an independent scientific assembly and implementation review of the supplied snapshot. It is additional to, and cannot replace, full individual theorem review. It is not a fresh whole-book proof certification.

## Evidence and isolation

Reviewed only /tmp/pde_continuation_integration_1: 27 scientific files, 29,482 lines, plus INPUTS.json. No checkout, studies, generated historical data, prior review, earlier verdict, other task, or external bibliography was consulted. No work was delegated. The two requested skills were read in full: /etc/codex/skills/solve-math-rigorously/SKILL.md and /etc/codex/skills/investigate-conjectures/SKILL.md. The latter's research-contract, evidence-ledger, adversarial-audit, and decisive-experiments references were also read in full. Proof-search orchestration was not applicable to this isolated integration review.

Before computation, all 27 manifest hashes, byte counts, and line counts matched. After computation they matched again; every scientific file's hash also matched the independently saved before list. INPUTS.json was unchanged. No file was added to the snapshot. All review outputs and logs are outside it.

- INPUTS.json SHA-256: 70df5be4bdd278814a1d9e5701699a57c9cd6457c43912392053c71c05cc7368.
- Canonically sorted 27-file SHA-256 list digest: c9773910d196c904095238e54b90a4037cd4ea38e2f69edd029169498ff99510.
- Saved lists: /tmp/pde_continuation_integration_hashes_before_1.txt and /tmp/pde_continuation_integration_hashes_after_1.txt. Their ordering differs; their entries are identical.

## Scientific integration findings

| Material | Checks and conclusion |
|---|---|
| Shared contract and reading guides | Stored hidden matrices act with no additional width factor; first inputs use division by square root of input dimension; readout division is by width; backward fields omit residuals. Raw block mobilities, simultaneous GD, and recomputation under raw interpolation agree between the finite chapter and core API. Guides distinguish optimization, identification, compact-time approximation, initialized geometry, hidden motion, absolute nonaffinity, and relative nonlinear strength. |
| Finite dynamics, entire chapter | Checked all gradient/kernel/energy factors, finite continuation and fixed-depth bounds. For QI/IQ, ordinary Euclidean isometries supply the scalar block factors and the IQ factor two. The orientation witness preserves spectrum, hidden feature and output while changing the kernel. QQ row/column balances and both differentiated RMS denominators, induced first-feature operator, signed balance drifts, and raw-lift restart argument agree with the formulas and API. All these reductions retain width and have fixed finite, one-sample scope. |
| Gaussian calculus Section 9, lines 3302–3668 | Checked the raw-metric linear coordinate conversion, full squared-loss sign and moving residual, finite noncommuting pullback words, binomial slot weights, complete temporal table, integral remainder, arbitrary-residual cubic contractions, and stationary/affine checks. The hybrid-path inclusion and convexity hypotheses suffice for the telescoping estimate. The displayed fixed-order coefficient cancellation is expressly separated from a uniform-in-update-count remainder or a neural width limit. |
| Gaussian calculus Section 10, lines 3669–4164 | Checked initialization and mobility conversion in primitive Gaussian coordinates; all three derivative-forest rewrites, normalization exponents, and nonnegative coefficient structure; Gaussian pairing/free-label counting and component factorization; fixed-order annealed limits; formal inversion and continuity of the finite negative witness. The strictly positive mobility interval is existential and does not include a proved canonical-metric Stieltjes conclusion. Checked the frozen-block comparison, conditional Gaussian moments, invariant-ray polynomial evaluation, factorial lower bound, and zero-radius deduction. The residual-clock construction, shrinking level times, discontinuous pointwise loss limit and common-target triangle contradiction apply to the prescribed positive Taylor family with the stated order of limits. They are not assertions about positive-time finite-network or population trajectories. |
| Gaussian dependencies | Fully checked Section 4 and Section 7.2, including the frozen-row reduction, limiting monomial recurrence, six rational moments, both witness routes, inverse-series algorithm and colored-forest key logic. Section 7.1 was also read in full to match the moving-jet API, its degree budget and physical-clock terms. The new square-activation formal result is not silently subjected to or derived from the differently normalized, bounded-slope fixed-program theorem. |
| Finite controls Section 12, lines 1745–2162 | Checked prescribed separable L2 spaces, genuine adjoint, Hilbert–Schmidt increments, activation bounds and curvewise loss chain rule. The joint first-row cap preserves a common nonnegative multiplier even when sample directions cancel. The temporary readout cap provides local Lipschitz construction, becomes inactive, and permits global energy continuation. Under the explicitly unproved exponential-tail premise, the reference-state truncation estimate has one cutoff factor, yielding the stated logarithmic modulus, Cauchy comparison and reached-state uniqueness. Strong field/kernel passage does not use compactness of an arbitrary bounded Hilbert ball. Gaussian action construction and finite-network GF/GD identification remain absent and are expressly identified as additional obligations. |
| Finite controls Section 13, lines 2163–2404 | Checked all four initial-matrix orientations, both trained rank memories, the transformed first equation and its Fubini term, and the converse reconstruction. The supplied-path derivative bounds, mesh count and normalized action error are consistent. Integration by parts gives the retained-memory estimates without convergence of the primitive derivative. The section correctly separates actual sampled queries from a causally valid conditioning transcript and separates integrated-response approximation from derivative/kernel convergence. Its tail and compactness counterexamples are norm-obstruction examples, not claims about canonical reached states. |
| Continuous depth Section 14, lines 1499–1878 | Checked dense residual forward/adjoint derivatives, all kernel factors, physical energy and finite continuation. Its input map deliberately has no input-dimension normalization, its stored readout is order one, its middle mobility is residual depth, and its full mean loss is explicitly stated. These differ openly from the scalar-particle benchmark. Ordered product orientation, grade recurrences, forcing insertions and factorial bounds are correct at supplied-trajectory scope. Recomputed backward sources have the separate propagated source defect; its coordinate multiplier need not be bounded uniformly in width. No dense joint width/depth/GD or autonomous compressed-flow conclusion is inferred. |
| Older chapter interfaces | Selectively checked the ranges listed below against the assembly descriptions. The one-input unshifted-arctan local/global split, fixed-depth shifted-arctan result, special-data restrictions, linear order-one-readout comparisons, scalar-particle assumptions, and initialization-only sequential depth conclusions remain separate. Their unread interior proofs are not certified by this review. |

The loss clocks are explicitly converted where they differ: prescribed-space Section 12 uses half-sum loss for three samples and factor 2/3 to convert its vector field to common mean-loss time; the mixed finite fitting model uses the unhalved two-sample sum; the scalar-particle result uses half mean loss; dense residual Section 14 uses full mean loss. No conversion turns transformed continuous coordinates into exact transformed Euler updates.

## Code and reproducibility

All supplied production, test and tool Python was read in full. Public imports and examples match actual APIs. The new finite reductions evaluate existing finite states and do not integrate or initialize a trajectory; both RMS normalizers are differentiated. Lax matrices retain orientation and size. Euler primitives emit exact rational combinatorial weights and do not evaluate neural derivatives or moments. Exact certificate generation derives its own coefficients rather than loading tables. The floating evaluators clearly retain ordinary float64 limitations; their narrower range contract is not replaced by an exact-arithmetic claim.

The supplied make check command passed under Python 3.10.12 and NumPy 1.26.4, matching requirements.txt:

- Library boundary/local-file-link check: **25 files passed**.
- Unit tests: **86 passed**, reported runtime 0.432 seconds.
- Log: /tmp/pde_continuation_integration_make_check_1.log.

Both new Python examples were extracted directly from the supplied code/README.md and executed unchanged in fresh namespaces:

- Finite quadratic and RMS reductions: passed; printed kernel blocks [0.0346 0.07703125 0.1140625] and [0.00843756 0.05290351 0.19226667].
- Exact Euler pullback words: both exact assertions passed.
- Environment/output log: /tmp/pde_continuation_integration_examples_1.log.

The tests include independent coordinate differentiation, loss/output directional checks, separate scalar polynomial Euler composition through degree six, direct rational witness multiplication, and permutation-determinant verification. Those checks support finite implementation correctness at their tested scope and do not validate a population limit or an increasing-order campaign.

No training run, high-order campaign, external-source audit, or exporter execution was performed. No exporter was supplied. All proof and code dependencies needed for the new material are supplied within the mathematical library; the implementation check and examples run without studies or data. The structural checker checks local file links and declared imports, not mathematical correctness or every Markdown anchor.

## Exact reading ledger

“Full” means all lines of that file were read. For selectively read chapters, each listed interval was read in full; all complementary body intervals were not read. Heading inventories were additionally inspected throughout every mathematical chapter, so an isolated heading inside a complementary interval may have been seen. Heading discovery is not counted as reading the corresponding proof.

| Fully read file | Lines |
|---|---:|
| Makefile | 1–9 |
| code/README.md | 1–394 |
| code/pde/__init__.py | 1–26 |
| code/pde/exact_calculus.py | 1–249 |
| code/pde/finite_jets.py | 1–176 |
| code/pde/finite_network.py | 1–363 |
| code/pde/finite_reductions.py | 1–251 |
| code/pde/gaussian_moments.py | 1–114 |
| code/tests/test_exact_calculus.py | 1–217 |
| code/tests/test_finite_jets.py | 1–296 |
| code/tests/test_finite_network.py | 1–297 |
| code/tests/test_finite_reductions.py | 1–239 |
| code/tests/test_gaussian_moments.py | 1–110 |
| code/tests/test_library_boundary.py | 1–58 |
| code/tests/test_numerical_contract.py | 1–202 |
| code/tools/check_library.py | 1–100 |
| docs/NOTATION.md | 1–98 |
| docs/README.md | 1–265 |
| docs/finite_dynamics.md | 1–654 |
| requirements.txt | 1–2 |

INPUTS.json was also fully read and verified.

| Selectively read chapter | Full body intervals read | Complementary body intervals unread |
|---|---|---|
| docs/gaussian_calculus.md | 1–357, 1746–2524, 3203–4164 | 358–1745, 2525–3202 |
| docs/finite_optimization_and_controls.md | 1–110, 198–260, 342–386, 650–687, 756–806, 966–1006, 1217–1354, 1636–1695, 1745–2404 | 111–197, 261–341, 387–649, 688–755, 807–965, 1007–1216, 1355–1635, 1696–1744 |
| docs/continuous_depth.md | 1–398, 1481–1878 | 399–1480 |
| docs/arctan_limits.md | 1–128, 690–904 | 129–689, 905–3117 |
| docs/global_nonlinear.md | 1–180, 1755–1796 | 181–1754 |
| docs/linear_dynamics.md | 1–150, 2602–2641 | 151–2601 |
| docs/special_data_limits.md | 1–133, 7936–8000, 9253–9362 | 134–7935, 8001–9252 |

Total full-body scientific lines read: **9,283 of 29,482**. The remainder was not subjected to a fresh proof review. The mandatory new ranges and exact Gaussian dependency ranges are included completely.

## Immutable scientific input hashes

| File | SHA-256 (before and after) |
|---|---|
| Makefile | 740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65 |
| code/README.md | 13de3198894b7fc436e85c0051eba2d10b52e06fbb3384ed4972642971a4d500 |
| code/pde/__init__.py | 65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3 |
| code/pde/exact_calculus.py | d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3 |
| code/pde/finite_jets.py | 1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2 |
| code/pde/finite_network.py | efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551 |
| code/pde/finite_reductions.py | b74b7da576e75749417dce2662e04c110f6028f09b724cfa1d295f1055c99225 |
| code/pde/gaussian_moments.py | 6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae |
| code/tests/test_exact_calculus.py | 58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242 |
| code/tests/test_finite_jets.py | 991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a |
| code/tests/test_finite_network.py | a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931 |
| code/tests/test_finite_reductions.py | bd0063b5d7865cdb9f9b13e7bbea9118379a9baf2cb28845989ffbdd77935a9e |
| code/tests/test_gaussian_moments.py | 9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea |
| code/tests/test_library_boundary.py | 375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a |
| code/tests/test_numerical_contract.py | c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92 |
| code/tools/check_library.py | 7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/README.md | 3d7dc6f3cec2881d83fb4b221e22a068e4796484a67d7e7b81dece81a01da2f6 |
| docs/arctan_limits.md | 19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead |
| docs/continuous_depth.md | f9685c32594f0dc4fc2d6a786b719dd49189bcc7b8d09bd13eed96015b2366bf |
| docs/finite_dynamics.md | bbf3a99af2f13f196410d456744af7e8a20ee0faf5b4fdfbf3418909268444aa |
| docs/finite_optimization_and_controls.md | e49c1e2c6e401dcec03c0046819c58abd463aa30a80779c3b23517f206398bc9 |
| docs/gaussian_calculus.md | 1f68acab1d9ce92db2e79f3339e52d8a1000b9d6288467f64ae2aa8ea7ae833d |
| docs/global_nonlinear.md | becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95 |
| docs/linear_dynamics.md | c1920b78c8788c6025776943944da4f4756717cb8250189e7e91ea81ee830090 |
| docs/special_data_limits.md | be4573af77f32d53913b1a50f0eb6e003f54bbf7571db95951d47ebc6c65719a |
| requirements.txt | c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2 |
