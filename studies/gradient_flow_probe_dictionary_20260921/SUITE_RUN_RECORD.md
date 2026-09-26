# Width2048 suite execution record

2026-09-21, continuation under SUITE_PROTOCOL.md and frozen SUITE_MANIFEST.json
SHA256 d34ea135c3a2d60dcccce94f23114d92a3692ac3475d13fc3d20dd68387b3670.
User selected newp1,p3,p5, kept the negative-control exclusion, and requested
both GPUs. The 11 original n2048 tasks are the comparison scope; the two much
earlier n512-only tasks lack n2048 baselines and are not silently rescaled.

Starting inherited balance2028.182881616056 GPU-worker seconds; new ceiling2000.
Preflight suite_preflight01 passed in2.701803021132946 seconds. All22 archived
full initial checkpoints match exactly and all three frozen dictionaries pass
dimensions, projected initialization, finite values and conditioning gates.
Released unused preflight reservation57.298196978867054 seconds.

Base reservations: four workers400 each, total1600. Level0 worker0 usesGPU0
and worker1 usesGPU1; after completion each GPU starts the same worker's level1.
No two workers are assigned the same GPU concurrently. Within each invocation
the frozen schedule is newp5, newp3, newp1, original case order/parity.
Reserve200 for numerical analysis/audit before any additional training branch.
All launched commands/configurations and completed elapsed times are saved in
the generated suite_preflight01/suite_primary01/suite_refined01 directories.
Study sources and archived data are preserved; no shared index write.

Interpreter /home/amir/miniconda3/bin/python -B, environment PYTHONPATH=code,
PYTHONDONTWRITEBYTECODE=1, OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1,
CUBLAS_WORKSPACE_CONFIG=:4096:8. Each invocation uses suite_run.py with
--out data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01
or suite_refined01, --worker0/1, --device cuda:0/1, --level0/1, --budget400
(actual argv saved in each config; spell each flag and value separately).
The preflight substitutes --preflight, --budget60 and suite_preflight01.

## Completed base grid and numerical branch

All66 base trajectories fitted. Worker seconds(primary0,primary1,refined0,
refined1)=(182.7316008284688,157.8086477816105,218.17476180568337,
193.7137425839901). No base attempt capped or remained unattempted.
The user's live-update request added suite_progress01, a provisional endpoint
comparison costing0.31677309423685074GPU-worker seconds. Its same-p framing
is superseded for reporting by SUITE_REPORTING_AMENDMENT.md, with no training
or numerical-selection change.

Main audits suite_analysis01a/01b coveredall132 modelrows in7.7514046132564545
and21.106414780020714GPU-worker seconds. All states/provenance/schema gates
passed. Three modelrows were unresolved: the two pre-existing old controls,
plus quadrant_alternating_new_p3 with own-endpoint sampled maximum
0.023758355969924594. Both of its base attempts fitted, so the frozen branch
permits exactly one /4 attempt at rtol3.90625e-6,atol3.90625e-8. No other new
cell triggered the branch. Reserve100GPU-worker seconds onGPU1 for this one
trajectory in suite_extra01; leave all base files intact.

Independent first3-case replay suite_independent01 cost10.695641931146383
seconds and passed all78 raw trajectories; remaining8 cases have a separate
100-second reservation onGPU0. Its all-snapshot checks are independent of
the main analyzer. Exact archived source recovery for four older dense
wrapper hashes is documented in SUITE_SOURCE_RECONCILIATION.md; the recorded
producer bytes were recovered and authenticated, not waived.

## Final selection and independent check

The extra worker fitted in26.972995191812515 seconds. Its latest pair has
sampled maximum0.01499866627868407, so the newp3 quadrant-alternating row
remains unresolved and no further extra is allowed. The final case audit
suite_analysis02a took3.0449966825544834 GPU-worker seconds. Independent
remaining8-case and extra replay took24.874052811414003 and0.7606001682579517
seconds. Every reservation was released after completion; no job remains.

Final authoritative merge suite_analysis_final01 retains the latest whole
quadrant-alternating case from02a and unchanged other cases from01a/01b.
It preserves all132 rows,143 validation cells,99 closest-size comparisons,
286 selected endpoint curves and their grids. All2672 snapshots from287
distinct trajectories pass independent reconstruction. Final metrics and
closest-size counts agree independently; see SUITE_INDEPENDENT_CHECK.md.

CPU-only merge, scalar reporting and figures consume no GPU-worker budget.
Final figures suite_plots02 fix the initial presentation spacing; plots01
is retained. The final check verifies132 curve points and44 nearest-size
table values directly against audited metrics. Root read both full checker
reports and inspected the final figures. Tracked working tree/index unchanged.

Final exact charge850.6534352935851GPU-worker seconds leaves
1177.529446322471 of the inherited balance. Full per-invocation accounting is
suite_summary01/summary.json. This is below the continuation ceiling2000.
All67 new attempts fitted; numerical validity remains32/33 new cells and
129/132 overall. No accuracy-based additional run or baseline retraining.
