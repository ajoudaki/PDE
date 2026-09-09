# Bounded implementation: F1–F4

Status: **implemented and frozen for independent review**. The original NOT CLEAN review remains byte-identical. This implementation record does not replace that verdict or claim historical scientific reproducibility.

## Changes

- **F1:** `mfp_linear_growth_uniform_counterexample/full_l2_paired_transition.py` now names the routing object `STUDY_PATHS`. The mathematical `PATHS` tuple and every compiler body remain unchanged. Its actual absolute-path `--help` succeeds from an external working directory; a separate mocked call verifies neither compiler is called.
- **F2:** Added a CLI refusal before ordinary imports and a refusal as the first callable-writer statement in all six identified writers: scalar independent `forward_contraction.py`, `reverse_contraction.py`, `moving_contraction.py`, and `build_full_report.py`; scalar multi-observable route-A `gamma04_contraction.py`; and observables independent `gamma04_contraction.py`. Original writer bodies, formulas, payload serialization, and digest expressions remain in place behind the guards. No replacement output or seal workflow was introduced.
- **F3:** `order5/run_checks.py` and `order5/audit_hostile.py` now refuse both direct CLI execution and callable `run()` entry before any checks. Pure modules and individual tests remain separately importable.
- **F4:** Scalar independent `depth_assembler.py::_read_accepted()` explicitly reads the frozen H2/H3/H4 comparison maps under `data/historical/studies/mfp_gaussian_calculus`. Only its root declaration and explanatory docstring changed. Both existing map schemas, coefficient parsing, and all comparison/recurrence bodies remain identical. No formula/proof payload was moved. The shared reference loader and its expected hashes/counts were not modified.

Exactly **10 existing source files** changed, plus **2 new narrow test files**:

- [Gaussian guard and retained-input tests](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/test_migration_retired_interfaces.py)
- [Linear producer routing tests](/home/amir/Codes/PDE/studies/mfp_linear_growth_uniform_counterexample/test_migration_paths.py)

The [private implementation manifest](/tmp/pde-gaussian-routing-final.bJLzzv91/implementation_manifest.json) lists every changed repository-relative path with exact before/after SHA-256 hashes; new files have a null before hash. No Git operation, source documentation edit, data write, dependency installation, or historical seal/hash reset occurred.

## Verification

**17 bounded tests passed:** eight new regression tests plus the nine existing Gaussian path tests. The archive CLI test covers all eight retired writer/runner commands from an external temporary directory using isolated Python without site dependencies. Callable tests install filesystem and scientific-work tripwires, including explicit scratch arguments to `emit()`. Tiny mocked map fixtures exercise both retained schemas, all three historical paths, the comparison's loader dependency, and missing/malformed input failure.

Command, executed with all temporary files confined to the private directory:

```text
TMPDIR=/tmp/pde-gaussian-routing-final.bJLzzv91 PYTHONPATH=/home/amir/Codes/PDE python -B -m unittest studies.mfp_linear_growth_uniform_counterexample.test_migration_paths studies.mfp_gaussian_calculus.test_migration_retired_interfaces studies.mfp_gaussian_calculus.test_migration_paths -v
```

The actual linear producer command also passed independently:

```text
python -B /home/amir/Codes/PDE/studies/mfp_linear_growth_uniform_counterexample/full_l2_paired_transition.py --help
```

No coefficient generation, recurrence compilation, experiment, empirical reanalysis, GPU work, or report production ran. Only Python import/parsing, guard/help calls, and tiny mocked fixtures ran. The original trailing blank line in the package runner was restored after the tests; this changes no parsed program behavior.

## Preservation and freeze evidence

[Preservation results](/tmp/pde-gaussian-routing-final.bJLzzv91/implementation_preservation.json) pass for all ten modified source files. The private checker reconstructs each entire expected file from its before snapshot using only the permitted routing/docstring/guard insertions and compares it byte-for-byte with current source. Removing precisely those interface changes also restores an identical complete AST. Thus the original mathematical bodies, tuples, expected constants, serialized payload definitions, and digest expressions are preserved, including unreachable historical writer bodies.

The implementation baseline contains 485 repository snapshot files plus the immutable review. The final comparison finds only the ten authorized source changes and two new tests: **476 pre-existing snapshot entries remain byte-identical**, including the review. No unrelated changes were detected in that enumerated set. The original review hash is recorded before and after in the implementation manifest. Existing source/provenance seals were not updated to endorse the modified source; any resulting historical digest failures remain explicit limitations.

Private evidence consists of `implementation_before.json`, `implementation_preservation.json`, `check_implementation_preservation.py`, and `implementation_manifest.json`. Source and tests are frozen at the manifest's after hashes; further changes are left to the independent review process.
