# Independent complete scientific promotion review A6

**Verdict: PASS for the stated frozen-v4 finite scope. No necessary correction or unresolved blocking objection found.** This is a scientific/code review, not promotion approval or the separate integration/placement review.

Reviewer: `/root/review_a6`, a fresh isolated context, distinct from the named authors, assembler, coordinator and selector. Date: 2026-09-16. The reviewed manifest SHA256 is `b8292d5e4fe22b8855d03aee87b3dc3ccbd937b4c31e15a569959b7838e0b363`.

## Scope and isolation

Inputs were the neutral assignment, manifest, their immutable `frozen_v4` packet and applicable packet skill/process instructions. I did not read the study README/history, previous reports or verdicts, another reviewer, other studies, live scientific files, chats or Git history. I did not delegate reading or testing. Writes were confined to this report and `data/generated/first_order_dimension_mnist/review_a6_v4/`. No frozen input was changed; every manifest hash was checked before and after execution. The external assignment is byte-identical to its hashed frozen copy.

The object reviewed is bias-free two-hidden tanh, stored independent Gaussian variances `(1,1/n,1/n²)`, input rows `U=x/sqrt(d)`, unhalved probability-weighted squared loss, block mobilities `(n,1,n)`, and physical time. Closure order p, population rule count P, width n, dimension d and sample count m remain separate. The positive results here concern exact initialized coefficient identities, a specified finite vector field, a sign-paired finite integration rule, its tensor implementation, actual finite-network comparison and array diagnostics. They establish no general-d trained-network convergence, fixed-order accuracy, rotation invariance, MNIST/PCA result, cost-to-accuracy bound or speed ratio.

I applied the frozen `solve-math-rigorously` and `investigate-conjectures` skills, including research-contract, adversarial-audit, decisive-experiments and evidence-ledger references. This was not a new conjecture search or a research campaign.

## Complete read coverage

I read every line of `docs/observable_p1.md` (332), `dependencies/global_nonlinear_source_units.md` (393), `docs/NOTATION.md` (98), and `code/GENERAL_P1.md` (235). The source units include the complete supplied Section 2, Sections 3.1–3.4 source/response proof and elementary dependencies, H3.1 contraction proof, and H3.N1/N2 definitions and equations. No circle trained-flow theorem is needed by this addition.

I read the complete unchanged original docs guide (738 lines) and code guide (1113 lines). Byte-prefix comparison established that the proposed `docs/README.md` and `code/README.md` consist of those exact complete originals plus four lines each; I read both complete appended differences. Thus all proposed guide lines were covered without treating summaries as substitutes for omitted text. The old guides were context, not a fresh proof audit of their other chapters or old empirical results.

I read all lines of all eleven supplied Python modules: `__init__.py` (26), `finite_network.py` (363), `gaussian_moments.py` (114), `observable_initialization.py` (397), `observable_words.py` (217), `observable_arithmetic.py` (230), `observable_fixed.py` (223), `observable_p1_initialization.py` (181), `observable_torch_p1.py` (403), `finite_torch.py` (153), and `closure_comparison.py` (226). I also read the complete maintained tests (380), producer (131) and analyzer (46), rather than relying on outputs. All instruction bodies used were read completely. An initial combined instruction read was truncated around the promotion rules; the affected workflow range 155–225 was reread in full. Scientific/code reads were complete.

Unread complement: placement and assembly bodies (`PROMOTION_PLACEMENT.md`, `PROMOTION_assemble.py`) were hash-only as authorized; the two skill agent YAML files and proof-search-orchestration reference were hash-only and not invoked. All other non-packet repository and scientific material was outside scope. The absent generic compiler is not a missing first-order dependency: dictionary order 1 contains only the displayed core and codes 0/1, and its core execution was independently tested with a compiler callable that would fail immediately if used.

## Scientific and implementation audit

| Component | Finding and verdict |
|---|---|
| Source reuse and general-d coefficients | **PASS.** The independent coordinate construction repeats the finite Gaussian calculation at fixed d. The reversed field contains `alpha*h`, with independent innovation variance tau; sampling G and R independently would be wrong. The supplied proof justifies the bounded smooth finite program and singular Gaussian integration by parts. For `F=k_i`, both `alpha*beta` and `tau*gamma` remain in the raw action contraction. The constant and cross-coordinate blocks vanish by joint sign symmetry and independence, not empirical diagonal projection. |
| Ridge and normalization | **PASS.** Cauchy–Schwarz gives beta²≤vs, hence the displayed lower Schur complement is at least eta+s*eta/(v+eta)>0. Multiplication by the inverse lower factor on the left and inverse transposed lower factor on the right yields the stated second band `alpha*beta*eta/(v+eta)+tau*gamma`. Feature table orientation agrees with the dense Cholesky oracle. The scalar coefficient target and the old finite-Q full-Gram normalization are explicitly different. |
| Numerical initialization | **PASS within declared floating limitations.** The three child random streams separate lower roots, reverse innovations and upper roots while preserving the lower joint tuple. No empirical Gram, trained path, neural-width parameter or old array enters. The positive scalar/tensor rule, cutoff normalization, coarse/fine diagnostic and immutable scalar cache agree with the guide. The omitted-tail probability is correctly not sold as a nonlinear coefficient certificate. |
| Folding and observations | **PASS.** Odd marks/current w,c and zero constant row/column form an invariant finite-rule class. Hidden activations and reverse q are odd; gates are even; coefficient pairings are even. Thus every velocity and simultaneous stage preserves the representation for arbitrary data/labels. The base-half probabilities represent both signs, and the observation method explicitly restores `(initial,current)` pairs at both signs with half weights. Dense perturbed moving M is allowed. No claim is made for an arbitrary unfolded state outside this class. |
| Closure field, Heun and energy | **PASS.** Direct differentiation gives `df/dw_i=pi1_i*gate1_i*q_i*u`, `df/dc_j=pi2_j*h2_j`, and `df/dM=upsilon*a.T`. All factors 2 and sample probabilities are present. M and its actual transpose are reused. The weighted energy identity remains true at zero population weights by multiplication, without division. Both Heun stages evaluate every block from one common state. Association/block changes alter rounding only. |
| Actual finite network | **PASS.** Initialization retains the small random readout, unlike closure c=0. Draw order and scales were checked against independently regenerated RNG arrays. Full middle state and transpose are retained. Multiplying ordinary loss gradients by `(n,1,n)` gives the implemented first/readout velocities and middle factor `2/n`. Canonical NumPy and independent autograd checks agree. |
| Ownership, restart and cost | **PASS.** Constructors/data preparation copy arrays; standard mutation is detected, while deliberate PyTorch version bypass is explicitly forbidden by contract. Frozen caches and recorded arithmetic policy are checked. Archives preserve current/frozen state, data and representation; same-environment continuation is exact without rerunning initialization. Entry counts agree with both symbolic formulas; workspace and retained-history exclusions are stated. |
| Comparison semantics | **PASS.** Ordered unique IDs are required; prediction, seed-pair and Gram paths reject tested integer mismatches. Constants, zero references, exact zero error, missing classes, signed zero prediction and within-class metrics have explicit meanings. Scaled norms/means avoid ordinary underflow/overflow traps; subnormal and unresolved range cases are disclosed and tested. Training-loss selection never receives passive predictions, refuses extrapolation and handles nonmonotone losses with earliest ties and bracket indices. |
| Maintained producer/analyzer | **PASS for operation/replay.** Producer starts from the declared initializer, records limits before work, uses fresh outputs, includes random finite readout, and hashes source/output inputs. CUDA phases synchronize. Analyzer independently rebuilds NumPy predictions and activation Grams from saved state, verifies output hashes and compares repeat arrays exactly. These checks do not make the finite closure an accurate network approximation. |

## Executed evidence and limits

The pre-run record is [PRECOMMIT.md](/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a6_v4/PRECOMMIT.md). Fixed recipes only; 120 seconds per subprocess, 600 seconds aggregate command wall allowance, one numerical thread, allocated `cuda:1`, 15% device allocator cap, `CUBLAS_WORKSPACE_CONFIG=:4096:8`. No exploratory grid, dataset campaign or old generated array was used. Failed output was retained.

All exact commands, environments, cwd, exit statuses and measured wall times are in [commands.jsonl](/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a6_v4/commands.jsonl). The supervisor [run_check.py](/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a6_v4/run_check.py) enforces the per-process timeout and aggregate allowance. Commands used `/home/amir/miniconda3/bin/python -B`, cwd equal to the frozen root, and `PYTHONPATH=<frozen_root>/code`, so no live scientific module was imported.

- CPU maintained suite: all 16 tests pass. GPU suite: initial sandbox run failed before tests with “No CUDA GPUs are available”; the authorized device-access rerun ran all 16 tests successfully on `cuda:1`. This environmental failure was not counted as CUDA validation.
- Two fresh producer runs per device used the maintained defaults `d=3,m=9,n=P=16,seed=101`, folded antithetic population, 10 Heun steps of .005, float64, block size 4. Each device's analyzer found exact repeat arrays. NumPy replay maximum absolute error: CPU `2.220446049250313e-16`, GPU `1.1102230246251565e-16`.
- Comparing every saved CPU/GPU observation/state/input array at absolute tolerance 2e-12 and relative tolerance 2e-11 passed; largest absolute difference was `2.220446049250313e-16`. This is tolerance agreement, not cross-device bitwise equivalence.
- The maintained suites exercise dense moving states, unequal populations/features, d=1/2/7, nontrivial folding, same-state restart, input zeros/duplicates/nonunit lengths, data zeros, invalid inputs/mutation, all gradient blocks, both matrix associations, simultaneous Heun, energy, float32 evolution and saturation. Float32 checks use absolute 3e-6 and relative 3e-4 tolerances after 12 steps, not an arbitrary-horizon certificate.
- Independent seed-606 checks used `P1=5,P2=7,K1=4,K2=3,d=2,m=6`, zero population and sample weights, dense nonzero readout/matrix, duplicate and zero inputs. Multiplication-form gradient errors were at most `5.551115123125783e-17`; the energy residual was `5.551115123125783e-17`. Constructor copy ownership, coefficient-cache return ownership, exact retained counts (552 unfolded and 252 folded scalar entries for d=3,P=16), direct RNG initialization, and all new guide Python examples passed.
- The first-order old initializer ran with a trap `raw_compiler`; it completed through `tanh-core-bounded-contractions` and recorded no source regularizer use. No unsupported compiler branch was imported.
- A targeted ID coercion attack compared distinct allowed integer arrays `int64([9007199254740992])` and `uint64([9007199254740993])`. All three comparison wrappers correctly rejected them in NumPy 1.26.4; this suspected objection did not survive execution.

Independent details are in [independent_results.json](/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a6_v4/independent_results.json), with original executable checks beside it. Replay results are [cpu_analysis.json](/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a6_v4/cpu_analysis.json) and [gpu_analysis.json](/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a6_v4/gpu_analysis.json). Final integrity and cross-device results are [final_checks.json](/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a6_v4/final_checks.json).

Environment: Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130; actual GPU NVIDIA GeForce RTX 3090. GPU producer A recorded 33,610,752 peak allocated bytes and 35,651,584 peak reserved bytes; retained closure/network tensor counts were 2,016/5,120 bytes. These are whole-process peaks with both systems present, not isolated speed/memory benchmarks. Torch emitted a future TF32-policy API deprecation warning; it did not invalidate current checks.

## Remaining limitations and completion

No scientific dependencies needed for the stated first-order addition were missing. No necessary correction remains. Ordinary rounding, saturation cancellation, underflow, intermediate overflow, unproved quadrature error, independent finite populations, finite-width randomness and finite time-step error remain exactly the limitations stated in the candidate. Nothing here certifies arbitrary floating inputs, all devices/versions, numerical global stability, trained-network identification or whole-domain accuracy from finite panels.

The complete mandatory scientific/code audit and bounded CPU/actual-GPU execution are finished. Integration correspondence, placement and preservation remain the separately assigned review; user approval remains a separate promotion gate.

## Input hashes and command summary

The following appendix is generated directly from the inspected manifest and retained command records; it supplies all input hashes rather than relying on a claimed packet label.

Total supervised subprocess wall time, including the failed sandbox attempt: 15.580779 seconds.

| Command record | Exit | Wall seconds |
|---|---:|---:|
| cpu_suite | 0 | 1.787283 |
| gpu_suite | 1 | 1.622285 |
| gpu_suite_access | 0 | 2.607451 |
| cpu_producer_a | 0 | 1.541732 |
| cpu_producer_b | 0 | 1.646713 |
| cpu_analyzer | 0 | 0.158278 |
| gpu_producer_a | 0 | 2.138980 |
| gpu_producer_b | 0 | 2.049284 |
| gpu_analyzer | 0 | 0.146344 |
| independent_checks | 0 | 1.726882 |
| final_checks | 0 | 0.155547 |

External manifest SHA256: `b8292d5e4fe22b8855d03aee87b3dc3ccbd937b4c31e15a569959b7838e0b363`. External assignment SHA256: `841e1d470d3328f74c7554bee987c214168c8f9a6e7b7370099b7e4da4797c3e`.

| Frozen relative input | SHA256 |
|---|---|
| `PROMOTION_PLACEMENT.md` | `b3ca29eb03eaacf95b7b06410bf50bdb8141d2ca343881ce33fc9d34b3a26db6` |
| `PROMOTION_REVIEW_ASSIGNMENT.md` | `841e1d470d3328f74c7554bee987c214168c8f9a6e7b7370099b7e4da4797c3e` |
| `PROMOTION_assemble.py` | `9afd22e391e517a741a12b3c1752732acc8c8efe0c3d0e692b9f5241bca16bf2` |
| `code/GENERAL_P1.md` | `97709c4e525e05f57cb42e250be13d3e1f9c9f8788aeaf280623f8d89b771a47` |
| `code/README.md` | `ff5a89effef3fc1bc86a2bcc699453731c50bebffd9fd5ff0844f690717dc237` |
| `code/pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/closure_comparison.py` | `f715624c7d81116fd24d888ab5bce1afc3e8b353406b23553e6a6ff8b4f0a89e` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_torch.py` | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `code/pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_arithmetic.py` | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_fixed.py` | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_initialization.py` | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_p1_initialization.py` | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `code/pde/observable_torch_p1.py` | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `code/pde/observable_words.py` | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/scripts/analyze_general_p1.py` | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| `code/scripts/example_general_p1.py` | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| `code/tests/test_general_p1.py` | `99de6d99818d022002e432021f0e86f14b263c382ea6caedb2f4c7351ecafb03` |
| `dependencies/global_nonlinear_source_units.md` | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |
| `dependencies/original_code_README.md` | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `dependencies/original_docs_README.md` | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `instructions/AGENTS.md` | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `instructions/RESEARCH_WORKFLOW.md` | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `instructions/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `instructions/investigate-conjectures/agents/openai.yaml` | `ba8e39aba0463d706c4fa49375b90d0b9ce4d0ce436875e6d35ca61bcf387d02` |
| `instructions/investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `instructions/investigate-conjectures/references/decisive-experiments.md` | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| `instructions/investigate-conjectures/references/evidence-ledger.md` | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `instructions/investigate-conjectures/references/proof-search-orchestration.md` | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
| `instructions/investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `instructions/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `instructions/solve-math-rigorously/agents/openai.yaml` | `13e1679d378e917628b9f7d58c687e78e0442df8b6ad9089a4720a87f6bb3d1c` |
