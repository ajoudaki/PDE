# Width4096 execution record

This is the explicitly user-requested continuation defined in
SCALING_WIDTH4096_PROTOCOL.md, not a rerun of the old conditional StageD.
Root is sole Git writer. The original two geometries and seeds are fixed.
The old campaign ended with2008.2156020626426 timed worker seconds and175
trajectories; this continuation permits52 main trajectories and at most8
numerical-resolution attempts within the remaining3991.7843979373574 seconds.

## Before main launch

Both RTX3090 GPUs are idle for this study, with >23GiB free each; unrelated
Jupyter/service processes are preserved. Filesystem has297GiB available.
The producer changes only CLI scope and protocol provenance; vector field,
dictionary construction, initialization and trajectory integration are unchanged.
Syntax/help and diff checks pass. Existing dictionary validation is reused;
each actual4096 dictionary also undergoes runtime algebra/conditioning gates.

Reserve2400 seconds for four600-second invocations before launch:

- Primary worker0/cuda0: quadrant_pairs, full +3methods*p1,3,5,7;13 cells.
- Primary worker1/cuda1: two_outliers_alternating, same13 models.
- Refined worker0/cuda0: same paired13 models at level1.
- Refined worker1/cuda1: same outlier13 models at level1.

Initial unreserved balance1591.7843979373574 seconds. No new training has yet
completed at this entry. Each unused allocation returns after completion.
Primary/refined roots are scaling_width4096_primary01/refined01, logs in
scaling_width4096_logs01, all within this study's generated namespace.

All commands use /home/amir/miniconda3/bin/python -B and environment
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1.
Full argv, source/configuration hashes and environment are recorded by each
worker. No historical endpoints are supplied to this width's analysis.

## Main-worker progress

Both primary workers exited0, all26 cells fitted. Paired worker0 used
104.80270920321345 seconds; outlier worker1 used237.87287602573633.
Refinement was launched on each GPU only after its primary worker released it.
Paired refinement exited0,13/13 fitted,153.39275132119656 seconds.

After these three workers: extension actual496.06833655014634 seconds;
old+new actual2504.283938612789; remaining3495.716061387211. The last outlier
refinement retains its previously reserved600-second cap, leaving
2895.716061387211 unreserved. Budget snapshots are retained in the logs root's
`budget.json`. Fitting alone does not yet establish endpoint validity.

Outlier refinement exited0,13/13 fitted,285.40562715008855 seconds. All52 base
trajectories fitted. Extension worker total781.4739637002349; cumulative
old+new2789.6895657628775; remaining3210.3104342371225, zero outstanding caps.
Metadata supplement`scaling_width4096_logs01/metadata_gate.json` has no problems
and confirms52 executed cells. Its time subtotal intentionally covers only the
new roots; `budget.json` includes the earlier campaign.

Initial analysis`scaling_width4096_analysis01` exited0:21/24 comparisons valid.
Three outlier closure cells meet the predeclared extra-resolution condition:

| Cell | Own endpoint discrepancy | Both endpoints fitted |
|---|---:|---|
| two_outliers_alternating_gaussian_p1 | 0.011023455544842964 | yes |
| two_outliers_alternating_orthogonal_p1 | 0.01814546073319301 | yes |
| two_outliers_alternating_orthogonal_p5 | 0.043742954232485864 | yes |

Reserve540 seconds for these three cells together on the availablecuda0,
worker1/workers2, groupwidth, stageextra, level2, orders1,5 and all-orders1,3,5,7,
with the new protocol explicitly passed and an exact`--only-cells` list.
Root`scaling_width4096_extra01` is new. Remaining unreserved2670.3104342371225.
These are3/8 permitted resolution attempts; no other cell is rerun, and none
receives a second extra attempt. Selection uses only the endpoint discrepancy,
not method ranking. Initial adverse analysis is retained; final analysis will
select the latest two attempted levels for exactly these cells.

All three extra cells fitted; extra worker exited0 in104.88483361899853 seconds.
Extension total886.3587973192334; cumulative old+new2894.574399381876; remaining
3105.425600618124; no outstanding reservation. Total55 new trajectories,
230 old+new;3/8 allowed extras used. Final metadata audit has no problems.

Final analysis02, with extra01 explicitly supplied, exited0 with23/24 valid
comparisons. Gaussianp1 and orthogonalp1 now pass at0.0018859777885733564 and
0.009840226156567766 endpoint discrepancy. Orthogonalp5 remains unresolved at
0.05371220463817572 and is not rerun again under the predeclared rule.

Independent final raw audit`scaling_independent_check_width4096_02` exited0:
all3231 technical checks pass;48 metric records agree exactly,75 producer-source
checks match, and the same sole numerical failure is confirmed. An additional
53 structural checks pass. Initial independent audit01 retains its three earlier
numerical failures; the paired-only preliminary audit retains the pending
out-of-scope worker markers from when the other worker was still running.

Requested plots and radial export retain the unresolved fitted diagnostic with
explicit markers via`--allow-unresolved`; strict-default export is not described
as having passed. No additional training follows. Final interpretation and
evidence links are in SCALING_WIDTH4096_RESULTS.md.
