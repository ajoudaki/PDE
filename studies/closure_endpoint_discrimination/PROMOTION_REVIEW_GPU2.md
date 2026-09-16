# Independent scientific promotion review — candidate04 — reviewer GPU2

**Verdict: PASS for the proposed finite float64 CPU/CUDA circle backend and its bounded operational recipe. No required corrections or unresolved correctness objections.** This is one independent scientific review, not promotion approval, integration review, or a new population/network convergence theorem.

Review identity: `/root/review_circle2`, 2026-09-16. Candidate root: `data/generated/closure_endpoint_discrimination/promotion_20260916/candidate04`. Reviewer scratch: `data/generated/closure_endpoint_discrimination/review_gpu2`. Original full report: this file.

## Isolation, input identity and coverage

I received only the neutral assignment, packet pointer, frozen candidate, and supervisor instruction to use CUDA:1. I am distinct from the named authors/assemblers and selector. I did not read author notes, study README/history, selector reports, earlier reviews, other reviewers' findings, live replacement code/docs, other studies, chats, or Git history. I did not fetch scientific inputs from outside this packet. I used `/etc/codex/skills/solve-math-rigorously/SKILL.md` for proof checking. No source changes, Git operations, additional research campaign, or parameter search were performed. My writes are this assigned report, reviewer-owned scratch, and the expressly assigned fresh producer outputs inside the frozen edition's `data/established/`.

The neutral assignment's SHA256 is `d9652f6e2079f188a43e8503a0cb34a832064fbcc45381a81ecfa22a07352c46`; the packet pointer SHA256 is `227a476750b48eda2e0474f3be78d1a357df34bc5d1d42408e4303c74bfb4280`. The frozen manifest SHA256 is **`ae6caf4643cb10b109e98f58828541e44943153216f0ac09b1f22277054a06cc`**. I recomputed all **65** listed file hashes before scientific checks and after the producer/tests; every file matched both times. The producer's own source hashes also matched that manifest. The manifest fixes the exact edition, including context files that I did not scientifically reread.

I read every line of the assignment and packet, new implementation, new tests, new producer, the entire `code/README.md` (not only the added section), checker and checker tests. I also read every line of all required older implementation dependencies and the supplied complete instructions, notation contract and theory reading guide. An aggregate tool response truncated part of `docs/NOTATION.md`; I repaired that read by separately reading the complete file. The complete read inventory, with line counts and hashes, is appended below. No remaining read was truncated.

The new guide section is `code/README.md:1115–1236`. Older guide material was read as context; its historical empirical results and theorem summaries are not newly recertified by this review. I did not audit older chapter proof bodies. The full unread complement is appended explicitly. Hashing and the structural checker's scans do not count as scientific reading of that complement.

The generic `observable_compiler.py` implementation is unnecessary to this restricted promotion: `build_dictionary(1/3/5).fast_core` is true; orders 1 and 3 add no tails, while order 5 adds only codes 4 and 5, `sin(1)` and `cos(1)` on population 1. I verified this both from the complete dictionary/dispatch implementation and by supplying an exception-raising `raw_compiler` to initialization for each supported order: it was never called. No unsupported generic-branch theorem is imported into the new claims.

## Scientific and implementation audit

### Finite equations, loss, transpose and metric — PASS

The implemented shapes consistently use normalized directions `u=x/sqrt(2)` in dimension two, lower/upper population rows P1/P2, and retained feature dimensions K1/K2. These rows are integration points, not a hidden neural width. The API's initialized and imported order range is precisely p=1,3,5, and the supported float64 tensor/state contract is checked before evaluation.

For one input, write `h_j=tanh(w_j·u)`, `a=b1.T diag(pi1)h`, `H_i=tanh((b2 M a)_i)`, `f=sum_i pi2_i c_i H_i`, `d=b2.T[pi2*c*(1-H²)]`, and `q=b1 M.T d`. Direct differentiation gives

- `partial f / partial c_i = pi2_i H_i`;
- `partial f / partial M_kl = d_k a_l`;
- `partial f / partial w_j = pi1_j (1-h_j²) q_j u`.

Multiplying by `2 rho_a (f_a-y_a)` and summing inputs gives the ordinary Euclidean derivatives of the unhalved weighted squared loss. Cancelling positive population weights against the corresponding weighted metric gives exactly the three documented velocities. Consequently

`dL/dt = -sum_j pi1_j ||w_dot_j||² - sum_i pi2_i c_dot_i² - ||M_dot||_F²`.

Zero-weight coordinates have zero ordinary loss derivatives; the weighted form is degenerate on those coordinates, which can be omitted. The retained formulas choose their extensions without changing any positive-weight field or trajectory. My tests explicitly deleted zero-weight nodes and checked predictions and all active velocity blocks. This supports the guide's stated interpretation; I am not assuming an invertible metric at zero-weight coordinates.

The same matrix and its genuine transpose occur in the two orientations. No independent random backward map, whitening, extra width normalization, halved loss, frozen first layer, or replacement residual enters the implementation. Independent broadcast-sum autograd and a separate scalar-loop loss oracle verify the derivatives and energy on arbitrary noninitial states at all three orders, with unequal populations, nonuniform weights, zero-weight nodes, duplicate inputs and antipodal inputs.

### Initialization and numerical scope — PASS

The polynomial feature counts are `binomial(p+4,4)` and `binomial(p+2,2)`: (5,3), (35,10), (126,21). Order 5 retains its two syntactically distinct constant tails, giving (128,21), without rank pruning. The initialization coefficient rule Q and replay rule P remain separate. The full joint lower marks use `(g, sqrt(tau)*z + alpha*tanh(g))`; replay retains these correlations rather than drawing each feature independently. The upper marks use the matching two-coordinate Gaussian rule.

I independently rebuilt the Chebyshev values and derivatives using NumPy polynomial evaluation, reconstructed both response-contraction terms, the Q-node Grams, ridge `1/[1024(p+1)^2]`, inverse lower Cholesky factors, and the P-node feature tables. All three orders agreed with the candidate producer within `2e-10`. This check separately verifies the response contribution and all normalization transposes. The strict positive ridge retains redundant directions; Cholesky failure is surfaced rather than repaired by deleting a mode.

The backend calls the unchanged CPU initializer, transfers owned float64 values, and retains initialized `w=g`, `c=0`, `M=D`. Its zero initial readout is explicitly a population convention, not an assertion that a finite random readout was literally zero. Decimal and rational CPU states, and their portable archives, are rejected by the Torch import path. CPU and CUDA transfer preserve working float values in the supported range. The module imports do not set global Torch policy, and ordinary `import pde` does not import Torch; I checked both in clean subprocesses.

The floating limitations are correctly bounded. The code uses ordinary products and `1-tanh²`; saturation, cancellation, underflow and intermediate overflow remain possible. It is not a correct-rounding or extreme-range implementation. I forced nonfinite fields/velocities, overflowing loss evaluation and a nonfinite Heun stage; the tested paths rejected these results. I did not infer universal detection of every lost intermediate from these checks.

### Heun, ownership, storage, observations and restart — PASS

`evolve` performs two evaluations at simultaneous states followed by the explicit Heun combination. I reconstructed a full one-step update independently from the public RHS and checked every moving block. The original state stays unchanged. The returned state owns copies of all original frozen/current arrays and deep-copied metadata; internal stage sharing is private and does not accumulate with elapsed steps. There is no trajectory list, source tape, absolute clock, or observation history in the retained state.

Counting the nine arrays gives precisely

`P1*(K1+5) + P2*(K2+2) + 2*K1*K2`

float64 entries. Data have four entries per input node. I checked the formula against `state_bytes` for unequal populations and against the supplied producer records. The RHS field workspace and contraction work match the guide's block dependence, with a fixed number of moving arrays for Heun. Full-panel fields/Grams and explicitly requested pairs are documented separately. Input validation and stored state are additional fixed-resolution costs; `state_bytes` is not a total memory measurement.

Initial/current pairs use the same population marks, with initial hidden fields reconstructed from frozen `g,D`. The pair axis is initial then current, and the product of population/input weights gives the pair law. Independent scalar-loop fields reproduce all pairs, weighted Grams, activation RMS, displacement RMS, loss and predictions. Blocking changes reduction order, not the finite mathematical equations. Calls with/without retained pairs agree on RMS.

The portable restart includes all nine arrays, the three finite data arrays and metadata. I checked exact encoding/decoding and exact subsequent evolution at all three orders, on CPU and on CUDA:1 separately. Loading uses no initializer. Same-device, same-block, same-step continuation passed bitwise. No cross-device bitwise claim is inferred; cross-backend comparisons use tolerances. The caller must retain physical time and step schedule, as the guide states.

### Structural boundary and bounded producer — PASS

The checker remains a structural file/import/link check. Declaring `torch`, `psutil` and `scripts` in its allowlist is consistent with this packet's optional backend and existing supervisors. The complete five-test checker fixture suite passed; the edition checker passed over 58 eligible source/Markdown files. This is not evidence for mathematical correctness of unread chapters.

The producer fixes Q=64, P=32, four Heun steps of .005, the four recorded directions/labels/weights, block size two, and orders 1,3,5. It starts from its initializer, writes independent observations and checkpoints, compares its final arrays with the CPU reference, and verifies exact own-state restart. The wall alarm begins after imports/device setup/source hashing, as the guide explicitly explains. The tiny fixed allocations and measured CUDA peak satisfy its tensor allowance. The allowance is not a hard process-RSS reservation; CPU/GPU context and allocator reservation are reported separately. No accuracy, speedup, settled endpoint or trained-network fidelity conclusion is promoted from these examples.

Both actual producer runs completed. I independently checked all output hashes and all reported source hashes, then recomputed saved loss, displacement RMS, activation RMS and Grams from the saved pair arrays and weights. Repeating the command with an existing output directory raised `FileExistsError` and left every output hash unchanged.

## Actual commands and results

All code commands below ran from the frozen candidate root with `/home/amir/miniconda3/bin/python`, Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130 and CUDA runtime 13.0. The GPU was CUDA:1, NVIDIA GeForce RTX 3090, per the supervisor's explicit allocation; the neutral recipe's example CUDA:0 was not this reviewer's device. Numerical thread settings were `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1`; Python bytecode writes were disabled. CUDA runs additionally set `CUBLAS_WORKSPACE_CONFIG=:4096:8`.

The exact suite command, run once with each `CIRCLE_TEST_DEVICE=cpu` and `CIRCLE_TEST_DEVICE=cuda:1`, was:

```sh
env PYTHONPATH=code CIRCLE_TEST_DEVICE=cpu CIRCLE_TEST_SCRATCH=/home/amir/Codes/PDE/data/generated/closure_endpoint_discrimination/review_gpu2 PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B code/tests/test_observable_torch_circle.py
```

CPU: four tests passed in 0.437 s. CUDA:1: four tests passed in 0.914 s. The initial sandboxed CUDA attempt failed all four setup checks because CUDA was unavailable inside the sandbox; this is preserved in `suite_cuda1_sandbox.log`. The expressly authorized escalation exposed the GPU and passed. No candidate change occurred between these attempts.

The independent attack command, run with `--device cpu` and `--device cuda:1` under the same environment, was:

```sh
/home/amir/miniconda3/bin/python -B /home/amir/Codes/PDE/data/generated/closure_endpoint_discrimination/review_gpu2/independent_attacks.py --device cpu --scratch /home/amir/Codes/PDE/data/generated/closure_endpoint_discrimination/review_gpu2
```

Both passed. The script uses fixed seeds `90311+p`, populations 7 and 5, all three supported feature counts, and six predeclared directions. The largest absolute error of the scalar-loop central energy derivative was `3.459e-11` (central step `2e-5`); the declared comparison tolerance was `3e-8`. Weighted autograd/equation comparisons used `3e-12`; independent initializer reconstruction used `2e-10`. The script also exercised invalid imported tags, float32/requires-grad tensors, mass/sign errors, NaN/Inf states, invalid steps/block sizes/shapes/directions, the nonfinite arithmetic cases above, higher-precision import/archive rejection, factory ownership and the exact guide example. Full checks and actual metrics are retained in `independent_cpu.json`, `independent_cuda.json`, and their logs.

Producer commands were:

```sh
env PYTHONDONTWRITEBYTECODE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 /home/amir/miniconda3/bin/python -B code/scripts/validate_torch_circle.py --device cpu --output data/established/review_gpu2_cpu
env PYTHONDONTWRITEBYTECODE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 /home/amir/miniconda3/bin/python -B code/scripts/validate_torch_circle.py --device cuda:1 --output data/established/review_gpu2_cuda1
```

| Device | Status/orders | Validation work seconds | Maximum reference array discrepancy | Exact restarts | Process peak RSS bytes | CUDA allocated/reserved peak bytes |
|---|---|---:|---:|---|---:|---|
| CPU | complete / 1,3,5 | 0.0849352591 | 3.46944695195e-18 | all three | 518606848 | not applicable |
| CUDA:1 | complete / 1,3,5 | 0.4207521081 | 1.73472347598e-18 | all three | 870268928 | 34144768 / 35651584 |

Retained state bytes were 4080, 18912 and 82944 at orders 1,3,5 on both devices. These phase timings are operational records, not a speed comparison. The producer emitted Torch's deprecation warning for the older TF32 settings API; execution and float64 results passed.

Additional commands:

```sh
env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/home/amir/Codes/PDE/data/generated/closure_endpoint_discrimination/review_gpu2 /home/amir/miniconda3/bin/python -B code/tests/test_library_boundary.py
env PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python -B code/tools/check_library.py
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B /home/amir/Codes/PDE/data/generated/closure_endpoint_discrimination/review_gpu2/final_checks.py
```

All returned zero. The final-check script also performs the two deliberate existing-output refusal subprocesses, clean import/global-setting checks, producer-array recomputation and final frozen hash verification. The two refusal subprocesses each returned one as expected; their full errors are preserved. No scientific test failed. All logs are under the reviewer scratch path, and producer JSON/NPZ outputs are under the two edition-local `data/established/review_gpu2_*` paths.

## Required corrections, suggestions and limits

**Required corrections: none. Unresolved correctness objections within the assigned new scope: none. Missing inputs: none.**

Optional maintenance suggestion only: update the opt-in producer's TF32-setting calls when the supported Torch version policy is revised, since this tested runtime emits a deprecation warning. It does not affect these float64 calculations, and the library itself changes no global settings. This suggestion is not a condition of acceptance.

The review proves/checks finite equations and implementation contracts. Tests do not certify finite-rule accuracy against an exact flow, quadrature error, uniform whole-circle/time error, monotone order convergence, a practical tolerance selector, population convergence, or finite-network fidelity. Older theorems keep their exact separate law/horizon/limit-order hypotheses. I did not use historical timing/result claims as evidence for this new addition. A separate independent integration review and concrete user approval are still required by the supplied workflow before promotion.

## Complete read inventory and exact unread complement

All line ranges below are complete files, from line 1 through the stated count.

| Frozen path | Lines read | SHA256 |
|---|---:|---|
| `AGENTS.md` | 62 | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `RESEARCH_WORKFLOW.md` | 225 | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `docs/README.md` | 738 | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/README.md` | 1236 | `3ccb617d05d3989b7a65f251e82143219dfddf69554124034e092d8f2f1f37b8` |
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_torch_circle.py` | 313 | `4fa63eb6abdd1c8573abfa1a7dc0a107d13ec669ae078659e8298cd517000430` |
| `code/tests/test_observable_torch_circle.py` | 137 | `437b9f577621d854afc62171c285129fe424e1eb3ef406b680d8ddd3a72a1181` |
| `code/scripts/validate_torch_circle.py` | 105 | `edb42a5bb72b28f96f484a54ddc2f65043329ab0c8539ff3aa415923f5a885e0` |
| `code/tools/check_library.py` | 100 | `4b0ec381caee28f8768ac7bc6e2d4af04e7860abdff73c75e7bc75af3067a018` |
| `code/tests/test_library_boundary.py` | 58 | `375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a` |

The remaining frozen manifest entries were **not scientifically read**:

- `code/pde/exact_calculus.py`
- `code/pde/finite_jets.py`
- `code/pde/finite_reductions.py`
- `code/pde/observable_closure.py`
- `code/pde/observable_compiler.py`
- `code/pde/observable_laws.py`
- `code/scripts/analyze_observable_horizon.py`
- `code/scripts/analyze_observable_solver.py`
- `code/scripts/run_observable_validation.py`
- `code/scripts/validate_observable_horizon.py`
- `code/scripts/validate_observable_solver.py`
- `code/tests/test_book_exporter.py`
- `code/tests/test_exact_calculus.py`
- `code/tests/test_finite_jets.py`
- `code/tests/test_finite_network.py`
- `code/tests/test_finite_reductions.py`
- `code/tests/test_gaussian_moments.py`
- `code/tests/test_numerical_contract.py`
- `code/tests/test_observable_closure.py`
- `code/tests/test_observable_compiler.py`
- `code/tests/test_observable_horizon_analysis.py`
- `code/tests/test_observable_horizon_validation.py`
- `code/tests/test_observable_initialization.py`
- `code/tests/test_observable_laws.py`
- `code/tests/test_observable_solver.py`
- `code/tests/test_observable_validation.py`
- `code/tools/book_pdf/README.md`
- `code/tools/book_pdf/build-pdf.sh`
- `code/tools/book_pdf/export_book.py`
- `code/tools/book_pdf/layout.tex`
- `code/tools/book_pdf/render_book.py`
- `code/tools/two_layer_risk/README.md`
- `code/tools/two_layer_risk/angle_error_bound.py`
- `code/tools/two_layer_risk/certificate.py`
- `code/tools/two_layer_risk/certificate_kernel.cpp`
- `code/tools/two_layer_risk/check_driver.py`
- `code/tools/two_layer_risk/check_kernel.py`
- `code/validation/observable_horizon_plan.json`
- `code/validation/observable_solver_plan.json`
- `docs/arctan_limits.md`
- `docs/continuous_depth.md`
- `docs/finite_dynamics.md`
- `docs/finite_optimization_and_controls.md`
- `docs/gaussian_calculus.md`
- `docs/global_nonlinear.md`
- `docs/linear_dynamics.md`
- `docs/special_data_limits.md`

Reviewer-owned executable evidence hashes:

- `data/generated/closure_endpoint_discrimination/review_gpu2/independent_attacks.py`: `38c7f484a6d60f38ef278e5412ee1de4577609d267376ca5cd9af2a46e31365d`.
- `data/generated/closure_endpoint_discrimination/review_gpu2/final_checks.py`: `2e01f3215a14053ab433a20376d0a29210f39f9d0862d65c4dafd7f32488f341`.
- `data/generated/closure_endpoint_discrimination/review_gpu2/independent_cpu.json`: `ad2ac651f7a42494192331dff696651b25750e5bb777e8600515d73df84edb2c`.
- `data/generated/closure_endpoint_discrimination/review_gpu2/independent_cuda.json`: `75e1275fed92acbea58cf815ee14f36db5e589a4b6d9e97864f2f1f0ee01c01a`.
- `data/generated/closure_endpoint_discrimination/review_gpu2/final_checks.json`: `aa0533d43e6a1862bc3661b28959a9d97a3f907667988a26c93409490c5ad10f`.

Completion attestation: the required complete scientific/code/recipe/dependency read scope, independent adversarial checks, CPU and allocated CUDA execution, fresh bounded producer runs, artifact checks, and final frozen-source hash verification are complete. This file is the original full report; the candidate was not repaired or edited.
