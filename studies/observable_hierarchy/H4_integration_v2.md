# H4 frozen integration review v2 — INCOMPLETE, STOPPED

Reviewer: `/root/h4_integration_v2`, a fresh isolated review context. Frozen edition: `data/generated/observable_hierarchy/H4_candidate_v2b`. Input manifest: `studies/observable_hierarchy/H4_review_manifest_v2.json`, SHA256 `873de70c02d4d198613688791b0f430c3d92ee7f4dfd3fcecc26eeaa6c6187c5`.

**This is an incomplete original report, not an integration PASS or a completed promotion review.** The coordinator stopped further v2 review work because the complete guide still contains an unrepaired all-tests recipe and the edition will be superseded. No further tests or scientific reads were undertaken after that instruction; only evidence preservation, input rehashing and this report were completed. A corrected edition requires a fresh complete integration review.

## Predeclared plan and actual resources

Before testing I recorded: at most 600 CPU seconds total, 4 GiB address-space limit for numerical children, one numerical thread, zero research trajectories. Planned work was relevant deterministic tests, the documented public law example, CLI help, static preservation/link/fragment/source-correspondence checks, and producer record/configuration inspection. No time-40 trajectories or finite-network campaign were authorized or executed.

All six executed checks exited zero. Reaped child CPU summed to **5.588667 seconds**, elapsed command wall time to **6.107566 seconds**, and the largest reported cumulative child peak RSS was **59,420,672 bytes**. Children had `RLIMIT_AS=4 GiB` and `RLIMIT_CPU=580 seconds`; the latter reserved room inside the 600-second total. All six numerical-thread environment variables were set to one. The retained command records are in `data/generated/observable_hierarchy/H4_integration_v2/commands.json`. The initial/final input hash checks and generated read-coverage record add negligible administrative work; they were not research experiments.

The test working directory was `data/generated/observable_hierarchy/H4_integration_v2/standalone/`. Its `code` and `docs` entries are read-only-use symbolic links to those directories in the frozen edition; its generated `data/established/` tree lies entirely inside the assigned scratch namespace. This allowed the complete new literal test setup to run unmodified, without writing into the frozen edition. The shared checkout and Git index were not copied, moved, reset or written.

## Completed direct reading

Exact full-file hashes, line counts and coverage are retained in `data/generated/observable_hierarchy/H4_integration_v2/read_coverage.json` (18 entries). The manifest was parsed completely and every one of its 271 file hashes and byte counts matched both at the start and after stopping; both checks have retained JSON records. Hashing an input is not claimed as semantic reading.

I read the neutral integration assignment completely, `RESEARCH_WORKFLOW.md` completely (including Part 2), and `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely. The supplied shared AGENTS instructions governed the isolated scope; no author startup or study README was read.

Completed scientific/new-material reads:

- Entire `H4_proposed_section_v2.md`, lines 1–1754, including every new display/proof in D.1–D.5, all storage/work contracts and empirical interpretation paragraphs.
- Entire `H4_code_guide_v2.md`, including its public example, full literal test/generation/analysis recipe, all configuration and empirical claims.
- Entire frozen `docs/NOTATION.md` and `docs/README.md`, including the complete roadmap, chapter-role and future-scope sections.
- Frozen `code/README.md` lines 1–940 directly, including the earlier all-tests and H3 observable-test recipes. The complete proposed H4 append was separately read as `H4_code_guide_v2.md`; I had **not** yet independently checked the assembled suffix against that source. Thus this report does not claim a completed direct read/correspondence check of assembled lines 941–1110.
- Entire frozen `code/pde/observable_laws.py`.
- Entire frozen `code/scripts/validate_observable_horizon.py`, `run_observable_validation.py`, and `analyze_observable_horizon.py`.
- Entire frozen `code/tests/test_observable_laws.py`, `test_observable_horizon_validation.py`, and `test_observable_horizon_analysis.py`.
- Entire frozen `code/validation/observable_horizon_plan.json` and `edition_manifest.json`.

For `H4_dependencies.md`, I obtained only a heading/line-number inventory to locate the assigned older sections. **No older statement or proof-body coverage is claimed.** I did not read the scientific assignment, author histories, study README, selector findings, any prior/current scientific, integration or reproduction report, or other studies. The retained author arrays were accessed solely by the maintained analyzer for the completed algebra check; no author/reviewer verdict was consumed as evidence.

## Actual checks and results

The handwritten orchestration source is retained as the flat study file `H4_integration_v2_checks.py`, SHA256 `bcfcdec878227d6f9e75cf122d0d8b4f8fd5d3a9b94f7c5824f6189c9dedb785`, and copied byte-for-byte into the assigned scratch directory. It records exact commands, exit codes, timing and resource counters. Logs remain beside `commands.json`.

1. **New literal deterministic test recipe: PASS, 67 tests.** I extracted the first three lines of the H4 guide's text recipe and ran them literally from the scratch standalone view:

   ```sh
   mkdir -p data/established
   observable_test_scratch=$(mktemp -d "$PWD/data/established/observable_tests.XXXXXX")
   env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 H4_LAW_TEST_SCRATCH="$observable_test_scratch" H4_VALIDATION_TEST_SCRATCH="$observable_test_scratch" TMPDIR="$observable_test_scratch" python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v
   ```

   `literal_test_recipe.log` ends with `Ran 67 tests in 4.838s` and `OK`. This includes the deterministic inherited tests and the manufactured four-step worker check. It is not a newly generated research trajectory or reproduction of the time-40 campaign. Reaped CPU was 4.709977 seconds.

2. **Public supported-law example: PASS.** The exact Python block was extracted from the H4 guide into scratch and executed with the frozen package. It constructs `supported_law(a="-1", b="1", c="-1/2", d="1")`, round-trips its complete exact descriptor, and asserts that eight nodes per nondegenerate component produce 16 labels. No initializer or trajectory is called. Reaped CPU was 0.124426 seconds.

3. **Public CLI parsing/help: PASS.** Each of `run_observable_validation.py --help`, `validate_observable_horizon.py --help`, and `analyze_observable_horizon.py --help` exited zero with the frozen modules. Their exact command records/logs are retained. This tests argument availability, not campaign execution.

4. **Maintained analysis of allowed retained producer arrays: PASS for its stated algebra checks.** Executed the frozen analyzer with the frozen horizon plan, input `data/generated/observable_hierarchy/H4_author_runs_v1/`, and fresh output `data/generated/observable_hierarchy/H4_integration_v2/analysis/`. It checked recorded artifact hashes, observation shapes/finiteness, literal-weight losses, paired RMS/moments and comparable configurations. It reported 14 declared/14 operationally successful producer records, no problems, 12 comparisons, recorded worker CPU sum 506.290977526 seconds and recorded peak RSS 56,119,296 bytes. These last two values describe the **existing producer runs**, not this review's resource consumption. The new analyzer itself used 0.444882 CPU seconds.

   This was a fresh analysis of retained arrays, **not an independent empirical reproduction**: no initialization-to-time-40 campaign was rerun. The analyzer checks exact JSON presence/hash but does not independently decode every retained high-precision array; all-backend exact observation encoding is covered by the deterministic producer tests, not by a claim that I audited every exact JSON scalar. The operational numbers agree with the new guide's CPU/RSS claims at their displayed precision. Broader numerical-difference claims were not fully reconciled before stopping.

## Retained required correction

**Packaging/documentation blocker: the inherited general all-tests command lacks the mandatory H4 scratch setup.** Frozen `code/README.md`, in the `## Tests` section around line 120, still instructs:

```sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_*.py' -v
```

The new H4 law test explicitly fails when `H4_LAW_TEST_SCRATCH` is absent, and `ScratchTest.setUp` in `test_observable_horizon_validation.py` explicitly fails when `H4_VALIDATION_TEST_SCRATCH` is absent. Those tests match `test_*.py`. Therefore this advertised complete-suite recipe cannot run successfully in a clean environment as printed, even though the two observable-specific recipe blocks supply the correct settings. The general section also still describes the full suite as using only NumPy and standard `unittest`, while the discovered supervisor tests import `psutil`; the guide elsewhere correctly describes that optional supervisor dependency. The dependency wording should be made consistent with the scope of the advertised full-suite command.

Required correction: supply fresh in-edition scratch setup and the required environment for **every advertised discovery command that includes the H4 tests**, or provide an equally complete working reference to the setup; ensure the general test dependency statement names the actually required dependencies. This is a packaging/test-documentation correction, not a proposed mathematical alteration.

I noticed the missing-scratch issue independently while reading the early complete-guide command, before the coordinator's stop message. I had not yet executed that deficient command; the failure conclusion above follows directly from the read command and explicit test prerequisites. The coordinator then separately identified the same omission and ordered this review stopped. No further failure demonstration was run after that instruction.

## Unfinished obligations and unread complement

The older scope assigned for this integration review was: complete prior C.4.7.10 A–C and C.4.7.8–9; statements/domain definitions of C.4.7.1–5 and C.4.7.7; notation and complete book/code guides; full unchanged H3 runtime, initializer, compiler, arithmetic and word modules, relevant interacting tests, and the older supervisor API. Of that older scope, only the notation/book guide and the directly read portion of the code guide were completed. The older scientific packet bodies, unchanged runtime/dependencies/tests and old supervisor source remain unread. Tests executing a module do not count as reading it.

The prescribed unread complement, even for a future completed integration review, is the rest of the older proof bodies, other global-chapter sections and other book chapters. This assignment is not a fresh whole-book scientific audit. Other unchanged imports could have been inspected as needed within the frozen edition; their read scope was not expanded before stopping.

Not completed: complete assembled chapter placement and byte-preservation checks; exact source-to-edition transformations; systematic heading/equation/fragment/link checks; old/new API compatibility comparison; full mathematical dependency and notation reconciliation; complete resource-contract audit against unchanged implementation; all earlier literal test recipes; complete producer/source/configuration correspondence and numerical table reconciliation. No passing conclusions are asserted for those obligations. The completed new-material reads exposed no separately finalized mathematical correction, but that is **not** a scientific clearance because the dependency/interface audit was unfinished.

## Isolation and completion evidence

This context began from the neutral bounded assignment without inherited author research history. No excluded reviewer was contacted, no review result was read, and no research material from another study was used. No subreview was delegated. The coordinator's final stop message disclosed its independent packaging finding only after this context had already noticed it; that exposure and the stop are disclosed here. This report cannot be reused as a completed isolated verdict.

Writes were limited to this report, the flat handwritten checker source, and the assigned fresh scratch tree. Frozen source hashes remain unchanged: all 271 manifest entries still match. No Git writes, frozen-input edits, additional time-40 trajectories or finite-network campaign occurred. Completed logs, original commands, source and exact read coverage are retained. **Review status: INCOMPLETE / STOPPED; corrected edition requires fresh complete review.**
