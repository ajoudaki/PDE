# Scaling execution record

Frozen plan/producer commit: acfbedf. Dictionary preflight:385 checks passed;
latest artifact data/generated/random_dictionary_learned_circle_20260920/scaling_dictionary_validation02/validation.json.
Root is sole Git writer. No maintained source edits.

All commands use /home/amir/miniconda3/bin/python -B and env
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1.
Exact command/config/source hashes are saved by each worker. All output roots below
are within data/generated/random_dictionary_learned_circle_20260920/.

## Reservations, in execution order

1. Stage A primary, scaling_discovery_primary01, workers0/1 on cuda:0/1,
   orders6,7, planned6,7,8,9, include-full, level0,400 seconds each.
   Reserve800 of6000 summed worker seconds before launch. Actual completion will replace reservation.

## Graceful pause: completed checkpoint

Both Stage A primary workers exited0; each7/7 fitted. All14 primary trajectories
reached MSE1e-3. No producer or reviewer remains working for this task.
Worker0: 47.792691741139s; worker1: 96.719784043729s.
Actual sum 144.512475784868s; unused reservation returned. Remaining allowance
**5855.487524215132 seconds** of the6000-second campaign budget.
No refinement, later stage, or extra-resolution trajectory was launched.
No new scientific comparison is yet validated.

Complete producer configs/commands and source hashes remain in the primary root.
All current primary artifacts are hashed in scaling_discovery_primary01/pause_manifest.json.
Manifest SHA256: `fabdbfef31dd2dabc6fe936bf834baec4f5ccc113e7ccea9e5a5acb39e5cf250`.

Next task starts with Stage A refinement (two400-second reservations), then
replay/refinement analysis and protocol branch decisions.
Read HANDOFF_SCALING.md for exact commands, scope and remaining obligations.
New output independent-audit implementation was deferred without creating a file.

## Resumption from 22d2ed0

2026-09-20: root resumed as lead and sole Git writer. No prior scaling worker
is running; both RTX3090 devices are available. Scientific producer/dependency
hashes match the primary configurations (14 files); the pause-manifest hash
matches the handoff. Unrelated untracked studies are preserved.

2. Stage A refinement, scaling_discovery_refined01, workers0/1 on cuda:0/1,
   orders6,7, planned6,7,8,9, include-full, level1,400 seconds each.
   Reserve800 from5855.487524215132 before launch; unreserved balance
   5055.487524215132. Return unused allocations after completion.

Scoped independent checker owns scaling_independent_check.py/.md only and its
generated audit roots. It has no analyzer source or author findings as inputs;
root coordinates GPU availability. All other study reporting remains root-owned.

Stage A refinement completed: both processes exited0, each7/7 fitted. Worker0
70.737427301705s; worker1 114.503111045808s. Refinement sum185.240538347512s;
campaign sum329.753014132381s; remaining5670.246985867620s. Unused allocation
returned. Stage A analysis launched with the exact handoff command into
scaling_discovery_A_analysis01 on cuda:0; scientific gate awaits replay/audit.

Stage A initial analysis exited0:29/30 closure comparisons valid; the sole
resolution candidate is two_outliers_alternating_gaussian_p7, both endpoints
fitted, own discrepancy0.012985499879930806>0.01. No Stage B yet.

3. Reserve180 seconds for this ONE level2 cell in scaling_discovery_extra01,
   group discovery, stage extra, orders7, all-orders6,7,8,9, worker1/workers2
   on cuda:0, level2, budget180, --only-cells
   two_outliers_alternating_gaussian_p7. Remaining unreserved5490.246985867620.
   This is resolution cell1/12; no cell may receive a second extra attempt.

The resolution worker exited0,1/1 fitted,26.318581540138s. Campaign
sum356.071595672518s; balance5643.928404327482s. Analysis rerun in a NEW
root scaling_discovery_A_analysis02 with --orders6 7 and --extra
scaling_discovery_extra01; latest two attempts retained. Earlier analysis01
remains unchanged.

Resolved A is accepted for the B gate: all32 selected endpoint pairs and30
closure/reference comparisons pass; dictionary metadata/executed-set audit
also passes. Independent CUDA1 audit scaling_independent_check_A02/checks.json
passes technical and numerical checks,60 metric rows within1e-11,6.564021911472s
postprocessing. Initial A01 audit remains adverse for its old p7 pair.

4. Reserve800 (400each) for Stage B primary workers0/1 on cuda:0/1 in
   scaling_discovery_primary01, stage B, orders8,9, all-orders6,7,8,9,
   no include-full, level0. Unreserved balance4843.928404327482s.
   This branch follows A validity irrespective of which method wins.

5. Reserve another800 (400each) for Stage B refinement workers0/1 on
   cuda:0/1 in scaling_discovery_refined01, stage B, orders8,9,
   all-orders6,7,8,9, no include-full, level1. These launch only after each
   corresponding primary worker frees its device. With both B reservations
   outstanding the unreserved balance is4043.928404327482s.

Both B primary workers exited0,6/6 fitted each:37.201980061829s and
70.896819494665s. B primary sum108.098799556494s. Cumulative actual
464.170395229012s; remaining5535.829604770988s, of which800 reserved
for B refinement. Both refinement workers launched on their freed devices.

Both B refined workers exited0,6/6 fitted each:54.399530295283s and
85.918584611267s. B total248.416914463043s. Campaign total604.488510135561s;
remaining5395.511489864439s; no outstanding training reservation.
Complete A+B analysis launched into scaling_discovery_analysis01 using existing
extra01 and historical selection; no --orders override. Its inherited summary
stage label may read A; selected configs/orders define its actual A+B scope.

B is validated:42/42 comparisons, no new resolution candidates; independent
B01 CUDA1 audit passes84 metric records and all numerical/source checks,
exit0,10.234403058887s. B.json records p_high9: paired-case RMS reductions
72.4038%/72.4883% and ratio gains51.3186%/51.4124% trigger C; outliers fail.
All6 fixed fresh conditions must run, retaining negatives. No D decision yet.

6. Reserve4800 seconds for all8 Stage C worker invocations,600seconds each,
   against5395.511489864439 remaining; initial unreserved595.511489864439.
   Groups confirm1/confirm2, separate scaling_confirm1_primary01,
   scaling_confirm1_refined01, scaling_confirm2_primary01,
   scaling_confirm2_refined01 roots; stage C, orders1 5 9, include-full,
   workers0/1 on cuda:0/1, level0/1 for primary/refined respectively.
   Each group/level has20 cells onworker0 and10 onworker1;120 trajectories.
   Worker allocations are released individually on completion; physical GPU
   scheduling follows free devices only, never relative errors.

C confirm1 primaryworker0 completed exit0,20/20 fitted,104.336970284581s;
its600s reservation released. Confirm1 refinedworker0 launched oncuda:0
while primaryworker1 continues oncuda:1. No scientific selection involved.

C confirm1 primaryworker1 completed exit0,10/10 fitted,200.134291801602s;
its600s reservation released. Confirm1 refinedworker1 launched oncuda:1.

C confirm1 refinedworker0 completed exit0,20/20 fitted,166.215858481824s;
its600s reservation released. Confirm2 primaryworker0 launched oncuda:0
while confirm1 refinedworker1 continues. All cases/seeds were predeclared.

C confirm2 primaryworker0 completed exit0,20/20 fitted,97.763658646494s;
its600s reservation released. Confirm1 refinedworker1 completed exit0,10/10
fitted,234.308919709176s; its600s reservation released. Confirm2 refinedworker0
launched oncuda:0. First confirmation analysis runs on temporarily freecuda:1.
The discovery summary-only independent audit completed before that GPU reuse:
6327/6327 checks passed, all ratios/target/budget-ratio JSON and CSV rows agree.

C1 initial analysis26/27 comparisons valid. C1_initial.json identifies one
eligible resolution cell: outliers_confirm1_orthogonal_p5, both fitted and own
endpoint discrepancy0.010847879157941165. Initial analysis remains preserved.

7. Reserve180 seconds for this ONE level2 cell, campaign resolution2/12,
   in scaling_confirm1_extra01: group confirm1, stage extra, orders5,
   all-orders1,5,9, worker1/workers2 oncuda:1, level2, budget180,
   --only-cells outliers_confirm1_orthogonal_p5. Launch after initial independent
   audit frees device, before confirm2 primaryworker1. Actual campaign total
   1407.248209059238s, remaining4592.751790940762; three outstanding C caps
   total1800, plus this180 leaves2612.751790940762 unreserved. This selection
   uses numerical discrepancy only; all fresh conditions remain included.

C1 initial independent raw/summary audits exited0:3639 technical checks and
8762 summary checks pass; the sole invalid numerical pair is independently
confirmed. The reserved extra cell launched oncuda:1. Confirm2 refinedworker0
completed exit0,20/20 fitted,167.267456240952s, releasing its600s reservation.
Confirm2 primaryworker1 launches on the newly freecuda:0 (worker partition is
unchanged; device scheduling only). Its pre-reserved600s cap remains in force.
