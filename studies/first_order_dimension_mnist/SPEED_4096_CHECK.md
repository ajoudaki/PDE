# Scoped audit: short width/particle speed and memory benchmark

The current `RUN.py` and `BATCH.py` were read completely. The timing and
memory fields support the proposed comparison without changing either
engine. No training was performed by this reviewer.

Use the same full 10,552-row MNIST training data, d784, seed1729, float32,
TF32 disabled, block2048, and T100 for both models at n=P2048 and4096.
Keep the declared steps0.25(network) and0.125(closure), with two repetitions
per configuration in fresh directories. Omit continuation and precision
probe flags. Verify final_time100, horizon stop, and respectively400/800
Heun steps. Existing `BATCH.py wider` is not this benchmark: it requests a
single4096 run through the prior T600 horizon. Use explicit fresh jobs.

**Timing interpretation.** Primary speed should be `integration_seconds/100`
(seconds per physical time), alongside total integration seconds and
milliseconds per Heun step. The closure takes twice as many steps, so
per-step speed alone does not measure this workload. GPU synchronization
brackets each timed step; measured integration includes host dispatch and
the final synchronization, but excludes observation/checkpoint work and
initialization. `training_wall_seconds` additionally includes observations,
printing, validation, and checkpoint cloning; report it separately if useful.
The outer subprocess time also includes startup, serialization, and final
evaluation and is a different quantity.

`observe(0)` warms forward evaluation, but the first RHS/Heun call is not
discarded. Call the result a whole-T100 integration measurement, not a
steady-state kernel benchmark. Two repetitions give a small repeatability
check; retain individual values and their range. Swap model-to-GPU assignment
on the second repetition and reverse width order if feasible, to reduce
physical-card and ordering confounding between the two RTX3090 devices.
Otherwise disclose the fixed assignment.

**Memory interpretation.** Use `peak_allocated_bytes`: reset occurs after
initialization, and the peak is captured before optional precision probes
and final test evaluation. It includes live model/input tensors, Heun
temporaries, observations, and the best checkpoint. It excludes freed
initialization transients and is neither reserved CUDA memory nor whole-
process/system memory. The retained-model count fairly includes the
network's initial state and the closure's fixed marks/caches; the best
checkpoint is separately counted.

Expected float32 model counts, independently calculated from array shapes:

| Nominal n=P | Network moving | Closure moving | Network retained | Closure retained |
|---:|---:|---:|---:|---:|
| 2048 | 22.1328125 MiB | 7.7558594 MiB | 44.265625 MiB | 33.890625 MiB |
| 4096 | 76.265625 MiB | 10.8222656 MiB | 152.531250 MiB | 58.402344 MiB |

Peak working allocation must be measured, not inferred from this table.
P denotes nominal sign-paired population count; stored rows are P/2. The
closure's automatic forward association changes between these two sizes:
precontracted at P2048, direct at P4096 for this full batch. Measured scaling
therefore reflects the actual implemented algorithm, not just one fixed
matrix-multiplication association.

This is a fixed numerical-workload speed/memory comparison. The inherited
steps were validated in the earlier campaign; this short benchmark does
not itself establish equal prediction accuracy or convergence at n=P4096.
Two sizes and two timing repetitions do not establish an asymptotic runtime
law. No additional accuracy claim is needed for the user's narrow request.

Reviewed hashes: RUN.py
`19c76bbb5b8ae012c13fd5c926cea0be43ab5f852fab84e35190d0001009a69e`;
BATCH.py
`fb21d7c62ce8724c9077e152830c324c19dccef00eac200eb420cfa7fc4fe248`.
The added `BATCH.py speed4096` mode was subsequently read completely. It
implements exactly eight fresh runs, reverses width order and swaps model
GPU assignment on repetition2, and omits continuation/probe flags. The
corrected `SPEED_ANALYZE.py` was also read completely; it explicitly checks
the declared settings, GPU crossover, horizons, repeat equivalence, and
retained-memory equality.

## Completed artifact verification

**PASS.** All eight finished runs reach T100 with the correct400/800 steps
and no runtime truncation. Independently checked actual frozen core-source
bytes match the unchanged current engines and dataset producer. Dataset
hashes, settings, device assignment, checkpoint array shapes/nbytes, and
analytic moving/retained-memory counts all agree. Every reported timing
row, aggregate, width factor, ratio, and CSV cell matches independent
recalculation from the run summaries. Every saved observation array is
bitwise identical between repetitions, including across the two GPUs.
No forward replay or training was needed for these computational checks.

| n=P | Network integration seconds, mean [range] | Closure integration seconds, mean [range] | Network peak | Closure peak |
|---:|---:|---:|---:|---:|
| 2048 | 17.46 [15.76,19.16] | 18.52 [17.26,19.79] | 320.16 MiB | 207.32 MiB |
| 4096 | 55.72 [49.24,62.20] | 32.84 [30.53,35.15] | 756.96 MiB | 278.42 MiB |

At4096, the closure's peak live training allocation is63.22% lower.
Comparisons on each individual GPU give network/closure integration-time
ratios1.6131 and1.7694. The ratio of means is1.6968. Both network timing
relative ranges exceed15% (19.48% at2048 and23.26% at4096), so reporting
the full ranges and observed same-GPU ratios is appropriate; no precise
universal speedup is established. Peak allocations are identical between
the two repetitions for each configuration.

Independent machine-readable evidence is retained in
`data/generated/first_order_dimension_mnist/speed4096_checks/audit.json`,
including input-summary hashes, verified core hashes, analytic counts,
repeat checks, and recomputed tables. The audited analysis source hash is
`a8c19d62d4570666eff2cc4ee0e2387a8cd5b0b7b2cd13741e8b32144fc27820`.
No unresolved comparability or arithmetic issue remains; the measurement
and accuracy qualifications above still apply.
