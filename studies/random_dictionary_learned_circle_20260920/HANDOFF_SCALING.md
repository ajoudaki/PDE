# Resume the bounded circle dictionary scaling experiment

Checkpoint prepared 2026-09-20 at the user's request to change accounts. This is
an explicitly authorized continuation of this SAME study, not a new direction.
PDE and PDE-2 share this exact checkout and generated data on the same machine.
Do not clone, copy, create a worktree, reset, or overwrite concurrent work.

## Objective and authorization

The user wants to know whether our initialized-observable dictionaries have a
substantial, growing approximation-efficiency advantage over Gaussian and
orthogonal dictionaries, rather than only a modest constant-factor advantage.
The target is the SAME finite full network's learned function over the circle,
not teacher risk, test-label accuracy, or merely fitting the training points.
All models must reduce training MSE to the same threshold1e-3. Preserve complete
circle outputs for post hoc analysis. GPU-only evolution and metrics; use both
GPUs. The user authorized the focused recommendation with “go on wiht your
recommendation,” then requested a graceful pause and handoff. Existing authority
covers the finite conditional protocol below; no further permission is needed to
resume those runs. Do not expand this into an unbounded experiment campaign.

## Read first, scoped to this investigation

1. /home/amir/Codes/PDE/AGENTS.md and Part1 of RESEARCH_WORKFLOW.md.
2. This study's README.md, SCALING_ASSESSMENT.md, SCALING_PROTOCOL.md and
   SCALING_RUN_RECORD.md. The last records actual execution/budget at pause.
3. docs/README.md, docs/NOTATION.md and code/README.md for maintained model/API
   conventions. Use investigate-conjectures and its required experiment/audit
   instructions. Use solve-math-rigorously if making new mathematical claims;
   this task primarily requires a disciplined computational comparison.
4. New scaling_cases.py, scaling_dictionary.py, scaling_benchmark.py,
   scaling_analyze.py, validate_scaling_dictionary.py, scaling_runner_check.md.
5. Their direct own-study dependencies: benchmark.py, diverse_benchmark.py,
   diverse_dictionary.py, diverse_cases.py, analyze.py, diverse_analyze.py;
   relevant maintained engines/compiler reached through those imports.

All named study files live directly in
/home/amir/Codes/PDE/studies/random_dictionary_learned_circle_20260920/.
All generated files live in
/home/amir/Codes/PDE/data/generated/random_dictionary_learned_circle_20260920/.
Do not search/read other studies or recover their findings through chats/history.
Unrelated untracked studies are concurrent work and must remain untouched.
No established-book/code promotion is authorized or needed for this experiment.

## Current checkpoint: what is complete and what is NOT

- Frozen protocol/source commit acfbedf. Earlier scaling assessment3666533;
  completed twelve-case report48d89a7; independent previous aggregation check
  1c16f0b. A later handoff-only commit contains this file and final run record.
- Dictionary preflight:385 checks passed,2.084 seconds, artifact
  scaling_dictionary_validation02/validation.json. Includes exact reproduction
  of oldp1/3/5, nested random spans, algebra, conditioning and seed behavior.
  Earlier validation01 remains preserved. No need to repeat unchanged tests.
- Stage A PRIMARY only was launched: full,p6,p7 for each discoverycase, all
  three dictionary methods, one case/GPU. Root
  scaling_discovery_primary01. Read SCALING_RUN_RECORD.md for final completion
  counts, elapsed seconds and process status. Do NOT rerun/overwrite these cells.
- Stage A refinement has NOT launched. No StageB/C/D or extra-resolution run.
- No new endpoint comparison/scientific branch decision has been made. Fitting
  status alone does not validate the approximation or trigger the next stage.
- scaling_analyze.py has been source-reviewed and its actual primary/historical
  metadata selection checked. It has NOT yet run on the new GPU output pairs.
- Independent new output audit was scoped but paused before implementation:
  scaling_independent_check.py DOES NOT EXIST. A future scoped checker should
  independently recompute errors/refinement from raw saved endpoint arrays,
  compare to metrics.json within1e-11, verify source hashes and fitted status,
  grids and shapes. Use CUDA float64, one endpoint pair at a time. Do not ask
  the analyzer's author to certify its own numerical output.
- All subagents were asked to stop; no new work should rely on their continued
  existence. New scoped agents should receive only explicit necessary inputs.

## Exact model and comparison

Two hidden layers, tanh, d2,n2048, canonical Gaussian initialization, actual
small random readout, unhalved mean squared loss, GF mobilities(n,1,n), all
three parameter blocks train. x=sqrt(2)(cos(theta),sin(theta)); implementation
stores u=x/sqrt(2). Compare each model at its OWN first detected MSE1e-3 crossing
with the full network at ITS crossing. Adaptive Heun and crossing interpolation
are inherited unchanged from diverse_benchmark.trajectory.
Save8192-angle endpoints,2048-angle trajectory snapshots, all reconstructible
w,c,M states and dictionary arrays. This is a finite-carrier diagnostic, not an
independent population initializer. Actual full first rows/readout still train.
Moving-state scalars=3n+K1*K2; dictionary storage=n(K1+K2), plus caches.

Observable core uses lower=tanh(W1_0), upper=tanh(W2_0@lower),
reverse=tanh(W2_0.T@upper), lower coordinates[lower,reverse], upper coordinates
upper, total-degree Chebyshev words and maintained tails, ridge1/[1024(p+1)^2].
Counts p1(5,3),p3(35,10),p5(128,21),p6(213,28),p7(333,36),p8(499,45),p9(720,55).
Redundant constant tails reduce actual lower ranks at higher orders; report
metadata, not just nominal counts. Throughp9 polynomial refinement adds no new
independent action queries. Full-hierarchy asymptotics are not tested here.

Random Gaussian columns are RMS-normalized. Orthogonal uses QR of the SAME raw
columns, times sqrt(n); same spans, differing frame conditioning. Keep both.
Old random blocks n*128 and n*21 at seed7319 are bit-preserved. Appended fixed
blocks n*592 and n*34 have seeds dictionary_seed+100000+layer. Merely enlarging
an old torch.randn shape changes old columns and invalidates historical reuse.
No future trajectory, labels, PCA, fitted features or observed errors inform
any dictionary. Original networkseed20260920, dictionaryseed7319.

## Previous findings motivating the test (not new evidence)

The twelve-case benchmark data are in diverse_primary01/diverse_refined01 and
four recorded finer roots. diverse_analysis01/selected_levels.json is the
AUTHORITATIVE per-cell historical level selection; never assume all historical
cells used the same tolerance. metrics.json, validation.json, tables and arrays
are beside it. Complete earlier commands/hashes are in README.md.

At p1/3/5, circle RMS ours vs better random:
- quadrant_pairs: .28505/.63253, .16563/.55031, .09425/.45519;
  better-random/ours ratios2.219,3.322,4.830.
- two_outliers_alternating:1.03824/1.56292,.54986/1.30339,.37820/1.17742;
  ratios1.505,2.370,3.113.
Both cases passed prior refinement checks. Other cases favor random; preserve
those contrary results. Three orders at one seed do not establish a rate.

## Frozen stages: obey SCALING_PROTOCOL.md exactly

A: two discoverycases, p6,p7+full, two levels,28 trajectories total.
B: if every A endpoint fits and passes refinement/algebra gates, p8,p9 on both
   cases, regardless of winner;24 trajectories.
C: if at p_high(9 ifvalidB else7 ifvalidA), at least one discoveryfamily improves
   OUR RMS by>=15% vs p5 AND increases better-random/ours RMS ratio by>=20%, at
   BOTH selected numerical levels, run all6 fixed fresh seed/geometry conditions
   (two families+negativecontrol in eachgroup), p1,p5,p_high+full,120 trajectories.
D: only if the SAME family passes that discriminator in BOTH freshconditions,
   one originalcase atn4096,p5,p_high+full,twolevels,14 trajectories. Ifboth
   qualify choosequadrant_pairs. No alternate seeds/geometries/search.
Extra: atmost12 cells acrosscampaign, once/cell, ONLY if bothendpointsfit and
   own endpoint refinementmax>.01. New tolerance=refined/4. Selectlatesttwo
   attemptedlevels, retainingfailure. If>12 selectliteralcase/method/order.
Maximum198 new trajectories,6000 seconds SUMMED timed workerexecution,
perinvocation<=600sec,pertrajectory180sec,T10000,maxsteps30000. Allocate caps
against remainingbalance BEFORE launchingparallelworkers; returnunusedallocation.
Preflight allowance120GPU seconds separate. Accountactualcompletiontimes.

Primary rtol6.25e-5/atol6.25e-7; refinement1.5625e-5/1.5625e-7; extraquarteragain.
Require fit, replay<=1e-10, perpredictor endpointrefinementmax<=.01,
regularizedGramcond<=1e10, triangular/orthogonalityresidual<=1e-8, matchinggrids.
Report sampled maximum as such, not certified continuous supremum. No fitted
asymptotic exponent or numerical guarantee. Report error-vs-budget and smallest
TESTED budget meetingfixedtargets at BOTH tolerances; do not infer untested
smallerbudgets fail. Show negatives/nonmonotonicity/failuresexplicitly.

## Immediate commands after verifying status/resources

Python /home/amir/miniconda3/bin/python (torch2.9.0+cu130,numpy1.26.4).
Two RTX3090 GPUs cuda:0/1. Set these for every worker/analyzer:
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1.
Use -B. CUDA tools require sandbox escalation on this account; previous approvals
covered these bounded authorized study commands. Outputs stay in ownnamespace.

NEXT: reserve800 seconds (400each, withinremainingbalance), then run the two
StageA refinement workers concurrently, substituting I=0/1 in BOTH flags:

```sh
/home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/scaling_benchmark.py --out data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01 --group discovery --stage A --orders 6 7 --all-orders 6 7 8 9 --include-full --worker I --device cuda:I --level 1 --budget 400
```

Then analyze A (newoutput; defaultcommandneedsenvironmentabove):

```sh
/home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/scaling_analyze.py --primary data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_primary01 --refined data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01 --historical data/generated/random_dictionary_learned_circle_20260920/diverse_analysis01/selected_levels.json --orders 6 7 --out data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_A_analysis01 --device cuda:0
```

The analyzer recomputes oldp1/3/5 AND newclosureerrors against the SAME refreshed
full reference at corresponding selectedlevels. Do not splice old tablemetrics
with newerrors. Outputincludes metrics.json,summary.json,validation.json,
provenance.json,tables.md,curves.png,ratios/target_accuracyCSV,circle_errors.npz.

IfAgatespass, StageB uses SAME primary/refinedroots but --stage B --orders 8 9
--all-orders 6 7 8 9, NO --include-full, level0/1respectively, sameworker/device
partition. Newconfig_B_worker#.json and newcells coexist withA. Analyzeagain
without --orders override into NEWroot scaling_discovery_analysis01.

ForC use --group confirm1/confirm2 --stage C --orders 1 5 P_HIGH --include-full,
separateprimary/refinedrootspergroup, level0/1. Worker0 gets pair+negative,
worker1outlier. AnalyzeeachgroupWITHOUT --historical. Protocolseed/geometries
are in scaling_cases.py. ForD use --group width --stage D --cases SELECTED_CASE
--orders 5 P_HIGH --include-full --worker 0 --workers 1 (case filteringchanges
partition!) separatelyeachlevel/GPU ifbudgetpermits. Always freshroot/configids.

## Review/implementation qualifications for resumption

Read final scaling_runner_check.md. Budget guards and None handling fixed before
training, no vector-field change. Runtime gates checkactualdictionaryconditioning
and triangular/orthogonalalgebra. Analyzer recordsdictionarymetadata but does
not itselfrejectfailingmetadata or declared_executed=False; trustedproducer
gatesnewtraining. Independentlycheckthese beforeclaimingallgatespass, or make
a narrow analyzerhardeningfix withownsourcehashandmetadataunitcheck. Do not
rerunvalidunchangedtrainingbecauseanalysiscodechanges.

The previous diverse_analyze process once lingeredafterwritingalloutputsand
printingcompletion. Verifiedoutputs/auditwerepreserved; SIGTERMofcompleted
processwasdocumented(exit143). NewanalyzerexplicitlycleansCUDA, but noGPUrunyet.
Ifithappensagainverifyoutputs/processstateandrecordhonestly; do notconfuseit
with producer failure or leaveGPUprocessesrunningduringhandoff.

## Finish criteria and Git

Completeonlyconditionalprotocolstageswhosegatesandremainingbudgetpermit.
Saveexplicitdecisionrecordsandremainingbudget. Independentlyauditaggregation,
produceconciseRMS/maxerrorbudgettables/curves, andanswerwhetheradvantagegrows,
plateausorreversesandwhetherfreshcasesconfirmit. Thisisanempiricalfinite-range
answer, notaprovenasymptoticrate. Noarbitrarynewbatchaftertheprotocolends.

Preservealloutputsandconcurrentchanges. Commitownsource/reportsprogressively;
generatedarraysstayseparateandhash-recorded. OneGitwritercommonlock:
flock -n .git/pde-writer.lock; verifyindexempty; gitaddONLYexplicitownpaths;
diffcheck; scopedcommit. Never gitadd-all or reset. NewtaskisnowleadGitwriter
once it confirms this task stopped. No live worker should be assumed safe to
kill based on GPUusage alone; inspectprocesscommand/ownership first.
