# Bounded SELU fitting-fix attempt (2026-09-26)

Outcome: no all-fit correction was found in the requested quick search.
All six pilots ended at their wall-time caps; none reached training RMS0.05.
No larger batch was launched after a failed pilot gate.

The unchanged stress tasks have64 training samples and8192 whole-manifold queries,
width2048,10 hidden layers,SELU,seed20260920,float32 and the existing muP mobilities.
Target training RMS was0.04; the fitted-comparison gate was0.05. Test cases were
the previously underfit full-circle/P1 and90-degree-arc/P3 closures. The first
candidate changes only Euler step and runtime. The second also changes the
initial readout law; the third changes LayerNorm placement. These are separate
retained attempts, not a single model subjected to successive modifications.

| Configuration | Full-circle P1 train RMS | Arc P3 train RMS | Cap per model |
|---|---:|---:|---:|
| Step 1/1024, original initialization and after LayerNorm | 0.98368 | 0.65459 | 60 s |
| Readout std 1, step 1/512, after LayerNorm | 0.91663 | 0.71116 | 30 s |
| LayerNorm before SELU, original initialization, step 1/128 | 0.99794 | 1.01680 | 30 s |

The original step1/128 results were also underfit. Reducing the step to1/1024
was not sufficient to deliver a quick fit. Initializing c with standard deviation1
(instead of1/n) while preserving f=c@h/n retains width-independent feature-learning
scaling but did not solve these pilots. Moving LayerNorm before SELU also failed.
These finite-duration, differently timed tests do not establish an intrinsic
positive-loss floor, nor distinguish slow dynamics from closure or integration
problems. They do not support claiming that all SELU models now fit.

No new closure-versus-dense RMS comparison is reported: the new settings did not
pass fitting, and the changed initialization/normalization would require matching
new dense reference runs. Prior fitted GELU/ReLU and failed SELU evidence remain
in their own directories. No numerical core equations or old defaults changed.

Implementation: fit_stress_tasks.py now exposes optional --readout-std and
--normalization controls; the defaults retain the previous setup. The analyzer
checks the readout initialization matches within each dense/closure comparison,
with legacy records interpreted as std(c)=1/n. The scientific core and generator
hashes match the earlier activation experiment. The driver was extended between
attempts; each result records its actual driver hash, and the current driver can
reproduce all the recorded commands with the same numerical settings.

Evidence: data/generated/neural_response_memory_20260922/compact_selu_fix01/.
Each model directory retains result.json with exact command, configuration,
source hashes,versions,GPU and timing, plus arrays.npz. pilots.csv and summary.json
summarize all six runs. All workers exited0. Independent rescoring reproduced
training and target errors within1e-12; archive checksums and exact training/query
array equality against the original SELU tasks passed for all six records.

This bounded attempt is closed without achieving the requested all-fit fix.
No further configurations or runs are queued.

User correction and supersession: moving LayerNorm was outside the intended
training-configuration scope. The subsequent original-architecture decay pilots
also failed the0.05 fitting gate (full-circle/P1:0.96424483; arc/P3:0.26210512).
Their full phase records are in compact_selu_fix01/original_decay/.
The user then directed all current work to the common implementation, with no
normalization. See CANONICAL_FLOW.md and canonical_unnormalized01/ for that setup;
no normalized or case-specific fitting prescription is adopted here.
