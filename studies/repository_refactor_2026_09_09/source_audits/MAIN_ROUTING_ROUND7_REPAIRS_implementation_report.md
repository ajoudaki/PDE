# Three-blocker implementation handoff

Implemented exactly the three assigned repairs. Bounded interface validation passes. This does not revise or replace the previous acceptance report: that report remains unchanged with its exact **NOT CLEAN** verdict for the reviewed pre-repair source.

## Changes

- [Campaign 1 runner](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py:106): the existing `require_distinct_output` preflight now includes the consumed `graded_sector.cpp` provenance source, alongside the lower result and executable. It runs before hashing or sector dispatch. Ordinary distinct exports remain refreshable.
- [Centered-depth publisher](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py:197): imports the existing guard and checks the concrete `RESULTS.json` destination against both its source and protocol before computation. The later output assignment was moved into this preflight; the calculation and publication bodies otherwise remain unchanged. A separate existing result can still be refreshed.
- [Long-horizon wrapper](/home/amir/Codes/PDE/studies/resnet_dense_long_horizon/reproduce.sh:8): invokes the existing stdlib output validator once, before its first test/science dispatch, and forwards the single normalized root to both `run_all.py` and `make_manifest.py`. Default, home-expanded, relative, and spaced paths are covered.
- Added five bounded regression methods in [test_quadratic_routing.py](/home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_quadratic_routing.py:185) and [test_resnet_routing.py](/home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_resnet_routing.py:496). `test_metadata_routing.py` was not changed.

Exactly five repository files were edited: the three assigned implementation files and those two assigned test files. No Gaussian/identity file, `test_gaussian_consumer_routing.py`, shared helper, unrelated writer, seal, or budget was edited. No commit was made.

## Verification

Executed only the three inspected routing test modules: **56 tests passed, zero failures, zero errors, zero skips, 7.464 seconds**. [Full test log](/tmp/pde-three-blocker-repair.TpFZAx1b/bounded_tests.log) and [machine-readable result](/tmp/pde-three-blocker-repair.TpFZAx1b/bounded_results.json).

New regression cases exercise:

- Campaign 1 source collisions through the same name, symlink, hardlink, and parent-directory alias; refusal precedes any hashing or sector work.
- Centered source and protocol collisions through symlinks, hardlinks, and dangling links, in both normal and long-search argument modes; refusal precedes scientific work.
- Complete centered `main()` publication twice with all scientific routines mocked, preserving both provenance inputs while refreshing an ordinary result.
- Actual centered module bootstrap and guard binding, with external identity/scientific imports mocked so their source is neither read nor executed.
- A wrapper recorder that delegates only the stdlib validation query. It verifies exactly one query, no test/science dispatch on rejected roots, and three recorded downstream commands with the same normalized root for valid selections. No study tests, experiments, or manifest generation are dispatched by the recorder.

The two formerly excluded `CAMPAIGN_REPORT.md` and `SECTOR_ENGINE.md` tests also passed. Those documents were permitted only while their specific path-command tests were active; their shell snippets received syntax/path inspection only. No compiler or scientific command ran, and no conclusions were drawn from those documents.

## Preservation evidence

[preservation.json](/tmp/pde-three-blocker-repair.TpFZAx1b/preservation.json) verifies that each implementation file differs from the captured starting source by exactly the specified guard/import/assignment or wrapper-validation insertion. All 14 non-main calculation/helper functions in the two Python implementation files are byte-for-byte unchanged. The full original calculation text inside each `main()` is also retained by the exact replacement check. Frozen digest constants, regression values, hash-failure branches, and resource limits are unchanged.

The captured shared helpers, manifest validator, `graded_sector.cpp`, and metadata test have unchanged file hashes. The 218 inputs read by the bounded test run have identical hashes before and after that run; this includes the explicitly permitted historical path/digest inputs, without reading historical arrays.

Implementation files necessarily have new source-file hashes; no historical digest or source seal was rewritten to match them. [Before snapshot](/tmp/pde-three-blocker-repair.TpFZAx1b/before.json), [after snapshot](/tmp/pde-three-blocker-repair.TpFZAx1b/after.json), and [repair diff against this worker's starting source](/tmp/pde-three-blocker-repair.TpFZAx1b/repair.diff) are private handoff artifacts.

All temporary files and caches were under the private `mktemp` directory `/tmp/pde-three-blocker-repair.TpFZAx1b`, with bytecode disabled. Tests used AST/mocked boundaries, inert transport fixtures, stdlib path checks, and wrapper recording. No training, actual scientific calculation, coefficient generation, reanalysis, native build, installation, production seal generation, or reset was performed. The checks do not promise resistance to malicious concurrent filesystem changes or scientifically certify the studies. Disjoint Gaussian integration remains with the main coordinator.
