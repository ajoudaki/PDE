# Independent scientific promotion review B — frozen version 1

**Verdict: REQUIRES CORRECTION. Review complete for the assigned scope; this is not an acceptance.**

There are two required corrections: an accepted exactly singular training Gram in the new selected-coordinate runtime, and an incorrect coefficient name in an older-theory proof. The proposed deterministic tests pass, but do not detect the first defect for all ordinary initializations. Neither finding is a counterexample to the compact chapter's exact-arithmetic theorem under its positive-Gram hypotheses.

## Identity, isolation and inputs

Reviewer: `/root/scientific_review_b_v1`, a newly created independent context. I did not author, assemble, select, or edit the candidate. I did not read the study README, study history, other reviews, author verification logs, the live book/code, or another study. No scientific messages from other reviewers were inputs. The supervisor supplied the assignment and requested completion of the entire original scope after I reported the defects; it supplied no mathematical solution or desired verdict. No new agents, research campaign, network lookup, or dataset download was used.

The sole scientific input was `/home/amir/Codes/PDE/data/generated/book_promotion_20261010/promotion_review_v1/`. I began with its neutral assignment and manifest and verified all 114 manifest entries, both byte counts and SHA256. I verified them again after the checks; all still match. The SHA256 of `inputs.json` itself is:

```text
155cdfe9e8cd3f25b0aa3ade60619877f28704a9c8ad48a8e84778b26768cea2
```

The required process inputs were the packet's complete `edition/AGENTS.md` and `edition/RESEARCH_WORKFLOW.md`, `/home/amir/.codex/skills/solve-math-rigorously/SKILL.md`, `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`, and its `references/neural-response-memory.md`. These did not expand scientific access. No additional scientific input was necessary or obtained. Historical operational statements encountered in the required full frozen `code/README.md` are not independently reproduced historical evidence in this review.

There are 51 entries requiring complete reading and 63 frozen standalone build/runtime inputs excluded from a fresh whole-book/unrelated-code audit. I read all 51 in their assigned scope, repaired truncated displays, and inspected every custom line of the HTML/JavaScript. The sole source-line exception within those 51 is `edition/code/pde/radial_explorer.html:97`, the unmodified bundled D3 library, explicitly excluded by the assignment; its custom surroundings, attribution, and application code were read and its actual library executed by the Node test. `inputs.json` was read for all scope and identity metadata and all entries were processed for verification. The exact entry-level read coverage, line counts, original and verified hashes, and byte counts are in [final_read_coverage.json](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/final_read_coverage.json). The initial verification is retained in [verified_inputs.json](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/verified_inputs.json).

## Required correction B1: singular training Gram can be accepted

**Severity: substantive numerical boundary defect; blocks the selected runtime and hence the proposed code package.**

Locations: frozen `edition/code/pde/compression.py:311` and `:320–333`; the singularity test at `edition/code/tests/test_compression.py:270–274`; the corrected-readout contract in `edition/code/COMPRESSION.md:128–144`.

Let `inputs` contain two identical unit rows `(1,0)`, and let the label vector be `y=(0.1,-0.08)`. Use float64 CPU `Dense(12,2,seed=0)` and `Selected(dense,inputs,y,budget=12)`. The two last-layer feature columns are identical. Therefore, with `V` the last-layer features divided by the square root of the number of training examples and `M` the positive source metric, the matrix `Q=V.T @ M @ V` has rank one. It cannot satisfy the required positive-definiteness condition.

The constructor nevertheless succeeds. `_readout` symmetrizes `Q`, calls `torch.linalg.cholesky_ex`, and treats `info==0` as sufficient. Floating Cholesky can report success for this exactly singular matrix. The constructor comment explicitly promises to reject deficient training Grams, and the supplied test verifies rejection only at seed 1.

The independent attack tried seeds 0 through 19, without changing the packet. Seeds **0, 10, 12, 13, 14, 15 and 19** were accepted. For seed 0 the computed eigenvalues were `[0.0,0.17866456729266422]`.

The guide permits the caller to own and edit a returned moving state. Clone the accepted initial state and set its final deficit vector `c` to zero. The corrected-prediction identity would require the two training predictions to be `y-c=(0.1,-0.08)`. The actual prediction is:

```text
[-0.271755553237388, -0.271755553237388]
maximum absolute identity error = 0.37175555323738796
```

This is an order-one failure, not normal roundoff in a well-conditioned solve. Identical inputs cannot produce the two requested distinct outputs; the boundary must reject this invalid Gram before using the inverse. The six other accepted seeds also violate the identity, with maximum absolute error `0.1` in this check.

A separate short check kept the unmodified initial moving state: seed 0 was accepted at construction, one Euler step of size `0.001` retained the identity to `4.24e-22`, and evaluation at step 2 raised `ArithmeticError` for the still-singular Gram. This latter result is recorded to distinguish the deliberately edited-state identity attack from actual evolution; I do not claim an order-one trajectory error from that short run.

Required repair: impose an explicit, scale-aware numerical rank/conditioning acceptance criterion suitable for this inverse contract, and reject unresolved solves. Check the corrected training identity or the relevant solve residual against the declared precision/conditioning contract. The solution must not silently introduce a ridge, floor, or pseudoinverse while retaining the exact-Gram claim. Add meaningful coverage for multiple singular geometries/seeds and near-singular cases, including an accepted Cholesky factorization with unresolved rank. This is a request to repair numerical admissibility, not to prove exact spectral decisions in floating arithmetic.

Evidence: [duplicate_gram.json](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/duplicate_gram.json), [duplicate_gram_evolution.json](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/duplicate_gram_evolution.json), and the retained independent reproducer [duplicate_gram_attack.py](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/duplicate_gram_attack.py).

This example is outside the compact theorem's positive initial Gram hypothesis. It does **not** refute that theorem, the source-selection lemma, or the corrected optimizer in exact arithmetic. It does refute the numerical constructor's deficient-Gram rejection and its resulting readout identity on an accepted instance.

## Required correction B2: the tanh series uses the wrong coefficient name

**Severity: local mathematical correctness/notation error; required correction before accepting the older-theory addition.**

Location: frozen `additions/promotion_09.qmd:332–334` in `proof-fixed-closure-landscape`.

After defining `tanh(t)=sum_{j>=0}(-1)^j A_j t^(2j+1)`, the proof says the identity `phi'=1-phi^2` gives `a_reg=1`. It gives **`A_0=1`**. The already defined `a_reg` is the regression coefficient of `eq-fixed-closure-regression`, lines 180–187; it is not the leading tanh-series coefficient.

The erroneous equation is also false for that established symbol. Its first normal equation is

```text
(nu+eta) a_reg + beta b_reg = alpha nu.
```

Here the same proof has `nu>0`, `eta>0`, `0<alpha<1`, `beta>0`, and `b_reg>0`. Consequently `a_reg < alpha*nu/(nu+eta) < 1`. The correction is to replace `a_reg=1` with `A_0=1` and to state the following coefficient recurrence for `j>=1`:

```text
(2j+1) A_j = sum_{k+l=j-1} A_k A_l > 0.
```

With that correction, the nonzero odd coefficients and the Vandermonde independence argument have the intended justification. I found no independent obstruction to that argument. The defect must remain visible in the gate result until the frozen text is corrected and reviewed; it is not silently repaired by this report.

## Mathematical audit and component conclusions

Every line of the five mathematical additions and the five assigned maintained-book excerpts was read. The complete compact chapter has 4,537 lines; the four older additions have 800, 288, 108 and 90 lines. I checked statements against their actual model and quantifiers, not against historical summaries.

| Component | Review conclusion |
|---|---|
| Complete-trajectory compact theorem and full proof | Complete review; no additional required correction identified. This is an exact mathematical result under its assumptions, not a certificate for the numerical source builders. |
| Older fixed-order geometry/trainability addition (`promotion_09`) | **Requires B2.** Remaining arguments reviewed; no further objection identified. |
| Protected pairs, cyclic triples, and passive-predictor freedom (`promotion_10`, `_12`, `_13`) | Complete review; no additional objection identified within the stated fixed-closure scopes. Their shared dependence on the corrected ridge-independence argument must be retained. |
| Dense/Legendre finite numerical implementation | Complete source and test review; exercised checks pass; no additional defect identified. |
| Harmonic/Taylor selected runtime | **Requires B1.** Neither backend is the theorem's certified global compiler. |
| Initialized finite-carrier dictionaries and named maintained dependencies | Complete assigned-source review; deterministic tests pass; no additional required correction identified. |
| Data construction, prediction views, radial explorer, guides and tiny recipes | Complete custom-source review; scoped deterministic and operational checks pass; no additional required correction identified. |
| Package promotion as a whole | **REQUIRES CORRECTION.** No acceptance, even though the review is complete and ordinary tests pass. |

The compact-theorem audit covered the following proof obligations and boundary distinctions.

1. **Finite model and initialization.** I checked normalized input rows, the stored hidden/readout scaling, physical unhalved-loss mobilities, exact zero readout, the positive training-Gram hypothesis, and the exceptionally small label hypothesis. The width threshold is allowed to depend on the fixed problem. Random small readout in the old maintained network is a separate convention, not silently interchangeable with this theorem.
2. **Fitting and signed perturbations.** I followed the exit/continuation argument, derivative/feature bounds and integrable residual tails. Real fitting is separate from complex analyticity. The signed comparison uses the relevant time-dependent coercivity and does not derive a uniform-in-time comparison merely from finite-horizon Gronwall.
3. **Analytic-source foundations.** I read the entire local-power, local-map, remainder, passive-observable, Gaussian-rectangle and provisional-stop arguments, including cavity conditioning, trace retention, finite nets/control entropy, and the order of width/moment limits. I checked the distinction between whole-sphere and finite-panel analytic domains, the residual-adapted panel construction, and the finite all-time source carriers. No theorem step was accepted merely from an empirical source fit.
4. **Legendre compression.** I checked normalization of the shifted Legendre projection, the constant prefix represented by `tau(0)=1`, transport of moments, and the product of endpoint projection errors in the hidden-matrix defect. The independent-fitting argument is needed at each fixed order; the finite truncation is not equated to a fitted dense trajectory without its perturbation and tail estimates. The residual-zero boundary does not require division by a vanishing residual.
5. **Dense fluctuation.** I followed the last-layer innovation variance, conditional scalar small-ball argument and analytic derivative-to-trajectory transfer. A nonzero formal derivative alone would not prove the positive-time lower fluctuation; the chapter supplies the transfer argument. Conditioning and shifts are retained rather than treated as unconditional centered independence.
6. **Selected dynamics.** I checked the constructive finite selector, exact source inner product and metric adjoint, the corrected readout's training interpolation identity when the Gram is positive definite, and the prescribed residual equation. The energy/fitting argument is for this prescribed optimizer; it is not a claim that differentiating the corrected predictor gives an ordinary Euclidean gradient. The finite-horizon comparison, cancellation terms and independently controlled endpoint tails are separate obligations.
7. **Compiler and state counts.** I followed finite origin jets, analytic continuation/coefficient determination, whole-sphere polynomial sources and their joint time/spatial counts, then the adaptive finite-panel construction and input-span reduction. Existence of finite initialization-only preprocessing does not establish practical efficiency. The final assembly keeps frozen matrices, metrics and moving state in the counts, and keeps whole-sphere and declared-panel approximation targets distinct.

For the older additions, I checked the joint correlated lower Gaussian marks and independent upper population, ridge normalization and physical weighted row/readout metric; the regression bounds yielding strict coordinate monotonicity; the architectural loss floor under equal/opposite inputs; the distinction between the stated `L2`/Frobenius local-minimum topology and bounded representatives used in flow arguments; the small-set variation and ridge independence; the three-direction lower-layer submersion and the upper-collapse example; and the scalar ascent/readout-normalization calculation used to protect a feature norm. The protected-pair result is for the explicitly listed reflections/antipodes, with an additional small-label basin for other orientations; it is not full rotational invariance. The cyclic-triple result keeps its compact-family and positive initial contrast assumptions. Passive-query freedom is expressivity at fixed initialized features and arbitrary readout, not reachability of every such predictor by the initialized optimizer.

The five maintained excerpts were sufficient to define the inherited fixed closure, joint mark laws, normalization, word grammar, polynomial enrichment and finite-time existence used by these additions. I did not treat unrelated old chapters as fresh proof inputs or silently fill a missing claim from the live book.

## Code, data and display audit

All five new Python implementation modules, both custom viewer implementations, both new scripts, the structural checker, all six proposed test files, the full named maintained modules and all assigned guides were read. Source setup and runtime were distinguished throughout.

The finite equations use the actual forward matrix and its true transpose or source-metric adjoint. The selected deficit is extra state, not a residual substituted after differentiating a corrected predictor. Full-retention equivalence is tested on compatible states. The initialized-dictionary adapter keeps actual finite carrier rows and the small random finite readout; it is not a selected-coordinate model or an all-time approximation theorem. Its observable ridge is an intended filter and is not a reason to introduce a hidden ridge into B1's different contract.

The numerical Harmonic producer uses a disposable finite dense rollout and sampled coefficient construction; the Taylor producer supports origin jets through order two or a finite-panel rollout. Rank truncation and finite quadrature are explicit approximation steps. Their provenance and guides properly deny the theorem's certified global source bound, analytic continuation implementation, fitted-endpoint guarantee and efficient preprocessing claim. The scripts use short finite times and no archived reference trajectory. I found no hidden scientific claim that these examples prove neural fidelity or a compression speedup.

Toy data use local seeded draws, unit rows, train-only target normalization, and independent declared query geometry. The MNIST path preserves separate supplied/official pools, uses raw pixel normalization and split-qualified IDs, requires explicit download opt-in, and does not consume query labels in a source constructor. The tests use fixtures/mocks; no real dataset-quality or downloaded-data validation was performed.

Static and interactive views operate on supplied arrays. The signed radial offset preserves input angle; sphere hemispheres are complementary; sample error statistics do not purport to be continuum norms. The radial explorer distinguishes actual training predictions, mean seed loss versus loss of a mean predictor, physical-time interpolation, loss-bracket interpolation and recorded endpoints. Custom Python and JavaScript validation, safe embedding and controls were inspected. Node checks execute the custom application, including the actual D3 bundle in the radial case, with stand-ins for browser objects. They are not a pixel/layout or full-browser validation.

## Executed checks, commands and results

Working directory for all commands: `/home/amir/Codes/PDE`. Python was `/home/amir/miniconda3/bin/python` (3.10.14), NumPy 1.26.4, Torch 2.9.0+cu130 used on CPU with one Torch/numerical thread; Node was v19.9.0. Torch emitted its upstream TF32-setting deprecation warning during metadata access; no CUDA execution was used. Environment evidence is in [environment.json](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/environment.json).

The relevant command environment was:

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=/home/amir/Codes/PDE/data/generated/book_promotion_20261010/promotion_review_v1/edition/code
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PDE_OPTIONAL_TEST_SCRATCH=/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/tests
export TMPDIR=/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1
export MPLCONFIGDIR=/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/matplotlib
```

1. **Hash/size verification.** A Python `hashlib.sha256` pass over every `inputs.json` entry compared both size and hash, initially and after all checks. Both passes had zero mismatches. No packet file was edited, and no bytecode/cache/output was written into it. Exact results are retained in the two verification ledgers linked above.
2. **Proposed tests.** I executed the following discovery body in one Python process, with output retained to `proposed_tests.log`:

   ```python
   suite = unittest.TestSuite()
   for pattern in ['test_compression*.py', 'test_observable_dictionaries.py',
                   'test_prediction_views.py', 'test_radial*.py']:
       suite.addTests(unittest.defaultTestLoader.discover(str(root), pattern=pattern))
   result = unittest.TextTestRunner(stream=out, verbosity=2).run(suite)
   ```

   `root` was the absolute frozen `edition/code/tests` directory; `out` was this reviewer's scratch log. The exact executable equivalent, retaining the original body, environment record and exit status behavior, is now [run_proposed_tests.py](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/run_proposed_tests.py). Invoke it with `/home/amir/miniconda3/bin/python -B` under the environment above. **Result: 52 tests, 0 failures, 0 errors, 0 skips; 1.806 seconds of unittest execution.** The full [proposed_tests.log](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/proposed_tests.log) preserves individual names and outcomes.

   These include independent autograd/NumPy finite-flow oracles, all six activation mobilities, moment quadrature/transport, nonzero Legendre defect, origin-jet derivatives, selected energy/training identities, BSS/metric identities, complete-basis dense equivalence, all retained dictionary words and seeded prefixes, weighted general-dimensional initialization, endpoint status, dataset separation and normalization, signed geometry/scales, JSON embedding and both JavaScript harnesses. Their finite assertions do not prove asymptotic theorems. In particular, the existing seed-1 singularity test passes while B1 remains reproducible.
3. **Independent boundary attacks.** Two inline Python commands used the frozen `pde.compression` import and the code now preserved in `duplicate_gram_attack.py`: first the 20-seed construction/edited-deficit check, then seed-0 ordinary Euler evolution. Their exact parameters, accepted seeds, failures and numerical outputs are in B1 and its JSON logs. The saved reproducer combines those two already-executed bodies; it was not used to alter the candidate or to erase failed outputs.
4. **End-to-end short recipes.** I ran these actual commands with the environment above, once each, through `subprocess.run(...,timeout=120)`:

   ```sh
   /home/amir/miniconda3/bin/python -B /home/amir/Codes/PDE/data/generated/book_promotion_20261010/promotion_review_v1/edition/code/scripts/example_compression.py --out /home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/example_compression
   /home/amir/miniconda3/bin/python -B /home/amir/Codes/PDE/data/generated/book_promotion_20261010/promotion_review_v1/edition/code/scripts/example_radial_explorer.py --out /home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/example_radial_explorer
   ```

   Both exited 0; elapsed subprocess times were 3.721 and 1.868 seconds. Generated arrays, images, HTML and their manifests remain in the two named scratch directories. Exact command arrays and timings are in [example_runs.json](/home/amir/Codes/PDE/data/generated/book_promotion_20261010/reviewer_b_v1/example_runs.json); stdout/stderr are in `example_compression.log` and `example_radial_explorer.log`. These are operation checks only, without fitted-limit, speed or approximation conclusions.
5. **Structural boundary/local links.** I ran `/home/amir/miniconda3/bin/python -B data/generated/book_promotion_20261010/promotion_review_v1/edition/code/tools/check_library.py`. It exited 0 and printed `Library boundary and local links checked: 92 files.` This checker reads frozen standalone inputs structurally; it is not a scientific review of the excluded 63 files or a theorem/PDF-render certificate.
6. **Analytic contradiction check.** B2 was checked directly against the supplied regression normal equations and strict inequalities. No numerical quadrature was needed to establish the error.

I did not run historical long-horizon campaigns, a full unrelated maintained test suite, CUDA checks, real MNIST loading, a browser screenshot campaign, or a Quarto/PDF render. None is claimed here. The assigned full reading and relevant deterministic/operational checks are complete; excluded historical runtime inputs were not independently scientifically endorsed.

## Unresolved objections and completion

B1 and B2 remain unresolved in the exact frozen packet. No proposed correction was applied or assumed. I have no other identified required correction after completing the assigned mathematical, code, test and recipe review, and no missing necessary input remains. The parent was promptly notified of the rank-handling defect and the proof coefficient error; at its explicit request I completed the rest of the original scope to consolidate findings.

This is a completed independent review with a **REQUIRES CORRECTION** verdict. The current packet is not accepted. A corrected concrete packet must be evaluated on its own changed mathematics, boundary behavior and preserved regression checks; successful ordinary tests alone do not close these objections.

## Exact complete-reading inventory

The table below uses paths relative to the frozen packet. Every listed entry was read in full, with the explicitly assigned D3 exception described above. All 63 excluded build/runtime entries, their exact hashes and unread status are recorded individually in `final_read_coverage.json`; they are not missing complete-reading obligations.

| Frozen path | Lines | SHA256 |
|---|---:|---|
| `additions/promotion_09.qmd` | 800 | `0874d7399c125b2639225e65c5a5a94701feb8d318d5a19302e0fec807eede12` |
| `additions/promotion_10.qmd` | 288 | `82824a92deef50a47c5445c259f42624aaa0d435cfbc7d12a6a35df8040e38c2` |
| `additions/promotion_12.qmd` | 108 | `a5b40e79c58ee4746a1ecafcf7bf74e33864ae3875a35d9ba3398a844eca3ff1` |
| `additions/promotion_13.qmd` | 90 | `b637dfbd85b4cedb2fdeebe6ff7eb927edad43bd71ba1571f9fa95b3cd832c57` |
| `additions/promotion_compression.qmd` | 4537 | `5302a2a1e077f5ef18d860374d21b2da484fc67253759d399c1c4ab520b1dca0` |
| `assignment.md` | 44 | `b0ff4a51dae7faf3b876deb15fb29613ff468007ce6bc4a45826f31d9fb14d75` |
| `book_dependencies/07-observable-closure.qmd.lines-4888-5040.txt` | 153 | `8d1132b68270f1f4ff5e750faf791e75301f098b2c2e30f958771b19e38e93a3` |
| `book_dependencies/07-observable-closure.qmd.lines-5265-5421.txt` | 157 | `9419d7c80fedc61dfdb8608801b13448766d75737b7d4d46228ac7f3d6c2535c` |
| `book_dependencies/07-observable-closure.qmd.lines-5461-5492.txt` | 32 | `1bed870ff26a81829f298c3b9e5488f5b934e9249d5cf5fb10b029deefcfc871` |
| `book_dependencies/08-autonomous-computation.qmd.lines-3119-3393.txt` | 275 | `dff5d0b73444886a63d206251213b5eb7967cab5b622ff6c1f96c38195bb98db` |
| `book_dependencies/08-autonomous-computation.qmd.lines-5345-5387.txt` | 43 | `b2af10e2d28b9ae71b6616e86b1461f932703015c0a2476ea276f2c0fc55888c` |
| `edition/AGENTS.md` | 99 | `d9835366632b1077c371218c67dd43b1da3c002fb55963c3c21b3cb26fa20e97` |
| `edition/RESEARCH_WORKFLOW.md` | 257 | `459143719de664d1d6669c615b499d5b2f2505c5d7bad0c22dd7657e9ac41dd1` |
| `edition/code/COMPRESSION.md` | 209 | `43280504b77f738b6ea30a3de9e1ef4cc57f51a985833d030eafe42f44a375e6` |
| `edition/code/COMPRESSION_DATA.md` | 136 | `189c0a7ffd62364d47d3670f9667f9f83af0ff7fb09c9ff1c3d4c0a2c400f346` |
| `edition/code/GENERAL_P1.md` | 235 | `6eab7abf57530cae3c4669ad9cecb9cfadaa42f4b638d70ae742ce5334f55b74` |
| `edition/code/OBSERVABLE_DICTIONARIES.md` | 266 | `807e679baa162ea151e419fef58e0bb570fb253a7e54307f27c9cc61c861ad87` |
| `edition/code/PREDICTION_VIEWS.md` | 129 | `ea1cce40fcc7d253309351e0e2a0e0c9b9fe1ab4ac79f3fbf36c59dbc31979d5` |
| `edition/code/RADIAL_EXPLORER.md` | 80 | `c15d04bad246ab801ded97674fdb205cd7f38423ef1890855ad5732d53873f18` |
| `edition/code/README.md` | 1254 | `b038f6033e8e387c602b0e7947ab08a793fb825f179d5afa161d6c12d4495807` |
| `edition/code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `edition/code/pde/closure_comparison.py` | 226 | `f715624c7d81116fd24d888ab5bce1afc3e8b353406b23553e6a6ff8b4f0a89e` |
| `edition/code/pde/compression.py` | 754 | `47b0045f128b3ef36431e3311514632724fc5c6208a4466c017094e3685968d3` |
| `edition/code/pde/compression_data.py` | 226 | `12b8e9c351d368660f8655587e05e828fee4608e369c5ce128c982c19f5557d6` |
| `edition/code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `edition/code/pde/finite_torch.py` | 153 | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `edition/code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `edition/code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `edition/code/pde/observable_compiler.py` | 528 | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `edition/code/pde/observable_dictionaries.py` | 385 | `4ac8d595f8250e8e2e90cb12e9ad83c61dfb50210057f07060b2a551fe05d5b3` |
| `edition/code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `edition/code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `edition/code/pde/observable_p1_initialization.py` | 181 | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `edition/code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `edition/code/pde/observable_torch_p1.py` | 403 | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `edition/code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `edition/code/pde/prediction_views.py` | 319 | `9f1fa503ed0f4a60e63c0cdda80ea33b9b443be8993c722e52b32ed0a6af2e5f` |
| `edition/code/pde/radial_explorer.html` | 365 | `390499a83fcaba395614cebf31dc2935b072aa0b9cfbd7cdd5832fe8fc08296c` |
| `edition/code/pde/radial_explorer.py` | 320 | `61412b5c2202a1ed45f49c56ce2092da5234c2fd231119f3bc796833fc903506` |
| `edition/code/scripts/example_compression.py` | 85 | `90df9f20cef5fb0964b8b09ee7a1970695fbeeb98ba2641adbd316eef8279435` |
| `edition/code/scripts/example_radial_explorer.py` | 70 | `706636fcd3868dc2b6f4f19efce073d31fdf17433df8ba917b3222c865d9f525` |
| `edition/code/tests/test_compression.py` | 297 | `99c23de2fa009f7af0469166305229f7afa99a589e1dcc4ca420e27ca4ebf95c` |
| `edition/code/tests/test_compression_data.py` | 209 | `24115018f7f1231bc2b1bdcb8ccb8096bf067e75d0b0837008006cc00bda11d7` |
| `edition/code/tests/test_observable_dictionaries.py` | 212 | `149b3d8be11fed0689b1d8e0389d6e3ab057924b750952277bfdafdfbceb8457` |
| `edition/code/tests/test_prediction_views.py` | 154 | `4d808ba2bb1a8e832685d09f6a843987eb969044bbe4eac08962d5f6ddead4f7` |
| `edition/code/tests/test_radial_data.py` | 212 | `4db24ee6165e6d00144fb0a77664052a0f60d951e0bf002090171962a8e6db58` |
| `edition/code/tests/test_radial_viewer.py` | 124 | `a37a4e2ab0e301bd8069146e1e9c2e2cce53e1c3c81e37168e6dadad85702c0a` |
| `edition/code/tools/check_library.py` | 100 | `c47052910683fff26a448f854a55a5f1378346836b9a8c03cccadc373d794054` |
| `edition/docs/_quarto.yml` | 55 | `18e7c1e8241f38e6637a4ac5954f5cc0289ac0704af01e9dccefb906b0ef6192` |
| `edition/docs/index.qmd` | 260 | `f9f46a53c71d7cc87d4848ab9f79a3d10df73f3f3ef5c7cb6ff47b07b19105d8` |
| `edition/docs/notation.qmd` | 98 | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
