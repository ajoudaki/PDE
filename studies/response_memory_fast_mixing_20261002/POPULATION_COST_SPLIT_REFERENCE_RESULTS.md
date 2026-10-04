# Population accuracy–cost completion

**The frozen primary empirical screen passes.** The reference-only split FWHT
repairs the width32768 resource ceiling. All32 prescribed reference seeds8001–8032
completed; the original128 candidate outputs, costs, scientific protocol and
thresholds remain unchanged. Among the declared widths and K in{1,2,4,8,16}:

| Cheapest primary-eligible choice | Width | K | Complete estimated cost | Prediction RMS | Second-layer Gram RMS |
|---|---:|---:|---:|---:|---:|
| Dense Gaussian | 8192 | 8 | 37.2749s | 0.00204211 | 0.00116669 |
| Fast quarter-circle | 16384 | 4 | 9.91962s | 0.00195334 | 0.00108744 |

Both observables meet the predeclared0.0025 RMS tolerance. The fast/Gaussian cost
ratio is0.266121, or3.7577 times less cost. All1000 paired bootstrap draws have
both methods eligible and satisfy the twofold rule; ratio2.5%/50%/97.5% quantiles
are0.127827/0.252766/0.281794. These are empirical resampling diagnostics, not a
rigorous confidence guarantee. The descriptive tighter tolerance0.00125 remains
unsupported: only46/1000 draws have both methods eligible. Every declared choice,
secondary result and bootstrap ratio is in the
[full report](../../data/generated/response_memory_fast_mixing_20261002/population_cost_split_analysis01/population_cost.md)
and [JSON](../../data/generated/response_memory_fast_mixing_20261002/population_cost_split_analysis01/population_cost.json).

The finite reference passed both gates **before** cost/error calculations.
Prediction/Gram sampling RMS SEs are0.000494268/0.000283894, below0.000833333.
Width16384–32768 mean differences0.000964945/0.000582392 are below twice-combined
sampling-SE bounds0.00219616/0.00120285. This remains accuracy against a finite
32768-wide fast-ensemble mean, not a certified infinite-width error. The result
supports this population calculation on one digits3/8 split, horizon40 and the
frozen tanh q=1 learner. It establishes no globally cheapest method, classifier
advantage or broad architecture claim. This new campaign was not freshly
reproduced; “screen passes” does not mean a fully internally checked empirical
claim under the repository workflow, or promotion approval.

The separate [producer](fast_training_split_reference.py) retains the original
increasing-bit butterfly order, signs, surrounding permutations and final
normalization. Two unnormalized16384-half transforms precede the cross-half
sum/difference. [Verification](../../data/generated/response_memory_fast_mixing_20261002/population_cost_split_verification01/verification.json)
is bitwise equal to direct PyTorch FWHT, preserves explicit basis signs and
lower-width output, and has float64-reference forward/transpose errors1.59e-7
and adjoint error3.71e-10, below the unchanged3e-6 gate. All160 records pass
source/data/artifact checks. The learning/evaluation functions and analyzer's
error/bootstrap formulas are unchanged, as recorded in the
[source audit](../../data/generated/response_memory_fast_mixing_20261002/population_cost_split_verification01/source_diff_audit.json).
CPU analysis reran bitwise; all80 point/observable checks agree with direct
vector calculation within2.14e-13. No further validation or experiment follows.

The [amendment](POPULATION_COST_SPLIT_REFERENCE_AMENDMENT.md) was frozen before
implementation. Authority was the user's broad research/compute authorization
plus root's bounded delegation; its phrase “explicit user authorization to
repair” overstates who specified the kernel repair and is corrected here without
changing consumed source hashes. The original
[blocked result](POPULATION_COST_RESULTS.md) and every failure remain preserved.
This completion supersedes the absence of a valid reference, not that historical
failure. Root owns README synthesis; no manuscript, maintained code, proof or
Git index changed.

Work began15:36:04 UTC; feasibility passed by15:39:51. GPU1 reference execution
ran15:40:38–15:43:49,191.192s including startup. Its outer worker enforces a700s
subprocess timeout, requires GPU1 and checks verified source hashes before
launch. Including verification, GPU-process use was well below12 minutes;
repair and total wall caps were met. GPU1 is released. The split-kernel runtime
is reference-generation overhead, never candidate cost. The table uses original
complete-trajectory medians times K, with shared loading/import overhead and all
reference-generation costs separately recorded rather than charged per estimate.

Exact reference entry command from /home/amir/Codes/PDE:

```bash
env CUDA_VISIBLE_DEVICES=1 /home/amir/miniconda3/bin/python studies/response_memory_fast_mixing_20261002/run_split_reference.py
```

[The worker record](../../data/generated/response_memory_fast_mixing_20261002/population_cost_split_worker01.json)
retains the full producer command, source hashes, GPU, timestamps and exit status.
The [analysis producer](analyze_population_cost_split_reference.py) was invoked
with `--allow-oracle-repair`, `--candidate-dirs` set to the four selected batches
in POPULATION_COST_RESULTS.md, `--reference-dirs` set to
`data/generated/response_memory_fast_mixing_20261002/population_cost_gpu1_reference_split01`,
and fresh `--out-dir` values ending `population_cost_split_analysis01` and
`population_cost_split_analysis02`. Both JSON outputs have SHA256
`f8104cd6371045a1727dcef8c556b77376284be9d0eb1dcf1791644593bd5300`.
Split producer SHA256:
`24265e260e1741b6771df2d551a16d834667d277a070539151cbbea37c12d4c1`.
Original unchanged producer SHA256:
`7356bce354297abedd38c1db7b433d882d283885657ea2e39bfe521c238142a2`.
The runner intentionally refuses to overwrite retained outputs.
