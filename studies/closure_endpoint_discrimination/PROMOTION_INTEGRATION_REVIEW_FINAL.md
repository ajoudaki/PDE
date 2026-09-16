# Independent integration review of integrated04

**Verdict: required integration correction; do not accept this edition yet.** The new general-p1 test module breaks the documented standard test-discovery command in a NumPy-only environment. The complete assigned mathematical/interface review, byte-preservation checks, Torch CPU/CUDA tests, new Python examples, local links, and fresh producer/replay checks otherwise passed within the stated scope. This is an integration verdict, not either scientific review and not user approval.

## Identity, isolation and frozen inputs

Reviewer: fresh isolated agent `/root/integration_review_final`, 2026-09-16. I received the neutral assignment and explicit paths only. I did not author/assemble this edition, read a study README/history, selector/scientific/prior integration report, another reviewer's findings, Git history, or retained operational outputs. I did not delegate the required reading. I used the required `solve-math-rigorously` skill. No external theorem or external source was needed beyond the supplied complete established extract.

Let `R` denote `data/generated/closure_endpoint_discrimination/promotion_20260916/integrated04/`, `S` its sibling `integration_review_final_scratch/`, and `E=R/data/established/integration_review_final/`. These are relative to `/home/amir/Codes/PDE/`. Only this report, private `S` artifacts, and fresh `E` outputs were written; no frozen/live source or Git writes were made.

Verified SHA256 values:

| Input | SHA256 |
|---|---|
| Neutral assignment | `585de6813a60ddb6569ce4e7f8f05612d83b65cab534f32dfc6c9cbb545ab9f4` |
| `R/FROZEN_SHA256.json` | `1220b4160830a79513b0c025a2746797f16e6e1a91f1c498118914ce43adf808` |
| `R/ASSEMBLY.json` | `ff8bd686df56cb920924504934ba276515fb5879d11a5297e5a7c070c52db9ca` |
| `R/integration_inputs/BASELINE_SHA256.json` | `db145c32cec7c5713b232b489fa23103d29ad717c2085092a131d5a66cd5b01a` |
| Assigned `global_nonlinear_source_units.md` | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |

All 74 edition-manifest entries and all four baseline-manifest entries matched their per-file SHA256 values. All assembly destination hashes matched. The baseline hashes also matched `ASSEMBLY.json`. The exact per-file input hashes are the verified frozen manifests; `S/auxiliary_input_hashes.json`, `S/preservation.json`, and `S/exact_byte_preservation.json` retain the extra hash and preservation evidence. The only authorized external extract was the 393-line file at `data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v4/dependencies/global_nonlinear_source_units.md`; no other material from that study was consulted.

## Complete read coverage

Every line in the following complete files was read, including implementation, tests, examples, proofs and limitations. Initial oversized reads of the notation/proof material and docs guide were repaired with complete smaller reads.

| File under R | Lines read |
|---|---:|
| `docs/observable_p1.md` | 1–332 |
| `code/GENERAL_P1.md` | 1–235 |
| `code/pde/observable_torch_circle.py` | 1–313 |
| `code/pde/observable_p1_initialization.py` | 1–181 |
| `code/pde/observable_torch_p1.py` | 1–403 |
| `code/pde/finite_torch.py` | 1–153 |
| `code/pde/closure_comparison.py` | 1–226 |
| `code/tests/test_observable_torch_circle.py` | 1–137 |
| `code/tests/test_general_p1.py` | 1–380 |
| `code/scripts/validate_torch_circle.py` | 1–105 |
| `code/scripts/example_general_p1.py` | 1–131 |
| `code/scripts/analyze_general_p1.py` | 1–46 |
| `code/tools/check_library.py` | 1–100 |
| `code/tests/test_library_boundary.py` | 1–58 |
| `docs/README.md` | 1–742 |
| `docs/NOTATION.md` | 1–98 |
| `code/README.md` | 1–1240 |
| `AGENTS.md` | 1–62 |
| `RESEARCH_WORKFLOW.md` | 1–225 |
| `code/pde/__init__.py` | 1–26 |
| `code/pde/finite_network.py` | 1–363 |
| `code/pde/gaussian_moments.py` | 1–114 |
| `code/pde/observable_solver.py` | 1–350 |
| `code/pde/observable_initialization.py` | 1–397 |
| `code/pde/observable_words.py` | 1–217 |
| `code/pde/observable_arithmetic.py` | 1–230 |
| `code/pde/observable_fixed.py` | 1–223 |

I read `docs/global_nonlinear.md` lines 13161–13786 completely: all of C.4.7.10.B and C.1, including the new remark headed **“Order, angular symmetry, and the closure's own tangent kernel.”** at line 13469. The exact insertion is lines 13469–13732 (264 lines), covering every equation H3.CS1–H3.CS10 and every proof. C.1 starts at 13431; C.2 starts at 13787. I inspected that next boundary. I read the complete 393-line established-source extract, including Sections 2 and 3 and its H3.1/H3.N1–N2 units.

The four old baselines were used for hashes and exact preservation/diffs only. Older book proofs outside the preceding units/extract were not re-audited. Older guide summaries were read as required, not treated as a complete proof review of their subjects. Other unchanged source files were hashed, and the maintained structural checker parsed/scanned the edition; their scientific bodies were not manually read. The supported p=1,3,5 initializer paths remain `fast_core`; the generic compiler is not dispatched. The observed `pde` import closure contains only the assigned runtime dependencies and new modules. No missing runtime/scientific input was relied upon.

## Required correction

**R1 — Optional Torch breaks standard NumPy-only test discovery.** `code/tests/test_general_p1.py:11` imports Torch unconditionally, then imports the tensor modules and performs global Torch setup. `code/README.md:117` still introduces the all-tests discovery command as runnable using Python 3.10+ and NumPy (the later paragraph names NumPy/psutil). Ordinary `import pde` succeeds without Torch, but discovery of the newly added test fails before any test or skip can run. The circle suite already guards its optional Torch dependency and skips appropriately.

I reproduced the failure using the default Python 3.10.12 / NumPy 1.26.4 environment:

```text
python -B -m unittest discover -s code/tests -p test_general_p1.py -v
ImportError: Failed to import test module: test_general_p1
ModuleNotFoundError: No module named 'torch'
FAILED (errors=1)
exit status 1
```

This is the same loader used by the documented `test_*.py` command, restricted to the affected module to avoid unrelated execution. The problem is test-suite integration, not failure of ordinary package import or a mathematical objection. Make optional tensor tests discoverable without Torch, with explicit skips for the tensor groups and guarded setup/imports; preserve the NumPy tests where practical. An intentional change to the standard test dependency contract would instead need concrete corresponding documentation. A fresh complete integration review is required after repair; any scientific changes also reopen the scientific gates under the workflow.

## Preservation, placement and interfaces

- **Exact preservation:** all 56 unchanged established files match their recorded original bytes. Removing only inserted lines 739–742 of `docs/README.md`, 1114–1240 of `code/README.md`, and 13469–13732 of `docs/global_nonlinear.md` reconstructs each complete baseline byte-for-byte. The checker differs only at line 72: the allowed import set adds `scripts`, `psutil`, and `torch` to `numpy,pde`. There are no other replacements or deletions. Its existing five structural fixtures pass.
- **Placement/distinct value:** the circle remark immediately follows the finite equations and precedes the numerical refinement theorem, so its finite-state and conditional-symmetry conclusions remain separate from the existing convergence theorem. The separate general-d page contains the coefficient reduction, response term, normalization, folding proof and finite metric derivation; its cross-links connect theory and usage. The CPU closure and C-H1–C-H4 are not presented as new. The additions supply optional tensor execution, a scalar general-d p=1 initialization and finite comparator/diagnostics, rather than duplicate the earlier CPU theorem.
- **Notation and mathematics:** local p order, P populations, n width, d input dimension and the older precision p are explicitly distinguished. The p=1 block Gram and inverse-lower-Cholesky derivation retain `tau*gamma` and the right transpose. Both implementations evolve full M and use its actual transpose. The metric cancels population probabilities in row/readout velocities, including zero-weight nodes interpreted without division. The finite network retains its random readout, normalization `cᵀh2/n`, stored variances `(1,1/n,1/n²)` and mobilities `(n,1,n)`.
- **Scope:** the circle API enforces d=2, unit directions and p=1,3,5. The general engine accepts arbitrary finite supplied dimensions and U=x/sqrt(d), without assigning a neural law to arbitrary supplied states. Its scalar quadrature target differs from the finite-Q Halton normalization; this is disclosed in both proof and guide. The parity equality of orders one and two requires common ridge and symmetric rules; the actual differing ridge schedule and nonsymmetric default Halton prefixes are expressly excluded. The angular construction is a represented-state argument, not a reachability result. The tangent kernel is the closure's own kernel, not a newly identified neural kernel. No new convergence, accuracy, performance-ratio or historical MNIST/PCA claim was found.
- **Numerics/observations/restart:** simultaneous Heun uses the same state for every block at each stage; it is not raw GD or an exact flow. Folding preserves the odd invariant state class and returns both signs for joint pairs, with half weights. Initial/current and cross-Gram conventions agree with the formulas. Both restart formats retain complete current/frozen state and the finite data law without history. General-p1 restart checks arithmetic policy/device type; circle restart preserves float-hex values with exact continuation qualified by device/reduction/block schedule. Float32/64 restrictions, saturation, overflow, quadrature and panel-only limitations are stated.
- **Independence:** source inspection and explicit path scanning found no new runtime references to studies, generated history, `/home/`, `/tmp/`, or `.git/`. Imports resolve to R/code, and the boundary checker passes 67 source files. All producer inputs were generated freshly from the fixed source recipes; no archived array was consumed. The analyzer consumed only this review's fresh outputs.

## Actual execution and evidence

Before numerical execution I saved `S/limits.json`: one worker, one numerical thread, cuda:0, 120 seconds maximum per subprocess and 600 seconds aggregate subprocess wall time; only fixed finite tests/guide examples and recipes, no campaign or adaptive search. Both producers and the analyzer were read in full before execution. Circle recipe: p=1,3,5, Q=64, P=32, four steps at .005, block size two. General recipe: d=3,m=9,n=P=16, seed 101, ten steps at .005, float64. No optional dataset was supplied.

All commands used cwd R. Shared environment: `PYTHONPATH=R/code`, `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`, `CUBLAS_WORKSPACE_CONFIG=:4096:8`, `TMPDIR=CIRCLE_TEST_SCRATCH=S`. `PDE_TEST_DEVICE` and `CIRCLE_TEST_DEVICE` were both set to `cpu` or both to `cuda:0` for their respective phases. `S/commands.json` retains the exact absolute commands, environments, statuses and process wall times; each named `.log` retains complete output. The bounded harness was invoked as `python -B S/run_checks.py cpu` and `python -B S/run_checks.py cuda`; CUDA received authorized tool escalation.

Torch commands used `/home/amir/miniconda3/bin/python` (Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130). cuda:0 was an NVIDIA GeForce RTX 3090 with 24124 MiB reported memory. Default `python` was Python 3.10.12 / NumPy 1.26.4 without Torch.

| Actual command/check (under stated environment) | Result |
|---|---|
| Default Python: `import pde`; assert Torch absent from loaded modules | Pass; R/code package |
| Conda Python: import all five new public modules and enumerate loaded pde module paths | Pass; assigned dependencies only |
| `code/tools/check_library.py` | Pass, 67 files |
| `code/tests/test_library_boundary.py` | 5 tests pass |
| `code/tests/test_observable_torch_circle.py`, CPU then cuda:0 | 4 tests pass on each |
| `code/tests/test_general_p1.py`, CPU then cuda:0 | 16 tests pass on each |
| `S/guide_checks.py` | All three new Python examples pass; all seven added file links and both section fragments resolve |
| `code/scripts/validate_torch_circle.py --device cuda:0 --output data/established/integration_review_final/circle` | Complete; all three orders restart exactly |
| `code/scripts/example_general_p1.py --device cuda:0 --output data/established/integration_review_final/general_a` | Complete |
| Same producer with fresh `general_b` output | Complete |
| `code/scripts/analyze_general_p1.py --run data/established/integration_review_final/general_a --repeat data/established/integration_review_final/general_b --output data/established/integration_review_final/general_analysis.json` | Pass; exact repeat arrays and independent NumPy replay |
| Default Python discovery of `test_general_p1.py` | **Fails**, required correction R1 |

Thus 45 executed tests passed in Torch-equipped environments; the separate optional-dependency discovery check failed. Tests substantively cover dense Cholesky/response coefficients, independent samplewise NumPy and autograd oracles, weighted energy, physical finite-network scaling, actual-transpose contractions, simultaneous Heun, unequal populations, ownership/mutation, signed nontrivial folding, zero/nonunit/duplicate inputs, float32, restart and diagnostic edge cases. No skipped Torch test was counted as passing.

Circle maximum CPU-reference discrepancy was `1.734723475976807e-18` against `2e-11`; all three exact-restart flags were true. Its retained state sizes were 4080, 18912, 82944 bytes; peak CUDA allocation was 34,144,768 bytes, below the declared 1 GiB cap. General NumPy replay maximum discrepancy was `1.1102230246251565e-16`, within the analyzer's tolerances; all repeat observation arrays matched exactly. Retained closure/network tensor counts were 2016/5120 bytes; each general run peaked at 33,610,752 CUDA-allocated bytes. These are tiny-run operation records, not comparative speed or neural-fidelity evidence. Total supervised subprocess wall time, including the failed discovery, was 20.8265 seconds; longest subprocess was 2.6201 seconds. No resource limit was approached. Torch emitted a deprecation warning for its older TF32 control API; execution succeeded.

Fresh producer records contain source/output hashes. `S/results_summary.json` retains the reported measurements, and `S/evidence_hashes.json` fingerprints the review's logs, check sources and E outputs. Frozen-manifest integrity was rechecked after execution. Existing historical empirical results in unchanged guide text were not rerun, and no conclusion here relies on them. I did not test other accelerators, Torch versions, higher circle orders, other dimensions' neural convergence, large training campaigns or arbitrary numerical extremes.

## Completion

Complete assigned reading and bounded integration checks are finished. Required correction: R1 only. No additional unresolved mathematical, preservation, interface or placement objection was found in the assigned scope. Optional suggestions: none required for this review. Retain this original report and its failure evidence when preparing the corrected edition. This report neither replaces the paired scientific reviews nor authorizes live promotion.
