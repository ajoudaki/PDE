# H4 v3 independent integration review

Verdict: **PASS for the complete assigned H4 integration scope.** No required
scientific, implementation, packaging or editorial correction was identified
within that scope. This is an integration verdict, not a replacement for the
two scientific reviews, the independent trajectory reproduction, or promotion
approval. The standalone edition is a scoped H4/H3 validation edition; it is
not a complete executable copy of every older module and chapter mentioned in
the repository-wide guides.

Reviewer: `/root/h4_integration_v3`. Date: 2026-09-13. Assignment:
`studies/observable_hierarchy/H4_integration_assignment_v3.md`.

## Identity, isolation and frozen edition

I started without inherited author discussion, earlier candidates, study
history, selection findings or other scientific/integration/reproduction
verdicts. I read the neutral integration assignment, the frozen inputs below,
the required mathematical skill at
`/etc/codex/skills/solve-math-rigorously/SKILL.md`, and only Part 2 of the shared
`RESEARCH_WORKFLOW.md` for the promotion process. I did not read the study
README, other studies, Git history, author chats, prior reviewer reports or
concurrent scientific findings. No external scientific sources were fetched.
Scientific observations were sent only to the coordinator, not other reviewers.
There was no Git mutation and no frozen-input edit.

The complete 271-file input manifest has SHA256
`06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02`.
Every listed size and SHA256 matched. The edition is
`data/generated/observable_hierarchy/H4_candidate_v3`; its edition manifest
SHA256 is
`64bd43d30e11e1f591b12f9c07c76d192c5fa7dcd8f22c1c0e3fd313c27e8250`.
The proposed section SHA256 is
`b755c3d05eacc0ef20df6d0499f73dcc6fbf46abdcf4a04084c346ce6b4ad432`.
The assembled global chapter SHA256 is
`cbcf00fd705a9a938a6a3fd0d2bbc2f1c2dd3ab4303d848740a549dbb169f629`.
Full individual hashes and the 31 source/destination mappings are retained in
`data/generated/observable_hierarchy/H4_integration_v3/hashes.json`.

The global insertion is exactly the complete part D, once, immediately after
the old C.4.7.10 and before C.4.8. It occupies assembled lines 13982–15735.
Removing only that insertion reproduces the complete declared older chapter
SHA256
`77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932`.
Thus all preceding and following chapter bytes are preserved. Identity-copy
destinations match their declared source hashes. Reversing the sole canonical
import rename in the law tests reproduces their declared source hash. The full
proposed guide files match their assembled destinations; the entire separate
H4 code-guide append is an exact suffix of the assembled code guide. These are
checks against the frozen declared base, not a claim to have audited a changing
live checkout.

## Complete read coverage and unread complement

The following new material was read in full, without selecting only favorable
claims. Initial overlong combined tool displays were repaired with smaller
reads.

| Input | Read coverage |
| --- | --- |
| `H4_proposed_section_v2.md` | All 1754 lines, D.1–D.5, every proof display, table, resource and empirical-interface claim; byte correspondence to the full insertion checked |
| Assembled `docs/NOTATION.md` | All 98 lines |
| Assembled `docs/README.md` | All 738 lines, including roadmap, scope summaries, chapter table and prior-work orientation |
| Assembled `code/README.md` | All 1113 lines, including every old and new example/recipe; relevant H3/H4 commands audited as described below |
| `H4_code_guide_v2.md`, `H4_assemble_v3.py`, edition and dependency manifests | Complete texts; byte-identical guide representatives were not treated as separate scientific versions |
| `pde/observable_laws.py` | Complete new public law implementation |
| `scripts/run_observable_validation.py`, `validate_observable_horizon.py`, `analyze_observable_horizon.py` | Complete supervisor replacement, new producer and new analyzer |
| `tests/test_observable_laws.py`, `test_observable_horizon_validation.py`, `test_observable_horizon_analysis.py` | Complete new/replaced tests |
| `validation/observable_horizon_plan.json` | Complete configuration, law, interpretation, resource and stopping declarations for all 14 runs |

The full unchanged H3 interfaces were also read: `observable_solver.py`,
`observable_initialization.py`, `observable_compiler.py`,
`observable_arithmetic.py`, `observable_fixed.py`, `observable_words.py`,
`validate_observable_solver.py`, `analyze_observable_solver.py`,
`observable_solver_plan.json`, and the complete compiler, initializer, solver
and old-supervisor test files. The old supervisor's default CLI/API protocol
was checked through these complete producer, plan, guide and preserved tests,
and the replacement's optional/default dispatch implementation. The package
`pde/__init__.py` was read in full. In the older H2 prototype I read only
`observable_closure.py` lines 1–170, its exact word and decoder interface used
by the H3 compatibility tests. No other older implementation body was used as
a scientific premise.

In `H4_dependencies.md`, the older scientific coverage was:

- Lines 5989–8531: complete C.4.7.8, C.4.7.9 and C.4.7.10 parts A–C, including
  every proof, initialization rule, observation interface and cost statement.
- Lines 4374–4735: C.4.7.1's complete model/theorem/observation contract,
  C.4.7.2's raw/comparison interface, and C.4.7.3's setup and cap statement.
- Lines 5692–5740 and 5810–5860: the completion premises/comparison and
  finite-proxy/observation interface prefixes in C.4.7.4–5.
- Lines 5946–5988: the complete C.4.7.7 risk/activity interface and its limits.

Read-scope disclosure: the fetched C.4.7.2 block included its adjoining proof,
and the C.4.7.4–5 prefixes included short derivations as well as the requested
statements/domain definitions. This was additional frozen older material
beyond the statement-only minimum; it did not introduce history or another
reviewer's reasoning. The precise ranges above, rather than a claim of an
entirely statement-only older read, define the actual coverage.

The unread scientific complement is the rest of the older dependency packet,
including the earlier finite-dynamics, III.F, A/B/C dependency proof bodies,
C.4.7.3's main source-proof body, the remainder of C.4.7.4–5, and all other
older global-chapter sections and other book chapters. Full chapter bytes were
hashed, and heading/fragment metadata was mechanically scanned, without reading
those excluded proof bodies. Older unrelated finite-network, Gaussian-moment,
jet, reduction and certificate-tool implementations were not newly audited.
This is expressly **not a fresh whole-book scientific audit**.

For the empirical interface I read the complete author summary text, the full
frozen plan, the producer/analyzer source, and the full recorded-test metadata
and reference checker source. Machine checks parsed all 14 producer records,
their full configurations and metadata, all 84 exact observation JSON files,
all 84 NPZ archives, and all 28 exact checkpoints. The entire recorded analysis
was recomputed and compared recursively, including every run and every declared
comparison. Author operational records were evidence to inspect, not review
verdicts to adopt.

## Integration findings

**Model and normalization.** D.1/D.3, the notation contract, both guides, the
law rule and unchanged runtime agree on normalized directions `u=x/sqrt(2)`,
the quarter-turn binary family, equal label masses, residual `f-y`, unhalved
square loss, physical GF time, Gaussian stored variances `(1,1/n,1/n^2)` and
mobilities `(n,1,n)`. The positive finite tower describes a fixed law rather
than a precision-dependent family. The nonorthogonal atom and nondegenerate
interval examples have the advertised exact geometric meanings. The tiny
positive radius is never claimed to be numerically resolved by the supplied
supported runs.

**Mathematical interfaces.** D.2 supplies its own supported-domain cap and
radius; it does not silently assume membership in the older unnamed law ball.
The split-reference constants, causal earlier-row use, same-input passive
comparison and limiting-carrier conventions remain explicit. The risk and
paired-activity conclusions retain their distinct times. D.3 uses precisely
the unchanged full initialized dictionary and ridge, and gives both strong
action directions plus the projected HS source. It does not replace strong
action approximation with operator-norm approximation. The stability argument
uses the exact reference's tails; no unproved projected-trajectory tail
condition enters the implementation. D.4 keeps the nested precision, time,
data, population, initialization, regularization and order limits in their
specified order. Its compact-query argument addresses the full input circle,
while measured panels are separately identified as finite diagnostics.

**Action and joint-state semantics.** The state retains nine arrays
`b1,g,w,p1,b2,c,p2,M,D`; only `w,c,M` move. Forward and reverse evaluation use
the same feature coefficient matrix and its actual transpose, with the
appropriate population weights. The initializer's inverse-lower-Cholesky
transposes agree with D.3/C.4.7.10.B. Both Gaussian source orientations and
response terms survive initialization, which is completed and discarded before
evolution. The upper initial observation is reconstructed from `g,D` on the
same joint marks; pair arrays preserve initial/current correlation and use
literal product weights. Probability normalization is a stated interpretation,
not a change of the ODE weights. No neuron-by-neuron middle matrix, imported
target state, fitted trajectory or evolving source transcript is present.

**Restart and observation scheduling.** The worker evolves each configuration
from its own prescribed initializer. Its event routine retains adjacent actual
Heun endpoints, observes off-mesh interpolants, and resumes from the actual
right endpoint. A checkpoint must be an interior mesh node. The midpoint
checkpoint, plan and record together retain the full state, law, arithmetic,
intended step, step counts and block size. All arrays, both metadata mappings,
arithmetic and final prediction are compared by exact scalar encoding after
continuation. The tests attack signed zero, differences below float64 display
resolution, every retained-array change, metadata changes, and multiple
off-mesh events in one step. There is no claim that a new mesh started at an
interpolated interior state reproduces the original finite computation.

**Resource and scope wording.** The retained-state formula
`P1*(d1+5)+P2*(d2+2)+2*d1*d2`, data count `4*A`, and pair-output count
`2*(P1+P2)*A` match the arrays and were checked for every supplied checkpoint.
The runtime contracts cover blocking, constant-stage storage and total work
proportional to step count. Initialization, symbolic descriptions, enormous
resolved denominators, fixed-point units/scales, temporary rational arithmetic,
serialization and process memory are distinguished. Part C.6 remains the
inherited detailed account of Gaussian-node digit generation and bit work;
D.5's displayed algebra counts are not a cost-to-accuracy assertion. Resource
ceilings are adjustable guards, not a mathematically truncated hierarchy.
RSS is sampled and can overshoot; neither guide calls it a memory reservation.
Worker CPU and supervisor accounting are explicitly distinguished from parent
CPU. No finite-panel agreement is promoted to population accuracy, monotonicity,
an arbitrary simultaneous limit, or resolution of the tiny perturbation.

**Placement, summaries and rendering.** Extending C.4.7.10 with part D is
coherent: A–C keep their separate short-time family, while D supplies the
distinct time-40 domain. The older construction is reused rather than copied
into a separate chapter. The local repetition of definitions/constants makes
the extension reviewable and does not change older claims. Roadmap and scope
summaries keep GF, finite-network probability limits, early activity and
time-40 risk distinct. All 79 new H40 equation tags are unique in the complete
assembled chapter. Guide fences are balanced, the headings have valid Markdown
levels, the displayed tables have coherent columns, and every local fragment
whose file is present resolves under the chapter's heading convention.

Six legacy guide targets are not bundled in this scoped standalone edition:
`docs/gaussian_calculus.md`, `docs/arctan_limits.md`,
`docs/linear_dynamics.md`, `docs/continuous_depth.md`,
`docs/finite_optimization_and_controls.md`, and
`code/tools/two_layer_risk/README.md`. I did not fetch them. Likewise, unchanged
guide examples for older jet/reduction/exact-calculus modules are not executable
from this selected dependency tree. These are disclosed limits of the frozen
review edition, outside the assigned older scientific/implementation scope;
I do not claim a whole-guide or whole-repository standalone validation. They
do not prevent the new H4 or affected H3 recipes, imports and tests from working
without studies/history/retained research arrays. No required H4/H3 target or
fragment is missing.

## Checks, results and resource record

The budget was declared before testing: at most 600 CPU seconds, 4 GiB, one
numerical thread, and zero new research trajectories. Tests used a fresh
review-owned scratch directory and `PYTHONDONTWRITEBYTECODE=1`; all six thread
environment variables were set to one. Test subprocesses had CPU and 4-GiB
address-space limits. No time-40 trajectory, finite-network campaign,
parameter search or extra reproduction was run.

The exact commands, working directories, environment, exit codes, CPU/wall
times and logs are in
`data/generated/observable_hierarchy/H4_integration_v3/execution_summary.json`.
The substantive operations were:

1. Hash and byte-correspondence checks for all 271 manifest files and 31 edition
   destinations, including inverse reconstruction of the preserved old chapter.
2. From the frozen edition root,
   `python3 -B -m unittest discover -s code/tests -p 'test_observable*.py' -v`,
   with `PYTHONPATH=code` and both H4 scratch settings plus `TMPDIR` directed to
   review scratch: **67 tests passed**, 4.717609 charged child CPU seconds,
   50,741,248 bytes peak child RSS. Tests include positive/singular covariance
   handling, exact grammar compatibility, inverse-Cholesky orientation, source
   responses, weighted gradient/energy, genuine transpose contractions,
   law/collapse/resource limits, exact restart, archive algebra, optional/default
   worker selection, invalid plans/records, CPU/wall/RSS/total stops, capped logs
   and interruption cleanup.
3. Execute the exact new public-law example: the round-trip exact descriptor
   agrees, the rule has 16 nodes, and supported scope/collapse metadata are
   preserved. This uses no initializer or trajectory.
4. Recompute the entire author analysis using the maintained frozen analyzer;
   recursively compare aggregate, all run entries, all 12 comparable pairs,
   problems and supervisor metadata. They match. Independently decode every
   exact observation archive and compare every float64 view entry to its NPZ:
   **84/84 match**. Decode every checkpoint, reconstruct its exact finite law,
   and compare fixed signatures, data arrays/metadata and scalar counts:
   **28/28 pass**. Recompute each final observation from its checkpoint, using
   only evaluation and the saved circle: **14/14 match exact encoded working
   values**, including both pairs, weights, prediction, loss and RMS. No
   initializer or integration step is used in this archive audit.
5. Run the supplied exact rational reference-constant checker: **pass**,
   3.240369 child CPU seconds. Its scope is the stated finite algebraic margins,
   not independent reproof of the excluded older analytic dependencies.
6. Execute `--help` for both workers, both analyzers and the shared supervisor:
   **all five pass**. Full source/test inspection verifies the H3 default is
   preserved and the new `--worker validate_observable_horizon.py` protocol is
   usable. The maintained H4 analyzer requires only NumPy; the supervisor
   installs the canonical code path for its worker. All three affected guide
   test setups provide both required scratch variables and `TMPDIR`.

The measured nine check subprocesses used **15.626431 CPU seconds total**,
including the preliminary archive pass and its complete final extension.
Their maximum recorded peak RSS was **73,949,184 bytes**. Read/hash/report
orchestration is separate from that measured subprocess total. No numerical
job approached the declared budget.

The checked recorded operational claims are exactly 14 completed configurations,
12 comparisons, worker CPU sum **506.290977526 seconds** and maximum recorded
process peak RSS **56,119,296 bytes**. The reported step, initializer, population
and exploratory-input differences round to the guide's numbers. Supported
input refinement differs at rounding level; the two rational precisions agree
in the float64 panel view. Exact higher-precision encodings are retained, not
silently inferred equal from that view. This verifies the supplied evidence
and maintained analysis, not a new independent trajectory reproduction.

Handwritten checker sources are preserved as flat
`H4_integration_v3_check.py`, `H4_integration_v3_interfaces_initial.py` and
`H4_integration_v3_interfaces.py`, with identical scratch copies and SHA256s
in the execution summary. The initial source is retained separately from the
expanded final checker. `interface_results.json` contains every exact archive
and checkpoint hash, all comparisons and the link audit. The original logs
are retained. Final manifest verification again found every frozen input
unchanged.

## Completion

Coverage is complete for every assigned new section, implementation, test,
configuration and affected interface. Required corrections: **none**.
Unresolved candidate objections within that scope: **none**. The explicit
unread complement, additional adjoining older derivations read, unbundled
legacy guide targets and absence of a new trajectory reproduction are recorded
above. This report is the original independent integration report; no other
review outcome was used to choose its verdict.
