# Population accuracy–cost campaign: blocked at the reference resource gate

**Decision: BLOCKED; close this bounded campaign.** All128 distinct candidate
trajectories were completed, but none of the32 prescribed width32768 reference
trajectories could be produced. The first reference attempt failed the
predeclared kernel resource gate. Consequently there is no population
accuracy–cost estimate, no bootstrap success fraction, and no demonstrated
twofold advantage under this protocol. This is an operational failure to supply
the required evidence, not a statistical rejection of a twofold advantage.

The study remains a supporting finite-step transfer/implementation result.
Its previously measured same-width computational saving is not converted into
an accuracy-matched cost saving by this campaign. A broad architecture claim,
full-spectrum necessity claim, or strengthened practical significance is not
supported. No additional experiment or implementation change is scheduled.

## Resource stop and retained artifacts

The GPU1 width32768 reference hit the first Hadamard action with
`triton.runtime.errors.OutOfResources`: required shared memory131072 bytes,
hardware limit101376 bytes on the RTX3090. The exact traceback is retained in
[the reference log](../../data/generated/response_memory_fast_mixing_20261002/population_cost_gpu1_reference_repair01.log).
No training step or reference trajectory was completed. On observing this new
substantive failure, the GPU0 worker and its newly launched reference child
were terminated; its reference directory had not yet been created. Both GPUs
returned to0% utilization, with ordinary background allocations289MiB on GPU0
and43MiB on GPU1. No narrower reference, alternative kernel, changed tolerance,
or increased budget was substituted.

| Retained candidate batch | Law/seeds | Complete trajectories | Producer-recorded process time |
|---|---|---:|---:|
| population_cost_gpu0_a_repair01 | Gaussian7601–7608 | 32 | 199.93s |
| population_cost_gpu1_b_repair01 | Gaussian7609–7616 | 32 | 178.08s |
| population_cost_gpu1_a | Fast7601–7608 | 32 | 39.10s |
| population_cost_gpu0_b_repair01 | Fast7609–7616 | 32 | 40.80s |

Each batch covers widths512,2048,8192,16384. The128 unique candidates retain
predictions, both feature Grams, frozen trajectories, motion diagnostics,
per-run checks and timings. The earlier failed Gaussian directories retain
9 and13 completed duplicate candidates respectively and are excluded from the
selected candidate pools. The original failed outputs were not overwritten.

The completion task began15:00:28 UTC and stopped GPU work by15:06:56 UTC on
2026-10-02, within its additional10-wall-minute cap. Recorded worker cumulative
times through completed batches are244.71s for repaired GPU0 and185.39s for
repaired GPU1; GPU0's final canceled child adds only the brief interval before
termination. Including the original6.68s/50.43s worker attempts and the two
compact-verification fits remains below20 GPU-process minutes. Producer process
timers omit Python imports; worker timers include subprocess startup. Neither
summed GPU time nor the sum of trajectory costs is elapsed concurrent wall time.

## Specific oracle repair

The original protocol is preserved as
[POPULATION_COST_PROTOCOL_V1.md](POPULATION_COST_PROTOCOL_V1.md), and the
pre-repair producer as [fast_training_v5.py](fast_training_v5.py). The first
Gaussian attempts at width2048, seeds7602 and7614, failed their exact adjoint
check while TF32 was enabled. The authorized repair sets IEEE matmul only inside
the per-run Hadamard/adjoint oracle, restoring the previous TF32 flag in a
`finally` block before initialization and training. The existing threshold3e-6,
learning equations, data, schedule, seeds, recording, and decision criteria
are unchanged. The amended protocol documents this exception explicitly.

The exact producer prefix was tested on both offending cases without running
training: adjoint errors were3.70e-9 and7.71e-9, and the restored TF32 flag was
true in both. The result and source manifest are retained under
[population_cost_repaircheck01](../../data/generated/response_memory_fast_mixing_20261002/population_cost_repaircheck01/verification.json).
The earlier compact-producer verification independently retained bitwise equal
predictions for both width8192 cases; maximum Gram discrepancies were2.68e-7
or less, below1e-6. That evidence remains in
[verification.json](../../data/generated/response_memory_fast_mixing_20261002/population_cost_verification01/verification.json).

## Analysis and interpretation

[analyze_population_cost.py](analyze_population_cost.py) was run with the four
selected candidate directories, both intended reference directories, and
`--allow-oracle-repair`. That option accepts only the exact archived/current
producer–protocol pairs and the unchanged reuse source. The JSON records each
source version. The complete candidate metadata have the expected source/data
correspondence; aggregate missing-data/source failures in the report arise
from the absent GPU0 reference metadata, not a detected disagreement among
completed candidates.

[The generated report](../../data/generated/response_memory_fast_mixing_20261002/population_cost_analysis01/population_cost.md)
and [JSON](../../data/generated/response_memory_fast_mixing_20261002/population_cost_analysis01/population_cost.json)
record all five missing-reference/metadata failures and the BLOCKED decision.
They deliberately do not fabricate reference errors, resolution gates, cost
ratios or bootstrap results. The predeclared primary tolerance0.0025 and
secondary tolerances0.00125/0.005 remain unevaluated. No candidate averaging
limit or observable was changed after these outcomes.

Before campaign outcomes, the analyzer passed direct-vector versus normalized
Gram/bootstrap comparisons, exact finite-population enumeration of the squared
error estimator's unbiasedness, eligibility-category checks, and complete and
incomplete synthetic artifact/report checks. These validate analysis logic;
they cannot replace missing scientific data.

The previously completed
[initial-acceleration review](INITIAL_ACCELERATION_REVIEW.md) is an internal
PASS in its stated local/small-scale scope. The actual tanh finite-step transfer
also retains its separate internal PASS. Neither theorem supplies the missing
finite-width reference resolution or accuracy–cost evidence here. No material
is promoted, and no further GPU work remains active.
