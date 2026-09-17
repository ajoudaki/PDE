# Independent PCA benchmark arithmetic and reproduction check

Checked 2026-09-15 within the assigned continuation of this study. This is an
internal scoped audit, not an independent promotion review. Inputs are the
eight completed `pca_speed/{original,pca}_{network,closure}_r{1,2}` run
summaries/configurations and saved observations, `RUN.py`, `PCA_BATCH.py`,
`PCA_PLAN.md`, `PCA_ANALYZE.py`, its authoritative benchmark export
`pca_benchmark_analysis_003/summary.json`, and the T0–T100 observation prefixes from
`main4096/{network,closure}_1729`. No training or PCA refitting was performed.
The bounded read-only audit source is [PCA_SPEED_CHECK.py](PCA_SPEED_CHECK.py);
its full results are in
`data/generated/first_order_dimension_mnist/pca_speed_check/check.json`.
The generated `check.py` remains the exact source snapshot of the recorded
audit. The flat study source differs only in its path setup.

**PASS:** the eight run configurations, crossed GPU assignments, horizon and
step counts, dataset hashes/dimensions, recorded state-byte counts, and
within-data repeated numerical trajectories agree with the assigned design.
All saved training predictions, validation predictions, first/second activation
Grams, labels and panel inputs agree **bit for bit** across the two GPU-swapped
repetitions of each of the four models/data representations. The original
input repetition-1 trajectories also agree bit for bit with the corresponding
original T600 main run restricted to the common T0–T100 clock. Timing values
are deliberately excluded from this numerical-equality check.

All runs have nominal P=n=4096, seed 1729, float32 dynamics, TF32 disabled,
block size 2048, T=100, and eleven saved times 0,10,...,100. Network steps
are 0.25 (400 steps), closure steps 0.125 (800 steps). Closure initialization
records 2048 stored independent base marks with implicit negative partners,
with full folded dictionary dimensions 2d and d. The two configurations name
NVIDIA GeForce RTX 3090 GPUs. Repetition 1 uses network GPU0/closure GPU1;
repetition 2 uses network GPU1/closure GPU0. The batch source reverses the
original/PCA order in repetition 2. Relevant runner, engine and initializer
source hashes agree across all eight runs. Runtime environments agree except
for the GPU device index.

The original dimension is 784, archive SHA256
`bc18a91521dff93f563a3828a0ba3d941ac7f23436978db7810aeeee06ef8c7f`.
The PCA dimension is 240, archive SHA256
`420da6f2ca6fb3c6163d9d91f32ddf95b1c3258c98f5e26cea6860f43dfa1b54`.
Each metadata dimension is independently checked against the saved panel
matrix. The summaries agree exactly with their separate configuration files.

## Observed timing and allocation

Seconds below cover the fixed physical horizon T100. Each integration step is
surrounded by GPU synchronization; `integration_seconds` adds these step
times. `training_wall_seconds` additionally includes initial/intermediate
observations, validation checkpoint selection and loop overhead. Both exclude
engine initialization, loading the prepared dataset, final serialization and
test evaluation. PCA fitting/transformation is a separate CPU cost recorded
in `PCA_DATA_CHECK.md`. End-of-run cumulative integration timing equals each
summary's total exactly.

| Inputs/model | Repetition | GPU | Integration seconds | Training-loop seconds | Training peak MiB |
|---|---:|---:|---:|---:|---:|
| Original network | 1 | 0 | 63.0263 | 63.5154 | 756.9570 |
| Original network | 2 | 1 | 49.6778 | 50.1065 | 756.9570 |
| Original closure | 1 | 1 | 30.2877 | 30.5504 | 278.4189 |
| Original closure | 2 | 0 | 33.4264 | 33.6891 | 278.4189 |
| PCA network | 1 | 0 | 52.7267 | 53.1593 | 659.0703 |
| PCA network | 2 | 1 | 44.9936 | 45.3868 | 659.0703 |
| PCA closure | 1 | 1 | 12.0094 | 12.1948 | 130.5200 |
| PCA closure | 2 | 0 | 13.3029 | 13.4969 | 130.5200 |

Training peak is PyTorch `max_memory_allocated` measured after resetting its
peak immediately before training, with retained model and prepared inputs
already live. It includes live training temporaries and checkpoint copies;
it is neither the allocator's reserved memory nor whole-process GPU memory.
In all eight runs, `peak_with_controls_and_test_bytes` equals the training
peak; no larger allocation peak occurred during the subsequent recording or
test phase. The logged initialization times range from 0.3173 to 0.5859 seconds
and are not included in the displayed training ratios.

## Same-GPU ratios

Every ratio is numerator divided by denominator on the **same physical GPU
index**. Thus a value of 0.25 means one quarter of the denominator's measured
time or allocation. GPU0 pairs closure repetition 2 with network repetition
1; GPU1 pairs closure repetition 1 with network repetition 2.

| Numerator / denominator | Integration ratio GPU0 | Integration ratio GPU1 | Training-loop ratio range | Training-peak ratio |
|---|---:|---:|---:|---:|
| PCA closure / PCA network | 0.252300 | 0.266913 | 0.253895–0.268686 | 0.198037 |
| Original closure / original network | 0.530357 | 0.609683 | 0.530408–0.609709 | 0.367813 |
| PCA closure / original network | 0.211069 | 0.241746 | 0.212498–0.243378 | 0.172427 |
| PCA closure / original closure | 0.397976 | 0.396510 | 0.399170–0.400630 | 0.468790 |
| PCA network / original network | 0.836583 | 0.905709 | 0.836951–0.905808 | 0.870684 |

For this benchmark, PCA reduces closure integration time by 60.20–60.35% and
training peak by 53.12% relative to the original closure. Relative to the
original network, the PCA closure uses 21.11–24.17% of integration time and
17.24% of training peak. The corresponding PCA-network time reduction is
9.43–16.34%, with a 12.93% peak reduction.

Repeated integration times differ by 23.69% for the original network and
15.83% for the PCA network, using (maximum−minimum)/mean consistently with
`PCA_ANALYZE.py`. Both exceed the predeclared 15% flag. Original/PCA closure
differences are 9.85%/10.22%.
The report therefore preserves observed ranges; these two repetitions are
not a confidence interval or a precise universal speed factor. The runs
control GPU index in each ratio, but are sequential at different times and
do not identify a cause for timing dispersion.

## Array-count verification

For float32 network width n=4096 and input dimension d, moving state bytes
are 4(nd+n²+n), retained bytes are twice that count, and retained state plus
one best checkpoint is three times it. For folded closure N=2048, the
corresponding moving and retained counts are 4[N(d+1)+2d²] and
4[8Nd+3N+4d²], with one additional moving-state copy for the best checkpoint.
These formulas match every recorded byte count exactly.

| Inputs/model | Moving bytes | Retained bytes | Retained plus best bytes | Training-peak bytes |
|---|---:|---:|---:|---:|
| Original network | 79,970,304 | 159,940,608 | 239,910,912 | 793,726,976 |
| Original closure | 11,347,968 | 61,239,296 | 72,587,264 | 291,943,424 |
| PCA network | 71,057,408 | 142,114,816 | 213,172,224 | 691,085,312 |
| PCA closure | 2,435,072 | 16,674,816 | 19,109,888 | 136,860,160 |

These observations establish arithmetic, recorded resource use and finite
trajectory reproduction for these runs. They establish neither an
asymptotic complexity law, equivalent independent sampling at P=n, similar
classification accuracy, nor prediction agreement between distinct models
or input representations.

The independent checks take less than a second. SHA256 hashes of all eight
input summaries, configurations and observation archives, and the checker
source are retained in `pca_speed_check/check.json`.

## Analysis-export cross-check

**PASS:** all 126 checked fields in
`pca_benchmark_analysis_003/summary.json` agree with independent arithmetic:
eight benchmark rows, GPU assignments, dimensions, timings, byte-to-MiB
conversions, summary hashes, four timing/memory ranges and timing flags,
ten same-GPU speedup/memory comparisons, the copied PCA metadata, and the
analysis source hash. The source is
[PCA_SPEED_ANALYSIS_CHECK.py](PCA_SPEED_ANALYSIS_CHECK.py), and its detailed
result is `pca_speed_check/root_analysis_check.json`. The generated
`root_analysis_check.py` remains the exact source snapshot of the recorded
audit. The flat study source differs only in its path setup.

The export uses the reciprocal of the ratio convention in the preceding
table: reference time divided by candidate time, called speedup. Thus the
PCA closure is 3.7465–3.9635 times faster in integration than the PCA network,
and 4.1366–4.7378 times faster than the original network in these fixed-T100
benchmarks. Its training peak is 130.5200 MiB, versus 659.0703 MiB for the PCA
network and 756.9570 MiB for the original network. These are consistent with
the fraction-of-reference tables above.

An earlier export, `_002`, preceded additional metadata guards in the
analysis source; comparing its saved source hash to the later working file
therefore differed. `_003` records the current source hash and passes the
provenance check. This version change did not rerun training or change the
benchmarked trajectories.

The source scripts are retained flat in this study. From the repository root,
the reproduction commands are
`python studies/first_order_dimension_mnist/PCA_SPEED_CHECK.py`, followed by
`python studies/first_order_dimension_mnist/PCA_SPEED_ANALYSIS_CHECK.py`.
Both use the same recorded input/output namespace and perform read-only
checks on the benchmark inputs. Moving the maintained source into the study
folder did not rerun either audit or alter existing results.
