# Original independent scientific promotion review GPU1

**Verdict: PASS for the stated finite Torch backend addition. No required correction or unresolved correctness objection was found.** This conclusion concerns the exact frozen candidate and the limited claims below. It is not approval to integrate it, a new population theorem, a network-fidelity result, or a performance comparison.

Reviewer: fresh isolated agent `/root/review_circle1`, assigned report name GPU1. Date: 2026-09-16.

## Independence, inputs and integrity

I acted independently of every author/assembler and the selector named in the assignment. I received the neutral assignment and candidate pointer without inherited author research history. I did not read the study README, previous checks or reports, selector findings, another reviewer’s findings, other studies, live replacement sources, or Git history. No research findings arrived from another reviewer. I did not delegate any part of this review, edit the frozen sources, edit the live library, or use Git.

I read the required `solve-math-rigorously` skill completely at `/etc/codex/skills/solve-math-rigorously/SKILL.md` and applied it to the finite identities. No external theorem was needed to validate the new equations. The new material does not import an older population theorem to prove a stronger result, so I did not treat the surrounding book summaries as new proof obligations.

The edition is `data/generated/closure_endpoint_discrimination/promotion_20260916/candidate04`.

- Frozen manifest SHA256: `ae6caf4643cb10b109e98f58828541e44943153216f0ac09b1f22277054a06cc`.
- Neutral assignment SHA256: `d9652f6e2079f188a43e8503a0cb34a832064fbcc45381a81ecfa22a07352c46`.
- Packet SHA256: `227a476750b48eda2e0474f3be78d1a357df34bc5d1d42408e4303c74bfb4280`.

The manifest and assignment match the supplied expected hashes. I checked **every one of the manifest’s 65 file hashes before and after the work; both checks found zero mismatches**. Producer source and output hashes were independently recomputed and also matched. Newly generated review outputs live outside the source manifest.

All complete reads are listed below. I repaired the initially truncated combined guide output by rereading `docs/README.md` and its lines 370–585, and the small clipped portion of `code/README.md` by rereading lines 990–1045. No required source read remains truncated or missing.

| Complete source read | Lines read | SHA256 |
|---|---:|---|
| `AGENTS.md` | 1–62 | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `RESEARCH_WORKFLOW.md` | 1–225 | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `docs/README.md` | 1–738 | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/README.md` | 1–1236 | `3ccb617d05d3989b7a65f251e82143219dfddf69554124034e092d8f2f1f37b8` |
| `code/pde/__init__.py` | 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 1–363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_solver.py` | 1–350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/pde/observable_initialization.py` | 1–397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_words.py` | 1–217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/pde/observable_arithmetic.py` | 1–230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_fixed.py` | 1–223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_torch_circle.py` | 1–313 | `4fa63eb6abdd1c8573abfa1a7dc0a107d13ec669ae078659e8298cd517000430` |
| `code/tests/test_observable_torch_circle.py` | 1–137 | `437b9f577621d854afc62171c285129fe424e1eb3ef406b680d8ddd3a72a1181` |
| `code/scripts/validate_torch_circle.py` | 1–105 | `edb42a5bb72b28f96f484a54ddc2f65043329ab0c8539ff3aa415923f5a885e0` |
| `code/tools/check_library.py` | 1–100 | `4b0ec381caee28f8768ac7bc6e2d4af04e7860abdff73c75e7bc75af3067a018` |
| `code/tests/test_library_boundary.py` | 1–58 | `375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a` |

The complete `code/README.md`, both parts of the workflow, the complete notation contract, the complete theory guide, all new implementation/test/producer/checker lines, and all eight named implementation dependencies were read. The old finite-network and exact-moment bodies are included because package import reaches them.

**Generic-compiler exclusion:** orders 1 and 3 add no tail; order 5 adds codes 4 and 5, namely `sin(1)` and `cos(1)` on population 1. These add no action. The DAG traversal therefore sets `fast_core=True` for every admitted order. `initialize_features` reaches the generic import only in its opposite branch. An independent import guard that raises on any import of `pde.observable_compiler` allowed every admitted initialization to complete. Thus its body was not needed or read.

The precise unread scientific complement is reproduced at the end. Those files were hashed, and the structural checker scanned applicable Markdown/Python files, but neither action is a scientific reading or a whole-book audit. Historical empirical results appearing in the old guide were not re-reproduced or newly endorsed.

## Finite mathematical and initialization audit

The scope is exactly two-dimensional normalized directions `u=x/sqrt(2)`, two hidden tanh layers, orders 1/3/5, finite populations and finite laws, and detached float64 tensors on CPU or CUDA. The population nodes are quadrature rows, not neural widths. Imported states must carry the supported order and dictionary scheme, with the corresponding feature shapes. They need not be states reached by training; this makes the noninitial-state contract meaningful.

Writing `Pi_l=diag(pi_l)`, the forward action is

```text
T v = b2 M b1.T Pi1 v,
T* z = b1 M.T b2.T Pi2 z.
```

For arbitrary finite vectors, `z.T Pi2 T v = (T* z).T Pi1 v`. This identifies the implemented reverse map as the weighted adjoint of the same action; it does not introduce an independent random backward map.

For one input, set `h=tanh(w u)`, `a=b1.T Pi1 h`, `H=tanh(b2 M a)`, `f=sum_i pi2_i c_i H_i`, and `d=b2.T Pi2[c*(1-H^2)]`. Direct differentiation gives

```text
partial f / partial c_i = pi2_i H_i
partial f / partial w_j = pi1_j (1-h_j^2) (b1 M.T d)_j u
partial f / partial M_ij = d_i a_j.
```

Differentiating `L=sum_a rho_a(f_a-y_a)^2`, then cancelling the positive population metric weights, gives exactly the three documented velocities with factor `-2 rho_a(f_a-y_a)`. The data weights already supply the mean/mixture normalization; no additional batch factor or factor one-half is missing. The first-layer normalization is already in `u`.

Consequently the exact finite real-arithmetic vector field satisfies

```text
dL/dt = -sum_j pi1_j |w_dot_j|^2
        -sum_i pi2_i |c_dot_i|^2
        -||M_dot||_F^2.
```

At a zero-weight node the weighted metric is degenerate. Its stored coordinate velocity remains defined by the displayed formula, but its coordinate never contributes to fields, observations, or any positive-weight coordinate’s future evolution. Deleting such nodes is therefore observationally valid. I checked this explicitly for unequal populations and unequal weights. The finite comparison uses tolerances; the scratch record’s label `zero_weight_rows_omitted_exactly` describes the mathematical deletion identity, not bitwise equality of differently shaped matrix products.

The initialization audit found the following:

- The polynomial feature counts are `binom(p+4,4)` and `binom(p+2,2)`, giving (5,3), (35,10), and (126,21). The two retained constant tail words make the last actual dimensions (128,21).
- Both Gaussian directions and the reverse response term remain present. The lower joint tuple uses the same frozen `g` and reverse marks, with reverse core `sqrt(tau_core)*z + alpha*tanh(g)`. Population replay does not redraw each coordinate independently.
- The coefficient rule Q and population rule P are separate. The action contraction keeps both `upper_derivative @ beta.T` and `upper_pairing @ gamma.T`.
- For raw feature Grams `G_l`, `eta=1/[1024(p+1)^2]` is strictly positive. With `L_l L_l.T=G_l+eta I`, the row feature table is `raw_l L_l^{-T}` and the action is `L_2^{-1} C L_1^{-T}`. All required transposes are present. No singular direction or redundant constant is dropped.
- The operational state starts with `w=g`, `c=0`, `M=D`. Its zero readout is the population small-readout convention, not a claim that an actual finite network has identically zero random initial readout.
- Explicit resource-limit rejection remains delegated to the unchanged CPU initializer.

My independent reconstruction used NumPy’s Chebyshev polynomial evaluator and derivative routine, regenerated the raw coordinates, both contraction terms, the ridge matrices, and triangular solves. It did not call the initializer’s table evaluator or normalization routine. The largest absolute normalization discrepancy was `4.441e-16`, `3.775e-14`, and `2.478e-11` for orders 1, 3, and 5. These are finite-roundoff comparisons, not Gaussian quadrature accuracy or conditioning certificates.

The time integrator makes both first-stage and second-stage velocities from their respective complete states, then updates all moving blocks simultaneously. It is explicit Heun. The guide correctly avoids identifying it with an exact flow map or arbitrary discrete network GD, and supplies no unconditional step-stability or loss-decrease claim.

## API, observations, storage and arithmetic

I checked the complete nine-array state, mutable-state revalidation, float64/device checks, positive integer block/step counts, finite positive step size, unit input directions, valid probabilities, supported metadata tags and feature sizes. Decimal/rational CPU states and their portable checkpoints were independently confirmed to be rejected by the Torch import/load interface, rather than down-converted.

Factories and CPU transfers copy their arrays. Evolution initially copies all state arrays and metadata; stage sharing is internal to the new state only. I checked distinct tensor storage pointers for every returned array and mutation isolation of nested metadata. Public observation weights/inputs are cloned. The module import did not change the checked Torch thread count, default dtype or TF32 setting. A fresh process confirmed ordinary `import pde` does not import Torch.

The initial and current observations use the same marks: the first initial field uses `g`, and the second uses `g,D,b1,b2,pi1`. Their pair axes are (population row, input, initial/current). Pair probabilities are the product of the returned population and input weights. Grams, weighted activation RMS, paired displacement RMS and unhalved loss agree with independently reconstructed formulas at noninitial states. No observations are fed back into evolution.

The storage count is exactly

```text
P1*(K1+5) + P2*(K2+2) + 2*K1*K2
```

float64 entries, with `4m` additional law entries. I checked the count against `state_bytes` using unequal population sizes. Block field storage and contractions have the documented dependence on B, populations and feature counts. The moving output/stage arrays add a fixed number of `2P1+P2+K1K2` entries. Full observations intentionally use an entire input panel and produce two m-by-m Grams. Explicit pairs are optional and have the documented linear population-by-input storage. The implementation retains no growing sequence of states, source tape, observation history or absolute clock.

Nonfinite mutations in every state array were rejected before evaluation. Separate tests forced nonfinite velocities, observations and integration stages and confirmed rejection. The documented ordinary float64 arithmetic limitations remain real: saturation can erase derivatives, intermediate products can overflow or underflow, and detection of a nonfinite returned field/stage is not an interval bound on all intermediate operations. The candidate does not promise extreme-range robustness or correct rounding.

Checkpointing uses the existing exact float-hex format with all state and law arrays and metadata. Loading does not invoke initialization. Every tested same-device continuation reproduced all nine arrays bitwise, including independent noninitial and unequal-weight cases. Cross-device results are numerical comparisons, not a claim of bitwise cross-device reproducibility.

## Executed checks and retained evidence

All commands used the frozen edition as their working directory unless their full scratch path is shown. Define these path abbreviations only for this report:

```text
E=/home/amir/Codes/PDE/data/generated/closure_endpoint_discrimination/promotion_20260916/candidate04
S=/home/amir/Codes/PDE/data/generated/closure_endpoint_discrimination/promotion_20260916/review_gpu1_scratch
PY=/home/amir/miniconda3/bin/python
```

The deterministic suite commands were:

```sh
env PYTHONPATH=code CIRCLE_TEST_DEVICE=cpu CIRCLE_TEST_SCRATCH="$S/tests_cpu" PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "$PY" -B code/tests/test_observable_torch_circle.py
env PYTHONPATH=code CIRCLE_TEST_DEVICE=cuda:0 CIRCLE_TEST_SCRATCH="$S/tests_cuda" CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "$PY" -B code/tests/test_observable_torch_circle.py
```

CPU: **4 tests passed**, 0.440 seconds reported by unittest. The initial sandboxed CUDA attempt exited 1 with four setup failures because the device was invisible. Its complete original output is retained in `S/suite_results.json`. Repeating the identical CUDA command with the explicitly authorized GPU access passed **4 tests**, 1.011 seconds reported by unittest. This was an environment-access failure, not a suppressed numerical test failure.

The structural commands were:

```sh
env PYTHONDONTWRITEBYTECODE=1 TMPDIR="$S/boundary" "$PY" -B code/tests/test_library_boundary.py
env PYTHONDONTWRITEBYTECODE=1 "$PY" -B code/tools/check_library.py
```

All **5 boundary tests passed**; the standalone checker passed on **58 files**. Its allowlist contains the declared optional Torch/psutil dependencies and local scripts import root. This result verifies its structural scope, not mathematical correctness or proof completeness.

The actual fixed producers were:

```sh
env PYTHONDONTWRITEBYTECODE=1 "$PY" -B code/scripts/validate_torch_circle.py --device cpu --output data/established/review_gpu1_cpu_20260916
env PYTHONDONTWRITEBYTECODE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 "$PY" -B code/scripts/validate_torch_circle.py --device cuda:0 --output data/established/review_gpu1_cuda_20260916
```

The CUDA producer used authorized GPU access. Both used the unmodified recipe: orders 1,3,5, Q=64, P=32, four steps of 0.005, block size 2, the declared four angles/labels/weights, and a single numerical CPU thread. No parameter search, training campaign, external data, historical arrays or replacement configurations were used.

| Producer result | CPU | CUDA device 0 |
|---|---:|---:|
| Status | complete | complete |
| Validation work seconds | 0.113135 | 0.437736 |
| Peak process RSS bytes | 518,393,856 | 869,974,016 |
| Peak CUDA allocated bytes | n/a | 34,144,768 |
| Peak CUDA reserved bytes | n/a | 35,651,584 |
| Largest reference array discrepancy | 3.469447e-18 | 1.734723e-18 |
| Exact restart | all 3 orders | all 3 orders |

Retained state bytes are 4,080; 18,912; and 82,944 by order for both devices. The CUDA peak is below the declared one-GiB tensor limit; validation work is far below 120 seconds. The CPU initialization and transfer phase is included as documented. The timer excludes interpreter/import/device setup and hashing, so these values do not establish end-to-end speedup. The CUDA run is not faster for this deliberately tiny example.

Environment: Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130, CUDA runtime 13.0; GPU NVIDIA GeForce RTX 3090. CUDA runs supplied `CUBLAS_WORKSPACE_CONFIG=:4096:8`. The producer emitted a PyTorch deprecation warning about the legacy TF32 settings API; it did not cause a test or execution failure.

I independently checked every producer source and output hash and recomputed all six saved archives’ loss, both pair RMS values, both Grams and activation RMS from their stored arrays. These checks passed. As a defensive check, rerunning the producer with its existing CPU output path raised the expected `FileExistsError` before writing; the original outputs and hashes remained intact.

The independent attack commands were:

```sh
env PYTHONPATH="$E/code" PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "$PY" -B "$S/independent_attacks.py" --device cpu --output "$S/attacks_cpu"
env PYTHONPATH="$E/code" PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 "$PY" -B "$S/independent_attacks.py" --device cuda:0 --output "$S/attacks_cuda"
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "$PY" -B "$S/final_checks.py"
```

They all exited 0; the CUDA attack command used authorized GPU access. The third command records its subprocess commands in full, including the exact new guide example and the Torch-free ordinary import.

The independent state fixtures had P1=7 and P2=5, nonuniform population weights with a zero-weight row in each population, nonzero readout, separately randomized M and D, moved w relative to g, unequal law weights including zero, duplicated inputs, antipodal inputs, and all supported feature orders. The oracle explicitly formed the small dense population action `b2 @ M @ b1.T` only in the test, then differentiated its loss with Torch autograd. Production never forms this dense population matrix.

| Independent result, maximum over orders | CPU | CUDA device 0 |
|---|---:|---:|
| Weighted gradient discrepancy | 2.082e-17 | 1.735e-17 |
| Energy identity discrepancy | 4.337e-19 | 2.168e-19 |
| Central finite-difference energy discrepancy | 3.845e-12 | 3.845e-12 |
| Prediction discrepancy | 1.735e-17 | 1.908e-17 |
| Weighted adjoint discrepancy | 1.041e-17 | 1.735e-17 |
| Independently assembled Heun discrepancy | 0 | 0 |
| Pair discrepancy | 1.596e-16 | 1.388e-16 |
| Gram discrepancy | 9.541e-18 | 1.128e-17 |

Additional attacks covered block sizes 1/2/3/larger-than-panel, actual zero-row deletion, mutated metadata and feature shapes, attached autograd state, float32 rejection, all-zero and negative weights, unsupported orders, invalid directions and integer arguments, nonfinite step sizes, initializer limits, unsupported Decimal/rational transfers and loads, source-dispatch guarding, array and metadata ownership, and exact continuation from saved noninitial states.

Evidence under S:

- `hashes_before.json`, `hashes_after.json`, `read_coverage.json`;
- `suite_results.json`, preserving CPU success, sandbox CUDA failure and CUDA success;
- `additional_results.json`, preserving producer/checker/independent-attack outputs and warnings;
- `independent_attacks.py`, `attacks_cpu/record.json`, `attacks_cuda/record.json`, and their saved checkpoints;
- `final_checks.py`, `final_checks.json`, containing the archive reanalysis and expected overwrite refusal.

Producer records and archives are inside the edition at `data/established/review_gpu1_cpu_20260916/` and `data/established/review_gpu1_cuda_20260916/`. Their `record.json` files contain complete configuration, environment, phase records and source/output hashes.

## Component verdicts and limitations

| Component | Verdict |
|---|---|
| Complete frozen coverage and isolation | PASS |
| Supported range and finite mathematical equations | PASS |
| Core dispatch, feature retention, response, ridge and transpose | PASS |
| Weighted gradients, loss clock, energy and noninitial states | PASS |
| CPU and CUDA finite implementation parity | PASS |
| Blocking, ownership, validation and fixed storage | PASS |
| Pairs, Grams, activation/displacement RMS | PASS |
| Float64 handling and explicit rejection of other arithmetic | PASS |
| Same-device exact own-state continuation | PASS |
| Maintained producer and independent archive checks | PASS |
| Structural library boundary and standalone example | PASS |
| Claim calibration and documented limitations | PASS |

**Required corrections:** none.

**Unresolved correctness objections:** none within the assigned scope.

**Optional suggestion:** when dropping support for older Torch versions, consider replacing the producer’s legacy TF32 setters with the supported version’s current API to remove the observed deprecation warning. This is future maintenance; the present float64 calculations passed and require no precision-policy correction.

The tests establish implementation and operational behavior at the declared finite sizes. They do not bound the distance to a continuous flow, an exact Gaussian population closure, or trained finite networks. They do not prove population convergence, useful order monotonicity, conditioning guarantees, whole-circle error, long-horizon reliability, a target-resolution rule, a settled endpoint, or speedup. Those claims are expressly absent from the new section. The separate integration review and user-approval gates remain outside this scientific reviewer’s authority.

## Exact older unread scientific complement

The following frozen files were not scientifically read in this review. Their hashes are covered by the unchanged manifest. This explicit complement prevents the complete guide and import-chain read from being mistaken for a whole-library proof audit.

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

This is the original full report of reviewer GPU1. No findings from any other reviewer were used to create or revise it.

