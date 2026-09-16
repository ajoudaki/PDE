# Independent complete scientific review A3 — frozen_v3

Reviewer: `/root/review_a3`, freshly launched isolated context. Date: 2026-09-16.
Candidate manifest SHA256: `c150f99336f891c6f38c8485b58c3ba0f1971123da142240e85b267108867de0`.
Frozen root: `/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v3`.
Own scratch: `/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a3_v3`.

## Verdict

**HOLD: one required software-contract correction, R1 below.** The comparison
helpers can report relative error zero for distinct finite arrays when their
squared norms underflow. In particular, they violate the stated zero-reference,
nonzero-error null semantics. This is localized to the comparison API; it does
not invalidate the initialized coefficient identities, the sign-folding proof,
the finite vector field, or the network comparator.

The complete required scientific material was read. All 36 frozen manifest
entries matched their declared hashes, before and after verification. All 13
maintained tests passed on CPU and cuda:1. Independent finite checks passed,
and two fresh producer runs on each device passed the maintained NumPy analyzer
with exact repeat-array agreement. Those successes do not close R1. A corrected
candidate needs the workflow's two fresh complete scientific reviews; this
report is not promotion approval.

## Scope, isolation, and read completion

The scientific object reviewed is bias-free two-hidden tanh, stored Gaussian
variances `(1,1/n,1/n²)`, output `cᵀh2/n`, rows `U=x/sqrt(d)`, unhalved weighted
squared loss, endpoint/middle mobilities `(n,1,n)`, and physical time. Closure
order `p=1`, population count `P`, width `n`, input dimension `d`, and input
count `m` remain distinct. The scope is exact initialized coefficient identities,
finite-rule antithetic folding, explicit finite equations and their implementation,
actual-network comparison, and generic prediction/Gram comparison methods.

I read every line of the following frozen scientific/code inputs, including
all comments, function bodies, proof bodies, examples, and reproduction recipes:

- `docs/observable_p1.md`, `docs/NOTATION.md`, and complete `docs/README.md`.
- `code/GENERAL_P1.md` and complete `code/README.md`.
- `code/pde/observable_p1_initialization.py`, `observable_torch_p1.py`,
  `finite_torch.py`, and `closure_comparison.py`.
- `code/tests/test_general_p1.py`, `code/scripts/example_general_p1.py`, and
  `code/scripts/analyze_general_p1.py`.
- All three unchanged runtime dependencies: `code/pde/__init__.py`,
  `finite_network.py`, and `gaussian_moments.py`.
- The complete supplied `observable_initialization.py`, `observable_words.py`,
  `observable_arithmetic.py`, and `observable_fixed.py` definitions supporting
  the first-order dictionary, dispatch, and finite-rule distinction.
- `dependencies/global_nonlinear_source_units.md` in full: the complete supplied
  Sections 2 and 3, including conditional projection, source-response induction,
  and singular-Gram argument; the full H3.1 contraction proof; and H3.N1/N2.
- Both full original guides. A byte-content comparison verified that each
  `dependencies/original_*_README.md` is precisely the corresponding fully read
  proposed guide with its final four added lines removed. Thus all original-guide
  content was read through the identical prefix, not inferred from a summary.

I read the neutral assignment, manifest, frozen AGENTS, the full supplied
research workflow (including Part 2), and both required skill bodies. Applicable
investigate-conjectures references read completely were research-contract,
adversarial-audit, decisive-experiments, and evidence-ledger. An initially
truncated combined instruction read was repaired with smaller complete reads;
scientific files were read in complete, nontruncated chunks. The hash/line-count
table below gives exact file-level coverage.

Unread complement: no study README/history, author or selector report, previous
review, other reviewer's findings, other study, old generated numerical array,
or unassigned live scientific file was read. The wider book and implementations
mentioned only as context in the guides were not re-audited or fetched. The
generic source compiler is not in this packet and is not a first-order proof or
runtime dependency: both static control-flow inspection and an executed injected
failure hook verified this. No general-d trained-network limit, higher-order
general-d convergence, MNIST/PCA conclusion, or speed/accuracy benchmark was
reviewed as a positive claim.

Placement and assembly files were hash-verified but deliberately not read.
The supervisor explicitly confirmed this isolation choice: placement/preservation
are assigned to a separate fresh integration review. Unused skill agent YAML
files and the proof-search-orchestration reference were hash-verified only;
there was no delegated multi-route proof search. No necessary scientific input
was missing for the limited candidate claim.

All outputs are my assigned report or my own generated namespace. I did not
edit candidate code, live established material, Git/index, or another reviewer’s
scratch. I did not delegate any part of the required complete review. No
scientific outcome was supplied to me in advance.

## Required correction R1: false zero relative errors after underflow

Locations: `code/pde/closure_comparison.py:33–43` and `:96–99`; the documented
comparison semantics are in `code/GENERAL_P1.md` under “Comparison semantics.”

The code computes RMS by squaring unscaled entries and uses a *computed* zero
RMS/norm to decide exact zero-reference/zero-error semantics. The Frobenius
routine similarly uses unscaled `np.linalg.norm`. With the packet's NumPy
1.26.4, the following accepted, finite inputs reproduce the defect:

```python
kw = dict(ids=[1, 2], reference_ids=[1, 2])
prediction_metrics([1e-200, 0], [0, 0], **kw)
# rms=0.0, relative_rms=0.0, max_absolute=1e-200, sign_disagreements=1

prediction_metrics([2e-200, 4e-200], [1e-200, 2e-200], **kw)
# rms=0.0, relative_rms=0.0, correlation=None

gram_metrics([[1e-200, 0], [0, 0]], [[0, 0], [0, 0]], **kw)
# frobenius=0.0, relative_frobenius=0.0, rms_entry=0.0,
# max_absolute=1e-200
```

In the first case the RMS is `1e-200/sqrt(2)`, a representable nonzero float,
and the relative error must be null for the documented zero-reference case.
In the second case candidate is exactly twice reference, so relative RMS is
one and correlation is one. The implementation instead reports a perfect zero
relative error. In the Gram case the Frobenius error is `1e-200`, the entry RMS
is `5e-201`, and the zero-reference relative value should be null. All are
representable; it is the intermediate square that underflows. The retained
evidence is `tiny_comparison_attack.log` in my scratch.

This is a scoped numerical/API correction, not an argument that every ordinary
floating operation must be exact or that the tensor backend must support all
extreme ranges. The guide's tensor derivative/loss caveats do not establish a
comparison-domain restriction or justify mapping an undefined ratio to the
explicit “identical zero arrays” sentinel. The nonzero-reference example also
has order-one relative-error distortion, despite tiny absolute entries.

Required disposition: distinguish actual zero arrays/errors from unresolved
computed norms, and either compute these diagnostics with suitable scaling or
explicitly reject an unsupported/unresolved norm regime. The zero-reference,
nonzero-error case must retain its documented null value. State any remaining
supported-range limitations. Add regression checks for tiny nonzero errors,
zero references, proportional tiny vectors, and analogous Gram inputs. Check
the shared `_metrics` path through within-class and seed-pair results as well.
No correction was applied during this review.

## Mathematical and algorithmic audit

### Initialized joint laws and coefficients — passes for stated scope

The finite Gaussian program has finitely many queries and uses only tanh and
linear operations at this order. Its roots have all finite moments and its
coordinate maps have bounded first derivatives, so the supplied source-rule
hypotheses apply. Independence of the coordinate roots gives
`E[h_i h_j]=v δ_ij`, hence forward source covariance `v I`. The upper tanh
fields have second moment `tau` and expected source derivative `alpha=1-tau`.
The reverse reuse therefore gives `R_i=sqrt(tau) Z_i+alpha h_i` jointly with
`G_i`; the innovation variance is the full `tau`, not a response-subtracted
variance. The implementation retains precisely that within-lower tuple and
uses a separate upper stream. Upper/lower population indices are not coupled.

Oddness under simultaneous `(G_i,Z_i)` negation and independence across
coordinate pairs give the displayed raw Gram blocks. Appending `A0 F` yields
the two contractions in H3.1: forward regression/Stein produces `alpha v`
for `F=h_i`, while `F=k_i` contributes both `alpha beta` and `tau gamma`.
The bounded functions/derivatives justify the Gaussian integration by parts,
and an independent centered residual, including a zero-variance residual,
has zero pairing with the upper feature. No trajectory or future coefficient
is used in this calculation.

For normalization, `beta²<=v s` gives
`b²=s+eta-beta²/(v+eta)>=eta+s eta/(v+eta)>0`.
The block `L_kh=beta/a` yields the normalized lower feature
`(k-beta h/(v+eta))/b`. Right multiplication by `L1^{-T}` then subtracts
`alpha v beta/(v+eta)` from `alpha beta+tau gamma`; the residual is exactly
`alpha beta eta/(v+eta)+tau gamma`. This independently confirms the right
transpose and both displayed nonzero bands of D. Only initial D has this
structure; the equations and code evolve every entry of M.

At d=2, graded descending-lexicographic total degrees zero and one yield
`1,h1,h2,k1,k2` and `1,H1,H2`. Codes 0/1 decode to already-present constants.
All action dependencies lie in the four core actions. The older finite Halton
rule computes its empirical full Grams and therefore is not identical to the
new exact-expectation target at finite Q. This distinction is correctly stated.
The executed injected compiler hook confirms that p=1 does not enter a missing
generic branch.

The working coefficient rule is a normalized truncated-normal Legendre rule,
with scalar/two-dimensional integration independent of d. Its refinement
difference and omitted scalar mass are explicitly diagnostics, not coefficient
certificates. The documented separate cutoff/quadrature/population axes are
necessary and are retained. Independent whole-Gaussian Hermite checks support
the finite default calculation but do not add a numerical-limit theorem.

### Folding and signed observations — passes

The sign-invariant class has odd nonconstant frozen features, odd w and c,
and zero constant row/column of M. For arbitrary data, h1/h2 and q remain odd,
gates remain even, and the feature pairings determining a and upsilon are
even; their constant entries vanish. The velocities preserve these parities
and the zero constant matrix row/column. Simultaneous Euler/Heun stages and
linear interpolation preserve the same linear constraints in real arithmetic.
This needs paired population marks, not a symmetric data law.

Folding is equality of one chosen antithetic integration rule, not equality
to P iid sampling. A dense moving M is essential and is retained. The folded
observation API explicitly restores both signs and halves base weights, so
it returns the signed initial/current joint law rather than just even moments.
Independent nonuniform-weight tests with zero population weights and unequal
feature dimensions verified this at nontrivial moving states.

### Finite vector field, gradients, and Heun — passes

For a supplied finite law, differentiating the actual scalar prediction gives
`partial_(w_i) f=pi1_i gate1_i q_i u`,
`partial_(c_j) f=pi2_j h2_j`, and `partial_M f=upsilon aᵀ`.
The factor `2 mu r` from the unhalved loss gives precisely the displayed
velocities after the population-L2/Frobenius metric. Multiplication, without
division by zero probabilities, proves the energy identity even with zero
weights. Independent autograd checks were accordingly made in the form
`grad_w=-pi1*v_w`, `grad_c=-pi2*v_c`, `grad_M=-v_M`.

Matrix dimensions and orientations are consistent for independent P1/P2 and
K1/K2. Every batch block uses the same state. Each Heun stage evaluates all
three velocities from one common state; there is no sequential within-stage
parameter update. Reference/optimized associations compute the same exact sums
while allowing ordinary reduction differences. Zero, nonunit and repeated
data rows do not invoke Gram inversion or normalization. No finite-step
loss-decrease or global numerical-stability conclusion follows or is claimed.

### Actual-network comparator — passes

The constructor calls the complete canonical finite initializer, which draws
first weights, middle matrix, then readout at the stated variances and retains
the random finite readout. Direct differentiation of `cᵀh2/n` and multiplication
by mobilities `(n,1,n)` gives the implemented endpoint velocities with factor
`-2` and middle velocity with factor `-2/n`. The full stored middle matrix and
its actual transpose are used. The canonical NumPy oracle is independently
implemented; its saturation derivative protection differs from Torch's
`1-tanh²`, and the candidate correctly disclaims that stronger range behavior.
The maintained uniform-law oracle and independent nonuniform-law autograd
checks both pass. Equal seed integers are not presented as a probabilistic
coupling between this finite network and the closure.

### State, ownership, caches, restart, and cost — passes with stated limits

Construction and prepared data copy user arrays; moving states are explicitly
mutable and revalidated. Version/identity checks reject ordinary frozen-cache
and prepared-data mutations; intentional `.data`/NumPy-view bypass is excluded
by the stated contract. Coefficient caches contain immutable scalar pairs and
return fresh dictionaries. The full w/c/M, frozen marks/D/probabilities, data,
representation and arithmetic metadata suffice to resume; no initialization
program or historical trajectory is needed. Exact working restart was checked
on each device in both float32 and float64 under one reduction environment.
No cross-device/version bitwise claim was inferred.

Counting moving and frozen/cache tensors gives the claimed unfolded total
`P(8d+7)+2(d+1)(2d+1)` and folded total `8Bd+3B+4d²`.
Independent executable counts agree. These are tensor-entry counts, not process
RSS, and do not deduplicate shared transpose storage. Heun needs a bounded
number of states; blocked activations and optional full-panel observations have
the stated additional costs. Saved observation histories grow separately.
The direct and precontracted work estimates preserve the d dependence and do
not assert a uniform advantage as both d and n grow.

### Comparisons and producer/analyzer — scoped pass except R1

Unique ordered IDs are checked before image/Gram comparisons. I attacked
reordered/duplicate IDs and mixed signed/unsigned large integer identity; the
last attack also rejected genuinely distinct IDs and revealed no defect.
Ordinary-scale zero/constant/absent-class cases, including decimal constants,
pass; exact constant detection avoids relying on rounded centering. All seed
pairs remain descriptive. Training-loss matching receives only training times,
losses and target, rejects extrapolation, and chooses earliest-time ties with
both attained brackets. It therefore does not select checkpoints by passive
prediction agreement. These semantics are distinct from equal physical time.

The producer was read fully, including initialization, input validation,
training, observation, checkpointing, source/output hashes, timing boundaries,
resource-limit handling, and failure records. The analyzer was also read fully:
it verifies saved-output hashes and independently reconstructs predictions and
current Grams from saved raw states with NumPy before checking repeated arrays.
Fresh d=3,m=9,n=P=16 runs completed on each device without archived inputs.
The recipe demonstrates finite operation only. Its visibly nonzero
closure/network discrepancies are not recast as a successful approximation
or a speed ratio.

## Executed checks and evidence

All substantive Python verification used `/home/amir/miniconda3/bin/python -B`.
The working directory was my scratch. For the commands below, `F` is the frozen
root and `S` is my scratch root defined above. Every run used:

```sh
TMPDIR="$S/tmp"
PYTHONPATH="$F/code"
PYTHONDONTWRITEBYTECODE=1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
CUBLAS_WORKSPACE_CONFIG=:4096:8
```

These names abbreviate the actual absolute environment values in the executed
commands. CUDA executions used the supervisor-allocated `cuda:1` with tool
escalation, not a CPU-only inference of GPU support.

| Executed operation | Outcome and retained evidence |
|---|---|
| `PDE_TEST_DEVICE=cpu timeout 300 python -B "$F/code/tests/test_general_p1.py"` | Exit 0; 13 tests, 0.311 s test-body time; `cpu_tests.log`. |
| `PDE_TEST_DEVICE=cuda:1 timeout 600 python -B "$F/code/tests/test_general_p1.py"` | Exit 0; 13 tests, 0.871 s; `cuda_tests.log`. |
| `timeout 150 python -B "$F/code/scripts/example_general_p1.py" --output "$S/cpu_run_a" --device cpu` and a separate `cpu_run_b` invocation | Both exit 0; fresh records, arrays, checkpoints and logs. |
| The same two producer invocations with `cuda_run_a`, `cuda_run_b`, `--device cuda:1` | Both exit 0; fresh records and logs. |
| `timeout 120 python -B "$F/code/scripts/analyze_general_p1.py" --run cpu_run_a --repeat cpu_run_b --output cpu_analysis.json` | Exit 0; exact repeat arrays; replay max error `2.220446049250313e-16`. |
| Same analyzer for CUDA runs, output `cuda_analysis.json` | Exit 0; exact repeat arrays; replay max error `1.1102230246251565e-16`. |
| `timeout 120 python -B independent_checks.py --device cpu --output independent_cpu_v2.json` | Exit 0; complete independent checks and per-check results in JSON/log. |
| Same independent checks, `--device cuda:1 --output independent_cuda.json` | Exit 0; complete CUDA checks and results. |
| Both literal Python blocks from `GENERAL_P1.md`, executed in order via a shared namespace | Exit 0; `guide_and_import.log`; NumPy-only `import pde` also verified before Torch import. |
| Exact finite tiny-array counterexamples above | All three accepted with false-zero metrics; `tiny_comparison_attack.log`; R1. |
| Large mixed signed/unsigned integer ID mismatch | Correct rejection; `integer_id_attack.log`. |

Independent checks use fixed seed 90210 and small nondegenerate supplied
states. At P1=5,P2=8,K1=4,K2=3,d=2,m=6 with nonuniform and zero weights, the
samplewise NumPy RHS maximum discrepancy was `2.7755575615628914e-17` on both
devices. Energy was approximately `-0.022856308640359698`; a centered loss
directional difference with step `1e-6` differed by about `1.093e-11`.
Independent lower/upper permutations preserved predictions and the permuted
velocities. Weighted folding used four base marks, K1=5,K2=2,d=3, dense nonzero
states, seven arbitrary inputs and five Heun steps; the maximum discrepancy
over every returned observation was `3.886e-16` CPU and `2.221e-16` CUDA.

The independent float32 and float64 network autograd comparisons and exact
five-step/split-restart comparisons passed on both devices. Cache mutation,
field replacement, complex/bool inputs and invalid mass were rejected. The
p=1 old initializer completed with a compiler hook that would raise if called,
and `pde.observable_compiler` was absent from imported modules. Independent
Hermite orders 160/240 differed by `2.007e-13`; the 240-rule v/tau/s/beta values
differed from the working Legendre constants by at most `3.331e-16`. This is
an independent numerical diagnostic, not a rigorous quadrature error bound.

The first invocation of my independent script stopped at its late dispatch
check because **I** supplied the rational string `'1/1024'` to an arithmetic
conversion accepting a numeric value there. This was not candidate failure.
The original script and failed log are preserved as `independent_checks_initial.py`
and `independent_cpu.log`, with its already-written restart archives retained.
Only my script was corrected to exact dyadic numeric `1/1024`; the rerun used
new `_v2` output/checkpoint names. Also, my preregistration described the
maintained suite as 14 tests; inspection/execution established its actual count
as 13, all run. Neither adjustment changes a scientific threshold or candidate.

Environment: Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130; allocated GPU
NVIDIA GeForce RTX 3090. One Torch/numerical thread, deterministic algorithms,
TF32 disabled, and `CUBLAS_WORKSPACE_CONFIG=:4096:8` were used for reference
checks. A Torch TF32-control deprecation warning was emitted; it did not fail
execution. Each CUDA process used the existing 15% allocation cap.

Producer work times were about 0.070/0.048 s CPU and 0.373/0.375 s CUDA; these
are the documented work timers, not process end-to-end timings. Peak process
RSS was at most 518,152,192 bytes CPU and 920,547,328 bytes CUDA. CUDA peak
allocated/reserved bytes were 33,610,752/35,651,584. Each producer counted
2016 retained closure tensor bytes and 5120 network bytes. No timing ratio or
general memory benchmark is inferred. The hard command limits were not reached.

## Component disposition and remaining limits

| Component | Disposition |
|---|---|
| Exact joint initialized law, source response, C and Cholesky normalization | Pass for fixed finite d and the stated exact-expectation target. |
| p=1 dictionary correspondence and absence of generic compiler dependency | Pass. |
| Scalar coefficient approximation and population sampling metadata | Pass as disclosed finite numerical constructions; no certificate. |
| Sign folding and full signed observation law | Pass. |
| Closure vector field, weights, gradients, energy, dense M, Heun | Pass for the supplied finite model. |
| Actual finite-network initialization, gradients and comparator | Pass. |
| CPU/CUDA, float32 controls, state ownership and own-state restart | Pass within the explicitly stated arithmetic/environment contract. |
| State/workspace accounting | Pass as tensor/work estimates, not certified process-memory limits. |
| Comparison API | Required R1 correction. Other checked ordinary-range semantics pass. |
| Maintained finite producer/analyzer | Reproduced on CPU and CUDA; operational claims only. |

There are no other unresolved correctness objections in the reviewed scope.
Optional maintenance: update deprecated Torch TF32 controls in a future
compatibility change, and consider retaining the independent weighted-zero and
population-permutation checks in the maintained suite. These are optional and
do not add required scientific claims. R1 is the sole required correction.

This review gives no accuracy guarantee between fixed-p closure and a trained
network, no general-d hierarchy convergence, no uniform rotation invariance,
no generalization conclusion, and no comparative speed claim. It has not
reproved the whole book. Acceptance remains blocked by R1 even though all
maintained tests and the ordinary-range independent checks pass.

## Exact input hashes and read coverage

The following table was generated from my independently verified
`input_hashes.json`. “Full” means every line read; original-guide equality
coverage is explained above. “Hash only” denotes deliberately unread metadata
or inapplicable auxiliary skill files, not scientific dependency omission.

<!-- A3 verified input table follows. -->
| Frozen input | Lines | Coverage | SHA256 |
|---|---:|---|---|
| `PROMOTION_PLACEMENT.md` | 27 | Hash only | `b3ca29eb03eaacf95b7b06410bf50bdb8141d2ca343881ce33fc9d34b3a26db6` |
| `PROMOTION_REVIEW_ASSIGNMENT.md` | 62 | Full | `ac4b0fe843f21b54a195ff49d7fe1e82d91eba93be6dd2240c6b21ef7095a2b3` |
| `PROMOTION_assemble.py` | 38 | Hash only | `9afd22e391e517a741a12b3c1752732acc8c8efe0c3d0e692b9f5241bca16bf2` |
| `code/GENERAL_P1.md` | 212 | Full | `982cace29181a9e049fe9e9e88a735c8631015d36614c13d8c81b9074f90f114` |
| `code/README.md` | 1117 | Full | `ff5a89effef3fc1bc86a2bcc699453731c50bebffd9fd5ff0844f690717dc237` |
| `code/pde/__init__.py` | 26 | Full | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/closure_comparison.py` | 128 | Full | `650f93aee1590aaf25549dc555e5b2d706c5058e25469b31e988a2b4883ea6f1` |
| `code/pde/finite_network.py` | 363 | Full | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_torch.py` | 153 | Full | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `code/pde/gaussian_moments.py` | 114 | Full | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_arithmetic.py` | 230 | Full | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_fixed.py` | 223 | Full | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_initialization.py` | 397 | Full | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_p1_initialization.py` | 181 | Full | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `code/pde/observable_torch_p1.py` | 403 | Full | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `code/pde/observable_words.py` | 217 | Full | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/scripts/analyze_general_p1.py` | 46 | Full | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| `code/scripts/example_general_p1.py` | 131 | Full | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| `code/tests/test_general_p1.py` | 297 | Full | `9c6b55f4e4efd68fca45ffd0b2095c6a390b582dec28c5dadba50c8b6c15ae12` |
| `dependencies/global_nonlinear_source_units.md` | 393 | Full | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |
| `dependencies/original_code_README.md` | 1113 | Full; identical-prefix verification | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `dependencies/original_docs_README.md` | 738 | Full; identical-prefix verification | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | 98 | Full | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | 742 | Full | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `docs/observable_p1.md` | 332 | Full | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `instructions/AGENTS.md` | 62 | Full | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `instructions/RESEARCH_WORKFLOW.md` | 225 | Full | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `instructions/investigate-conjectures/SKILL.md` | 185 | Full | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `instructions/investigate-conjectures/agents/openai.yaml` | 11 | Hash only | `ba8e39aba0463d706c4fa49375b90d0b9ce4d0ce436875e6d35ca61bcf387d02` |
| `instructions/investigate-conjectures/references/adversarial-audit.md` | 121 | Full | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `instructions/investigate-conjectures/references/decisive-experiments.md` | 141 | Full | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| `instructions/investigate-conjectures/references/evidence-ledger.md` | 157 | Full | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `instructions/investigate-conjectures/references/proof-search-orchestration.md` | 97 | Hash only | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
| `instructions/investigate-conjectures/references/research-contract.md` | 99 | Full | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `instructions/solve-math-rigorously/SKILL.md` | 115 | Full | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `instructions/solve-math-rigorously/agents/openai.yaml` | 12 | Hash only | `13e1679d378e917628b9f7d58c687e78e0442df8b6ad9089a4720a87f6bb3d1c` |

Live neutral assignment hash: `ac4b0fe843f21b54a195ff49d7fe1e82d91eba93be6dd2240c6b21ef7095a2b3`, equal to the frozen assignment. The manifest itself has the hash given at the start. Final rehash of every frozen entry also passed.
