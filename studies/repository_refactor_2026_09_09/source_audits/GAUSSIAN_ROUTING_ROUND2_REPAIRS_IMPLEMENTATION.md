# F1–F5 implementation handoff

Implementation complete; all 21 bounded tests pass. This is an implementation-worker handoff, not an independent review or scientific validation. No commits were made.

## Changes

- F1: `reduce_frozen_head.main()` now refuses before reduction, source reads, or writes. Direct CLI dispatch enters this guarded callable. The existing pure `reduce()` function is unchanged; the old writer body is preserved beneath the refusal.
- F2: `build_self_contained_report.build()` now has the same pre-work archive refusal as its CLI `main()`. `build_bytes()` remains available and unchanged.
- F3: the compiler check reads both frozen comparison JSON files from `HISTORICAL_ROOT / "order5"`. Its existing comparison assertions are unchanged.
- F4: the Stieltjes validator maps six exact labels—two basenames, two former repository labels, and two maintained labels—to the two maintained hidden-recurrence source files. Unknown/traversing labels refuse before reads. The digest comparison still uses the unmodified expected digest in the input document.
- F5: Gaussian `require_output` delegates to shared `StudyPaths.require_output`. Dirac's completed shared-helper update rejects existing symlink components/children and existing hardlinked files. The Gaussian consumers now consistently reject both child-alias kinds before scientific work or input/output operations. Valid generated defaults and unaliased scratch still work.

I did not edit `studies/_output_paths.py`. The final integration tests used Dirac's helper at SHA-256 `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e`. Before that change arrived, the hardlink regression failed; after the shared update all 21 tests passed without adding duplicate Gaussian link-validation code.

## Exact changed-file hashes

The table lists all eight files changed by this worker. SHA-256 values are complete. All repository paths are under `/home/amir/Codes/PDE`.

| File | Final SHA-256 |
| --- | --- |
| [Gaussian frozen-head writer](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_observables/independent/reduce_frozen_head.py) | `b4bbc0723e476cf312bb57f4e73b2364837ebc4d219a2e72be8b995a072012e6` |
| [Gaussian report writer](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5/primary/build_self_contained_report.py) | `dd00192dbdd61b0618faa843595314ee7c5ae46ebdb5035c3c315bba03c5fb2f` |
| [Compiler retained-input check](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/compiler/test_population_jet.py) | `1688771f624db74d206e14f23457f92b90b37f7b2d2ad9e7da47e66093969f1d` |
| [Gaussian output guard](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/study_paths.py) | `aea6795fae0b4429d7f23e120c5c1e662084f189298db897caec54acfdbf531a` |
| [Stieltjes source-role validator](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py) | `75465c1de279d4e6b0cdd8f7bd1d0a583a77b10d6ecf875af5ee238e90eefbb4` |
| [Gaussian routing regressions](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/test_migration_paths.py) | `763ad9e3fe6919110ad62f06b4f2314e9ae17623fb060e7f94be8191ab242825` |
| [Gaussian retirement/dispatch regressions](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/test_migration_retired_interfaces.py) | `af21c7634bf88b5b8a7521e6b145a0075e25b5e253825d961bea40bb346cdf12` |
| [New Stieltjes migration regressions](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/test_migration_paths.py) | `df00e0e5ee74fd36fd9d513f22f7a820bd98717c4a99f1691d9c27658625292e` |

## Bounded validation

```text
python -B /tmp/pde-gaussian-routing-implementation.4Vx4c9sn/run_tests.py
Ran 21 tests in 0.248s
OK — failures=0, errors=0, skipped=0
```

The private runner restricts writes to this temporary directory and disables bytecode writing. It runs only these inspected modules:

```text
studies.mfp_gaussian_calculus.test_migration_paths
studies.mfp_gaussian_calculus.test_migration_retired_interfaces
studies.stieltjes_resolution.canonical_hidden_high_order.test_migration_paths
```

The tests cover:

- Ten retired CLI/callable interfaces, including the two newly guarded writers. Actual CLIs run from external temporary working directories with `-B -I -S`; callable tripwires reject any scientific or filesystem work after import.
- The compiler package's actual first dispatched check, which reads the two retained JSONs and checks existing flags/counts. Every subsequent scientific test is replaced by a stopping tripwire; the full mathematical suite does not run.
- Actual Gaussian output guards and H3 sine/curvature/postprocessor/comparison callers against tiny private symlink and hardlink fixtures. Rejection occurs before reading inputs, creating outputs, or running science; fixture retained bytes remain unchanged.
- Exact legacy/current/basename source-label selection; unknown and traversal rejection; and unchanged wrong-digest rejection. The successful source-role cases use tiny byte fixtures only.
- The two actual Stieltjes retained source records now read the maintained files and still fail their original frozen source-hash gates. This preserved failure is explicitly asserted, not waived.
- The pre-existing tiny Gaussian postprocessor fit and empty-map serialization fixtures, with scientific producers mocked, plus historical coefficient-reader schema/refusal fixtures.

`git diff --check -- studies/mfp_gaussian_calculus studies/stieltjes_resolution` passes. All 176 current Python files in the two implementation trees compile in memory. No coefficient generation, science experiments/reanalysis, recurrence evaluation, native compilation, installation, GPU/training work, or seal reset occurred. Optional-dependency limitations from the review remain; no full scientific or historical replay is claimed. Link protection is for existing aliases, not a malicious concurrent filesystem race.

Full test log: [tests.txt](/tmp/pde-gaussian-routing-implementation.4Vx4c9sn/tests.txt). Machine-readable summary: [tests.json](/tmp/pde-gaussian-routing-implementation.4Vx4c9sn/tests.json).

## Preservation proof

Full before/after inventories cover both implementation source trees and their corresponding retained data. They include exact file hashes and AST hashes for every existing top-level function. The shared helper is recorded separately because it belongs to Dirac.

- [before.json](/tmp/pde-gaussian-routing-implementation.4Vx4c9sn/before.json): SHA-256 `8feaf3c4232d7b6e9d8ba989f9bcec97c2ef4f0ea1d525b787be610ba37352ca`.
- [after.json](/tmp/pde-gaussian-routing-implementation.4Vx4c9sn/after.json): SHA-256 `cc28ed05545848172400cfa4e2b9d1a7bee0ea96c1b5d3da7b9d3cf621dae6fe`.
- [preservation.json](/tmp/pde-gaussian-routing-implementation.4Vx4c9sn/preservation.json): complete changed-file before/after hashes and changed-function inventory.
- [verification.json](/tmp/pde-gaussian-routing-implementation.4Vx4c9sn/verification.json): asserted preservation results.

Of 1,089 existing top-level functions, 1,085 are identical at the AST level. The only four changed existing functions are the report writer `build`, the retained-comparison path check, Gaussian `require_output`, and Stieltjes `validate_source`. Removing the single new `raise` from `build` reconstructs its original AST exactly. The pure `reduce()` AST is unchanged at SHA-256 `b61f34089c6424f6a885354d0f380521e97eb3d7e7c12a623fb6b69a1d2c45b4`.

Every pre-existing 64-character hexadecimal digest literal in Python source is unchanged. Every retained-data file and every non-Python source payload—including formulas, proofs, reports, manifests, seals, and pre-existing bytecode—is byte-identical to the implementation baseline. No documentation/core files were edited by this worker.

The two current hidden-recurrence source hashes remain `0597f9f291f9b39d5e39b6fe7d7f0d27e63c23f363b052cd1b20ab707d86625b` (production) and `a18dea37e4bb0f346012e9ce33d2de1124efadf872585917ee76879e2462c161` (independent). Their retained expected digests remain `d49a8a19cbe2cd31699776d1359d947ec4f3f825eef06346c0e81331b5777530` and `fd923a6bff5e7f6d3f09a56f8a2ec208068615e7545c7e2d31178dd7c4817893`, respectively. Correct routing has not converted these historical validation failures into passes.

Ready for a fresh different reviewer. Existing copied review/evidence artifacts were left untouched.
