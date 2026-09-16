# Independent scientific promotion review A1 — frozen_v2

Reviewer: `/root/review_a1`. Date: 2026-09-16. Assignment: complete isolated scientific/code review of the general-dimensional p=1 initialized coefficients, finite closure, Torch comparator and comparison methods.

**Disposition: corrections required; this frozen candidate is not ready for promotion.** The initialized coefficient calculation, finite equations, sign folding and network comparator survived the checks below. A reproducible bug violates the comparison API's stated constant-vector correlation semantics (L1). A precise claim of equality with the existing dictionary implementation lacks the narrowly needed frozen definition/source (L2). Both are localized; neither invalidates the independently defined coefficient identities or the finite dynamics. Under Part 2, necessary corrections require a new frozen candidate and two fresh complete reviews.

This is the original full A1 report. It is not an author validation, selector decision, integration review, venue-scored paper review or user approval.

## 1. Input identity, isolation and read coverage

The controlling manifest is:

`studies/first_order_dimension_mnist/PROMOTION_MANIFEST.json`

SHA256: `395ac0e660eadaca2bb9972a55e2f8dc8627ad60796a13db3458dd449b30660d`.

All scientific content and execution imports came from:

`/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v2`.

Every listed frozen input was hashed against the manifest, with all hashes matching. Hashes were checked again after execution. Exact per-file hashes and read flags are in [input_hashes.json](../../data/generated/first_order_dimension_mnist/review_a1_v2/input_hashes.json), with a human-readable appendix below. Hashing a file is distinguished from reading its content.

I read every line of:

- The assignment and manifest; the complete frozen theory and new implementation guide.
- All four proposed library modules, the complete new tests, producer and analyzer.
- The three unchanged runtime dependencies: `finite_network.py`, `gaussian_moments.py`, and `pde/__init__.py`.
- Full `docs/NOTATION.md`, `docs/README.md`, and `code/README.md`.
- The complete original docs and code guides: these are byte-for-byte full prefixes of the corresponding proposed guides, verified by full-file comparison. Reading the complete proposed guides therefore covered every line of both original guides, plus the two four-line additions. Their body was not treated as a mandate to reprove the whole book.
- The complete `dependencies/global_nonlinear_source_units.md`: Section 2, Section 3 including the singular-Gram argument, H3.1, H3.N1 and H3.N2. No proof-dependency body in that supplied file was omitted.
- The frozen assembly script, statically only.
- The complete shared instructions/workflow, the required mathematical skill, the paper-review skill and severity rubric, and the supplied investigation skill plus its adversarial-audit and bounded-experiment references.

Two early combined tool outputs were truncated. I repaired them by complete separate reads of NOTATION, the source-dependency file, and GENERAL_P1. The long guides were read in consecutive, nonoverlapping ranges covering their entire contents. The appendix records their precise line counts.

Unread complement:

- `PROMOTION_PLACEMENT.md` was hash-checked only: its selector conclusions were intentionally excluded.
- Skill agent descriptors and the unused research-contract, evidence-ledger and multi-route proof-search references were hash-checked only. This assignment involved an isolated review, not restoring author research state or a new proof-search program.
- Study README/history, author checks, selector findings, other reviewer findings, other studies, old numerical outputs, the manifest's assembled-edition directory and the remainder of the established book/code were not read.
- No unavailable dictionary/decoder material was silently imported. L2 records the exact remaining source limitation.
- No external paper or online source was used. The scientific dependencies needed for the self-contained identities are in the supplied packet; external contextual links in the old guides were not invoked as proof premises.

I was newly assigned in a fresh isolated context, distinct from the named authors, assembler and selector. I did not receive another reviewer's results. I sent preliminary findings to the supervisor; the only subsequent instruction was to finish and retain this review without changing the packet. There was no scientific delegation or imported review opinion.

Writes were confined to this report and fresh scratch:

`data/generated/first_order_dimension_mnist/review_a1_v2/`.

The shared checkout was neither copied nor reset; no frozen/live source was edited and no Git staging or commit was performed. Metadata-only Git checks found HEAD `04b61a12795734cbfc93830bf0a164bab7d101c4`, an empty index, and unrelated unstaged work, which was preserved. Current shared instruction hashes matched the frozen instructions.

## 2. Scientific object and claim boundaries

The reviewed object is a bias-free two-hidden tanh network, with stored initialization variances \((1,1/n,1/n^2)\), inputs \(u=x/\sqrt d\), output \(c^T h_2/n\), unhalved weighted squared loss and physical mobilities \((n,1,n)\). Closure order p=1, population quadrature count P, neural width n, dimension d and sample count m remain separate.

The candidate supplies exact expectation identities for its explicitly retained initialized features, an explicit finite vector field and numerical implementations. It does not claim that a fixed p=1 system converges to a trained general-d neural network, that this basis is rotation invariant, that the finite example estimates MNIST/PCA performance, or that its operation timings prove a speed advantage. The documentation preserves these distinctions.

The review used the requested promotion format. The claim ledger, code audit and evidence log are consolidated here in the single assigned report, rather than writing unassigned report files. The material was supplied as repository-owned candidate work; no confidential venue submission or venue score was involved.

## 3. Claim ledger and independent mathematical audit

### C1. Joint initialized coordinates, raw contraction and normalization

**Assessment: sound for the explicitly defined features; implementation corroborated. Exact dictionary provenance remains limited by L2.**

The fixed program consists of Gaussian roots, linear maps and tanh maps with bounded first derivatives. There are finitely many calls at each fixed positive d, so the finite-program hypotheses of the supplied Section 3 apply. The argument invokes neither a growing query count nor a trained-time program. Section 2 supplies the finite Gaussian norm and convergence tools used in that proof. The small-readout scaling is consistent with the zero limiting closure readout and the retained random finite comparator readout.

I independently reconstructed the reused action. With \(h_i=\tanh G_i\), the forward sources have covariance \(vI_d\); the upper \(H_i\) have covariance \(\tau I_d\) and expected source derivative \(\alpha I_d\). The reverse law is therefore
\[
R_i=\sqrt\tau Z_i+\alpha h_i,
\]
jointly with the same \(G_i\). The response is not removable. Independence holds between coordinate pairs and the separate upper population, not between \(G_i\) and its reverse coordinate. The three independent SeedSequence children in the producer preserve precisely this distinction.

For retained lower \(F\) and upper \(B\), the supplied source rule gives
\[
E[B A_0F]=\sum_i E[Fh_i]E[\partial_{\Xi_i}B]
 +\sum_i E[\partial_{\zeta_i}F]E[BH_i].
\]
The centered forward-source regression residual is independent of the upper Gaussian coordinates and has zero pairing with B. This statement discards that residual only inside this expectation. It does not replace an entire joint action law. Gaussian integration by parts applies to the bounded tanh expressions and bounded derivatives.

For \(B=H_j,F=h_i\), the two terms are \(\alpha v\delta_{ij}\) and zero. For \(F=k_i=\tanh R_i\), they are \(\alpha\beta\delta_{ij}\) and \(\tau\gamma\delta_{ij}\). The constant bands vanish. This independently verifies the raw contraction, including the response contribution \(\tau\gamma\). Simultaneous sign negation and independent coordinate pairs give the stated uncentered Grams.

Positivity is valid: \(v,\tau,s>0\) by the nondegenerate normal/conditional-normal laws, and \(\beta^2\le vs\). Thus
\[
b^2=s+\eta-\beta^2/(v+\eta)
\ge \eta+s\eta/(v+\eta)>0.
\]
The lower Cholesky inverse maps the k coordinate to
\((k-\beta h/(v+\eta))/b\). Right multiplication by \(L_1^{-T}\) is necessary. In its k band the raw numerator becomes
\[
\alpha\beta+\tau\gamma
 -\alpha v\beta/(v+\eta)
=\alpha\beta\eta/(v+\eta)+\tau\gamma.
\]
This gives exactly the candidate's D; it is not an empirical off-diagonal deletion.

The tests independently reconstruct dense Cholesky factors for d=1,2,7,17 and compare all normalized arrays and D. I additionally used a different scalar quadrature family: 240-node Gauss-Hermite on the full Gaussian law. Its eleven constants differed from the production Gauss-Legendre values by at most \(5.56\times10^{-16}\). This is a strong ordinary-precision check, not a quadrature error certificate. The documentation correctly separates finite cutoff, quadrature refinement and population sampling.

The exact identities are a straightforward specialization of the provided finite source calculus. No broader literature novelty or priority claim was assessed.

### C2. Finite sign folding and signed observations

**Assessment: sound in the stated invariant state class; CPU and CUDA tests pass.**

The relevant symmetry negates the full lower joint mark and its moving w, and separately negates the upper mark and its moving c. Initial c=0 is compatible with this parity. In the unfolded representation, the constant feature exists but M's constant row and column vanish.

At a parity-preserving state, h1 is odd on lower pairs and a's constant coordinate vanishes; its nonconstant pairings are even. Upper h2 and c are odd and the upper gate is even. Therefore the constant coordinate of the backward contraction vanishes and every retained nonconstant contraction is even. The w and c velocities are odd and the M velocity has zero constant row/column. This uses no label or input-law symmetry. It preserves every full retained matrix entry; it is not a diagonal-M restriction.

Euler stages, simultaneous Heun stages and affine interpolation preserve these linear parity relations in exact arithmetic. Half-population integration equals full paired integration for all required even integrands. Floating reduction order can differ, as documented.

The maintained test starts with nonzero c, a perturbed w and a dense perturbed M, then checks four Heun steps, zero constant bands, every returned observation and representation restart. It passed on CPU and GPU. Returning both \((h^0,h)\) and \((-h^0,-h)\), with half base weights, is necessary for the signed joint law; the code does this. A positive-half-only observation would be wrong, but that bug is absent.

Generic supplied folded marks are a caller-declared odd extension, as the guide explicitly states. This is not a claim that arbitrary unfolded states can be folded automatically.

### C3. Full finite closure equations, metric, Heun and restart

**Assessment: sound within the documented finite-arithmetic contract.**

For finite tables and nonnegative normalized population/data weights, independent differentiation yields
\[
\partial_{w_i} f=\pi_{1i}(1-h_{1i}^2)q_i u^T,\qquad
\partial_{c_j} f=\pi_{2j}h_{2j},\qquad
\partial_M f=\upsilon a^T.
\]
Multiplication by \(2\mu_a r_a\) and summation gives the displayed vector field. The factor 2, transpose M, and weights agree with both reference and optimized implementations. Optimized precontractions change matrix association only; each RHS uses the complete old state throughout all input blocks.

At positive row weights the metric is population L2 and Frobenius for M. At zero row weights the finite formulas still define a representative velocity; the energy calculation uses multiplication by the zero weight, never division. My additional case had unequal populations/features \((P_1,P_2,K_1,K_2,d,m)=(5,8,4,3,2,7)\), dense nonzero moving blocks, zero weights in both populations and data, zero/nonunit/duplicate inputs and conflicting duplicate labels. Autograd gave
\[
\nabla_w\mathcal L=-\operatorname{diag}(\pi_1)\dot w,\quad
\nabla_c\mathcal L=-\operatorname{diag}(\pi_2)\dot c,\quad
\nabla_M\mathcal L=-\dot M
\]
to a maximum absolute discrepancy \(5.56\times10^{-17}\). The energy identity discrepancy was \(2.78\times10^{-17}\); an independent centered directional finite difference differed by \(8.64\times10^{-12}\). The zero-weight rows had nonzero velocities, which is consistent with the zero contribution to the weighted energy. All-zero inputs gave zero prediction and zero velocity for arbitrary nonzero state and labels, as required by the bias-free model.

The maintained sample-by-sample NumPy oracle uses separate scalar contractions. It and autograd exercise dense nontrivial states, rather than only the c=0 initialization where two velocities vanish. The tests compare a hand-assembled simultaneous Heun stage and completion. All blocks use the same state at each stage.

Fixed arrays and prepared data are copied. Ordinary in-place mutation and field replacement are rejected by identity/version checks. I also verified cache mutation rejection, independent zero-step copies, observation output ownership, real/bool/complex boundaries and preservation of a near-unit mass instead of silent renormalization. Deliberately bypassing PyTorch version tracking through storage views is expressly outside the contract, so the checks are not represented as a security boundary.

The pickle-free restart contains current state, all needed frozen marks, weights, D, data, association and arithmetic metadata. No source tape or prior trajectory is needed. Exact own-state continuation passed on both devices, including arbitrary supplied states; the folding test preserves its representation metadata. Exact replay still requires the documented same device/reduction environment and steps. The implementation does not certify cross-device or cross-version equality.

### C4. Actual finite-network comparator and resource accounting

**Assessment: sound for ordinary float32/64 two-hidden tanh computation.**

The comparator uses the canonical NumPy initializer. I read its complete producer and independently regenerated the RNG draw sequence: first \((n,d)\) standard normals, then \((n,n)\) standard normals divided by \(\sqrt n\), then n standard normals divided by n. At \(n=7,d=3,\mathrm{seed}=271\), all three arrays agreed bitwise. The nonzero random finite readout is not replaced by the closure's zero readout.

Direct differentiation of \(f=c^Th_2/n\), followed by mobilities \((n,1,n)\), gives exactly the comparator's w and c factors -2 and middle factor \(-2/n\). Its transpose is the same dense M transpose. The maintained weighted autograd check and separate NumPy forward/flow oracle pass, as does independently assembled simultaneous Heun.

The unchanged NumPy reference has protected tanh derivative/scaled-product arithmetic. The new Torch comparator explicitly does not inherit that extreme-range promise; its derivative \(1-\tanh^2\) can cancel at saturation. Ordinary numerical limitations are stated correctly. Float32 versus float64 evolved-prediction checks pass on CPU and CUDA at the maintained tolerances \(\mathrm{atol}=3\times10^{-6},\mathrm{rtol}=3\times10^{-4}\); this is a bounded test, not an arbitrary-horizon guarantee.

The symbolic tensor-entry count is correct. Independently summing arrays gave 153 entries for my unequal-size case, 614 entries for unfolded d=3,P=18, and 279 for folded nominal P=18. These match the guide's formulas. The example reports 2016 retained closure bytes and 5120 retained network bytes in float64. Cached transposes are counted even if physical storage can alias, exactly as disclosed. Data, stage copies, observation panels, Python overhead and allocator workspaces are separate. The RHS and precontraction costs do not imply a cost-to-accuracy bound or a uniform advantage when d and n both grow.

### C5. Prediction/Gram comparisons and loss matching

**Assessment: correction required for constant-vector correlations; remaining checked semantics pass.**

Explicit ordered IDs prevent accidental row permutations and duplicate sample identifiers. Prediction errors are deliberately unweighted per image. Gram metrics compare uncentered matrices. Zero-reference and absent-class outputs have the stated null/zero distinctions. The all-seed routine retains each pair and candidate versus reference mean without suggesting that equal seeds couple the distinct objects.

The training-loss matcher sees no passive predictions; it permits nonmonotone saved losses, selects the earliest saved time on equal nearest-loss distances, reports actual mismatch and nearest attained lower/upper loss brackets, and rejects extrapolation. I independently checked nonmonotone ties, target zero, duplicate/permuted IDs, string IDs and zero-reference semantics. These checks passed.

L1 invalidates the stated constant-vector correlation semantics, including within-class and all-seed uses of the shared helper. It does not invalidate the finite equations, prediction arrays, Gram arrays, or the other comparison metrics.

## 4. Required corrections and optional advice

### L1 — ordinary constant arrays can produce a numerical correlation

**Severity: Minor Point, necessary implementation correction.** It is localized and has a straightforward repair without changing the mathematical construction, but the present API contract is false.

Affected source: `code/pde/closure_comparison.py`, lines 30–41, especially mean centering at 36 and the denominator check at 40. The guide promises that either constant vector gives null correlation.

Exact minimal reproducer, on the reviewed NumPy 1.26.4 environment:

```python
from pde.closure_comparison import prediction_metrics

kw = dict(ids=[1, 2, 3], reference_ids=[1, 2, 3])
print(prediction_metrics([.1] * 3, [.1] * 3, **kw)["overall"]["correlation"])
# 1.0000000000000002; required result is None

print(prediction_metrics([.1] * 3, [1., 2., 3.], **kw)["overall"]["correlation"])
# 0.0; required result is None
```

The mean of three stored 0.1 values rounds away from the stored value, so subtraction produces a nonzero constant residual vector. Testing only whether the product of residual norms is zero misclassifies an exactly constant input. The maintained tests use exactly representable constants such as 1 and therefore miss this case. A within-class three-element constant 0.1 subvector reproduces the same failure.

Required repair: detect exact constant input arrays before mean centering (or use another method that provably handles this case), return None when either is constant, and test both overall and class-level decimal-constant inputs. Merely clamping the reported correlation to [-1,1] does not repair undefined constant-vector correlation. The specific reproducer and outputs are retained in the independent attack script/JSON.

### L2 — precise old-dictionary equality is not fully auditable from the packet

**Severity: Minor Point / unavailable supporting dependency, necessary packet or statement correction.** This is a provenance gap, not evidence that the stated equality is false.

Affected statement: `docs/observable_p1.md`, line 64: exact equality with `build_dictionary(1)` ordering and the assertion that codes 0 and 1 add no extra features. The supplied H3.N1 excerpt refers to the “exact coding and order of part B,” but neither that coding definition nor the relevant dictionary/decoder implementation is in the frozen packet. The old code guide reports the p=1 dimensions (5,3), which verifies a count but not this exact ordering/code assertion.

Required resolution: supply the complete narrowly needed frozen coding/dictionary definition and implementation dependency, or remove/narrow this precise implementation-provenance assertion so the chapter claims only its self-contained explicitly displayed retained feature construction. I did not access live omitted source to fill the gap. All coefficient and finite-equation checks above stand independently of that provenance sentence.

### Optional advice

The current nonconstant correlation calculation can overshoot 1 by rounding even outside L1; a small numerical range guard may be useful after valid nonzero variance is established. This is optional and is not the basis for the disposition. The larger API might eventually offer scaled norm calculations for extreme magnitude inputs, but no such enhancement is required for this candidate's ordinary-arithmetic claims.

No major or fatal scientific flaw was found in the checked initialized algebra, finite vector field, parity argument or finite-network scaling. No claim of general-d trained-network convergence was silently evaluated as if it were present.

## 5. Execution evidence and reproducibility

All executed scientific code was read statically first. Runs used only the frozen modules, no external dataset, no downloads and no historical arrays. They were small finite verification jobs. GPU work used the supervisor-authorized `cuda:1`; there was no parameter sweep or scientific campaign.

Environment: Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130; GPU NVIDIA GeForce RTX 3090. Numerical threads were one. TF32 was disabled and deterministic algorithms enabled by the maintained tests/producer before engine construction. CUBLAS_WORKSPACE_CONFIG was `:4096:8`. The tools emitted the expected deprecation warning about Torch's older TF32 setting API, with no execution failure.

Every command below exited 0. Logs and fresh source/output arrays remain under the scratch root. CPU tests had a 300-second limit, CUDA tests 600 seconds, producers an outer 180-second limit plus their internal 120-second work alarm, and the independent/guide checks 60 seconds. No limit was reached.

| Check | Actual result |
|---|---|
| Maintained CPU suite | 12/12 pass; unittest runtime 0.329 s |
| Maintained cuda:1 suite | 12/12 pass; unittest runtime 0.883 s |
| Two fresh CPU producers | Both complete; exact repeat observation arrays |
| CPU independent analyzer | Pass; replay max absolute error \(2.220446049250313\times10^{-16}\) |
| Two fresh GPU producers | Both complete; exact repeat observation arrays |
| GPU independent analyzer, NumPy replay | Pass; replay max absolute error \(1.1102230246251565\times10^{-16}\) |
| CPU versus GPU example arrays | Max absolute discrepancy \(2.220446049250313\times10^{-16}\) across all saved fields |
| Independent attacks | All stated algebra, ownership, domain, mass, initialization and cost checks pass; L1 deliberately reproduced |
| New guide Python blocks | Both execute successfully, including restart |
| Optional-import boundary | `import pde` does not import Torch |
| Imported Gaussian-moment dependency smoke checks | Both guide identities pass |
| Frozen hash recheck | Every manifest hash still matches |

The producer's measured work times were 0.06755/0.05298 seconds on CPU and 0.39490/0.39507 seconds on GPU. These tiny times are recorded only as operation evidence, with the producer's explicit timing exclusions. Both GPU runs peaked at 33,610,752 allocated bytes and 35,651,584 reserved bytes. These are whole-process allocator measurements with both systems present, not isolated per-system benchmarks.

The analyzer independently recomputes endpoint predictions and Grams from saved current/frozen arrays and verifies saved output hashes and comparison metrics. It does not independently rerun the full time integration. Separate RHS, gradient and Heun checks provide the integration evidence. Neither successful endpoint replay nor exact repeats establishes closure approximation accuracy.

### Exact command record

Working directory: `/home/amir/Codes/PDE`. The following named paths expand the actual commands used; destinations were fresh at execution:

```sh
B=/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v2
S=/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a1_v2
P=/home/amir/miniconda3/bin/python
export PYTHONPATH="$B/code" PYTHONDONTWRITEBYTECODE=1
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export CUBLAS_WORKSPACE_CONFIG=:4096:8 TMPDIR="$S/tmp"

PDE_TEST_DEVICE=cpu timeout 300 "$P" -B "$B/code/tests/test_general_p1.py" > "$S/cpu_tests.log" 2>&1
PDE_TEST_DEVICE=cuda:1 timeout 600 "$P" -B "$B/code/tests/test_general_p1.py" > "$S/cuda_tests.log" 2>&1
timeout 180 "$P" -B "$B/code/scripts/example_general_p1.py" --output "$S/cpu_a" --device cpu > "$S/cpu_a.log" 2>&1
timeout 180 "$P" -B "$B/code/scripts/example_general_p1.py" --output "$S/cpu_b" --device cpu > "$S/cpu_b.log" 2>&1
"$P" -B "$B/code/scripts/analyze_general_p1.py" --run "$S/cpu_a" --repeat "$S/cpu_b" --output "$S/cpu_analysis.json"
timeout 180 "$P" -B "$B/code/scripts/example_general_p1.py" --output "$S/cuda_a" --device cuda:1 > "$S/cuda_a.log" 2>&1
timeout 180 "$P" -B "$B/code/scripts/example_general_p1.py" --output "$S/cuda_b" --device cuda:1 > "$S/cuda_b.log" 2>&1
"$P" -B "$B/code/scripts/analyze_general_p1.py" --run "$S/cuda_a" --repeat "$S/cuda_b" --output "$S/cuda_analysis.json"
timeout 60 "$P" -B "$S/independent_attacks.py" > "$S/independent_attacks.log" 2>&1
timeout 60 "$P" -B "$S/guide_checks.py" > "$S/guide_checks.log" 2>&1
```

The independent attacks were fixed to seed 583 for the generic weighted state and seed 271 for the separately regenerated comparator draws. They used the tolerances stored explicitly in their retained source. Repeated deterministic examples used the maintained fixed seed 101, d=3,m=9,n=P=16, folded base count 8, ten Heun steps of .005. There was no selection among runs.

Evidence links:

- [Independent attack source](../../data/generated/first_order_dimension_mnist/review_a1_v2/independent_attacks.py), [results](../../data/generated/first_order_dimension_mnist/review_a1_v2/independent_attacks.json), [execution log](../../data/generated/first_order_dimension_mnist/review_a1_v2/independent_attacks.log).
- [CPU tests](../../data/generated/first_order_dimension_mnist/review_a1_v2/cpu_tests.log), [CUDA tests](../../data/generated/first_order_dimension_mnist/review_a1_v2/cuda_tests.log).
- [CPU replay](../../data/generated/first_order_dimension_mnist/review_a1_v2/cpu_analysis.json), [CUDA replay](../../data/generated/first_order_dimension_mnist/review_a1_v2/cuda_analysis.json).
- [Guide/import check source](../../data/generated/first_order_dimension_mnist/review_a1_v2/guide_checks.py), [log](../../data/generated/first_order_dimension_mnist/review_a1_v2/guide_checks.log).
- [Full evidence output hashes](../../data/generated/first_order_dimension_mnist/review_a1_v2/output_hashes.json). This covers the four generated runs, logs, analysis results and reviewer check sources.

## 6. Completion, limits and component verdicts

| Component | Verdict and limit |
|---|---|
| Self-contained general-d initialized coefficient algebra | Sound within the displayed feature construction |
| Exact equivalence to old p=1 dictionary order/codes | Unverifiable from supplied dependency; L2 requires correction |
| Nontrivial antithetic folding and full signed observations | Sound for the stated invariant odd extension |
| Generic weighted finite closure, both action orientations | Sound; independently checked at nonzero dense states and zero weights |
| Simultaneous Heun, boundary checks, owned state and cache handling | Pass within stated arithmetic/mutation contract |
| Same-environment own-state restart | Pass on CPU and CUDA |
| Actual finite-network initialization and physical gradient factors | Pass with independent producer/gradient checks |
| Comparison methods | L1 required; other exercised semantics pass |
| Producer, analyzer and new guide recipe | Fresh CPU/CUDA reproduction passes |
| Complexity/storage description | Correct tensor accounting; no speed/accuracy conclusion |
| General-d trained neural identification, MNIST/PCA, broad numerical accuracy | Outside candidate claims and not established by this review |

Confidence is high in the scoped algebra and finite implementation conclusions because all proposed scientific/runtime lines and supplied proof dependencies were read, the difficult response/transpose/metric steps were independently derived, and both CPU and CUDA executions were checked. Confidence in the precise old-dictionary provenance assertion is withheld because the needed input is absent. The review does not cover arbitrary GPU environments, long-horizon numerical stability, general-d closure accuracy, all old book claims, or old-code examples unrelated to the addition.

The full assigned review is complete with the two stated necessary corrections outstanding. Frozen_v2 and these adverse findings should remain preserved. A corrected packet must not inherit an unconditional PASS from this report.

## Appendix: exact frozen input hashes and coverage

The following appendix is generated from the already verified manifest and actual file bytes. “Read” means complete content covered; “hash only” means no content exposure. The two original guides were covered through their byte-identical full prefixes as described above. The frozen mathematical skill is byte-identical to the fully read system skill.

| Input | Lines | Coverage | SHA256 |
|---|---:|---|---|
| `PROMOTION_PLACEMENT.md` | 27 | Hash only | `b3ca29eb03eaacf95b7b06410bf50bdb8141d2ca343881ce33fc9d34b3a26db6` |
| `PROMOTION_REVIEW_ASSIGNMENT.md` | 56 | Read | `2ca132680a8965644cfc4f9e44b4a0380821588de2485736979b945c5a773ede` |
| `PROMOTION_assemble.py` | 38 | Read | `9afd22e391e517a741a12b3c1752732acc8c8efe0c3d0e692b9f5241bca16bf2` |
| `code/GENERAL_P1.md` | 212 | Read | `982cace29181a9e049fe9e9e88a735c8631015d36614c13d8c81b9074f90f114` |
| `code/README.md` | 1117 | Read | `ff5a89effef3fc1bc86a2bcc699453731c50bebffd9fd5ff0844f690717dc237` |
| `code/pde/__init__.py` | 26 | Read | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/closure_comparison.py` | 125 | Read | `750203dc5ceb7a72dc2abf160fa97c3e38311c0cac38bc1463b2dfaa1c75809b` |
| `code/pde/finite_network.py` | 363 | Read | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_torch.py` | 153 | Read | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `code/pde/gaussian_moments.py` | 114 | Read | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_p1_initialization.py` | 181 | Read | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `code/pde/observable_torch_p1.py` | 403 | Read | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `code/scripts/analyze_general_p1.py` | 46 | Read | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| `code/scripts/example_general_p1.py` | 131 | Read | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| `code/tests/test_general_p1.py` | 271 | Read | `4ceeab90632505a694783a44a254acdcb57214ce9e9eaffba65b485b6a0e298a` |
| `dependencies/global_nonlinear_source_units.md` | 393 | Read | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |
| `dependencies/original_code_README.md` | 1113 | Read | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `dependencies/original_docs_README.md` | 738 | Read | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | 98 | Read | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | 742 | Read | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `docs/observable_p1.md` | 326 | Read | `290f97011bf4cd04be8962030cec8c3d58f5ad9667bfe67ba47ad9de17c3c93e` |
| `instructions/AGENTS.md` | 62 | Read | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `instructions/RESEARCH_WORKFLOW.md` | 225 | Read | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `instructions/investigate-conjectures/SKILL.md` | 185 | Read | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `instructions/investigate-conjectures/agents/openai.yaml` | 11 | Hash only | `ba8e39aba0463d706c4fa49375b90d0b9ce4d0ce436875e6d35ca61bcf387d02` |
| `instructions/investigate-conjectures/references/adversarial-audit.md` | 121 | Read | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `instructions/investigate-conjectures/references/decisive-experiments.md` | 141 | Read | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| `instructions/investigate-conjectures/references/evidence-ledger.md` | 157 | Hash only | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `instructions/investigate-conjectures/references/proof-search-orchestration.md` | 97 | Hash only | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
| `instructions/investigate-conjectures/references/research-contract.md` | 99 | Hash only | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `instructions/solve-math-rigorously/SKILL.md` | 115 | Read | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `instructions/solve-math-rigorously/agents/openai.yaml` | 12 | Hash only | `13e1679d378e917628b9f7d58c687e78e0442df8b6ad9089a4720a87f6bb3d1c` |

Additional fully read inputs:

- `/home/amir/Codes/PDE/studies/first_order_dimension_mnist/PROMOTION_MANIFEST.json`: `395ac0e660eadaca2bb9972a55e2f8dc8627ad60796a13db3458dd449b30660d`
- `/home/amir/Codes/PDE/studies/first_order_dimension_mnist/PROMOTION_REVIEW_ASSIGNMENT.md`: `2ca132680a8965644cfc4f9e44b4a0380821588de2485736979b945c5a773ede`
- `/home/codex-b/.codex/skills/review-ai-paper/SKILL.md`: `723bea71235b35d04e8e6c07f6a90ad28e09b18a0364cc9dc19ff5296f3ca567`
- `/home/codex-b/.codex/skills/review-ai-paper/references/severity-rubric.md`: `0f6a2f47218931343187ffdb6b6da35cedbc79dde5699647383b1b08b24b6c0e`
- `/etc/codex/skills/solve-math-rigorously/SKILL.md`: `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`
