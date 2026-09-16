# Independent integration review — incomplete / superseded

**Status: INCOMPLETE / SUPERSEDED. This is not an integration-gate PASS.**

Reviewer: fresh isolated agent `/root/integration_review`, 2026-09-16.
Assigned edition: `data/generated/closure_endpoint_discrimination/promotion_20260916/integrated03/`.

The supervisor stopped this review after stating that the assembled edition
would be superseded following a required scientific correction. No description
of that correction, scientific-review finding, or other review report was
requested or read. I stopped substantive review and preserved the work already
done. The CPU and CUDA batches had been launched before the stop and completed;
no new numerical check was launched after it. This report neither evaluates the
undisclosed correction nor supplies approval for this or a future edition.

## Isolation and input identity

I read only the neutral assignment, the assigned frozen edition and baseline
metadata, the specifically authorized established-source extract, and the
`solve-math-rigorously` skill. I did not read a study README, history, previous
verdict, selector conclusion, proposal/validation report, another review, Git
history, or other-study scientific finding. The external-looking path to the
specified source extract was used only for that named unchanged established
dependency. Assembly origin paths and source-manifest hashes were treated as
metadata; their targets were not fetched.

No live `docs/` or `code/`, frozen source, Git index, or repository history was
edited. My writes are this report, private assigned scratch, and fresh operation
outputs beneath the assigned edition's `data/established/integration_review/`.
There was no review delegation or exchange of scientific conclusions with
another reviewer. The supervisor's stop instruction supplied status only.

Verified SHA256 identities:

| Input | SHA256 |
|---|---|
| Edition `FROZEN_SHA256.json` | `3808b2228bd2b5dc76c64ba42736dbfd19b2418be25d04a75627c4a813ec673c` |
| Edition `ASSEMBLY.json` | `f5912f8eb83db49fb31bba9219ee323b250622ea49f000c5df4d35f13b806043` |
| `integration_inputs/BASELINE_SHA256.json` | `db145c32cec7c5713b232b489fa23103d29ad717c2085092a131d5a66cd5b01a` |
| Named complete established-source extract | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |

I recomputed and matched all **74** source-file entries in the frozen source
manifest and all **four** baseline-file entries. Each baseline entry also
matched the corresponding original hash in `ASSEMBLY.json`. Thus all edition
inputs read or executed here are covered by a checked complete manifest. A
line-count and per-file hash inventory of the complete assigned reading appears
at the end of this report. Hashing other manifest files did not constitute
reading their scientific bodies.

## Completed reading and its limits

I read every line of all new modules, tests, scripts, the new theory page and
general-p1 guide, the complete supplied notation and both reading/implementation
guides, `AGENTS.md`, `RESEARCH_WORKFLOW.md`, the checker and its maintained
fixtures. This includes both producer and analyzer before execution. Long tool
outputs were repaired with narrower reads; in particular the notation/theory
page and both guides were reread in the ranges hidden by output truncation.

The new remark is the insertion at `docs/global_nonlinear.md:13469–13732`,
headed **“Order, angular symmetry, and the closure's own tangent kernel.”**
I read all H3.CS1–H3.CS10 statements and proofs. For its surrounding established
placement I read lines **13150–13795**, covering the complete B unit beginning
at 13161, the complete C.1 unit beginning at 13431, the insertion, and the
immediate neighboring boundary lines. The first lines of C.2 were seen only
as that ending boundary; its proof was not reviewed.

The complete older runtime bodies read were exactly:
`__init__.py`, `finite_network.py`, `gaussian_moments.py`,
`observable_solver.py`, `observable_initialization.py`, `observable_words.py`,
`observable_arithmetic.py`, and `observable_fixed.py` under edition `code/pde/`.
The named 393-line established-source extract was read completely: it contains
the elementary tools and complete finite Gaussian adaptive-reuse source units,
the H3.1 contraction proof, and H3.N1/N2 placement equations. The four baseline
files were used for hash and preservation/diff checks, not as an invitation to
read unrelated old proofs.

The unread scientific complement includes every other book proof and the
other older implementation/test/recipe bodies, including the generic source
compiler and older closure/law modules. The full guide summaries were read as
assigned; that is not verification of every theorem they summarize. The
structural checker scans Markdown links and Python syntax across the edition;
that scan is not scientific reading or a whole-library proof audit. I did not
run the older data campaigns or re-audit C-H1–C-H4. For p=1,3,5 the read
initializer selects its core branch; its conditional import of the generic
compiler is not dispatched by these supported paths. No missing dispatched
runtime dependency was identified before the stop.

## Findings reached before the stop

These are preserved observations, not a completed integration verdict.

1. **Preservation and narrow change.** The assembly baseline lists 60 existing
   files. The hashes of 56 match unchanged edition files. Textual sequence
   comparison of the other four found exactly: an append at code-guide lines
   1114–1240; an append at docs-guide lines 739–742; the theory insertion at
   13469–13732; and one checker-line replacement. The latter changes only the
   permitted absolute import roots from `{numpy,pde}` to
   `{numpy,pde,scripts,psutil,torch}` at line 72. The maintained checker tests
   have their original hash. For the edited files this was a decoded-text
   comparison; a separate raw-byte removal/reconstruction assertion had not
   been completed when the review was stopped. The manifest check does prove
   exact bytes for the 56 unchanged originals.

2. **Scope and notation.** The new pages explicitly distinguish closure order
   p from P population nodes, n neural width, d input dimension, and the older
   theorem's arithmetic-precision p. They retain normalized inputs U=x/sqrt(d),
   independent Gaussian stored variances (1,1/n,1/n²), output cᵀh2/n, unhalved
   weighted loss, and physical mobilities (n,1,n). Both evolving backends use
   the complete M and its actual transpose. Heun's two stages use simultaneous
   moving-block states. Numerical GF, raw GD, exact flow, finite observations,
   and neural approximation are explicitly separated.

3. **Separate initializer contracts.** The circle backend supports d=2,
   p=1,3,5, detached float64 CPU/CUDA tensors, and transfer from the maintained
   CPU initializer. Its dimensions include both redundant p=5 constant tails.
   The general-p1 initializer instead uses repeated exact-population scalar
   Gram blocks approximated by normalized truncated-normal quadrature and
   independent seeded population sampling. The general guide explicitly says
   this is not equality with the finite-Q Halton normalization. Separate
   module names and metadata make that distinction visible. The supplied-state
   general engine allows arbitrary finite feature/population sizes without
   assigning those states a Gaussian neural-law theorem.

4. **General-p1 coefficients and folding.** The displayed response term,
   inverse-lower-Cholesky right transpose, fixed ridge 1/4096, and two initial
   bands agree with the read implementation and its dense-factorization test.
   Only the initial D is banded; the dynamics keep a dense M. The sign-folding
   statement requires an antithetic rule, not iid P draws. Its lower joint
   marks and separate upper population are retained, while signed paired
   observations explicitly return both signs with half weights. The tested
   nontrivial folded and unfolded states compare full observations as well
   as moving blocks.

5. **Inserted theory placement.** The remark is placed directly after the
   existing finite equations H3.N2 and before their numerical-refinement
   parameters and theorem. Its finite-state odd-input argument, unrestricted
   odd-frequency example, metric/kernel identities, and own frozen-readout
   comparator concern that finite closure. It explicitly excludes a neural
   limit, learned endpoint/bandwidth rule, or universal improvement with order.
   The p=1 versus p=2 parity claim explicitly requires matched positive ridge
   and symmetric coefficient/evolution rules. It states the default schedule
   1/4096 versus 1/9216 and ordinary Halton rules do not meet those matched
   assumptions. This avoids claiming default numerical equality.

6. **Distinct maintained value and duplication.** The circle module adds an
   optional tensor execution path for existing finite equations, not a new
   C-H1–C-H4 theorem. General-p1 adds arbitrary-d scalar coefficient assembly,
   optional antithetic storage, a separate finite network comparator, restart,
   and explicit prediction/Gram/checkpoint-comparison utilities. The theory
   page records the narrow coefficient and finite-equation justification.
   The guides state no MNIST/PCA, speed-ratio, or empirical neural-accuracy
   result is being added. Old recorded-operation prose in the unchanged guide
   prefix remains old maintained content; it was not reproduced here.

7. **Ownership, arithmetic and restart.** Circle transfer/factory/evolution
   results own their arrays, with mutable states revalidated at evaluation.
   General-p1 copies construction/prepared data, caches fixed contractions,
   checks ordinary tensor mutation versions, and documents bypasses as outside
   contract. Its NPZ record includes frozen/current arrays, data,
   representation, dtype, association, block size and arithmetic policy.
   Circle uses the existing float-hex serializer and keeps its own-step/device
   replay caveat. The tests exercise same-environment exact restart and
   finite-range behavior. Precision/device limitations remain explicit;
   ordinary 1−tanh² and intermediate matrix operations do not inherit the
   NumPy reference's specialized extreme-range promises.

8. **Comparison semantics.** Explicit arrays and matching ordered unique IDs
   are required. Undefined constant correlations and zero-reference relative
   errors are handled explicitly. Training-loss matching uses only saved
   training losses, reports brackets/mismatch, refuses extrapolation, and is
   not represented as equality of learned maps or a pure clock change.

No required integration correction had been established independently in this
partial review before the stop. That sentence does not clear the edition: the
review is incomplete, and the supervisor separately reported supersession.

## Executed checks and fresh outputs

The exact command arrays, environment, return codes, per-process wall times,
and log paths are retained in
[`checks.json`](../../data/generated/closure_endpoint_discrimination/promotion_20260916/integration_review_scratch/checks.json).
The CUDA driver is retained alongside it as `run_cuda_checks.py`. CPU checks
used an inline subprocess supervisor with the same recorded limits.

Working directory for every subprocess was the assigned edition root.
Interpreter: `/home/amir/miniconda3/bin/python`, Python 3.10.14.
Observed dependencies: NumPy 1.26.4, Torch 2.9.0+cu130, CUDA 13.0.
CUDA device: explicitly assigned `cuda:0`, NVIDIA GeForce RTX 3090.
The CUDA launch used the authorized escalation to access this device.

Before training, the scratch record declared 120 wall seconds per subprocess,
600 total compute wall seconds, one numerical thread, no adaptive search, and
the fixed guide bounds: circle p=1,3,5, Q=64, P=32, four Heun steps of .005;
general d=3, m=9, n=P=16, seed=101, ten Heun steps of .005. Each producer also
writes its own running/budget record before its numerical work. Outputs were
fresh and separated from the frozen source and baseline inputs.

Environment for all subprocesses:

```text
PYTHONPATH=<edition>/code
PYTHONDONTWRITEBYTECODE=1
OPENBLAS_NUM_THREADS=1
OMP_NUM_THREADS=1
MKL_NUM_THREADS=1
NUMEXPR_NUM_THREADS=1
CUBLAS_WORKSPACE_CONFIG=:4096:8
TMPDIR=<assigned integration_review_scratch>
CIRCLE_TEST_SCRATCH=<assigned integration_review_scratch>
CIRCLE_TEST_DEVICE=cpu       # cuda:0 in the CUDA batch
PDE_TEST_DEVICE=cpu          # cuda:0 in the CUDA batch
```

All command rows below are prefixed with the stated interpreter and `-B`.
`OUT` denotes edition `data/established/integration_review`, and is expanded
literally in `checks.json`.

| Command | Actual outcome |
|---|---|
| `code/tests/test_observable_torch_circle.py`, CPU | 4 tests passed; process 1.897 s |
| `code/tests/test_general_p1.py`, CPU | 13 tests passed; process 1.911 s |
| `code/tests/test_library_boundary.py` | 5 fixtures passed; process 0.054 s |
| `code/tools/check_library.py` | 67 files structurally checked; exit 0; 0.486 s |
| `code/scripts/validate_torch_circle.py --device cpu --output OUT/circle_cpu` | Complete; all orders, parity and exact restart; 1.727 s |
| `code/scripts/example_general_p1.py --device cpu --output OUT/general_cpu_a` | Complete; 1.603 s |
| `code/scripts/example_general_p1.py --device cpu --output OUT/general_cpu_b` | Complete independent rerun; 1.590 s |
| `code/scripts/analyze_general_p1.py --run OUT/general_cpu_a --repeat OUT/general_cpu_b --output OUT/general_cpu_analysis.json` | NumPy replay and exact repeat arrays passed; 0.155 s |
| `code/tests/test_observable_torch_circle.py`, CUDA | 4 tests passed; process 2.498 s |
| `code/tests/test_general_p1.py`, CUDA | 13 tests passed; process 2.644 s |
| `code/scripts/validate_torch_circle.py --device cuda:0 --output OUT/circle_cuda` | Complete; all orders, parity and exact restart; 2.105 s |
| `code/scripts/example_general_p1.py --device cuda:0 --output OUT/general_cuda_a` | Complete; 2.116 s |
| `code/scripts/example_general_p1.py --device cuda:0 --output OUT/general_cuda_b` | Complete independent rerun; 2.098 s |
| `code/scripts/analyze_general_p1.py --run OUT/general_cuda_a --repeat OUT/general_cuda_b --output OUT/general_cuda_analysis.json` | NumPy replay and exact repeat arrays passed; 0.150 s |

All 14 subprocesses exited zero. Their summed process wall time was
**21.034903 s**, below the recorded compute budget. General tests emitted a
Torch warning about future deprecation of the existing TF32 setting API;
there was no associated check failure. This is an environment observation,
not a conclusion about compatibility with an untested future Torch version.

The suites include independent autograd metric checks, samplewise NumPy
contractions, canonical finite-network normalization/RHS checks, dense
Cholesky comparison, stage semantics, unequal populations, zero weights,
nonunit/duplicate/zero general inputs, input/ownership rejection, float32,
association/block changes, signed pairs and exact same-environment restart.
The circle CPU comparison produced a largest reported moving-array absolute
difference of 3.469446951953614e-18; the CUDA comparison's largest was
1.734723475976807e-18. All three orders restarted exactly on both devices.
The independent general-example analyzers reported maximum replay discrepancies
2.220446049250313e-16 on CPU and 1.1102230246251565e-16 for CUDA-produced
arrays, with exact same-device rerun arrays in both cases.

Producer records retain their own source/output hashes, policies, phase times,
state bytes and process/device memory measures. The circle CUDA producer
reported a 34,144,768-byte allocated peak, below its 1 GiB tensor limit;
general CUDA run A reported 33,610,752 bytes under its 15% allocator policy.
These are tiny operation checks. No timing ratio, accuracy, convergence rate,
whole-domain bound, or dataset result follows.

## Remaining obligations and objections

The review was stopped before these integration tasks were completed:

- Execute the literal newly added Python guide snippets together in their
  documented sequence. Their producer recipes were executed, but that is not
  execution of every inline snippet.
- Independently check new link fragments against generated heading anchors.
  The maintained checker validated local files and dependency boundaries but
  deliberately strips fragments.
- Complete a clean optional-dependency import isolation check and module-origin
  trace. The explicit new imports succeeded in tests, and the complete
  `pde/__init__.py` source imports only NumPy-based dependencies, but a separate
  Torch-unavailable subprocess was not run.
- Complete raw-byte preservation reconstruction for the four edited files,
  beyond the completed textual diffs and exact unchanged-file hashes.
- Finish adversarial integration synthesis and any independent examples beyond
  the maintained suites and fresh producer/analyzer replays.

I make no completed optional-change recommendation from the interrupted review.
The outstanding items are recorded limits of this review, not newly demonstrated
defects in the implementation. The superseding scientific correction remains
unread and unevaluated here. A fresh reviewer must read and review the complete
corrected frozen scope; this report cannot be converted into approval by
appending only a correction check. This is not user approval and authorizes no
live integration or Git action.

## Complete-file reading inventory

The following inventory records complete assigned files read, with their
verified edition hashes. The selective `global_nonlinear.md` coverage is given
above; its entire file was hashed, not scientifically read in full.

| Edition file | Complete lines read | SHA256 |
|---|---:|---|
| `docs/observable_p1.md` | 332 | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `code/GENERAL_P1.md` | 212 | `982cace29181a9e049fe9e9e88a735c8631015d36614c13d8c81b9074f90f114` |
| `docs/README.md` | 742 | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/README.md` | 1240 | `7aa3bc9700a75294f9f209a34e05af4033cd35dd5edb736846ff8bdfdc4bdbb6` |
| `AGENTS.md` | 62 | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `RESEARCH_WORKFLOW.md` | 225 | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `code/pde/observable_torch_circle.py` | 313 | `4fa63eb6abdd1c8573abfa1a7dc0a107d13ec669ae078659e8298cd517000430` |
| `code/pde/observable_p1_initialization.py` | 181 | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `code/pde/observable_torch_p1.py` | 403 | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `code/pde/finite_torch.py` | 153 | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `code/pde/closure_comparison.py` | 128 | `650f93aee1590aaf25549dc555e5b2d706c5058e25469b31e988a2b4883ea6f1` |
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/tests/test_observable_torch_circle.py` | 137 | `437b9f577621d854afc62171c285129fe424e1eb3ef406b680d8ddd3a72a1181` |
| `code/tests/test_general_p1.py` | 297 | `9c6b55f4e4efd68fca45ffd0b2095c6a390b582dec28c5dadba50c8b6c15ae12` |
| `code/tests/test_library_boundary.py` | 58 | `375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a` |
| `code/scripts/validate_torch_circle.py` | 105 | `edb42a5bb72b28f96f484a54ddc2f65043329ab0c8539ff3aa415923f5a885e0` |
| `code/scripts/example_general_p1.py` | 131 | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| `code/scripts/analyze_general_p1.py` | 46 | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| `code/tools/check_library.py` | 100 | `4b0ec381caee28f8768ac7bc6e2d4af04e7860abdff73c75e7bc75af3067a018` |

Selective surrounding chapter file SHA256: `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.

Original baseline hashes used for the preservation comparison:

| Baseline | SHA256 |
|---|---|
| `integration_inputs/baseline/code/README.md` | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `integration_inputs/baseline/code/tools/check_library.py` | `7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6` |
| `integration_inputs/baseline/docs/README.md` | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `integration_inputs/baseline/docs/global_nonlinear.md` | `cbcf00fd705a9a938a6a3fd0d2bbc2f1c2dd3ab4303d848740a549dbb169f629` |

Neutral assignment SHA256: `bad05da254a0911888736735e3fd58acba105140fa52762bc03f03d9bc5e6bc2`.

Required skill read completely: `/etc/codex/skills/solve-math-rigorously/SKILL.md`; SHA256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
