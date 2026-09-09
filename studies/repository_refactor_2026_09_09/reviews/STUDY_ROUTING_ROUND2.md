# Migration-interface acceptance: NOT CLEAN

Reviewed 2026-09-09 against the current allowed source snapshot. **NOT CLEAN:** four concrete write-boundary defects remain. The ordinary generated-data destinations mostly agree across producers and immediate consumers, and all **41 supplied bounded tests pass**. Independent private fixtures nevertheless reproduced retained-input corruption and an unchecked failure-writer path escape. Passing the supplied tests is therefore insufficient for this acceptance.

No repository or historical file was written. No training, GPU work, compiler, coefficient generation, campaign, scientific reanalysis, installation, or real seal generation was performed. No authorization was refreshed, no attempt was reset, and no failing live gate was patched to pass. All diagnostic writes stayed under `/tmp/pde-study-routing-round2.Rz1tF1e3`.

## Blocking findings

### 1. Stage-V timeout finalization accepts paths as point IDs and escapes its generated tree [P1]

Source: [run_stage_v_point.py:183](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py:183), [early CLI dispatch:211](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py:211).

`main()` dispatches `--finalize-timeout` before checking that `--point` is one of the two frozen point IDs. `finalize_timeout()` computes `RUN_ROOT / point_id / "manifest.json"` without validating or resolving containment. An absolute point discards `RUN_ROOT`; a relative point containing `..` can also escape it. If the selected manifest says `status="running"`, the function rewrites it as `failed_inconclusive_external_timeout` and returns 0. Neither the normal source/unlock checks nor the historical-attempt guard is reached.

The independent fixture reproduced both absolute and relative escapes into a **private toy historical directory**. The relative argument was `../../../../../../historical/studies/stieltjes_hybrid_campaign/retained-point`. Both returned 0 and changed the retained manifest's bytes and status. The real `main`, `finalize_timeout`, JSON reader, clock, and atomic writer functions were compiled from current source; no GPU functions or gate substitutes were provided. This is a failure-path contract violation through a purported point identifier, not a complaint about a deliberately inappropriate standalone `--output` flag.

The shell wrapper restricts its own point arguments to the two known IDs, but the Python CLI and callable finalizer remain exposed. The fixture proves those interfaces, not a bypass of the shell's case statement. Because torch is absent, this is an AST-level execution of the CLI/writer path, not a successful full-module torch import.

Acceptance requires validating the point ID, resolved destination, and corresponding generated attempt before mutation. Historical records must remain outside this failure path; this finding does not authorize renewing any source lock.

### 2. Finite-width helper accepts a directory whose output archive aliases the retained input [P1]

Source: [run_paths.py:26](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_paths.py:26), [jet_control_variate.py:183](/home/amir/Codes/PDE/studies/stieltjes_finite_width/jet_control_variate.py:183), [first archive write:199](/home/amir/Codes/PDE/studies/stieltjes_finite_width/jet_control_variate.py:199).

`parse_paths()` checks the resolved output **directory** against the owning generated tree, but does not check its children. `jet_control_variate.main()` subsequently loads `raw_width_64.npz` and writes `jets_and_cv_width_64.npz` with a truncating NumPy writer. An existing output child that is a symlink **or hardlink** to the selected raw input passes the directory check and destroys that input.

The fixture used the actual parser and actual `main` body with toy repository roots confined to this review directory. The selected output was the toy owning generated tree. Selecting the toy historical directory directly was correctly rejected, while an output child linked to the raw input was accepted. After the first write, the raw archive's fields had changed from `pair_g,times` to `jets,corrected`:

```text
before SHA-256: a20099271ae7a73d97641f1b2663163f3f36b823fa6c6c35c8b4f8a83e4881db
after  SHA-256: 7af7861fa8527d49dcb47368fa1a0e09ec525a36007113174788762bff119747
```

Both link variants reproduced the same loss. `regenerate_pair_jets` was replaced with a fixed 1-by-4 zero array; execution stopped immediately after the first real tiny NPZ write. No jets were generated and no fitting or bootstrap ran. Toy `OUT`, `RUN`, and repository constants supplied the fixture locations; this tests the real helper/consumer behavior, while the current default root strings were checked separately.

Acceptance requires checking concrete output leaves and their aliases to selected retained inputs before work, and publishing without truncating an existing linked file. Merely rejecting a historical directory as the top-level `--output-dir` does not satisfy the restriction.

### 3. Generalization directory checks do not protect intermediate writer files [P1]

Source: [generalization_paths.py:32](/home/amir/Codes/PDE/studies/resnet_generalization/generalization_paths.py:32), [run_exact_reference.py:243](/home/amir/Codes/PDE/studies/resnet_generalization/run_exact_reference.py:243), [run_pde.py:379](/home/amir/Codes/PDE/studies/resnet_generalization/run_pde.py:379), [analyzer writer:1213](/home/amir/Codes/PDE/studies/resnet_generalization/analyze_generalization.py:1213).

`require_output()` resolves the selected path and checks root ownership. Both raw producers validate their output directory, then open a predictable `<archive>.npz.partial` in `wb` mode. The analyzer similarly validates its selected destinations at lines 1402–1408, but `_atomic_bytes()` opens `<deliverable>.partial` in `wb` mode without checking that intermediate path. A pre-existing intermediate symlink or hardlink can therefore redirect the write into retained data even though the nominal directory and final filename are acceptable.

Two independent demonstrations were made:

* The complete current `run_exact_reference.run` function and parser were executed with their default output selection in a toy generated tree. Only `_one_seed` was replaced by fixed tiny arrays; no model or training code was executed, and no PDE seal was supplied or created. A pre-existing archive `.partial` symlink redirected the writer into a private retained file. The retained bytes became identical to the newly published NPZ.
* The real analyzer `_atomic_bytes` function was executed after the real destination checks, with a linked `summary.json.partial`. Both symlink and hardlink variants overwrote the private retained file. This tests the callable writer and its destination check, not a successful full frozen analysis.

The raw-writer fixture changed the retained file hash from `f80b5128736743973807d806474bb9e1a0f487a83d5dc43612dc14234b4c77b4` to `16010e1d3c019da3b69e110f4b5172ffd9028cb924bdac059f74deee185a414c`. No concurrent race or malicious source edit was needed; the intermediate link existed before validation.

The generalization **combiner does not share this demonstrated failure**: it checks final/partial collisions before input loading, checks again before publication, and creates its partial exclusively. Its supplied alias and late-collision tests all passed.

Acceptance requires validating and exclusively creating intermediate files, with concrete input-alias protection where needed. The frozen grid currently refuses on source hashes; that valid refusal must remain. The standalone raw writer's boundary and the analyzer's callable writer can be assessed without waiving it.

### 4. Shared safety helper misses hardlinked children used by truncating consumers [P2]

Source: [shared restriction and check:29](/home/amir/Codes/PDE/studies/_output_paths.py:29), [simulate_loewner.py:382](/home/amir/Codes/PDE/studies/stieltjes_direct_loewner/simulate_loewner.py:382).

`StudyPaths.require_output()` rejects protected resolved roots and recursively rejects symlinks inside an existing output directory. It does not detect hardlinked regular files. `simulate_loewner.main()` calls that helper and immediately opens `run.log` in `w` mode. An accepted generated directory containing a `run.log` hardlink to a retained log therefore truncates the retained inode before any model work.

The fixture used the actual shared helper and the exact first five statements of `simulate_loewner.main`, stopping after opening and closing the log. A private toy historical log changed from SHA-256 `4cf45a1ae49e5672d53678c3e61883737ca8a82d054f6edfa1bb384935ebbad7` to the empty-file hash `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. This requires an existing hardlink and writable retained inode; it does not assert such a link is present in the live repository. A filesystem mounted read-only would provide additional protection, but the advertised helper restriction is not enforced by this consumer.

Acceptance requires preventing in-place truncation of linked existing leaves, or refusing them before opening. A directory symlink scan alone is insufficient.

## Routing and gate coverage

The following summarizes inspected interfaces, not scientific validation of the campaigns. Paths beginning with `data/` are relative to `/home/amir/Codes/PDE`.

| Interface | Current routing / result | Evidence and limit |
| --- | --- | --- |
| Generalization grid → precheck → verifier | All use `data/generated/resnet_generalization/results/generalization`. The precheck subprocess receives an explicit `--results-dir`; evidence labels round-trip against the generated evidence root. | Seven migration tests passed; grid continuation, dense-stage commands, seal lookup, verifier inventories, and both reproduction drivers inspected. No grid stage or real sealing executed. |
| Generalization precheck historical mode | `--historical` explicitly chooses retained results and defaults its decision output to generated `historical_review`. Protected output paths reject during parsing. | Tiny selected archive, input forwarding, label escape rejection, and default selection tested. The scientific numerical decision was not computed. |
| Generalization analysis / processed verifier | Defaults agree on processed files, figures, and generated-root `REPORT.md`; verifier interprets that report label against the generated evidence root. | Inspected writer/seal/verifier label agreement. Frozen analyzer wrapper currently refuses; processed pipeline not executed. Intermediate-file boundary fails as described above. |
| Generalization reference combiner | Owning generated tree or external scratch. Rejects equal, normalized, symlink, and hardlink input aliases and occupied final/partial paths before input loading. | Seven boundary tests passed, including tiny pooled output/provenance, dangling links, late partial insertion, and exclusive partial creation. No assertion of race-proof concurrent publication. |
| Proxy offline analysis CLI / callable writer | Explicit input/config/output arguments. CLI validates final and `.tmp` occupancy before `analyze_pilot`; success and exception paths share `write_json_atomic`. Writer independently checks ownership and collisions and uses exclusive temporary creation. | Eight boundary tests passed in both direct and package import modes. Scientific dependency/package was stubbed; actual CLI/helper/writer source executed. Success returned 0, analysis-invalid failure 2, other failure 1; failure JSON shape preserved. No frozen bootstrap/reanalysis. |
| Proxy producer / shards / merger | Reference producer defaults to generated `reference/runs`; run ID must resolve to a direct child. Shards and immediate merger agree on generated `reference/side_checks`; merger has explicit historical-input selection. | Source inspection of producer, FP32 wrapper, capped launcher, side checks, and merger. Production checks precede directory creation. No torch imports, reference run, or shard analysis. Fixed historical RK4 comparisons are retained-input tools, not fresh default trajectory sources. |
| Finite-width producers / consumers | Five campaign outputs point to the owning generated tree. Fresh-pair output matches positive-time input; corrected-clock output matches jet-CV input. Historical replay defaults to a distinct generated review tree. | Five migration and two boundary tests passed. Missing selected inputs checked before work. Compiler-dependent imports and campaign bodies not run. Jet child-alias defect reproduced independently. |
| Direct Loewner | Main, corrected-clock, pilot, and blowup-diagnostic destinations are generated. Corrected-clock producer and finite-width jet consumer agree. | Static entry-point inspection, plus the shared-helper hardlink fixture. No simulation, log creation at a live default, or numerical analysis. |
| Hybrid successive analyses | Fresh arrays/manifests default together under generated; historical arrays and source-retained manifests have separate roots. Comparison forwards both roots to both widths. Outputs are restricted to this study's generated tree or scratch. | Nine migration and two boundary tests passed. n8192 transformation refuses its changed n4096 analyzer before work/output. No transformation digest was changed and no analysis ran. |
| Hybrid FP64 legacy runtime | Four FP64 commands and two successive-width runners refuse before work. Attempt reservation and external failure finalization have explicit guards. | In addition to supplied AST checks, all six actual script entry points were run with `runpy`: each stopped at the archive-only guard before torch import. No watchdog, ledger, GPU, or result mutation. |
| Hybrid Stage V | Normal path checks source lock and generated-root unlock binding, and reservation checks the historical ledger. Timeout path has the separate defect above. | Source/manifest inspection; timeout writer only in private fixtures. Normal source mismatch and old unlock-root mismatch must not be waived. |
| Other hybrid breadth / width / bounded tools | One-/two-input point runners bind source locks and unlock paths before attempts. Width-ladder shell still supplies its old source-local run root; production runner requires its lock/unlock before directory creation. Bounded DMFT utilities print by default unless given an explicit output. | Static inspection only. Historical locked destinations are not permission to resume, reset attempts, or issue new authorization. Generic explicit standalone output flags alone were not counted as defects. |
| Proof audit | Common producer, structural producer, driver, analyzer, and verifier use generated `resnet_proof_audit/results`. Historical status is non-authorizing; explicit historical analysis writes a separate generated review. Freeze creator refuses a retained historical seal. | Source inspection; only the supplied one-test trapezoid compatibility suite executed. No proof-audit experiment, broad test suite, or historical scientific analysis. |
| Activation controls | Orchestrator, raw producers, analyzer, and figure consumer use generated roots. Figure reader explicitly supports historical compact evidence. Input-manifest creation refuses renewal from an existing retained seal. | Source inspection. Full `validate/all` was not run: it runs broader scientific tests before manifest handling. Raw producers use the shared helper; no blanket alias-safety claim follows for all consumers. |
| Root `.gitignore` | `/data/*`, array extensions, `outputs/`, and `runs/` exclude generated products from ordinary tracking. | Read-only inspection. Ignore rules do not enforce write safety or authorization. |

## Advertised reproduction limits

Current commands and prose are not uniformly reconciled. The generalization [README:89](/home/amir/Codes/PDE/studies/resnet_generalization/README.md:89) still says the full run writes source-local `results/generalization`, although its code and earlier README migration paragraph use `data/generated/resnet_generalization`. Its two reproduction drivers also differ: the README advertises the original driver, whereas `REPRODUCTION.md` advertises the post-freeze driver. The latter verifies source first; the former runs tests before its grid source check. Neither was executed here.

Activation [README:75](/home/amir/Codes/PDE/studies/resnet_activation_controls/README.md:75) still advertises source-local `results/` and a clean fresh freeze, inconsistent with current generated paths and the historical-seal refusal. Finite-width and direct-Loewner READMEs still point to local `runs/`. Proxy analysis README's explicit completed-run command is marked historical, so its old output flag alone is not a defect; its current “from the repository root” test command and the reference README's validation commands still name `studies/stieltjes_conjecture/numerics/global_proxy_campaign`, not the current source directory. These are documentation/interface limits, separately from the four demonstrated write defects.

Live source verification returned **`frozen source mismatch: README.md`**. The dense amendment stopped at **`frozen run_grid.py hash mismatch`**; the analysis amendment stopped at **`frozen analyzer hash mismatch`**. The n8192 analyzer/comparison similarly rejects the changed frozen base analyzer. These are real, correctly enforced reproducibility limits, not grounds to waive checks or regenerate seals. The restored environment record describes Python 3.12.13 / NumPy 2.3.5 from 2026-07-23; this diagnostic runtime was Python 3.10.12 / NumPy 1.26.4.

## Reproducing this acceptance

All scripts and logs referenced here are private diagnostics in this directory. Run the independent probes with:

```bash
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPYCACHEPREFIX=/tmp/pde-study-routing-round2.Rz1tF1e3/pycache \
python /tmp/pde-study-routing-round2.Rz1tF1e3/adversarial.py
```

The observed fixture paths, before/after content hashes, statuses, and six real archive refusals are in [adversarial-results.json](/tmp/pde-study-routing-round2.Rz1tF1e3/adversarial-results.json). Its successful completion means the described observations were reproduced; it does **not** mean acceptance passed. Each run constructs and removes its own small toy fixtures. Timestamps and temporary path names vary.

Run each supplied suite separately with:

```bash
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPYCACHEPREFIX=/tmp/pde-study-routing-round2.Rz1tF1e3/pycache \
python /tmp/pde-study-routing-round2.Rz1tF1e3/bounded_tests.py STUDY_TEST_PATH
```

| `STUDY_TEST_PATH` | Passed |
| --- | ---: |
| `studies/resnet_generalization/tests/test_migration_paths.py` | 7 |
| `studies/resnet_generalization/tests/test_output_boundaries.py` | 7 |
| `studies/stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py` | 8 |
| `studies/stieltjes_finite_width/test_migration_paths.py` | 5 |
| `studies/stieltjes_finite_width/test_output_boundaries.py` | 2 |
| `studies/stieltjes_hybrid_campaign/breadth_panel/test_migration_paths.py` | 9 |
| `studies/stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py` | 2 |
| `studies/resnet_proof_audit/tests/test_trapezoid_compat.py` | 1 |

Final per-suite logs are named `studies__... .log` without the space. Initial `*.harness-initial.log` files retain diagnostic-harness failures: the first guard misinterpreted descriptor-relative temporary cleanup and blocked NumPy testing's optional CPU-feature subprocess probe. The harness was corrected, the probe alone was stubbed, and all affected suites were rerun. Those initial failures are not source findings. Small leftover initial fixtures are confined here. No campaign subprocess was allowed by the diagnostic guard.

The supplied generalization tests create **synthetic** seal-shaped JSON solely in temporary directories and mock their synthetic fixture authorization. Those records were never live authorization and did not refresh any existing seal. AST checks elsewhere extracted only the stated path/hash/writer functions. No result here establishes full optional-dependency imports, training behavior, mathematical correctness, statistical validity, or complete historical reproducibility.

## Input integrity and isolation

Exactly **118 inspected source/document/config inputs** were SHA-256 recorded before first inspection or test import and rehashed after the checks. **118/118 match; zero changed.** Full exact maps:

* [input_hashes.before.json](/tmp/pde-study-routing-round2.Rz1tF1e3/input_hashes.before.json)
* [input_hashes.after.json](/tmp/pde-study-routing-round2.Rz1tF1e3/input_hashes.after.json)

The maps include every input opened by the bounded test import/read guard. Hashing a whole file does not mean its scientific contents were fully audited: large modules were inspected around imports, path construction, callers, validation, and writes. No prior review, chat, audit report, research report, other study source, or historical trajectory was used. References in permitted READMEs and frozen manifests were not followed into excluded material. Out-of-scope compiler/theory dependencies were identified from import/path strings only. No network access or package installation was used.

The verdict is limited to the current migration interfaces and the stated adversarial filesystem conditions. It makes no claim that the demonstrated links already exist in live data, that an actual retained artifact was damaged, or that the frozen campaigns can be reproduced in this runtime.
