# Independent integration review of integrated05

**Verdict: PASS for the assigned integration scope.** No required correction or unresolved integration objection was found. This is a complete fresh integration review, not user approval, a replacement for the paired scientific reviews, or a whole-book proof audit.

Reviewer: `/root/integration_review_05`, 2026-09-16. I received only the neutral assignment and named frozen inputs, used the required `solve-math-rigorously` skill, and did not delegate. I did not read study READMEs/history, previous reports, selector conclusions, scientific verdicts, other reviewers, chats or Git history. No live scientific source or Git state was changed. All generated checks are in the assigned scratch or fresh edition output namespace.

The edition root is `data/generated/closure_endpoint_discrimination/promotion_20260916/integrated05/`. Below, edition-relative paths refer to that root. Review scratch is `data/generated/closure_endpoint_discrimination/promotion_20260916/integration_review_05_scratch/`; fresh products are under edition `data/established/integration_review_05/`. Earlier retained products were not read.

## Inputs, integrity and complete coverage

The frozen manifest SHA256 is `83e0e4b3c1238880e7a8d87fdb251233a41b491462c8fa3e14a0fa3443c6ff3e`; all 74 listed files match. `ASSEMBLY.json` hashes to `b607c62c902936a9ea1262db8d6e56fd9f62929a094d88a6bca298faf49aa7b1`. The baseline manifest matches `db145c32cec7c5713b232b489fa23103d29ad717c2085092a131d5a66cd5b01a`; each of its four originals matches both its manifest and the assembly baseline. The full per-file SHA256 inventory is retained in scratch `hash_verification.json`. Frozen inputs still match after execution.

I read every line of the following new material:

- `docs/observable_p1.md` (332 lines), `code/GENERAL_P1.md` (235), and the complete inserted **“Order, angular symmetry, and the closure's own tangent kernel.”** remark at `docs/global_nonlinear.md:13469–13732`, including H3.CS1–H3.CS10 and every proof.
- `code/pde/observable_torch_circle.py` (313), `observable_p1_initialization.py` (181), `observable_torch_p1.py` (403), `finite_torch.py` (153), and `closure_comparison.py` (226).
- `code/tests/test_observable_torch_circle.py` (137), `test_general_p1.py` (391), `code/scripts/validate_torch_circle.py` (105), `example_general_p1.py` (131), and `analyze_general_p1.py` (46).
- Full `code/tools/check_library.py` (100), `code/tests/test_library_boundary.py` (58), `docs/README.md` (742), `docs/NOTATION.md` (98), `code/README.md` (1240), `AGENTS.md` (62), and `RESEARCH_WORKFLOW.md` (225). Truncated guide output was repaired with bounded rereads.

The complete older runtime bodies read were `code/pde/__init__.py`, `finite_network.py`, `gaussian_moments.py`, `observable_solver.py`, `observable_initialization.py`, `observable_words.py`, `observable_arithmetic.py`, and `observable_fixed.py`. The supported orders 1,3,5 all dispatch to the core initializer; their feature counts are (5,3), (35,10), (128,21), with tail codes (), (), (4,5). They do not dispatch the generic source compiler. No missing runtime dependency was needed for these paths.

The older mathematical scope was complete C.4.7.10.B, lines 13161–13430, and complete C.4.7.10.C.1, lines 13431–13786, with the following boundary and initial C.2 lines through 13805 read to locate the insertion. I also read all 393 lines of the assigned `frozen_v4/dependencies/global_nonlinear_source_units.md`, SHA256 `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766`: complete Sections 2–3 and the H3.1/H3.N1–N2 extracts. The named original `frozen_v4/code/tests/test_general_p1.py` matches SHA256 `99de6d99818d022002e432021f0e86f14b263c382ea6caedb2f4c7351ecafb03`; its complete contents were accounted for by the full current file and exact original/current diff. All 16 test bodies are byte-identical. Only optional imports/policy guards, two skip decorators, and the `array`/`case` helper adaptations differ; their Torch-equipped meaning is unchanged.

The unread scientific complement includes the rest of the book, older runtime bodies not listed above, and older test/recipe bodies not assigned. Hashing, link scanning and standard discovery do not constitute scientific review of that complement. No outside paper or historical material was used.

## Placement, interfaces and preservation

The new general-d page has distinct value: explicit scalar coefficient reduction, the reverse-response term, repeated-block Cholesky normalization, exact antithetic folding and a finite supplied-state implementation contract. It is appropriately separate from the established circle convergence development. The circle remark follows H3.N2 and precedes the original numerical-parameter/theorem text; it explains represented angular frequencies, conditional mark-parity equivalence, and the closure's own tangent kernel without presenting the existing C-H1–C-H4 results as new.

Notation and interfaces agree across the additions. Local p is closure order, P is integration population count, n is network width, and d is input dimension; the older precision-p convention is explicitly distinguished. Both action directions use the same full M and its transpose. Inputs are already x/sqrt(d); the comparator preserves canonical NumPy Gaussian draw order and stored variances (1,1/n,1/n²), random finite readout, output /n, unhalved weighted loss, and mobilities (n,1,n). The closure's zero initial readout has its stated different meaning. The population-weighted row/readout metric, Frobenius middle metric, and simultaneous two-stage Heun semantics match the displayed equations and independent gradient checks.

The two coefficient rules are not misleadingly interchangeable. The circle backend transfers the unchanged finite-Q Halton initializer, including response terms, redundant p=5 constants and ridge 1/[1024(p+1)²]. General-d p=1 instead uses scalar coefficient quadrature toward population expectations and the fixed ridge 1/4096; it retains the right inverse-Cholesky transpose. Its finite result is not asserted equal to the circle finite-Q normalization. The conditional p=1/p=2 parity result requires matched ridge and symmetric rules and explicitly excludes default-run equality.

Folded dynamics preserve the full active matrix, and observations restore both signs with half weights. Checkpoints retain the required marks, current arrays, data and representation/arithmetic information; the separate circle portable format has its explicit same-device/reduction continuation restriction. Float64-only circle versus explicit float32/64 general tensors, CPU initialization, saturation, roundoff, nonfinite rejection, and absence of an accuracy selector are disclosed. No public addition broadens a neural convergence theorem or asserts MNIST/PCA accuracy, speed ratios or endpoint fidelity.

Byte-level preservation passed: docs README adds only lines 739–742, code README adds only lines 1114–1240, and removing global-nonlinear lines 13469–13732 reproduces every original byte. The checker has exactly one changed line: its allowed imports expand from `{numpy,pde}` to `{numpy,pde,scripts,psutil,torch}`. The other 56 established baseline files are hash-identical. The edition has no `.git` or `studies` directory. Diff evidence and `byte_preservation.txt` are in scratch. There is deliberate overlap in finite contractions between the two optional backends, justified by their different initialization, state-ownership, precision and restart interfaces; no duplicate replacement of the maintained CPU theorem or solver is introduced.

## Executed checks and evidence

Limits were written before execution in `limits_cpu.json`, `limits_cuda.json`, and `limits_cuda_escalated.json`: one worker, one numerical thread, explicit `cuda:0`, 120 seconds per subprocess and 600 aggregate subprocess wall seconds. The unchanged tiny recipes use circle p=1,3,5, Q=64, P=32, four steps at .005; general p=1 uses d=3, m=9, n=P=16, seed 101, ten steps at .005. No dataset campaign or adaptive parameter search ran. Producers also save their own limits before training.

The common environment sets edition `PYTHONPATH=code`, `PYTHONDONTWRITEBYTECODE=1`, all of OPENBLAS/OMP/MKL thread counts to 1, and `CUBLAS_WORKSPACE_CONFIG=:4096:8`. Both `PDE_TEST_DEVICE` and `CIRCLE_TEST_DEVICE` select the device. `CIRCLE_TEST_SCRATCH`, `TMPDIR`, and inherited discovery scratch settings point to the existing private scratch directory. NumPy-only Python was `/usr/bin/python3` 3.10.12, NumPy 1.26.4. Torch Python was `/home/amir/miniconda3/bin/python` 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130/CUDA 13.0. Authorized CUDA execution used an NVIDIA GeForce RTX 3090.

From `/home/amir/Codes/PDE`, the actual supervisor commands were:

```text
python3 -B data/generated/closure_endpoint_discrimination/promotion_20260916/integration_review_05_scratch/run_checks.py cpu
python3 -B data/generated/closure_endpoint_discrimination/promotion_20260916/integration_review_05_scratch/run_checks.py cuda
python3 -B data/generated/closure_endpoint_discrimination/promotion_20260916/integration_review_05_scratch/run_checks.py cuda_escalated
```

Scratch `commands.jsonl` records the exact argv, cwd, environment record, exit code, individual wall time and cumulative wall time of every one of the 31 subprocesses. The runner and two small guide/structural scripts are retained there, together with every named command log. This includes direct runs of both new test modules and the named original p=1 test on CPU/CUDA, the boundary checker/fixtures, all new Python guide blocks, both producers, and the independent NumPy analyzer with `--repeat` on separately regenerated examples. Source/output hashes are in producer records and scratch `output_sha256.json`.

| Check | Observed result |
|---|---|
| NumPy-only standard discovery | 218 tests discovered, no import errors; ordinary pde and discovery did not load Torch. |
| NumPy-only affected tests | General p=1: 8 pass, 8 explicit Torch skips; circle: 4 explicit Torch skips. |
| Torch CPU and CUDA affected tests | General p=1: all 16 pass on each; circle: all 4 pass on each. |
| Original scientific test baseline | All 16 pass on CPU and CUDA, matching adapter execution. |
| Boundary / fixtures / links | 67 library source files checked; all 5 maintained fixtures pass; all 7 new/appended local links and their fragments resolve. |
| Guide examples | Both general-p1 Python blocks and the appended circle Python block pass. |
| Circle producer | All three orders complete on CPU and CUDA with exact restart. Largest NumPy-reference discrepancy: 3.47e-18 CPU, 1.74e-18 CUDA. |
| General producer and replay | Two fresh runs per device; all outputs replay successfully and every repeat observation array is exact. Largest replay discrepancy: 2.22e-16 CPU, 1.11e-16 CUDA. |

The sandbox initially hid CUDA: its requested-device tests and producers failed with device-unavailable errors, and the dependent analyzer lacked output. Those logs and failed output directories were retained. The authorized escalation reran only that failed device scope into fresh `_cuda_escalated` destinations; every subprocess then passed. No candidate change was needed. Two preliminary reviewer-harness mistakes—baseline key prefix handling and an overbroad demand that adapter helpers remain unchanged—were corrected before the successful byte/test-body checks; neither was a source defect.

All logged subprocesses, including failed sandbox attempts, total 42.634 wall seconds; the longest took 2.715 seconds. CUDA peak allocated bytes were 34,144,768 for the circle producer and 33,610,752 for each general producer, within their stated allowances. These numbers document bounded operation only. The whole inherited 218-test suite was discovered, not executed; affected suites and maintained checker fixtures were executed as specified.

**Required corrections:** none. **Optional suggestions:** none needed for this package. **Unresolved objections:** none within the assigned scope. Exact same-device continuation and finite operation are verified; broader approximation, performance, external-source novelty, and the unread book complement remain outside this verdict. User approval and the separate scientific gates remain necessary before live promotion.
