# Fresh isolated adversarial audit

**Verdict: CLEAN.** No required mathematical or implementation correction was found within the specified software contract and review scope. The supplied structural check and all 52 supplied tests pass. Seven additional independent diagnostic tests pass, covering the cases and comparisons recorded below. This is a bounded source audit with deterministic diagnostics, not a claim that testing proves correctness for every floating-point input.

Audit date: 2026-09-09. Audited root: `/tmp/pde-code-round4.XWUaF4`.

## 1. Isolation, scope, and preservation

The only supplied mathematical and implementation inputs inspected were `code/`, `docs/`, `Makefile`, and `requirements.txt` in this isolated root. No project checkout, Git history, previous review or finding, study, data directory, website, network service, agent, or outside mathematical reference was consulted. No packages were installed. The existing Python/NumPy runtime was used to execute the authorized checks.

Every original file has the same SHA-256 hash at the end of the diagnostic work as at the initial inventory. There were no original-file edits, and the final inventory of `code/` and `docs/` matches the initial inventory. Bytecode writing was disabled. The supplied structural tests create and dispose of their own temporary fixtures; these are not changes to the input snapshot.

The two added audit artifacts are this report and `audit_diagnostics.py`, both at the isolated root, outside the original input directories. The latter preserves the independently authored cases for reproduction. It does not modify the original inputs or access research material.

Mathematical review includes all of NOTATION and finite_dynamics, and Gaussian chapter sections 1–4. Gaussian chapter sections 5–6 were not substantively re-reviewed: the fixed-program limit proof is outside the requested software dependency. The complete Gaussian file was hashed and read by the existing automated structural/link check; its headings were inventoried to locate the section boundary. Neither operation is represented here as a mathematical review of the excluded proof.

## 2. Required and optional issues

### Required issues

**None found.** In particular, no discrepancy was found in raw forward normalization, residual-free backpropagation, ordinary loss gradients, block mobilities, the simultaneous GD update, any of the kernel blocks, exact rational moment multiplicities, or PSD rejection at singular/near-singular boundaries.

### Optional follow-up

Retain selected independent cases as ordinary regression tests: the separate scalar/complex-step derivative oracle, the exact latent-Gaussian polynomial expansion, and PSD comparisons against all principal minors. These add different failure detectors to the existing suite. This is a testing recommendation, not a discovered defect or a condition of the CLEAN verdict. No optional software correction is asserted without evidence.

## 3. Full read coverage and exact input hashes

All code, tests, the code README, NOTATION, finite_dynamics, Makefile and requirements were read completely. The substantive requested coverage totals **2,010 lines**; 252 of those are the Gaussian chapter's introduction and sections 1–4. Any truncated terminal passage was subsequently read again in a smaller range.

| Input file | Total lines | Substantive read coverage |
| --- | ---: | --- |
| `code/README.md` | 165 | 1–165, complete |
| `code/pde/__init__.py` | 26 | 1–26, complete |
| `code/pde/finite_network.py` | 363 | 1–363, complete |
| `code/pde/gaussian_moments.py` | 114 | 1–114, complete |
| `code/tests/test_finite_network.py` | 297 | 1–297, complete |
| `code/tests/test_gaussian_moments.py` | 110 | 1–110, complete |
| `code/tests/test_library_boundary.py` | 58 | 1–58, complete |
| `code/tests/test_numerical_contract.py` | 202 | 1–202, complete |
| `code/tools/check_library.py` | 100 | 1–100, complete |
| `docs/NOTATION.md` | 98 | 1–98, complete |
| `docs/finite_dynamics.md` | 214 | 1–214, complete |
| `docs/gaussian_calculus.md` | 1,808 | 1–252, introduction and sections 1–4; exclusions stated above |
| `Makefile` | 9 | 1–9, complete |
| `requirements.txt` | 2 | 1–2, complete |

Initial and final SHA-256 manifests agree exactly:

```text
0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6  code/tools/check_library.py
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
7e2db79e59de2b52ae3a13e3013cced1086096648ca3313ecefde4c17a36d6fc  docs/gaussian_calculus.md
740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt
```

Final independent harness: `audit_diagnostics.py`, 375 lines, SHA-256:

```text
7dc246fb8db4266be815805e9ba7c13d08a17e2a40816c5501e5918382f9e346
```

## 4. Mathematical and implementation contract

### Forward, backward, initialization, and data

The implementation stores one `(n,d)` matrix followed by `(n,n)` hidden matrices and a length-`n` readout. `initialize` uses a private explicitly seeded generator, with first-entry variance 1, hidden-entry variance `1/n`, and stored-readout variance `1/n²`, in the documented draw order. It does not touch the global RNG. Supplied tests check exact seeded draws and global-state preservation.

`_forward` (finite_network.py:202–214) computes `W1 @ X / sqrt(d)`, subsequent `Wl @ h`, and `readout @ hL / n`. There is no extra hidden width factor. `_backward` (227–238) starts from the stored readout and applies the actual transposes and activation derivatives. Consequently its output is `delta_l = n * partial f / partial z_l`, with no residual or `2/m` factor.

The data are used as given. No input Gram inversion, whitening, clipping, diagonalization, independent-sample assumption, or unit-diagonal assumption occurs. All equations hold for zero, duplicated, opposite, arbitrarily correlated and linearly dependent samples. Independent cases used a seven-column, rank-two input matrix with zero and unequal-norm columns, exact duplicates and opposites, and conflicting duplicate labels. These checks also exercise shifted nonlinear activations, where an odd-symmetry shortcut would be incorrect.

### Gradients, physical flow, and raw GD

Direct differentiation of the forward equations yields, for sample `a`,

```text
grad_W1 f_a = delta_1,a x_a^T / (n sqrt(d))
grad_Wl f_a = delta_l,a h_(l-1),a^T / n       (2 <= l <= L)
grad_readout f_a = h_L,a / n.
```

Multiplication by `2 r_a/m` and summation gives the raw contractions in `_loss_contractions` (276–285) and normalized gradients in `loss_gradients` (288–295). The separate readout contraction has the correct orientation and normalization.

`_physical_blocks` (298–307) cancels the endpoint mobility factor `n` against the gradient's `1/n`, leaving factors `1/sqrt(d)`, then `1/n` for each middle block, then 1 for the readout. With the common factor `-2 kappa_l/m`, these are exactly finite_dynamics equation (2). The middle-layer and endpoint conventions remain correct when `L=1`.

`gd_step` computes every contraction from the original state before constructing any returned weight (317–338). Its update is `theta + eta * velocity` in the raw parameters. It does not recompute the first block and then reuse it to update a later block, perform transformed-coordinate Euler, clip a step, or impose an unwarranted decrease condition. Zero step checks argument structure and returns independent arrays without invoking unused callbacks. Positive and zero-step ownership were both tested.

### Kernels and energy

The layer blocks in `kernel_blocks` (341–356) match

```text
K1_ab = kappa1 (x_a^T x_b/d) (delta_1,a^T delta_1,b/n)
Kl_ab = kappal (h_(l-1),a^T h_(l-1),b/n) (delta_l,a^T delta_l,b/n)
Kreadout_ab = kappa_readout (h_L,a^T h_L,b/n).
```

These are exactly the mobility-weighted output-Jacobian Gram matrices. Their mathematical PSD property holds for arbitrary data correlations, including singular sample Grams. Negative off-diagonal entries are valid and are retained. Float64 does not make an exactly PSD symbolic assertion about every computed matrix; numerical eigenvalue checks used a rounding tolerance.

The total kernel sums all `L+1` blocks. Residuals and `2/m` are absent from the kernel itself. The independent oracle verifies all three linked identities:

```text
f_dot = -(2/m) K r
loss_dot = -(4/m²) r^T K r
loss_dot = -sum_l ||velocity_l||² / mobility_l.
```

The finite-dynamics chapter's existence argument is also sound under its stated real C2 activation hypothesis. The finite loss is C2, so the vector field is locally Lipschitz. Nonnegative loss and the constant positive learning metric give the weighted energy bound; Cauchy–Schwarz then gives the square-root time modulus. At a putative finite endpoint this makes the finite-dimensional parameter path Cauchy and permits local extension. No bounded-activation hypothesis is needed for that argument, and it does not establish GD stability.

The width-uniform bounds in section 4 use the additional bounded-derivative and initial norm/loss assumptions actually stated. The forward and reverse RMS inductions, Frobenius-to-operator increment bound, Gaussian initialization scaling, and finite sphere-net union bound are consistent. These estimates do not identify a population trajectory or prove a width/depth-uniform training limit.

## 5. Float64 and ownership audit

The README explicitly limits its numerical claim: raw matrix products and raw derivative contractions remain float64 operations; arbitrary intermediate overflow/underflow and correct rounding are not guaranteed. The audit evaluates the stronger guarantees the implementation actually makes inside that boundary:

- Built-in tanh differentiation uses a decaying exponential instead of subtracting a rounded `tanh(z)^2` from 1. Arctangent branches on magnitude and uses reciprocal squares on the large branch, avoiding direct overflow in `z*z`. The supplied saturated-tanh and large-arctangent cases pass. Additional scalar probes retained subnormal derivatives at `tanh(370)` and `arctan(1e161)`.
- `_scaled_product` (31–54) combines the finite scalar/elementwise factors in mantissa/exponent form. Thus a representable physical block need not pass through a representable normalized loss gradient, and a GD result need not pass through a representable unscaled velocity. Its addend path aligns exponents before restoring magnitude, permitting cancellation with a large old weight. Zero factors receive an irrelevant-exponent correction. Existing cases and additional exact binary scale cases pass.
- Input-Gram normalization and both middle-block normalizers remain inside this combined scaling. Subnormal but representable raw Grams can therefore be recovered by a large mobility. Their prematurely normalized product is not required to be representable.
- Loss uses a scaled mean square. An independent two-sample example with residuals `(2^512, 0)` returns exactly `2^1023`, although directly squaring the first residual would overflow. Existing unrepresentable-loss and unrepresentable-total-kernel rejection tests pass.
- All returned public numerical results are checked through finite-array validation or scalar loss validation. The code does not promise a finite result for every finite input: an overflowing raw contraction is a documented failure mode.

Two deliberate out-of-guarantee cases were retained as boundary diagnostics. A first raw product `2^1023 * 4` raises `ValueError`; the later readout being zero does not make that raw product representable. With first-layer identity hidden value `2^-538`, its raw Gram square underflows to zero before a mobility `2^1023` is applied, so the computed readout kernel is zero although the exact real scaled answer is `2^-53`. This is explicitly within the documented raw-matrix-product limitation, not a newly discovered violation. The nearby raw square at hidden value `2^-537` is representable and the scaled kernel is preserved by the independent test.

`Parameters` intentionally may alias caller-owned float64 arrays. Freezing the dataclass does not freeze array contents, and the documentation says so. Evaluation revalidates parameters; the existing mutated-NaN case is rejected. Normal evaluation and GD do not mutate those arrays, inputs, labels or mobility arrays.

Each activation invocation receives a new input copy and its result is copied immediately (194–199). The independent ownership case combines read-only and strided inputs, overlapping parameter blocks, and a single shared scratch buffer used by both value and derivative callbacks across layers. Every public computation agrees with a pure callback version. Mutating retained callback inputs and the scratch buffer after return leaves returned results intact. All original arrays retain their contents. This checks the specified ownership contract; callbacks that mutate unrelated external calculation state remain excluded by the README.

## 6. Exact Gaussian mathematics and implementation

Gaussian chapter section 1 correctly conditions Gaussian rows on their sums. The mean of the reused transpose is the finite random response `a_n 1`, and its conditional covariance is `sigma_n² (I - 11^T/n)`. Replacing that response by an independent transpose or by its expectation at finite width would be wrong; neither substitution is made. The Gaussian integration by parts and the stated polynomial-growth moment and empirical-law arguments are consistent with the hypotheses.

Section 2's mean satisfies both constraints by `U^T Y = R^T V`. The homogeneous constraint space consists precisely of matrices `(I-P_U) A (I-P_V)`, and the displayed mean is orthogonal to it in the Frobenius pairing. Conditioning the isotropic finite Gaussian therefore gives the claimed projected residual law. The adaptive argument expressly requires queries determined from independent recorded roots and earlier answers; it does not permit unrecorded matrix observations. Dependent columns can be removed exactly; no limit through an unstable inverse is asserted here.

A separate flattened linear-constraint oracle checked 16 combinations of empty, one-column, two-column and full-rank forward/transpose query lists at width 4. The mean from the chapter agrees with the least-squares minimum-norm solution of the full observation system, and its covariance agrees with the orthogonal nullspace projector divided by 4. Section 1's response and covariance were checked separately. These are deterministic finite identities, not sampling evidence for an asymptotic theorem.

Section 3's differentiation identities have the correct coefficients: differentiating `<g,Hg>` contributes one `T[g,g,g]` and two `||Hg||²` terms, so the third directional derivative is `2 T[g,g,g] + 4 ||Hg||²`. The constant positive metric coordinate change is consistent, and the chapter correctly separates feature-direction derivatives from physical derivatives carrying an additional residual factor.

Section 4 establishes the exact moment recursion even for singular covariance by writing `X=A G` and integrating each independent Gaussian coordinate. Removing one leg of coordinate `i` and pairing with `j` contributes `(alpha_j - 1_(i=j)) Sigma_ij`. The code's decremented remainder, multiplicity, covariance entry and recursive degree reduction implement exactly that formula (gaussian_moments.py:93–109). It returns `Fraction` values, including the odd-degree zero and zero-degree one.

PSD validation is exact rational Schur elimination (23–43): a negative pivot fails; a zero pivot requires the remaining first row to vanish; a positive pivot reduces by its Schur complement. Symmetry is checked first. Completing the square proves equivalence at every step; no pivot tolerance or numerical eigenvalue decision is used. Shape, type, degree and PSD validation precede both constant and odd-moment shortcuts. Inputs are converted to immutable internal tuples without modifying the caller's sequences. Memoization is local to the call and cleared in `finally`, including exceptional exit.

The independent moment oracle does not use the covariance Wick recursion. It expands each monomial of `X=A Z` into powers of independent standard Gaussian latent coordinates, then integrates those powers with exact integer double factorials. All 705 rational comparisons pass, including negative correlation, zero coordinates, singular covariance, nontrivial fractions and dimensions three and four.

The independent PSD oracle uses exact determinants of every principal submatrix, computed by the Leibniz permutation formula. It checks all 729 symmetric 3-by-3 matrices with entries in `{-1,0,1}`, 18 permuted exact near-boundary cases at distance `10^-60`, and one indefinite matrix whose proper principal minors are positive. Of these 748 matrices, 36 are PSD and 712 are not. Checking each with zero, odd and even powers gives 2,244 API checks; every decision agrees. Thus a small leading-minor shortcut or validation bypass would have been detected in these cases.

## 7. Structural independence

All three implementation modules were read completely. Their dependencies are NumPy, ordinary standard-library modules, and the package's own relative imports. There are no runtime research/data reads, network calls, subprocess calls, installation steps, or fixed-program proof dependencies in the library. The public `pde` import includes NumPy through the finite-network API, as documented; the Gaussian implementation itself is standard-library-only.

The independent harness loaded the Gaussian source directly under an import guard rejecting NumPy or `pde` imports and evaluated an exact singular-covariance moment successfully. This supports the module-level independence claim without asserting that importing the public package avoids NumPy.

The supplied checker verifies the current local Markdown links, source symlinks, declared import roots and local import module paths without loading the implementation. It reports 12 checked source/doc files. Its five fixture tests pass. It is a structural checker, not a sandbox or a general proof that arbitrary future code cannot perform dynamic external access; the CLEAN conclusion about this snapshot also rests on the full source read.

## 8. Actual test evidence and reproduction

Observed environment:

```text
Python 3.10.12 (main, Jun 22 2026, 18:55:27) [GCC 11.4.0]
NumPy 1.26.4
pde loaded from /tmp/pde-code-round4.XWUaF4/code/pde/__init__.py
```

The NumPy version matches `requirements.txt`. Every command below ran with the isolated root as its working directory.

### Existing checks

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 make check
```

Observed output summary, exit status 0:

```text
python -B code/tools/check_library.py
Library boundary and local links checked: 12 files.
make test
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_*.py' -v
Ran 52 tests in 0.143s
OK
```

| Supplied test file | Test methods executed | Result |
| --- | ---: | --- |
| `test_finite_network.py` | 15 | All pass |
| `test_gaussian_moments.py` | 11 | All pass |
| `test_library_boundary.py` | 5 | All pass |
| `test_numerical_contract.py` | 21 | All pass |

### Independent diagnostics

```sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B audit_diagnostics.py
```

Final observed run, exit status 0:

```text
test_callback_buffers_readonly_inputs_and_aliases ... ok
test_exact_moments_by_independent_latent_expansion ... ok
test_exact_psd_against_all_principal_minors ... ok
test_finite_gaussian_conditioning_constraints ... ok
test_float64_binary_scale_extremes ... ok
test_gaussian_module_without_numpy_or_package_initialization ... ok
test_scalar_oracle_all_finite_dynamics ... ok
Ran 7 tests in 0.418s
OK
```

The finite oracle uses separate scalar loops for the network; it does not call the library's forward routine to construct expected derivatives. Complex steps of size `1e-30` give each output's derivative with respect to each raw parameter and each injected preactivation. The four `(width, hidden depth)` cases are `(1,1)`, `(2,4)`, `(3,5)`, and `(1,7)`, with input dimension 4, seven samples, layer-dependent arctangent/quadratic/tanh/identity activations and unequal positive mobilities. Tests compare all raw gradient and velocity blocks, the simultaneous GD result, every kernel block, and output/loss dissipation. They assert block PSD to tolerance and returned-weight independence.

Final harness counters:

| Diagnostic | Count |
| --- | ---: |
| Finite network cases | 4 |
| Parameter derivative directions | 89 |
| Preactivation derivative directions | 217 |
| Kernel blocks | 21 |
| Exact latent moment cases | 705 |
| PSD matrices, accepted / rejected | 36 / 712 |
| PSD API checks | 2,244 |
| Gaussian conditioning transcripts | 16 |
| Exact binary scale cases | 7 |
| Callback ownership API cases | 8 |
| Implementation modules inspected by the harness | 3 |

Selected maximum absolute discrepancies from the final run:

| Comparison | Maximum absolute discrepancy |
| --- | ---: |
| Forward output | `2.168404344971009e-19` |
| Backward delta | `5.551115123125783e-17` |
| Loss gradient | `1.3877787807814457e-17` |
| Physical flow | `6.938893903907228e-18` |
| Raw GD | `2.541098841762901e-21` |
| Individual kernel block | `3.469446951953614e-18` |
| Total kernel versus block sum | `0.0` |
| Loss | `1.1102230246251565e-16` |
| Output-flow identity | `1.734723475976807e-18` |
| Energy / loss directional identity | `8.673617379884035e-19` |
| Buffered callbacks versus pure callbacks | `0.0` |
| Two-sided conditioning mean | `4.440892098500626e-15` |
| Two-sided conditioning covariance | `1.3322676295501878e-15` |

The general numerical comparison tolerance is `rtol=3e-12`, `atol=3e-14`. Small values are therefore not certified to a uniform relative tolerance. Rational moments and PSD decisions use exact equality; binary scale cases use array/scalar equality. No Monte Carlo campaign, optimizer trajectory study, large parameter search, or installation was performed.

During authoring, the independent harness initially had an unmatched parenthesis, and its first proposed four-column conditioning fixture was singular despite the intended independent-column hypothesis. Both were corrected only in the new harness. These were diagnostic-authoring failures, not failures in the supplied implementation. The final seven-test run above uses the hashed 375-line harness. The supplied 52-test run passed without any original-file change.

## 9. Limits of the conclusion

The verdict concerns this exact immutable snapshot and its documented finite numerical API. Exact formulas were inspected algebraically; bounded diagnostics provide additional counterexample searches and implementation evidence. They do not establish correct rounding, eliminate the disclosed raw-contraction range limitations, enforce the mathematical correctness/C2 regularity of arbitrary user callbacks, or guarantee performance for large exact-moment degrees and dimensions. Python recursion and rational bit growth still limit the explicitly small-order moment API.

No conclusion is offered here about the excluded fixed-program Gaussian proof, a population or infinite-width limit, a scientific study, or another code revision. Within the requested boundary, no required issue remains.
