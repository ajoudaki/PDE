# Independent scientific promotion review A5 — frozen_v4

**Verdict: PASS for the submitted scientific and finite implementation scope.**
I found no necessary correction or unresolved correctness objection. This is
an independent review of this frozen candidate, not promotion approval, a
placement/integration review, a general-dimensional trained-network theorem,
or certification of numerical approximation accuracy.

Reviewer: `/root/review_a5`, fresh isolated context, distinct from the listed
authors, assembler and selector. Review date: 2026-09-16. The neutral assignment
and manifest were the only research entry points. I did not read study history,
README, prior reports/verdicts, other reviewers, other studies, live scientific
files, or the assembled edition. No scientific reading or checking was delegated.
Supervisor messages supplied scope, resource allocation, and a request to avoid
optional work; they supplied no findings. Git metadata was checked only for
write safety (HEAD `04b61a12795734cbfc93830bf0a164bab7d101c4`; no staged paths).
Writes were limited to this report and the assigned scratch directory.

## Input boundary and complete reading

Frozen root:
`/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v4`.
Scratch/evidence root:
`/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a5_v4`.

I read all scientific content of the nine proposed additions: the entire theory,
initializer, closure engine, network comparator, comparison module, tests,
producer, analyzer and general-p1 guide. I also read the complete supplied
Gaussian proof/dependency unit, NOTATION, `__init__.py`, `finite_network.py`,
`gaussian_moments.py`, and all four supplied older observable modules
(`observable_initialization`, `observable_words`, `observable_arithmetic`,
`observable_fixed`). There are no missing scientific or runtime dependencies
for this p=1 scope.

The complete original docs guide (738 lines) and original code guide (1113
lines) were read in contiguous, nontruncated ranges. Exact file comparison
verified that the candidate guides consist of those complete original contents
plus four appended lines each; I read both complete appended sections. Thus
all 742 and 1117 candidate guide lines are covered without rereading duplicate
content. The old whole-book summaries were contextual, not evidence certifying
the separate theorems they describe. An initially truncated combined read was
repaired by complete separate reads of the theory and dependency unit; the
earlier skill references and NOTATION were visible in full.

Required process reading covered the frozen AGENTS and complete workflow
(including all of Part 2), `solve-math-rigorously/SKILL.md`,
`investigate-conjectures/SKILL.md`, and its adversarial-audit and bounded-experiment
references. The latter two governed the claim separation and precommitted checks.
No new conjecture, research-state recovery, or multi-route search was performed.

The hash table below records exact line counts and read status. **F** means
complete content read; **D** means complete guide content covered by verified
identical original prefix plus read append; **H** means hash-only. The unread
complement is precisely the H files: placement/assembly metadata (assigned to
integration review), skill UI metadata, and nonapplicable skill references.
No scientific proof, implementation, test, or recipe needed here is in that
unread complement. The larger book and generic compiler are outside this
packet; the latter is not invoked by the first-order branch.

## Scientific audit and component verdicts

| Component | Independent audit and conclusion |
|---|---|
| Model and scope | PASS. The same bias-free two-hidden tanh convention is retained: U=x/sqrt(d), stored variances (1,1/n,1/n²), unhalved weighted loss, mobilities (n,1,n), physical time. Closure order p, integration P, width n, dimension d and sample count m are separate. Finite random readout and zero population readout are correctly distinguished. |
| Gaussian source and initialization | PASS. I followed the conditional projection, empirical induction, Stein identity and singular-Gram argument in the complete dependency bodies. Their finite smooth-program hypotheses apply to the tanh core. Forward sources have covariance vI, reverse innovation covariance tau I, and the same-action response is alpha h. Lower G and R are jointly sampled; neither the reverse response nor cross-population independence is lost. |
| Coefficients and normalization | PASS. Odd parity and independent coordinate pairs give the stated full block Grams. The contraction has alpha v and alpha beta+tau gamma bands. Solving the lower Cholesky transform on the right as L1^(-T) gives the stated residual band alpha beta eta/(v+eta)+tau gamma. The ridge lower bound follows from beta²<=vs and ensures a positive second pivot. Production uses only scalar/two-variable quadrature, not empirical Gram diagonalization. |
| Older d=2 correspondence | PASS. The actual dictionary ordering is constant, h1,h2,k1,k2 and constant,H1,H2. Codes 0,1 add no tails. All action dependencies are the core. I read both dispatch branches and executed p=1 with a deliberately failing injected generic compiler: it was never called. The older finite-Q full-Gram normalization is correctly distinguished from population-block normalization. |
| Folding | PASS. I independently checked that simultaneous mark negation makes w,c and nonconstant features odd, a0 and upsilon0 zero, and all retained pairings even. The full middle velocity keeps the constant row/column zero. The argument permits arbitrary data directions and labels and preserves dense nonconstant M. Maintained checks exercise perturbed nonzero c and dense M through several Heun steps, not merely initialization. Signed observations restore both signs and half weights. |
| Closure equations | PASS. Differentiating the finite predictor gives pi1_i gate1_i q_i u, pi2_j h2_j, and upsilon aᵀ. All loss factors, transposes and population weights agree. The direct, optimized and precontracted associations evaluate these contractions without intermediate block updates. All Heun blocks use the same state at each stage. The weighted dissipation identity remains valid at zero population weights without dividing by them. |
| Actual network comparator | PASS. The NumPy initializer draws W1, W2/sqrt(n), c/n in layer order and Torch copies them. The independent NumPy forward/backward implementation and autograd check the factors: first/readout velocities cancel the output 1/n through their mobility; the middle velocity retains 1/n. It retains the complete n-by-n middle matrix and its transpose. |
| Observations, ownership and restart | PASS. Initial/current pairing uses the same frozen marks and input; upper initialization is reconstructed from g,D. Grams are uncentered and cross Grams order initial rows/current columns. Owned arrays, frozen caches, version checks, state validation and copied observations match the documented contract. Pickle-free restart retains the entire fixed/current representation and arithmetic metadata. Exact continuation was tested on each device. Deliberate version-tracking bypass is explicitly outside the immutability contract. |
| Comparison methods | PASS. Ordered unique IDs are required; constant, zero-reference, absent-class, sign and seed-pair semantics are explicit. I checked scaled norms, exponent combination, centered correlation, mean formation, rejection of unrepresentable diagnostics and wrappers. Training-loss matching sees no passive predictions, refuses extrapolation, handles nonmonotone losses and earliest-time ties, and exposes the attained brackets. |
| Producer and analyzer | PASS. Both were read line by line. The producer runs complete fixed initializations and simultaneous updates, writes source/environment/output provenance, and reports phase timing and process-level memory honestly. The analyzer hashes outputs, independently reconstructs predictions/Grams using NumPy, recomputes metrics and checks exact repeated arrays. Four fresh producer runs and both analyzers passed. No previous generated arrays were consumed. |
| Cost and numerical claims | PASS within stated limits. Counting every frozen/cache/current tensor gives the published counts; independently checked d=3,P=16 counts are 552 unfolded and 252 folded scalars. RHS workspace is bounded by input blocking and a fixed number of state copies; saved observations are additional. O(Pd²) precontraction construction and O(Pd) output storage are distinguished. Neither a uniform joint-(d,n) advantage nor cost-to-accuracy claim is inferred. |

## Executed evidence

Before numerical work, `preregistered_limits.json` fixed: no campaign; fixed tiny
recipes; at most 120 seconds per subprocess and 600 aggregate wall seconds;
one numerical thread; allocated `cuda:0`; CUDA allocator fraction 0.15;
`CUBLAS_WORKSPACE_CONFIG=:4096:8`; no grids or post-outcome parameter searches.
The independent script fixed seed 20260916 and its finite-difference threshold
before execution. The suite and example retain their own fixed seeds and
tolerances. Every launched numerical command, exact argument list, working
directory, timeout, exit code and wall time is in `commands.json`; full stdout
and stderr are retained in separate logs.

Interpreter: `/home/amir/miniconda3/bin/python`, Python 3.10.14, NumPy 1.26.4,
Torch 2.9.0+cu130. Actual GPU: NVIDIA GeForce RTX 3090, cuda:0. The suite and
producer use one Torch thread, TF32 disabled, highest float32 matmul precision,
and deterministic algorithms. All commands used the frozen `code` import path,
disabled bytecode writes, single-thread BLAS/OpenMP, and assigned scratch TMPDIR.

The exact maintained commands are reproduced by the retained `run_checks.py`
with `cpu` or `gpu`. It invokes the frozen `code/tests/test_general_p1.py`,
then `code/scripts/example_general_p1.py` twice into distinct fresh directories,
then `code/scripts/analyze_general_p1.py` with `--run`, `--repeat` and a fresh
analysis output. Each command ran with the frozen packet as working directory.
The custom command was the same interpreter with `-B independent_checks.py`.

| Check | Actual outcome |
|---|---|
| CPU maintained suite | 16/16 pass, 0.297 s suite time; 1.821 s subprocess wall. |
| Initial sandbox CUDA invocation | Failed before tests: `No CUDA GPUs are available`. Preserved in `gpu_suite.log`; it is an environment failure, not CUDA evidence. |
| CUDA suite with approved device access | 16/16 pass on cuda:0, 0.920 s suite time; 2.699 s subprocess wall. |
| CPU example A/B and analyzer | All exit 0; independently replayed predictions/Grams have maximum absolute discrepancy 2.220446049250313e-16; every repeated observation/state array exactly equal. |
| CUDA example A/B and analyzer | All exit 0; NumPy replay maximum discrepancy 1.1102230246251565e-16; every repeated observation/state array exactly equal. |
| Zero population weights | For unequal P1=3,P2=5,K1=4,K2=2, d=3, dense moving states, zero/duplicate inputs and zero data/population weights: maximum gradient-metric error 2.220446049250313e-16; energy error 4.440892098500626e-16; centered directional loss difference error 3.0819435892226466e-10, below 2e-8. |
| Additional ownership/cache checks | Constructor-source edits and observation edits do not affect prediction. Both cached transpose mutations are rejected. |
| p=1 core dispatch and finite-rule distinction | Injected compiler was not called; metadata marks source regularization unused. Q=64 older initialization differs from the new coefficient target by 0.06649101764758317 in max-entry D, consistent with the explicitly different finite rules, not an accuracy estimate. |
| Tensor count check | Exact agreement: 552 unfolded and 252 folded retained scalar entries at d=3,P=16. |

Maintained checks include dense Cholesky verification in d=1,2,7,17; independent
samplewise NumPy RHS and simultaneous Heun; autograd and energy; unequal feature
and population dimensions; block/association changes; actual finite-network
initialization and NumPy oracle; perturbed folding and signed law; exact
own-state restart; CPU/CUDA float32-versus-float64 controls; saturation; domain,
mutation and probability failures; and tiny/large/subnormal comparison cases.

Aggregate numerical subprocess wall time, including the failed sandbox CUDA
attempt, was **15.36652821302414 s**, below 600 s. No subprocess approached 120 s.
The CUDA example A measured peak allocated/reserved device memory
33,610,752/35,651,584 bytes; its process peak RSS was 920,657,920 bytes.
CPU example A peak RSS was 517,267,456 bytes. Both examples retained 2016
closure tensor bytes and 5120 network tensor bytes. These tiny operation counts
and timings do not constitute a speed or accuracy benchmark.

## Objections, limits and completion

Necessary corrections: **none**. Unresolved correctness objections within this
submission: **none**. There was no external-source or generic-compiler dependency
gap for the claimed identities and finite first-order implementation.

The scientific claims remain narrow: quadrature refinement is diagnostic,
not a certified coefficient error; sampling, quadrature, time integration,
precision, closure order and finite network width are distinct axes. No general-d
trained-network convergence, MNIST/PCA result, fixed-order rotation invariance,
global step stability, pure clock equivalence, or cost-to-accuracy theorem was
established by this review. Float32 saturation cancellation, intermediate
overflow, underflow, device/reduction dependence and immutable-tensor contractual
limits are disclosed. GPU coverage is this actual device/environment and these
fixed tiny cases. Exact repeat is within each device, not cross-device equality.
The original guides' other algorithms and empirical studies were not rerun.

All required scientific reading and bounded validation are complete. Final
rehashing matched every manifest entry and the manifest's launch digest. No
frozen inputs changed. This original report and its scratch evidence can be
used as one complete scientific review of these identical inputs; separate
integration review and user approval remain outside my assigned scope.

## SHA256 input inventory

Manifest SHA256:
`b8292d5e4fe22b8855d03aee87b3dc3ccbd937b4c31e15a569959b7838e0b363`.
The external neutral assignment SHA256 is
`841e1d470d3328f74c7554bee987c214168c8f9a6e7b7370099b7e4da4797c3e`,
identical to its frozen copy. `input_hashes.json` retains the complete machine-readable
inventory. The following table is generated directly from independently recomputed
hashes, checked against the manifest; F/D/H meanings are defined above.

| File | Lines | Read | SHA256 |
|---|---:|:---:|---|
| `PROMOTION_PLACEMENT.md` | 27 | H | `b3ca29eb03eaacf95b7b06410bf50bdb8141d2ca343881ce33fc9d34b3a26db6` |
| `PROMOTION_REVIEW_ASSIGNMENT.md` | 62 | F | `841e1d470d3328f74c7554bee987c214168c8f9a6e7b7370099b7e4da4797c3e` |
| `PROMOTION_assemble.py` | 38 | H | `9afd22e391e517a741a12b3c1752732acc8c8efe0c3d0e692b9f5241bca16bf2` |
| `code/GENERAL_P1.md` | 235 | F | `97709c4e525e05f57cb42e250be13d3e1f9c9f8788aeaf280623f8d89b771a47` |
| `code/README.md` | 1117 | D | `ff5a89effef3fc1bc86a2bcc699453731c50bebffd9fd5ff0844f690717dc237` |
| `code/pde/__init__.py` | 26 | F | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/closure_comparison.py` | 226 | F | `f715624c7d81116fd24d888ab5bce1afc3e8b353406b23553e6a6ff8b4f0a89e` |
| `code/pde/finite_network.py` | 363 | F | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_torch.py` | 153 | F | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `code/pde/gaussian_moments.py` | 114 | F | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_arithmetic.py` | 230 | F | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_fixed.py` | 223 | F | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_initialization.py` | 397 | F | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_p1_initialization.py` | 181 | F | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `code/pde/observable_torch_p1.py` | 403 | F | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `code/pde/observable_words.py` | 217 | F | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/scripts/analyze_general_p1.py` | 46 | F | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| `code/scripts/example_general_p1.py` | 131 | F | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| `code/tests/test_general_p1.py` | 380 | F | `99de6d99818d022002e432021f0e86f14b263c382ea6caedb2f4c7351ecafb03` |
| `dependencies/global_nonlinear_source_units.md` | 393 | F | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |
| `dependencies/original_code_README.md` | 1113 | F | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `dependencies/original_docs_README.md` | 738 | F | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | 98 | F | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | 742 | D | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `docs/observable_p1.md` | 332 | F | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `instructions/AGENTS.md` | 62 | F | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `instructions/RESEARCH_WORKFLOW.md` | 225 | F | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `instructions/investigate-conjectures/SKILL.md` | 185 | F | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `instructions/investigate-conjectures/agents/openai.yaml` | 11 | H | `ba8e39aba0463d706c4fa49375b90d0b9ce4d0ce436875e6d35ca61bcf387d02` |
| `instructions/investigate-conjectures/references/adversarial-audit.md` | 121 | F | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `instructions/investigate-conjectures/references/decisive-experiments.md` | 141 | F | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| `instructions/investigate-conjectures/references/evidence-ledger.md` | 157 | H | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `instructions/investigate-conjectures/references/proof-search-orchestration.md` | 97 | H | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
| `instructions/investigate-conjectures/references/research-contract.md` | 99 | H | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `instructions/solve-math-rigorously/SKILL.md` | 115 | F | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `instructions/solve-math-rigorously/agents/openai.yaml` | 12 | H | `13e1679d378e917628b9f7d58c687e78e0442df8b6ad9089a4720a87f6bb3d1c` |

Generated evidence is indexed by `evidence_hashes.json` in the assigned scratch. It includes both producer records/archives per device, both analyses, every command log (including the initial CUDA failure), the precommitted limits, original independent-check source and complete coverage/hash records. These outputs were generated during this review and are not scientific input dependencies.
